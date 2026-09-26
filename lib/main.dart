import 'dart:async';
import 'dart:convert';
import 'dart:math';
import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:uuid/uuid.dart';
import 'localization/app_language.dart';
import 'localization/language_controller.dart';
import 'localization/puzzle_localizer.dart';
import 'screens/auth_screen.dart';
import 'screens/language_selection_screen.dart';
import 'screens/store_screen.dart';
import 'screens/worlds_screen.dart';
import 'services/audio_service.dart';
import 'services/auth_service.dart';
import 'widgets/app_drawer.dart';
import 'widgets/level_background_builder.dart';
import 'widgets/professional_game_icons.dart';

const supabaseUrl = 'https://zahklkpxzcbfrxathphy.supabase.co';
const supabaseAnonKey = 'sb_publishable_GnKSc1T827R5ZkYDLnHpbA_KZ-9DR2F';
bool isSupabaseReady = false;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await AudioService.instance.init();
  await initializeSupabaseSafely();
  await AuthService.instance.init();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  runApp(const MindTrapApp());
}

Future<void> initializeSupabaseSafely() async {
  try {
    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseAnonKey,
    ).timeout(const Duration(seconds: 8));
    isSupabaseReady = true;
    debugPrint('Supabase init completed');
  } catch (error, stackTrace) {
    isSupabaseReady = false;
    debugPrint('Supabase init skipped: $error');
    debugPrintStack(stackTrace: stackTrace);
  }
}

SupabaseClient get supabase => Supabase.instance.client;

class GuestUserService {
  GuestUserService._();

  static const guestIdKey = 'supabase_guest_id';
  static const _uuid = Uuid();
  static bool _isEnsuringGuest = false;
  static bool _isSyncingProgress = false;
  static bool _hasFetchedInitialData = false;

  static Future<String?> get localGuestId async {
    final storage = await GameStorage.prefs;
    return storage.getString(guestIdKey);
  }

  static Future<String?> ensureGuestUser() async {
    if (!isSupabaseReady) {
      debugPrint('Supabase guest ensure skipped: client is not initialized');
      return localGuestId;
    }

    if (_isEnsuringGuest) {
      return localGuestId;
    }

    _isEnsuringGuest = true;
    try {
      final storage = await GameStorage.prefs;
      final savedGuestId = storage.getString(guestIdKey);

      if (savedGuestId == null || savedGuestId.isEmpty) {
        final guestId = await createGuestUser();
        await storage.setString(guestIdKey, guestId);
        debugPrint('Supabase guest local id saved: $guestId');
        return guestId;
      }

      debugPrint('Supabase guest local id found: $savedGuestId');
      if (!_hasFetchedInitialData) {
        _hasFetchedInitialData = true;
        final guestData = await fetchGuestData(savedGuestId);
        if (guestData != null) {
          GameStorage.applyGuestData(guestData);
        }
      }
      return savedGuestId;
    } catch (error, stackTrace) {
      debugPrint('Supabase guest ensure failed: $error');
      debugPrintStack(stackTrace: stackTrace);
      return null;
    } finally {
      _isEnsuringGuest = false;
    }
  }

  static Future<String> createGuestUser() async {
    final guestId = _uuid.v4();
    final payload = {
      'id': guestId,
      'score': 0,
      'current_streak': 0,
      'total_wins': 0,
      'daily_streak': 0,
      'achievements': <String, dynamic>{},
      'settings': {
        'sound': true,
        'music': true,
        'vibration': true,
        'daily_first_install_date': GameStorage.dailyFirstInstallDate.isEmpty
            ? GameStorage.formatStorageDate(DateTime.now())
            : GameStorage.dailyFirstInstallDate,
        'daily_completion_dates': <String, bool>{},
      },
      'created_at': DateTime.now().toUtc().toIso8601String(),
    };

    try {
      await supabase.from('guest_users').insert(payload);
      debugPrint('Supabase guest created: $guestId');
    } catch (error, stackTrace) {
      debugPrint('Supabase guest create failed: $error');
      debugPrintStack(stackTrace: stackTrace);
    }

    return guestId;
  }

  static Future<Map<String, dynamic>?> fetchGuestData([String? guestId]) async {
    if (!isSupabaseReady) {
      debugPrint('Supabase guest fetch skipped: client is not initialized');
      return null;
    }

    final id = guestId ?? await localGuestId;
    if (id == null || id.isEmpty) {
      debugPrint('Supabase guest fetch skipped: missing guest id');
      return null;
    }

    try {
      final response = await supabase
          .from('guest_users')
          .select()
          .eq('id', id)
          .maybeSingle();
      debugPrint('Supabase guest fetched: $response');

      if (response is Map<String, dynamic>) {
        return response;
      }
    } catch (error, stackTrace) {
      debugPrint('Supabase guest fetch failed: $error');
      debugPrintStack(stackTrace: stackTrace);
    }

    return null;
  }

  static Future<Map<String, dynamic>?> updateGuestProgress({
    required int score,
    required int currentStreak,
    required Map<String, dynamic> achievements,
    required Map<String, dynamic> settings,
    required int totalWins,
    required int dailyStreak,
  }) async {
    if (!isSupabaseReady) {
      debugPrint('Supabase guest update skipped: client is not initialized');
      return null;
    }

    if (_isSyncingProgress) {
      debugPrint('Supabase guest update skipped: sync already running');
      return null;
    }

    _isSyncingProgress = true;
    try {
      final guestId = await localGuestId ?? await ensureGuestUser();
      if (guestId == null || guestId.isEmpty) {
        debugPrint('Supabase guest update skipped: missing guest id');
        return null;
      }

      final payload = {
        'score': score,
        'current_streak': currentStreak,
        'total_wins': totalWins,
        'daily_streak': dailyStreak,
        'achievements': achievements,
        'settings': settings,
      };

      debugPrint('Supabase guest update payload for $guestId: $payload');

      final response = await supabase
          .from('guest_users')
          .update(payload)
          .eq('id', guestId)
          .select()
          .maybeSingle();

      debugPrint('Supabase guest progress update succeeded: $response');

      if (response is Map<String, dynamic>) {
        return response;
      }
    } catch (error, stackTrace) {
      debugPrint('Supabase guest progress update failed: $error');
      debugPrintStack(stackTrace: stackTrace);
    } finally {
      _isSyncingProgress = false;
    }

    return null;
  }
}

Future<void> testSupabaseConnection() async {
  if (!isSupabaseReady) {
    debugPrint('Supabase test skipped: client is not initialized');
    return;
  }

  try {
    final response = await Supabase.instance.client.from('test_table').select();
    // ignore: avoid_print
    print('Supabase Data: $response');
  } catch (error) {
    // ignore: avoid_print
    print('Supabase test_table query failed: $error');

    final session = Supabase.instance.client.auth.currentSession;
    // ignore: avoid_print
    print('Supabase Auth Session: $session');
  }
}

Future<void> runSupabaseConnectionTest(BuildContext context) async {
  try {
    await testSupabaseConnection();
    if (context.mounted) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(const SnackBar(content: Text('Supabase test completed')));
    }
  } catch (error, stackTrace) {
    debugPrint('Supabase test failed unexpectedly: $error');
    debugPrintStack(stackTrace: stackTrace);
  }
}

/*
Supabase examples for future online features:

await supabase.auth.signInWithPassword(email: email, password: password);

await supabase.auth.signUp(email: email, password: password);

await supabase.from('scores').insert({
  'user_id': supabase.auth.currentUser?.id,
  'score': score,
});

final leaderboard = await supabase
    .from('scores')
    .select()
    .order('score', ascending: false);
*/

final appNavigatorKey = GlobalKey<NavigatorState>();
final List<AchievementItem> _pendingAchievementPopups = [];
bool _isShowingAchievementPopup = false;
bool _isAchievementPopupRetryScheduled = false;

Route<T> smoothPageRoute<T>(Widget page) {
  return PageRouteBuilder<T>(
    transitionDuration: const Duration(milliseconds: 1050),
    reverseTransitionDuration: const Duration(milliseconds: 760),
    pageBuilder: (context, animation, secondaryAnimation) => page,
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      final curvedAnimation = CurvedAnimation(
        parent: animation,
        curve: Curves.easeOutCubic,
        reverseCurve: Curves.easeInCubic,
      );

      return FadeTransition(
        opacity: curvedAnimation,
        child: SlideTransition(
          position: Tween<Offset>(
            begin: const Offset(0, 0.1),
            end: Offset.zero,
          ).animate(curvedAnimation),
          child: ScaleTransition(
            scale: Tween<double>(begin: 0.975, end: 1).animate(curvedAnimation),
            child: child,
          ),
        ),
      );
    },
  );
}

class GameStorage {
  GameStorage._();

  static const soundKey = 'settings_sound_enabled';
  static const musicKey = 'settings_music_enabled';
  static const vibrationKey = 'settings_vibration_enabled';
  static const bestScoreKey = 'game_best_score';
  static const currentStreakKey = 'game_current_streak';
  static const bestStreakKey = 'game_best_streak';
  static const totalGamesPlayedKey = 'game_total_games_played';
  static const totalWinsKey = 'game_total_wins';
  static const totalCorrectAnswersKey = 'game_total_correct_answers';
  static const totalWrongAnswersKey = 'game_total_wrong_answers';
  static const dailyLastCompletedDateKey = 'daily_last_solved_date';
  static const dailyStreakKey = 'daily_streak';
  static const dailyAttemptedDateKey = 'daily_attempted_date';
  static const dailyAttemptedAnswerKey = 'daily_attempted_answer';
  static const dailyAttemptedCorrectKey = 'daily_attempted_correct';
  static const dailyFirstInstallDateKey = 'daily_first_install_date';
  static const dailyCompletionDatesKey = 'daily_completion_dates';
  static const dailyWeekStartKey = 'daily_week_start';
  static const dailyWeekCompletionKey = 'daily_week_completion';
  static const challengeHighestLevelKey = 'challenge_highest_level_reached';
  static const challengeLastScoreKey = 'challenge_last_score';
  static const perfectGamesKey = 'challenge_perfect_games';
  static const comebackWinsKey = 'challenge_comeback_wins';
  static const completedChallengesKey = 'challenge_completed_challenges';
  static const stageLevelStarsKey = 'stage_level_stars';
  static const storeLoginDatesKey = 'store_login_dates';
  static const dailyRewardClaimedDateKey = 'daily_reward_claimed_date';
  static const coinBalanceKey = 'store_coin_balance';
  static const gemBalanceKey = 'store_gem_balance';
  static const hintBalanceKey = 'store_hint_balance';
  static const selectedLanguageKey = 'app_selected_language_code';

  static const Map<String, int> _intDefaults = {
    bestScoreKey: 0,
    currentStreakKey: 0,
    bestStreakKey: 0,
    totalGamesPlayedKey: 0,
    totalWinsKey: 0,
    totalCorrectAnswersKey: 0,
    totalWrongAnswersKey: 0,
    dailyStreakKey: 0,
    challengeHighestLevelKey: 0,
    challengeLastScoreKey: 0,
    perfectGamesKey: 0,
    comebackWinsKey: 0,
    completedChallengesKey: 0,
    coinBalanceKey: 0,
    gemBalanceKey: 0,
    hintBalanceKey: 0,
  };
  static const Map<String, String> _stringDefaults = {
    dailyLastCompletedDateKey: '',
    dailyAttemptedDateKey: '',
    dailyAttemptedAnswerKey: '',
    dailyFirstInstallDateKey: '',
    dailyCompletionDatesKey: '',
    dailyWeekStartKey: '',
    dailyWeekCompletionKey: '',
    stageLevelStarsKey: '',
    dailyRewardClaimedDateKey: '',
    selectedLanguageKey: '',
  };
  static const Map<String, bool> _boolDefaults = {
    dailyAttemptedCorrectKey: false,
    soundKey: true,
    musicKey: true,
    vibrationKey: true,
  };

  static SharedPreferences? _prefs;
  static int bestScore = 0;
  static int currentStreak = 0;
  static int bestStreak = 0;
  static int totalGamesPlayed = 0;
  static int totalWins = 0;
  static int totalCorrectAnswers = 0;
  static int totalWrongAnswers = 0;
  static int dailyStreak = 0;
  static String dailyLastCompletedDate = '';
  static String dailyAttemptedDate = '';
  static String dailyAttemptedAnswer = '';
  static String dailyFirstInstallDate = '';
  static Map<String, bool> dailyCompletionDates = {};
  static String dailyWeekStart = '';
  static Map<String, bool> dailyWeekCompletion = defaultDailyWeekCompletion();
  static bool dailyAttemptedCorrect = false;
  static int challengeHighestLevelReached = 0;
  static int challengeLastScore = 0;
  static int perfectGames = 0;
  static int comebackWins = 0;
  static int completedChallenges = 0;
  static Map<String, int> stageLevelStars = {};
  static Set<String> storeLoginDates = {};
  static String dailyRewardClaimedDate = '';
  static String selectedLanguageCode = '';
  static int coinBalance = 0;
  static int gemBalance = 0;
  static int hintBalance = 0;
  static bool soundEnabled = true;
  static bool musicEnabled = true;
  static bool vibrationEnabled = true;
  static final Map<String, int> _achievementProgress = {};
  static final Map<String, bool> _achievementUnlocked = {};

  static Future<SharedPreferences> get prefs async {
    return _prefs ??= await SharedPreferences.getInstance();
  }

  static const List<String> dailyWeekDayKeys = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun',
  ];

  static Map<String, bool> defaultDailyWeekCompletion() {
    return {for (final day in dailyWeekDayKeys) day: false};
  }

  static String formatStorageDate(DateTime date) {
    final month = date.month.toString().padLeft(2, '0');
    final day = date.day.toString().padLeft(2, '0');
    return '${date.year}-$month-$day';
  }

  static String weekStartFor(DateTime date) {
    final monday = DateTime(
      date.year,
      date.month,
      date.day,
    ).subtract(Duration(days: date.weekday - DateTime.monday));
    return formatStorageDate(monday);
  }

  static String weekDayKeyFor(DateTime date) {
    return dailyWeekDayKeys[date.weekday - 1];
  }

  static Map<String, bool> decodeDailyWeekCompletion(String encoded) {
    if (encoded.isEmpty) {
      return defaultDailyWeekCompletion();
    }

    try {
      final decoded = jsonDecode(encoded);
      if (decoded is Map) {
        return {for (final day in dailyWeekDayKeys) day: decoded[day] == true};
      }
    } catch (error) {
      debugPrint('Daily week completion decode failed: $error');
    }

    return defaultDailyWeekCompletion();
  }

  static Map<String, bool> decodeDailyCompletionDates(String encoded) {
    if (encoded.isEmpty) {
      return {};
    }

    try {
      final decoded = jsonDecode(encoded);
      if (decoded is Map) {
        return {
          for (final entry in decoded.entries)
            if (entry.key is String && entry.value == true)
              entry.key as String: true,
        };
      }
    } catch (error) {
      debugPrint('Daily completion dates decode failed: $error');
    }

    return {};
  }

  static Map<String, int> decodeStageLevelStars(String encoded) {
    if (encoded.isEmpty) {
      return {};
    }

    try {
      final decoded = jsonDecode(encoded);
      if (decoded is Map) {
        return {
          for (final entry in decoded.entries)
            if (entry.key is String && entry.value is num)
              entry.key as String: (entry.value as num).toInt().clamp(0, 3),
        };
      }
    } catch (error) {
      debugPrint('Stage stars decode failed: $error');
    }

    return {};
  }

  static String stageLevelKey(int stageIndex, int levelIndex) {
    return '${stageIndex + 1}-${levelIndex + 1}';
  }

  static int starsForStageLevel(int stageIndex, int levelIndex) {
    return stageLevelStars[stageLevelKey(stageIndex, levelIndex)] ?? 0;
  }

  static bool isStageLevelUnlocked(int stageIndex, int levelIndex) {
    if (stageIndex == 0 && levelIndex == 0) {
      return true;
    }

    if (levelIndex > 0) {
      return starsForStageLevel(stageIndex, levelIndex - 1) > 0;
    }

    return starsForStageLevel(stageIndex - 1, 39) > 0 ||
        starsForStageLevel(stageIndex - 1, 9) > 0;
  }

  static Future<void> saveStageLevelStars({
    required int stageIndex,
    required int levelIndex,
    required int stars,
  }) async {
    final key = stageLevelKey(stageIndex, levelIndex);
    final bestStars = max(stageLevelStars[key] ?? 0, stars.clamp(0, 3).toInt());
    stageLevelStars[key] = bestStars;
    debugPrint('Stage progress saved: $key = $bestStars stars');
    await _saveAll();
  }

  static DateTime dateOnly(DateTime date) {
    return DateTime(date.year, date.month, date.day);
  }

  static DateTime? parseStorageDate(String date) {
    final parsed = DateTime.tryParse(date);
    return parsed == null ? null : dateOnly(parsed);
  }

  static void ensureDailyFirstInstallDate([DateTime? now]) {
    if (dailyFirstInstallDate.isNotEmpty) {
      return;
    }

    final installDate = dateOnly(now ?? DateTime.now());
    dailyFirstInstallDate = formatStorageDate(installDate);
    debugPrint('Daily first install date set: $dailyFirstInstallDate');
  }

  static DateTime dailyTrackerWeekStartFor([DateTime? now]) {
    ensureDailyFirstInstallDate(now);
    final today = dateOnly(now ?? DateTime.now());
    final installDate = parseStorageDate(dailyFirstInstallDate) ?? today;
    final daysSinceInstall = max(0, today.difference(installDate).inDays);
    return installDate.add(Duration(days: (daysSinceInstall ~/ 7) * 7));
  }

  static List<DailyTrackerDay> dailyTrackerDays([DateTime? now]) {
    final today = dateOnly(now ?? DateTime.now());
    final installDate =
        parseStorageDate(dailyFirstInstallDate) ?? dateOnly(today);
    final monthStart = DateTime(today.year, today.month);
    final daysInMonth = DateTime(today.year, today.month + 1, 0).day;
    final leadingEmptyDays = monthStart.weekday - DateTime.monday;
    final totalCells = ((leadingEmptyDays + daysInMonth + 6) ~/ 7) * 7;

    final days = <DailyTrackerDay>[];
    for (var index = 0; index < totalCells; index++) {
      final dayNumber = index - leadingEmptyDays + 1;
      if (dayNumber < 1 || dayNumber > daysInMonth) {
        days.add(
          DailyTrackerDay(
            date: monthStart,
            dateKey: '',
            label: '',
            status: DailyTrackerDayStatus.empty,
            isPlaceholder: true,
          ),
        );
        continue;
      }

      final date = DateTime(today.year, today.month, dayNumber);
      final dateKey = formatStorageDate(date);
      final isCompleted = dailyCompletionDates[dateKey] == true;
      final isFuture = date.isAfter(today);
      final isBeforeInstall = date.isBefore(installDate);
      final isToday = date == today;
      final status = isBeforeInstall || isFuture
          ? DailyTrackerDayStatus.empty
          : isCompleted
          ? DailyTrackerDayStatus.complete
          : isToday
          ? DailyTrackerDayStatus.today
          : DailyTrackerDayStatus.missed;

      debugPrint(
        'Daily month tracker $dateKey: status=$status completed=$isCompleted',
      );

      days.add(
        DailyTrackerDay(
          date: date,
          dateKey: dateKey,
          label: dayNumber.toString(),
          status: status,
          isPlaceholder: false,
        ),
      );
    }

    return days;
  }

  static void migrateLegacyDailyWeekCompletion() {
    if (dailyWeekStart.isEmpty) {
      return;
    }

    final weekStart = parseStorageDate(dailyWeekStart);
    if (weekStart == null) {
      return;
    }

    for (var index = 0; index < dailyWeekDayKeys.length; index++) {
      final dayKey = dailyWeekDayKeys[index];
      if (dailyWeekCompletion[dayKey] == true) {
        final dateKey = formatStorageDate(weekStart.add(Duration(days: index)));
        dailyCompletionDates[dateKey] = true;
      }
    }
  }

  static void ensureCurrentDailyWeek([DateTime? now]) {
    final today = now ?? DateTime.now();
    final currentWeekStart = weekStartFor(today);

    if (dailyWeekStart != currentWeekStart) {
      dailyWeekStart = currentWeekStart;
      dailyWeekCompletion = defaultDailyWeekCompletion();
      debugPrint('Daily week reset for new week: $dailyWeekStart');
    }
  }

  static Map<String, bool> dailyWeekCompletionForCurrentWeek() {
    ensureCurrentDailyWeek();
    debugPrint('Daily week completion map: $dailyWeekCompletion');
    return Map<String, bool>.from(dailyWeekCompletion);
  }

  static void markDailyWeekDayComplete(String date) {
    if (date.isEmpty) {
      return;
    }

    final completedDate = DateTime.tryParse(date);
    if (completedDate == null) {
      debugPrint('Daily week mark skipped for invalid date: $date');
      return;
    }

    ensureCurrentDailyWeek(completedDate);
    final dayKey = weekDayKeyFor(completedDate);
    final dateKey = formatStorageDate(completedDate);
    dailyCompletionDates[dateKey] = true;
    dailyWeekCompletion[dayKey] = true;
    debugPrint(
      'Daily marked complete: date=$dateKey day=$dayKey '
      'week=$dailyWeekCompletion dates=$dailyCompletionDates',
    );
  }

  static int savedInt(SharedPreferences storage, String key, {int? fallback}) {
    return storage.getInt(key) ?? fallback ?? _intDefaults[key] ?? 0;
  }

  static String savedString(SharedPreferences storage, String key) {
    return storage.getString(key) ?? _stringDefaults[key] ?? '';
  }

  static bool savedBool(SharedPreferences storage, String key) {
    return storage.getBool(key) ?? _boolDefaults[key] ?? false;
  }

  static Future<void> load() async {
    final storage = await prefs;
    storeLoginDates = (storage.getStringList(storeLoginDatesKey) ?? <String>[])
        .toSet();
    final todayKey = formatStorageDate(DateTime.now());
    if (storeLoginDates.add(todayKey)) {
      await storage.setStringList(
        storeLoginDatesKey,
        storeLoginDates.toList()..sort(),
      );
      debugPrint('Store daily login recorded: $todayKey');
    }
    bestScore = savedInt(storage, bestScoreKey);
    currentStreak = savedInt(storage, currentStreakKey);
    bestStreak = savedInt(storage, bestStreakKey, fallback: currentStreak);
    totalGamesPlayed = savedInt(storage, totalGamesPlayedKey);
    totalWins = savedInt(storage, totalWinsKey);
    totalCorrectAnswers = savedInt(storage, totalCorrectAnswersKey);
    totalWrongAnswers = savedInt(storage, totalWrongAnswersKey);
    dailyStreak = savedInt(storage, dailyStreakKey);
    dailyLastCompletedDate = savedString(storage, dailyLastCompletedDateKey);
    dailyAttemptedDate = savedString(storage, dailyAttemptedDateKey);
    dailyAttemptedAnswer = savedString(storage, dailyAttemptedAnswerKey);
    dailyFirstInstallDate = savedString(storage, dailyFirstInstallDateKey);
    dailyCompletionDates = decodeDailyCompletionDates(
      savedString(storage, dailyCompletionDatesKey),
    );
    dailyWeekStart = savedString(storage, dailyWeekStartKey);
    dailyWeekCompletion = decodeDailyWeekCompletion(
      savedString(storage, dailyWeekCompletionKey),
    );
    ensureDailyFirstInstallDate();
    migrateLegacyDailyWeekCompletion();
    ensureCurrentDailyWeek();
    dailyAttemptedCorrect = savedBool(storage, dailyAttemptedCorrectKey);
    challengeHighestLevelReached = savedInt(storage, challengeHighestLevelKey);
    challengeLastScore = savedInt(storage, challengeLastScoreKey);
    perfectGames = savedInt(storage, perfectGamesKey);
    comebackWins = savedInt(storage, comebackWinsKey);
    completedChallenges = savedInt(storage, completedChallengesKey);
    dailyRewardClaimedDate = savedString(storage, dailyRewardClaimedDateKey);
    selectedLanguageCode = savedString(storage, selectedLanguageKey);
    LanguageController.instance.init(selectedLanguageCode);
    LanguageController.instance.onLanguageSaved = (code) => setSelectedLanguageCode(code);
    coinBalance = savedInt(storage, coinBalanceKey);
    gemBalance = savedInt(storage, gemBalanceKey);
    hintBalance = savedInt(storage, hintBalanceKey);
    stageLevelStars = decodeStageLevelStars(
      savedString(storage, stageLevelStarsKey),
    );
    soundEnabled = savedBool(storage, soundKey);
    musicEnabled = savedBool(storage, musicKey);
    vibrationEnabled = savedBool(storage, vibrationKey);
    _loadAchievementState(storage);
    await GuestUserService.ensureGuestUser();
    await _saveAll(notifyAchievementUnlocks: false);
  }

  static Future<void> _saveAll({bool notifyAchievementUnlocks = true}) async {
    final storage = await prefs;
    await Future.wait([
      storage.setInt(bestScoreKey, bestScore),
      storage.setInt(currentStreakKey, currentStreak),
      storage.setInt(bestStreakKey, bestStreak),
      storage.setInt(totalGamesPlayedKey, totalGamesPlayed),
      storage.setInt(totalWinsKey, totalWins),
      storage.setInt(totalCorrectAnswersKey, totalCorrectAnswers),
      storage.setInt(totalWrongAnswersKey, totalWrongAnswers),
      storage.setInt(dailyStreakKey, dailyStreak),
      storage.setString(dailyLastCompletedDateKey, dailyLastCompletedDate),
      storage.setString(dailyAttemptedDateKey, dailyAttemptedDate),
      storage.setString(dailyAttemptedAnswerKey, dailyAttemptedAnswer),
      storage.setString(dailyFirstInstallDateKey, dailyFirstInstallDate),
      storage.setString(
        dailyCompletionDatesKey,
        jsonEncode(dailyCompletionDates),
      ),
      storage.setString(dailyWeekStartKey, dailyWeekStart),
      storage.setString(
        dailyWeekCompletionKey,
        jsonEncode(dailyWeekCompletion),
      ),
      storage.setBool(dailyAttemptedCorrectKey, dailyAttemptedCorrect),
      storage.setInt(challengeHighestLevelKey, challengeHighestLevelReached),
      storage.setInt(challengeLastScoreKey, challengeLastScore),
      storage.setInt(perfectGamesKey, perfectGames),
      storage.setInt(comebackWinsKey, comebackWins),
      storage.setInt(completedChallengesKey, completedChallenges),
      storage.setString(dailyRewardClaimedDateKey, dailyRewardClaimedDate),
      storage.setString(selectedLanguageKey, selectedLanguageCode),
      storage.setInt(coinBalanceKey, coinBalance),
      storage.setInt(gemBalanceKey, gemBalance),
      storage.setInt(hintBalanceKey, hintBalance),
      storage.setString(stageLevelStarsKey, jsonEncode(stageLevelStars)),
      storage.setBool(soundKey, soundEnabled),
      storage.setBool(musicKey, musicEnabled),
      storage.setBool(vibrationKey, vibrationEnabled),
    ]);
    await _saveAchievementState(notifyAchievementUnlocks);
    unawaited(syncGuestProgress());
  }

  static Future<void> syncGuestProgress() async {
    await GuestUserService.updateGuestProgress(
      score: totalCorrectAnswers * 10,
      currentStreak: currentStreak,
      totalWins: totalWins,
      dailyStreak: dailyStreak,
      achievements: achievementSnapshot(),
      settings: settingsSnapshot(),
    );
  }

  static bool get canClaimDailyReward =>
      dailyRewardClaimedDate != formatStorageDate(DateTime.now());

  static Future<bool> claimDailyReward(DailyRewardData reward) async {
    final todayKey = formatStorageDate(DateTime.now());
    final storage = await prefs;
    final savedClaimDate = storage.getString(dailyRewardClaimedDateKey) ?? '';
    if (savedClaimDate == todayKey) {
      dailyRewardClaimedDate = todayKey;
      debugPrint('Daily reward already claimed: $todayKey');
      return false;
    }

    switch (reward.type) {
      case DailyRewardType.coins:
        coinBalance += reward.quantity;
        await storage.setInt(coinBalanceKey, coinBalance);
      case DailyRewardType.gems:
        gemBalance += reward.quantity;
        await storage.setInt(gemBalanceKey, gemBalance);
      case DailyRewardType.hints:
        hintBalance += reward.quantity;
        await storage.setInt(hintBalanceKey, hintBalance);
    }

    dailyRewardClaimedDate = todayKey;
    await storage.setString(dailyRewardClaimedDateKey, todayKey);
    debugPrint(
      'Daily reward claimed: ${reward.quantity} ${reward.label} on $todayKey',
    );
    await _saveAll(notifyAchievementUnlocks: false);
    return true;
  }

  static Future<void> setSelectedLanguageCode(String code) async {
    selectedLanguageCode = code;
    final storage = await prefs;
    await storage.setString(selectedLanguageKey, code);
    await _saveAll(notifyAchievementUnlocks: false);
  }

  static Future<bool> buyHints({
    required int hintCount,
    required int price,
    required bool useGems,
  }) async {
    final storage = await prefs;
    if (useGems) {
      if (gemBalance < price) return false;
      gemBalance -= price;
      hintBalance += hintCount;
      await storage.setInt(gemBalanceKey, gemBalance);
      await storage.setInt(hintBalanceKey, hintBalance);
    } else {
      if (coinBalance < price) return false;
      coinBalance -= price;
      hintBalance += hintCount;
      await storage.setInt(coinBalanceKey, coinBalance);
      await storage.setInt(hintBalanceKey, hintBalance);
    }
    await _saveAll(notifyAchievementUnlocks: false);
    return true;
  }

  static Future<void> awardLevelDiamonds([int amount = 5]) async {
    gemBalance += amount;
    final storage = await prefs;
    await storage.setInt(gemBalanceKey, gemBalance);
    await _saveAll(notifyAchievementUnlocks: false);
    debugPrint('Level diamonds awarded: +$amount (new total: $gemBalance)');
  }

  static Future<void> awardStageCoins([int amount = 150]) async {
    coinBalance += amount;
    final storage = await prefs;
    await storage.setInt(coinBalanceKey, coinBalance);
    await _saveAll(notifyAchievementUnlocks: false);
    debugPrint('Stage coins awarded: +$amount (new total: $coinBalance)');
  }

  static Future<void> addDiamonds(int amount) async {
    gemBalance += amount;
    final storage = await prefs;
    await storage.setInt(gemBalanceKey, gemBalance);
    await _saveAll(notifyAchievementUnlocks: false);
    debugPrint('Purchased diamonds awarded: +$amount (new total: $gemBalance)');
  }

  static Future<void> addCoins(int amount) async {
    coinBalance += amount;
    final storage = await prefs;
    await storage.setInt(coinBalanceKey, coinBalance);
    await _saveAll(notifyAchievementUnlocks: false);
    debugPrint('Purchased coins awarded: +$amount (new total: $coinBalance)');
  }

  static Future<bool> useHint() async {
    if (hintBalance <= 0) return false;
    hintBalance--;
    final storage = await prefs;
    await storage.setInt(hintBalanceKey, hintBalance);
    await _saveAll(notifyAchievementUnlocks: false);
    debugPrint('Hint used. Remaining hints: $hintBalance');
    return true;
  }

  static Map<String, dynamic> achievementSnapshot() {
    return {
      'progress': Map<String, int>.from(_achievementProgress),
      'unlocked': Map<String, bool>.from(_achievementUnlocked),
    };
  }

  static Map<String, dynamic> settingsSnapshot() {
    return {
      'sound': soundEnabled,
      'music': musicEnabled,
      'vibration': vibrationEnabled,
      'daily_first_install_date': dailyFirstInstallDate,
      'daily_completion_dates': Map<String, bool>.from(dailyCompletionDates),
      'daily_week_start': dailyWeekStart,
      'daily_week_completion': Map<String, bool>.from(dailyWeekCompletion),
      'stage_level_stars': Map<String, int>.from(stageLevelStars),
    };
  }

  static void applyGuestData(Map<String, dynamic> data) {
    final remoteScore = data['score'];
    if (remoteScore is int) {
      bestScore = max(bestScore, remoteScore);
      totalCorrectAnswers = max(totalCorrectAnswers, remoteScore ~/ 10);
    }

    final remoteCurrentStreak = data['current_streak'];
    if (remoteCurrentStreak is int) {
      currentStreak = max(currentStreak, remoteCurrentStreak);
      bestStreak = max(bestStreak, currentStreak);
    }

    final remoteTotalWins = data['total_wins'];
    if (remoteTotalWins is int) {
      totalWins = max(totalWins, remoteTotalWins);
    }

    final remoteDailyStreak = data['daily_streak'];
    if (remoteDailyStreak is int) {
      dailyStreak = max(dailyStreak, remoteDailyStreak);
    }

    final remoteSettings = data['settings'];
    if (remoteSettings is Map) {
      final remoteFirstInstallDate = remoteSettings['daily_first_install_date'];
      if (remoteFirstInstallDate is String &&
          remoteFirstInstallDate.isNotEmpty &&
          (dailyFirstInstallDate.isEmpty ||
              remoteFirstInstallDate.compareTo(dailyFirstInstallDate) < 0)) {
        dailyFirstInstallDate = remoteFirstInstallDate;
      }

      final remoteCompletionDates = remoteSettings['daily_completion_dates'];
      if (remoteCompletionDates is Map) {
        for (final entry in remoteCompletionDates.entries) {
          if (entry.key is String && entry.value == true) {
            dailyCompletionDates[entry.key as String] = true;
          }
        }
      }

      final remoteStageStars = remoteSettings['stage_level_stars'];
      if (remoteStageStars is Map) {
        for (final entry in remoteStageStars.entries) {
          final value = entry.value;
          if (entry.key is String && value is num) {
            final key = entry.key as String;
            stageLevelStars[key] = max(
              stageLevelStars[key] ?? 0,
              value.toInt().clamp(0, 3).toInt(),
            );
          }
        }
      }

      final remoteWeekStart = remoteSettings['daily_week_start'];
      if (remoteWeekStart is String && remoteWeekStart.isNotEmpty) {
        dailyWeekStart = remoteWeekStart;
      }

      final remoteWeekCompletion = remoteSettings['daily_week_completion'];
      if (remoteWeekCompletion is Map) {
        dailyWeekCompletion = {
          for (final day in dailyWeekDayKeys)
            day: remoteWeekCompletion[day] == true,
        };
      }
      ensureDailyFirstInstallDate();
      migrateLegacyDailyWeekCompletion();
      ensureCurrentDailyWeek();
    }

    final remoteAchievements = data['achievements'];
    if (remoteAchievements is Map) {
      final progress = remoteAchievements['progress'];
      if (progress is Map) {
        for (final entry in progress.entries) {
          final value = entry.value;
          if (entry.key is String && value is int) {
            _achievementProgress[entry.key as String] = max(
              _achievementProgress[entry.key] ?? 0,
              value,
            );
          }
        }
      }

      final unlocked = remoteAchievements['unlocked'];
      if (unlocked is Map) {
        for (final entry in unlocked.entries) {
          if (entry.key is String && entry.value is bool) {
            _achievementUnlocked[entry.key as String] =
                (_achievementUnlocked[entry.key] ?? false) ||
                entry.value as bool;
          }
        }
      }
    }

    debugPrint('Supabase guest data applied locally: ${data['id']}');
  }

  static Future<void> saveSettings({
    bool? sound,
    bool? music,
    bool? vibration,
  }) async {
    soundEnabled = sound ?? soundEnabled;
    musicEnabled = music ?? musicEnabled;
    vibrationEnabled = vibration ?? vibrationEnabled;
    await _saveAll(notifyAchievementUnlocks: false);
    if (music != null) {
      updateBackgroundMusicSetting();
    }
  }

  static Future<void> recordAnswer({
    required bool isCorrect,
    required int score,
    required int levelReached,
  }) async {
    challengeLastScore = score;
    challengeHighestLevelReached = max(
      challengeHighestLevelReached,
      levelReached,
    );
    bestScore = max(bestScore, score);

    if (isCorrect) {
      totalCorrectAnswers++;
      currentStreak++;
      bestStreak = max(bestStreak, currentStreak);
    } else {
      totalWrongAnswers++;
      currentStreak = 0;
    }

    await _saveAll();
  }

  static Future<void> recordQuestionResult({required bool isCorrect}) async {
    await _saveAll(notifyAchievementUnlocks: false);
  }

  static Future<void> recordGameFinished({
    required bool didWin,
    required int finalScore,
    required int levelsCompleted,
    required bool wasPerfect,
    required int remainingLives,
  }) async {
    totalGamesPlayed++;
    if (didWin) {
      totalWins++;
    }
    if (wasPerfect) {
      perfectGames++;
    }
    if (didWin && remainingLives == 1) {
      comebackWins++;
    }
    completedChallenges += levelsCompleted;
    bestScore = max(bestScore, finalScore);
    challengeLastScore = finalScore;
    challengeHighestLevelReached = max(
      challengeHighestLevelReached,
      levelsCompleted,
    );
    await _saveAll();
  }

  static Future<void> saveDailyAttempt({
    required String date,
    required String answer,
    required bool isCorrect,
  }) async {
    dailyAttemptedDate = date;
    dailyAttemptedAnswer = answer;
    dailyAttemptedCorrect = isCorrect;
    await _saveAll(notifyAchievementUnlocks: false);
  }

  static Future<void> saveDailyCompletion({
    required String date,
    required int streak,
  }) async {
    dailyStreak = streak;
    dailyLastCompletedDate = date;
    markDailyWeekDayComplete(date);
    await _saveAll();
  }

  static Future<void> resetProgress() async {
    bestScore = 0;
    currentStreak = 0;
    bestStreak = 0;
    totalGamesPlayed = 0;
    totalWins = 0;
    totalCorrectAnswers = 0;
    totalWrongAnswers = 0;
    dailyStreak = 0;
    dailyLastCompletedDate = '';
    dailyAttemptedDate = '';
    dailyAttemptedAnswer = '';
    dailyFirstInstallDate = formatStorageDate(DateTime.now());
    dailyCompletionDates = {};
    dailyWeekStart = weekStartFor(DateTime.now());
    dailyWeekCompletion = defaultDailyWeekCompletion();
    dailyAttemptedCorrect = false;
    challengeHighestLevelReached = 0;
    challengeLastScore = 0;
    perfectGames = 0;
    comebackWins = 0;
    completedChallenges = 0;
    stageLevelStars = {};
    coinBalance = 0;
    gemBalance = 0;
    hintBalance = 0;
    _achievementProgress.clear();
    _achievementUnlocked.clear();
    _pendingAchievementPopups.clear();
    _isShowingAchievementPopup = false;
    _isAchievementPopupRetryScheduled = false;

    final storage = await prefs;
    final achievementKeys = storage
        .getKeys()
        .where((key) => key.startsWith('achievement_'))
        .toList(growable: false);
    await Future.wait(achievementKeys.map(storage.remove));
    await _saveAll(notifyAchievementUnlocks: false);
  }

  static String achievementKey(String id, String field) {
    return 'achievement_${id}_$field';
  }

  static int achievementProgressFor(AchievementItem item) {
    return switch (item.id) {
      'first_win' => totalWins,
      'perfect_mind' => perfectGames > 0 ? 1 : 0,
      'comeback' => comebackWins > 0 ? 1 : 0,
      'sharp_thinker' => totalCorrectAnswers,
      'trap_survivor' => totalGamesPlayed,
      'perfect_score' => perfectGames,
      'challenge_expert' => completedChallenges,
      'daily_champion' => dailyStreak,
      'streak_starter' => dailyStreak,
      'dedicated_mind' => dailyStreak,
      'streak_master' => dailyStreak,
      _ => item.current,
    };
  }

  static AchievementItem applyAchievementProgress(AchievementItem item) {
    final savedProgress = _achievementProgress[item.id];
    final derivedProgress = achievementProgressFor(item);
    final wasUnlocked = _achievementUnlocked[item.id] ?? false;
    final current = wasUnlocked
        ? max(item.target, max(savedProgress ?? 0, derivedProgress))
        : max(savedProgress ?? 0, derivedProgress);
    return item.copyWith(current: current);
  }

  static int get totalAnswers => totalCorrectAnswers + totalWrongAnswers;

  static int get accuracyPercent {
    if (totalAnswers == 0) {
      return 0;
    }
    return (totalCorrectAnswers / totalAnswers * 100).round();
  }

  static Future<void> _saveAchievementState(
    bool notifyAchievementUnlocks,
  ) async {
    final storage = await prefs;
    final writes = <Future<bool>>[];
    final achievements = allAchievements;
    final newlyUnlocked = <AchievementItem>[];

    for (final achievement in achievements) {
      final wasUnlocked = _achievementUnlocked[achievement.id] ?? false;
      if (!wasUnlocked && achievement.isCompleted) {
        newlyUnlocked.add(achievement);
      }
    }

    if (notifyAchievementUnlocks && newlyUnlocked.isNotEmpty) {
      for (final achievement in newlyUnlocked) {
        debugPrint('Unlocked achievement: ${achievement.id}');
      }
      queueAchievementUnlockPopups(newlyUnlocked);
    }

    for (final achievement in achievements) {
      _achievementProgress[achievement.id] = achievement.current;
      _achievementUnlocked[achievement.id] = achievement.isCompleted;
      writes.add(
        storage.setInt(
          achievementKey(achievement.id, 'progress'),
          achievement.current,
        ),
      );
      writes.add(
        storage.setBool(
          achievementKey(achievement.id, 'unlocked'),
          achievement.isCompleted,
        ),
      );
    }
    await Future.wait(writes);
  }

  static void _loadAchievementState(SharedPreferences storage) {
    _achievementProgress.clear();
    _achievementUnlocked.clear();
    for (final achievement in baseAchievementItems) {
      _achievementProgress[achievement.id] =
          storage.getInt(achievementKey(achievement.id, 'progress')) ?? 0;
      _achievementUnlocked[achievement.id] =
          storage.getBool(achievementKey(achievement.id, 'unlocked')) ?? false;
    }
  }
}

void playTapSound() {
  AudioService.instance.playTap(isSoundEnabled: GameStorage.soundEnabled);
}

void playCorrectSound() {
  AudioService.instance.playCorrect(isSoundEnabled: GameStorage.soundEnabled);
}

void playWrongSound() {
  AudioService.instance.playWrong(isSoundEnabled: GameStorage.soundEnabled);
}

void playWinSound() {
  AudioService.instance.playWin(isSoundEnabled: GameStorage.soundEnabled);
}

void playLoseSound() {
  AudioService.instance.playLose(isSoundEnabled: GameStorage.soundEnabled);
}

void playCoinSound() {
  AudioService.instance.playCoin(isSoundEnabled: GameStorage.soundEnabled);
}

void updateBackgroundMusicSetting() {
  if (GameStorage.musicEnabled) {
    AudioService.instance.startBackgroundMusic(isMusicEnabled: true);
  } else {
    AudioService.instance.stopBackgroundMusic();
  }
}

void triggerLightFeedback() {
  // TODO: Re-enable haptic feedback after device support is validated.
}

void triggerMediumFeedback() {
  // TODO: Re-enable haptic feedback after device support is validated.
}

void triggerHeavyFeedback() {
  // TODO: Re-enable haptic feedback after device support is validated.
}

void triggerSuccessFeedback() {
  // TODO: Re-enable success-style haptic feedback after device support is validated.
}

void triggerButtonFeedback() {
  playTapSound();
  triggerLightFeedback();
}

VoidCallback? withButtonFeedback(VoidCallback? action) {
  if (action == null) {
    return null;
  }

  return () {
    triggerButtonFeedback();
    action();
  };
}

void showGameNotification({
  required BuildContext context,
  required String message,
  IconData icon = Icons.auto_awesome_rounded,
  Color accentColor = const Color(0xFF0284C7),
  Color iconColor = const Color(0xFF38BDF8),
  Duration duration = const Duration(milliseconds: 2200),
}) {
  final messenger = ScaffoldMessenger.of(context);
  messenger.hideCurrentSnackBar();
  messenger.showSnackBar(
    SnackBar(
      behavior: SnackBarBehavior.floating,
      elevation: 0,
      backgroundColor: Colors.transparent,
      padding: EdgeInsets.zero,
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 24),
      duration: duration,
      content: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: const Color(0xFF0F172A).withAlpha(245),
          borderRadius: BorderRadius.circular(18),
          border: Border.all(
            color: accentColor.withAlpha(204),
            width: 1.5,
          ),
          boxShadow: [
            BoxShadow(
              color: accentColor.withAlpha(90),
              blurRadius: 16,
              offset: const Offset(0, 4),
            ),
            const BoxShadow(
              color: Colors.black54,
              blurRadius: 10,
              offset: Offset(0, 2),
            ),
          ],
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: accentColor.withAlpha(51),
                shape: BoxShape.circle,
              ),
              child: Icon(
                icon,
                color: iconColor,
                size: 20,
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Text(
                message,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 14,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.2,
                ),
              ),
            ),
          ],
        ),
      ),
    ),
  );
}

void queueAchievementUnlockPopups(List<AchievementItem> achievements) {
  _pendingAchievementPopups.addAll(achievements);
  _showNextAchievementUnlockPopup();
}

void _scheduleAchievementPopupRetry() {
  if (_isAchievementPopupRetryScheduled) {
    return;
  }

  _isAchievementPopupRetryScheduled = true;
  SchedulerBinding.instance.addPostFrameCallback((_) {
    _isAchievementPopupRetryScheduled = false;
    _showNextAchievementUnlockPopup();
  });
}

void _showNextAchievementUnlockPopup() {
  if (_isShowingAchievementPopup || _pendingAchievementPopups.isEmpty) {
    return;
  }

  final overlay = appNavigatorKey.currentState?.overlay;
  if (overlay == null || !overlay.mounted) {
    _scheduleAchievementPopupRetry();
    return;
  }

  final item = _pendingAchievementPopups.removeAt(0);
  late final OverlayEntry entry;
  _isShowingAchievementPopup = true;
  var hasRemoved = false;

  void dismiss() {
    if (hasRemoved) {
      return;
    }
    hasRemoved = true;
    if (entry.mounted) {
      entry.remove();
    }
    _isShowingAchievementPopup = false;
    _showNextAchievementUnlockPopup();
  }

  entry = OverlayEntry(
    builder: (context) {
      return AchievementUnlockPopup(item: item, onDismissed: dismiss);
    },
  );

  overlay.insert(entry);
}

class AchievementUnlockPopup extends StatefulWidget {
  const AchievementUnlockPopup({
    super.key,
    required this.item,
    required this.onDismissed,
  });

  final AchievementItem item;
  final VoidCallback onDismissed;

  @override
  State<AchievementUnlockPopup> createState() => _AchievementUnlockPopupState();
}

class _AchievementUnlockPopupState extends State<AchievementUnlockPopup> {
  bool isVisible = false;
  Timer? closeTimer;
  Timer? removeTimer;

  @override
  void initState() {
    super.initState();
    SchedulerBinding.instance.addPostFrameCallback((_) {
      if (mounted) {
        setState(() => isVisible = true);
      }
    });
    closeTimer = Timer(const Duration(milliseconds: 1650), () {
      if (mounted) {
        setState(() => isVisible = false);
      }
    });
    removeTimer = Timer(const Duration(seconds: 2), widget.onDismissed);
  }

  @override
  void dispose() {
    closeTimer?.cancel();
    removeTimer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: IgnorePointer(
        child: SafeArea(
          child: Align(
            alignment: Alignment.topCenter,
            child: Padding(
              padding: const EdgeInsets.fromLTRB(22, 26, 22, 0),
              child: AnimatedOpacity(
                opacity: isVisible ? 1 : 0,
                duration: const Duration(milliseconds: 360),
                curve: Curves.easeOutCubic,
                child: AnimatedScale(
                  scale: isVisible ? 1 : 0.88,
                  duration: const Duration(milliseconds: 420),
                  curve: Curves.easeOutBack,
                  child: AchievementUnlockCard(item: widget.item),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class AchievementUnlockCard extends StatelessWidget {
  const AchievementUnlockCard({super.key, required this.item});

  final AchievementItem item;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(28),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 18, sigmaY: 18),
          child: Container(
            width: min(MediaQuery.sizeOf(context).width - 44, 360),
            padding: const EdgeInsets.fromLTRB(18, 16, 18, 16),
            decoration: BoxDecoration(
              color: Colors.white.withAlpha(194),
              borderRadius: BorderRadius.circular(28),
              border: Border.all(
                color: Colors.white.withAlpha(218),
                width: 1.4,
              ),
              boxShadow: [
                BoxShadow(
                  color: item.color.withAlpha(105),
                  blurRadius: 30,
                  spreadRadius: 2,
                  offset: const Offset(0, 12),
                ),
                const BoxShadow(
                  color: Color(0x66FFFFFF),
                  blurRadius: 12,
                  offset: Offset(0, -3),
                ),
              ],
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Colors.white.withAlpha(235),
                  const Color(0xFFEFE7FF).withAlpha(218),
                  item.color.withAlpha(52),
                ],
              ),
            ),
            child: Row(
              children: [
                Container(
                  width: 74,
                  height: 74,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.white.withAlpha(190),
                    boxShadow: [
                      BoxShadow(
                        color: item.color.withAlpha(115),
                        blurRadius: 18,
                        spreadRadius: 1,
                      ),
                    ],
                  ),
                  child: Center(
                    child: AchievementVisualIcon(
                      visual: item.visual,
                      assetPath: item.assetPath,
                      size: 54,
                      color: item.color,
                    ),
                  ),
                ),
                const SizedBox(width: 15),
                Expanded(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Achievement Unlocked!',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          color: Color(0xFF0284C7),
                          fontSize: 13,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0,
                        ),
                      ),
                      const SizedBox(height: 5),
                      Text(
                        item.title,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(
                          color: Color(0xFF241873),
                          fontSize: 18,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        item.description.replaceAll('\n', ' '),
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(
                          color: Color(0xFF7562C4),
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                          height: 1.25,
                          letterSpacing: 0,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class MindTrapApp extends StatefulWidget {
  const MindTrapApp({super.key});

  @override
  State<MindTrapApp> createState() => _MindTrapAppState();
}

class _MindTrapAppState extends State<MindTrapApp> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    AudioService.instance.dispose();
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused) {
      AudioService.instance.pauseBackgroundMusic();
    } else if (state == AppLifecycleState.resumed) {
      AudioService.instance.resumeBackgroundMusic(
        isMusicEnabled: GameStorage.musicEnabled,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return MaterialApp(
          navigatorKey: appNavigatorKey,
          title: 'MindTrap AI',
          locale: Locale(langCode),
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            brightness: Brightness.dark,
            scaffoldBackgroundColor: const Color(0xFF10121A),
            fontFamily: 'Roboto',
          ),
          builder: (context, child) {
            return Directionality(
              textDirection: LanguageController.instance.directionality,
              child: child!,
            );
          },
          home: const AppStartupGate(),
        );
      },
    );
  }
}

class AppStartupGate extends StatefulWidget {
  const AppStartupGate({super.key});

  @override
  State<AppStartupGate> createState() => _AppStartupGateState();
}

class _AppStartupGateState extends State<AppStartupGate> {
  Future<void>? startupFuture;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    startupFuture ??= loadStartupDataAndMedia();
  }

  Future<void> loadStartupDataAndMedia() async {
    await GameStorage.load();
    updateBackgroundMusicSetting();
    if (!mounted) {
      return;
    }
    await preloadAppImages(context);
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<void>(
      future: startupFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState != ConnectionState.done) {
          return const PremiumLoading();
        }

        return const SplashScreen();
      },
    );
  }
}

Future<void> preloadAppImages(BuildContext context) async {
  try {
    PaintingBinding.instance.imageCache.maximumSizeBytes = 250 << 20;

    final manifest = await AssetManifest.loadFromAssetBundle(rootBundle);
    final imageAssets = manifest
        .listAssets()
        .where(
          (asset) =>
              asset.startsWith('assets/images/') &&
              (asset.endsWith('.png') ||
                  asset.endsWith('.jpg') ||
                  asset.endsWith('.jpeg') ||
                  asset.endsWith('.webp')),
        )
        .toList(growable: false);

    for (final asset in imageAssets) {
      try {
        // ignore: use_build_context_synchronously
        await precacheImage(AssetImage(asset), context);
      } catch (error, stackTrace) {
        debugPrint('Image preload skipped for $asset: $error');
        debugPrintStack(stackTrace: stackTrace);
      }
    }

    debugPrint('Preloaded ${imageAssets.length} image assets');
  } catch (error, stackTrace) {
    debugPrint('Image preload failed: $error');
    debugPrintStack(stackTrace: stackTrace);
  }
}

class PremiumLoading extends StatefulWidget {
  const PremiumLoading({super.key});

  @override
  State<PremiumLoading> createState() => _PremiumLoadingState();
}

class _PremiumLoadingState extends State<PremiumLoading> {
  @override
  Widget build(BuildContext context) {
    return const MindTrapStartupPage();
  }
}

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController controller;
  late final Animation<double> fadeAnimation;
  late final Animation<double> scaleAnimation;
  Timer? splashTimer;

  @override
  void initState() {
    super.initState();
    controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 950),
    );
    final curvedAnimation = CurvedAnimation(
      parent: controller,
      curve: Curves.easeOutCubic,
    );
    fadeAnimation = CurvedAnimation(parent: controller, curve: Curves.easeOut);
    scaleAnimation = Tween<double>(
      begin: 0.94,
      end: 1,
    ).animate(curvedAnimation);
    controller.forward();
    splashTimer = Timer(const Duration(milliseconds: 1500), openHome);
  }

  void openHome() {
    if (!mounted) {
      return;
    }

    final hasSelectedLanguage = GameStorage.selectedLanguageCode.isNotEmpty;

    Navigator.of(context).pushReplacement(
      PageRouteBuilder<void>(
        transitionDuration: const Duration(milliseconds: 720),
        pageBuilder: (context, animation, secondaryAnimation) {
          if (!hasSelectedLanguage) {
            return LanguageSelectionScreen(
              onLanguageChosen: () {
                GameStorage.setSelectedLanguageCode(
                  LanguageController.instance.currentCode,
                );
                Navigator.of(context).pushReplacement(
                  smoothPageRoute(const HomeScreen()),
                );
              },
            );
          }
          return const HomeScreen();
        },
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(
            opacity: CurvedAnimation(parent: animation, curve: Curves.easeOut),
            child: child,
          );
        },
      ),
    );
  }

  @override
  void dispose() {
    splashTimer?.cancel();
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: fadeAnimation,
      child: ScaleTransition(
        scale: scaleAnimation,
        child: const MindTrapStartupPage(),
      ),
    );
  }
}

class MindTrapStartupPage extends StatelessWidget {
  const MindTrapStartupPage({super.key});

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);
    final size = MediaQuery.sizeOf(context);
    final isShort = size.height < 700;
    final isVeryShort = size.height < 590;

    return Scaffold(
      body: Stack(
        children: [
          const Positioned.fill(
            child: Image(
              image: AssetImage(
                'assets/images/puzzle_complete_background.webp',
              ),
              fit: BoxFit.cover,
              alignment: Alignment.center,
            ),
          ),
          Positioned.fill(
            child: DecoratedBox(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    Colors.white.withAlpha(10),
                    Colors.white.withAlpha(80),
                    const Color(0x667EE7FF),
                  ],
                ),
              ),
            ),
          ),
          SafeArea(
            child: Center(
              child: SingleChildScrollView(
                padding: EdgeInsets.fromLTRB(
                  28,
                  34,
                  28,
                  28 + safePadding.bottom,
                ),
                child: ConstrainedBox(
                  constraints: BoxConstraints(
                    minHeight: max(0, size.height - safePadding.vertical - 72),
                    maxWidth: 430,
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Image(
                        image: const AssetImage('assets/images/home_logo.webp'),
                        width: isVeryShort ? 138 : (isShort ? 170 : 230),
                        height: isVeryShort ? 110 : (isShort ? 136 : 180),
                        fit: BoxFit.contain,
                      ),
                      SizedBox(height: isVeryShort ? 10 : (isShort ? 16 : 28)),
                      FittedBox(
                        fit: BoxFit.scaleDown,
                        child: RichText(
                          textAlign: TextAlign.center,
                          text: const TextSpan(
                            children: [
                              TextSpan(
                                text: 'MindTrap ',
                                style: TextStyle(
                                  color: Color(0xFF142A75),
                                  fontSize: 48,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 0,
                                ),
                              ),
                              TextSpan(
                                text: 'AI',
                                style: TextStyle(
                                  color: Color(0xFF9D3AF4),
                                  fontSize: 48,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 0,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      SizedBox(height: isVeryShort ? 14 : (isShort ? 20 : 30)),
                      Row(
                        children: [
                          Expanded(
                            child: Container(
                              height: 2,
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(999),
                                gradient: LinearGradient(
                                  colors: [
                                    Colors.transparent,
                                    const Color(0xFF5FA8F7).withAlpha(180),
                                  ],
                                ),
                              ),
                            ),
                          ),
                          const Padding(
                            padding: EdgeInsets.symmetric(horizontal: 16),
                            child: Icon(
                              Icons.auto_awesome_rounded,
                              color: Color(0xFF3D78F4),
                              size: 25,
                            ),
                          ),
                          Expanded(
                            child: Container(
                              height: 2,
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(999),
                                gradient: LinearGradient(
                                  colors: [
                                    const Color(0xFF9B7CF6).withAlpha(180),
                                    Colors.transparent,
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: isVeryShort ? 14 : (isShort ? 20 : 34)),
                      Text(
                        'Train your mind. Escape the trap.',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: const Color(0xFF3B39A9),
                          fontSize: isVeryShort ? 16 : 20,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 0,
                        ),
                      ),
                      SizedBox(height: isVeryShort ? 28 : (isShort ? 44 : 92)),
                      SizedBox(
                        width: isVeryShort ? 42 : 54,
                        height: isVeryShort ? 42 : 54,
                        child: CircularProgressIndicator(
                          strokeWidth: isVeryShort ? 4 : 5,
                          valueColor: const AlwaysStoppedAnimation<Color>(
                            Color(0xFF764CF4),
                          ),
                          backgroundColor: const Color(0x554DB9FF),
                        ),
                      ),
                      SizedBox(height: isVeryShort ? 12 : 20),
                      Text(
                        'Loading your adventure...',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: const Color(0xFF6254E8),
                          fontSize: isVeryShort ? 15 : 18,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 0,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

enum DailyRewardType { coins, gems, hints }

class DailyRewardData {
  const DailyRewardData({
    required this.type,
    required this.quantity,
    required this.assetPath,
    required this.label,
  });

  final DailyRewardType type;
  final int quantity;
  final String assetPath;
  final String label;
}

DailyRewardData dailyRewardForDate(DateTime date) {
  final day = date.day;
  if (day % 7 == 0) {
    return DailyRewardData(
      type: DailyRewardType.gems,
      quantity: 5 + ((day ~/ 7) * 5),
      assetPath: 'assets/images/gem.webp',
      label: 'Gems',
    );
  }
  if (day.isEven) {
    return DailyRewardData(
      type: DailyRewardType.hints,
      quantity: 1 + ((day ~/ 8) % 3),
      assetPath: 'assets/images/hint-icon.webp',
      label: 'Hints',
    );
  }
  return DailyRewardData(
    type: DailyRewardType.coins,
    quantity: 100 + ((day ~/ 7) * 50),
    assetPath: 'assets/images/coin.webp',
    label: 'Coins',
  );
}

class DailyRewardDialog extends StatefulWidget {
  const DailyRewardDialog({super.key, required this.reward});

  final DailyRewardData reward;

  @override
  State<DailyRewardDialog> createState() => _DailyRewardDialogState();
}

class _DailyRewardDialogState extends State<DailyRewardDialog> {
  bool isClaiming = false;

  Future<void> claimReward() async {
    if (isClaiming) {
      return;
    }
    setState(() => isClaiming = true);
    await GameStorage.claimDailyReward(widget.reward);
    playCoinSound();
    if (!mounted) {
      return;
    }
    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      insetPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
      backgroundColor: Colors.transparent,
      elevation: 0,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 390),
        child: SingleChildScrollView(
          child: Stack(
            clipBehavior: Clip.none,
            alignment: Alignment.topCenter,
            children: [
              Container(
                margin: const EdgeInsets.only(top: 48),
                padding: const EdgeInsets.fromLTRB(22, 72, 22, 24),
                decoration: BoxDecoration(
                  color: const Color(0xFFF5F5FF),
                  borderRadius: BorderRadius.circular(28),
                  border: Border.all(color: const Color(0xFFAF78FF), width: 3),
                  boxShadow: const [
                    BoxShadow(
                      color: Color(0x995C2BD5),
                      blurRadius: 24,
                      spreadRadius: 2,
                    ),
                  ],
                ),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Text(
                      'Welcome Back!',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: Color(0xFF6232D5),
                        fontSize: 28,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(height: 5),
                    const Text(
                      'Your daily reward is ready!',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: Color(0xFF394471),
                        fontSize: 15,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                    const SizedBox(height: 20),
                    Container(
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: const Color(0xFFEDE8FF),
                        border: Border.all(
                          color: const Color(0xFFB785FF),
                          width: 3,
                        ),
                        boxShadow: const [
                          BoxShadow(
                            color: Color(0x66A669FF),
                            blurRadius: 20,
                            spreadRadius: 5,
                          ),
                        ],
                      ),
                      child: Image.asset(
                        widget.reward.assetPath,
                        width: 112,
                        height: 112,
                        fit: BoxFit.contain,
                      ),
                    ),
                    Transform.translate(
                      offset: const Offset(0, -4),
                      child: Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 24,
                          vertical: 7,
                        ),
                        decoration: BoxDecoration(
                          gradient: const LinearGradient(
                            colors: [Color(0xFF9D58F2), Color(0xFF6331D8)],
                          ),
                          borderRadius: BorderRadius.circular(18),
                          border: Border.all(color: Colors.white, width: 1.5),
                        ),
                        child: Text(
                          '${widget.reward.quantity} ${widget.reward.label}',
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 12),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 16,
                        vertical: 9,
                      ),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE9E8FA),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(color: Colors.white, width: 1.5),
                      ),
                      child: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Image(
                            image: AssetImage(
                              'assets/images/daily_calendar.webp',
                            ),
                            width: 30,
                            height: 30,
                            fit: BoxFit.contain,
                          ),
                          SizedBox(width: 8),
                          Text(
                            "TODAY'S REWARD",
                            style: TextStyle(
                              color: Color(0xFF6232D5),
                              fontSize: 14,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 22),
                    Material(
                      color: Colors.transparent,
                      child: InkWell(
                        onTap: isClaiming
                            ? null
                            : withButtonFeedback(claimReward),
                        borderRadius: BorderRadius.circular(24),
                        child: Container(
                          width: double.infinity,
                          padding: const EdgeInsets.symmetric(
                            horizontal: 18,
                            vertical: 14,
                          ),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(24),
                            gradient: const LinearGradient(
                              colors: [Color(0xFF8E43F4), Color(0xFF2F74E8)],
                            ),
                            border: Border.all(
                              color: Colors.white.withAlpha(205),
                              width: 1.5,
                            ),
                            boxShadow: const [
                              BoxShadow(
                                color: Color(0x663A43E8),
                                blurRadius: 16,
                                offset: Offset(0, 8),
                              ),
                            ],
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              if (isClaiming)
                                const SizedBox(
                                  width: 26,
                                  height: 26,
                                  child: CircularProgressIndicator(
                                    strokeWidth: 3,
                                    color: Colors.white,
                                  ),
                                )
                              else
                                const Image(
                                  image: AssetImage(
                                    'assets/images/daily_gift.webp',
                                  ),
                                  width: 42,
                                  height: 42,
                                  fit: BoxFit.contain,
                                ),
                              const SizedBox(width: 10),
                              const Flexible(
                                child: Text(
                                  'CLAIM REWARD',
                                  maxLines: 1,
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 19,
                                    fontWeight: FontWeight.w900,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),
                    const Text(
                      'Come back tomorrow for another reward!',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: Color(0xFF5938C8),
                        fontSize: 13,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ],
                ),
              ),
              Positioned(
                top: 0,
                left: 2,
                right: 2,
                child: Image.asset(
                  'assets/images/daily-reward-heading.webp',
                  fit: BoxFit.contain,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    unawaited(GuestUserService.ensureGuestUser());
    updateBackgroundMusicSetting();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      unawaited(showDailyRewardPopup());
    });
  }

  Future<void> showDailyRewardPopup() async {
    if (!mounted || !GameStorage.canClaimDailyReward) {
      return;
    }

    await showDialog<void>(
      context: context,
      barrierDismissible: false,
      barrierColor: const Color(0xB30A2B62),
      builder: (context) =>
          DailyRewardDialog(reward: dailyRewardForDate(DateTime.now())),
    );
    if (mounted) setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          key: _scaffoldKey,
          drawer: AppLanguageDrawer(
            onLanguageChanged: (code) async {
              await GameStorage.setSelectedLanguageCode(code);
              if (mounted) setState(() {});
            },
            onWorldsPressed: () {
              Navigator.push(
                context,
                smoothPageRoute(
                  WorldsScreen(
                    getStarsMap: () => GameStorage.stageLevelStars,
                    onLevelSelected: (worldIndex, levelIndex) async {
                      await Navigator.push(
                        context,
                        smoothPageRoute(
                          PuzzleScreen(
                            stageIndex: worldIndex,
                            levelIndex: levelIndex,
                          ),
                        ),
                      );
                      if (mounted) setState(() {});
                    },
                  ),
                ),
              ).then((_) {
                if (mounted) setState(() {});
              });
            },
          ),
          body: LayoutBuilder(
            builder: (context, constraints) {
              final safePadding = MediaQuery.paddingOf(context);
              final isCompact = constraints.maxHeight < 700;
              final contentHeight = max(620.0, constraints.maxHeight);

              return Stack(
                children: [
                  const Positioned.fill(
                    child: Image(
                      image: AssetImage('assets/images/home_background.webp'),
                      fit: BoxFit.cover,
                      alignment: Alignment.topCenter,
                    ),
                  ),
                  SafeArea(
                    child: SingleChildScrollView(
                      padding: EdgeInsets.fromLTRB(
                        22,
                        isCompact ? 14 : 22,
                        22,
                        22 + safePadding.bottom,
                      ),
                      child: SizedBox(
                        height: contentHeight - safePadding.vertical - 22,
                        child: Stack(
                          children: [
                            Align(
                              alignment: Alignment.topCenter,
                              child: Column(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  HomeTopBar(
                                    onMenuPressed: () =>
                                        _scaffoldKey.currentState?.openDrawer(),
                                  ),
                                  SizedBox(height: isCompact ? 2 : 8),
                                  const NeonBrainLogo(),
                                  const SizedBox(height: 10),
                                  Text(
                                    tr('app_title'),
                                    textAlign: TextAlign.center,
                                    style: const TextStyle(
                                      fontSize: 30,
                                      fontWeight: FontWeight.w800,
                                      letterSpacing: 0,
                                      color: Color(0xFF10184C),
                                    ),
                                  ),
                                  const SizedBox(height: 4),
                                  const Text(
                                    'Train your mind. Escape the trap.',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 12,
                                      fontWeight: FontWeight.w600,
                                      color: Color(0xFF35406E),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            Center(
                              child: HomePlayButton(
                                onPressed: () {
                                  Navigator.push(
                                    context,
                                    smoothPageRoute(
                                      WorldsScreen(
                                        getStarsMap: () => GameStorage.stageLevelStars,
                                        onLevelSelected: (worldIndex, levelIndex) async {
                                          await Navigator.push(
                                            context,
                                            smoothPageRoute(
                                              PuzzleScreen(
                                                stageIndex: worldIndex,
                                                levelIndex: levelIndex,
                                              ),
                                            ),
                                          );
                                          if (mounted) setState(() {});
                                        },
                                      ),
                                    ),
                                  ).then((_) {
                                    if (mounted) setState(() {});
                                  });
                                },
                              ),
                            ),
                            Align(
                              alignment: Alignment.bottomCenter,
                              child: Padding(
                                padding: EdgeInsets.only(
                                  bottom: isCompact ? 20 : 28,
                                ),
                                child: HomeFeatureGrid(
                                  onDailyPressed: () {
                                    Navigator.push(
                                      context,
                                      smoothPageRoute(
                                        const DailyPuzzleLandingScreen(),
                                      ),
                                    ).then((_) {
                                      if (mounted) setState(() {});
                                    });
                                  },
                                  onStatsPressed: () {
                                    Navigator.push(
                                      context,
                                      smoothPageRoute(const StatsScreen()),
                                    ).then((_) {
                                      if (mounted) setState(() {});
                                    });
                                  },
                                  onAchievementsPressed: () {
                                    Navigator.push(
                                      context,
                                      smoothPageRoute(const AchievementsScreen()),
                                    ).then((_) {
                                      if (mounted) setState(() {});
                                    });
                                  },
                                  onStorePressed: () {
                                    Navigator.push(
                                      context,
                                      smoothPageRoute(
                                        const StoreScreen(),
                                      ),
                                    ).then((_) {
                                      if (mounted) setState(() {});
                                    });
                                  },
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ],
              );
            },
          ),
        );
      },
    );
  }
}

class HomeNeonBackground extends StatelessWidget {
  const HomeNeonBackground({super.key});

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: const BoxDecoration(color: Color(0xFF05060D)),
      child: Stack(
        children: [
          Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Color(0xFF090B19),
                  Color(0xFF0A0E24),
                  Color(0xFF05060D),
                ],
              ),
            ),
          ),
          Positioned(
            top: 88,
            left: -64,
            child: HomeGlowOrb(size: 200, color: const Color(0xAA9B2CFF)),
          ),
          Positioned(
            top: 240,
            right: -92,
            child: HomeGlowOrb(size: 260, color: const Color(0x883DD7FF)),
          ),
          Positioned(
            bottom: -72,
            left: 26,
            right: 26,
            child: Container(
              height: 190,
              decoration: const BoxDecoration(
                gradient: RadialGradient(
                  colors: [Color(0x553D35D8), Color(0x0005060D)],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class HomeGlowOrb extends StatelessWidget {
  const HomeGlowOrb({super.key, required this.size, required this.color});

  final double size;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        gradient: RadialGradient(colors: [color, const Color(0x00000000)]),
      ),
    );
  }
}

class HomeTopBar extends StatelessWidget {
  final VoidCallback? onMenuPressed;

  const HomeTopBar({super.key, this.onMenuPressed});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          children: [
            ProfessionalCircleButton(
              size: 42,
              customIcon: const ProfessionalMenuIcon(size: 21),
              tooltip: 'Menu',
              onPressed: onMenuPressed ?? () => Scaffold.maybeOf(context)?.openDrawer(),
            ),
            const SizedBox(width: 8),
            ProfessionalCircleButton(
              size: 42,
              customIcon: const ProfessionalProfileIcon(size: 23),
              tooltip: 'Profile',
              onPressed: () {
                Navigator.push(context, smoothPageRoute(const AuthScreen()));
              },
            ),
            Expanded(
              child: Center(
                child: FittedBox(
                  fit: BoxFit.scaleDown,
                  child: const HomeCurrencyRow(),
                ),
              ),
            ),
            ProfessionalCircleButton(
              size: 42,
              customIcon: const ProfessionalWorldsIcon(size: 23),
              tooltip: 'Worlds',
              hasGlow: true,
              glowColor: const Color(0x330D9488),
              onPressed: () {
                Navigator.push(
                  context,
                  smoothPageRoute(
                    WorldsScreen(
                      getStarsMap: () => GameStorage.stageLevelStars,
                    ),
                  ),
                );
              },
            ),
            const SizedBox(width: 8),
            ProfessionalCircleButton(
              size: 42,
              customIcon: const ProfessionalSettingsIcon(size: 23),
              tooltip: 'Settings',
              onPressed: () {
                Navigator.push(context, smoothPageRoute(const SettingsScreen()));
              },
            ),
          ],
        ),
        const SizedBox(height: 10),
        Row(
          children: [
            const Spacer(),
            ProfessionalGiftButton(
              onPressed: () {
                Navigator.push(
                  context,
                  smoothPageRoute(const DailyRewardScreen()),
                );
              },
            ),
          ],
        ),
      ],
    );
  }
}

class HomeCurrencyRow extends StatefulWidget {
  const HomeCurrencyRow({super.key});

  @override
  State<HomeCurrencyRow> createState() => _HomeCurrencyRowState();
}

class _HomeCurrencyRowState extends State<HomeCurrencyRow> {
  void _openStore(int tabIndex) {
    Navigator.push(
      context,
      smoothPageRoute(StoreScreen(initialTabIndex: tabIndex)),
    ).then((_) {
      if (mounted) setState(() {});
    });
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        HomeCurrencyPill(
          iconAsset: 'assets/images/coin.webp',
          value: GameStorage.coinBalance,
          onTap: () => _openStore(1),
        ),
        const SizedBox(width: 5),
        HomeCurrencyPill(
          iconAsset: 'assets/images/gem.webp',
          value: GameStorage.gemBalance,
          onTap: () => _openStore(0),
        ),
        const SizedBox(width: 5),
        HomeCurrencyPill(
          iconAsset: 'assets/images/hint-icon.webp',
          value: GameStorage.hintBalance,
          onAddPressed: () => _openStore(2),
        ),
      ],
    );
  }
}

class HomeCurrencyPill extends StatelessWidget {
  const HomeCurrencyPill({
    super.key,
    required this.iconAsset,
    required this.value,
    this.onTap,
    this.onAddPressed,
  });

  final String iconAsset;
  final int value;
  final VoidCallback? onTap;
  final VoidCallback? onAddPressed;

  @override
  Widget build(BuildContext context) {
    return ProfessionalCurrencyPill(
      iconAsset: iconAsset,
      value: value,
      onTap: onTap != null ? withButtonFeedback(onTap!) : null,
      onAddPressed: onAddPressed != null ? withButtonFeedback(onAddPressed!) : null,
    );
  }
}

class HomeCircleButton extends StatelessWidget {
  const HomeCircleButton({
    super.key,
    this.icon,
    this.iconAsset,
    this.onPressed,
    this.iconColor,
    this.isSpecialReward = false,
  }) : assert(icon != null || iconAsset != null);

  final IconData? icon;
  final String? iconAsset;
  final VoidCallback? onPressed;
  final Color? iconColor;
  final bool isSpecialReward;

  @override
  Widget build(BuildContext context) {
    if (isSpecialReward) {
      return ProfessionalGiftButton(
        onPressed: onPressed != null ? withButtonFeedback(onPressed!) : null,
      );
    }

    Widget? custom;
    if (icon == Icons.menu_rounded) {
      custom = const ProfessionalMenuIcon(size: 21);
    } else if (icon == Icons.person_rounded) {
      custom = const ProfessionalProfileIcon(size: 23);
    } else if (icon == Icons.public_rounded) {
      custom = const ProfessionalWorldsIcon(size: 23);
    } else if (icon == Icons.settings_rounded) {
      custom = const ProfessionalSettingsIcon(size: 23);
    } else if (iconAsset != null) {
      custom = Image.asset(iconAsset!, width: 22, height: 22, fit: BoxFit.contain);
    }

    return ProfessionalCircleButton(
      icon: custom == null ? icon : null,
      customIcon: custom,
      iconColor: iconColor,
      onPressed: onPressed != null ? withButtonFeedback(onPressed!) : null,
    );
  }
}

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool soundEnabled = true;
  bool musicEnabled = true;
  bool vibrationEnabled = true;
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    loadSettings();
  }

  Future<void> loadSettings() async {
    final prefs = await GameStorage.prefs;

    if (!mounted) {
      return;
    }

    setState(() {
      soundEnabled = GameStorage.savedBool(prefs, GameStorage.soundKey);
      musicEnabled = GameStorage.savedBool(prefs, GameStorage.musicKey);
      vibrationEnabled = GameStorage.savedBool(prefs, GameStorage.vibrationKey);
      isLoading = false;
    });
  }

  Future<void> updateToggle(String key, bool value) async {
    await GameStorage.saveSettings(
      sound: key == GameStorage.soundKey ? value : null,
      music: key == GameStorage.musicKey ? value : null,
      vibration: key == GameStorage.vibrationKey ? value : null,
    );
  }

  Future<void> resetProgress() async {
    final shouldReset = await showDialog<bool>(
      context: context,
      barrierColor: const Color(0x990A0D2E),
      builder: (context) {
        return const ResetProgressDialog();
      },
    );

    if (shouldReset != true) {
      return;
    }

    await GameStorage.resetProgress();

    if (!mounted) {
      return;
    }

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        behavior: SnackBarBehavior.floating,
        backgroundColor: const Color(0xFF6E35E8),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        content: const Text(
          'Progress reset',
          style: TextStyle(fontWeight: FontWeight.w800),
        ),
      ),
    );
  }

  void openAboutGame() {
    Navigator.push(context, smoothPageRoute(const AboutGameScreen()));
  }

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          body: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/home_background.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              Positioned.fill(
                child: DecoratedBox(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.black.withAlpha(50),
                        Colors.transparent,
                        Colors.black.withAlpha(140),
                      ],
                      stops: const [0.0, 0.35, 1.0],
                    ),
                  ),
                ),
              ),
          SafeArea(
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 430),
                child: SingleChildScrollView(
                  padding: EdgeInsets.fromLTRB(
                    18,
                    18,
                    18,
                    24 + safePadding.bottom,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Align(
                        alignment: Alignment.centerLeft,
                        child: SettingsBackButton(
                          onPressed: () => Navigator.of(context).maybePop(),
                        ),
                      ),
                      const SizedBox(height: 0),
                      const SettingsRibbon(),
                      const SizedBox(height: 0),
                      SettingsPanel(
                        isLoading: isLoading,
                        soundEnabled: soundEnabled,
                        musicEnabled: musicEnabled,
                        vibrationEnabled: vibrationEnabled,
                        onSoundChanged: (value) {
                          setState(() => soundEnabled = value);
                          unawaited(updateToggle(GameStorage.soundKey, value));
                        },
                        onMusicChanged: (value) {
                          setState(() => musicEnabled = value);
                          unawaited(updateToggle(GameStorage.musicKey, value));
                        },
                        onVibrationChanged: (value) {
                          setState(() => vibrationEnabled = value);
                          unawaited(
                            updateToggle(GameStorage.vibrationKey, value),
                          );
                        },
                        onResetPressed: resetProgress,
                        onAboutPressed: openAboutGame,
                        onLanguagePressed: () {
                          Navigator.push(
                            context,
                            smoothPageRoute(
                              LanguageSelectionScreen(
                                isFromSettings: true,
                                onLanguageChosen: () {
                                  GameStorage.setSelectedLanguageCode(
                                    LanguageController.instance.currentCode,
                                  );
                                  Navigator.of(context).pop();
                                  if (mounted) setState(() {});
                                },
                              ),
                            ),
                          ).then((_) {
                            if (mounted) setState(() {});
                          });
                        },
                      ),
                      const SizedBox(height: 22),
                      const SettingsThanksCard(),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
      },
    );
  }
}

class ResetProgressDialog extends StatelessWidget {
  const ResetProgressDialog({super.key});

  @override
  Widget build(BuildContext context) {
    return Dialog(
      insetPadding: const EdgeInsets.symmetric(horizontal: 28, vertical: 24),
      backgroundColor: Colors.transparent,
      elevation: 0,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 360),
        child: Stack(
          clipBehavior: Clip.none,
          alignment: Alignment.topCenter,
          children: [
            Container(
              margin: const EdgeInsets.only(top: 52),
              padding: const EdgeInsets.fromLTRB(28, 78, 28, 28),
              decoration: BoxDecoration(
                color: const Color(0xFFF8F3FF),
                borderRadius: BorderRadius.circular(28),
                border: Border.all(
                  color: Colors.white.withAlpha(225),
                  width: 2,
                ),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x665B35D0),
                    blurRadius: 24,
                    offset: Offset(0, 12),
                  ),
                  BoxShadow(
                    color: Color(0x99FFFFFF),
                    blurRadius: 16,
                    offset: Offset(0, -3),
                  ),
                ],
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text(
                    'Reset Progress?',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Color(0xFF241873),
                      fontSize: 27,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0,
                    ),
                  ),
                  const SizedBox(height: 12),
                  const Text(
                    'Are you sure?',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Color(0xFF241873),
                      fontSize: 18,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0,
                    ),
                  ),
                  const SizedBox(height: 18),
                  const Text(
                    'This action cannot be undone.\nAll your progress will be lost.',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Color(0xFF7562C4),
                      fontSize: 16,
                      fontWeight: FontWeight.w800,
                      height: 1.25,
                    ),
                  ),
                  const SizedBox(height: 34),
                  Row(
                    children: [
                      Expanded(
                        child: ResetDialogButton(
                          label: 'Cancel',
                          isPrimary: false,
                          onPressed: () => Navigator.of(context).pop(false),
                        ),
                      ),
                      const SizedBox(width: 18),
                      Expanded(
                        child: ResetDialogButton(
                          label: 'Reset',
                          isPrimary: true,
                          onPressed: () => Navigator.of(context).pop(true),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            const Positioned(top: 0, child: ResetDialogIcon()),
          ],
        ),
      ),
    );
  }
}

class ResetDialogIcon extends StatelessWidget {
  const ResetDialogIcon({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 104,
      height: 104,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        color: const Color(0xFFFDFBFF),
        border: Border.all(color: Colors.white.withAlpha(240), width: 2),
        boxShadow: const [
          BoxShadow(
            color: Color(0x4F6E35E8),
            blurRadius: 16,
            offset: Offset(0, 8),
          ),
        ],
      ),
      child: const Icon(
        Icons.restart_alt_rounded,
        size: 62,
        color: Color(0xFFFF3F78),
        shadows: [
          Shadow(color: Color(0x669A244C), blurRadius: 4, offset: Offset(0, 3)),
        ],
      ),
    );
  }
}

class ResetDialogButton extends StatelessWidget {
  const ResetDialogButton({
    super.key,
    required this.label,
    required this.isPrimary,
    required this.onPressed,
  });

  final String label;
  final bool isPrimary;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    final foreground = isPrimary ? Colors.white : const Color(0xFF4F2BD5);

    return Material(
      color: Colors.transparent,
      borderRadius: BorderRadius.circular(24),
      child: InkWell(
        onTap: withButtonFeedback(onPressed),
        borderRadius: BorderRadius.circular(24),
        child: Container(
          height: 56,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            gradient: isPrimary
                ? const LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [Color(0xFFFF5B8F), Color(0xFFF12861)],
                  )
                : const LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [Color(0xFFFFFFFF), Color(0xFFF1E9FF)],
                  ),
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: Colors.white.withAlpha(230), width: 1.4),
            boxShadow: [
              BoxShadow(
                color: isPrimary
                    ? const Color(0x66B41948)
                    : const Color(0x335B35D0),
                blurRadius: 10,
                offset: const Offset(0, 5),
              ),
            ],
          ),
          child: Text(
            label,
            style: TextStyle(
              color: foreground,
              fontSize: 17,
              fontWeight: FontWeight.w900,
              letterSpacing: 0,
            ),
          ),
        ),
      ),
    );
  }
}

class AboutGameScreen extends StatelessWidget {
  const AboutGameScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          body: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/home_background.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              Positioned.fill(
                child: DecoratedBox(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.black.withAlpha(50),
                        Colors.transparent,
                        Colors.black.withAlpha(140),
                      ],
                      stops: const [0.0, 0.35, 1.0],
                    ),
                  ),
                ),
              ),
          SafeArea(
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 430),
                child: SingleChildScrollView(
                  padding: EdgeInsets.fromLTRB(
                    18,
                    18,
                    18,
                    24 + safePadding.bottom,
                  ),
                  child: const Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Align(
                        alignment: Alignment.centerLeft,
                        child: SettingsBackButtonPlaceholder(),
                      ),
                      SizedBox(height: 0),
                      SettingsRibbon(
                        title: 'ABOUT GAME',
                        assetPath: 'assets/images/about-banner.png',
                      ),
                      SizedBox(height: 0),
                      AboutGamePanel(),
                      SizedBox(height: 22),
                      AboutThanksCard(),
                    ],
                  ),
                ),
              ),
            ),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(18, 18, 18, 0),
              child: SettingsBackButton(
                onPressed: () => Navigator.of(context).maybePop(),
              ),
            ),
          ),
        ],
      ),
    );
      },
    );
  }
}

class SettingsBackButtonPlaceholder extends StatelessWidget {
  const SettingsBackButtonPlaceholder({super.key});

  @override
  Widget build(BuildContext context) {
    return const SizedBox(width: 38, height: 38);
  }
}

class AboutGamePanel extends StatelessWidget {
  const AboutGamePanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(16, 22, 16, 16),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(170),
        borderRadius: BorderRadius.circular(34),
        border: Border.all(color: Colors.white.withAlpha(210), width: 2),
        boxShadow: const [
          BoxShadow(
            color: Color(0x385D39CA),
            blurRadius: 22,
            offset: Offset(0, 12),
          ),
          BoxShadow(
            color: Color(0x66FFFFFF),
            blurRadius: 14,
            offset: Offset(0, -3),
          ),
        ],
      ),
      child: const Column(
        children: [
          AboutDescriptionCard(),
          SizedBox(height: 12),
          AboutHowToPlayCard(),
          SizedBox(height: 12),
          AboutInfoRow(
            iconAssetPath: 'assets/images/version.png',
            label: 'VERSION',
            value: '1.0.0',
          ),
          SizedBox(height: 10),
          AboutInfoRow(
            iconAssetPath: 'assets/images/creator.png',
            label: 'CREATOR',
            value: 'Puzzle Studio',
          ),
          SizedBox(height: 10),
          AboutInfoRow(
            iconAssetPath: 'assets/images/company.png',
            label: 'COMPANY',
            value: 'Dreamy Games',
          ),
        ],
      ),
    );
  }
}

class AboutDescriptionCard extends StatelessWidget {
  const AboutDescriptionCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 18, 16, 18),
      decoration: aboutCardDecoration,
      child: const Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AboutSectionTitle(
            iconAssetPath: 'assets/images/Golden_Star_Icon.png',
            title: 'GAME DESCRIPTION',
          ),
          SizedBox(height: 18),
          Text(
            'Welcome to our magical world! Solve fun puzzles, complete exciting levels, and embark on a beautiful adventure filled with challenges and surprises!',
            style: TextStyle(
              color: Color(0xFF1A176A),
              fontSize: 14,
              fontWeight: FontWeight.w700,
              height: 1.55,
            ),
          ),
        ],
      ),
    );
  }
}

class AboutHowToPlayCard extends StatelessWidget {
  const AboutHowToPlayCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 18, 16, 18),
      decoration: aboutCardDecoration,
      child: const Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AboutSectionTitle(
            iconAssetPath: 'assets/images/how-to-play.png',
            title: 'HOW TO PLAY',
          ),
          SizedBox(height: 18),
          AboutPlayStep(
            iconAssetPath: 'assets/images/match-3.png',
            text: 'Match 3 or more items to clear them.',
          ),
          AboutDivider(),
          AboutPlayStep(
            iconAssetPath: 'assets/images/complete-level.png',
            text: 'Complete level goals to earn stars.',
          ),
          AboutDivider(),
          AboutPlayStep(
            iconAssetPath: 'assets/images/use-booster.png',
            text: 'Use boosters to help you pass difficult levels.',
          ),
          AboutDivider(),
          AboutPlayStep(
            iconAssetPath: 'assets/images/keep-playing.png',
            text: 'Keep playing and unlock new challenges and rewards!',
          ),
        ],
      ),
    );
  }
}

BoxDecoration get aboutCardDecoration {
  return BoxDecoration(
    color: Colors.white.withAlpha(190),
    borderRadius: BorderRadius.circular(24),
    border: Border.all(color: Colors.white.withAlpha(210), width: 1.2),
    boxShadow: const [
      BoxShadow(color: Color(0x1F3D2491), blurRadius: 12, offset: Offset(0, 6)),
      BoxShadow(color: Color(0x55FFFFFF), blurRadius: 8, offset: Offset(0, -2)),
    ],
  );
}

class AboutSectionTitle extends StatelessWidget {
  const AboutSectionTitle({
    super.key,
    required this.iconAssetPath,
    required this.title,
  });

  final String iconAssetPath;
  final String title;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        AboutAssetIcon(assetPath: iconAssetPath, size: 34),
        const SizedBox(width: 12),
        Expanded(
          child: Text(
            title,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(
              color: Color(0xFF4323C8),
              fontSize: 18,
              fontWeight: FontWeight.w900,
              letterSpacing: 0,
            ),
          ),
        ),
      ],
    );
  }
}

class AboutAssetIcon extends StatelessWidget {
  const AboutAssetIcon({
    super.key,
    required this.assetPath,
    required this.size,
  });

  final String assetPath;
  final double size;

  @override
  Widget build(BuildContext context) {
    return Image.asset(
      assetPath,
      width: size,
      height: size,
      fit: BoxFit.contain,
    );
  }
}

class AboutPlayStep extends StatelessWidget {
  const AboutPlayStep({
    super.key,
    required this.iconAssetPath,
    required this.text,
  });

  final String iconAssetPath;
  final String text;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        SizedBox(
          width: 38,
          height: 38,
          child: Image.asset(iconAssetPath, fit: BoxFit.contain),
        ),
        const SizedBox(width: 14),
        Expanded(
          child: Text(
            text,
            style: const TextStyle(
              color: Color(0xFF1A176A),
              fontSize: 13,
              fontWeight: FontWeight.w700,
              height: 1.28,
            ),
          ),
        ),
      ],
    );
  }
}

class AboutDivider extends StatelessWidget {
  const AboutDivider({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 1,
      margin: const EdgeInsets.fromLTRB(52, 10, 0, 10),
      color: const Color(0xFFD8CCF2),
    );
  }
}

class AboutShopIllustration extends StatelessWidget {
  const AboutShopIllustration({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 150,
      child: Stack(
        alignment: Alignment.bottomCenter,
        children: [
          Positioned(
            bottom: 6,
            child: Container(
              width: 116,
              height: 92,
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [Color(0xFF9E61FF), Color(0xFF7440DE)],
                ),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: const Color(0xFF5F2DD5), width: 2),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x55321698),
                    blurRadius: 10,
                    offset: Offset(0, 6),
                  ),
                ],
              ),
            ),
          ),
          Positioned(
            top: 36,
            child: Container(
              width: 132,
              height: 34,
              decoration: BoxDecoration(
                color: const Color(0xFFCFA8FF),
                borderRadius: BorderRadius.circular(8),
              ),
            ),
          ),
          Positioned(
            top: 46,
            child: Row(
              children: [
                for (var index = 0; index < 5; index++)
                  Container(
                    width: 24,
                    height: 34,
                    decoration: BoxDecoration(
                      color: index.isEven
                          ? const Color(0xFF7B45EA)
                          : const Color(0xFFFFF2FF),
                      borderRadius: const BorderRadius.vertical(
                        bottom: Radius.circular(10),
                      ),
                    ),
                  ),
              ],
            ),
          ),
          Positioned(
            top: 6,
            child: Container(
              width: 56,
              height: 56,
              decoration: const BoxDecoration(
                shape: BoxShape.circle,
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [Color(0xFFA77BFF), Color(0xFF5F32E7)],
                ),
              ),
              child: const Icon(
                Icons.star_rounded,
                color: Colors.white,
                size: 34,
              ),
            ),
          ),
          Positioned(
            left: 20,
            bottom: 6,
            child: Container(
              width: 36,
              height: 66,
              decoration: BoxDecoration(
                color: const Color(0xFF6F35D8),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: const Color(0xFF4F24B6), width: 2),
              ),
              child: const Center(
                child: Text(
                  'STORE',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 8,
                    fontWeight: FontWeight.w900,
                  ),
                ),
              ),
            ),
          ),
          Positioned(
            right: 20,
            bottom: 42,
            child: Container(
              width: 48,
              height: 52,
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF37B8FF), Color(0xFF1675E9)],
                ),
                borderRadius: BorderRadius.circular(6),
                border: Border.all(color: const Color(0xFF3D25B7), width: 2),
              ),
            ),
          ),
          const Positioned(
            left: 0,
            bottom: 4,
            child: Icon(
              Icons.shopping_bag_rounded,
              color: Color(0xFFE84A70),
              size: 42,
            ),
          ),
          const Positioned(
            right: -4,
            bottom: 4,
            child: Icon(
              Icons.shopping_cart_rounded,
              color: Color(0xFF2F87F2),
              size: 42,
            ),
          ),
        ],
      ),
    );
  }
}

class AboutRewardsIllustration extends StatelessWidget {
  const AboutRewardsIllustration({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 164,
      child: Stack(
        alignment: Alignment.center,
        children: const [
          Icon(
            Icons.favorite_rounded,
            color: Color(0xFFE84A70),
            size: 86,
            shadows: [
              Shadow(
                color: Color(0x66A3214C),
                blurRadius: 10,
                offset: Offset(0, 6),
              ),
            ],
          ),
          Positioned(
            right: 18,
            top: 28,
            child: Icon(
              Icons.star_rounded,
              color: Color(0xFFFFC930),
              size: 92,
              shadows: [
                Shadow(
                  color: Color(0x66965C00),
                  blurRadius: 8,
                  offset: Offset(0, 5),
                ),
              ],
            ),
          ),
          Positioned(
            bottom: 14,
            right: 48,
            child: Icon(
              Icons.crop_square_rounded,
              color: Color(0xFF2F9DF2),
              size: 76,
              shadows: [
                Shadow(
                  color: Color(0x66325DA5),
                  blurRadius: 8,
                  offset: Offset(0, 5),
                ),
              ],
            ),
          ),
          Positioned(
            left: 16,
            bottom: 18,
            child: Icon(
              Icons.auto_awesome_rounded,
              color: Color(0xFFD85DFF),
              size: 22,
            ),
          ),
          Positioned(
            right: 0,
            bottom: 36,
            child: Icon(
              Icons.auto_awesome_rounded,
              color: Color(0xFFD85DFF),
              size: 18,
            ),
          ),
          Positioned(
            right: 20,
            top: 14,
            child: Icon(
              Icons.auto_awesome_rounded,
              color: Color(0xFFFFD966),
              size: 18,
            ),
          ),
        ],
      ),
    );
  }
}

class AboutInfoRow extends StatelessWidget {
  const AboutInfoRow({
    super.key,
    this.icon,
    this.iconAssetPath,
    required this.label,
    required this.value,
  });

  final IconData? icon;
  final String? iconAssetPath;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      constraints: const BoxConstraints(minHeight: 58),
      padding: const EdgeInsets.fromLTRB(14, 10, 18, 10),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(185),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withAlpha(205), width: 1.2),
        boxShadow: const [
          BoxShadow(
            color: Color(0x18000000),
            blurRadius: 9,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          SizedBox(
            width: 40,
            height: 40,
            child: iconAssetPath == null
                ? Icon(icon, color: const Color(0xFF0284C7), size: 30)
                : Image.asset(iconAssetPath!, fit: BoxFit.contain),
          ),
          const SizedBox(width: 18),
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                color: Color(0xFF0284C7),
                fontSize: 17,
                fontWeight: FontWeight.w900,
                letterSpacing: 0,
              ),
            ),
          ),
          const SizedBox(width: 12),
          Text(
            value,
            textAlign: TextAlign.right,
            style: const TextStyle(
              color: Color(0xFF241873),
              fontSize: 16,
              fontWeight: FontWeight.w700,
            ),
          ),
        ],
      ),
    );
  }
}

class AboutThanksCard extends StatelessWidget {
  const AboutThanksCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        constraints: const BoxConstraints(maxWidth: 328),
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 16),
        decoration: BoxDecoration(
          color: Colors.white.withAlpha(220),
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: Colors.white.withAlpha(205), width: 1.2),
          boxShadow: const [
            BoxShadow(
              color: Color(0x365D39CA),
              blurRadius: 18,
              offset: Offset(0, 8),
            ),
          ],
        ),
        child: Row(
          children: const [
            Image(
              image: AssetImage('assets/images/Bottom_Heart_Icon.png'),
              width: 50,
              height: 50,
              fit: BoxFit.contain,
            ),
            SizedBox(width: 16),
            Expanded(
              child: Text(
                'Thank you for playing!\nWe hope you enjoy the game as much as we enjoyed creating it for you.',
                style: TextStyle(
                  color: Color(0xFF241873),
                  fontSize: 14,
                  fontWeight: FontWeight.w800,
                  height: 1.35,
                ),
              ),
            ),
            SizedBox(width: 8),
            Image(
              image: AssetImage('assets/images/thank-you.png'),
              width: 32,
              height: 32,
              fit: BoxFit.contain,
            ),
          ],
        ),
      ),
    );
  }
}

class SettingsBackButton extends StatelessWidget {
  const SettingsBackButton({
    super.key,
    required this.onPressed,
    this.icon = Icons.arrow_back_rounded,
  });

  final VoidCallback onPressed;
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: withButtonFeedback(onPressed),
        child: Container(
          width: 38,
          height: 38,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            gradient: const LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Color(0xFFA77BFF), Color(0xFF5F32E7)],
            ),
            border: Border.all(color: Colors.white.withAlpha(175), width: 1.4),
            boxShadow: const [
              BoxShadow(
                color: Color(0x665A25D8),
                blurRadius: 8,
                offset: Offset(0, 4),
              ),
              BoxShadow(
                color: Color(0x55FFFFFF),
                blurRadius: 5,
                offset: Offset(-1, -1),
              ),
            ],
          ),
          child: Icon(
            icon,
            color: Colors.white,
            size: 23,
            shadows: const [
              Shadow(
                color: Color(0x77321698),
                blurRadius: 4,
                offset: Offset(0, 1),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsRibbon extends StatelessWidget {
  const SettingsRibbon({
    super.key,
    this.title = 'SETTINGS',
    this.assetPath = 'assets/images/setting-banner.png',
  });

  final String title;
  final String assetPath;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 94,
      child: Image.asset(assetPath, fit: BoxFit.contain, semanticLabel: title),
    );
  }
}

class SettingsRibbonTail extends StatelessWidget {
  const SettingsRibbonTail({super.key, this.isRight = false});

  final bool isRight;

  @override
  Widget build(BuildContext context) {
    return Transform.scale(
      scaleX: isRight ? -1 : 1,
      child: ClipPath(
        clipper: SettingsTailClipper(),
        child: Container(
          width: 100,
          height: 58,
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Color(0xFF8D47F2), Color(0xFF5C2BD5)],
            ),
            boxShadow: const [
              BoxShadow(
                color: Color(0x664018A5),
                blurRadius: 8,
                offset: Offset(0, 5),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsTailClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    return Path()
      ..moveTo(0, size.height * 0.2)
      ..lineTo(size.width * 0.78, 0)
      ..lineTo(size.width, size.height * 0.5)
      ..lineTo(size.width * 0.78, size.height)
      ..lineTo(0, size.height * 0.82)
      ..quadraticBezierTo(
        size.width * 0.12,
        size.height * 0.5,
        0,
        size.height * 0.2,
      )
      ..close();
  }

  @override
  bool shouldReclip(covariant CustomClipper<Path> oldClipper) => false;
}

class SettingsStar extends StatelessWidget {
  const SettingsStar({super.key});

  @override
  Widget build(BuildContext context) {
    return const Icon(
      Icons.star_rounded,
      size: 35,
      color: Color(0xFFFFC930),
      shadows: [
        Shadow(color: Color(0x998F4A00), blurRadius: 4, offset: Offset(0, 3)),
      ],
    );
  }
}

class SettingsPanel extends StatelessWidget {
  const SettingsPanel({
    super.key,
    required this.isLoading,
    required this.soundEnabled,
    required this.musicEnabled,
    required this.vibrationEnabled,
    required this.onSoundChanged,
    required this.onMusicChanged,
    required this.onVibrationChanged,
    required this.onResetPressed,
    required this.onAboutPressed,
    this.onLanguagePressed,
  });

  final bool isLoading;
  final bool soundEnabled;
  final bool musicEnabled;
  final bool vibrationEnabled;
  final ValueChanged<bool> onSoundChanged;
  final ValueChanged<bool> onMusicChanged;
  final ValueChanged<bool> onVibrationChanged;
  final VoidCallback onResetPressed;
  final VoidCallback onAboutPressed;
  final VoidCallback? onLanguagePressed;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 22, 18, 18),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(170),
        borderRadius: BorderRadius.circular(34),
        border: Border.all(color: Colors.white.withAlpha(210), width: 2),
        boxShadow: const [
          BoxShadow(
            color: Color(0x18000000),
            blurRadius: 22,
            offset: Offset(0, 12),
          ),
          BoxShadow(
            color: Color(0x66FFFFFF),
            blurRadius: 14,
            offset: Offset(0, -3),
          ),
        ],
      ),
      child: Column(
        children: [
          ValueListenableBuilder<bool>(
            valueListenable: AuthService.instance.isLoggedIn,
            builder: (context, loggedIn, _) {
              return SettingsRow(
                icon: Icons.person_rounded,
                iconColor: loggedIn ? const Color(0xFF10B981) : const Color(0xFF0284C7),
                label: tr('profile'),
                subtitle: loggedIn ? AuthService.instance.userName.value : tr('guest_player'),
                onPressed: () {
                  Navigator.push(context, smoothPageRoute(const AuthScreen()));
                },
                trailing: const Icon(
                  Icons.chevron_right_rounded,
                  color: Color(0xFF0284C7),
                  size: 38,
                ),
              );
            },
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.language_rounded,
            iconColor: const Color(0xFF0284C7),
            label: tr('language'),
            subtitle: '${LanguageController.instance.currentLanguage.flagEmoji} ${LanguageController.instance.currentLanguage.nativeName}',
            onPressed: onLanguagePressed,
            trailing: const Icon(
              Icons.chevron_right_rounded,
              color: Color(0xFF0284C7),
              size: 38,
            ),
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.volume_up_rounded,
            iconColor: const Color(0xFF0284C7),
            label: tr('sound'),
            trailing: SettingsSwitch(
              value: soundEnabled,
              onChanged: isLoading ? null : onSoundChanged,
            ),
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.music_note_rounded,
            iconColor: const Color(0xFFE84A70),
            label: tr('music'),
            trailing: SettingsSwitch(
              value: musicEnabled,
              onChanged: isLoading ? null : onMusicChanged,
            ),
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.vibration_rounded,
            iconColor: const Color(0xFF2F87F2),
            label: tr('vibration'),
            subtitle: 'Device support may vary',
            trailing: SettingsSwitch(
              value: vibrationEnabled,
              onChanged: isLoading ? null : onVibrationChanged,
            ),
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.restart_alt_rounded,
            iconColor: const Color(0xFFE84A70),
            label: tr('reset_progress'),
            onPressed: onResetPressed,
            trailing: const Icon(
              Icons.chevron_right_rounded,
              color: Color(0xFF0284C7),
              size: 38,
              shadows: [
                Shadow(
                  color: Color(0x330284C7),
                  blurRadius: 5,
                  offset: Offset(0, 2),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SettingsRow(
            icon: Icons.info_rounded,
            iconColor: const Color(0xFF0284C7),
            label: tr('about_game'),
            onPressed: onAboutPressed,
            trailing: const Icon(
              Icons.chevron_right_rounded,
              color: Color(0xFF0284C7),
              size: 38,
              shadows: [
                Shadow(
                  color: Color(0x330284C7),
                  blurRadius: 5,
                  offset: Offset(0, 2),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          const SettingsRow(
            icon: Icons.verified_user_rounded,
            iconColor: Color(0xFF2F87F2),
            label: 'Version',
            trailing: SettingsVersionPill(),
          ),
        ],
      ),
    );
  }
}

class SettingsRow extends StatelessWidget {
  const SettingsRow({
    super.key,
    required this.icon,
    required this.iconColor,
    required this.label,
    required this.trailing,
    this.subtitle,
    this.onPressed,
  });

  final IconData icon;
  final Color iconColor;
  final String label;
  final String? subtitle;
  final Widget trailing;
  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: withButtonFeedback(onPressed),
        borderRadius: BorderRadius.circular(22),
        child: Container(
          constraints: const BoxConstraints(minHeight: 82),
          padding: const EdgeInsets.fromLTRB(14, 12, 16, 12),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(185),
            borderRadius: BorderRadius.circular(22),
            border: Border.all(color: Colors.white.withAlpha(205), width: 1.3),
            boxShadow: const [
              BoxShadow(
                color: Color(0x1A3D2491),
                blurRadius: 12,
                offset: Offset(0, 5),
              ),
              BoxShadow(
                color: Color(0x55FFFFFF),
                blurRadius: 10,
                offset: Offset(0, -2),
              ),
            ],
          ),
          child: Row(
            children: [
              SettingsIconTile(icon: icon, color: iconColor),
              const SizedBox(width: 18),
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      label,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Color(0xFF241873),
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        letterSpacing: 0,
                      ),
                    ),
                    if (subtitle != null) ...[
                      const SizedBox(height: 3),
                      Text(
                        subtitle!,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(
                          color: Color(0xFF7562C4),
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 0,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
              const SizedBox(width: 12),
              trailing,
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsIconTile extends StatelessWidget {
  const SettingsIconTile({super.key, required this.icon, required this.color});

  final IconData icon;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 58,
      height: 58,
      decoration: BoxDecoration(
        color: const Color(0xFFF8F3FF),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withAlpha(220), width: 1.2),
        boxShadow: const [
          BoxShadow(
            color: Color(0x183D2491),
            blurRadius: 9,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Icon(
        icon,
        color: color,
        size: 34,
        shadows: [
          Shadow(
            color: color.withAlpha(88),
            blurRadius: 6,
            offset: const Offset(0, 3),
          ),
        ],
      ),
    );
  }
}

class SettingsSwitch extends StatelessWidget {
  const SettingsSwitch({
    super.key,
    required this.value,
    required this.onChanged,
  });

  final bool value;
  final ValueChanged<bool>? onChanged;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      toggled: value,
      button: true,
      child: GestureDetector(
        onTap: onChanged == null
            ? null
            : () {
                triggerButtonFeedback();
                onChanged!(!value);
              },
        child: AnimatedContainer(
          width: 68,
          height: 34,
          duration: const Duration(milliseconds: 220),
          curve: Curves.easeOutCubic,
          padding: const EdgeInsets.all(4),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(999),
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: value
                  ? const [Color(0xFF8B54FF), Color(0xFF5F2FE2)]
                  : const [Color(0xFFC7BCD9), Color(0xFF9A8BB9)],
            ),
            boxShadow: const [
              BoxShadow(
                color: Color(0x5533158E),
                blurRadius: 8,
                offset: Offset(0, 4),
              ),
              BoxShadow(
                color: Color(0x55FFFFFF),
                blurRadius: 5,
                offset: Offset(0, -1),
              ),
            ],
          ),
          child: Stack(
            children: [
              Align(
                alignment: value ? Alignment.centerLeft : Alignment.centerRight,
                child: Padding(
                  padding: EdgeInsets.only(
                    left: value ? 9 : 0,
                    right: value ? 0 : 8,
                  ),
                  child: Text(
                    value ? 'ON' : 'OFF',
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 12,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0,
                      shadows: [
                        Shadow(
                          color: Color(0x66321698),
                          blurRadius: 4,
                          offset: Offset(0, 2),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
              AnimatedAlign(
                alignment: value ? Alignment.centerRight : Alignment.centerLeft,
                duration: const Duration(milliseconds: 220),
                curve: Curves.easeOutCubic,
                child: Container(
                  width: 26,
                  height: 20,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Color(0xFFF9F6FF),
                    boxShadow: [
                      BoxShadow(
                        color: Color(0x55321698),
                        blurRadius: 5,
                        offset: Offset(0, 2),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsVersionPill extends StatelessWidget {
  const SettingsVersionPill({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      constraints: const BoxConstraints(minWidth: 92),
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 9),
      decoration: BoxDecoration(
        color: const Color(0xFFE6D8FF),
        borderRadius: BorderRadius.circular(999),
        border: Border.all(color: Colors.white.withAlpha(150)),
      ),
      child: const Text(
        '1.0.0',
        textAlign: TextAlign.center,
        style: TextStyle(
          color: Color(0xFF241873),
          fontSize: 17,
          fontWeight: FontWeight.w900,
        ),
      ),
    );
  }
}

class SettingsThanksCard extends StatelessWidget {
  const SettingsThanksCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        constraints: const BoxConstraints(maxWidth: 328),
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 16),
        decoration: BoxDecoration(
          color: Colors.white.withAlpha(220),
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: Colors.white.withAlpha(205), width: 1.2),
          boxShadow: const [
            BoxShadow(
              color: Color(0x365D39CA),
              blurRadius: 18,
              offset: Offset(0, 8),
            ),
          ],
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: const [
            Icon(
              Icons.favorite_rounded,
              size: 48,
              color: Color(0xFFE84A70),
              shadows: [
                Shadow(
                  color: Color(0x66A3214C),
                  blurRadius: 6,
                  offset: Offset(0, 4),
                ),
              ],
            ),
            SizedBox(width: 16),
            Flexible(
              child: Text(
                'Thanks for being part of our journey!\nYour support means the world to us.',
                style: TextStyle(
                  color: Color(0xFF241873),
                  fontSize: 14,
                  fontWeight: FontWeight.w800,
                  height: 1.35,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class NeonBrainLogo extends StatelessWidget {
  const NeonBrainLogo({super.key});

  @override
  Widget build(BuildContext context) {
    return const Image(
      image: AssetImage('assets/images/home_logo.webp'),
      width: 112,
      height: 88,
      fit: BoxFit.contain,
    );
  }
}

class NeonBrainPainter extends CustomPainter {
  const NeonBrainPainter();

  @override
  void paint(Canvas canvas, Size size) {
    final leftColor = const Color(0xFF12E7FF);
    final rightColor = const Color(0xFFFF2DE2);
    final strokeWidth = size.width * 0.06;
    final centerX = size.width / 2;

    Paint glowPaint(Color color, double width) {
      return Paint()
        ..color = color.withAlpha(115)
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round
        ..strokeWidth = width
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 8);
    }

    Paint linePaint(Color color, double width) {
      return Paint()
        ..color = color
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round
        ..strokeWidth = width;
    }

    final leftOutline = Path()
      ..moveTo(centerX - 2, size.height * 0.13)
      ..cubicTo(
        size.width * 0.23,
        size.height * 0.06,
        size.width * 0.08,
        size.height * 0.23,
        size.width * 0.16,
        size.height * 0.37,
      )
      ..cubicTo(
        size.width * 0.02,
        size.height * 0.47,
        size.width * 0.09,
        size.height * 0.69,
        size.width * 0.25,
        size.height * 0.68,
      )
      ..cubicTo(
        size.width * 0.26,
        size.height * 0.86,
        size.width * 0.49,
        size.height * 0.88,
        centerX - 2,
        size.height * 0.72,
      )
      ..lineTo(centerX - 2, size.height * 0.13);

    final rightOutline = Path()
      ..moveTo(centerX + 2, size.height * 0.13)
      ..cubicTo(
        size.width * 0.77,
        size.height * 0.06,
        size.width * 0.92,
        size.height * 0.23,
        size.width * 0.84,
        size.height * 0.37,
      )
      ..cubicTo(
        size.width * 0.98,
        size.height * 0.47,
        size.width * 0.91,
        size.height * 0.69,
        size.width * 0.75,
        size.height * 0.68,
      )
      ..cubicTo(
        size.width * 0.74,
        size.height * 0.86,
        size.width * 0.51,
        size.height * 0.88,
        centerX + 2,
        size.height * 0.72,
      )
      ..lineTo(centerX + 2, size.height * 0.13);

    final leftFolds = [
      Path()
        ..moveTo(size.width * 0.25, size.height * 0.25)
        ..cubicTo(
          size.width * 0.34,
          size.height * 0.19,
          size.width * 0.4,
          size.height * 0.27,
          size.width * 0.36,
          size.height * 0.36,
        ),
      Path()
        ..moveTo(size.width * 0.18, size.height * 0.42)
        ..cubicTo(
          size.width * 0.31,
          size.height * 0.39,
          size.width * 0.32,
          size.height * 0.54,
          size.width * 0.22,
          size.height * 0.55,
        ),
      Path()
        ..moveTo(size.width * 0.32, size.height * 0.5)
        ..cubicTo(
          size.width * 0.42,
          size.height * 0.51,
          size.width * 0.42,
          size.height * 0.67,
          size.width * 0.3,
          size.height * 0.66,
        ),
    ];

    final rightFolds = [
      Path()
        ..moveTo(size.width * 0.75, size.height * 0.25)
        ..cubicTo(
          size.width * 0.66,
          size.height * 0.19,
          size.width * 0.6,
          size.height * 0.27,
          size.width * 0.64,
          size.height * 0.36,
        ),
      Path()
        ..moveTo(size.width * 0.82, size.height * 0.42)
        ..cubicTo(
          size.width * 0.69,
          size.height * 0.39,
          size.width * 0.68,
          size.height * 0.54,
          size.width * 0.78,
          size.height * 0.55,
        ),
      Path()
        ..moveTo(size.width * 0.68, size.height * 0.5)
        ..cubicTo(
          size.width * 0.58,
          size.height * 0.51,
          size.width * 0.58,
          size.height * 0.67,
          size.width * 0.7,
          size.height * 0.66,
        ),
    ];

    final divider = Path()
      ..moveTo(centerX, size.height * 0.16)
      ..lineTo(centerX, size.height * 0.76);

    for (final path in [leftOutline, ...leftFolds, divider]) {
      canvas.drawPath(path, glowPaint(leftColor, strokeWidth * 1.7));
    }
    for (final path in [rightOutline, ...rightFolds, divider]) {
      canvas.drawPath(path, glowPaint(rightColor, strokeWidth * 1.7));
    }

    canvas.drawPath(leftOutline, linePaint(leftColor, strokeWidth));
    for (final path in leftFolds) {
      canvas.drawPath(path, linePaint(leftColor, strokeWidth * 0.78));
    }
    canvas.drawPath(rightOutline, linePaint(rightColor, strokeWidth));
    for (final path in rightFolds) {
      canvas.drawPath(path, linePaint(rightColor, strokeWidth * 0.78));
    }
    canvas.drawPath(divider, linePaint(leftColor, strokeWidth * 0.8));
    canvas.drawPath(divider, linePaint(rightColor, strokeWidth * 0.45));
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

class HomePlayButton extends StatefulWidget {
  const HomePlayButton({super.key, required this.onPressed});

  final VoidCallback onPressed;

  @override
  State<HomePlayButton> createState() => _HomePlayButtonState();
}

class _HomePlayButtonState extends State<HomePlayButton> {
  bool isPressed = false;

  void setPressed(bool value) {
    if (isPressed == value) {
      return;
    }

    setState(() {
      isPressed = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Listener(
        onPointerDown: (_) => setPressed(true),
        onPointerUp: (_) => setPressed(false),
        onPointerCancel: (_) => setPressed(false),
        child: AnimatedScale(
          scale: isPressed ? 0.97 : 1,
          duration: const Duration(milliseconds: 180),
          curve: Curves.easeOutCubic,
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              onTap: withButtonFeedback(widget.onPressed),
              borderRadius: BorderRadius.circular(24),
              child: AnimatedContainer(
                width: 224,
                height: 58,
                duration: const Duration(milliseconds: 220),
                curve: Curves.easeOutCubic,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(29),
                  gradient: const LinearGradient(
                    begin: Alignment.centerLeft,
                    end: Alignment.centerRight,
                    colors: [Color(0xFF54B7FF), Color(0xFF2F74E8)],
                  ),
                  border: Border.all(
                    color: Colors.white.withAlpha(190),
                    width: 1,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(
                        0x662F74E8,
                      ).withAlpha(isPressed ? 76 : 135),
                      blurRadius: isPressed ? 12 : 22,
                      offset: Offset(0, isPressed ? 4 : 10),
                    ),
                  ],
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Icon(
                      Icons.play_arrow_rounded,
                      size: 30,
                      color: Colors.white,
                    ),
                    const SizedBox(width: 10),
                    Text(
                      tr('play'),
                      style: const TextStyle(
                        fontSize: 17,
                        fontWeight: FontWeight.w800,
                        letterSpacing: 0,
                        color: Colors.white,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class HomeFeatureGrid extends StatelessWidget {
  const HomeFeatureGrid({
    super.key,
    required this.onDailyPressed,
    required this.onStatsPressed,
    required this.onAchievementsPressed,
    required this.onStorePressed,
  });

  final VoidCallback onDailyPressed;
  final VoidCallback onStatsPressed;
  final VoidCallback onAchievementsPressed;
  final VoidCallback onStorePressed;

  @override
  Widget build(BuildContext context) {
    return Wrap(
      alignment: WrapAlignment.center,
      runAlignment: WrapAlignment.center,
      spacing: 12,
      runSpacing: 12,
      children: [
        HomeFeatureCard(
          icon: Icons.calendar_month_rounded,
          iconColor: const Color(0xFF4D75FF),
          label: tr('daily_challenge'),
          subtitle: "Daily puzzle",
          iconSize: 40,
          labelFontSize: 13,
          onPressed: onDailyPressed,
        ),
        HomeFeatureCard(
          icon: Icons.bar_chart_rounded,
          iconColor: const Color(0xFF2F74E8),
          label: tr('statistics'),
          subtitle: 'Progress',
          iconSize: 40,
          labelFontSize: 13,
          onPressed: onStatsPressed,
        ),
        HomeFeatureCard(
          icon: Icons.emoji_events_rounded,
          iconColor: const Color(0xFFFFB11F),
          label: tr('achievements'),
          subtitle: 'Milestones',
          iconSize: 40,
          labelFontSize: 12,
          subtitleFontSize: 7.5,
          onPressed: onAchievementsPressed,
        ),
        HomeFeatureCard(
          icon: Icons.shopping_bag_rounded,
          iconColor: const Color(0xFFE84A70),
          label: tr('store'),
          subtitle: 'Hints & gems',
          iconSize: 40,
          labelFontSize: 13,
          onPressed: onStorePressed,
        ),
      ],
    );
  }
}

class HomeFeatureCard extends StatelessWidget {
  const HomeFeatureCard({
    super.key,
    required this.icon,
    required this.iconColor,
    required this.label,
    required this.subtitle,
    this.onPressed,
    this.iconSize = 33,
    this.labelFontSize = 15,
    this.subtitleFontSize = 8.5,
  });

  final IconData icon;
  final Color iconColor;
  final String label;
  final String subtitle;
  final VoidCallback? onPressed;
  final double iconSize;
  final double labelFontSize;
  final double subtitleFontSize;

  @override
  Widget build(BuildContext context) {
    return TactileBounce(
      onTap: withButtonFeedback(onPressed ?? () {}),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(18),
          gradient: const LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              Colors.white,
              Color(0xFFF8FAFC),
              Color(0xFFF1F5F9),
            ],
          ),
          border: Border.all(color: Colors.white, width: 1.4),
          boxShadow: [
            const BoxShadow(
              color: Color(0x201E293B),
              blurRadius: 10,
              offset: Offset(0, 4),
            ),
            BoxShadow(
              color: iconColor.withAlpha(25),
              blurRadius: 6,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: iconSize + 6,
              height: iconSize + 6,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(12),
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [
                    Color.lerp(iconColor, Colors.white, 0.25) ?? iconColor,
                    iconColor,
                    Color.lerp(iconColor, Colors.black, 0.2) ?? iconColor,
                  ],
                ),
                border: Border.all(color: Colors.white.withAlpha(200), width: 1.3),
                boxShadow: [
                  BoxShadow(
                    color: iconColor.withAlpha(90),
                    blurRadius: 8,
                    offset: const Offset(0, 3),
                  ),
                ],
              ),
              child: Center(
                child: Icon(icon, color: Colors.white, size: iconSize * 0.58),
              ),
            ),
            const SizedBox(width: 9),
            Column(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  label,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: labelFontSize,
                    height: 0.95,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0,
                    color: const Color(0xFF1E293B),
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subtitle,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: subtitleFontSize,
                    fontWeight: FontWeight.w700,
                    color: const Color(0xFF64748B),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class StoreComingSoonScreen extends StatelessWidget {
  const StoreComingSoonScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const StoreScreen();
  }
}

class DailyRewardScreen extends StatefulWidget {
  const DailyRewardScreen({super.key});

  @override
  State<DailyRewardScreen> createState() => _DailyRewardScreenState();
}

class _DailyRewardScreenState extends State<DailyRewardScreen> {
  bool isClaiming = false;

  Future<void> _claimToday() async {
    if (isClaiming || !GameStorage.canClaimDailyReward) return;
    setState(() => isClaiming = true);
    final reward = dailyRewardForDate(DateTime.now());
    await GameStorage.claimDailyReward(reward);
    if (!mounted) return;
    playWinSound();
    triggerSuccessFeedback();
    setState(() => isClaiming = false);
    showGameNotification(
      context: context,
      message: '+${reward.quantity} ${reward.label} claimed!',
      icon: Icons.check_circle_rounded,
      accentColor: const Color(0xFF16A947),
      iconColor: const Color(0xFF4ADE80),
    );
  }

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);
    final todayReward = dailyRewardForDate(DateTime.now());
    final canClaim = GameStorage.canClaimDailyReward;

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          body: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/home_background.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              Positioned.fill(
                child: DecoratedBox(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.black.withAlpha(50),
                        Colors.transparent,
                        Colors.black.withAlpha(140),
                      ],
                      stops: const [0.0, 0.35, 1.0],
                    ),
                  ),
                ),
              ),
          SafeArea(
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 430),
                child: SingleChildScrollView(
                  padding: EdgeInsets.fromLTRB(
                    18,
                    18,
                    18,
                    24 + safePadding.bottom,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Row(
                        children: [
                          SettingsBackButton(
                            onPressed: () => Navigator.of(context).maybePop(),
                          ),
                          const Spacer(),
                          const HomeCurrencyRow(),
                          const Spacer(),
                          SettingsBackButton(
                            icon: Icons.settings_rounded,
                            onPressed: () => Navigator.push(
                              context,
                              smoothPageRoute(const SettingsScreen()),
                            ).then((_) {
                              if (mounted) setState(() {});
                            }),
                          ),
                        ],
                      ),
                      const SizedBox(height: 0),
                      SettingsRibbon(
                        title: tr('daily_reward'),
                        assetPath: 'assets/images/daily-reward-heading.webp',
                      ),
                      const SizedBox(height: 12),
                      const StoreMonthlyRewards(),
                      const SizedBox(height: 14),
                      if (canClaim)
                        Material(
                          color: Colors.transparent,
                          child: InkWell(
                            onTap: isClaiming
                                ? null
                                : withButtonFeedback(_claimToday),
                            borderRadius: BorderRadius.circular(20),
                            child: Ink(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 18,
                                vertical: 14,
                              ),
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(20),
                                gradient: const LinearGradient(
                                  colors: [
                                    Color(0xFF8E43F4),
                                    Color(0xFF2F74E8),
                                  ],
                                ),
                                border: Border.all(
                                  color: Colors.white.withAlpha(205),
                                  width: 1.5,
                                ),
                                boxShadow: const [
                                  BoxShadow(
                                    color: Color(0x663A43E8),
                                    blurRadius: 16,
                                    offset: Offset(0, 8),
                                  ),
                                ],
                              ),
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Image.asset(
                                    todayReward.assetPath,
                                    width: 30,
                                    height: 30,
                                  ),
                                  const SizedBox(width: 10),
                                  Text(
                                    '${tr('claim_reward')} (+${todayReward.quantity} ${todayReward.label})',
                                    style: const TextStyle(
                                      color: Colors.white,
                                      fontSize: 16,
                                      fontWeight: FontWeight.w900,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        )
                      else
                        Container(
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          decoration: BoxDecoration(
                            color: const Color(0xFF16A947).withAlpha(45),
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(
                              color: const Color(0xFF16A947),
                              width: 1.5,
                            ),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              const Icon(
                                Icons.check_circle_rounded,
                                color: Color(0xFF16A947),
                                size: 22,
                              ),
                              const SizedBox(width: 8),
                              Text(
                                tr('claimed'),
                                style: const TextStyle(
                                  color: Color(0xFF16A947),
                                  fontSize: 15,
                                  fontWeight: FontWeight.w800,
                                ),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
      },
    );
  }
}

class StoreMonthlyRewards extends StatelessWidget {
  const StoreMonthlyRewards({super.key});

  static const monthNames = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ];

  static const weekDays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'];

  @override
  Widget build(BuildContext context) {
    final today = DateTime.now();
    final firstDay = DateTime(today.year, today.month);
    final daysInMonth = DateTime(today.year, today.month + 1, 0).day;
    final leadingEmptyDays = firstDay.weekday - 1;
    final itemCount = ((leadingEmptyDays + daysInMonth + 6) ~/ 7) * 7;

    return StoreGlassPanel(
      child: Column(
        children: [
          const StoreSectionBanner(
            title: 'DAILY LOGIN REWARDS',
            assetPath: 'assets/images/daily_calendar.webp',
          ),
          const SizedBox(height: 12),
          Text(
            '${monthNames[today.month - 1]} ${today.year}',
            style: const TextStyle(
              color: Color(0xFF25346D),
              fontSize: 20,
              fontWeight: FontWeight.w900,
            ),
          ),
          const SizedBox(height: 12),
          Row(
            children: weekDays
                .map(
                  (day) => Expanded(
                    child: Center(
                      child: Text(
                        day,
                        style: const TextStyle(
                          color: Color(0xFF53639A),
                          fontSize: 10,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                    ),
                  ),
                )
                .toList(),
          ),
          const SizedBox(height: 7),
          LayoutBuilder(
            builder: (context, constraints) {
              const spacing = 5.0;
              final tileWidth = (constraints.maxWidth - (spacing * 6)) / 7;
              return Wrap(
                spacing: spacing,
                runSpacing: 8,
                children: List.generate(itemCount, (index) {
                  final day = index - leadingEmptyDays + 1;
                  if (day < 1 || day > daysInMonth) {
                    return SizedBox(width: tileWidth);
                  }
                  return SizedBox(
                    width: tileWidth,
                    child: StoreRewardDay(
                      day: day,
                      isOpened: GameStorage.storeLoginDates.contains(
                        GameStorage.formatStorageDate(
                          DateTime(today.year, today.month, day),
                        ),
                      ),
                      isMissed:
                          day < today.day &&
                          !GameStorage.storeLoginDates.contains(
                            GameStorage.formatStorageDate(
                              DateTime(today.year, today.month, day),
                            ),
                          ),
                    ),
                  );
                }),
              );
            },
          ),
        ],
      ),
    );
  }
}

class StoreRewardDay extends StatelessWidget {
  const StoreRewardDay({
    super.key,
    required this.day,
    required this.isOpened,
    required this.isMissed,
  });

  final int day;
  final bool isOpened;
  final bool isMissed;

  @override
  Widget build(BuildContext context) {
    final rewardAsset = day % 7 == 0
        ? 'assets/images/gem.webp'
        : day.isEven
        ? 'assets/images/hint-icon.webp'
        : 'assets/images/coin.webp';
    final rewardQuantity = day % 7 == 0
        ? 5 + ((day ~/ 7) * 5)
        : day.isEven
        ? 1 + ((day ~/ 8) % 3)
        : 100 + ((day ~/ 7) * 50);

    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Text(
          '$day',
          textAlign: TextAlign.center,
          style: TextStyle(
            color: isOpened
                ? const Color(0xFF138A42)
                : isMissed
                ? const Color(0xFFC62828)
                : const Color(0xFF26366F),
            fontSize: 11,
            fontWeight: FontWeight.w900,
          ),
        ),
        const SizedBox(height: 3),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(horizontal: 3, vertical: 7),
          decoration: BoxDecoration(
            color: isOpened
                ? const Color(0xFF39BF68).withValues(alpha: 0.3)
                : isMissed
                ? const Color(0xFFE53935).withValues(alpha: 0.3)
                : Colors.white.withAlpha(205),
            borderRadius: BorderRadius.circular(10),
            border: Border.all(
              color: isOpened
                  ? const Color(0xFF39BF68)
                  : isMissed
                  ? const Color(0xFFE53935)
                  : Colors.white,
              width: isOpened || isMissed ? 2 : 1,
            ),
            boxShadow: const [
              BoxShadow(
                color: Color(0x1E283A82),
                blurRadius: 5,
                offset: Offset(0, 2),
              ),
            ],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Image.asset(
                rewardAsset,
                width: 30,
                height: 30,
                fit: BoxFit.contain,
                alignment: Alignment.center,
              ),
              const SizedBox(height: 2),
              Text(
                '$rewardQuantity',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF26366F),
                  fontSize: 10,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class StoreHintSection extends StatelessWidget {
  const StoreHintSection({
    super.key,
    required this.title,
    required this.currencyAsset,
    required this.prices,
    required this.buttonColors,
    this.onBuy,
  });

  final String title;
  final String currencyAsset;
  final List<int> prices;
  final List<Color> buttonColors;
  final void Function(int count, int price)? onBuy;

  static const hintCounts = [1, 3, 5, 15];

  @override
  Widget build(BuildContext context) {
    return StoreGlassPanel(
      child: Column(
        children: [
          StoreSectionBanner(title: title, assetPath: currencyAsset),
          const SizedBox(height: 14),
          LayoutBuilder(
            builder: (context, constraints) {
              final columns = constraints.maxWidth >= 360 ? 4 : 2;
              return GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: hintCounts.length,
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: columns,
                  crossAxisSpacing: 8,
                  mainAxisSpacing: 10,
                  childAspectRatio: columns == 4 ? 0.62 : 0.94,
                ),
                itemBuilder: (context, index) => StoreHintPack(
                  count: hintCounts[index],
                  price: prices[index],
                  currencyAsset: currencyAsset,
                  buttonColors: buttonColors,
                  onTap: onBuy != null
                      ? () => onBuy!(hintCounts[index], prices[index])
                      : null,
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}

class StoreHintPack extends StatelessWidget {
  const StoreHintPack({
    super.key,
    required this.count,
    required this.price,
    required this.currencyAsset,
    required this.buttonColors,
    this.onTap,
  });

  final int count;
  final int price;
  final String currencyAsset;
  final List<Color> buttonColors;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(6, 10, 6, 8),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(230),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.white, width: 1.5),
        boxShadow: const [
          BoxShadow(
            color: Color(0x24283A82),
            blurRadius: 7,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        children: [
          Expanded(
            child: Image.asset(
              'assets/images/hint-icon.webp',
              fit: BoxFit.contain,
            ),
          ),
          const SizedBox(height: 5),
          Text(
            '$count ${count == 1 ? tr('hint') : tr('hints')}',
            maxLines: 1,
            style: const TextStyle(
              color: Color(0xFF26366F),
              fontSize: 13,
              fontWeight: FontWeight.w900,
            ),
          ),
          const SizedBox(height: 7),
          Material(
            color: Colors.transparent,
            borderRadius: BorderRadius.circular(13),
            child: InkWell(
              borderRadius: BorderRadius.circular(13),
              onTap: onTap != null ? withButtonFeedback(onTap!) : null,
              child: Ink(
                height: 34,
                decoration: BoxDecoration(
                  gradient: LinearGradient(colors: buttonColors),
                  borderRadius: BorderRadius.circular(13),
                  boxShadow: const [
                    BoxShadow(
                      color: Color(0x33253670),
                      blurRadius: 4,
                      offset: Offset(0, 3),
                    ),
                  ],
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset(currencyAsset, width: 20, height: 20),
                    const SizedBox(width: 4),
                    Flexible(
                      child: Text(
                        '$price',
                        maxLines: 1,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 14,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StoreGlassPanel extends StatelessWidget {
  const StoreGlassPanel({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(12, 14, 12, 14),
      decoration: BoxDecoration(
        color: const Color(0xEAF7F7FF),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.white.withAlpha(225), width: 1.5),
        boxShadow: const [
          BoxShadow(
            color: Color(0x33502AB8),
            blurRadius: 12,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: child,
    );
  }
}

class StoreSectionBanner extends StatelessWidget {
  const StoreSectionBanner({
    super.key,
    required this.title,
    required this.assetPath,
  });

  final String title;
  final String assetPath;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 48,
      padding: const EdgeInsets.symmetric(horizontal: 14),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF9D58F2), Color(0xFF6932D7)],
        ),
        borderRadius: BorderRadius.circular(14),
        boxShadow: const [
          BoxShadow(
            color: Color(0x553F169D),
            blurRadius: 7,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset(assetPath, width: 34, height: 34, fit: BoxFit.contain),
          const SizedBox(width: 9),
          Flexible(
            child: FittedBox(
              fit: BoxFit.scaleDown,
              child: Text(
                title,
                maxLines: 1,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 19,
                  fontWeight: FontWeight.w900,
                  shadows: [
                    Shadow(
                      color: Color(0x663B177D),
                      blurRadius: 3,
                      offset: Offset(0, 2),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StoreHelpPill extends StatelessWidget {
  const StoreHelpPill({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 11),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(220),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white, width: 1.5),
      ),
      child: const Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.favorite_rounded, color: Color(0xFFFF5F86), size: 24),
          SizedBox(width: 10),
          Flexible(
            child: Text(
              'Use hints to get help and solve puzzles easily!',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Color(0xFF26366F),
                fontSize: 13,
                fontWeight: FontWeight.w800,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StoreTopBar extends StatelessWidget {
  const StoreTopBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        HomeCircleButton(
          icon: Icons.arrow_back_ios_new_rounded,
          onPressed: () => Navigator.of(context).maybePop(),
        ),
        const Spacer(),
        const HomeCircleButton(icon: Icons.settings_rounded),
      ],
    );
  }
}

class StoreHero extends StatelessWidget {
  const StoreHero({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 170,
      child: Stack(
        alignment: Alignment.center,
        clipBehavior: Clip.none,
        children: [
          const Positioned(
            top: 12,
            child: Image(
              image: AssetImage('assets/images/Purple_Store_Building_Icon.png'),
              width: 202,
              height: 145,
              fit: BoxFit.contain,
            ),
          ),
          const Positioned(
            left: 62,
            bottom: 16,
            child: Image(
              image: AssetImage('assets/images/Pink_Shopping_Bag_Icon.png'),
              width: 58,
              height: 58,
              fit: BoxFit.contain,
            ),
          ),
          Positioned(
            right: 70,
            bottom: 28,
            child: Transform.rotate(
              angle: -0.12,
              child: const Image(
                image: AssetImage('assets/images/Store_Sign_Board.png'),
                width: 82,
                fit: BoxFit.contain,
              ),
            ),
          ),
          const Positioned(
            right: 90,
            top: 34,
            child: StoreFloatingAsset(
              assetPath: 'assets/images/Golden_Star_Icon.png',
              size: 36,
            ),
          ),
          const Positioned(
            left: 82,
            top: 76,
            child: StoreDot(color: Color(0xFF8D49EC), size: 13),
          ),
          const Positioned(
            right: 54,
            top: 88,
            child: StoreDot(color: Color(0xFFE84A70), size: 10),
          ),
        ],
      ),
    );
  }
}

class StoreMainPanel extends StatelessWidget {
  const StoreMainPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 28, 18, 20),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(178),
        borderRadius: BorderRadius.circular(34),
        border: Border.all(color: Colors.white.withAlpha(210), width: 1.6),
        boxShadow: const [
          BoxShadow(
            color: Color(0x204F7AC2),
            blurRadius: 24,
            offset: Offset(0, 12),
          ),
        ],
      ),
      child: const Column(
        children: [
          FittedBox(
            fit: BoxFit.scaleDown,
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                StoreSpark(color: Color(0xFF9A65F4)),
                SizedBox(width: 10),
                Text(
                  'COMING',
                  style: TextStyle(
                    color: Color(0xFF7D46E8),
                    fontSize: 40,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0,
                    shadows: [
                      Shadow(
                        color: Color(0x33814EE9),
                        blurRadius: 7,
                        offset: Offset(0, 3),
                      ),
                    ],
                  ),
                ),
                SizedBox(width: 10),
                Text(
                  'SOON',
                  style: TextStyle(
                    color: Color(0xFFE84A70),
                    fontSize: 40,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0,
                    shadows: [
                      Shadow(
                        color: Color(0x33E84A70),
                        blurRadius: 7,
                        offset: Offset(0, 3),
                      ),
                    ],
                  ),
                ),
                SizedBox(width: 10),
                StoreSpark(color: Color(0xFF9A65F4)),
              ],
            ),
          ),
          SizedBox(height: 16),
          Text(
            'Our store is getting ready\nto bring you something amazing!',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Color(0xFF17275B),
              fontSize: 18,
              fontWeight: FontWeight.w700,
              height: 1.32,
            ),
          ),
          SizedBox(height: 24),
          StoreCountdownRow(),
          SizedBox(height: 24),
          StoreAlertPill(),
        ],
      ),
    );
  }
}

class StoreCountdownRow extends StatelessWidget {
  const StoreCountdownRow({super.key});

  @override
  Widget build(BuildContext context) {
    return const Row(
      children: [
        Expanded(
          child: StoreCountdownTile(
            value: '07',
            label: 'DAYS',
            color: Color(0xFF7D46E8),
          ),
        ),
        StoreColon(),
        Expanded(
          child: StoreCountdownTile(
            value: '15',
            label: 'HOURS',
            color: Color(0xFFE84A70),
          ),
        ),
        StoreColon(),
        Expanded(
          child: StoreCountdownTile(
            value: '34',
            label: 'MINUTES',
            color: Color(0xFFFF982B),
          ),
        ),
        StoreColon(),
        Expanded(
          child: StoreCountdownTile(
            value: '28',
            label: 'SECONDS',
            color: Color(0xFF2F86F4),
          ),
        ),
      ],
    );
  }
}

class StoreCountdownTile extends StatelessWidget {
  const StoreCountdownTile({
    super.key,
    required this.value,
    required this.label,
    required this.color,
  });

  final String value;
  final String label;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: 0.86,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 9),
        decoration: BoxDecoration(
          color: Colors.white.withAlpha(222),
          borderRadius: BorderRadius.circular(18),
          border: Border.all(color: Colors.white, width: 2),
          boxShadow: const [
            BoxShadow(
              color: Color(0x1B3F5B93),
              blurRadius: 10,
              offset: Offset(0, 5),
            ),
          ],
        ),
        child: FittedBox(
          fit: BoxFit.scaleDown,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                value,
                style: TextStyle(
                  color: color,
                  fontSize: 34,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0,
                ),
              ),
              Text(
                label,
                style: const TextStyle(
                  color: Color(0xFF5B6380),
                  fontSize: 12,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class StoreColon extends StatelessWidget {
  const StoreColon({super.key});

  @override
  Widget build(BuildContext context) {
    return const Padding(
      padding: EdgeInsets.symmetric(horizontal: 5),
      child: Text(
        ':',
        style: TextStyle(
          color: Color(0xFF8D49EC),
          fontSize: 30,
          fontWeight: FontWeight.w900,
        ),
      ),
    );
  }
}

class StoreAlertPill extends StatelessWidget {
  const StoreAlertPill({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(14, 12, 18, 12),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(222),
        borderRadius: BorderRadius.circular(34),
        border: Border.all(color: Colors.white, width: 1.5),
        boxShadow: const [
          BoxShadow(
            color: Color(0x183F5B93),
            blurRadius: 12,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: const Row(
        children: [
          StoreRoundIcon(
            assetPath: 'assets/images/Purple_Bell_Notification_Icon.png',
            size: 62,
            imageSize: 48,
          ),
          SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Stay Tuned!',
                  style: TextStyle(
                    color: Color(0xFF17275B),
                    fontSize: 22,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                SizedBox(height: 3),
                Text(
                  'Exciting products are on the way.',
                  style: TextStyle(
                    color: Color(0xFF3E4C78),
                    fontSize: 14,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class StoreWhyWaitSection extends StatelessWidget {
  const StoreWhyWaitSection({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            StoreSpark(color: Color(0xFF9A65F4), small: true),
            SizedBox(width: 12),
            Text(
              'Why wait?',
              style: TextStyle(
                color: Color(0xFF17275B),
                fontSize: 22,
                fontWeight: FontWeight.w900,
              ),
            ),
            SizedBox(width: 12),
            StoreSpark(color: Color(0xFF9A65F4), small: true),
          ],
        ),
        SizedBox(height: 14),
        Row(
          children: [
            Expanded(
              child: StoreMiniFeatureCard(
                assetPath: 'assets/images/gift_3.png',
                title: 'Amazing Offers',
                subtitle: 'Coming your way',
              ),
            ),
            SizedBox(width: 12),
            Expanded(
              child: StoreMiniFeatureCard(
                assetPath: 'assets/images/Golden_Star_Icon.png',
                title: 'Premium Content',
                subtitle: 'Handpicked for you',
              ),
            ),
            SizedBox(width: 12),
            Expanded(
              child: StoreMiniFeatureCard(
                assetPath: 'assets/images/Pink_Shopping_Bag_Icon.png',
                title: 'Exclusive Items',
                subtitle: 'Only for you',
              ),
            ),
          ],
        ),
      ],
    );
  }
}

class StoreMiniFeatureCard extends StatelessWidget {
  const StoreMiniFeatureCard({
    super.key,
    required this.assetPath,
    required this.title,
    required this.subtitle,
  });

  final String assetPath;
  final String title;
  final String subtitle;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: 0.9,
      child: Container(
        padding: const EdgeInsets.fromLTRB(8, 12, 8, 10),
        decoration: BoxDecoration(
          color: Colors.white.withAlpha(214),
          borderRadius: BorderRadius.circular(22),
          border: Border.all(color: Colors.white, width: 1.5),
          boxShadow: const [
            BoxShadow(
              color: Color(0x173F5B93),
              blurRadius: 11,
              offset: Offset(0, 6),
            ),
          ],
        ),
        child: Column(
          children: [
            Expanded(
              child: Image(image: AssetImage(assetPath), fit: BoxFit.contain),
            ),
            const SizedBox(height: 5),
            FittedBox(
              fit: BoxFit.scaleDown,
              child: Text(
                title,
                maxLines: 1,
                style: const TextStyle(
                  color: Color(0xFF17275B),
                  fontSize: 13,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ),
            const SizedBox(height: 3),
            FittedBox(
              fit: BoxFit.scaleDown,
              child: Text(
                subtitle,
                maxLines: 1,
                style: const TextStyle(
                  color: Color(0xFF4F5D82),
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class StoreThanksPill extends StatelessWidget {
  const StoreThanksPill({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(14, 12, 18, 12),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(222),
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: Colors.white, width: 1.4),
        boxShadow: const [
          BoxShadow(
            color: Color(0x183F5B93),
            blurRadius: 12,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: const Row(
        children: [
          StoreRoundIcon(
            assetPath: 'assets/images/Bottom_Heart_Icon.png',
            size: 52,
            imageSize: 38,
            plain: true,
          ),
          SizedBox(width: 14),
          Expanded(
            child: Text(
              "Thank you for being part of MindTrap AI.\nWe can't wait to surprise you!",
              style: TextStyle(
                color: Color(0xFF17275B),
                fontSize: 14,
                height: 1.35,
                fontWeight: FontWeight.w700,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StoreRoundIcon extends StatelessWidget {
  const StoreRoundIcon({
    super.key,
    required this.assetPath,
    required this.size,
    required this.imageSize,
    this.plain = false,
  });

  final String assetPath;
  final double size;
  final double imageSize;
  final bool plain;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: plain ? Colors.white.withAlpha(220) : const Color(0xFF8D49EC),
        shape: BoxShape.circle,
        boxShadow: const [
          BoxShadow(
            color: Color(0x263F5B93),
            blurRadius: 10,
            offset: Offset(0, 5),
          ),
        ],
      ),
      child: Center(
        child: Image(
          image: AssetImage(assetPath),
          width: imageSize,
          height: imageSize,
          fit: BoxFit.contain,
        ),
      ),
    );
  }
}

class StoreFloatingAsset extends StatelessWidget {
  const StoreFloatingAsset({
    super.key,
    required this.assetPath,
    required this.size,
  });

  final String assetPath;
  final double size;

  @override
  Widget build(BuildContext context) {
    return Image(
      image: AssetImage(assetPath),
      width: size,
      height: size,
      fit: BoxFit.contain,
    );
  }
}

class StoreDot extends StatelessWidget {
  const StoreDot({super.key, required this.color, required this.size});

  final Color color;
  final double size;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(color: color, shape: BoxShape.circle),
    );
  }
}

class StoreSpark extends StatelessWidget {
  const StoreSpark({super.key, required this.color, this.small = false});

  final Color color;
  final bool small;

  @override
  Widget build(BuildContext context) {
    final width = small ? 24.0 : 30.0;
    final height = small ? 28.0 : 34.0;

    return CustomPaint(
      size: Size(width, height),
      painter: StoreSparkPainter(color),
    );
  }
}

class StoreSparkPainter extends CustomPainter {
  const StoreSparkPainter(this.color);

  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color
      ..strokeWidth = 3.2
      ..strokeCap = StrokeCap.round;

    canvas.drawLine(
      Offset(size.width * 0.75, size.height * 0.15),
      Offset(size.width * 0.25, size.height * 0.04),
      paint,
    );
    canvas.drawLine(
      Offset(size.width * 0.88, size.height * 0.48),
      Offset(size.width * 0.18, size.height * 0.48),
      paint,
    );
    canvas.drawLine(
      Offset(size.width * 0.72, size.height * 0.82),
      Offset(size.width * 0.22, size.height * 0.96),
      paint,
    );
  }

  @override
  bool shouldRepaint(covariant StoreSparkPainter oldDelegate) {
    return oldDelegate.color != color;
  }
}

enum AchievementVisual {
  shieldTarget,
  shieldStar,
  shieldCrown,
  medal,
  book,
  globe,
  calendar,
  trophy,
  shield,
  target,
}

class AchievementItem {
  const AchievementItem({
    required this.id,
    required this.title,
    required this.description,
    required this.visual,
    this.assetPath,
    this.giftAssetPath,
    this.date,
    this.current = 0,
    this.target = 1,
    this.color = const Color(0xFF6F63FF),
  });

  final String id;
  final String title;
  final String description;
  final AchievementVisual visual;
  final String? assetPath;
  final String? giftAssetPath;
  final String? date;
  final int current;
  final int target;
  final Color color;

  bool get isCompleted => target > 0 && current >= target;
  bool get isInProgress => current > 0 && !isCompleted;
  bool get isLocked => !isCompleted && !isInProgress;

  AchievementItem copyWith({
    String? giftAssetPath,
    int? current,
    Color? color,
  }) {
    return AchievementItem(
      id: id,
      title: title,
      description: description,
      visual: visual,
      assetPath: assetPath,
      giftAssetPath: giftAssetPath ?? this.giftAssetPath,
      date: date,
      current: current ?? this.current,
      target: target,
      color: color ?? this.color,
    );
  }
}

const progressGiftAssetPaths = [
  'assets/images/Speedy_Thinker_gift_icon.png',
  'assets/images/Streak_Champion_gift_icon.png',
  'assets/images/gift_3.png',
  'assets/images/gift_4.png',
  'assets/images/gift_5.png',
];

const progressGiftColors = [
  Color(0xFF9460E2),
  Color(0xFFF78C26),
  Color(0xFF31C58A),
  Color(0xFF419BF5),
  Color(0xFFF33952),
];

const completedAchievements = [
  AchievementItem(
    id: 'first_win',
    title: 'First Win',
    description: 'Win your first\nchallenge round',
    visual: AchievementVisual.shieldTarget,
    assetPath: 'assets/images/achievement_sharpshooter.webp',
    target: 1,
    color: Color(0xFF31C882),
  ),
  AchievementItem(
    id: 'perfect_mind',
    title: 'Perfect Mind',
    description: 'Finish a challenge\nwith 100% accuracy',
    visual: AchievementVisual.shieldStar,
    assetPath: 'assets/images/Smart_Solver.png',
    target: 1,
    color: Color(0xFF2F9DF2),
  ),
  AchievementItem(
    id: 'comeback',
    title: 'Comeback',
    description: 'Win with exactly\n1 heart left',
    visual: AchievementVisual.shieldCrown,
    assetPath: 'assets/images/Perfect_Master.png',
    target: 1,
    color: Color(0xFF9F58D9),
  ),
];

const inProgressAchievements = [
  AchievementItem(
    id: 'sharp_thinker',
    title: 'Sharp Thinker',
    description: 'Answer 50 challenge\nquestions correctly',
    visual: AchievementVisual.shieldStar,
    assetPath: 'assets/images/Speedy_Thinker_main_icon.png',
    giftAssetPath: 'assets/images/Speedy_Thinker_gift_icon.png',
    target: 50,
    color: Color(0xFF9962EA),
  ),
  AchievementItem(
    id: 'trap_survivor',
    title: 'Trap Survivor',
    description: 'Play 10 challenge\nrounds',
    visual: AchievementVisual.trophy,
    assetPath: 'assets/images/Streak_Champion_main_icon.png',
    giftAssetPath: 'assets/images/Streak_Champion_gift_icon.png',
    target: 10,
    color: Color(0xFFFF8A22),
  ),
];

const lockedAchievements = [
  AchievementItem(
    id: 'perfect_score',
    title: 'Perfect Score',
    description: 'Complete 10 perfect\nchallenge rounds',
    visual: AchievementVisual.medal,
    assetPath: 'assets/images/Puzzle_Pro.png',
    target: 10,
    color: Color(0xFFFF8A22),
  ),
  AchievementItem(
    id: 'challenge_expert',
    title: 'Challenge Expert',
    description: 'Complete 25\nchallenge levels',
    visual: AchievementVisual.book,
    assetPath: 'assets/images/Knowledge_King.png',
    target: 25,
    color: Color(0xFF2F9DF2),
  ),
  AchievementItem(
    id: 'daily_champion',
    title: 'Daily Champion',
    description: 'Play daily puzzle\n7 days in a row',
    visual: AchievementVisual.globe,
    assetPath: 'assets/images/World_Explorer.png',
    target: 7,
    color: Color(0xFF31C882),
  ),
  AchievementItem(
    id: 'streak_starter',
    title: 'Streak Starter',
    description: 'Reach a 3-day\ndaily streak',
    visual: AchievementVisual.calendar,
    assetPath: 'assets/images/Daily_Champion.png',
    target: 3,
  ),
  AchievementItem(
    id: 'dedicated_mind',
    title: 'Dedicated Mind',
    description: 'Reach a 7-day\ndaily streak',
    visual: AchievementVisual.trophy,
    assetPath: 'assets/images/Perfect_Score.png',
    target: 7,
  ),
  AchievementItem(
    id: 'streak_master',
    title: 'Streak Master',
    description: 'Reach a 30-day\ndaily streak',
    visual: AchievementVisual.shield,
    assetPath: 'assets/images/Streak_Master.png',
    target: 30,
  ),
];

List<AchievementItem> get baseAchievementItems => [
  ...completedAchievements,
  ...inProgressAchievements,
  ...lockedAchievements,
];

List<AchievementItem> get allAchievements => baseAchievementItems
    .map(GameStorage.applyAchievementProgress)
    .toList(growable: false);

List<AchievementItem> get completedAchievementItems => allAchievements
    .where((achievement) => achievement.isCompleted)
    .toList(growable: false);

List<AchievementItem> get inProgressAchievementItems => allAchievements
    .where((achievement) => achievement.isInProgress)
    .toList(growable: false);

List<AchievementItem> get lockedAchievementItems => allAchievements
    .where((achievement) => achievement.isLocked)
    .toList(growable: false);

List<AchievementItem> progressItemsWithOrderedGifts(
  List<AchievementItem> items,
) {
  return [
    for (var index = 0; index < items.length; index++)
      items[index].copyWith(
        giftAssetPath:
            progressGiftAssetPaths[index % progressGiftAssetPaths.length],
        color: progressGiftColors[index % progressGiftColors.length],
      ),
  ];
}

class AchievementsScreen extends StatelessWidget {
  const AchievementsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        final completedItems = completedAchievementItems;
        final inProgressItems = progressItemsWithOrderedGifts(
          inProgressAchievementItems,
        );
        final lockedItems = lockedAchievementItems;
        final completedCount = completedItems.length;
        final inProgressCount = inProgressItems.length;
        final lockedCount = lockedItems.length;

        return Scaffold(
          body: Stack(
            children: [
              const Positioned.fill(
                child: OptionalAssetImage(
                  assetPath: 'assets/images/achievements_background.webp',
                  fallbackAssetPath:
                      'assets/images/puzzle_complete_background.webp',
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              SafeArea(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.fromLTRB(18, 20, 18, 24),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          Align(
                            alignment: Alignment.centerLeft,
                            child: StatsCircleButton(
                              icon: Icons.arrow_back_ios_new_rounded,
                              onPressed: () => Navigator.of(context).maybePop(),
                            ),
                          ),
                          const SizedBox(height: 8),
                          Text(
                            tr('achievements'),
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              color: Color(0xFF10234D),
                              fontSize: 34,
                              fontWeight: FontWeight.w900,
                              letterSpacing: 0,
                            ),
                          ),
                      const SizedBox(height: 8),
                      const Text(
                        'Unlock achievements and earn rewards!',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: Color(0xFF41557A),
                          fontSize: 15,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      const SizedBox(height: 24),
                      const AchievementSummaryCard(),
                      const SizedBox(height: 26),
                      AchievementSectionHeader(
                        icon: Icons.star_rounded,
                        iconColor: const Color(0xFFFFB52E),
                        title: 'Completed',
                        count: completedCount,
                      ),
                      const SizedBox(height: 12),
                      CompletedAchievementsRail(items: completedItems),
                      const SizedBox(height: 26),
                      AchievementSectionHeader(
                        icon: Icons.lock_open_rounded,
                        iconColor: const Color(0xFF8892AE),
                        title: 'In Progress',
                        count: inProgressCount,
                      ),
                      const SizedBox(height: 12),
                      for (
                        var index = 0;
                        index < inProgressItems.length;
                        index++
                      ) ...[
                        InProgressAchievementCard(item: inProgressItems[index]),
                        if (index != inProgressItems.length - 1)
                          const SizedBox(height: 12),
                      ],
                      const SizedBox(height: 22),
                      AchievementSectionHeader(
                        icon: Icons.lock_rounded,
                        iconColor: const Color(0xFF8892AE),
                        title: 'Locked',
                        count: lockedCount,
                      ),
                      const SizedBox(height: 12),
                      LockedAchievementsRail(items: lockedItems),
                      const SizedBox(height: 26),
                      StatsHomeButton(
                        onPressed: () {
                          Navigator.of(
                            context,
                          ).popUntil((route) => route.isFirst);
                        },
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
      },
    );
  }
}

class AchievementSummaryCard extends StatelessWidget {
  const AchievementSummaryCard({super.key});

  @override
  Widget build(BuildContext context) {
    final completedCount = completedAchievementItems.length;
    final totalCount = allAchievements.length;
    final completionValue = totalCount == 0 ? 0.0 : completedCount / totalCount;
    final completionPercent = (completionValue * 100).round();

    return Container(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 18),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(153),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withAlpha(125)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x1CCA7DA4),
            blurRadius: 22,
            offset: Offset(0, 10),
          ),
        ],
      ),
      child: Row(
        children: [
          SizedBox(
            width: 148,
            height: 108,
            child: Stack(
              alignment: Alignment.center,
              children: [
                Positioned(
                  left: 0,
                  bottom: 14,
                  child: Transform.rotate(
                    angle: 12 * pi / 180,
                    child: const Image(
                      image: AssetImage(
                        'assets/images/puzzle_complete_leaf1.png',
                      ),
                      width: 48,
                      fit: BoxFit.contain,
                    ),
                  ),
                ),
                Positioned(
                  right: 0,
                  bottom: 14,
                  child: Transform.rotate(
                    angle: -12 * pi / 180,
                    child: const Image(
                      image: AssetImage(
                        'assets/images/puzzle_complete_leaf2.png',
                      ),
                      width: 48,
                      fit: BoxFit.contain,
                    ),
                  ),
                ),
                const Image(
                  image: AssetImage('assets/images/level_complete_trophy.png'),
                  width: 92,
                  height: 92,
                  fit: BoxFit.contain,
                ),
              ],
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Total Achievements',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    color: Color(0xFF10234D),
                    fontSize: 16,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                const SizedBox(height: 10),
                FittedBox(
                  fit: BoxFit.scaleDown,
                  alignment: Alignment.centerLeft,
                  child: Text.rich(
                    TextSpan(
                      children: [
                        TextSpan(
                          text: '$completedCount',
                          style: const TextStyle(
                            color: Color(0xFFE84A70),
                            fontSize: 38,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                        TextSpan(
                          text: ' / $totalCount',
                          style: const TextStyle(
                            color: Color(0xFF3F5277),
                            fontSize: 30,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(999),
                        child: LinearProgressIndicator(
                          value: completionValue,
                          minHeight: 12,
                          backgroundColor: const Color(0xFFEADFE8),
                          valueColor: const AlwaysStoppedAnimation<Color>(
                            Color(0xFFE84A70),
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Text(
                      '$completionPercent%',
                      style: const TextStyle(
                        color: Color(0xFF10234D),
                        fontSize: 15,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class AchievementSectionHeader extends StatelessWidget {
  const AchievementSectionHeader({
    super.key,
    required this.icon,
    required this.iconColor,
    required this.title,
    required this.count,
  });

  final IconData icon;
  final Color iconColor;
  final String title;
  final int count;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(icon, color: iconColor, size: 28),
        const SizedBox(width: 10),
        Text(
          title,
          style: const TextStyle(
            color: Color(0xFF10234D),
            fontSize: 19,
            fontWeight: FontWeight.w900,
          ),
        ),
        const SizedBox(width: 8),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(178),
            borderRadius: BorderRadius.circular(999),
            border: Border.all(color: const Color(0xFFE2E8F6)),
          ),
          child: Text(
            '$count',
            style: const TextStyle(
              color: Color(0xFF10234D),
              fontSize: 14,
              fontWeight: FontWeight.w900,
            ),
          ),
        ),
      ],
    );
  }
}

class AchievementStatusBadge extends StatelessWidget {
  const AchievementStatusBadge({
    super.key,
    required this.icon,
    required this.color,
  });

  final IconData icon;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Positioned(
      right: -3,
      top: -5,
      child: Container(
        width: 20,
        height: 20,
        decoration: BoxDecoration(color: color, shape: BoxShape.circle),
        child: Icon(icon, color: Colors.white, size: 11),
      ),
    );
  }
}

class CompletedAchievementsRail extends StatelessWidget {
  const CompletedAchievementsRail({super.key, required this.items});

  final List<AchievementItem> items;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      clipBehavior: Clip.none,
      child: Row(
        children: [
          for (var index = 0; index < items.length; index++) ...[
            CompletedAchievementCard(item: items[index]),
            if (index != items.length - 1) const SizedBox(width: 12),
          ],
        ],
      ),
    );
  }
}

class CompletedAchievementCard extends StatelessWidget {
  const CompletedAchievementCard({super.key, required this.item});

  final AchievementItem item;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 128,
      height: 174,
      padding: const EdgeInsets.fromLTRB(8, 10, 8, 10),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(153),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withAlpha(125)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x14CA7DA4),
            blurRadius: 14,
            offset: Offset(0, 7),
          ),
        ],
      ),
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          const AchievementStatusBadge(
            icon: Icons.check_rounded,
            color: Color(0xFF37C97B),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              AchievementVisualIcon(
                visual: item.visual,
                color: item.color,
                size: 70,
                assetPath: item.assetPath,
                locked: false,
              ),
              const SizedBox(height: 6),
              Text(
                item.title,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF10234D),
                  fontSize: 12,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 5),
              Text(
                item.description,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF40577D),
                  fontSize: 10,
                  fontWeight: FontWeight.w700,
                  height: 1.25,
                ),
              ),
              const Spacer(),
              Text(
                item.date ?? '',
                maxLines: 1,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF15A964),
                  fontSize: 10,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class InProgressAchievementCard extends StatelessWidget {
  const InProgressAchievementCard({super.key, required this.item});

  final AchievementItem item;

  @override
  Widget build(BuildContext context) {
    final progress = (item.current / item.target).clamp(0.0, 1.0);

    return Container(
      padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(153),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withAlpha(125)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x14CA7DA4),
            blurRadius: 14,
            offset: Offset(0, 7),
          ),
        ],
      ),
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          const AchievementStatusBadge(
            icon: Icons.lock_open_rounded,
            color: Color(0xFF6F63FF),
          ),
          Row(
            children: [
              AchievementVisualIcon(
                visual: item.visual,
                color: item.color,
                size: 62,
                assetPath: item.assetPath,
                compact: true,
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      item.title,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Color(0xFF10234D),
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(height: 5),
                    Text(
                      item.description,
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Color(0xFF40577D),
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        height: 1.2,
                      ),
                    ),
                    const SizedBox(height: 10),
                    Row(
                      children: [
                        Expanded(
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(999),
                            child: LinearProgressIndicator(
                              value: progress,
                              minHeight: 8,
                              backgroundColor: const Color(0xFFEADFE8),
                              valueColor: AlwaysStoppedAnimation<Color>(
                                item.color,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Text(
                          '${item.current} / ${item.target}',
                          style: TextStyle(
                            color: item.color,
                            fontSize: 12,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 12),
              Container(
                width: 52,
                height: 52,
                decoration: BoxDecoration(
                  color: item.color.withAlpha(28),
                  borderRadius: BorderRadius.circular(14),
                ),
                child: Center(
                  child: SizedBox(
                    width: 42,
                    height: 42,
                    child: item.giftAssetPath == null
                        ? const SizedBox.shrink()
                        : OptionalAssetImage(
                            assetPath: item.giftAssetPath!,
                            fit: BoxFit.contain,
                            fallback: const SizedBox.shrink(),
                          ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class LockedAchievementsRail extends StatelessWidget {
  const LockedAchievementsRail({super.key, required this.items});

  final List<AchievementItem> items;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      clipBehavior: Clip.none,
      child: Row(
        children: [
          for (var index = 0; index < items.length; index++) ...[
            LockedAchievementCard(item: items[index]),
            if (index != items.length - 1) const SizedBox(width: 12),
          ],
        ],
      ),
    );
  }
}

class LockedAchievementCard extends StatelessWidget {
  const LockedAchievementCard({super.key, required this.item});

  final AchievementItem item;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 128,
      height: 180,
      padding: const EdgeInsets.fromLTRB(10, 11, 10, 10),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(153),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withAlpha(125)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x10CA7DA4),
            blurRadius: 12,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          const AchievementStatusBadge(
            icon: Icons.lock_rounded,
            color: Color(0xFF9DA0B5),
          ),
          Column(
            children: [
              AchievementVisualIcon(
                visual: item.visual,
                color: const Color(0xFF9DA0B5),
                size: 66,
                assetPath: item.assetPath,
                locked: true,
              ),
              const SizedBox(height: 8),
              Text(
                item.title,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF566681),
                  fontSize: 13,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 7),
              Text(
                item.description,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF647391),
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  height: 1.25,
                ),
              ),
              const Spacer(),
              Text(
                '${item.current} / ${item.target}',
                style: const TextStyle(
                  color: Color(0xFF647391),
                  fontSize: 12,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class OptionalAssetImage extends StatelessWidget {
  const OptionalAssetImage({
    super.key,
    required this.assetPath,
    this.fallbackAssetPath,
    this.fallback,
    this.fit,
    this.alignment = Alignment.center,
    this.opacity,
  });

  final String assetPath;
  final String? fallbackAssetPath;
  final Widget? fallback;
  final BoxFit? fit;
  final AlignmentGeometry alignment;
  final Animation<double>? opacity;

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<ByteData>(
      future: rootBundle.load(assetPath),
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Image.memory(
            snapshot.data!.buffer.asUint8List(),
            fit: fit,
            alignment: alignment,
            opacity: opacity,
          );
        }

        if (snapshot.hasError) {
          if (fallback != null) {
            return fallback!;
          }
          if (fallbackAssetPath != null) {
            return Image(
              image: AssetImage(fallbackAssetPath!),
              fit: fit,
              alignment: alignment,
              opacity: opacity,
            );
          }
        }

        return fallback ?? const SizedBox.shrink();
      },
    );
  }
}

class AchievementVisualIcon extends StatelessWidget {
  const AchievementVisualIcon({
    super.key,
    required this.visual,
    required this.color,
    this.assetPath,
    this.size = 72,
    this.locked = false,
    this.compact = false,
  });

  final AchievementVisual visual;
  final Color color;
  final String? assetPath;
  final double size;
  final bool locked;
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final fallbackIcon = CustomPaint(
      size: Size.square(size),
      painter: AchievementIconPainter(
        visual: visual,
        color: locked ? const Color(0xFF9DA0B5) : color,
        locked: locked,
        compact: compact,
      ),
    );
    final imagePath =
        assetPath ??
        switch (visual) {
          AchievementVisual.calendar => 'assets/images/daily_calendar.webp',
          AchievementVisual.trophy => 'assets/images/level_complete_trophy.png',
          _ => null,
        };

    Widget icon;
    if (imagePath != null) {
      icon = ColorFiltered(
        colorFilter: locked
            ? const ColorFilter.matrix(<double>[
                0.2126,
                0.7152,
                0.0722,
                0,
                0,
                0.2126,
                0.7152,
                0.0722,
                0,
                0,
                0.2126,
                0.7152,
                0.0722,
                0,
                0,
                0,
                0,
                0,
                0.58,
                0,
              ])
            : const ColorFilter.mode(Colors.transparent, BlendMode.dst),
        child: OptionalAssetImage(
          assetPath: imagePath,
          fallback: fallbackIcon,
          fit: BoxFit.contain,
          opacity: locked ? const AlwaysStoppedAnimation(0.58) : null,
        ),
      );
    } else {
      icon = fallbackIcon;
    }

    return SizedBox(
      width: size,
      height: size,
      child: Center(child: icon),
    );
  }
}

class AchievementIconPainter extends CustomPainter {
  const AchievementIconPainter({
    required this.visual,
    required this.color,
    required this.locked,
    required this.compact,
  });

  final AchievementVisual visual;
  final Color color;
  final bool locked;
  final bool compact;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final paint = Paint()..isAntiAlias = true;
    final shadowPaint = Paint()
      ..color = Colors.black.withAlpha(locked ? 18 : 30)
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 5);

    void drawShield(IconData glyph) {
      final path = Path()
        ..moveTo(center.dx, size.height * 0.08)
        ..quadraticBezierTo(
          size.width * 0.18,
          size.height * 0.18,
          size.width * 0.15,
          size.height * 0.36,
        )
        ..quadraticBezierTo(
          size.width * 0.13,
          size.height * 0.72,
          center.dx,
          size.height * 0.92,
        )
        ..quadraticBezierTo(
          size.width * 0.87,
          size.height * 0.72,
          size.width * 0.85,
          size.height * 0.36,
        )
        ..quadraticBezierTo(
          size.width * 0.82,
          size.height * 0.18,
          center.dx,
          size.height * 0.08,
        )
        ..close();
      canvas.drawPath(path.shift(const Offset(0, 3)), shadowPaint);
      paint.shader = LinearGradient(
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        colors: locked
            ? const [Color(0xFFC9CBD6), Color(0xFF8F93A7)]
            : [color.withAlpha(230), color],
      ).createShader(Offset.zero & size);
      canvas.drawPath(path, paint);
      paint
        ..shader = null
        ..style = PaintingStyle.stroke
        ..strokeWidth = size.width * 0.07
        ..color = Colors.white.withAlpha(locked ? 55 : 90);
      canvas.drawPath(path, paint);
      paint.style = PaintingStyle.fill;
      _drawGlyph(
        canvas,
        glyph,
        center,
        size.width * 0.48,
        locked ? const Color(0xFFF1F2F7) : Colors.white,
      );
    }

    switch (visual) {
      case AchievementVisual.shieldTarget:
        drawShield(Icons.my_location_rounded);
        break;
      case AchievementVisual.shieldStar:
        drawShield(Icons.star_rounded);
        break;
      case AchievementVisual.shieldCrown:
        drawShield(Icons.workspace_premium_rounded);
        break;
      case AchievementVisual.shield:
        drawShield(Icons.star_rounded);
        break;
      case AchievementVisual.medal:
        _drawGlyph(
          canvas,
          Icons.workspace_premium_rounded,
          center,
          size.width * 0.82,
          color,
        );
        break;
      case AchievementVisual.book:
        _drawGlyph(
          canvas,
          Icons.menu_book_rounded,
          center,
          size.width * 0.82,
          color,
        );
        break;
      case AchievementVisual.globe:
        _drawGlyph(
          canvas,
          Icons.public_rounded,
          center,
          size.width * 0.82,
          color,
        );
        break;
      case AchievementVisual.target:
        _drawGlyph(
          canvas,
          Icons.my_location_rounded,
          center,
          size.width * 0.82,
          color,
        );
        break;
      case AchievementVisual.calendar:
      case AchievementVisual.trophy:
        break;
    }
  }

  void _drawGlyph(
    Canvas canvas,
    IconData icon,
    Offset center,
    double iconSize,
    Color glyphColor,
  ) {
    final textPainter = TextPainter(textDirection: TextDirection.ltr);
    textPainter.text = TextSpan(
      text: String.fromCharCode(icon.codePoint),
      style: TextStyle(
        fontFamily: icon.fontFamily,
        package: icon.fontPackage,
        fontSize: iconSize,
        color: glyphColor,
        shadows: [
          Shadow(
            color: Colors.black.withAlpha(locked ? 16 : 34),
            blurRadius: 5,
            offset: const Offset(0, 3),
          ),
        ],
      ),
    );
    textPainter.layout();
    textPainter.paint(
      canvas,
      center - Offset(textPainter.width / 2, textPainter.height / 2),
    );
  }

  @override
  bool shouldRepaint(covariant AchievementIconPainter oldDelegate) {
    return oldDelegate.visual != visual ||
        oldDelegate.color != color ||
        oldDelegate.locked != locked ||
        oldDelegate.compact != compact;
  }
}

class StatsScreen extends StatelessWidget {
  const StatsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          body: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage(
                    'assets/images/puzzle_complete_background.webp',
                  ),
                  fit: BoxFit.cover,
                  alignment: Alignment.center,
                ),
              ),
              const LevelCompleteConfettiLayer(),
              SafeArea(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.fromLTRB(24, 24, 24, 26),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          Align(
                            alignment: Alignment.centerLeft,
                            child: StatsCircleButton(
                              icon: Icons.arrow_back_ios_new_rounded,
                              onPressed: () => Navigator.of(context).maybePop(),
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            tr('statistics'),
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                          color: Color(0xFF11224D),
                          fontSize: 36,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0,
                        ),
                      ),
                      const SizedBox(height: 8),
                      const Text(
                        'Track your progress and keep improving!',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: Color(0xFF3B466A),
                          fontSize: 16,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      const SizedBox(height: 26),
                      const StatsTotalScoreCard(),
                      const SizedBox(height: 18),
                      const StatsMetricStrip(),
                      const SizedBox(height: 18),
                      const StatsCategoryCard(),
                      const SizedBox(height: 18),
                      StatsHomeButton(
                        onPressed: () {
                          Navigator.of(
                            context,
                          ).popUntil((route) => route.isFirst);
                        },
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
      },
    );
  }
}

class StatsCircleButton extends StatelessWidget {
  const StatsCircleButton({
    super.key,
    required this.icon,
    required this.onPressed,
  });

  final IconData icon;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.white.withAlpha(235),
      shape: const CircleBorder(),
      elevation: 8,
      shadowColor: const Color(0x243B4E78),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: withButtonFeedback(onPressed),
        child: SizedBox(
          width: 38,
          height: 38,
          child: Icon(icon, color: const Color(0xFF11224D), size: 18),
        ),
      ),
    );
  }
}

class StatsGlassCard extends StatelessWidget {
  const StatsGlassCard({
    super.key,
    required this.child,
    this.padding = const EdgeInsets.all(18),
    this.borderRadius = 24,
  });

  final Widget child;
  final EdgeInsets padding;
  final double borderRadius;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: padding,
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(222),
        borderRadius: BorderRadius.circular(borderRadius),
        border: Border.all(color: Colors.white.withAlpha(178)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x1A58B887),
            blurRadius: 18,
            offset: Offset(0, 8),
          ),
        ],
      ),
      child: child,
    );
  }
}

class StatsTotalScoreCard extends StatelessWidget {
  const StatsTotalScoreCard({super.key});

  @override
  Widget build(BuildContext context) {
    final totalScore = GameStorage.totalCorrectAnswers * 10;
    final streakLabel = '${GameStorage.currentStreak} Days';

    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 360),
        child: StatsGlassCard(
          padding: const EdgeInsets.fromLTRB(18, 18, 18, 16),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Expanded(
                child: Column(
                  children: [
                    SizedBox(
                      width: 132,
                      height: 108,
                      child: Stack(
                        alignment: Alignment.center,
                        children: [
                          Positioned(
                            left: 5,
                            bottom: 25,
                            child: Transform.rotate(
                              angle: 15 * pi / 180,
                              child: const Image(
                                image: AssetImage(
                                  'assets/images/puzzle_complete_leaf1.png',
                                ),
                                width: 35,
                                fit: BoxFit.contain,
                              ),
                            ),
                          ),
                          Positioned(
                            right: 5,
                            bottom: 25,
                            child: Transform.rotate(
                              angle: -15 * pi / 180,
                              child: const Image(
                                image: AssetImage(
                                  'assets/images/puzzle_complete_leaf2.png',
                                ),
                                width: 35,
                                fit: BoxFit.contain,
                              ),
                            ),
                          ),
                          const Image(
                            image: AssetImage(
                              'assets/images/level_complete_trophy.png',
                            ),
                            width: 75,
                            height: 75,
                            fit: BoxFit.contain,
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 6),
                    const Text(
                      'Total Score',
                      style: TextStyle(
                        color: Color(0xFF3B466A),
                        fontSize: 16,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      '$totalScore',
                      style: TextStyle(
                        color: Color(0xFF18A96F),
                        fontSize: 34,
                        fontWeight: FontWeight.w900,
                        height: 1,
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                width: 1,
                height: 126,
                margin: const EdgeInsets.symmetric(horizontal: 12),
                color: const Color(0x1F172D56),
              ),
              Expanded(
                child: Column(
                  children: [
                    const Icon(
                      Icons.local_fire_department_rounded,
                      color: Color(0xFFFF7A1A),
                      size: 64,
                    ),
                    const SizedBox(height: 10),
                    const Text(
                      'Current Streak',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: Color(0xFF3B466A),
                        fontSize: 16,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
                    const SizedBox(height: 3),
                    Text(
                      streakLabel,
                      style: const TextStyle(
                        color: Color(0xFF18A96F),
                        fontSize: 28,
                        fontWeight: FontWeight.w900,
                        height: 1,
                      ),
                    ),
                    const SizedBox(height: 5),
                    const Text(
                      'Keep it up!',
                      style: TextStyle(
                        color: Color(0xFF3B466A),
                        fontSize: 13,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class StatsMetricStrip extends StatelessWidget {
  const StatsMetricStrip({super.key});

  @override
  Widget build(BuildContext context) {
    final accuracy = '${GameStorage.accuracyPercent}%';
    final totalStars = GameStorage.totalWins * 3;

    return Column(
      children: [
        Row(
          children: [
            Expanded(
              child: StatsMetricItem(
                icon: Icons.extension_rounded,
                color: Color(0xFF4CD99D),
                label: 'Puzzles Solved',
                value: '${GameStorage.totalCorrectAnswers}',
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: StatsMetricItem(
                icon: Icons.my_location_rounded,
                color: Color(0xFF5B9DF5),
                label: 'Accuracy',
                value: accuracy,
              ),
            ),
          ],
        ),
        const SizedBox(height: 14),
        Row(
          children: [
            Expanded(
              child: StatsMetricItem(
                icon: Icons.bolt_rounded,
                color: Color(0xFF9F68E8),
                label: 'Best Streak',
                value: '${GameStorage.bestStreak}',
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: StatsMetricItem(
                icon: Icons.star_rounded,
                color: Color(0xFFFFAB2E),
                label: 'Total Stars',
                value: '$totalStars',
              ),
            ),
          ],
        ),
      ],
    );
  }
}

class StatsMetricItem extends StatelessWidget {
  const StatsMetricItem({
    super.key,
    required this.icon,
    required this.color,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final Color color;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return StatsGlassCard(
      padding: const EdgeInsets.fromLTRB(12, 16, 12, 16),
      borderRadius: 24,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Stack(
            alignment: Alignment.center,
            children: [
              SizedBox(
                width: 96,
                height: 70,
                child: CustomPaint(painter: StatsSparklePainter(color)),
              ),
              Container(
                width: 66,
                height: 66,
                decoration: BoxDecoration(
                  color: color,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: color.withAlpha(92),
                      blurRadius: 16,
                      offset: const Offset(0, 7),
                    ),
                  ],
                ),
                child: Icon(icon, color: Colors.white, size: 37),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Color(0xFF27325E),
              fontSize: 16,
              fontWeight: FontWeight.w800,
            ),
          ),
          const SizedBox(height: 10),
          FittedBox(
            fit: BoxFit.scaleDown,
            child: Text(
              value,
              maxLines: 1,
              style: const TextStyle(
                color: Color(0xFF111D3A),
                fontSize: 38,
                fontWeight: FontWeight.w900,
                height: 1,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StatsSparklePainter extends CustomPainter {
  const StatsSparklePainter(this.color);

  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color.withAlpha(170)
      ..style = PaintingStyle.fill;

    void drawSparkle(Offset center, double radius) {
      final path = Path()
        ..moveTo(center.dx, center.dy - radius)
        ..quadraticBezierTo(
          center.dx + radius * 0.22,
          center.dy - radius * 0.22,
          center.dx + radius,
          center.dy,
        )
        ..quadraticBezierTo(
          center.dx + radius * 0.22,
          center.dy + radius * 0.22,
          center.dx,
          center.dy + radius,
        )
        ..quadraticBezierTo(
          center.dx - radius * 0.22,
          center.dy + radius * 0.22,
          center.dx - radius,
          center.dy,
        )
        ..quadraticBezierTo(
          center.dx - radius * 0.22,
          center.dy - radius * 0.22,
          center.dx,
          center.dy - radius,
        )
        ..close();
      canvas.drawPath(path, paint);
    }

    const leftPosition = 5.0;
    const rightPosition = 5.0;
    const firstVerticalPosition = 15.0;
    const secondVerticalPosition = 55.0;

    drawSparkle(Offset(leftPosition, firstVerticalPosition), 8);
    drawSparkle(Offset(leftPosition, secondVerticalPosition), 6);
    drawSparkle(
      Offset(size.width - rightPosition, size.height - firstVerticalPosition),
      10,
    );
    drawSparkle(
      Offset(size.width - rightPosition, size.height - secondVerticalPosition),
      5,
    );
  }

  @override
  bool shouldRepaint(covariant StatsSparklePainter oldDelegate) {
    return oldDelegate.color != color;
  }
}

class StatsCategoryCard extends StatelessWidget {
  const StatsCategoryCard({super.key});

  @override
  Widget build(BuildContext context) {
    final accuracy = GameStorage.accuracyPercent / 100;
    final winRate = GameStorage.totalGamesPlayed == 0
        ? 0.0
        : GameStorage.totalWins / GameStorage.totalGamesPlayed;
    final bestScoreProgress = (GameStorage.bestScore / 50).clamp(0.0, 1.0);
    final streakProgress = (GameStorage.bestStreak / 15).clamp(0.0, 1.0);

    return StatsGlassCard(
      padding: const EdgeInsets.fromLTRB(18, 18, 18, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Performance by Category',
            style: TextStyle(
              color: Color(0xFF172D56),
              fontSize: 16,
              fontWeight: FontWeight.w900,
            ),
          ),
          const SizedBox(height: 18),
          StatsCategoryRow(
            icon: Icons.public_rounded,
            color: Color(0xFF4CD99D),
            label: 'Geography',
            percent: accuracy,
          ),
          const SizedBox(height: 14),
          StatsCategoryRow(
            icon: Icons.science_rounded,
            color: Color(0xFF5B9DF5),
            label: 'Science',
            percent: winRate,
          ),
          const SizedBox(height: 14),
          StatsCategoryRow(
            icon: Icons.menu_book_rounded,
            color: Color(0xFF9F68E8),
            label: 'History',
            percent: bestScoreProgress,
          ),
          const SizedBox(height: 14),
          StatsCategoryRow(
            icon: Icons.palette_rounded,
            color: Color(0xFFFFAB2E),
            label: 'Art & Culture',
            percent: streakProgress,
          ),
        ],
      ),
    );
  }
}

class StatsCategoryRow extends StatelessWidget {
  const StatsCategoryRow({
    super.key,
    required this.icon,
    required this.color,
    required this.label,
    required this.percent,
  });

  final IconData icon;
  final Color color;
  final String label;
  final double percent;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Container(
          width: 36,
          height: 36,
          decoration: BoxDecoration(color: color, shape: BoxShape.circle),
          child: Icon(icon, color: Colors.white, size: 22),
        ),
        const SizedBox(width: 12),
        SizedBox(
          width: 94,
          child: Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(
              color: Color(0xFF27325E),
              fontSize: 15,
              fontWeight: FontWeight.w900,
            ),
          ),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: ClipRRect(
            borderRadius: BorderRadius.circular(999),
            child: LinearProgressIndicator(
              value: percent,
              minHeight: 8,
              backgroundColor: const Color(0xFFD8E8E2),
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
          ),
        ),
        const SizedBox(width: 12),
        Text(
          '${(percent * 100).round()}%',
          style: const TextStyle(
            color: Color(0xFF27325E),
            fontSize: 15,
            fontWeight: FontWeight.w900,
          ),
        ),
      ],
    );
  }
}

class StatsCurrentStreakCard extends StatelessWidget {
  const StatsCurrentStreakCard({super.key});

  @override
  Widget build(BuildContext context) {
    return const StatsGlassCard(
      padding: EdgeInsets.fromLTRB(12, 18, 12, 18),
      child: Column(
        children: [
          Text(
            'Current Streak',
            style: TextStyle(
              color: Color(0xFF172D56),
              fontSize: 16,
              fontWeight: FontWeight.w900,
            ),
          ),
          SizedBox(height: 14),
          Icon(
            Icons.local_fire_department_rounded,
            color: Color(0xFFFF7A1A),
            size: 70,
          ),
          SizedBox(height: 8),
          Text(
            '5 Days',
            style: TextStyle(
              color: Color(0xFF18A96F),
              fontSize: 28,
              fontWeight: FontWeight.w900,
            ),
          ),
          SizedBox(height: 4),
          Text(
            'Keep it up!',
            style: TextStyle(
              color: Color(0xFF3B466A),
              fontSize: 14,
              fontWeight: FontWeight.w700,
            ),
          ),
        ],
      ),
    );
  }
}

class StatsActionButton extends StatelessWidget {
  const StatsActionButton({
    super.key,
    required this.label,
    required this.icon,
    required this.onPressed,
  });

  final String label;
  final IconData icon;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 62,
      child: ElevatedButton(
        onPressed: withButtonFeedback(onPressed),
        style: ElevatedButton.styleFrom(
          elevation: 10,
          shadowColor: const Color(0x5520C997),
          backgroundColor: const Color(0xFF34C987),
          foregroundColor: Colors.white,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(28),
          ),
        ),
        child: Row(
          children: [
            const Spacer(),
            Icon(icon, size: 30, color: Colors.white),
            const SizedBox(width: 16),
            Text(
              label,
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.w900,
                color: Colors.white,
              ),
            ),
            const Spacer(),
            const Icon(
              Icons.chevron_right_rounded,
              size: 34,
              color: Colors.white,
            ),
          ],
        ),
      ),
    );
  }
}

class StatsHomeButton extends StatelessWidget {
  const StatsHomeButton({super.key, required this.onPressed});

  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 56,
      child: ElevatedButton.icon(
        onPressed: withButtonFeedback(onPressed),
        icon: const Icon(
          Icons.home_rounded,
          color: Color(0xFF3B466A),
          size: 28,
        ),
        label: const Text(
          'Back to Home',
          style: TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.w900,
            color: Color(0xFF3B466A),
          ),
        ),
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.white,
          foregroundColor: const Color(0xFF3B466A),
          elevation: 6,
          shadowColor: const Color(0x1C3B4E78),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(28),
          ),
        ),
      ),
    );
  }
}

class HomeStatsRow extends StatelessWidget {
  const HomeStatsRow({super.key});

  @override
  Widget build(BuildContext context) {
    return const Row(
      children: [
        Expanded(
          child: HomeStatPill(
            icon: Icons.local_fire_department_rounded,
            iconColor: Color(0xFFFF7A1A),
            label: 'Streak',
            value: '3 Days',
          ),
        ),
        SizedBox(width: 10),
        Expanded(
          child: HomeStatPill(
            icon: Icons.workspace_premium_rounded,
            iconColor: Color(0xFFFFD54A),
            label: 'Best Score',
            value: '250',
          ),
        ),
      ],
    );
  }
}

class HomeStatPill extends StatelessWidget {
  const HomeStatPill({
    super.key,
    required this.icon,
    required this.iconColor,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final Color iconColor;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 52,
      padding: const EdgeInsets.symmetric(horizontal: 12),
      decoration: BoxDecoration(
        color: const Color(0xCC101832),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: const Color(0xFF263B72)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x443D35D8),
            blurRadius: 14,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: Row(
        children: [
          Icon(icon, color: iconColor, size: 22),
          const SizedBox(width: 9),
          Expanded(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                FittedBox(
                  fit: BoxFit.scaleDown,
                  alignment: Alignment.centerLeft,
                  child: Text(
                    label.toUpperCase(),
                    maxLines: 1,
                    style: const TextStyle(
                      fontSize: 10,
                      fontWeight: FontWeight.w800,
                      color: Color(0xFF9AA8D9),
                    ),
                  ),
                ),
                Text(
                  value,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w900,
                    color: Colors.white,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class PuzzleLevel {
  const PuzzleLevel({
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });

  final String question;
  final List<String> options;
  final String correctAnswer;
  final String explanation;
}

List<PuzzleLevel> buildMindTrapPuzzleBank() {
  final puzzles = <PuzzleLevel>[
    const PuzzleLevel(
      question: 'Which word is longest?',
      options: ['Snake', 'Train', 'Road', 'Queue'],
      correctAnswer: 'Queue',
      explanation: 'Queue has five letters, more than the other options.',
    ),
    const PuzzleLevel(
      question: 'What gets wetter while drying?',
      options: ['Towel', 'Sun', 'Fire', 'Sand'],
      correctAnswer: 'Towel',
      explanation: 'A towel absorbs water while drying something else.',
    ),
    const PuzzleLevel(
      question: 'Which month has 28 days?',
      options: ['February', 'January', 'All of them', 'June'],
      correctAnswer: 'All of them',
      explanation: 'Every month has at least 28 days.',
    ),
    const PuzzleLevel(
      question: "What has keys but can't open locks?",
      options: ['Piano', 'Door', 'Car', 'Chest'],
      correctAnswer: 'Piano',
      explanation: 'A piano has musical keys, not lock keys.',
    ),
    const PuzzleLevel(
      question: 'Which number is half of 8?',
      options: ['4', '3', '0', 'Depends'],
      correctAnswer: '4',
      explanation: 'Half of 8 is 4.',
    ),
    const PuzzleLevel(
      question: 'What has a face and two hands but no arms?',
      options: ['Clock', 'Robot', 'Person', 'Mirror'],
      correctAnswer: 'Clock',
      explanation: 'A clock has a face and hands, but no arms.',
    ),
    const PuzzleLevel(
      question: 'What stays in a corner while traveling?',
      options: ['Stamp', 'Plane', 'Map', 'Compass'],
      correctAnswer: 'Stamp',
      explanation: 'A stamp stays on the corner of a traveling envelope.',
    ),
    const PuzzleLevel(
      question: 'In a dark room, what do you light first?',
      options: ['Candle', 'Lamp', 'Match', 'Fireplace'],
      correctAnswer: 'Match',
      explanation: 'You must light the match before lighting anything else.',
    ),
    const PuzzleLevel(
      question: 'What has many teeth but cannot bite?',
      options: ['Comb', 'Shark', 'Saw', 'Zipper'],
      correctAnswer: 'Comb',
      explanation: 'A comb has teeth, but they are not for biting.',
    ),
    const PuzzleLevel(
      question: 'What goes up but never comes down?',
      options: ['Age', 'Balloon', 'Smoke', 'Elevator'],
      correctAnswer: 'Age',
      explanation: 'Your age increases as time passes.',
    ),
    const PuzzleLevel(
      question: 'Which is heavier?',
      options: ['1 kg feathers', '1 kg rocks', 'Rocks', 'Feathers'],
      correctAnswer: '1 kg feathers',
      explanation: 'Both weigh 1 kg, so the named 1 kg option is correct.',
    ),
    const PuzzleLevel(
      question: 'What has one eye but cannot see?',
      options: ['Needle', 'Cyclops', 'Camera', 'Storm'],
      correctAnswer: 'Needle',
      explanation: 'A needle has an eye for thread.',
    ),
    const PuzzleLevel(
      question: 'What can you catch but not throw?',
      options: ['Cold', 'Ball', 'Fish', 'Frisbee'],
      correctAnswer: 'Cold',
      explanation: 'You can catch a cold, but you cannot throw it.',
    ),
    const PuzzleLevel(
      question: 'What has a neck but no head?',
      options: ['Bottle', 'Giraffe', 'Shirt', 'Guitar'],
      correctAnswer: 'Bottle',
      explanation: 'A bottle has a neck but no head.',
    ),
    const PuzzleLevel(
      question: 'Which word gets shorter when letters are added?',
      options: ['Short', 'Small', 'Tiny', 'Long'],
      correctAnswer: 'Short',
      explanation: 'Adding "er" to short makes "shorter".',
    ),
    const PuzzleLevel(
      question: 'What appears once in minute and twice in moment?',
      options: ['M', 'Time', 'Second', 'Memory'],
      correctAnswer: 'M',
      explanation: 'The letter M appears once in minute and twice in moment.',
    ),
    const PuzzleLevel(
      question: 'Which one is not a fruit?',
      options: ['Grape', 'Potato', 'Peach', 'Orange'],
      correctAnswer: 'Potato',
      explanation: 'Potato is a vegetable, not a fruit.',
    ),
    const PuzzleLevel(
      question: 'What comes next: 2, 4, 6, ?',
      options: ['7', '8', '9', '10'],
      correctAnswer: '8',
      explanation: 'The sequence adds 2 each time.',
    ),
    const PuzzleLevel(
      question: 'What has hands but cannot clap?',
      options: ['Clock', 'Baby', 'Robot', 'Gloves'],
      correctAnswer: 'Clock',
      explanation: 'A clock has hands that show time.',
    ),
    const PuzzleLevel(
      question: 'What is full of holes but holds water?',
      options: ['Sponge', 'Bucket', 'Net', 'Cup'],
      correctAnswer: 'Sponge',
      explanation: 'A sponge has holes and still absorbs water.',
    ),
    const PuzzleLevel(
      question: 'What comes next: A, C, E, ?',
      options: ['F', 'G', 'H', 'I'],
      correctAnswer: 'G',
      explanation: 'The pattern skips one letter each time.',
    ),
    const PuzzleLevel(
      question: 'What is in front of you but unseen?',
      options: ['Future', 'Air', 'Nose', 'Shadow'],
      correctAnswer: 'Future',
      explanation: 'The future is ahead, but cannot be seen yet.',
    ),
    const PuzzleLevel(
      question: 'Which one is a planet?',
      options: ['Moon', 'Mars', 'Sun', 'Comet'],
      correctAnswer: 'Mars',
      explanation: 'Mars is a planet.',
    ),
    const PuzzleLevel(
      question: 'What breaks when you say its name?',
      options: ['Silence', 'Glass', 'Promise', 'Code'],
      correctAnswer: 'Silence',
      explanation: 'Saying anything ends silence.',
    ),
    const PuzzleLevel(
      question: 'I speak without a mouth and hear without ears. What am I?',
      options: ['Echo', 'Shadow', 'Whistle', 'Radio'],
      correctAnswer: 'Echo',
      explanation: 'An echo repeats sound without having a body or mouth.',
    ),
    const PuzzleLevel(
      question: 'A boat is full of people, yet not a single person is on board. Why?',
      options: ['All were married', 'They jumped', 'Ghost ship', 'They left'],
      correctAnswer: 'All were married',
      explanation: 'None of them were single—they were all married.',
    ),
    const PuzzleLevel(
      question: 'The person who makes it does not want it. The buyer does not use it. What is it?',
      options: ['Coffin', 'Anchor', 'Medicine', 'Parachute'],
      correctAnswer: 'Coffin',
      explanation: 'A coffin is made for someone else, bought by relatives, and used by the deceased.',
    ),
    const PuzzleLevel(
      question: 'A cowboy rides into town on Friday, stays 2 days, and leaves on Friday. How?',
      options: ['Horse named Friday', 'Time travel', 'Stayed a week', 'Calendar error'],
      correctAnswer: 'Horse named Friday',
      explanation: 'His horse is named Friday.',
    ),
    const PuzzleLevel(
      question: 'What runs around the entire yard without ever moving?',
      options: ['A fence', 'A dog', 'The wind', 'Grass'],
      correctAnswer: 'A fence',
      explanation: 'A fence borders the whole yard while standing completely still.',
    ),
    const PuzzleLevel(
      question: 'What begins with T, finishes with T, and has T inside it?',
      options: ['A teapot', 'Tent', 'Toast', 'Target'],
      correctAnswer: 'A teapot',
      explanation: 'A teapot starts and ends with T and contains tea inside.',
    ),
    const PuzzleLevel(
      question: 'How many letters are in "the alphabet"?',
      options: ['11', '26', '24', '10'],
      correctAnswer: '11',
      explanation: 'The phrase "the alphabet" contains exactly 11 letters.',
    ),
    const PuzzleLevel(
      question: 'What has a head and a tail, but no body?',
      options: ['A coin', 'A snake', 'A comet', 'A lizard'],
      correctAnswer: 'A coin',
      explanation: 'A coin has heads and tails on its two sides.',
    ),
    const PuzzleLevel(
      question: 'What belongs to you, but others use it far more than you do?',
      options: ['Your name', 'Your money', 'Your shoes', 'Your phone'],
      correctAnswer: 'Your name',
      explanation: 'Other people call you by your name more than you say it yourself.',
    ),
    const PuzzleLevel(
      question: 'What has words, but never speaks?',
      options: ['A book', 'A statue', 'An echo', 'A recorder'],
      correctAnswer: 'A book',
      explanation: 'A book contains printed words but has no voice.',
    ),
    const PuzzleLevel(
      question: 'If you drop me I crack, but smile at me and I smile back. What am I?',
      options: ['A mirror', 'An egg', 'A picture', 'A glass'],
      correctAnswer: 'A mirror',
      explanation: 'A mirror reflects your smile back and cracks if dropped.',
    ),
    const PuzzleLevel(
      question: 'What can fill an entire room without taking up any physical space?',
      options: ['Light', 'Air', 'Sound', 'Smoke'],
      correctAnswer: 'Light',
      explanation: 'Light illuminates the whole room without occupying volume.',
    ),
    const PuzzleLevel(
      question: 'What has cities but no houses, and rivers but no water?',
      options: ['A map', 'A globe', 'A painting', 'A desert'],
      correctAnswer: 'A map',
      explanation: 'A map depicts cities, mountains, and rivers symbolically.',
    ),
    const PuzzleLevel(
      question: 'The more there is of this, the less you can see. What is it?',
      options: ['Darkness', 'Fog', 'Light', 'Rain'],
      correctAnswer: 'Darkness',
      explanation: 'As darkness increases, visibility decreases.',
    ),
    const PuzzleLevel(
      question: 'I have branches, but no fruit, trunk, or leaves. What am I?',
      options: ['A bank', 'A river', 'A tree', 'A road'],
      correctAnswer: 'A bank',
      explanation: 'A financial bank has branches in different locations.',
    ),
    const PuzzleLevel(
      question: 'What can you break without ever touching or dropping it?',
      options: ['A promise', 'A glass', 'A heart', 'A stick'],
      correctAnswer: 'A promise',
      explanation: 'A promise can be broken simply by not keeping your word.',
    ),
    const PuzzleLevel(
      question: 'What architectural invention allows you to look right through a wall?',
      options: ['A window', 'A telescope', 'X-ray', 'A mirror'],
      correctAnswer: 'A window',
      explanation: 'A window is built into a wall allowing vision through it.',
    ),
    const PuzzleLevel(
      question: 'If two is company, and three is a crowd, what are four and five?',
      options: ['Nine', 'A party', 'A mob', 'Seven'],
      correctAnswer: 'Nine',
      explanation: 'Four plus five equals nine.',
    ),
    const PuzzleLevel(
      question: 'What goes up and down constantly but never moves an inch?',
      options: ['Stairs', 'Elevator', 'Thermometer', 'Seesaw'],
      correctAnswer: 'Stairs',
      explanation: 'Stairs lead both up and down while staying fixed.',
    ),
    const PuzzleLevel(
      question: 'Feed me and I live, but give me a drink of water and I die. What am I?',
      options: ['Fire', 'Ice', 'Fish', 'Plant'],
      correctAnswer: 'Fire',
      explanation: 'Fire feeds on wood/fuel, but water extinguishes it.',
    ),
    const PuzzleLevel(
      question: 'What has to be broken before you can ever use it?',
      options: ['An egg', 'A nut', 'A glowstick', 'A bottle'],
      correctAnswer: 'An egg',
      explanation: 'An eggshell must be broken to cook or bake with it.',
    ),
    const PuzzleLevel(
      question: 'I am tall when I am young, and short when I am old. What am I?',
      options: ['A candle', 'A pencil', 'A tree', 'A human'],
      correctAnswer: 'A candle',
      explanation: 'A candle melts down and gets shorter as it burns over time.',
    ),
    const PuzzleLevel(
      question: 'What begins with an E and contains only one single letter?',
      options: ['An envelope', 'Eye', 'Echo', 'Egg'],
      correctAnswer: 'An envelope',
      explanation: 'An envelope starts with E and contains a letter inside.',
    ),
    const PuzzleLevel(
      question: 'A man pushes his car to a hotel and immediately declares bankruptcy. Why?',
      options: ['Playing Monopoly', 'Car broke down', 'Hotel was pricey', 'Lost his wallet'],
      correctAnswer: 'Playing Monopoly',
      explanation: 'He landed on a hotel tile in the board game Monopoly.',
    ),
    const PuzzleLevel(
      question: 'How can a person go 25 days without sleeping?',
      options: ['Sleeps at night', 'Drinks coffee', 'Daydreams', 'Impossible'],
      correctAnswer: 'Sleeps at night',
      explanation: 'They stay awake during the day and sleep normally at night.',
    ),
    const PuzzleLevel(
      question: 'What comes down from the sky but never goes back up?',
      options: ['Rain', 'Snow', 'Temperature', 'Smoke'],
      correctAnswer: 'Rain',
      explanation: 'Rain falls down as precipitation.',
    ),
    const PuzzleLevel(
      question: 'Where does today always come before yesterday?',
      options: ['In a dictionary', 'In a calendar', 'In a timeline', 'In history'],
      correctAnswer: 'In a dictionary',
      explanation: 'In alphabetical order, T comes before Y in the dictionary.',
    ),
    const PuzzleLevel(
      question: 'What can you hold in your right hand, but never in your left hand?',
      options: ['Your left hand', 'Your right hand', 'Your elbow', 'A pen'],
      correctAnswer: 'Your left hand',
      explanation: 'You cannot hold your left hand with your left hand.',
    ),
    const PuzzleLevel(
      question: 'What has legs, but cannot take a single step?',
      options: ['A table', 'A chair', 'A clock', 'A bed'],
      correctAnswer: 'A table',
      explanation: 'A dining or study table has four legs for support.',
    ),
    const PuzzleLevel(
      question: 'What has a thumb and four fingers, but is not alive or human?',
      options: ['A glove', 'A mitten', 'A robot', 'A puppet'],
      correctAnswer: 'A glove',
      explanation: 'A glove is shaped like a hand with fingers and a thumb.',
    ),
    const PuzzleLevel(
      question: 'If an electric train travels north at 60 mph, which way does the smoke blow?',
      options: ['No smoke', 'South', 'North', 'West'],
      correctAnswer: 'No smoke',
      explanation: 'An electric train produces no smoke.',
    ),
    const PuzzleLevel(
      question: 'What gets sharper the more you train and challenge it?',
      options: ['Your brain', 'A knife', 'A pencil', 'A saw'],
      correctAnswer: 'Your brain',
      explanation: 'Mental exercise and puzzles sharpen cognitive acuity.',
    ),
    const PuzzleLevel(
      question: '2 fathers and 2 sons caught 3 fish, 1 each. How is this possible?',
      options: ['Grandfather, father, son', 'One fish jumped', 'One cheated', 'Shared'],
      correctAnswer: 'Grandfather, father, son',
      explanation: 'There were only 3 people: a grandfather, his son, and his grandson.',
    ),
    const PuzzleLevel(
      question: 'What runs constantly without walking, and has a bed but never sleeps?',
      options: ['A river', 'A clock', 'A car', 'A shoe'],
      correctAnswer: 'A river',
      explanation: 'A river runs along a riverbed.',
    ),
    const PuzzleLevel(
      question: 'What kind of band never plays musical instruments?',
      options: ['A rubber band', 'A headband', 'A rock band', 'A jazz band'],
      correctAnswer: 'A rubber band',
      explanation: 'A rubber band is an elastic loop, not a musical group.',
    ),
    const PuzzleLevel(
      question: 'Which word in every standard English dictionary is spelled incorrectly?',
      options: ['Incorrectly', 'Wrong', 'Misspelled', 'None'],
      correctAnswer: 'Incorrectly',
      explanation: 'The word "incorrectly" is spelled I-N-C-O-R-R-E-C-T-L-Y.',
    ),
    const PuzzleLevel(
      question: 'A plane crashes on the exact border of US and Canada. Where are survivors buried?',
      options: ['Survivors aren’t buried', 'In the US', 'In Canada', 'On border'],
      correctAnswer: 'Survivors aren’t buried',
      explanation: 'You never bury people who survived.',
    ),
    const PuzzleLevel(
      question: 'What body part tastes food much better than it smells?',
      options: ['Your tongue', 'Chocolate', 'Coffee', 'Vanilla'],
      correctAnswer: 'Your tongue',
      explanation: 'Your tongue does the tasting, while your nose does the smelling.',
    ),
    const PuzzleLevel(
      question: 'What object has a spine, but has absolutely no bones inside?',
      options: ['A book', 'A jellyfish', 'A worm', 'A cactus'],
      correctAnswer: 'A book',
      explanation: 'The binding edge of a book is called its spine.',
    ),
    const PuzzleLevel(
      question: 'What household item loses its head in the morning and gets it back at night?',
      options: ['A pillow', 'A coin', 'A bed', 'A hat'],
      correctAnswer: 'A pillow',
      explanation: 'You lay your head on the pillow at night and remove it in the morning.',
    ),
    const PuzzleLevel(
      question: 'What celestial or household item has rings, but no fingers?',
      options: ['A telephone', 'Saturn', 'A tree', 'A binder'],
      correctAnswer: 'A telephone',
      explanation: 'A traditional telephone rings when receiving a call.',
    ),
    const PuzzleLevel(
      question: 'I am full of holes, yet I can hold water securely. What am I?',
      options: ['A sponge', 'A sieve', 'A net', 'A colander'],
      correctAnswer: 'A sponge',
      explanation: 'A sponge is porous with holes, yet absorbs and holds water.',
    ),
  ];

  puzzles
    ..addAll(_buildOddOneOutPuzzles())
    ..addAll(_buildNotCategoryPuzzles())
    ..addAll(_buildLetterCountPuzzles())
    ..addAll(_buildNumberSequencePuzzles())
    ..addAll(_buildLetterSequencePuzzles())
    ..addAll(_buildReverseLogicPuzzles())
    ..addAll(_literalTrapPuzzles);

  final unique = _dedupePuzzleBank(puzzles);
  assert(unique.length >= 500, 'Puzzle bank must contain at least 500 puzzles');
  return List.unmodifiable(unique);
}

List<PuzzleLevel> _dedupePuzzleBank(List<PuzzleLevel> puzzles) {
  final seen = <String>{};
  final unique = <PuzzleLevel>[];

  for (final puzzle in puzzles) {
    final key = puzzle.question.trim().toLowerCase();
    if (seen.add(key)) {
      unique.add(puzzle);
    }
  }

  return unique;
}

PuzzleLevel _puzzle({
  required String question,
  required List<String> options,
  required String correctAnswer,
  required String explanation,
}) {
  return PuzzleLevel(
    question: question,
    options: List.unmodifiable(options),
    correctAnswer: correctAnswer,
    explanation: explanation,
  );
}

List<String> _orderedOptions(List<String> options, int seed) {
  final ordered = List<String>.from(options);

  for (var index = 0; index < ordered.length; index++) {
    final swapIndex = (seed + (index * 2)) % ordered.length;
    final temp = ordered[index];
    ordered[index] = ordered[swapIndex];
    ordered[swapIndex] = temp;
  }

  return ordered;
}

List<PuzzleLevel> _buildOddOneOutPuzzles() {
  const prompts = [
    'Which one does not belong?',
    'Find the odd one out.',
    'Which option breaks the group?',
    'Which word is the outsider?',
    'Which choice is unlike the others?',
    'Which option is the mismatch?',
  ];
  final categories = _mindTrapCategories.entries.toList();
  final puzzles = <PuzzleLevel>[];

  for (
    var categoryIndex = 0;
    categoryIndex < categories.length;
    categoryIndex++
  ) {
    final base = categories[categoryIndex];
    final odd = categories[(categoryIndex + 7) % categories.length];
    final baseItems = base.value;
    final oddItems = odd.value;

    for (var turn = 0; turn < baseItems.length; turn++) {
      final correct = oddItems[(turn + categoryIndex) % oddItems.length];
      final options = [
        baseItems[turn % baseItems.length],
        baseItems[(turn + 2) % baseItems.length],
        baseItems[(turn + 4) % baseItems.length],
        correct,
      ];
      puzzles.add(
        _puzzle(
          question:
              '${prompts[(categoryIndex + turn) % prompts.length]} '
              '${options.join(', ')}',
          options: _orderedOptions(options, categoryIndex + turn),
          correctAnswer: correct,
          explanation:
              '$correct is the only ${odd.key}; the others are ${base.key}.',
        ),
      );
    }
  }

  return puzzles;
}

List<PuzzleLevel> _buildNotCategoryPuzzles() {
  final categories = _mindTrapCategories.entries.toList();
  final puzzles = <PuzzleLevel>[];

  for (var index = 0; index < categories.length; index++) {
    final base = categories[index];
    final odd = categories[(index + 11) % categories.length];
    final baseItems = base.value;
    final oddItems = odd.value;

    for (var turn = 0; turn < 3; turn++) {
      final correct = oddItems[(index + turn) % oddItems.length];
      final options = [
        baseItems[(turn + 1) % baseItems.length],
        correct,
        baseItems[(turn + 3) % baseItems.length],
        baseItems[(turn + 5) % baseItems.length],
      ];
      puzzles.add(
        _puzzle(
          question: 'Which option is not one of the ${base.key}?',
          options: _orderedOptions(options, index + turn + 31),
          correctAnswer: correct,
          explanation: '$correct belongs to ${odd.key}, not ${base.key}.',
        ),
      );
    }
  }

  return puzzles;
}

List<PuzzleLevel> _buildLetterCountPuzzles() {
  const prompts = [
    'Which word has exactly',
    'Pick the word with',
    'Which option contains',
    'Find the word with',
  ];
  final byLength = <int, List<String>>{};

  for (final word in _letterTrapWords) {
    byLength.putIfAbsent(word.length, () => <String>[]).add(word);
  }

  final lengths =
      byLength.keys.where((length) => byLength[length]!.length > 3).toList()
        ..sort();
  final puzzles = <PuzzleLevel>[];

  for (
    var index = 0;
    index < _letterTrapWords.length && puzzles.length < 130;
    index++
  ) {
    final correct = _letterTrapWords[index];
    final targetLength = correct.length;
    if (!lengths.contains(targetLength)) {
      continue;
    }

    final distractorLengths = lengths
        .where((length) => length != targetLength)
        .toList();
    final options = <String>[correct];
    for (var offset = 0; options.length < 4; offset++) {
      final length =
          distractorLengths[(index + offset) % distractorLengths.length];
      final word =
          byLength[length]![(index + offset) % byLength[length]!.length];
      if (!options.contains(word)) {
        options.add(word);
      }
    }

    final plural = targetLength == 1 ? 'letter' : 'letters';
    puzzles.add(
      _puzzle(
        question: '${prompts[index % prompts.length]} $targetLength $plural?',
        options: _orderedOptions(options, index + 71),
        correctAnswer: correct,
        explanation: '$correct has $targetLength $plural.',
      ),
    );
  }

  return puzzles;
}

List<PuzzleLevel> _buildNumberSequencePuzzles() {
  final puzzles = <PuzzleLevel>[];

  for (var index = 0; index < 90; index++) {
    final start = (index % 12) + 1;
    final step = (index % 7) + 2;
    final first = start;
    final second = start + step;
    final third = start + (step * 2);
    final correct = start + (step * 3);
    final options = [
      '$correct',
      '${correct + step}',
      '${correct - 1}',
      '${correct + 1}',
    ];
    puzzles.add(
      _puzzle(
        question: 'What comes next: $first, $second, $third, ?',
        options: _orderedOptions(options, index + 103),
        correctAnswer: '$correct',
        explanation: 'The sequence adds $step each time.',
      ),
    );
  }

  for (var index = 0; index < 50; index++) {
    final start = (index % 8) + 2;
    final first = start;
    final second = start * 2;
    final third = start * 4;
    final correct = start * 8;
    final options = [
      '$correct',
      '${correct ~/ 2}',
      '${correct + start}',
      '${correct - start}',
    ];
    puzzles.add(
      _puzzle(
        question: 'What comes next: $first, $second, $third, ?',
        options: _orderedOptions(options, index + 211),
        correctAnswer: '$correct',
        explanation: 'Each number doubles.',
      ),
    );
  }

  return puzzles;
}

List<PuzzleLevel> _buildLetterSequencePuzzles() {
  const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  final puzzles = <PuzzleLevel>[];

  for (var index = 0; index < 70; index++) {
    final step = (index % 4) + 1;
    final start = index % (letters.length - (step * 4));
    final first = letters[start];
    final second = letters[start + step];
    final third = letters[start + (step * 2)];
    final correct = letters[start + (step * 3)];
    final options = [
      correct,
      letters[start + (step * 3) + 1],
      letters[start + (step * 2) + 1],
      letters[start + step + 1],
    ];
    puzzles.add(
      _puzzle(
        question: 'Which letter comes next: $first, $second, $third, ?',
        options: _orderedOptions(options, index + 307),
        correctAnswer: correct,
        explanation:
            'The pattern skips $step letter${step == 1 ? '' : 's'} each time.',
      ),
    );
  }

  return puzzles;
}

List<PuzzleLevel> _buildReverseLogicPuzzles() {
  final puzzles = <PuzzleLevel>[];

  for (var index = 0; index < _reverseLogicFacts.length; index++) {
    final fact = _reverseLogicFacts[index];
    puzzles.add(
      _puzzle(
        question: fact.question,
        options: _orderedOptions(fact.options, index + 409),
        correctAnswer: fact.correctAnswer,
        explanation: fact.explanation,
      ),
    );
  }

  return puzzles;
}

class _ReverseLogicFact {
  const _ReverseLogicFact({
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });

  final String question;
  final List<String> options;
  final String correctAnswer;
  final String explanation;
}

const Map<String, List<String>> _mindTrapCategories = {
  'fruits': ['Apple', 'Mango', 'Peach', 'Grape', 'Pear', 'Banana'],
  'vegetables': ['Carrot', 'Potato', 'Onion', 'Spinach', 'Cabbage', 'Pea'],
  'planets': ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Mercury', 'Neptune'],
  'weekdays': [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Sunday',
  ],
  'months': ['January', 'March', 'April', 'June', 'August', 'October'],
  'colors': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange'],
  'shapes': ['Circle', 'Square', 'Triangle', 'Oval', 'Cube', 'Star'],
  'tools': ['Hammer', 'Saw', 'Drill', 'Wrench', 'Chisel', 'Pliers'],
  'vehicles': ['Car', 'Bus', 'Train', 'Truck', 'Bicycle', 'Scooter'],
  'birds': ['Eagle', 'Sparrow', 'Pigeon', 'Falcon', 'Parrot', 'Owl'],
  'fish': ['Salmon', 'Tuna', 'Carp', 'Trout', 'Cod', 'Herring'],
  'insects': ['Ant', 'Bee', 'Moth', 'Beetle', 'Wasp', 'Fly'],
  'body parts': ['Hand', 'Foot', 'Elbow', 'Knee', 'Nose', 'Ear'],
  'clothes': ['Shirt', 'Jacket', 'Coat', 'Scarf', 'Glove', 'Sock'],
  'furniture': ['Chair', 'Table', 'Sofa', 'Desk', 'Stool', 'Shelf'],
  'kitchen items': ['Spoon', 'Plate', 'Cup', 'Bowl', 'Fork', 'Pan'],
  'school items': ['Pencil', 'Eraser', 'Notebook', 'Ruler', 'Marker', 'Bag'],
  'sports': ['Tennis', 'Cricket', 'Hockey', 'Golf', 'Boxing', 'Rugby'],
  'instruments': ['Piano', 'Violin', 'Guitar', 'Drum', 'Flute', 'Trumpet'],
  'weather words': ['Rain', 'Snow', 'Wind', 'Cloud', 'Storm', 'Fog'],
  'metals': ['Gold', 'Silver', 'Copper', 'Iron', 'Tin', 'Zinc'],
  'gems': ['Ruby', 'Emerald', 'Sapphire', 'Opal', 'Pearl', 'Topaz'],
  'drinks': ['Water', 'Tea', 'Coffee', 'Juice', 'Milk', 'Soda'],
  'rooms': ['Kitchen', 'Bedroom', 'Bathroom', 'Office', 'Garage', 'Hall'],
  'jobs': ['Doctor', 'Teacher', 'Pilot', 'Chef', 'Nurse', 'Judge'],
  'devices': ['Phone', 'Tablet', 'Laptop', 'Camera', 'Printer', 'Router'],
  'directions': ['North', 'South', 'East', 'West', 'Left', 'Right'],
  'time units': ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Year'],
  'containers': ['Bottle', 'Jar', 'Box', 'Bucket', 'Bag', 'Crate'],
  'writing marks': ['Comma', 'Period', 'Colon', 'Hyphen', 'Apostrophe', 'Dash'],
  'board games': [
    'Chess',
    'Ludo',
    'Checkers',
    'Scrabble',
    'Monopoly',
    'Carrom',
  ],
  'materials': ['Wood', 'Glass', 'Plastic', 'Paper', 'Cotton', 'Rubber'],
  'natural places': [
    'River',
    'Mountain',
    'Forest',
    'Desert',
    'Valley',
    'Island',
  ],
  'computer terms': ['Mouse', 'Keyboard', 'Screen', 'Folder', 'File', 'Cursor'],
};

const List<String> _letterTrapWords = [
  'ant',
  'bee',
  'cat',
  'dog',
  'egg',
  'fan',
  'gem',
  'hat',
  'ice',
  'jar',
  'key',
  'log',
  'map',
  'net',
  'owl',
  'pen',
  'quiz',
  'ring',
  'star',
  'tree',
  'vase',
  'wave',
  'yard',
  'zest',
  'apple',
  'brain',
  'clock',
  'dream',
  'flame',
  'grape',
  'house',
  'ivory',
  'jelly',
  'knife',
  'lemon',
  'magic',
  'night',
  'ocean',
  'piano',
  'queen',
  'river',
  'stone',
  'table',
  'unity',
  'voice',
  'water',
  'zebra',
  'anchor',
  'bottle',
  'candle',
  'dragon',
  'engine',
  'forest',
  'garden',
  'hammer',
  'island',
  'jacket',
  'kitten',
  'ladder',
  'mirror',
  'needle',
  'orange',
  'planet',
  'rocket',
  'silver',
  'ticket',
  'window',
  'yellow',
  'blanket',
  'crystal',
  'diamond',
  'emerald',
  'feather',
  'gateway',
  'harvest',
  'journey',
  'kingdom',
  'lantern',
  'mystery',
  'notebook',
  'octagon',
  'picture',
  'question',
  'rainbow',
  'sandwich',
  'treasure',
  'umbrella',
  'velocity',
  'whisper',
  'xylophone',
  'backpack',
  'calendar',
  'doorbell',
  'elephant',
  'football',
  'goldfish',
  'hospital',
  'internet',
  'kangaroo',
  'language',
  'mountain',
  'necklace',
  'painting',
  'sandpaper',
  'telephone',
  'universe',
  'waterfall',
  'crossword',
  'flashlight',
  'microphone',
  'strawberry',
  'skyscraper',
  'watermelon',
  'conversation',
  'imagination',
  'temperature',
  'responsibility',
];

const List<_ReverseLogicFact> _reverseLogicFacts = [
  _ReverseLogicFact(
    question: 'Which option is always even?',
    options: ['Two', 'Seven', 'Nine', 'Eleven'],
    correctAnswer: 'Two',
    explanation: 'Two is the only even number listed.',
  ),
  _ReverseLogicFact(
    question: 'Which option is not alive?',
    options: ['Tree', 'Flower', 'Stone', 'Grass'],
    correctAnswer: 'Stone',
    explanation: 'A stone is not a living thing.',
  ),
  _ReverseLogicFact(
    question: 'Which word has no letter A?',
    options: ['Plane', 'Table', 'Cloud', 'Chair'],
    correctAnswer: 'Cloud',
    explanation: 'Cloud is the only option without A.',
  ),
  _ReverseLogicFact(
    question: 'Which option can be empty and full?',
    options: ['Glass', 'Plate', 'Wall', 'Stone'],
    correctAnswer: 'Glass',
    explanation: 'A glass can be empty or full.',
  ),
  _ReverseLogicFact(
    question: 'Which option can run but has no legs?',
    options: ['Water', 'Horse', 'Runner', 'Dog'],
    correctAnswer: 'Water',
    explanation: 'Water can run as a stream.',
  ),
  _ReverseLogicFact(
    question: 'Which one gets sharper by losing part of itself?',
    options: ['Pencil', 'Spoon', 'Book', 'Window'],
    correctAnswer: 'Pencil',
    explanation: 'A pencil gets sharpened as wood is shaved away.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be cracked but not eaten?',
    options: ['Code', 'Egg', 'Nut', 'Cookie'],
    correctAnswer: 'Code',
    explanation: 'Code can be cracked as a puzzle or password.',
  ),
  _ReverseLogicFact(
    question: 'Which one has a bark but no bite?',
    options: ['Tree', 'Dog', 'Wolf', 'Fox'],
    correctAnswer: 'Tree',
    explanation: 'Tree bark is not an animal bite.',
  ),
  _ReverseLogicFact(
    question: 'Which one has a ring but no finger?',
    options: ['Phone', 'Hand', 'Glove', 'Bracelet'],
    correctAnswer: 'Phone',
    explanation: 'A phone can ring without having fingers.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be drawn but not pulled?',
    options: ['Picture', 'Rope', 'Curtain', 'Cart'],
    correctAnswer: 'Picture',
    explanation: 'A picture can be drawn with a pencil.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be read without pages?',
    options: ['Clock', 'Book', 'Magazine', 'Novel'],
    correctAnswer: 'Clock',
    explanation: 'You can read the time from a clock.',
  ),
  _ReverseLogicFact(
    question: 'Which one can hold a line?',
    options: ['Queue', 'Cup', 'Plate', 'Basket'],
    correctAnswer: 'Queue',
    explanation: 'A queue is a line of people.',
  ),
  _ReverseLogicFact(
    question: 'Which one is a word and a direction?',
    options: ['Right', 'Bright', 'Tight', 'Light'],
    correctAnswer: 'Right',
    explanation: 'Right can mean correct and a direction.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be high but not tall?',
    options: ['Score', 'Tower', 'Tree', 'Ladder'],
    correctAnswer: 'Score',
    explanation: 'A score can be high without physical height.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be missed without moving?',
    options: ['Chance', 'Bus', 'Train', 'Arrow'],
    correctAnswer: 'Chance',
    explanation: 'You can miss a chance while standing still.',
  ),
  _ReverseLogicFact(
    question: 'Which one can open without hands?',
    options: ['Doorbell', 'Flower', 'Lock', 'Box'],
    correctAnswer: 'Flower',
    explanation: 'A flower opens as it blooms.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be broken by a promise?',
    options: ['Trust', 'Glass', 'Plate', 'Stick'],
    correctAnswer: 'Trust',
    explanation: 'Breaking a promise can break trust.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be raised but not lifted?',
    options: ['Question', 'Chair', 'Stone', 'Box'],
    correctAnswer: 'Question',
    explanation: 'You can raise a question in discussion.',
  ),
  _ReverseLogicFact(
    question: 'Which one has a head but no brain?',
    options: ['Nail', 'Person', 'Teacher', 'Bird'],
    correctAnswer: 'Nail',
    explanation: 'A nail has a head but no brain.',
  ),
  _ReverseLogicFact(
    question: 'Which one has feet but no shoes?',
    options: ['Table', 'Runner', 'Baby', 'Dancer'],
    correctAnswer: 'Table',
    explanation: 'A table can have feet but wears no shoes.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be right but not correct?',
    options: ['Direction', 'Answer', 'Solution', 'Reply'],
    correctAnswer: 'Direction',
    explanation: 'Right can mean the direction, not correctness.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be light but not bright?',
    options: ['Feather', 'Bulb', 'Lamp', 'Torch'],
    correctAnswer: 'Feather',
    explanation: 'A feather is light in weight.',
  ),
  _ReverseLogicFact(
    question: 'Which one has letters but is not a word?',
    options: ['Mailbox', 'Poem', 'Sentence', 'Title'],
    correctAnswer: 'Mailbox',
    explanation: 'A mailbox can contain letters.',
  ),
  _ReverseLogicFact(
    question: 'Which one can fly without wings?',
    options: ['Time', 'Bird', 'Plane', 'Butterfly'],
    correctAnswer: 'Time',
    explanation: 'Time can fly as an expression.',
  ),
  _ReverseLogicFact(
    question: 'Which one gets bigger when more is taken?',
    options: ['Hole', 'Pile', 'Box', 'Bag'],
    correctAnswer: 'Hole',
    explanation: 'A hole grows bigger when more material is removed.',
  ),
  _ReverseLogicFact(
    question: 'Which one is made by breaking silence?',
    options: ['Sound', 'Sleep', 'Shadow', 'Stone'],
    correctAnswer: 'Sound',
    explanation: 'A sound breaks silence.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be crossed without walking?',
    options: ['Letter T', 'Road', 'Bridge', 'Field'],
    correctAnswer: 'Letter T',
    explanation: 'The letter T is crossed with a line.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be folded but not laundry?',
    options: ['Arms', 'Shirt', 'Socks', 'Towel'],
    correctAnswer: 'Arms',
    explanation: 'You can fold your arms.',
  ),
  _ReverseLogicFact(
    question: 'Which one can be counted but not touched?',
    options: ['Idea', 'Coin', 'Apple', 'Chair'],
    correctAnswer: 'Idea',
    explanation: 'Ideas can be counted, but they are not physical objects.',
  ),
  _ReverseLogicFact(
    question: 'Which one is loudest in silence?',
    options: ['Thought', 'Drum', 'Bell', 'Horn'],
    correctAnswer: 'Thought',
    explanation: 'A thought can feel loud when everything is quiet.',
  ),
];

const List<PuzzleLevel> _literalTrapPuzzles = [
  PuzzleLevel(
    question: 'How many birthdays does one person have?',
    options: ['One', 'Every year', 'Twelve', 'None'],
    correctAnswer: 'One',
    explanation: 'A person is born on one day; anniversaries repeat yearly.',
  ),
  PuzzleLevel(
    question: 'What can fill a room but takes no space?',
    options: ['Light', 'Water', 'Smoke', 'Furniture'],
    correctAnswer: 'Light',
    explanation: 'Light fills a room without occupying physical space.',
  ),
  PuzzleLevel(
    question: 'What is easy to lift but hard to throw?',
    options: ['Feather', 'Brick', 'Stone', 'Chair'],
    correctAnswer: 'Feather',
    explanation: 'A feather is light, but air makes it hard to throw far.',
  ),
  PuzzleLevel(
    question: 'What has cities but no houses?',
    options: ['Map', 'Country', 'Street', 'Village'],
    correctAnswer: 'Map',
    explanation: 'A map shows cities but contains no real houses.',
  ),
  PuzzleLevel(
    question: 'What has roads but no cars?',
    options: ['Map', 'Garage', 'Bridge', 'Tunnel'],
    correctAnswer: 'Map',
    explanation: 'A map shows roads, but cars do not drive on it.',
  ),
  PuzzleLevel(
    question: 'What can be opened but never closed?',
    options: ['An egg', 'A door', 'A book', 'A window'],
    correctAnswer: 'An egg',
    explanation: 'Once an egg is cracked open, it cannot be closed again.',
  ),
  PuzzleLevel(
    question: 'What comes down but never goes up?',
    options: ['Rain', 'Smoke', 'Balloon', 'Age'],
    correctAnswer: 'Rain',
    explanation: 'Rain falls down from clouds.',
  ),
  PuzzleLevel(
    question: 'What has words but never speaks?',
    options: ['Book', 'Teacher', 'Radio', 'Singer'],
    correctAnswer: 'Book',
    explanation: 'A book contains words but cannot speak.',
  ),
  PuzzleLevel(
    question: 'What gets cut but never bleeds?',
    options: ['Paper', 'Finger', 'Knee', 'Apple'],
    correctAnswer: 'Paper',
    explanation: 'Paper can be cut and has no blood.',
  ),
  PuzzleLevel(
    question: 'What can be lost without being owned?',
    options: ['Temper', 'Wallet', 'Phone', 'Key'],
    correctAnswer: 'Temper',
    explanation: 'You can lose your temper as an expression.',
  ),
  PuzzleLevel(
    question: 'What has a bottom at the top?',
    options: ['Leg', 'Bottle', 'Mountain', 'Chair'],
    correctAnswer: 'Leg',
    explanation: 'Your leg has a bottom at the top of your foot.',
  ),
  PuzzleLevel(
    question: 'What can be heard but never touched?',
    options: ['Sound', 'Bell', 'Drum', 'Phone'],
    correctAnswer: 'Sound',
    explanation: 'Sound is heard, not touched.',
  ),
  PuzzleLevel(
    question: 'What belongs to you but others use more?',
    options: ['Your name', 'Your phone', 'Your car', 'Your bag'],
    correctAnswer: 'Your name',
    explanation: 'Other people say your name more than you do.',
  ),
  PuzzleLevel(
    question: 'What has four wheels and flies?',
    options: ['Garbage truck', 'Airplane', 'Car', 'Bike'],
    correctAnswer: 'Garbage truck',
    explanation: 'A garbage truck can have flies around it.',
  ),
  PuzzleLevel(
    question: 'What has a thumb and four fingers but is not alive?',
    options: ['Glove', 'Hand', 'Monkey', 'Robot'],
    correctAnswer: 'Glove',
    explanation: 'A glove has finger shapes but is not alive.',
  ),
  PuzzleLevel(
    question: 'What is black when clean and white when dirty?',
    options: ['Chalkboard', 'Paper', 'Shoe', 'Window'],
    correctAnswer: 'Chalkboard',
    explanation: 'A chalkboard becomes white with chalk dust.',
  ),
  PuzzleLevel(
    question: 'What is always answered without asking?',
    options: ['Phone', 'Question', 'Door', 'Letter'],
    correctAnswer: 'Phone',
    explanation: 'A phone is answered when it rings.',
  ),
  PuzzleLevel(
    question: 'What can you keep after giving it away?',
    options: ['Your word', 'Money', 'Gift', 'Book'],
    correctAnswer: 'Your word',
    explanation: 'You can give and keep your word.',
  ),
  PuzzleLevel(
    question: 'What has no life but can die?',
    options: ['Battery', 'Dog', 'Plant', 'Fish'],
    correctAnswer: 'Battery',
    explanation: 'A battery can die when it loses charge.',
  ),
  PuzzleLevel(
    question: 'What can you break without touching?',
    options: ['Promise', 'Glass', 'Plate', 'Stick'],
    correctAnswer: 'Promise',
    explanation: 'A promise can be broken by not keeping it.',
  ),
  PuzzleLevel(
    question: 'What has a spine but no bones?',
    options: ['Book', 'Fish', 'Person', 'Snake'],
    correctAnswer: 'Book',
    explanation: 'A book has a spine along its cover.',
  ),
  PuzzleLevel(
    question: 'What has a bed but never sleeps?',
    options: ['River', 'Child', 'Cat', 'Guest'],
    correctAnswer: 'River',
    explanation: 'A river has a riverbed.',
  ),
  PuzzleLevel(
    question: 'What has banks but no money?',
    options: ['River', 'Wallet', 'Market', 'Safe'],
    correctAnswer: 'River',
    explanation: 'A river has banks along its sides.',
  ),
  PuzzleLevel(
    question: 'What can be still and running?',
    options: ['Water', 'Clock', 'Car', 'Child'],
    correctAnswer: 'Water',
    explanation: 'Water can be still or running.',
  ),
  PuzzleLevel(
    question: 'What has roots nobody sees?',
    options: ['Mountain', 'Tree', 'Flower', 'Grass'],
    correctAnswer: 'Mountain',
    explanation: 'A mountain can be described as having deep roots.',
  ),
  PuzzleLevel(
    question: 'What has no beginning, middle, or end?',
    options: ['Circle', 'Story', 'Road', 'Book'],
    correctAnswer: 'Circle',
    explanation: 'A circle is continuous.',
  ),
  PuzzleLevel(
    question: 'What can point but has no finger?',
    options: ['Compass', 'Hand', 'Teacher', 'Glove'],
    correctAnswer: 'Compass',
    explanation: 'A compass points directions.',
  ),
  PuzzleLevel(
    question: 'What goes around but stays in place?',
    options: ['Clock hand', 'Car', 'Runner', 'Ball'],
    correctAnswer: 'Clock hand',
    explanation: 'A clock hand rotates around the clock face.',
  ),
  PuzzleLevel(
    question: 'What has a tongue but cannot talk?',
    options: ['Shoe', 'Singer', 'Teacher', 'Child'],
    correctAnswer: 'Shoe',
    explanation: 'A shoe has a tongue part.',
  ),
  PuzzleLevel(
    question: 'What can be clean and dirty at once?',
    options: ['Laundry water', 'Mirror', 'Soap', 'Towel'],
    correctAnswer: 'Laundry water',
    explanation: 'Laundry water can clean clothes while becoming dirty.',
  ),
  PuzzleLevel(
    question: 'What is bought to eat but never eaten?',
    options: ['Plate', 'Bread', 'Rice', 'Apple'],
    correctAnswer: 'Plate',
    explanation: 'A plate is bought for eating from, not eating.',
  ),
  PuzzleLevel(
    question: 'What starts with T, ends with T, and has T?',
    options: ['Teapot', 'Tent', 'Toast', 'Ticket'],
    correctAnswer: 'Teapot',
    explanation: 'Teapot starts and ends with T and holds tea.',
  ),
  PuzzleLevel(
    question: 'What has an end but no start?',
    options: ['Stick', 'Circle', 'Cloud', 'Wind'],
    correctAnswer: 'Stick',
    explanation: 'A stick has ends, even if no marked start.',
  ),
  PuzzleLevel(
    question: 'What can be right, left, and wrong?',
    options: ['Answer', 'Direction', 'Hand', 'Turn'],
    correctAnswer: 'Answer',
    explanation: 'An answer can be right or wrong; left is the trap option.',
  ),
  PuzzleLevel(
    question: 'Which table has no legs?',
    options: ['Timetable', 'Dining table', 'Desk', 'Coffee table'],
    correctAnswer: 'Timetable',
    explanation: 'A timetable is a schedule, not furniture.',
  ),
  PuzzleLevel(
    question: 'Which room has no walls?',
    options: ['Mushroom', 'Bedroom', 'Kitchen', 'Classroom'],
    correctAnswer: 'Mushroom',
    explanation: 'Mushroom contains "room" but has no walls.',
  ),
  PuzzleLevel(
    question: 'Which key opens no door?',
    options: ['Monkey', 'House key', 'Car key', 'Locker key'],
    correctAnswer: 'Monkey',
    explanation: 'Monkey contains "key" but is not a key.',
  ),
  PuzzleLevel(
    question: 'Which star cannot shine?',
    options: ['Starfish', 'North Star', 'Sun', 'Movie star'],
    correctAnswer: 'Starfish',
    explanation: 'A starfish is an animal, not a shining star.',
  ),
  PuzzleLevel(
    question: 'Which date never appears on a calendar?',
    options: ['Blind date', 'Monday', 'January 1', 'Friday'],
    correctAnswer: 'Blind date',
    explanation: 'A blind date is an event, not a calendar date.',
  ),
  PuzzleLevel(
    question: 'Which watch cannot tell time?',
    options: ['Watchdog', 'Wristwatch', 'Smartwatch', 'Clock'],
    correctAnswer: 'Watchdog',
    explanation: 'A watchdog watches, but does not tell time.',
  ),
  PuzzleLevel(
    question: 'Which light is not bright?',
    options: ['Lightweight', 'Sunlight', 'Flashlight', 'Moonlight'],
    correctAnswer: 'Lightweight',
    explanation: 'Lightweight means low weight, not brightness.',
  ),
  PuzzleLevel(
    question: 'Which line can wait?',
    options: ['Queue', 'Straight line', 'Fishing line', 'Underline'],
    correctAnswer: 'Queue',
    explanation: 'A queue is a waiting line.',
  ),
  PuzzleLevel(
    question: 'Which nail is never hammered?',
    options: ['Fingernail', 'Iron nail', 'Wall nail', 'Roof nail'],
    correctAnswer: 'Fingernail',
    explanation: 'A fingernail is part of a finger.',
  ),
  PuzzleLevel(
    question: 'Which band cannot play music?',
    options: ['Rubber band', 'Rock band', 'Jazz band', 'Marching band'],
    correctAnswer: 'Rubber band',
    explanation: 'A rubber band is an object, not musicians.',
  ),
  PuzzleLevel(
    question: 'Which cap cannot be worn?',
    options: ['Bottle cap', 'Baseball cap', 'Winter cap', 'Sun cap'],
    correctAnswer: 'Bottle cap',
    explanation: 'A bottle cap covers a bottle.',
  ),
  PuzzleLevel(
    question: 'Which plant cannot grow?',
    options: ['Power plant', 'Rose plant', 'Mint plant', 'Bean plant'],
    correctAnswer: 'Power plant',
    explanation: 'A power plant produces electricity.',
  ),
  PuzzleLevel(
    question: 'Which spring has no flowers?',
    options: ['Coil spring', 'Spring season', 'Garden spring', 'Warm spring'],
    correctAnswer: 'Coil spring',
    explanation: 'A coil spring is a metal part.',
  ),
  PuzzleLevel(
    question: 'Which mouse hates cheese least?',
    options: ['Computer mouse', 'House mouse', 'Field mouse', 'Cartoon mouse'],
    correctAnswer: 'Computer mouse',
    explanation: 'A computer mouse does not eat.',
  ),
  PuzzleLevel(
    question: 'Which bark belongs to no dog?',
    options: ['Tree bark', 'Loud bark', 'Puppy bark', 'Guard bark'],
    correctAnswer: 'Tree bark',
    explanation: 'Tree bark is part of a tree.',
  ),
  PuzzleLevel(
    question: 'Which seal cannot swim?',
    options: ['Envelope seal', 'Sea seal', 'Baby seal', 'Grey seal'],
    correctAnswer: 'Envelope seal',
    explanation: 'An envelope seal is not an animal.',
  ),
  PuzzleLevel(
    question: 'Which jam is not food?',
    options: ['Traffic jam', 'Strawberry jam', 'Mango jam', 'Grape jam'],
    correctAnswer: 'Traffic jam',
    explanation: 'A traffic jam is stuck vehicles.',
  ),
  PuzzleLevel(
    question: 'Which match cannot burn?',
    options: ['Football match', 'Wooden match', 'Safety match', 'Lit match'],
    correctAnswer: 'Football match',
    explanation: 'A football match is a game.',
  ),
  PuzzleLevel(
    question: 'Which fan cannot cool you?',
    options: ['Sports fan', 'Ceiling fan', 'Table fan', 'Hand fan'],
    correctAnswer: 'Sports fan',
    explanation: 'A sports fan is a person.',
  ),
  PuzzleLevel(
    question: 'Which letter can be mailed?',
    options: ['Envelope letter', 'Letter A', 'Letter B', 'Letter C'],
    correctAnswer: 'Envelope letter',
    explanation: 'A written letter can be mailed.',
  ),
  PuzzleLevel(
    question: 'Which bank holds no cash?',
    options: ['River bank', 'City bank', 'Savings bank', 'Cash bank'],
    correctAnswer: 'River bank',
    explanation: 'A river bank is land beside water.',
  ),
  PuzzleLevel(
    question: 'Which bat is not alive?',
    options: ['Cricket bat', 'Fruit bat', 'Cave bat', 'Baby bat'],
    correctAnswer: 'Cricket bat',
    explanation: 'A cricket bat is sports equipment.',
  ),
  PuzzleLevel(
    question: 'Which crane has no feathers?',
    options: ['Building crane', 'White crane', 'Grey crane', 'Wild crane'],
    correctAnswer: 'Building crane',
    explanation: 'A building crane is a machine.',
  ),
  PuzzleLevel(
    question: 'Which current is not water?',
    options: [
      'Electric current',
      'River current',
      'Ocean current',
      'Tide current',
    ],
    correctAnswer: 'Electric current',
    explanation: 'Electric current is a flow of charge.',
  ),
  PuzzleLevel(
    question: 'Which draft is not wind?',
    options: ['First draft', 'Cold draft', 'Air draft', 'Window draft'],
    correctAnswer: 'First draft',
    explanation: 'A first draft is a version of writing.',
  ),
];

class PuzzleScreen extends StatefulWidget {
  const PuzzleScreen({super.key, this.stageIndex, this.levelIndex});

  final int? stageIndex;
  final int? levelIndex;

  bool get isStageMode => stageIndex != null && levelIndex != null;

  @override
  State<PuzzleScreen> createState() => _PuzzleScreenState();
}

enum DailyTrackerDayStatus { empty, today, complete, missed }

class DailyTrackerDay {
  const DailyTrackerDay({
    required this.date,
    required this.dateKey,
    required this.label,
    required this.status,
    required this.isPlaceholder,
  });

  final DateTime date;
  final String dateKey;
  final String label;
  final DailyTrackerDayStatus status;
  final bool isPlaceholder;
}

class DailyPuzzleLandingScreen extends StatefulWidget {
  const DailyPuzzleLandingScreen({super.key});

  @override
  State<DailyPuzzleLandingScreen> createState() =>
      _DailyPuzzleLandingScreenState();
}

class _DailyPuzzleLandingScreenState extends State<DailyPuzzleLandingScreen> {
  int streak = 0;
  bool isLoadingDailyState = true;
  List<DailyTrackerDay> trackerDays = const [];

  @override
  void initState() {
    super.initState();
    loadStreak();
  }

  Future<void> loadStreak() async {
    final prefs = await GameStorage.prefs;
    final savedStreak = GameStorage.savedInt(prefs, GameStorage.dailyStreakKey);
    final savedTrackerDays = GameStorage.dailyTrackerDays();

    if (!mounted) {
      return;
    }

    setState(() {
      streak = savedStreak;
      trackerDays = savedTrackerDays;
      isLoadingDailyState = false;
    });
  }

  void openPuzzle() {
    Navigator.push(context, smoothPageRoute(const DailyPuzzleScreen())).then((
      _,
    ) {
      if (mounted) {
        loadStreak();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final canPop = Navigator.canPop(context);

    if (isLoadingDailyState) {
      return const PremiumLoading();
    }

    return Scaffold(
      body: Stack(
        children: [
          const Positioned.fill(
            child: Image(
              image: AssetImage(
                'assets/images/daily_puzzle_landing_background.webp',
              ),
              fit: BoxFit.cover,
              alignment: Alignment.center,
            ),
          ),
          SafeArea(
            child: SingleChildScrollView(
              padding: const EdgeInsets.fromLTRB(14, 12, 14, 20),
              child: Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 430),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      DailyLandingTopBar(
                        canPop: canPop,
                        streak: streak,
                        onBack: () => Navigator.of(context).maybePop(),
                      ),
                      const SizedBox(height: 50),
                      DailyLandingHeroCard(onStart: openPuzzle),
                      const SizedBox(height: 50),
                      DailyLandingStreakCard(trackerDays: trackerDays),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class DailyLandingTopBar extends StatelessWidget {
  const DailyLandingTopBar({
    super.key,
    required this.canPop,
    required this.streak,
    required this.onBack,
  });

  final bool canPop;
  final int streak;
  final VoidCallback onBack;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Material(
          color: Colors.white.withAlpha(230),
          shape: const CircleBorder(),
          elevation: 2,
          shadowColor: const Color(0x1F33406C),
          child: InkWell(
            customBorder: const CircleBorder(),
            onTap: withButtonFeedback(canPop ? onBack : null),
            child: SizedBox(
              width: 38,
              height: 38,
              child: Icon(
                Icons.arrow_back_rounded,
                color: canPop
                    ? const Color(0xFF1F2E55)
                    : const Color(0x661F2E55),
                size: 24,
              ),
            ),
          ),
        ),
        const Spacer(),
        const Text(
          'Daily Puzzle',
          style: TextStyle(
            color: Color(0xFF1F2E55),
            fontSize: 16,
            fontWeight: FontWeight.w900,
          ),
        ),
        const Spacer(),
        Container(
          height: 38,
          padding: const EdgeInsets.symmetric(horizontal: 14),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(230),
            borderRadius: BorderRadius.circular(999),
            boxShadow: const [
              BoxShadow(
                color: Color(0x1F33406C),
                blurRadius: 10,
                offset: Offset(0, 4),
              ),
            ],
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(
                Icons.local_fire_department_rounded,
                color: Color(0xFFFF7A1A),
                size: 20,
              ),
              const SizedBox(width: 6),
              Text(
                '$streak',
                style: const TextStyle(
                  color: Color(0xFFE84A3A),
                  fontSize: 16,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class DailyLandingHeroCard extends StatelessWidget {
  const DailyLandingHeroCard({super.key, required this.onStart});

  final VoidCallback onStart;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 42),
      padding: const EdgeInsets.fromLTRB(22, 24, 22, 22),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(153),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withAlpha(125)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x1FCA7DA4),
            blurRadius: 20,
            offset: Offset(0, 10),
          ),
        ],
      ),
      child: Column(
        children: [
          Container(
            width: 112,
            height: 112,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: Colors.white.withAlpha(125),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x14CA7DA4),
                  blurRadius: 18,
                  offset: Offset(0, 8),
                ),
              ],
            ),
            child: const Center(
              child: Image(
                image: AssetImage('assets/images/daily_calendar.webp'),
                width: 82,
                height: 82,
                fit: BoxFit.contain,
              ),
            ),
          ),
          const SizedBox(height: 24),
          const Text(
            "Today's MindTrap",
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Color(0xFF1F2E55),
              fontSize: 18,
              fontWeight: FontWeight.w900,
              letterSpacing: 0,
            ),
          ),
          const SizedBox(height: 5),
          const Text(
            'One puzzle a day keeps\nyour mind sharp!',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Color(0xFF41506F),
              fontSize: 13,
              fontWeight: FontWeight.w700,
              height: 1.22,
            ),
          ),
          const SizedBox(height: 28),
          SizedBox(
            height: 56,
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: withButtonFeedback(onStart),
              icon: const Icon(Icons.play_arrow_rounded, size: 26),
              label: const Text(
                'Start Daily Puzzle',
                style: TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0,
                ),
              ),
              style: ElevatedButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: const Color(0xFF6F63FF),
                elevation: 8,
                shadowColor: const Color(0x665B6FFA),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(22),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class DailyLandingStreakCard extends StatelessWidget {
  const DailyLandingStreakCard({super.key, required this.trackerDays});

  final List<DailyTrackerDay> trackerDays;

  @override
  Widget build(BuildContext context) {
    const monthNames = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ];
    const weekdayLabels = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
    final now = DateTime.now();
    final monthName = monthNames[now.month - 1];

    debugPrint(
      'Daily tracker UI: '
      '${trackerDays.map((day) => '${day.dateKey}:${day.status.name}').join(', ')}',
    );

    return Container(
      padding: const EdgeInsets.fromLTRB(18, 14, 18, 16),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(204),
        borderRadius: BorderRadius.circular(24),
        boxShadow: const [
          BoxShadow(
            color: Color(0x17CA7DA4),
            blurRadius: 18,
            offset: Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        children: [
          Row(
            children: [
              Text(
                monthName,
                style: const TextStyle(
                  color: Color(0xFF1F2E55),
                  fontSize: 14,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const Spacer(),
              Text(
                '${now.year}',
                style: const TextStyle(
                  color: Color(0xFF6F63FF),
                  fontSize: 14,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              for (final label in weekdayLabels)
                SizedBox(
                  width: 32,
                  child: Text(
                    label,
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      color: Color(0xFF6674A5),
                      fontSize: 10,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 8),
          GridView.builder(
            padding: EdgeInsets.zero,
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: trackerDays.length,
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 7,
              mainAxisSpacing: 7,
              crossAxisSpacing: 7,
              childAspectRatio: 0.78,
            ),
            itemBuilder: (context, index) {
              final day = trackerDays[index];
              return DailyLandingDayDot(
                label: day.label,
                status: day.status,
                isPlaceholder: day.isPlaceholder,
              );
            },
          ),
        ],
      ),
    );
  }
}

class DailyLandingDayDot extends StatelessWidget {
  const DailyLandingDayDot({
    super.key,
    required this.label,
    required this.status,
    required this.isPlaceholder,
  });

  final String label;
  final DailyTrackerDayStatus status;
  final bool isPlaceholder;

  @override
  Widget build(BuildContext context) {
    if (isPlaceholder) {
      return const SizedBox.shrink();
    }

    final isComplete = status == DailyTrackerDayStatus.complete;
    final isToday = status == DailyTrackerDayStatus.today;
    final isMissed = status == DailyTrackerDayStatus.missed;
    final backgroundColor = isComplete
        ? const Color(0xFF55D6A8)
        : isToday
        ? const Color(0xFF4E8CFF)
        : isMissed
        ? const Color(0xFFE84A5F).withAlpha(190)
        : Colors.white.withAlpha(150);
    final icon = isComplete
        ? Icons.check_rounded
        : isToday
        ? Icons.diamond_rounded
        : isMissed
        ? Icons.close_rounded
        : null;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          label,
          style: TextStyle(
            color: status == DailyTrackerDayStatus.empty
                ? const Color(0xFF9BA6C8)
                : const Color(0xFF1F2E55),
            fontSize: 10,
            fontWeight: FontWeight.w900,
          ),
        ),
        const SizedBox(height: 4),
        Container(
          width: 24,
          height: 24,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            color: backgroundColor,
            border: isComplete || isToday || isMissed
                ? null
                : Border.all(color: const Color(0xFFDDE2F0)),
          ),
          child: icon == null
              ? null
              : Icon(icon, color: Colors.white, size: isToday ? 13 : 15),
        ),
      ],
    );
  }
}

class LevelSelectScreen extends StatefulWidget {
  const LevelSelectScreen({super.key});

  static const int levelsPerStage = 40;
  static const int stageCount = 25;

  static int get currentGlobalLevelIndex {
    for (var stageIndex = 0; stageIndex < stageCount; stageIndex++) {
      for (
        var levelIndex = 0;
        levelIndex < levelsPerStage;
        levelIndex++
      ) {
        if (GameStorage.isStageLevelUnlocked(stageIndex, levelIndex) &&
            GameStorage.starsForStageLevel(stageIndex, levelIndex) == 0) {
          return stageIndex * levelsPerStage + levelIndex;
        }
      }
    }

    return 0;
  }

  static int get currentStageIndex =>
      currentGlobalLevelIndex ~/ levelsPerStage;

  static String get currentBackgroundAsset =>
      levelBackgroundAssetForStage(currentStageIndex);

  @override
  State<LevelSelectScreen> createState() => _LevelSelectScreenState();
}

class _LevelSelectScreenState extends State<LevelSelectScreen> {
  int get currentGlobalLevelIndex => LevelSelectScreen.currentGlobalLevelIndex;

  int get currentStageIndex => LevelSelectScreen.currentStageIndex;

  int get currentStageLevelIndex =>
      currentGlobalLevelIndex % LevelSelectScreen.levelsPerStage;

  int get currentLevelNumber => currentGlobalLevelIndex + 1;

  String get backgroundAsset => LevelSelectScreen.currentBackgroundAsset;
  LevelTheme get levelTheme => levelThemeForStage(currentStageIndex);

  Future<void> openCurrentLevel() async {
    await Navigator.push(
      context,
      smoothPageRoute(
        PuzzleScreen(
          stageIndex: currentStageIndex,
          levelIndex: currentStageLevelIndex,
        ),
      ),
    );

    if (mounted) {
      setState(() {});
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SizedBox.expand(
        child: Stack(
          fit: StackFit.expand,
          children: [
            Image(
              image: AssetImage(backgroundAsset),
              fit: BoxFit.cover,
              alignment: Alignment.topCenter,
              gaplessPlayback: true,
            ),
            SafeArea(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(20, 24, 20, 24),
                child: Column(
                  children: [
                    Row(
                      children: [
                        LevelRoundIconButton(
                          icon: Icons.arrow_back_rounded,
                          onPressed: () => Navigator.of(context).maybePop(),
                        ),
                        const Spacer(),
                        LevelRoundIconButton(
                          icon: Icons.settings_rounded,
                          onPressed: () {
                            Navigator.push(
                              context,
                              smoothPageRoute(const SettingsScreen()),
                            );
                          },
                        ),
                      ],
                    ),
                    const SizedBox(height: 28),
                    Text(
                      levelTheme.title,
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontFamily: 'Roboto',
                        color: levelTheme.titleColor,
                        fontSize: 25,
                        fontWeight: FontWeight.w900,
                        height: 1,
                        shadows: [
                          Shadow(
                            color: levelTheme.titleShadow,
                            blurRadius: 12,
                            offset: const Offset(0, 3),
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 2),
                    LevelLaunchCard(
                      levelNumber: currentLevelNumber,
                      levelInStage: currentStageLevelIndex + 1,
                      theme: levelTheme,
                      onPressed: openCurrentLevel,
                    ),
                    const Spacer(flex: 3),
                    LevelQuickActions(theme: levelTheme),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class LevelRoundIconButton extends StatelessWidget {
  const LevelRoundIconButton({
    super.key,
    required this.icon,
    required this.onPressed,
  });

  final IconData icon;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.white.withAlpha(238),
      shape: const CircleBorder(),
      elevation: 5,
      shadowColor: const Color(0x332178BA),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: withButtonFeedback(onPressed),
        child: SizedBox(
          width: 42,
          height: 42,
          child: Icon(icon, color: const Color(0xFF071A49), size: 26),
        ),
      ),
    );
  }
}

class LevelLaunchCard extends StatelessWidget {
  const LevelLaunchCard({
    super.key,
    required this.levelNumber,
    required this.levelInStage,
    required this.theme,
    required this.onPressed,
  });

  final int levelNumber;
  final int levelInStage;
  final LevelTheme theme;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    final progress = levelInStage / LevelSelectScreen.levelsPerStage;

    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: withButtonFeedback(onPressed),
        borderRadius: BorderRadius.circular(34),
        child: Container(
          width: 270,
          padding: const EdgeInsets.fromLTRB(22, 25, 22, 21),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(211),
            borderRadius: BorderRadius.circular(34),
            border: Border.all(color: theme.accent, width: 5),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                'Level $levelNumber',
                style: const TextStyle(
                  fontFamily: 'Roboto',
                  color: Color(0xFF071A49),
                  fontSize: 30,
                  fontWeight: FontWeight.w900,
                  height: 1,
                ),
              ),
              const SizedBox(height: 24),
              Container(
                height: 20,
                padding: const EdgeInsets.all(4),
                decoration: BoxDecoration(
                  color: Colors.white.withAlpha(175),
                  borderRadius: BorderRadius.circular(999),
                  border: Border.all(color: Colors.white, width: 2),
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(999),
                  child: LinearProgressIndicator(
                    value: progress,
                    minHeight: 12,
                    backgroundColor: Colors.transparent,
                    valueColor: AlwaysStoppedAnimation<Color>(theme.accent),
                  ),
                ),
              ),
              const SizedBox(height: 18),
              Text(
                '$levelInStage / ${LevelSelectScreen.levelsPerStage}',
                style: const TextStyle(
                  fontFamily: 'Roboto',
                  color: Color(0xFF071A49),
                  fontSize: 18,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class LevelQuickActions extends StatelessWidget {
  const LevelQuickActions({super.key, required this.theme});

  final LevelTheme theme;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(198),
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.white.withAlpha(215)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          LevelActionTile(
            icon: Icons.calendar_month_rounded,
            label: 'Daily Streak',
            color: theme.accent,
          ),
          LevelActionTile(
            icon: Icons.shopping_bag_rounded,
            label: 'Store',
            color: theme.accentDark,
          ),
        ],
      ),
    );
  }
}

class LevelActionTile extends StatelessWidget {
  const LevelActionTile({
    super.key,
    required this.icon,
    required this.label,
    required this.color,
  });

  final IconData icon;
  final String label;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        margin: const EdgeInsets.symmetric(horizontal: 5),
        padding: const EdgeInsets.symmetric(vertical: 14),
        decoration: BoxDecoration(
          color: Colors.white.withAlpha(165),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white.withAlpha(220)),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, color: color, size: 32),
            const SizedBox(height: 8),
            Text(
              label,
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: const TextStyle(
                fontFamily: 'Roboto',
                color: Color(0xFF071A49),
                fontSize: 12,
                fontWeight: FontWeight.w900,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class LevelTheme {
  const LevelTheme({
    required this.title,
    required this.titleColor,
    required this.titleShadow,
    required this.accent,
    required this.accentDark,
    required this.shadow,
  });

  final String title;
  final Color titleColor;
  final Color titleShadow;
  final Color accent;
  final Color accentDark;
  final Color shadow;
}

LevelTheme levelThemeForStage(int stageIndex) {
  const themes = [
    LevelTheme(
      title: 'Sunset Explorer',
      titleColor: Color(0xFF071A49),
      titleShadow: Color(0x66FFF4CF),
      accent: Color(0xFFFFB300),
      accentDark: Color(0xFFFF8A00),
      shadow: Color(0xFFFFB300),
    ),
    LevelTheme(
      title: 'Forest Trail',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA0E3E26),
      accent: Color(0xFF2ECC71),
      accentDark: Color(0xFF159947),
      shadow: Color(0xFF159947),
    ),
    LevelTheme(
      title: 'Crystal Path',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA243B7A),
      accent: Color(0xFF54B7FF),
      accentDark: Color(0xFF2F74E8),
      shadow: Color(0xFF2F74E8),
    ),
    LevelTheme(
      title: 'Mystic Peak',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA3A235E),
      accent: Color(0xFF9B5CFF),
      accentDark: Color(0xFF6A35E8),
      shadow: Color(0xFF6A35E8),
    ),
    LevelTheme(
      title: 'Ocean Mind',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA063F5C),
      accent: Color(0xFF19C7D4),
      accentDark: Color(0xFF0C8AA0),
      shadow: Color(0xFF0C8AA0),
    ),
    LevelTheme(
      title: 'Golden Quest',
      titleColor: Color(0xFF071A49),
      titleShadow: Color(0x66FFF4CF),
      accent: Color(0xFFFFC928),
      accentDark: Color(0xFFE89A00),
      shadow: Color(0xFFE89A00),
    ),
    LevelTheme(
      title: 'Night Logic',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA071A49),
      accent: Color(0xFF7C8BFF),
      accentDark: Color(0xFF4D5BE8),
      shadow: Color(0xFF4D5BE8),
    ),
    LevelTheme(
      title: 'Cosmic Nebula',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA4A148C),
      accent: Color(0xFFE040FB),
      accentDark: Color(0xFFAA00FF),
      shadow: Color(0xFFAA00FF),
    ),
    LevelTheme(
      title: 'Cyber Quantum',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA004D40),
      accent: Color(0xFF00E676),
      accentDark: Color(0xFF00B0FF),
      shadow: Color(0xFF00E676),
    ),
    LevelTheme(
      title: 'Master Mind',
      titleColor: Color(0xFFFFFFFF),
      titleShadow: Color(0xAA311B92),
      accent: Color(0xFFFF4081),
      accentDark: Color(0xFFC51162),
      shadow: Color(0xFFFF4081),
    ),
  ];
  return themes[stageIndex.clamp(0, themes.length - 1)];
}

class LevelHeaderPlayButton extends StatelessWidget {
  const LevelHeaderPlayButton({
    super.key,
    required this.label,
    required this.onPressed,
  });

  final String label;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: withButtonFeedback(onPressed),
        borderRadius: BorderRadius.circular(29),
        child: Container(
          width: 172,
          height: 50,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(29),
            gradient: const LinearGradient(
              begin: Alignment.centerLeft,
              end: Alignment.centerRight,
              colors: [Color(0xFF54B7FF), Color(0xFF2F74E8)],
            ),
            border: Border.all(color: Colors.white.withAlpha(190), width: 1),
            boxShadow: const [
              BoxShadow(
                color: Color(0x662F74E8),
                blurRadius: 18,
                offset: Offset(0, 8),
              ),
            ],
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(
                Icons.play_arrow_rounded,
                size: 28,
                color: Colors.white,
              ),
              const SizedBox(width: 8),
              Text(
                label,
                style: const TextStyle(
                  fontFamily: 'Roboto',
                  fontSize: 18,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0,
                  color: Colors.white,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

String levelBackgroundAssetForStage(int stageIndex) {
  final safeIndex = (stageIndex % 7).abs();
  return 'assets/images/Stage-${safeIndex + 1}.webp';
}

class StageSelectScreen extends StatefulWidget {
  const StageSelectScreen({super.key});

  static const int stageCount = 10;
  static const int levelsPerStage = 10;

  @override
  State<StageSelectScreen> createState() => _StageSelectScreenState();
}

class _StageSelectScreenState extends State<StageSelectScreen> {
  final ScrollController _scrollController = ScrollController();

  static const List<Alignment> _levelAlignments = [
    Alignment(0, 0.82),
    Alignment(0, 0.67),
    Alignment(0, 0.51),
    Alignment(0, 0.34),
    Alignment(0, 0.16),
    Alignment(0, -0.02),
    Alignment(0, -0.20),
    Alignment(0, -0.40),
    Alignment(0, -0.60),
    Alignment(0, -0.80),
  ];

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.jumpTo(_scrollController.position.maxScrollExtent);
      }
    });
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  Future<void> openLevel(int stageIndex, int levelIndex) async {
    await Navigator.push(
      context,
      smoothPageRoute(
        PuzzleScreen(stageIndex: stageIndex, levelIndex: levelIndex),
      ),
    );

    if (mounted) {
      setState(() {});
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        controller: _scrollController,
        child: Column(
          children: [
            for (
              var stageIndex = StageSelectScreen.stageCount - 1;
              stageIndex >= 0;
              stageIndex--
            )
              StageMapSection(
                stageIndex: stageIndex,
                levelAlignments: _levelAlignments,
                onLevelPressed: openLevel,
                onBackPressed: () => Navigator.of(context).maybePop(),
              ),
          ],
        ),
      ),
    );
  }
}

class StageMapSection extends StatelessWidget {
  const StageMapSection({
    super.key,
    required this.stageIndex,
    required this.levelAlignments,
    required this.onLevelPressed,
    required this.onBackPressed,
  });

  final int stageIndex;
  final List<Alignment> levelAlignments;
  final void Function(int stageIndex, int levelIndex) onLevelPressed;
  final VoidCallback onBackPressed;

  @override
  Widget build(BuildContext context) {
    final viewportHeight = MediaQuery.sizeOf(context).height;

    return SizedBox(
      height: viewportHeight,
      width: double.infinity,
      child: Stack(
        fit: StackFit.expand,
        children: [
          const Image(
            image: AssetImage('assets/images/puzzle_complete_background.webp'),
            fit: BoxFit.cover,
            alignment: Alignment.topCenter,
          ),
          Image(
            image: AssetImage('assets/images/Stage-${stageIndex + 1}.webp'),
            fit: BoxFit.cover,
            alignment: Alignment.topCenter,
            gaplessPlayback: true,
            frameBuilder: (context, child, frame, wasSynchronouslyLoaded) {
              if (wasSynchronouslyLoaded || frame != null) {
                return child;
              }

              return const SizedBox.shrink();
            },
            errorBuilder: (context, error, stackTrace) {
              debugPrint(
                'Stage image failed: assets/images/Stage-${stageIndex + 1}.webp $error',
              );
              return const SizedBox.shrink();
            },
          ),
          for (
            var levelIndex = 0;
            levelIndex < StageSelectScreen.levelsPerStage;
            levelIndex++
          )
            if (GameStorage.isStageLevelUnlocked(stageIndex, levelIndex))
              Align(
                alignment: levelAlignments[levelIndex],
                child: StageRoadTile(
                  onPressed: () => onLevelPressed(stageIndex, levelIndex),
                ),
              ),
          Positioned(
            top: 0,
            left: 0,
            right: 0,
            child: SafeArea(
              bottom: false,
              child: Padding(
                padding: const EdgeInsets.fromLTRB(14, 10, 14, 0),
                child: Row(
                  children: [
                    Material(
                      color: Colors.white.withAlpha(235),
                      shape: const CircleBorder(),
                      elevation: 2,
                      shadowColor: const Color(0x332178BA),
                      child: InkWell(
                        customBorder: const CircleBorder(),
                        onTap: withButtonFeedback(onBackPressed),
                        child: const SizedBox(
                          width: 42,
                          height: 42,
                          child: Icon(
                            Icons.arrow_back_rounded,
                            color: Color(0xFF244169),
                            size: 26,
                          ),
                        ),
                      ),
                    ),
                    const Spacer(),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 14,
                        vertical: 7,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.white.withAlpha(220),
                        borderRadius: BorderRadius.circular(999),
                        boxShadow: const [
                          BoxShadow(
                            color: Color(0x262178BA),
                            blurRadius: 10,
                            offset: Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Text(
                        'Stage ${stageIndex + 1}',
                        style: const TextStyle(
                          fontFamily: 'Roboto',
                          color: Color(0xFF244169),
                          fontSize: 14,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class StageRoadTile extends StatefulWidget {
  const StageRoadTile({super.key, required this.onPressed});

  final VoidCallback onPressed;

  @override
  State<StageRoadTile> createState() => _StageRoadTileState();
}

class _StageRoadTileState extends State<StageRoadTile>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _dropAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 880),
    )..forward();
    _dropAnimation = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeOutBack,
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        final progress = _controller.value;
        final dustProgress = ((progress - 0.58) / 0.34).clamp(0.0, 1.0);
        final dustOpacity = sin(dustProgress * pi).clamp(0.0, 1.0);
        final dustScale = 0.4 + dustProgress * 1.15;

        return SizedBox(
          width: 120,
          height: 126,
          child: Stack(
            alignment: Alignment.center,
            clipBehavior: Clip.none,
            children: [
              Positioned(
                bottom: 8,
                child: Opacity(
                  opacity: dustOpacity,
                  child: Transform.scale(
                    scale: dustScale,
                    child: const _StageTileDust(),
                  ),
                ),
              ),
              Transform.translate(
                offset: Offset(0, -82 * (1 - _dropAnimation.value)),
                child: child,
              ),
            ],
          ),
        );
      },
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(18),
          onTap: withButtonFeedback(widget.onPressed),
          child: const SizedBox(
            width: 100,
            height: 100,
            child: Image(
              image: AssetImage('assets/images/stage_1_tile.webp'),
              fit: BoxFit.contain,
            ),
          ),
        ),
      ),
    );
  }
}

class StageLevelButton extends StatefulWidget {
  const StageLevelButton({
    super.key,
    required this.stageIndex,
    required this.levelIndex,
    required this.isUnlocked,
    required this.stars,
    required this.onPressed,
  });

  final int stageIndex;
  final int levelIndex;
  final bool isUnlocked;
  final int stars;
  final VoidCallback onPressed;

  @override
  State<StageLevelButton> createState() => _StageLevelButtonState();
}

class _StageLevelButtonState extends State<StageLevelButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _dropAnimation;

  bool get _usesStageOneTile => widget.stageIndex == 0 && widget.isUnlocked;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 880),
    );
    _dropAnimation = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeOutBack,
    );

    if (_usesStageOneTile) {
      _controller.forward();
    } else {
      _controller.value = 1;
    }
  }

  @override
  void didUpdateWidget(covariant StageLevelButton oldWidget) {
    super.didUpdateWidget(oldWidget);
    final wasUsingTile = oldWidget.stageIndex == 0 && oldWidget.isUnlocked;
    if (_usesStageOneTile && !wasUsingTile) {
      _controller.forward(from: 0);
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final levelNumber = widget.levelIndex + 1;
    final isComplete = widget.stars > 0;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        _usesStageOneTile
            ? _StageOneFallingTile(
                controller: _controller,
                dropAnimation: _dropAnimation,
                levelNumber: levelNumber,
                isComplete: isComplete,
                onPressed: widget.onPressed,
              )
            : _StageCircleLevelButton(
                levelNumber: levelNumber,
                isUnlocked: widget.isUnlocked,
                isComplete: isComplete,
                onPressed: widget.onPressed,
              ),
        const SizedBox(height: 4),
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            for (var index = 0; index < 3; index++)
              Icon(
                Icons.star_rounded,
                color: index < widget.stars
                    ? const Color(0xFFFFC83D)
                    : Colors.white.withAlpha(185),
                size: 15,
                shadows: const [
                  Shadow(
                    color: Color(0x4D1D3154),
                    blurRadius: 3,
                    offset: Offset(0, 1),
                  ),
                ],
              ),
          ],
        ),
      ],
    );
  }
}

class _StageCircleLevelButton extends StatelessWidget {
  const _StageCircleLevelButton({
    required this.levelNumber,
    required this.isUnlocked,
    required this.isComplete,
    required this.onPressed,
  });

  final int levelNumber;
  final bool isUnlocked;
  final bool isComplete;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: isUnlocked ? Colors.white : Colors.white.withAlpha(170),
      shape: const CircleBorder(),
      elevation: isUnlocked ? 8 : 2,
      shadowColor: const Color(0x552178BA),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: withButtonFeedback(isUnlocked ? onPressed : null),
        child: Container(
          width: 54,
          height: 54,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            border: Border.all(
              color: isUnlocked
                  ? const Color(0xFF2F74E8)
                  : const Color(0xFFB8C5DD),
              width: 3,
            ),
            gradient: isComplete
                ? const LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    colors: [Color(0xFF59C1FF), Color(0xFF2F74E8)],
                  )
                : null,
          ),
          child: isUnlocked
              ? isComplete
                    ? const Icon(
                        Icons.play_arrow_rounded,
                        color: Colors.white,
                        size: 30,
                      )
                    : Text(
                        '$levelNumber',
                        style: const TextStyle(
                          fontFamily: 'Roboto',
                          color: Color(0xFF244169),
                          fontSize: 18,
                          fontWeight: FontWeight.w900,
                        ),
                      )
              : const Icon(
                  Icons.lock_rounded,
                  color: Color(0xFF8B9AB7),
                  size: 24,
                ),
        ),
      ),
    );
  }
}

class _StageOneFallingTile extends StatelessWidget {
  const _StageOneFallingTile({
    required this.controller,
    required this.dropAnimation,
    required this.levelNumber,
    required this.isComplete,
    required this.onPressed,
  });

  final AnimationController controller;
  final Animation<double> dropAnimation;
  final int levelNumber;
  final bool isComplete;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: controller,
      builder: (context, child) {
        final progress = controller.value;
        final dustProgress = ((progress - 0.58) / 0.34).clamp(0.0, 1.0);
        final dustOpacity = sin(dustProgress * pi).clamp(0.0, 1.0);
        final dustScale = 0.4 + dustProgress * 1.15;

        return SizedBox(
          width: 82,
          height: 86,
          child: Stack(
            alignment: Alignment.center,
            clipBehavior: Clip.none,
            children: [
              Positioned(
                bottom: 8,
                child: Opacity(
                  opacity: dustOpacity,
                  child: Transform.scale(
                    scale: dustScale,
                    child: const _StageTileDust(),
                  ),
                ),
              ),
              Transform.translate(
                offset: Offset(0, -82 * (1 - dropAnimation.value)),
                child: Transform.scale(
                  scale: 0.92 + (dropAnimation.value * 0.08),
                  child: child,
                ),
              ),
            ],
          ),
        );
      },
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(18),
          onTap: withButtonFeedback(onPressed),
          child: SizedBox(
            width: 66,
            height: 66,
            child: Stack(
              alignment: Alignment.center,
              children: [
                const Image(
                  image: AssetImage('assets/images/stage_1_tile.webp'),
                  width: 66,
                  height: 66,
                  fit: BoxFit.contain,
                ),
                Container(
                  width: 36,
                  height: 36,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.white.withAlpha(210),
                    boxShadow: const [
                      BoxShadow(
                        color: Color(0x332178BA),
                        blurRadius: 8,
                        offset: Offset(0, 3),
                      ),
                    ],
                  ),
                  child: isComplete
                      ? const Icon(
                          Icons.play_arrow_rounded,
                          color: Color(0xFF2F74E8),
                          size: 25,
                        )
                      : Text(
                          '$levelNumber',
                          style: const TextStyle(
                            fontFamily: 'Roboto',
                            color: Color(0xFF244169),
                            fontSize: 17,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _StageTileDust extends StatelessWidget {
  const _StageTileDust();

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 72,
      height: 24,
      child: Stack(
        alignment: Alignment.center,
        children: [
          _dustCloud(left: 6, width: 24, height: 10, alpha: 145),
          _dustCloud(left: 22, width: 32, height: 14, alpha: 170),
          _dustCloud(left: 48, width: 20, height: 9, alpha: 130),
        ],
      ),
    );
  }

  Widget _dustCloud({
    required double left,
    required double width,
    required double height,
    required int alpha,
  }) {
    return Positioned(
      left: left,
      bottom: 4,
      child: Container(
        width: width,
        height: height,
        decoration: BoxDecoration(
          color: const Color(0xFFEED7A0).withAlpha(alpha),
          borderRadius: BorderRadius.circular(999),
        ),
      ),
    );
  }
}

class DailyPuzzleScreen extends StatefulWidget {
  const DailyPuzzleScreen({super.key});

  @override
  State<DailyPuzzleScreen> createState() => _DailyPuzzleScreenState();
}

class _DailyPuzzleScreenState extends State<DailyPuzzleScreen> {
  PuzzleLevel get dailyPuzzle {
    final localized = PuzzleLocalizer.getTranslation(
      "What has keys but can't open locks?",
      const ['Piano', 'Door', 'Car', 'Chest'],
      'Piano',
      'A piano has musical keys, not keys for opening locks.',
      LanguageController.instance.currentCode,
    );
    return PuzzleLevel(
      question: localized.question,
      options: localized.options,
      correctAnswer: localized.correctAnswer,
      explanation: localized.explanation,
    );
  }

  int streak = 0;
  bool solvedToday = false;
  bool attemptedToday = false;
  bool isShowingFeedback = false;
  bool lastAnswerWasCorrect = false;
  bool isLoadingDailyState = true;
  String? selectedAnswer;

  @override
  void initState() {
    super.initState();
    loadDailyStreak();
  }

  String formatDate(DateTime date) {
    final month = date.month.toString().padLeft(2, '0');
    final day = date.day.toString().padLeft(2, '0');
    return '${date.year}-$month-$day';
  }

  Future<void> loadDailyStreak() async {
    final prefs = await GameStorage.prefs;
    final today = formatDate(DateTime.now());
    final yesterday = formatDate(
      DateTime.now().subtract(const Duration(days: 1)),
    );
    final lastSolvedDate = GameStorage.savedString(
      prefs,
      GameStorage.dailyLastCompletedDateKey,
    );
    final attemptedDate = GameStorage.savedString(
      prefs,
      GameStorage.dailyAttemptedDateKey,
    );
    final savedAnswer = GameStorage.savedString(
      prefs,
      GameStorage.dailyAttemptedAnswerKey,
    );
    final savedAnswerWasCorrect = GameStorage.savedBool(
      prefs,
      GameStorage.dailyAttemptedCorrectKey,
    );
    var savedStreak = GameStorage.savedInt(prefs, GameStorage.dailyStreakKey);
    final hasSolvedToday = lastSolvedDate == today;
    final hasSavedAttemptToday = attemptedDate == today;
    final hasAttemptedToday = hasSavedAttemptToday || hasSolvedToday;
    final restoredAnswer = savedAnswer.isEmpty
        ? dailyPuzzle.correctAnswer
        : savedAnswer;
    final restoredAnswerWasCorrect = hasSavedAttemptToday
        ? savedAnswerWasCorrect
        : hasSolvedToday;

    if (lastSolvedDate.isNotEmpty &&
        lastSolvedDate != today &&
        lastSolvedDate != yesterday) {
      savedStreak = 0;
      await GameStorage.saveDailyCompletion(date: '', streak: savedStreak);
    }

    if (!mounted) {
      return;
    }

    setState(() {
      streak = savedStreak;
      solvedToday = hasSolvedToday;
      attemptedToday = hasAttemptedToday;
      isShowingFeedback = hasAttemptedToday;
      lastAnswerWasCorrect = hasAttemptedToday && restoredAnswerWasCorrect;
      selectedAnswer = hasAttemptedToday ? restoredAnswer : null;
      isLoadingDailyState = false;
    });
  }

  Future<void> checkAnswer(String answer) async {
    if (attemptedToday || isShowingFeedback) {
      return;
    }

    final isCorrect = answer == dailyPuzzle.correctAnswer;
    if (isCorrect) {
      playCorrectSound();
      triggerMediumFeedback();
    } else {
      playWrongSound();
      triggerHeavyFeedback();
    }

    setState(() {
      attemptedToday = true;
      isShowingFeedback = true;
      lastAnswerWasCorrect = isCorrect;
      selectedAnswer = answer;
    });

    await saveDailyAttempt(answer, isCorrect);
    await GameStorage.recordQuestionResult(isCorrect: isCorrect);

    if (isCorrect) {
      await updateDailyStreak();
    }
  }

  Future<void> saveDailyAttempt(String answer, bool isCorrect) async {
    final today = formatDate(DateTime.now());

    await GameStorage.saveDailyAttempt(
      date: today,
      answer: answer,
      isCorrect: isCorrect,
    );
  }

  Future<void> updateDailyStreak() async {
    if (solvedToday) {
      return;
    }

    final today = formatDate(DateTime.now());
    final nextStreak = streak + 1;

    await GameStorage.saveDailyCompletion(date: today, streak: nextStreak);

    if (!mounted) {
      return;
    }

    setState(() {
      streak = nextStreak;
      solvedToday = true;
    });
  }

  Color getAnswerColor(String option) {
    if (!isShowingFeedback) {
      return const Color(0xFF272D42);
    }

    if (option == dailyPuzzle.correctAnswer) {
      return lastAnswerWasCorrect ? const Color(0xFF00C853) : Colors.green;
    }

    if (lastAnswerWasCorrect || option != selectedAnswer) {
      return lastAnswerWasCorrect
          ? const Color(0xFF272D42)
          : const Color(0xFFB84A4A);
    }

    return const Color(0xFF7A1F1F);
  }

  Color getAnswerBorderColor(String option) {
    if (!isShowingFeedback) {
      return const Color(0xFF39415E);
    }

    if (option == selectedAnswer) {
      return Colors.white;
    }

    return const Color(0xFF39415E);
  }

  IconData? getAnswerIcon(String option) {
    if (!isShowingFeedback) {
      return null;
    }

    if (option == dailyPuzzle.correctAnswer) {
      return Icons.check_rounded;
    }

    if (option == selectedAnswer && !lastAnswerWasCorrect) {
      return Icons.close_rounded;
    }

    return null;
  }

  @override
  Widget build(BuildContext context) {
    final canPop = Navigator.canPop(context);

    if (isLoadingDailyState) {
      return const PremiumLoading();
    }

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: Scaffold(
            body: Stack(
              children: [
                Positioned.fill(
                  child: LevelBackgroundBuilder(
                    worldIndex: (DateTime.now().year + DateTime.now().month) % 7,
                    levelIndex: DateTime.now().day,
                  ),
                ),
                Positioned.fill(
                  child: AnimatedOpacity(
                    opacity: isShowingFeedback && lastAnswerWasCorrect ? 1 : 0,
                    duration: const Duration(milliseconds: 950),
                    curve: Curves.easeInOutCubic,
                    child: const Image(
                      image: AssetImage('assets/images/quiz_correct_background.webp'),
                      fit: BoxFit.cover,
                      alignment: Alignment.topCenter,
                    ),
                  ),
                ),
                Positioned.fill(
                  child: AnimatedOpacity(
                    opacity: isShowingFeedback && !lastAnswerWasCorrect ? 1 : 0,
                    duration: const Duration(milliseconds: 950),
                    curve: Curves.easeInOutCubic,
                    child: const Image(
                      image: AssetImage('assets/images/quiz_wrong_background.webp'),
                      fit: BoxFit.cover,
                      alignment: Alignment.topCenter,
                    ),
                  ),
                ),
                SafeArea(
                  child: Center(
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 430),
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(28, 18, 28, 22),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            DailyPuzzleTopHud(
                              canPop: canPop,
                              streak: streak,
                              isSolved: solvedToday,
                              onBack: () => Navigator.of(context).maybePop(),
                            ),
                            const SizedBox(height: 20),
                            DailyPuzzleHeader(isSolved: solvedToday, streak: streak),
                            const SizedBox(height: 18),
                      Expanded(
                        child: LevelEntranceTransition(
                          child: SingleChildScrollView(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.stretch,
                              children: [
                                const SizedBox(height: 6),
                                PuzzleQuestionCard(
                                  question: dailyPuzzle.question,
                                  showBrandPill: false,
                                ),
                                const SizedBox(height: 20),
                                for (
                                  var index = 0;
                                  index < dailyPuzzle.options.length;
                                  index++
                                ) ...[
                                  PuzzleAnswerButton(
                                    label: dailyPuzzle.options[index],
                                    optionIndex: index,
                                    backgroundColor: getAnswerColor(
                                      dailyPuzzle.options[index],
                                    ),
                                    trailingIcon: getAnswerIcon(
                                      dailyPuzzle.options[index],
                                    ),
                                    onPressed: () =>
                                        checkAnswer(dailyPuzzle.options[index]),
                                    isEnabled:
                                        !attemptedToday && !isShowingFeedback,
                                  ),
                                  const SizedBox(height: 14),
                                ],
                                AnimatedSwitcher(
                                  duration: const Duration(milliseconds: 360),
                                  reverseDuration: const Duration(
                                    milliseconds: 220,
                                  ),
                                  switchInCurve: Curves.easeOutCubic,
                                  switchOutCurve: Curves.easeInCubic,
                                  child: isShowingFeedback
                                      ? DailyPuzzleCompleteCard(
                                          key: ValueKey(lastAnswerWasCorrect),
                                          isCorrect: lastAnswerWasCorrect,
                                          onBackHome: () =>
                                              Navigator.pop(context),
                                        )
                                      : const SizedBox.shrink(),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    ),
  );
      },
    );
  }
}

class _PuzzleScreenState extends State<PuzzleScreen> {
  final List<PuzzleLevel> questionBank = buildMindTrapPuzzleBank();

  late List<PuzzleLevel> sessionLevels;
  int currentLevelIndex = 0;
  int score = 0;
  int lives = 3;
  int correctAnswers = 0;
  int totalAnswers = 0;
  bool isShowingFeedback = false;
  bool isShowingResultOverlay = false;
  bool isShowingLevelCompletePage = false;
  bool isShowingWrongAnswerPage = false;
  bool isDismissingLevelCompletePage = false;
  bool isDismissingWrongAnswerPage = false;
  bool isDismissingResultOverlay = false;
  bool lastAnswerWasCorrect = false;
  bool? feedbackBackgroundWasCorrect;
  bool hasPrecachedCorrectBackground = false;
  bool hasPrecachedWrongBackground = false;
  bool hasPrecachedLevelCompleteAssets = false;
  bool hasWon = false;
  bool hasGameOver = false;
  bool hasRecordedGameResult = false;
  String? selectedAnswer;
  bool? resultOverlayWasCorrect;
  int levelRetryCount = 0;
  final Set<String> eliminatedOptions = {};

  Future<void> useHint() async {
    if (isShowingFeedback || hasWon || hasGameOver) return;
    if (GameStorage.hintBalance > 0) {
      final used = await GameStorage.useHint();
      if (used && mounted) {
        setState(() {
          final wrongOptions = currentLevel.options
              .where((opt) => opt != currentLevel.correctAnswer && !eliminatedOptions.contains(opt))
              .toList()..shuffle();
          eliminatedOptions.addAll(wrongOptions.take(2));
        });
        triggerSuccessFeedback();
        playCoinSound();
        showGameNotification(
          context: context,
          message: tr('hint_eliminated'),
          icon: Icons.lightbulb_rounded,
          accentColor: const Color(0xFF0284C7),
          iconColor: const Color(0xFF38BDF8),
        );
      }
    } else {
      _showBuyHintsDialog();
    }
  }

  void _showBuyHintsDialog() {
    showDialog<void>(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: const Color(0xFF0F172A),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(22),
          side: const BorderSide(color: Color(0xFF0284C7), width: 1.5),
        ),
        title: Row(
          children: [
            const Icon(Icons.lightbulb_outline_rounded, color: Color(0xFFFFB11F)),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                tr('out_of_hints'),
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900),
              ),
            ),
          ],
        ),
        content: Text(
          tr('buy_hints_prompt'),
          style: const TextStyle(color: Color(0xFFC7D2FE)),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(ctx).pop(),
            child: Text(tr('cancel'), style: const TextStyle(color: Colors.white70)),
          ),
          ElevatedButton.icon(
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF16A947),
              foregroundColor: Colors.white,
            ),
            icon: Image.asset('assets/images/coin.webp', width: 20, height: 20),
            label: const Text('100'),
            onPressed: () async {
              final ok = await GameStorage.buyHints(hintCount: 1, price: 100, useGems: false);
              if (ctx.mounted) Navigator.of(ctx).pop();
              if (ok && mounted) {
                setState(() {});
                await useHint();
              } else if (mounted) {
                showGameNotification(
                  context: context,
                  message: tr('not_enough_coins'),
                  icon: Icons.monetization_on_rounded,
                  accentColor: const Color(0xFFEF4444),
                  iconColor: const Color(0xFFFCA5A5),
                );
              }
            },
          ),
          ElevatedButton.icon(
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF8E43F4),
              foregroundColor: Colors.white,
            ),
            icon: Image.asset('assets/images/gem.webp', width: 20, height: 20),
            label: const Text('10'),
            onPressed: () async {
              final ok = await GameStorage.buyHints(hintCount: 1, price: 10, useGems: true);
              if (ctx.mounted) Navigator.of(ctx).pop();
              if (ok && mounted) {
                setState(() {});
                await useHint();
              } else if (mounted) {
                showGameNotification(
                  context: context,
                  message: tr('not_enough_gems'),
                  icon: Icons.diamond_rounded,
                  accentColor: const Color(0xFFEF4444),
                  iconColor: const Color(0xFFFCA5A5),
                );
              }
            },
          ),
        ],
      ),
    );
  }

  PuzzleLevel get currentLevel {
    final base = sessionLevels[currentLevelIndex];
    final localized = PuzzleLocalizer.getTranslation(
      base.question,
      base.options,
      base.correctAnswer,
      base.explanation,
      LanguageController.instance.currentCode,
    );
    return PuzzleLevel(
      question: localized.question,
      options: localized.options,
      correctAnswer: localized.correctAnswer,
      explanation: localized.explanation,
    );
  }
  LevelTheme get currentTheme => widget.isStageMode
      ? levelThemeForStage(widget.stageIndex!)
      : levelThemeForStage(2);

  @override
  void initState() {
    super.initState();
    updateBackgroundMusicSetting();
    startNewGame();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();

    if (!hasPrecachedCorrectBackground) {
      hasPrecachedCorrectBackground = true;
      precacheImage(
        const AssetImage('assets/images/quiz_correct_background.webp'),
        context,
      );
    }

    if (!hasPrecachedWrongBackground) {
      hasPrecachedWrongBackground = true;
      precacheImage(
        const AssetImage('assets/images/quiz_wrong_background.webp'),
        context,
      );
    }

    if (widget.isStageMode) {
      precacheImage(
        AssetImage(levelBackgroundAssetForStage(widget.stageIndex!)),
        context,
      );
    }

    if (!hasPrecachedLevelCompleteAssets) {
      hasPrecachedLevelCompleteAssets = true;
      precacheImage(
        const AssetImage('assets/images/level_complete_background.webp'),
        context,
      );
      precacheImage(
        const AssetImage('assets/images/level_complete_trophy.png'),
        context,
      );
    }
  }

  void startNewGame() {
    eliminatedOptions.clear();
    final randomSeed = widget.isStageMode
        ? ((widget.stageIndex! + 1) * 1000 +
              widget.levelIndex! +
              (levelRetryCount * 997))
        : DateTime.now().microsecondsSinceEpoch;
    sessionLevels = List<PuzzleLevel>.from(questionBank)
      ..shuffle(Random(randomSeed));
    sessionLevels = sessionLevels.take(widget.isStageMode ? 3 : 5).toList();
    currentLevelIndex = 0;
    score = 0;
    lives = 3;
    correctAnswers = 0;
    totalAnswers = 0;
    isShowingFeedback = false;
    isShowingResultOverlay = false;
    isShowingLevelCompletePage = false;
    isShowingWrongAnswerPage = false;
    isDismissingLevelCompletePage = false;
    isDismissingWrongAnswerPage = false;
    isDismissingResultOverlay = false;
    lastAnswerWasCorrect = false;
    feedbackBackgroundWasCorrect = null;
    hasWon = false;
    hasGameOver = false;
    hasRecordedGameResult = false;
    selectedAnswer = null;
    resultOverlayWasCorrect = null;
  }

  void checkAnswer(String answer) {
    if (eliminatedOptions.contains(answer) ||
        isShowingFeedback ||
        isShowingLevelCompletePage ||
        isShowingWrongAnswerPage ||
        hasWon ||
        hasGameOver) {
      return;
    }

    final isCorrect = answer == currentLevel.correctAnswer;
    final nextLives = isCorrect ? lives : lives - 1;
    if (isCorrect) {
      playCorrectSound();
      triggerMediumFeedback();
    } else {
      playWrongSound();
      triggerHeavyFeedback();
    }

    setState(() {
      isShowingFeedback = true;
      lastAnswerWasCorrect = isCorrect;
      feedbackBackgroundWasCorrect = isCorrect;
      selectedAnswer = answer;

      if (isCorrect) {
        score += 10;
        correctAnswers++;
      } else {
        lives = nextLives;
      }

      totalAnswers++;
    });
    unawaited(
      GameStorage.recordAnswer(
        isCorrect: isCorrect,
        score: score,
        levelReached: currentLevelIndex + 1,
      ),
    );

    if (isCorrect) {
      if (widget.isStageMode && currentLevelIndex == sessionLevels.length - 1) {
        showLevelCompletePage();
      } else if (currentLevelIndex == sessionLevels.length - 1) {
        Future.delayed(const Duration(milliseconds: 1800), () {
          if (mounted) advanceAfterAnswer(lives);
        });
      } else if (widget.isStageMode) {
        Future.delayed(const Duration(milliseconds: 900), () {
          if (mounted) advanceAfterAnswer(lives);
        });
      } else {
        showLevelCompletePage();
      }
    } else {
      showWrongAnswerPage();
    }
  }

  void showLevelCompletePage() {
    Future.delayed(const Duration(milliseconds: 1800), () {
      if (!mounted) {
        return;
      }

      setState(() {
        isShowingLevelCompletePage = true;
        isDismissingLevelCompletePage = false;
      });
    });
  }

  void dismissLevelCompletePageThenAdvance() {
    if (isDismissingLevelCompletePage) {
      return;
    }

    if (widget.isStageMode && currentLevelIndex == sessionLevels.length - 1) {
      setState(() {
        isDismissingLevelCompletePage = false;
      });
      advanceAfterAnswer(lives);
      return;
    }

    setState(() {
      isDismissingLevelCompletePage = true;
    });

    Future.delayed(const Duration(milliseconds: 420), () {
      advanceAfterAnswer(lives);
    });
  }

  void showWrongAnswerPage() {
    Future.delayed(const Duration(milliseconds: 1800), () {
      if (!mounted) {
        return;
      }

      setState(() {
        isShowingWrongAnswerPage = true;
        isDismissingWrongAnswerPage = false;
      });
    });
  }

  void dismissWrongAnswerPageThenAdvance() {
    if (isDismissingWrongAnswerPage) {
      return;
    }

    setState(() {
      isDismissingWrongAnswerPage = true;
    });

    Future.delayed(const Duration(milliseconds: 420), () {
      if (widget.isStageMode) {
        retryCurrentLevel();
      } else {
        advanceAfterAnswer(lives);
      }
    });
  }

  void retryCurrentLevel() {
    if (!mounted) {
      return;
    }

    setState(() {
      levelRetryCount++;
      startNewGame();
    });
  }

  String getCorrectAnswerExplanation(PuzzleLevel level) {
    return level.explanation;
  }

  void advanceAfterAnswer(int nextLives) {
    if (!mounted) {
      return;
    }

    var didFinish = false;
    var didWin = false;
    var finishedLevels = correctAnswers;

    setState(() {
      eliminatedOptions.clear();
      if (widget.isStageMode && currentLevelIndex == sessionLevels.length - 1) {
        hasWon = true;
        didFinish = true;
        didWin = true;
        finishedLevels = totalAnswers;
        playWinSound();
        triggerSuccessFeedback();
      } else if (nextLives == 0) {
        hasGameOver = true;
        didFinish = true;
        didWin = false;
        finishedLevels = correctAnswers;
        playLoseSound();
        triggerHeavyFeedback();
      } else if (currentLevelIndex == sessionLevels.length - 1) {
        hasWon = true;
        didFinish = true;
        didWin = true;
        finishedLevels = totalAnswers;
        playWinSound();
        triggerSuccessFeedback();
      } else {
        currentLevelIndex++;
      }

      final shouldKeepCompleteOverlay = didFinish && widget.isStageMode;

      isShowingFeedback = false;
      isShowingResultOverlay = false;
      isShowingLevelCompletePage = shouldKeepCompleteOverlay;
      isShowingWrongAnswerPage = false;
      isDismissingLevelCompletePage = false;
      isDismissingWrongAnswerPage = false;
      isDismissingResultOverlay = false;
      lastAnswerWasCorrect = false;
      feedbackBackgroundWasCorrect = null;
      selectedAnswer = shouldKeepCompleteOverlay ? selectedAnswer : null;
      resultOverlayWasCorrect = null;
    });
    if (didFinish && !hasRecordedGameResult) {
      hasRecordedGameResult = true;
      if (didWin) {
        unawaited(GameStorage.awardLevelDiamonds(5));
        final isStageCompletion = widget.isStageMode &&
            widget.levelIndex == (StageSelectScreen.levelsPerStage - 1);
        if (isStageCompletion) {
          unawaited(GameStorage.awardStageCoins(150));
        } else if (!widget.isStageMode) {
          unawaited(GameStorage.awardStageCoins(100));
        }
      }
      unawaited(
        GameStorage.recordGameFinished(
          didWin: didWin,
          finalScore: score,
          levelsCompleted: finishedLevels,
          wasPerfect: didWin && correctAnswers == totalAnswers,
          remainingLives: nextLives,
        ),
      );
    }
    if (didFinish && widget.isStageMode) {
      unawaited(
        GameStorage.saveStageLevelStars(
          stageIndex: widget.stageIndex!,
          levelIndex: widget.levelIndex!,
          stars: correctAnswers,
        ).then((_) {
          if (mounted) {
            Navigator.of(context).pop();
          }
        }),
      );
      return;
    }
  }

  void playAgain() {
    setState(() {
      startNewGame();
    });
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, currentLang, _) {
        final canPop = Navigator.canPop(context);

        if (hasWon || hasGameOver) {
          if (hasGameOver) {
            return GameOverScreen(
              finalScore: score,
              levelsCompleted: correctAnswers,
              correctAnswers: correctAnswers,
              totalAnswers: totalAnswers,
              onTryAgain: playAgain,
              onBackToHome: () {
                Navigator.of(context).popUntil((route) => route.isFirst);
              },
            );
          }
          return GameSummaryScreen(
            didWin: hasWon,
            finalScore: score,
            levelsCompleted: totalAnswers,
            correctAnswers: correctAnswers,
            totalAnswers: totalAnswers,
            onPlayAgain: playAgain,
            onBackToHome: () {
              Navigator.of(context).popUntil((route) => route.isFirst);
            },
          );
        }

        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: Stack(
            children: [
              Scaffold(
                body: Stack(
                  children: [
                    if (widget.isStageMode)
                      Positioned.fill(
                        child: LevelBackgroundBuilder(
                          worldIndex: widget.stageIndex!,
                          levelIndex: (widget.levelIndex! * 3) + currentLevelIndex,
                        ),
                      )
                    else
                      Positioned.fill(
                        child: LevelBackgroundBuilder(
                          worldIndex: currentLevelIndex ~/ 3,
                          levelIndex: currentLevelIndex,
                        ),
                      ),
                    Positioned.fill(
                      child: AnimatedOpacity(
                        opacity: 0.0,
                        duration: const Duration(milliseconds: 950),
                        curve: Curves.easeInOutCubic,
                        child: const Image(
                          image: AssetImage(
                            'assets/images/quiz_correct_background.webp',
                          ),
                          fit: BoxFit.cover,
                          alignment: Alignment.topCenter,
                        ),
                      ),
                    ),
                    Positioned.fill(
                      child: AnimatedOpacity(
                        opacity: 0.0,
                        duration: const Duration(milliseconds: 950),
                        curve: Curves.easeInOutCubic,
                        child: const Image(
                          image: AssetImage(
                            'assets/images/quiz_wrong_background.webp',
                          ),
                          fit: BoxFit.cover,
                          alignment: Alignment.topCenter,
                        ),
                      ),
                    ),
                    SafeArea(
                      child: Center(
                        child: ConstrainedBox(
                          constraints: const BoxConstraints(maxWidth: 430),
                          child: Padding(
                            padding: const EdgeInsets.fromLTRB(28, 18, 28, 22),
                            child: buildGameplayContent(canPop: canPop),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              if (isShowingLevelCompletePage)
                LevelCompleteScreen(
                  score: 10,
                  accuracy: 100,
                  isExiting: isDismissingLevelCompletePage,
                  isStageComplete: widget.isStageMode &&
                      widget.levelIndex == (StageSelectScreen.levelsPerStage - 1),
                  onNextPuzzle: dismissLevelCompletePageThenAdvance,
                ),
              if (isShowingWrongAnswerPage)
                if (selectedAnswer == '__timeout__')
                  TimeOutScreen(
                    selectedAnswer: 'Time ran out',
                    correctAnswer: currentLevel.correctAnswer,
                    isExiting: isDismissingWrongAnswerPage,
                    continueLabel: widget.isStageMode ? 'Try Again' : 'Continue',
                    onContinue: dismissWrongAnswerPageThenAdvance,
                    onBackToHome: () {
                      Navigator.of(context).popUntil((route) => route.isFirst);
                    },
                  )
                else
                  WrongAnswerScreen(
                    selectedAnswer: selectedAnswer ?? 'No answer',
                    correctAnswer: currentLevel.correctAnswer,
                    explanation: getCorrectAnswerExplanation(currentLevel),
                    isExiting: isDismissingWrongAnswerPage,
                    continueLabel: widget.isStageMode ? 'Try Again' : 'Continue',
                    onContinue: dismissWrongAnswerPageThenAdvance,
                    onBackToHome: () {
                      Navigator.of(context).popUntil((route) => route.isFirst);
                    },
                  ),
            ],
          ),
        );
      },
    );
  }

  Widget buildGameplayContent({required bool canPop}) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        PuzzleTopHud(
          canPop: canPop,
          lives: lives,
          score: score,
          scoreFeedbackWasCorrect: isShowingFeedback
              ? lastAnswerWasCorrect
              : null,
          onBack: () => Navigator.of(context).maybePop(),
          onHint: useHint,
          onLanguage: () {
            Navigator.of(context).push(
              MaterialPageRoute<void>(
                builder: (_) => LanguageSelectionScreen(
                  isFromSettings: true,
                  onLanguageChosen: () {
                    GameStorage.setSelectedLanguageCode(
                      LanguageController.instance.currentCode,
                    );
                    Navigator.of(context).pop();
                    if (mounted) setState(() {});
                  },
                ),
              ),
            ).then((_) {
              if (mounted) setState(() {});
            });
          },
        ),
        const SizedBox(height: 20),
        ProgressHeader(
          currentPuzzle: currentLevelIndex + 1,
          totalPuzzles: sessionLevels.length,
          theme: currentTheme,
        ),
        const SizedBox(height: 18),
        Expanded(
          child: LevelEntranceTransition(
            key: ValueKey(currentLevelIndex),
            child: buildPuzzleContent(),
          ),
        ),
      ],
    );
  }

  Widget buildPuzzleContent() {
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const SizedBox(height: 6),
          PuzzleQuestionCard(
            question: currentLevel.question,
            theme: currentTheme,
          ),
          const SizedBox(height: 20),
          for (var index = 0; index < currentLevel.options.length; index++) ...[
            Builder(
              builder: (context) {
                final opt = currentLevel.options[index];
                final isEliminated = eliminatedOptions.contains(opt);
                return Opacity(
                  opacity: isEliminated ? 0.35 : 1.0,
                  child: PuzzleAnswerButton(
                    label: opt,
                    optionIndex: index,
                    backgroundColor: isEliminated
                        ? const Color(0xFF1E2433)
                        : getAnswerColor(opt),
                    theme: currentTheme,
                    trailingIcon: isEliminated
                        ? Icons.block_rounded
                        : getAnswerIcon(opt),
                    onPressed: isEliminated ? () {} : () => checkAnswer(opt),
                    isEnabled: !isShowingFeedback && !isEliminated,
                  ),
                );
              },
            ),
            const SizedBox(height: 14),
          ],
        ],
      ),
    );
  }

  Color getAnswerColor(String option) {
    if (!isShowingFeedback) {
      return const Color(0xFF272D42);
    }

    if (option == currentLevel.correctAnswer) {
      return lastAnswerWasCorrect ? const Color(0xFF00C853) : Colors.green;
    }

    if (lastAnswerWasCorrect || option != selectedAnswer) {
      return lastAnswerWasCorrect
          ? const Color(0xFF272D42)
          : const Color(0xFFB84A4A);
    }

    return const Color(0xFF7A1F1F);
  }

  Color getAnswerBorderColor(String option) {
    if (!isShowingFeedback) {
      return const Color(0xFF39415E);
    }

    if (option == selectedAnswer) {
      return Colors.white;
    }

    return const Color(0xFF39415E);
  }

  IconData? getAnswerIcon(String option) {
    if (!isShowingFeedback) {
      return null;
    }

    if (option == currentLevel.correctAnswer) {
      return Icons.check_rounded;
    }

    if (option == selectedAnswer && !lastAnswerWasCorrect) {
      return Icons.close_rounded;
    }

    return null;
  }

  IconData getOptionIcon(String option) {
    final normalized = option.toLowerCase();

    if (normalized.contains('stamp')) return Icons.filter_frames_rounded;
    if (normalized.contains('plane')) return Icons.flight_rounded;
    if (normalized.contains('map')) return Icons.map_outlined;
    if (normalized.contains('compass')) return Icons.explore_outlined;
    if (normalized.contains('clock')) return Icons.access_time_rounded;
    if (normalized.contains('piano') || normalized.contains('keys')) {
      return Icons.piano_rounded;
    }
    if (normalized.contains('door')) return Icons.door_front_door_outlined;
    if (normalized.contains('car')) return Icons.directions_car_rounded;
    if (normalized.contains('chest')) return Icons.inventory_2_outlined;
    if (normalized.contains('towel')) return Icons.dry_cleaning_rounded;
    if (normalized.contains('sun')) return Icons.wb_sunny_rounded;
    if (normalized.contains('fire')) return Icons.local_fire_department_rounded;
    if (normalized.contains('sand')) return Icons.hourglass_bottom_rounded;
    if (normalized.contains('snake')) return Icons.timeline_rounded;
    if (normalized.contains('train')) return Icons.train_rounded;
    if (normalized.contains('road')) return Icons.add_road_rounded;
    if (normalized.contains('queue')) return Icons.format_line_spacing_rounded;

    return Icons.crop_square_rounded;
  }
}

class PuzzleGridGlow extends StatelessWidget {
  const PuzzleGridGlow({super.key});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Positioned.fill(
          child: DecoratedBox(
            decoration: const BoxDecoration(
              gradient: RadialGradient(
                center: Alignment(-0.18, -0.4),
                radius: 0.82,
                colors: [
                  Color(0xFFFFFFFF),
                  Color(0xFFEAF9FF),
                  Color(0xFFD7F1FF),
                ],
              ),
            ),
          ),
        ),
        Positioned.fill(
          child: DecoratedBox(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Color(0x00FFFFFF),
                  Color(0xC7E9F8FF),
                  Color(0xFFD5EEFF),
                ],
              ),
            ),
          ),
        ),
        Positioned(
          left: 0,
          right: 0,
          bottom: 0,
          height: 126,
          child: CustomPaint(painter: PuzzleGridPainter()),
        ),
      ],
    );
  }
}

class PuzzleGridPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final sky = Paint()
      ..shader = const LinearGradient(
        begin: Alignment.topCenter,
        end: Alignment.bottomCenter,
        colors: [Color(0x00FFFFFF), Color(0x88B7E6FF), Color(0xCC8CCDEF)],
      ).createShader(Rect.fromLTWH(0, 0, size.width, size.height));
    canvas.drawRect(Offset.zero & size, sky);

    final mountainPaint = Paint()..color = const Color(0x4497D6EC);
    final far = Path()
      ..moveTo(0, size.height * 0.62)
      ..quadraticBezierTo(
        size.width * 0.18,
        size.height * 0.44,
        size.width * 0.34,
        size.height * 0.58,
      )
      ..quadraticBezierTo(
        size.width * 0.54,
        size.height * 0.34,
        size.width * 0.75,
        size.height * 0.57,
      )
      ..quadraticBezierTo(
        size.width * 0.9,
        size.height * 0.47,
        size.width,
        size.height * 0.61,
      )
      ..lineTo(size.width, size.height)
      ..lineTo(0, size.height)
      ..close();
    canvas.drawPath(far, mountainPaint);

    final nearPaint = Paint()..color = const Color(0x666BBFD9);
    final near = Path()
      ..moveTo(0, size.height * 0.74)
      ..quadraticBezierTo(
        size.width * 0.22,
        size.height * 0.56,
        size.width * 0.46,
        size.height * 0.72,
      )
      ..quadraticBezierTo(
        size.width * 0.68,
        size.height * 0.51,
        size.width,
        size.height * 0.7,
      )
      ..lineTo(size.width, size.height)
      ..lineTo(0, size.height)
      ..close();
    canvas.drawPath(near, nearPaint);

    final leafPaint = Paint()..color = const Color(0x885CB9B8);
    void drawLeaf(Offset center, double radius, double rotation) {
      canvas.save();
      canvas.translate(center.dx, center.dy);
      canvas.rotate(rotation);
      final rect = Rect.fromCenter(
        center: Offset.zero,
        width: radius * 0.72,
        height: radius * 1.75,
      );
      canvas.drawOval(rect, leafPaint);
      canvas.restore();
    }

    for (var i = 0; i < 7; i++) {
      drawLeaf(
        Offset(6 + i * 3.0, size.height - 12 - i * 11.5),
        13 - i * 0.65,
        -0.45,
      );
      drawLeaf(
        Offset(size.width - 6 - i * 3.2, size.height - 10 - i * 10.8),
        12 - i * 0.55,
        0.5,
      );
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

class PuzzleTopHud extends StatelessWidget {
  const PuzzleTopHud({
    super.key,
    required this.canPop,
    required this.lives,
    required this.score,
    required this.scoreFeedbackWasCorrect,
    required this.onBack,
    this.onHint,
    this.onLanguage,
  });

  final bool canPop;
  final int lives;
  final int score;
  final bool? scoreFeedbackWasCorrect;
  final VoidCallback onBack;
  final VoidCallback? onHint;
  final VoidCallback? onLanguage;

  @override
  Widget build(BuildContext context) {
    final emptyLives = 3 - lives;
    final scoreFeedbackColor = scoreFeedbackWasCorrect == null
        ? null
        : scoreFeedbackWasCorrect!
        ? const Color(0xFF00C853)
        : const Color(0x8CF04438);
    final scoreLabelColor = scoreFeedbackColor ?? const Color(0xFF5D79AE);
    final scoreValueColor = scoreFeedbackColor ?? const Color(0xFF20345D);

    return Row(
      children: [
        Material(
          color: Colors.white,
          shape: const CircleBorder(),
          elevation: 2,
          shadowColor: const Color(0x332178BA),
          child: InkWell(
            customBorder: const CircleBorder(),
            onTap: withButtonFeedback(canPop ? onBack : null),
            child: SizedBox(
              width: 42,
              height: 42,
              child: Icon(
                Icons.arrow_back_rounded,
                color: canPop
                    ? const Color(0xFF244169)
                    : const Color(0x66244169),
                size: 26,
              ),
            ),
          ),
        ),
        const SizedBox(width: 12),
        for (var index = 0; index < lives; index++) ...[
          const Icon(
            Icons.favorite_rounded,
            size: 24,
            color: Color(0xFFFF4B63),
          ),
          const SizedBox(width: 4),
        ],
        for (var index = 0; index < emptyLives; index++) ...[
          const Icon(
            Icons.favorite_rounded,
            size: 24,
            color: Color(0xFFD4E3F3),
          ),
          const SizedBox(width: 4),
        ],
        const Spacer(),
        if (onLanguage != null) ...[
          Material(
            color: Colors.white,
            shape: const CircleBorder(),
            elevation: 2,
            shadowColor: const Color(0x332178BA),
            child: InkWell(
              customBorder: const CircleBorder(),
              onTap: withButtonFeedback(onLanguage!),
              child: const SizedBox(
                width: 38,
                height: 38,
                child: Icon(
                  Icons.translate_rounded,
                  color: Color(0xFF244169),
                  size: 20,
                ),
              ),
            ),
          ),
          const SizedBox(width: 8),
        ],
        Material(
          color: Colors.white,
          borderRadius: BorderRadius.circular(999),
          elevation: 2,
          shadowColor: const Color(0x332178BA),
          child: InkWell(
            borderRadius: BorderRadius.circular(999),
            onTap: onHint != null ? withButtonFeedback(onHint!) : null,
            child: Container(
              height: 42,
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Image.asset(
                    'assets/images/hint-icon.webp',
                    width: 22,
                    height: 22,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    formatNumber(GameStorage.hintBalance),
                    style: const TextStyle(
                      fontFamily: 'Roboto',
                      fontSize: 14,
                      fontWeight: FontWeight.w900,
                      color: Color(0xFF20345D),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(width: 8),
        Container(
          height: 42,
          padding: const EdgeInsets.symmetric(horizontal: 14),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(999),
            boxShadow: const [
              BoxShadow(
                color: Color(0x1F2178BA),
                blurRadius: 8,
                offset: Offset(0, 3),
              ),
            ],
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              AnimatedDefaultTextStyle(
                duration: const Duration(milliseconds: 240),
                curve: Curves.easeOutCubic,
                style: TextStyle(
                  fontFamily: 'Roboto',
                  fontSize: 14,
                  fontWeight: FontWeight.w900,
                  color: scoreLabelColor,
                ),
                child: Text('${tr('score')}: '),
              ),
              AnimatedDefaultTextStyle(
                duration: const Duration(milliseconds: 240),
                curve: Curves.easeOutCubic,
                style: TextStyle(
                  fontFamily: 'Roboto',
                  fontSize: 14,
                  fontWeight: FontWeight.w900,
                  color: scoreValueColor,
                ),
                child: Text(formatNumber(score)),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class DailyPuzzleTopHud extends StatelessWidget {
  const DailyPuzzleTopHud({
    super.key,
    required this.canPop,
    required this.streak,
    required this.isSolved,
    required this.onBack,
    this.timerSeconds = 0,
    this.showTimer = false,
  });

  final bool canPop;
  final int streak;
  final bool isSolved;
  final VoidCallback onBack;
  final int timerSeconds;
  final bool showTimer;

  @override
  Widget build(BuildContext context) {
    final isWarning = timerSeconds <= 5;
    return Row(
      children: [
        Material(
          color: Colors.white,
          shape: const CircleBorder(),
          elevation: 2,
          shadowColor: const Color(0x332178BA),
          child: InkWell(
            customBorder: const CircleBorder(),
            onTap: withButtonFeedback(canPop ? onBack : null),
            child: SizedBox(
              width: 42,
              height: 42,
              child: Icon(
                Icons.arrow_back_rounded,
                color: canPop
                    ? const Color(0xFF244169)
                    : const Color(0x66244169),
                size: 26,
              ),
            ),
          ),
        ),
        const Spacer(),
        if (showTimer && timerSeconds > 0)
          AnimatedSwitcher(
            duration: const Duration(milliseconds: 200),
            child: Container(
              key: ValueKey(timerSeconds),
              height: 42,
              padding: const EdgeInsets.symmetric(horizontal: 14),
              decoration: BoxDecoration(
                color: isWarning
                    ? const Color(0xFFE53935).withAlpha(220)
                    : const Color(0xFF2F74E8).withAlpha(200),
                borderRadius: BorderRadius.circular(999),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(
                    Icons.timer_rounded,
                    size: 16,
                    color: Colors.white,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    '${timerSeconds}s',
                    style: const TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w800,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
          ),
        const Spacer(),
        Container(
          height: 42,
          padding: const EdgeInsets.symmetric(horizontal: 15),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(999),
            boxShadow: const [
              BoxShadow(
                color: Color(0x1F2178BA),
                blurRadius: 8,
                offset: Offset(0, 3),
              ),
            ],
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                isSolved
                    ? Icons.check_circle_rounded
                    : Icons.local_fire_department_rounded,
                size: 19,
                color: isSolved
                    ? const Color(0xFF20C997)
                    : const Color(0xFFFF9F1C),
              ),
              const SizedBox(width: 7),
              Text(
                isSolved ? 'Solved' : 'Streak: $streak',
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w900,
                  color: Color(0xFF20345D),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class DailyPuzzleHeader extends StatelessWidget {
  const DailyPuzzleHeader({
    super.key,
    required this.isSolved,
    required this.streak,
  });

  final bool isSolved;
  final int streak;

  @override
  Widget build(BuildContext context) {
    final completedCount = isSolved ? 1 : 0;

    return ClipRRect(
      borderRadius: BorderRadius.circular(28),
      child: Container(
        padding: const EdgeInsets.all(22),
        decoration: BoxDecoration(
          color: const Color.fromRGBO(255, 255, 255, 0.5),
          borderRadius: BorderRadius.circular(28),
          boxShadow: const [
            BoxShadow(
              color: Color(0x1A5B7CFA),
              blurRadius: 32,
              offset: Offset(0, 10),
            ),
          ],
        ),
        child: Column(
          children: [
            Row(
              children: [
                const Image(
                  image: AssetImage('assets/images/daily_calendar.webp'),
                  width: 78,
                  height: 78,
                  fit: BoxFit.contain,
                ),
                const SizedBox(width: 18),
                const Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        "Today's Puzzle",
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0,
                          color: Color(0xFF1F2E55),
                        ),
                      ),
                      SizedBox(height: 6),
                      Text(
                        "Complete today's puzzle\nand keep your streak alive!",
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                          height: 1.25,
                          color: Color(0xFF52607C),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
              decoration: BoxDecoration(
                color: Colors.white.withAlpha(184),
                borderRadius: BorderRadius.circular(18),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x0D5B7CFA),
                    blurRadius: 12,
                    offset: Offset(0, 4),
                  ),
                ],
              ),
              child: Row(
                children: [
                  Expanded(
                    child: Text(
                      isSolved ? 'Solved' : 'Unsolved',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w900,
                        color: isSolved
                            ? const Color(0xFF6F63FF)
                            : const Color(0xFF8A94AE),
                      ),
                    ),
                  ),
                  Text(
                    '$completedCount / 1',
                    style: const TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w900,
                      color: Color(0xFF6674A5),
                    ),
                  ),
                  const Expanded(
                    child: Align(
                      alignment: Alignment.centerRight,
                      child: DailyPuzzleScorePill(),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class DailyPuzzleScorePill extends StatelessWidget {
  const DailyPuzzleScorePill({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: const [
        Image(
          image: AssetImage('assets/images/daily_gift.webp'),
          width: 30,
          height: 30,
          fit: BoxFit.contain,
        ),
        SizedBox(width: 6),
        Text(
          '+10 Score',
          maxLines: 1,
          style: TextStyle(
            fontSize: 12,
            fontWeight: FontWeight.w900,
            color: Color(0xFF6F63FF),
          ),
        ),
      ],
    );
  }
}

class DailyPuzzleCompleteCard extends StatelessWidget {
  const DailyPuzzleCompleteCard({
    super.key,
    required this.isCorrect,
    required this.onBackHome,
  });

  final bool isCorrect;
  final VoidCallback onBackHome;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 8, bottom: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            padding: const EdgeInsets.fromLTRB(18, 15, 18, 16),
            decoration: BoxDecoration(
              color: Colors.white.withAlpha(174),
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: Colors.white.withAlpha(148)),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x182178BA),
                  blurRadius: 9,
                  offset: Offset(0, 4),
                ),
              ],
            ),
            child: Row(
              children: [
                Icon(
                  isCorrect ? Icons.check_circle_rounded : Icons.cancel_rounded,
                  color: isCorrect
                      ? const Color(0xFF20C997)
                      : const Color(0xFFD92D20),
                  size: 28,
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    isCorrect
                        ? 'Come back tomorrow to continue streak.'
                        : "Today's puzzle completed.",
                    style: const TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w800,
                      height: 1.25,
                      color: Color(0xFF233B67),
                    ),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 14),
          SizedBox(
            height: 56,
            child: ElevatedButton.icon(
              onPressed: withButtonFeedback(onBackHome),
              icon: const Icon(Icons.home_rounded, size: 24),
              label: const Text(
                'Back Home',
                style: TextStyle(
                  fontSize: 17,
                  fontWeight: FontWeight.w800,
                  letterSpacing: 0,
                ),
              ),
              style: ElevatedButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: const Color(0xFF2F74E8),
                elevation: 7,
                shadowColor: const Color(0x553D35D8),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(18),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class PuzzleQuestionCard extends StatelessWidget {
  const PuzzleQuestionCard({
    super.key,
    required this.question,
    this.showBrandPill = true,
    this.theme,
  });

  final String question;
  final bool showBrandPill;
  final LevelTheme? theme;

  @override
  Widget build(BuildContext context) {
    final activeTheme = theme ?? levelThemeForStage(2);

    return Column(
      children: [
        if (showBrandPill) ...[
          Container(
            height: 40,
            padding: const EdgeInsets.symmetric(horizontal: 20),
            decoration: BoxDecoration(
              color: Colors.white.withAlpha(188),
              borderRadius: BorderRadius.circular(999),
              border: Border.all(color: activeTheme.accent.withAlpha(190)),
            ),
            child: const Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Image(
                  image: AssetImage('assets/images/home_logo.webp'),
                  width: 24,
                  height: 24,
                  fit: BoxFit.contain,
                ),
                SizedBox(width: 7),
                Text(
                  'MindTrap',
                  style: TextStyle(
                    fontFamily: 'Roboto',
                    fontSize: 16,
                    fontWeight: FontWeight.w900,
                    color: Color(0xFF2F74E8),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),
        ],
        Container(
          width: double.infinity,
          padding: const EdgeInsets.fromLTRB(24, 24, 24, 25),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(212),
            borderRadius: BorderRadius.circular(24),
            border: Border.all(
              color: activeTheme.accent.withAlpha(220),
              width: 2,
            ),
            boxShadow: [
              BoxShadow(
                color: activeTheme.shadow.withAlpha(86),
                blurRadius: 18,
                offset: const Offset(0, 8),
              ),
            ],
          ),
          child: Text(
            question,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontFamily: 'Roboto',
              fontSize: 22,
              fontWeight: FontWeight.w900,
              height: 1.22,
              color: Color(0xFF13264D),
            ),
          ),
        ),
      ],
    );
  }
}

class PuzzleAnswerButton extends StatefulWidget {
  const PuzzleAnswerButton({
    super.key,
    required this.label,
    required this.optionIndex,
    required this.backgroundColor,
    required this.isEnabled,
    required this.onPressed,
    this.theme,
    this.trailingIcon,
  });

  final String label;
  final int optionIndex;
  final Color backgroundColor;
  final bool isEnabled;
  final VoidCallback onPressed;
  final LevelTheme? theme;
  final IconData? trailingIcon;

  @override
  State<PuzzleAnswerButton> createState() => _PuzzleAnswerButtonState();
}

class _PuzzleAnswerButtonState extends State<PuzzleAnswerButton> {
  bool isPressed = false;

  void setPressed(bool value) {
    if (isPressed == value || (value && !widget.isEnabled)) {
      return;
    }

    setState(() {
      isPressed = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    final isFeedback = widget.trailingIcon != null;
    final isCorrectFeedback = widget.trailingIcon == Icons.check_rounded;
    final isWrongFeedback = widget.trailingIcon == Icons.close_rounded;
    final activeTheme = widget.theme ?? levelThemeForStage(2);
    final baseColor = isFeedback
        ? widget.backgroundColor
        : Colors.white.withAlpha(174);
    final labelColor = isWrongFeedback
        ? const Color(0xFFD92D20)
        : isFeedback
        ? Colors.white
        : const Color(0xFF233B67);
    final optionFontWeight = isCorrectFeedback
        ? FontWeight.w600
        : FontWeight.w700;
    const letterBadgeSize = 40.0;
    final isRtl = LanguageController.instance.isRtl;
    final urduLetters = const ['الف', 'ب', 'ج', 'د'];
    final englishLetters = const ['A', 'B', 'C', 'D'];
    final letters = isRtl ? urduLetters : englishLetters;
    final letter = widget.optionIndex < letters.length
        ? letters[widget.optionIndex]
        : '${widget.optionIndex + 1}';

    return Listener(
      onPointerDown: (_) => setPressed(true),
      onPointerUp: (_) => setPressed(false),
      onPointerCancel: (_) => setPressed(false),
      child: AnimatedScale(
        scale: isPressed ? 0.985 : 1,
        duration: const Duration(milliseconds: 160),
        curve: Curves.easeOutCubic,
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            onTap: withButtonFeedback(
              widget.isEnabled ? widget.onPressed : null,
            ),
            borderRadius: BorderRadius.circular(22),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(22),
              child: BackdropFilter(
                filter: ImageFilter.blur(
                  sigmaX: isWrongFeedback ? 10 : 0,
                  sigmaY: isWrongFeedback ? 10 : 0,
                ),
                child: AnimatedContainer(
                  height: 64,
                  duration: const Duration(milliseconds: 280),
                  curve: Curves.easeOutCubic,
                  padding: const EdgeInsets.symmetric(horizontal: 24),
                  decoration: BoxDecoration(
                    color: isCorrectFeedback
                        ? null
                        : isWrongFeedback
                        ? const Color(0xD1FFF0F0)
                        : baseColor,
                    gradient: isCorrectFeedback
                        ? const LinearGradient(
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                            colors: [
                              Color(0xFF47E6A1),
                              Color(0xFF35D6A3),
                              Color(0xFF20C997),
                            ],
                            stops: [0, 0.45, 1],
                          )
                        : null,
                    borderRadius: BorderRadius.circular(22),
                    border: isCorrectFeedback
                        ? Border.all(color: const Color(0xFF20C997), width: 2)
                        : isWrongFeedback
                        ? Border.all(color: const Color(0xFFE53935), width: 2)
                        : Border.all(
                            color: activeTheme.accent.withAlpha(210),
                            width: 2,
                          ),
                    boxShadow: [
                      BoxShadow(
                        color: isCorrectFeedback
                            ? const Color(0x4725D6A3)
                            : isWrongFeedback
                            ? const Color(0x14F04438)
                            : isFeedback
                            ? const Color(0x332178BA)
                            : activeTheme.shadow.withAlpha(45),
                        blurRadius: isCorrectFeedback
                            ? 20
                            : isWrongFeedback
                            ? 14
                            : 7,
                        offset: Offset(
                          0,
                          isCorrectFeedback
                              ? 8
                              : isWrongFeedback
                              ? 4
                              : 3,
                        ),
                      ),
                    ],
                  ),
                  child: Stack(
                    alignment: Alignment.center,
                    children: [
                      if (isCorrectFeedback || isWrongFeedback)
                        Positioned(
                          top: 0,
                          left: 18,
                          right: 18,
                          child: Container(
                            height: 1,
                            decoration: BoxDecoration(
                              color: Colors.white.withAlpha(115),
                              borderRadius: BorderRadius.circular(999),
                            ),
                          ),
                        ),
                      Row(
                        children: [
                          SizedBox(
                            width: 40,
                            height: 40,
                            child: Center(
                              child: Container(
                                width: letterBadgeSize,
                                height: letterBadgeSize,
                                alignment: Alignment.center,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: isCorrectFeedback
                                      ? Colors.white.withAlpha(191)
                                      : isWrongFeedback
                                      ? const Color(0x29F04438)
                                      : null,
                                  gradient: isCorrectFeedback || isWrongFeedback
                                      ? null
                                      : LinearGradient(
                                          begin: Alignment.topLeft,
                                          end: Alignment.bottomRight,
                                          colors: [
                                            activeTheme.accent,
                                            activeTheme.accentDark,
                                          ],
                                        ),
                                  boxShadow:
                                      isCorrectFeedback || isWrongFeedback
                                      ? [
                                          BoxShadow(
                                            color: Colors.white.withAlpha(89),
                                            blurRadius: 2,
                                            offset: const Offset(0, 1),
                                            blurStyle: BlurStyle.inner,
                                          ),
                                          if (isCorrectFeedback)
                                            const BoxShadow(
                                              color: Color(0x0F000000),
                                              blurRadius: 6,
                                              offset: Offset(0, 2),
                                            ),
                                        ]
                                      : null,
                                ),
                                child: Text(
                                  letter,
                                  style: TextStyle(
                                    fontFamily: 'Roboto',
                                    fontSize: 18,
                                    fontWeight: FontWeight.w900,
                                    color: isCorrectFeedback
                                        ? const Color(0xFF1CC282)
                                        : isWrongFeedback
                                        ? const Color(0xFFD92D20)
                                        : Colors.white,
                                  ),
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(width: 26),
                          Expanded(
                            child: Text(
                              widget.label,
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: TextStyle(
                                fontFamily: 'Roboto',
                                fontSize: 17,
                                fontWeight: optionFontWeight,
                                letterSpacing: 0,
                                color: labelColor,
                              ),
                            ),
                          ),
                          AnimatedSwitcher(
                            duration: const Duration(milliseconds: 220),
                            child: widget.trailingIcon == null
                                ? const SizedBox(
                                    key: ValueKey('empty'),
                                    width: 20,
                                    height: 24,
                                  )
                                : Icon(
                                    widget.trailingIcon,
                                    key: ValueKey(widget.trailingIcon),
                                    size: isCorrectFeedback ? 20 : 24,
                                    color: isWrongFeedback
                                        ? const Color(0xFFD92D20)
                                        : Colors.white,
                                  ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class GameOverScreen extends StatelessWidget {
  const GameOverScreen({
    super.key,
    required this.finalScore,
    required this.levelsCompleted,
    required this.correctAnswers,
    required this.totalAnswers,
    required this.onTryAgain,
    required this.onBackToHome,
  });

  final int finalScore;
  final int levelsCompleted;
  final int correctAnswers;
  final int totalAnswers;
  final VoidCallback onTryAgain;
  final VoidCallback onBackToHome;

  String get accuracyLabel {
    if (totalAnswers == 0) return '0%';
    return '${(correctAnswers / totalAnswers * 100).round()}%';
  }

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: LanguageController.instance.directionality,
      child: Scaffold(
        body: Stack(
          children: [
            const Positioned.fill(
              child: Image(
                image: AssetImage(
                  'assets/images/game over background image.webp',
                ),
                fit: BoxFit.cover,
                alignment: Alignment.topCenter,
              ),
            ),
            const PinkPetalAnimationLayer(),
            SafeArea(
              child: TweenAnimationBuilder<double>(
                tween: Tween<double>(begin: 0, end: 1),
                duration: const Duration(milliseconds: 720),
                curve: Curves.easeOutBack,
                builder: (context, value, child) {
                  return Opacity(
                    opacity: value.clamp(0.0, 1.0),
                    child: Transform.scale(
                      scale: 0.94 + (value * 0.06),
                      child: child,
                    ),
                  );
                },
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: LayoutBuilder(
                      builder: (context, constraints) {
                        return SingleChildScrollView(
                          padding: const EdgeInsets.fromLTRB(18, 24, 18, 24),
                          child: ConstrainedBox(
                            constraints: BoxConstraints(
                              minHeight: constraints.maxHeight - 48,
                            ),
                            child: IntrinsicHeight(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.stretch,
                                children: [
                                  const Spacer(),
                                  const Image(
                                    image: AssetImage(
                                      'assets/images/brain image.webp',
                                    ),
                                    width: 148,
                                    height: 148,
                                    fit: BoxFit.contain,
                                  ),
                                  const SizedBox(height: 18),
                                  Text(
                                    tr('game_over'),
                                    textAlign: TextAlign.center,
                                    style: const TextStyle(
                                      fontSize: 34,
                                      fontWeight: FontWeight.w900,
                                      letterSpacing: 0,
                                      color: Color(0xFF11224D),
                                    ),
                                  ),
                                  const SizedBox(height: 7),
                                  Text(
                                    tr('try_better'),
                                    textAlign: TextAlign.center,
                                    style: const TextStyle(
                                      fontSize: 16,
                                      fontWeight: FontWeight.w700,
                                      color: Color(0xFF38466F),
                                    ),
                                  ),
                                const SizedBox(height: 22),
                                Container(
                                  padding: const EdgeInsets.fromLTRB(
                                    18,
                                    16,
                                    18,
                                    12,
                                  ),
                                  decoration: BoxDecoration(
                                    color: Colors.white.withAlpha(219),
                                    borderRadius: BorderRadius.circular(18),
                                    boxShadow: const [
                                      BoxShadow(
                                        color: Color(0x18000000),
                                        blurRadius: 16,
                                        offset: Offset(0, 7),
                                      ),
                                    ],
                                  ),
                                  child: TweenAnimationBuilder<int>(
                                    tween: IntTween(begin: 0, end: finalScore),
                                    duration: const Duration(
                                      milliseconds: 1050,
                                    ),
                                    curve: Curves.easeOutCubic,
                                    builder: (context, value, child) {
                                      return Column(
                                        children: [
                                          Text(
                                            tr('score'),
                                            style: const TextStyle(
                                              fontSize: 16,
                                              fontWeight: FontWeight.w800,
                                              color: Color(0xFF26355D),
                                            ),
                                          ),
                                          const SizedBox(height: 3),
                                          Text(
                                            '$value',
                                            style: const TextStyle(
                                              fontSize: 50,
                                              fontWeight: FontWeight.w900,
                                              height: 1,
                                              color: Color(0xFFE85D75),
                                            ),
                                          ),
                                        ],
                                      );
                                    },
                                  ),
                                ),
                                const SizedBox(height: 12),
                                Row(
                                  children: [
                                    Expanded(
                                      child: Container(
                                        height: 115,
                                        padding: const EdgeInsets.symmetric(
                                          vertical: 10,
                                          horizontal: 12,
                                        ),
                                        decoration: BoxDecoration(
                                          color: Colors.white.withAlpha(230),
                                          borderRadius: BorderRadius.circular(
                                            16,
                                          ),
                                          boxShadow: const [
                                            BoxShadow(
                                              color: Color(0x12000000),
                                              blurRadius: 12,
                                              offset: Offset(0, 4),
                                            ),
                                          ],
                                        ),
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.center,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.center,
                                          children: [
                                            const Icon(
                                              Icons.workspace_premium_rounded,
                                              color: Color(0xFFE85D75),
                                              size: 35,
                                            ),
                                            const SizedBox(height: 4),
                                            Text(
                                              tr('levels_completed'),
                                              maxLines: 1,
                                              overflow: TextOverflow.ellipsis,
                                              textAlign: TextAlign.center,
                                              style: const TextStyle(
                                                fontSize: 13,
                                                fontWeight: FontWeight.w800,
                                                color: Color(0xFF3B466A),
                                              ),
                                            ),
                                            Text(
                                              '$levelsCompleted / ${totalAnswers == 0 ? 3 : totalAnswers}',
                                              textAlign: TextAlign.center,
                                              style: const TextStyle(
                                                fontSize: 18,
                                                fontWeight: FontWeight.w900,
                                                color: Color(0xFF151C5A),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 12),
                                    Expanded(
                                      child: Container(
                                        height: 115,
                                        padding: const EdgeInsets.symmetric(
                                          vertical: 10,
                                          horizontal: 12,
                                        ),
                                        decoration: BoxDecoration(
                                          color: Colors.white.withAlpha(230),
                                          borderRadius: BorderRadius.circular(
                                            16,
                                          ),
                                          boxShadow: const [
                                            BoxShadow(
                                              color: Color(0x12000000),
                                              blurRadius: 12,
                                              offset: Offset(0, 4),
                                            ),
                                          ],
                                        ),
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.center,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.center,
                                          children: [
                                            const Icon(
                                              Icons.track_changes_rounded,
                                              color: Color(0xFFE85D75),
                                              size: 35,
                                            ),
                                            const SizedBox(height: 4),
                                            Text(
                                              tr('accuracy'),
                                              maxLines: 1,
                                              overflow: TextOverflow.ellipsis,
                                              textAlign: TextAlign.center,
                                              style: const TextStyle(
                                                fontSize: 13,
                                                fontWeight: FontWeight.w800,
                                                color: Color(0xFF3B466A),
                                              ),
                                            ),
                                            Text(
                                              accuracyLabel,
                                              textAlign: TextAlign.center,
                                              style: const TextStyle(
                                                fontSize: 18,
                                                fontWeight: FontWeight.w900,
                                                color: Color(0xFF11224D),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 22),
                                SizedBox(
                                  height: 56,
                                  child: ElevatedButton.icon(
                                    onPressed: withButtonFeedback(onTryAgain),
                                    icon: const Icon(
                                      Icons.refresh_rounded,
                                      color: Colors.white,
                                    ),
                                    label: Text(
                                      tr('try_again'),
                                      style: const TextStyle(
                                        fontSize: 17,
                                        fontWeight: FontWeight.w800,
                                        color: Colors.white,
                                      ),
                                    ),
                                    style: ElevatedButton.styleFrom(
                                      backgroundColor: const Color(0xFFE85D75),
                                      foregroundColor: Colors.white,
                                      elevation: 4,
                                      shadowColor: const Color(0x40E85D75),
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(18),
                                      ),
                                    ),
                                  ),
                                ),
                                const SizedBox(height: 13),
                                SizedBox(
                                  height: 56,
                                  child: ElevatedButton.icon(
                                    onPressed: withButtonFeedback(onBackToHome),
                                    icon: const Icon(
                                      Icons.home_rounded,
                                      color: Color(0xFF11224D),
                                    ),
                                    label: Text(
                                      tr('back_home'),
                                      style: const TextStyle(
                                        fontSize: 17,
                                        fontWeight: FontWeight.w800,
                                        color: Color(0xFF11224D),
                                      ),
                                    ),
                                    style: ElevatedButton.styleFrom(
                                      backgroundColor: Colors.white,
                                      foregroundColor: const Color(0xFF11224D),
                                      elevation: 2,
                                      shadowColor: const Color(0x20000000),
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(18),
                                      ),
                                    ),
                                  ),
                                ),
                                const Spacer(),
                              ],
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    ),
  );
  }
}

class GameSummaryScreen extends StatelessWidget {
  const GameSummaryScreen({
    super.key,
    required this.didWin,
    required this.finalScore,
    required this.levelsCompleted,
    required this.correctAnswers,
    required this.totalAnswers,
    required this.onPlayAgain,
    required this.onBackToHome,
  });

  final bool didWin;
  final int finalScore;
  final int levelsCompleted;
  final int correctAnswers;
  final int totalAnswers;
  final VoidCallback onPlayAgain;
  final VoidCallback onBackToHome;

  String get accuracyLabel {
    if (totalAnswers == 0) {
      return '0%';
    }

    final percentage = (correctAnswers / totalAnswers * 100).round();
    return '$percentage%';
  }

  @override
  Widget build(BuildContext context) {
    final title = didWin ? tr('you_win') : tr('game_over');
    final subtitle = didWin
        ? tr('mind_escaped')
        : tr('try_better');

    return Directionality(
      textDirection: LanguageController.instance.directionality,
      child: Scaffold(
        body: Stack(
        children: [
          const Positioned.fill(
            child: Image(
              image: AssetImage(
                'assets/images/puzzle_complete_background.webp',
              ),
              fit: BoxFit.cover,
              alignment: Alignment.center,
            ),
          ),
          const PuzzleCompleteLeafAnimation(),
          SafeArea(
            child: TweenAnimationBuilder<double>(
              tween: Tween<double>(begin: 0, end: 1),
              duration: const Duration(milliseconds: 720),
              curve: Curves.easeOutBack,
              builder: (context, value, child) {
                final opacity = value.clamp(0.0, 1.0);
                final scale = 0.94 + (value * 0.06);

                return Opacity(
                  opacity: opacity,
                  child: Transform.scale(scale: scale, child: child),
                );
              },
              child: Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 430),
                  child: LayoutBuilder(
                    builder: (context, constraints) {
                      return SingleChildScrollView(
                        padding: const EdgeInsets.fromLTRB(18, 24, 18, 24),
                        child: ConstrainedBox(
                          constraints: BoxConstraints(
                            minHeight: constraints.maxHeight - 48,
                          ),
                          child: IntrinsicHeight(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.stretch,
                              children: [
                                const Spacer(),
                                SizedBox(
                                  height: 158,
                                  child: Stack(
                                    alignment: Alignment.center,
                                    clipBehavior: Clip.none,
                                    children: [
                                      Positioned(
                                        left: 56,
                                        top: 24,
                                        child: Transform.rotate(
                                          angle: 15 * pi / 180,
                                          child: const Image(
                                            image: AssetImage(
                                              'assets/images/puzzle_complete_leaf1.png',
                                            ),
                                            width: 68,
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        right: 56,
                                        top: 24,
                                        child: Transform.rotate(
                                          angle: -15 * pi / 180,
                                          child: const Image(
                                            image: AssetImage(
                                              'assets/images/puzzle_complete_leaf2.png',
                                            ),
                                            width: 68,
                                          ),
                                        ),
                                      ),
                                      Container(
                                        width: 132,
                                        height: 132,
                                        decoration: BoxDecoration(
                                          shape: BoxShape.circle,
                                          color: Colors.white.withAlpha(224),
                                          boxShadow: const [
                                            BoxShadow(
                                              color: Color(0x1F58B887),
                                              blurRadius: 28,
                                              offset: Offset(0, 10),
                                            ),
                                          ],
                                        ),
                                      ),
                                      const Image(
                                        image: AssetImage(
                                          'assets/images/puzzle_complete_diamond.png',
                                        ),
                                        width: 128,
                                        height: 128,
                                        fit: BoxFit.contain,
                                      ),
                                    ],
                                  ),
                                ),
                                const SizedBox(height: 10),
                                Text(
                                  title,
                                  textAlign: TextAlign.center,
                                  style: const TextStyle(
                                    fontSize: 34,
                                    fontWeight: FontWeight.w900,
                                    letterSpacing: 0,
                                    color: Color(0xFF11224D),
                                  ),
                                ),
                                const SizedBox(height: 7),
                                Text(
                                  subtitle,
                                  textAlign: TextAlign.center,
                                  style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w700,
                                    color: Color(0xFF38466F),
                                  ),
                                ),
                                const SizedBox(height: 22),
                                PuzzleCompleteScoreCard(score: finalScore),
                                const SizedBox(height: 12),
                                Row(
                                  children: [
                                    Expanded(
                                      child: PuzzleCompleteStatCard(
                                        icon: Icons.workspace_premium_rounded,
                                        label: tr('levels_completed'),
                                        value: '$levelsCompleted / 5',
                                      ),
                                    ),
                                    const SizedBox(width: 12),
                                    Expanded(
                                      child: PuzzleCompleteStatCard(
                                        icon: Icons.track_changes_rounded,
                                        label: tr('accuracy'),
                                        value: accuracyLabel,
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 22),
                                PuzzleCompleteActionButton(
                                  label: tr('play_again'),
                                  icon: Icons.refresh_rounded,
                                  onPressed: withButtonFeedback(onPlayAgain)!,
                                  isPrimary: true,
                                ),
                                const SizedBox(height: 13),
                                PuzzleCompleteActionButton(
                                  label: tr('back_home'),
                                  icon: Icons.home_rounded,
                                  onPressed: withButtonFeedback(onBackToHome)!,
                                  isPrimary: false,
                                ),
                                const Spacer(),
                              ],
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    ),
  );
  }
}

class PuzzleCompleteLeafAnimation extends StatefulWidget {
  const PuzzleCompleteLeafAnimation({super.key});

  @override
  State<PuzzleCompleteLeafAnimation> createState() =>
      _PuzzleCompleteLeafAnimationState();
}

class _PuzzleCompleteLeafAnimationState
    extends State<PuzzleCompleteLeafAnimation>
    with SingleTickerProviderStateMixin {
  late final Ticker _ticker;
  double _elapsed = 0.0;

  static const pieces = [
    ConfettiPieceSpec(
      startX: 0.08,
      delay: 0.02,
      speed: 0.72,
      rotationTurns: 0.34,
      color: Color(0xFF20C997),
      width: 5,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.28,
      delay: 0.32,
      speed: 0.64,
      rotationTurns: -0.42,
      color: Color(0xFFFFC400),
      width: 6,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.52,
      delay: 0.18,
      speed: 0.68,
      rotationTurns: 0.48,
      color: Color(0xFFFF9F1C),
      width: 5,
      height: 14,
    ),
    ConfettiPieceSpec(
      startX: 0.78,
      delay: 0.48,
      speed: 0.7,
      rotationTurns: -0.36,
      color: Color(0xFF54B7FF),
      width: 6,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.94,
      delay: 0.12,
      speed: 0.58,
      rotationTurns: 0.3,
      color: Color(0xFF20C997),
      width: 5,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.15,
      delay: 0.55,
      speed: 0.62,
      rotationTurns: -0.5,
      color: Color(0xFFFFC400),
      width: 6,
      height: 14,
    ),
    ConfettiPieceSpec(
      startX: 0.42,
      delay: 0.76,
      speed: 0.74,
      rotationTurns: 0.6,
      color: Color(0xFFFF9F1C),
      width: 5,
      height: 11,
    ),
    ConfettiPieceSpec(
      startX: 0.65,
      delay: 0.88,
      speed: 0.56,
      rotationTurns: -0.44,
      color: Color(0xFF54B7FF),
      width: 6,
      height: 13,
    ),
  ];

  @override
  void initState() {
    super.initState();
    _ticker = createTicker((elapsed) {
      setState(() {
        _elapsed = elapsed.inMilliseconds / 7600.0;
      });
    })..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: IgnorePointer(
        child: LayoutBuilder(
          builder: (context, constraints) {
            return Stack(
              children: [
                for (var index = 0; index < pieces.length; index++)
                  ConfettiPiece(
                    animationValue: _elapsed,
                    index: index,
                    spec: pieces[index],
                    canvasSize: Size(
                      constraints.maxWidth,
                      constraints.maxHeight,
                    ),
                  ),
              ],
            );
          },
        ),
      ),
    );
  }
}

class PuzzleCompleteLeafSpec {
  const PuzzleCompleteLeafSpec({
    required this.asset,
    required this.startX,
    required this.delay,
    required this.speed,
    required this.size,
    required this.drift,
    required this.rotationTurns,
  });

  final String asset;
  final double startX;
  final double delay;
  final double speed;
  final double size;
  final double drift;
  final double rotationTurns;
}

class PuzzleCompleteFallingLeaf extends StatelessWidget {
  const PuzzleCompleteFallingLeaf({
    super.key,
    required this.animationValue,
    required this.index,
    required this.spec,
    required this.canvasSize,
  });

  final double animationValue;
  final int index;
  final PuzzleCompleteLeafSpec spec;
  final Size canvasSize;

  @override
  Widget build(BuildContext context) {
    final progress = (animationValue * spec.speed + spec.delay) % 1;
    final wobble = sin((progress * pi * 2) + index) * spec.drift;
    final x = (canvasSize.width * spec.startX) + wobble;
    final y = -70 + ((canvasSize.height + 120) * progress);
    final rotation = (progress * spec.rotationTurns * pi * 2) + index;

    return Positioned(
      left: x,
      top: y,
      child: Opacity(
        opacity: 0.82,
        child: Transform.rotate(
          angle: rotation,
          child: Image(
            image: AssetImage(spec.asset),
            width: spec.size,
            height: spec.size * 1.45,
            fit: BoxFit.contain,
          ),
        ),
      ),
    );
  }
}

class PuzzleCompleteScoreCard extends StatelessWidget {
  const PuzzleCompleteScoreCard({super.key, required this.score});

  final int score;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 16, 18, 12),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(219),
        borderRadius: BorderRadius.circular(18),
        boxShadow: const [
          BoxShadow(
            color: Color(0x1758B887),
            blurRadius: 16,
            offset: Offset(0, 7),
          ),
        ],
      ),
      child: TweenAnimationBuilder<int>(
        tween: IntTween(begin: 0, end: score),
        duration: const Duration(milliseconds: 1050),
        curve: Curves.easeOutCubic,
        builder: (context, value, child) {
          return Column(
            children: [
              const Text(
                'Final Score',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w800,
                  color: Color(0xFF26355D),
                ),
              ),
              const SizedBox(height: 3),
              Text(
                '$value',
                style: const TextStyle(
                  fontSize: 50,
                  fontWeight: FontWeight.w900,
                  height: 1,
                  color: Color(0xFF16A86E),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}

class PuzzleCompleteStatCard extends StatelessWidget {
  const PuzzleCompleteStatCard({
    super.key,
    required this.icon,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 115,
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(219),
        borderRadius: BorderRadius.circular(16),
        boxShadow: const [
          BoxShadow(
            color: Color(0x1458B887),
            blurRadius: 14,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Icon(icon, color: const Color(0xFF20C997), size: 35),
          const SizedBox(height: 4),
          Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontSize: 13,
              fontWeight: FontWeight.w800,
              color: Color(0xFF3B466A),
            ),
          ),
          Text(
            value,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w900,
              color: Color(0xFF151C5A),
            ),
          ),
        ],
      ),
    );
  }
}

class PuzzleCompleteActionButton extends StatelessWidget {
  const PuzzleCompleteActionButton({
    super.key,
    required this.label,
    required this.icon,
    required this.onPressed,
    required this.isPrimary,
  });

  final String label;
  final IconData icon;
  final VoidCallback onPressed;
  final bool isPrimary;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 58,
      child: ElevatedButton.icon(
        onPressed: withButtonFeedback(onPressed),
        icon: Icon(icon, size: 27),
        label: Text(
          label,
          style: const TextStyle(
            fontSize: 22,
            fontWeight: FontWeight.w900,
            letterSpacing: 0,
          ),
        ),
        style: ElevatedButton.styleFrom(
          foregroundColor: isPrimary ? Colors.white : const Color(0xFF3B4E78),
          backgroundColor: isPrimary
              ? const Color(0xFF20C997)
              : Colors.white.withAlpha(228),
          elevation: isPrimary ? 9 : 5,
          shadowColor: isPrimary
              ? const Color(0x5A20C997)
              : const Color(0x1C3B4E78),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(28),
          ),
        ),
      ),
    );
  }
}

class AnimatedFinalScoreText extends StatelessWidget {
  const AnimatedFinalScoreText({super.key, required this.score});

  final int score;

  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder<int>(
      tween: IntTween(begin: 0, end: score),
      duration: const Duration(milliseconds: 1050),
      curve: Curves.easeOutCubic,
      builder: (context, value, child) {
        return Column(
          children: [
            const Text(
              'Final Score',
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w800,
                color: Color(0xFFAAB4CC),
              ),
            ),
            const SizedBox(height: 6),
            Text(
              '$value',
              style: const TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.w900,
                letterSpacing: -1,
                color: Color(0xFF7CFFCB),
              ),
            ),
          ],
        );
      },
    );
  }
}

class SummaryStatRow extends StatelessWidget {
  const SummaryStatRow({
    super.key,
    required this.icon,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
      decoration: BoxDecoration(
        color: const Color(0xFF272D42),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFF39415E)),
      ),
      child: Row(
        children: [
          Icon(icon, color: const Color(0xFF7CFFCB), size: 22),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: Color(0xFFAAB4CC),
              ),
            ),
          ),
          Text(
            value,
            style: const TextStyle(
              fontSize: 17,
              fontWeight: FontWeight.w900,
              color: Colors.white,
            ),
          ),
        ],
      ),
    );
  }
}

class LevelEntranceTransition extends StatefulWidget {
  const LevelEntranceTransition({super.key, required this.child});

  final Widget child;

  @override
  State<LevelEntranceTransition> createState() =>
      _LevelEntranceTransitionState();
}

class _LevelEntranceTransitionState extends State<LevelEntranceTransition>
    with SingleTickerProviderStateMixin {
  late final AnimationController controller;
  late final Animation<double> fadeAnimation;
  late final Animation<double> scaleAnimation;
  late final Animation<Offset> slideAnimation;

  @override
  void initState() {
    super.initState();
    controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1050),
    );
    final curvedAnimation = CurvedAnimation(
      parent: controller,
      curve: Curves.easeOutCubic,
    );
    fadeAnimation = CurvedAnimation(parent: controller, curve: Curves.easeOut);
    scaleAnimation = Tween<double>(
      begin: 0.975,
      end: 1,
    ).animate(curvedAnimation);
    slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.12),
      end: Offset.zero,
    ).animate(curvedAnimation);
    controller.forward();
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: fadeAnimation,
      child: SlideTransition(
        position: slideAnimation,
        child: ScaleTransition(scale: scaleAnimation, child: widget.child),
      ),
    );
  }
}

class PremiumActionButton extends StatefulWidget {
  const PremiumActionButton({
    super.key,
    required this.label,
    required this.icon,
    required this.onPressed,
  });

  final String label;
  final IconData icon;
  final VoidCallback onPressed;

  @override
  State<PremiumActionButton> createState() => _PremiumActionButtonState();
}

class _PremiumActionButtonState extends State<PremiumActionButton> {
  bool isPressed = false;

  void setPressed(bool value) {
    if (isPressed == value) {
      return;
    }

    setState(() {
      isPressed = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Listener(
      onPointerDown: (_) => setPressed(true),
      onPointerUp: (_) => setPressed(false),
      onPointerCancel: (_) => setPressed(false),
      child: AnimatedScale(
        scale: isPressed ? 0.965 : 1,
        duration: const Duration(milliseconds: 115),
        curve: Curves.easeOutCubic,
        child: SizedBox(
          height: 56,
          child: ElevatedButton.icon(
            onPressed: withButtonFeedback(widget.onPressed),
            icon: Icon(widget.icon, size: 24),
            label: Text(
              widget.label,
              style: const TextStyle(
                fontSize: 17,
                fontWeight: FontWeight.w700,
                letterSpacing: 0,
              ),
            ),
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: const Color(0xFF272D42),
              elevation: isPressed ? 3 : 7,
              shadowColor: const Color(0x553D35D8),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
                side: const BorderSide(color: Color(0xFF39415E)),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class LevelCompleteScreen extends StatelessWidget {
  const LevelCompleteScreen({
    super.key,
    required this.score,
    required this.accuracy,
    required this.isExiting,
    required this.onNextPuzzle,
    this.isStageComplete = false,
  });

  final int score;
  final int accuracy;
  final bool isExiting;
  final VoidCallback onNextPuzzle;
  final bool isStageComplete;

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: TweenAnimationBuilder<double>(
        tween: Tween<double>(begin: isExiting ? 1 : 0, end: isExiting ? 0 : 1),
        duration: Duration(milliseconds: isExiting ? 360 : 620),
        curve: isExiting ? Curves.easeInCubic : Curves.easeOutCubic,
        builder: (context, value, child) {
          final opacity = value.clamp(0.0, 1.0);
          final scale = 0.96 + (value * 0.04);
          final slideOffset = Offset(0, 22 * (1 - value));

          return Opacity(
            opacity: opacity,
            child: Transform.translate(
              offset: slideOffset,
              child: Transform.scale(scale: scale, child: child),
            ),
          );
        },
        child: Material(
          color: Colors.transparent,
          child: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage(
                    'assets/images/level_complete_background.webp',
                  ),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              const LevelCompleteConfettiLayer(),
              SafeArea(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: LayoutBuilder(
                      builder: (context, constraints) {
                        final isShort = constraints.maxHeight < 660;
                        final trophySize = isShort ? 178.0 : 214.0;
                        final horizontalPadding = isShort ? 24.0 : 28.0;
                        final verticalPadding = isShort ? 12.0 : 18.0;

                        return SingleChildScrollView(
                          padding: EdgeInsets.fromLTRB(
                            horizontalPadding,
                            verticalPadding,
                            horizontalPadding,
                            verticalPadding,
                          ),
                          child: ConstrainedBox(
                            constraints: BoxConstraints(
                              minHeight:
                                  constraints.maxHeight - (verticalPadding * 2),
                            ),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                SizedBox(
                                  width: trophySize,
                                  height: trophySize,
                                  child: DecoratedBox(
                                    decoration: const BoxDecoration(
                                      shape: BoxShape.circle,
                                      boxShadow: [
                                        BoxShadow(
                                          color: Color(0x66FFFFFF),
                                          blurRadius: 42,
                                          spreadRadius: 4,
                                          offset: Offset(0, 12),
                                        ),
                                      ],
                                    ),
                                    child: ClipOval(
                                      child: BackdropFilter(
                                        filter: ImageFilter.blur(
                                          sigmaX: 14,
                                          sigmaY: 14,
                                        ),
                                        child: Container(
                                          padding: const EdgeInsets.all(22),
                                          decoration: BoxDecoration(
                                            shape: BoxShape.circle,
                                            color: Colors.white.withAlpha(82),
                                            border: Border.all(
                                              color: Colors.white,
                                              width: 12,
                                            ),
                                            boxShadow: [
                                              BoxShadow(
                                                color: Colors.white.withAlpha(
                                                  140,
                                                ),
                                                blurRadius: 2,
                                                offset: const Offset(0, 1),
                                                blurStyle: BlurStyle.inner,
                                              ),
                                            ],
                                          ),
                                          child: const Image(
                                            image: AssetImage(
                                              'assets/images/level_complete_trophy.png',
                                            ),
                                            fit: BoxFit.contain,
                                          ),
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                                SizedBox(height: isShort ? 12 : 18),
                                Text(
                                  isStageComplete
                                      ? tr('stage_complete')
                                      : tr('level_complete'),
                                  textAlign: TextAlign.center,
                                  style: const TextStyle(
                                    color: Color(0xFF0E2754),
                                    fontSize: 26,
                                    fontWeight: FontWeight.w900,
                                    height: 1.05,
                                  ),
                                ),
                                const SizedBox(height: 6),
                                Text(
                                  tr('you_solved_round'),
                                  textAlign: TextAlign.center,
                                  style: const TextStyle(
                                    color: Color(0xFF223A63),
                                    fontSize: 15,
                                    fontWeight: FontWeight.w500,
                                  ),
                                ),
                                SizedBox(height: isShort ? 12 : 18),
                                Container(
                                  padding: const EdgeInsets.symmetric(
                                    horizontal: 16,
                                    vertical: 8,
                                  ),
                                  decoration: BoxDecoration(
                                    color: Colors.white.withAlpha(210),
                                    borderRadius: BorderRadius.circular(16),
                                    border: Border.all(
                                      color: const Color(0xFF38BDF8),
                                      width: 1.5,
                                    ),
                                    boxShadow: const [
                                      BoxShadow(
                                        color: Color(0x220284C7),
                                        blurRadius: 10,
                                        offset: Offset(0, 3),
                                      ),
                                    ],
                                  ),
                                  child: Column(
                                    children: [
                                      Row(
                                        mainAxisSize: MainAxisSize.min,
                                        children: [
                                          Image.asset(
                                            'assets/images/gem.webp',
                                            width: 26,
                                            height: 26,
                                          ),
                                          const SizedBox(width: 8),
                                          Text(
                                            tr('diamond_bonus'),
                                            style: const TextStyle(
                                              color: Color(0xFF0369A1),
                                              fontSize: 18,
                                              fontWeight: FontWeight.w900,
                                            ),
                                          ),
                                        ],
                                      ),
                                      if (isStageComplete) ...[
                                        const SizedBox(height: 6),
                                        Row(
                                          mainAxisSize: MainAxisSize.min,
                                          children: [
                                            Image.asset(
                                              'assets/images/coin.webp',
                                              width: 24,
                                              height: 24,
                                            ),
                                            const SizedBox(width: 8),
                                            Text(
                                              tr('stage_coin_bonus'),
                                              style: const TextStyle(
                                                color: Color(0xFFD97706),
                                                fontSize: 15,
                                                fontWeight: FontWeight.w900,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ],
                                    ],
                                  ),
                                ),
                                SizedBox(height: isShort ? 12 : 18),
                                Row(
                                  children: [
                                    Expanded(
                                      child: LevelCompleteStatCard(
                                        label: tr('score'),
                                        value: '$score',
                                      ),
                                    ),
                                    const SizedBox(width: 14),
                                    Expanded(
                                      child: LevelCompleteStatCard(
                                        label: tr('accuracy'),
                                        value: '$accuracy%',
                                      ),
                                    ),
                                  ],
                                ),
                                SizedBox(height: isShort ? 18 : 24),
                                SizedBox(
                                  width: double.infinity,
                                  height: isShort ? 58 : 64,
                                  child: ElevatedButton(
                                    onPressed: withButtonFeedback(
                                      isExiting ? null : onNextPuzzle,
                                    ),
                                    style: ElevatedButton.styleFrom(
                                      elevation: 12,
                                      shadowColor: const Color(0x5520C997),
                                      backgroundColor: Colors.transparent,
                                      foregroundColor: Colors.white,
                                      disabledForegroundColor: Colors.white,
                                      disabledBackgroundColor:
                                          Colors.transparent,
                                      padding: EdgeInsets.zero,
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(24),
                                      ),
                                    ),
                                    child: Ink(
                                      decoration: BoxDecoration(
                                        borderRadius: BorderRadius.circular(24),
                                        gradient: const LinearGradient(
                                          begin: Alignment.topLeft,
                                          end: Alignment.bottomRight,
                                          colors: [
                                            Color(0xFF47E6A1),
                                            Color(0xFF20C997),
                                            Color(0xFF08A66D),
                                          ],
                                        ),
                                      ),
                                      child: Container(
                                        alignment: Alignment.center,
                                        padding: const EdgeInsets.symmetric(
                                          horizontal: 22,
                                        ),
                                        child: Row(
                                          mainAxisAlignment:
                                              MainAxisAlignment.center,
                                          children: [
                                            Expanded(
                                              child: Text(
                                                tr('next_puzzle'),
                                                textAlign: TextAlign.center,
                                                style: const TextStyle(
                                                  fontSize: 19,
                                                  fontWeight: FontWeight.w900,
                                                  color: Colors.white,
                                                ),
                                              ),
                                            ),
                                            Icon(
                                              Icons.chevron_right_rounded,
                                              size: 32,
                                              color: Colors.white,
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class LevelCompleteConfettiLayer extends StatefulWidget {
  const LevelCompleteConfettiLayer({super.key});

  @override
  State<LevelCompleteConfettiLayer> createState() =>
      _LevelCompleteConfettiLayerState();
}

class _LevelCompleteConfettiLayerState extends State<LevelCompleteConfettiLayer>
    with SingleTickerProviderStateMixin {
  late final Ticker _ticker;
  double _elapsed = 0.0;

  static const pieces = [
    ConfettiPieceSpec(
      startX: 0.08,
      delay: 0.04,
      speed: 0.72,
      rotationTurns: 0.55,
      color: Color(0xFF20C997),
      width: 5,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.18,
      delay: 0.42,
      speed: 0.62,
      rotationTurns: -0.44,
      color: Color(0xFFFFC400),
      width: 6,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.28,
      delay: 0.18,
      speed: 0.8,
      rotationTurns: 0.68,
      color: Color(0xFFFF9F1C),
      width: 5,
      height: 14,
    ),
    ConfettiPieceSpec(
      startX: 0.39,
      delay: 0.64,
      speed: 0.58,
      rotationTurns: -0.52,
      color: Color(0xFF54B7FF),
      width: 6,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.51,
      delay: 0.09,
      speed: 0.7,
      rotationTurns: 0.5,
      color: Color(0xFF20C997),
      width: 5,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.62,
      delay: 0.35,
      speed: 0.66,
      rotationTurns: -0.66,
      color: Color(0xFFFFC400),
      width: 6,
      height: 14,
    ),
    ConfettiPieceSpec(
      startX: 0.73,
      delay: 0.72,
      speed: 0.76,
      rotationTurns: 0.42,
      color: Color(0xFFFF9F1C),
      width: 5,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.85,
      delay: 0.24,
      speed: 0.6,
      rotationTurns: -0.5,
      color: Color(0xFF54B7FF),
      width: 6,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.13,
      delay: 0.78,
      speed: 0.54,
      rotationTurns: 0.45,
      color: Color(0xFF20C997),
      width: 5,
      height: 11,
    ),
    ConfettiPieceSpec(
      startX: 0.33,
      delay: 0.88,
      speed: 0.56,
      rotationTurns: -0.58,
      color: Color(0xFFFFC400),
      width: 5,
      height: 12,
    ),
    ConfettiPieceSpec(
      startX: 0.67,
      delay: 0.02,
      speed: 0.64,
      rotationTurns: 0.62,
      color: Color(0xFFFF9F1C),
      width: 6,
      height: 13,
    ),
    ConfettiPieceSpec(
      startX: 0.91,
      delay: 0.52,
      speed: 0.5,
      rotationTurns: -0.4,
      color: Color(0xFF54B7FF),
      width: 5,
      height: 11,
    ),
  ];

  @override
  void initState() {
    super.initState();
    _ticker = createTicker((elapsed) {
      setState(() {
        _elapsed = elapsed.inMilliseconds / 6200.0;
      });
    })..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: IgnorePointer(
        child: LayoutBuilder(
          builder: (context, constraints) {
            return Stack(
              children: [
                for (var index = 0; index < pieces.length; index++)
                  ConfettiPiece(
                    animationValue: _elapsed,
                    index: index,
                    spec: pieces[index],
                    canvasSize: Size(
                      constraints.maxWidth,
                      constraints.maxHeight,
                    ),
                  ),
              ],
            );
          },
        ),
      ),
    );
  }
}

class ConfettiPieceSpec {
  const ConfettiPieceSpec({
    required this.startX,
    required this.delay,
    required this.speed,
    required this.rotationTurns,
    required this.color,
    required this.width,
    required this.height,
  });

  final double startX;
  final double delay;
  final double speed;
  final double rotationTurns;
  final Color color;
  final double width;
  final double height;
}

class ConfettiPiece extends StatelessWidget {
  const ConfettiPiece({
    super.key,
    required this.animationValue,
    required this.index,
    required this.spec,
    required this.canvasSize,
  });

  final double animationValue;
  final int index;
  final ConfettiPieceSpec spec;
  final Size canvasSize;

  @override
  Widget build(BuildContext context) {
    final progress = (animationValue * spec.speed + spec.delay) % 1;
    final fallDistance = canvasSize.height + 80;
    final wobble = sin((progress * pi * 2) + index) * 8;
    final x = (canvasSize.width * spec.startX) + wobble;
    final y = -40 + (fallDistance * progress);
    final rotation = (progress * spec.rotationTurns * pi * 2) + (index * 0.18);

    return Positioned(
      left: x,
      top: y,
      child: Transform.rotate(
        angle: rotation,
        child: Opacity(
          opacity: 0.72,
          child: Container(
            width: spec.width,
            height: spec.height,
            decoration: BoxDecoration(
              color: spec.color,
              borderRadius: BorderRadius.circular(4),
            ),
          ),
        ),
      ),
    );
  }
}

class PinkPetalAnimationLayer extends StatefulWidget {
  const PinkPetalAnimationLayer({super.key});

  @override
  State<PinkPetalAnimationLayer> createState() =>
      _PinkPetalAnimationLayerState();
}

class _PinkPetalAnimationLayerState extends State<PinkPetalAnimationLayer>
    with SingleTickerProviderStateMixin {
  late final Ticker _ticker;
  double _elapsed = 0.0;

  static const petals = [
    PinkPetalSpec(
      startX: 0.08,
      delay: 0.04,
      speed: 0.38,
      drift: 18,
      rotationTurns: 0.42,
      width: 10,
      height: 20,
      color: Color(0xFFFF8FA2),
    ),
    PinkPetalSpec(
      startX: 0.21,
      delay: 0.36,
      speed: 0.34,
      drift: 14,
      rotationTurns: -0.36,
      width: 8,
      height: 17,
      color: Color(0xFFFFA0AF),
    ),
    PinkPetalSpec(
      startX: 0.34,
      delay: 0.16,
      speed: 0.4,
      drift: 20,
      rotationTurns: 0.5,
      width: 9,
      height: 19,
      color: Color(0xFFFF7F96),
    ),
    PinkPetalSpec(
      startX: 0.52,
      delay: 0.62,
      speed: 0.32,
      drift: 16,
      rotationTurns: -0.44,
      width: 8,
      height: 16,
      color: Color(0xFFFF9DAE),
    ),
    PinkPetalSpec(
      startX: 0.68,
      delay: 0.24,
      speed: 0.36,
      drift: 19,
      rotationTurns: 0.38,
      width: 11,
      height: 21,
      color: Color(0xFFFF899F),
    ),
    PinkPetalSpec(
      startX: 0.84,
      delay: 0.48,
      speed: 0.35,
      drift: 15,
      rotationTurns: -0.52,
      width: 8,
      height: 18,
      color: Color(0xFFFFA8B7),
    ),
    PinkPetalSpec(
      startX: 0.94,
      delay: 0.08,
      speed: 0.39,
      drift: 17,
      rotationTurns: 0.46,
      width: 9,
      height: 18,
      color: Color(0xFFFF7C94),
    ),
    PinkPetalSpec(
      startX: 0.14,
      delay: 0.72,
      speed: 0.33,
      drift: 13,
      rotationTurns: -0.4,
      width: 7,
      height: 16,
      color: Color(0xFFFF9BAD),
    ),
    PinkPetalSpec(
      startX: 0.43,
      delay: 0.86,
      speed: 0.37,
      drift: 21,
      rotationTurns: 0.56,
      width: 10,
      height: 20,
      color: Color(0xFFFF8299),
    ),
    PinkPetalSpec(
      startX: 0.59,
      delay: 0.12,
      speed: 0.31,
      drift: 12,
      rotationTurns: -0.34,
      width: 8,
      height: 17,
      color: Color(0xFFFFB0BE),
    ),
    PinkPetalSpec(
      startX: 0.76,
      delay: 0.78,
      speed: 0.41,
      drift: 18,
      rotationTurns: 0.44,
      width: 9,
      height: 19,
      color: Color(0xFFFF7891),
    ),
    PinkPetalSpec(
      startX: 0.9,
      delay: 0.58,
      speed: 0.35,
      drift: 16,
      rotationTurns: -0.48,
      width: 7,
      height: 15,
      color: Color(0xFFFFA3B2),
    ),
  ];

  @override
  void initState() {
    super.initState();
    _ticker = createTicker((elapsed) {
      setState(() {
        _elapsed = elapsed.inMilliseconds / 7600.0;
      });
    })..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: IgnorePointer(
        child: LayoutBuilder(
          builder: (context, constraints) {
            return Stack(
              children: [
                for (var index = 0; index < petals.length; index++)
                  PinkPetal(
                    animationValue: _elapsed,
                    index: index,
                    spec: petals[index],
                    canvasSize: Size(
                      constraints.maxWidth,
                      constraints.maxHeight,
                    ),
                  ),
              ],
            );
          },
        ),
      ),
    );
  }
}

class PinkPetalSpec {
  const PinkPetalSpec({
    required this.startX,
    required this.delay,
    required this.speed,
    required this.drift,
    required this.rotationTurns,
    required this.width,
    required this.height,
    required this.color,
  });

  final double startX;
  final double delay;
  final double speed;
  final double drift;
  final double rotationTurns;
  final double width;
  final double height;
  final Color color;
}

class PinkPetal extends StatelessWidget {
  const PinkPetal({
    super.key,
    required this.animationValue,
    required this.index,
    required this.spec,
    required this.canvasSize,
  });

  final double animationValue;
  final int index;
  final PinkPetalSpec spec;
  final Size canvasSize;

  @override
  Widget build(BuildContext context) {
    final progress = (animationValue * spec.speed + spec.delay) % 1;
    final fallDistance = canvasSize.height + 70;
    final wobble = sin((progress * pi * 2) + index) * spec.drift;
    final x = (canvasSize.width * spec.startX) + wobble;
    final y = -42 + (fallDistance * progress);
    final rotation = (progress * spec.rotationTurns * pi * 2) + (index * 0.26);

    return Positioned(
      left: x,
      top: y,
      child: Transform.rotate(
        angle: rotation,
        child: Opacity(
          opacity: 0.72,
          child: Container(
            width: spec.width,
            height: spec.height,
            decoration: BoxDecoration(
              color: spec.color,
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(spec.width),
                topRight: Radius.circular(spec.width),
                bottomLeft: Radius.circular(spec.width),
                bottomRight: Radius.circular(2),
              ),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x22E85D75),
                  blurRadius: 4,
                  offset: Offset(0, 2),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class LevelCompleteStatCard extends StatelessWidget {
  const LevelCompleteStatCard({
    super.key,
    required this.label,
    required this.value,
  });

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 86,
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(205),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.white.withAlpha(178)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x182178BA),
            blurRadius: 12,
            offset: Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            label,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Color(0xFF172D56),
              fontSize: 13,
              fontWeight: FontWeight.w500,
            ),
          ),
          const SizedBox(height: 5),
          Text(
            value,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Color(0xFF08A66D),
              fontSize: 28,
              fontWeight: FontWeight.w900,
              height: 1,
            ),
          ),
        ],
      ),
    );
  }
}

class WrongAnswerScreen extends StatelessWidget {
  const WrongAnswerScreen({
    super.key,
    required this.selectedAnswer,
    required this.correctAnswer,
    required this.explanation,
    required this.isExiting,
    this.continueLabel = 'Continue',
    required this.onContinue,
    required this.onBackToHome,
  });

  final String selectedAnswer;
  final String correctAnswer;
  final String explanation;
  final bool isExiting;
  final String continueLabel;
  final VoidCallback onContinue;
  final VoidCallback onBackToHome;

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: TweenAnimationBuilder<double>(
        tween: Tween<double>(begin: isExiting ? 1 : 0, end: isExiting ? 0 : 1),
        duration: Duration(milliseconds: isExiting ? 360 : 620),
        curve: isExiting ? Curves.easeInCubic : Curves.easeOutCubic,
        builder: (context, value, child) {
          final opacity = value.clamp(0.0, 1.0);
          final scale = 0.96 + (value * 0.04);
          final slideOffset = Offset(0, 22 * (1 - value));

          return Opacity(
            opacity: opacity,
            child: Transform.translate(
              offset: slideOffset,
              child: Transform.scale(scale: scale, child: child),
            ),
          );
        },
        child: Material(
          color: Colors.transparent,
          child: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/wrong_ans_bg.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              const PinkPetalAnimationLayer(),
              SafeArea(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.fromLTRB(24, 26, 24, 28),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          const WrongAnswerHeroIcon(),
                          const SizedBox(height: 18),
                          Text(
                            tr('wrong_answer'),
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              color: Color(0xFF0E2754),
                              fontSize: 31,
                              fontWeight: FontWeight.w900,
                              height: 1.05,
                            ),
                          ),
                          const SizedBox(height: 8),
                          const Text(
                            "Oops! That's not the right one.",
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              color: Color(0xFF223A63),
                              fontSize: 16,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                          const SizedBox(height: 24),
                          Row(
                            children: [
                              Expanded(
                                child: WrongAnswerChoiceCard(
                                  label: tr('wrong_answer'),
                                  answer: selectedAnswer,
                                  icon: Icons.close_rounded,
                                  accentColor: const Color(0xFFFF4A63),
                                  bubbleColor: const Color(0xFFFFCDD4),
                                ),
                              ),
                              const SizedBox(width: 14),
                              Expanded(
                                child: WrongAnswerChoiceCard(
                                  label: tr('correct_answer'),
                                  answer: correctAnswer,
                                  icon: Icons.check_rounded,
                                  accentColor: Color(0xFF18B978),
                                  bubbleColor: Color(0xFFD9F2CC),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 14),
                          WrongAnswerInfoCard(explanation: explanation),
                          const SizedBox(height: 14),
                          const WrongAnswerPracticeCard(),
                          const SizedBox(height: 18),
                          SizedBox(
                            height: 64,
                            child: ElevatedButton.icon(
                              onPressed: withButtonFeedback(
                                isExiting ? null : onContinue,
                              ),
                              icon: const Icon(
                                Icons.arrow_forward_rounded,
                                color: Colors.white,
                                size: 28,
                              ),
                              label: Text(
                                continueLabel,
                                style: const TextStyle(
                                  fontSize: 22,
                                  fontWeight: FontWeight.w900,
                                  color: Colors.white,
                                ),
                              ),
                              style: ElevatedButton.styleFrom(
                                elevation: 12,
                                shadowColor: const Color(0x55F5314F),
                                backgroundColor: const Color(0xFFF5314F),
                                foregroundColor: Colors.white,
                                disabledForegroundColor: Colors.white,
                                disabledBackgroundColor: const Color(
                                  0xFFF5314F,
                                ),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(24),
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(height: 16),
                          SizedBox(
                            height: 56,
                            child: ElevatedButton.icon(
                              onPressed: withButtonFeedback(
                                isExiting ? null : onBackToHome,
                              ),
                              icon: const Icon(
                                Icons.home_rounded,
                                color: Color(0xFF3B466A),
                                size: 27,
                              ),
                              label: const Text(
                                'Back to Home',
                                style: TextStyle(
                                  fontSize: 18,
                                  fontWeight: FontWeight.w900,
                                  color: Color(0xFF3B466A),
                                ),
                              ),
                              style: ElevatedButton.styleFrom(
                                elevation: 8,
                                shadowColor: const Color(0x22000000),
                                backgroundColor: Colors.white,
                                foregroundColor: const Color(0xFF3B466A),
                                disabledForegroundColor: const Color(
                                  0xFF3B466A,
                                ),
                                disabledBackgroundColor: Colors.white,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(24),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class TimeOutScreen extends StatelessWidget {
  const TimeOutScreen({
    super.key,
    required this.selectedAnswer,
    required this.correctAnswer,
    required this.isExiting,
    this.continueLabel = 'Continue',
    required this.onContinue,
    required this.onBackToHome,
  });

  final String selectedAnswer;
  final String correctAnswer;
  final bool isExiting;
  final String continueLabel;
  final VoidCallback onContinue;
  final VoidCallback onBackToHome;

  @override
  Widget build(BuildContext context) {
    return Positioned.fill(
      child: TweenAnimationBuilder<double>(
        tween: Tween<double>(begin: isExiting ? 1 : 0, end: isExiting ? 0 : 1),
        duration: Duration(milliseconds: isExiting ? 360 : 620),
        curve: isExiting ? Curves.easeInCubic : Curves.easeOutCubic,
        builder: (context, value, child) {
          final opacity = value.clamp(0.0, 1.0);
          final scale = 0.96 + (value * 0.04);
          final slideOffset = Offset(0, 22 * (1 - value));

          return Opacity(
            opacity: opacity,
            child: Transform.translate(
              offset: slideOffset,
              child: Transform.scale(scale: scale, child: child),
            ),
          );
        },
        child: Material(
          color: Colors.transparent,
          child: Stack(
            children: [
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/wrong_ans_bg.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                ),
              ),
              const PinkPetalAnimationLayer(),
              SafeArea(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 430),
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.fromLTRB(24, 24, 24, 28),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          const TimeOutHeroIcon(),
                          const SizedBox(height: 18),
                          Text(
                            tr('time_out'),
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              color: Color(0xFF0E2754),
                              fontSize: 36,
                              fontWeight: FontWeight.w900,
                              height: 1.05,
                            ),
                          ),
                          const SizedBox(height: 8),
                          const Text(
                            'The time ran out. Better luck next time!',
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              color: Color(0xFF52607E),
                              fontSize: 16,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                          const SizedBox(height: 24),
                          Row(
                            children: [
                              Expanded(
                                child: WrongAnswerChoiceCard(
                                  label: 'Your Answer',
                                  answer: selectedAnswer,
                                  icon: Icons.close_rounded,
                                  accentColor: Color(0xFFFF4A63),
                                  bubbleColor: Color(0xFFFFCDD4),
                                ),
                              ),
                              const SizedBox(width: 14),
                              Expanded(
                                child: WrongAnswerChoiceCard(
                                  label: 'Correct Answer',
                                  answer: correctAnswer,
                                  icon: Icons.check_rounded,
                                  accentColor: Color(0xFF18B978),
                                  bubbleColor: Color(0xFFD9F2CC),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 14),
                          const TimeOutDetailCard(
                            icon: Icons.hourglass_bottom_rounded,
                            iconColor: Color(0xFF8055D8),
                            title: "Time's Up!",
                            message:
                                'You took too long to answer.\nPractice more to improve your speed!',
                          ),
                          const SizedBox(height: 14),
                          const TimeOutDetailCard(
                            icon: Icons.lightbulb_rounded,
                            iconColor: Color(0xFFFFC928),
                            title: 'Quick Tip',
                            message:
                                'Try to read the question carefully and answer faster next time!',
                          ),
                          const SizedBox(height: 18),
                          SizedBox(
                            height: 64,
                            child: ElevatedButton.icon(
                              onPressed: withButtonFeedback(
                                isExiting ? null : onContinue,
                              ),
                              icon: const Icon(
                                Icons.arrow_forward_rounded,
                                color: Colors.white,
                                size: 28,
                              ),
                              label: Text(
                                continueLabel,
                                style: const TextStyle(
                                  fontSize: 22,
                                  fontWeight: FontWeight.w900,
                                  color: Colors.white,
                                ),
                              ),
                              style: ElevatedButton.styleFrom(
                                elevation: 12,
                                shadowColor: const Color(0x55F5314F),
                                backgroundColor: const Color(0xFFF5314F),
                                foregroundColor: Colors.white,
                                disabledForegroundColor: Colors.white,
                                disabledBackgroundColor: const Color(
                                  0xFFF5314F,
                                ),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(24),
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(height: 16),
                          SizedBox(
                            height: 56,
                            child: ElevatedButton.icon(
                              onPressed: withButtonFeedback(
                                isExiting ? null : onBackToHome,
                              ),
                              icon: const Icon(
                                Icons.home_rounded,
                                color: Color(0xFF3B466A),
                                size: 27,
                              ),
                              label: const Text(
                                'Back to Home',
                                style: TextStyle(
                                  fontSize: 18,
                                  fontWeight: FontWeight.w900,
                                  color: Color(0xFF3B466A),
                                ),
                              ),
                              style: ElevatedButton.styleFrom(
                                elevation: 8,
                                shadowColor: const Color(0x22000000),
                                backgroundColor: Colors.white,
                                foregroundColor: const Color(0xFF3B466A),
                                disabledForegroundColor: const Color(
                                  0xFF3B466A,
                                ),
                                disabledBackgroundColor: Colors.white,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(24),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class TimeOutHeroIcon extends StatelessWidget {
  const TimeOutHeroIcon({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        width: 112,
        height: 112,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          gradient: const LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFFFFC3CB), Color(0xFFFF6B7E)],
          ),
          border: Border.all(color: Color(0xFFE93551), width: 5),
          boxShadow: const [
            BoxShadow(
              color: Color(0x44F5314F),
              blurRadius: 28,
              offset: Offset(0, 14),
            ),
          ],
        ),
        child: const Icon(
          Icons.alarm_rounded,
          color: Color(0xFFE93551),
          size: 66,
        ),
      ),
    );
  }
}

class TimeOutDetailCard extends StatelessWidget {
  const TimeOutDetailCard({
    super.key,
    required this.icon,
    required this.iconColor,
    required this.title,
    required this.message,
  });

  final IconData icon;
  final Color iconColor;
  final String title;
  final String message;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 17, 18, 17),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(128),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withAlpha(128)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x182178BA),
            blurRadius: 14,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: Row(
        children: [
          Icon(icon, color: iconColor, size: 46),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    color: Color(0xFF172D56),
                    fontSize: 16,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                const SizedBox(height: 7),
                Text(
                  message,
                  style: const TextStyle(
                    color: Color(0xFF223A63),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.38,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class WrongAnswerHeroIcon extends StatelessWidget {
  const WrongAnswerHeroIcon({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        width: 102,
        height: 102,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          gradient: const LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFFFFC3CB), Color(0xFFFF6B7E)],
          ),
          border: Border.all(color: Color(0xFFE93551), width: 5),
          boxShadow: const [
            BoxShadow(
              color: Color(0x44F5314F),
              blurRadius: 28,
              offset: Offset(0, 14),
            ),
          ],
        ),
        child: const Icon(
          Icons.close_rounded,
          color: Color(0xFFE93551),
          size: 56,
        ),
      ),
    );
  }
}

class WrongAnswerChoiceCard extends StatelessWidget {
  const WrongAnswerChoiceCard({
    super.key,
    required this.label,
    required this.answer,
    required this.icon,
    required this.accentColor,
    required this.bubbleColor,
  });

  final String label;
  final String answer;
  final IconData icon;
  final Color accentColor;
  final Color bubbleColor;

  @override
  Widget build(BuildContext context) {
    return Container(
      constraints: const BoxConstraints(minHeight: 132),
      padding: const EdgeInsets.fromLTRB(10, 10, 10, 10),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(128),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.white.withAlpha(128)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x182178BA),
            blurRadius: 12,
            offset: Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            width: 34,
            height: 34,
            decoration: BoxDecoration(
              color: bubbleColor,
              shape: BoxShape.circle,
            ),
            child: Icon(icon, color: accentColor, size: 25),
          ),
          const SizedBox(height: 6),
          Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            textAlign: TextAlign.center,
            style: TextStyle(
              color: accentColor,
              fontSize: 16,
              fontWeight: FontWeight.w900,
            ),
          ),
          const SizedBox(height: 5),
          FittedBox(
            fit: BoxFit.scaleDown,
            child: Text(
              answer,
              maxLines: 1,
              textAlign: TextAlign.center,
              style: const TextStyle(
                color: Color(0xFF172D56),
                fontSize: 16,
                fontWeight: FontWeight.w700,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class WrongAnswerInfoCard extends StatelessWidget {
  const WrongAnswerInfoCard({super.key, required this.explanation});

  final String explanation;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 18, 18, 18),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(128),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withAlpha(128)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x182178BA),
            blurRadius: 14,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const Icon(
            Icons.lightbulb_rounded,
            color: Color(0xFFFFC928),
            size: 46,
            shadows: [
              Shadow(
                color: Color(0x558B6A00),
                blurRadius: 8,
                offset: Offset(0, 3),
              ),
            ],
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Text(
                      'Explanation',
                      style: TextStyle(
                        color: Color(0xFF172D56),
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Container(
                        height: 2,
                        decoration: BoxDecoration(
                          color: const Color(0xFFE9C9D6),
                          borderRadius: BorderRadius.circular(999),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                Text(
                  explanation,
                  style: const TextStyle(
                    color: Color(0xFF223A63),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.34,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class WrongAnswerPracticeCard extends StatelessWidget {
  const WrongAnswerPracticeCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 17, 18, 17),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(128),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withAlpha(128)),
        boxShadow: const [
          BoxShadow(
            color: Color(0x182178BA),
            blurRadius: 14,
            offset: Offset(0, 6),
          ),
        ],
      ),
      child: const Row(
        children: [
          Icon(Icons.emoji_events_rounded, color: Color(0xFFE85D75), size: 44),
          SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Keep Practicing!',
                  style: TextStyle(
                    color: Color(0xFF172D56),
                    fontSize: 16,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                SizedBox(height: 5),
                Text(
                  "You'll get even better.",
                  style: TextStyle(
                    color: Color(0xFF223A63),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class ResultTransitionOverlay extends StatefulWidget {
  const ResultTransitionOverlay({
    super.key,
    required this.isCorrect,
    required this.isExiting,
  });

  final bool isCorrect;
  final bool isExiting;

  @override
  State<ResultTransitionOverlay> createState() =>
      _ResultTransitionOverlayState();
}

class _ResultTransitionOverlayState extends State<ResultTransitionOverlay>
    with SingleTickerProviderStateMixin {
  late final AnimationController controller;
  late final Animation<double> fadeAnimation;
  late final Animation<double> scaleAnimation;

  @override
  void initState() {
    super.initState();
    controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 520),
      reverseDuration: const Duration(milliseconds: 460),
    );
    final curvedAnimation = CurvedAnimation(
      parent: controller,
      curve: Curves.easeOutBack,
      reverseCurve: Curves.easeInCubic,
    );
    fadeAnimation = CurvedAnimation(
      parent: controller,
      curve: Curves.easeOutCubic,
      reverseCurve: Curves.easeInCubic,
    );
    scaleAnimation = Tween<double>(
      begin: 0.86,
      end: 1,
    ).animate(curvedAnimation);
    controller.forward();
  }

  @override
  void didUpdateWidget(ResultTransitionOverlay oldWidget) {
    super.didUpdateWidget(oldWidget);

    if (!oldWidget.isExiting && widget.isExiting) {
      controller.reverse();
    }
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final accentColor = widget.isCorrect
        ? const Color(0xFF7CFFCB)
        : const Color(0xFFFF5A6A);
    final title = widget.isCorrect ? 'Level Complete!' : 'Wrong!';
    final subtitle = widget.isCorrect ? '+10 Score' : 'No Score';

    return Positioned.fill(
      child: IgnorePointer(
        child: Material(
          color: Colors.transparent,
          child: Container(
            color: const Color(0xCC050711),
            child: Center(
              child: FadeTransition(
                opacity: fadeAnimation,
                child: ScaleTransition(
                  scale: scaleAnimation,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        title,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: widget.isCorrect ? Colors.white : accentColor,
                          fontSize: widget.isCorrect ? 34 : 38,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0,
                          shadows: [
                            Shadow(
                              color: accentColor,
                              blurRadius: 22,
                              offset: const Offset(0, 4),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 12),
                      Text(
                        subtitle,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: accentColor,
                          fontSize: 18,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 0,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class LivesDisplay extends StatelessWidget {
  const LivesDisplay({super.key, required this.lives});

  final int lives;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var index = 0; index < lives; index++) ...[
          const Icon(
            Icons.favorite_rounded,
            size: 17,
            color: Color(0xFFE84A5F),
            shadows: [
              Shadow(
                color: Color(0x88E53935),
                blurRadius: 8,
                offset: Offset(0, 2),
              ),
            ],
          ),
          if (index != lives - 1) const SizedBox(width: 5),
        ],
      ],
    );
  }
}

class ProgressHeader extends StatelessWidget {
  const ProgressHeader({
    super.key,
    required this.currentPuzzle,
    required this.totalPuzzles,
    this.timerSeconds,
    this.theme,
  });

  final int currentPuzzle;
  final int totalPuzzles;
  final int? timerSeconds;
  final LevelTheme? theme;

  @override
  Widget build(BuildContext context) {
    final progress = currentPuzzle / totalPuzzles;
    final activeTheme = theme ?? levelThemeForStage(2);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            AnimatedSwitcher(
              duration: const Duration(milliseconds: 320),
              switchInCurve: Curves.easeOutCubic,
              switchOutCurve: Curves.easeInCubic,
              child: Text(
                '${tr('level')} ${formatNumber(currentPuzzle)}',
                key: ValueKey(currentPuzzle),
                textAlign: TextAlign.left,
                style: TextStyle(
                  fontFamily: 'Roboto',
                  fontSize: 20,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0,
                  color: activeTheme.titleColor,
                  shadows: [
                    Shadow(
                      color: activeTheme.titleShadow,
                      blurRadius: 8,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
              ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(
                horizontal: 14,
                vertical: 6,
              ),
              decoration: BoxDecoration(
                color: activeTheme.accentDark.withAlpha(220),
                borderRadius: BorderRadius.circular(999),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x33000000),
                    blurRadius: 6,
                    offset: Offset(0, 2),
                  ),
                ],
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.stars_rounded, size: 16, color: Color(0xFFFFD700)),
                  const SizedBox(width: 5),
                  Text(
                    '${formatNumber(currentPuzzle)} / ${formatNumber(totalPuzzles)}',
                    style: const TextStyle(
                      fontFamily: 'Roboto',
                      fontSize: 14,
                      fontWeight: FontWeight.w800,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 24),
        Container(
          padding: const EdgeInsets.only(left: 8, top: 4, bottom: 4),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(100),
            borderRadius: BorderRadius.circular(999),
          ),
          child: Row(
            children: [
              Expanded(
                child: TweenAnimationBuilder<double>(
                  tween: Tween<double>(begin: 0, end: progress),
                  duration: const Duration(milliseconds: 620),
                  curve: Curves.easeOutCubic,
                  builder: (context, animatedProgress, _) {
                    return ClipRRect(
                      borderRadius: BorderRadius.circular(999),
                      child: LinearProgressIndicator(
                        value: animatedProgress,
                        minHeight: 12,
                        backgroundColor: const Color(0x66D4E6FA),
                        valueColor: AlwaysStoppedAnimation<Color>(
                          activeTheme.accent,
                        ),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(width: 12),
              AnimatedSwitcher(
                duration: const Duration(milliseconds: 260),
                child: Container(
                  key: ValueKey(currentPuzzle),
                  padding: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 4,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.white.withAlpha(118),
                    borderRadius: BorderRadius.circular(999),
                  ),
                  child: Text(
                    '${formatNumber(currentPuzzle)} / ${formatNumber(totalPuzzles)}',
                    style: const TextStyle(
                      fontFamily: 'Roboto',
                      fontSize: 18,
                      fontWeight: FontWeight.w800,
                      color: Color(0xFF5B76A8),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class ResultBadge extends StatelessWidget {
  const ResultBadge({super.key, required this.isCorrect});

  final bool isCorrect;

  @override
  Widget build(BuildContext context) {
    final color = isCorrect ? const Color(0xFF00C853) : const Color(0xFFE53935);
    final icon = isCorrect ? Icons.check_rounded : Icons.close_rounded;
    final label = isCorrect ? 'Correct!' : 'Wrong Answer';

    return Center(
      key: ValueKey(label),
      child: Container(
        height: 44,
        padding: const EdgeInsets.symmetric(horizontal: 18),
        decoration: BoxDecoration(
          color: color.withAlpha(230),
          borderRadius: BorderRadius.circular(999),
          border: Border.all(color: Colors.white.withAlpha(46)),
          boxShadow: [
            BoxShadow(
              color: color.withAlpha(88),
              blurRadius: 16,
              offset: const Offset(0, 6),
            ),
          ],
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, color: Colors.white, size: 20),
            const SizedBox(width: 7),
            Text(
              label,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 16,
                fontWeight: FontWeight.w800,
                letterSpacing: 0,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class AnswerButton extends StatefulWidget {
  const AnswerButton({
    super.key,
    required this.label,
    required this.onPressed,
    required this.backgroundColor,
    required this.isEnabled,
    this.isSelectedCorrect = false,
    this.icon,
  });

  final String label;
  final VoidCallback onPressed;
  final Color backgroundColor;
  final bool isEnabled;
  final bool isSelectedCorrect;
  final IconData? icon;

  @override
  State<AnswerButton> createState() => _AnswerButtonState();
}

class _AnswerButtonState extends State<AnswerButton> {
  bool isPressed = false;

  void setPressed(bool value) {
    if (isPressed == value || (value && !widget.isEnabled)) {
      return;
    }

    setState(() {
      isPressed = value;
    });
  }

  void handleTap() {
    if (!widget.isEnabled) {
      return;
    }

    triggerButtonFeedback();
    widget.onPressed();
  }

  @override
  Widget build(BuildContext context) {
    return Listener(
      onPointerDown: (_) => setPressed(true),
      onPointerUp: (_) => setPressed(false),
      onPointerCancel: (_) => setPressed(false),
      child: AnimatedScale(
        scale: widget.isSelectedCorrect ? 1.05 : (isPressed ? 0.97 : 1),
        duration: const Duration(milliseconds: 180),
        curve: Curves.easeOutCubic,
        child: SizedBox(
          height: 54,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 340),
            curve: Curves.easeOutCubic,
            decoration: BoxDecoration(
              color: widget.backgroundColor,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: const Color(
                    0x553D35D8,
                  ).withAlpha(widget.isEnabled ? 85 : 28),
                  blurRadius: widget.isEnabled ? 12 : 5,
                  offset: Offset(0, widget.isEnabled ? 5 : 2),
                ),
              ],
            ),
            child: Material(
              color: Colors.transparent,
              child: InkWell(
                onTap: widget.isEnabled ? handleTap : null,
                borderRadius: BorderRadius.circular(16),
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 18),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const SizedBox(width: 30),
                      Expanded(
                        child: Text(
                          widget.label,
                          textAlign: TextAlign.center,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.w800,
                            letterSpacing: 0,
                          ),
                        ),
                      ),
                      SizedBox(
                        width: 30,
                        child: AnimatedSwitcher(
                          duration: const Duration(milliseconds: 260),
                          reverseDuration: const Duration(milliseconds: 180),
                          switchInCurve: Curves.easeOutCubic,
                          switchOutCurve: Curves.easeInCubic,
                          transitionBuilder: (child, animation) {
                            return FadeTransition(
                              opacity: animation,
                              child: ScaleTransition(
                                scale: Tween<double>(
                                  begin: 0.76,
                                  end: 1,
                                ).animate(animation),
                                child: child,
                              ),
                            );
                          },
                          child: widget.icon == null
                              ? const SizedBox(
                                  key: ValueKey('empty-icon'),
                                  width: 30,
                                  height: 22,
                                )
                              : Icon(
                                  widget.icon,
                                  key: ValueKey(widget.icon),
                                  size: 22,
                                  color: Colors.white,
                                ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
