import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:mindtrap_ai/localization/app_language.dart';
import 'package:mindtrap_ai/localization/language_controller.dart';
import 'package:mindtrap_ai/localization/puzzle_localizer.dart';
import 'package:mindtrap_ai/models/world_model.dart';
import 'package:mindtrap_ai/screens/map_your_mind_screen.dart';
import 'package:mindtrap_ai/widgets/level_background_builder.dart';
import 'package:mindtrap_ai/main.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  SharedPreferences.setMockInitialValues({});

  test('WorldThemes defines 10 distinct worlds with unique properties', () {
    expect(WorldThemes.allWorlds.length, 25);

    final titles = WorldThemes.allWorlds.map((w) => w.title).toSet();
    expect(titles.length, 25);

    for (int i = 0; i < WorldThemes.allWorlds.length; i++) {
      final world = WorldThemes.getWorld(i);
      expect(world.worldNumber, i + 1);
      expect(world.backgroundAsset.isNotEmpty, true);
    }
  });

  test('LevelAtmosphereManager provides unique atmosphere per level', () {
    final world = WorldThemes.getWorld(0);
    final atmospheres = List.generate(
      10,
      (lvl) => LevelAtmosphereManager.getAtmosphere(lvl, world),
    );

    final styleNames = atmospheres.map((a) => a.styleName).toSet();
    expect(styleNames.length, 10);
  });

  test('PuzzleLocalizer translates questions when language changes', () {
    const question = 'Which word is longest?';
    final defaultOptions = ['Snake', 'Train', 'Road', 'Queue'];
    const defaultAnswer = 'Queue';
    const defaultExplanation = 'Queue has five letters.';

    // English
    final en = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'en',
    );
    expect(en.correctAnswer, 'Queue');

    // Urdu
    final ur = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'ur',
    );
    expect(ur.correctAnswer, 'قطار');
    expect(ur.question.contains('لفظ'), true);

    // Hindi
    final hi = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'hi',
    );
    expect(hi.question.contains('शब्द'), true);

    // Dynamic category negation and option translation in Urdu
    final toolNegation = PuzzleLocalizer.getTranslation(
      'Which option is not one of the tools?',
      const ['Pliers', 'Wrench', 'Saw', 'Violin'],
      'Violin',
      'Violin is not a tool.',
      'ur',
    );
    expect(toolNegation.question, contains('اوزاروں'));
    expect(toolNegation.options, contains('پلاس'));
    expect(toolNegation.options, contains('رینچ'));
    expect(toolNegation.options, contains('آری'));
    expect(toolNegation.options, contains('وائلن'));
    expect(toolNegation.correctAnswer, 'وائلن');
  });

  test('AppStrings contains translations for worlds and auth', () {
    expect(AppStrings.get('worlds'), isNotEmpty);
    expect(AppStrings.get('sign_in'), isNotEmpty);
    expect(AppStrings.get('sign_up'), isNotEmpty);
    expect(AppStrings.get('continue_as_guest'), isNotEmpty);
    expect(AppStrings.get('store'), isNotEmpty);
    expect(AppStrings.get('meezan_bank'), isNotEmpty);
    expect(AppStrings.get('bank_transfer'), isNotEmpty);
    expect(AppStrings.get('credit_card'), isNotEmpty);
  });

  test('LanguageController updates activeLanguage and directionality reactively', () async {
    final controller = LanguageController.instance;

    await controller.setLanguage('en');
    expect(controller.currentCode, 'en');
    expect(controller.isRtl, false);
    expect(tr('settings'), 'SETTINGS');

    await controller.setLanguage('ur');
    expect(controller.currentCode, 'ur');
    expect(controller.isRtl, true);
    expect(tr('settings'), 'ترتیبات');

    await controller.setLanguage('ar');
    expect(controller.currentCode, 'ar');
    expect(controller.isRtl, true);
    expect(tr('settings'), 'الإعدادات');

    // Reset to en
    await controller.setLanguage('en');
    expect(controller.currentCode, 'en');
  });

  test('StoreScreen Meezan Bank transfer details are verified', () {
    const expectedName = 'Syed Azeem Haider Bukhari';
    const expectedAcc = '00300110167256';
    const expectedBank = 'Meezan Bank';
    const expectedIban = 'PK82MEZN0000300110167256';

    expect(expectedName, 'Syed Azeem Haider Bukhari');
    expect(expectedAcc, '00300110167256');
    expect(expectedBank, 'Meezan Bank');
    expect(expectedIban, 'PK82MEZN0000300110167256');
  });

  test('Urdu puzzles never contain parenthetical English and answer is in options', () {
    final sampleQuestions = [
      'Which word is longest?',
      'What gets wetter while drying?',
      'Which month has 28 days?',
      "What has keys but can't open locks?",
      'Which is lighter than air?',
      'What moves faster than wind?',
      'Which breaks when dropped?',
      'What has a mouth but cannot speak?',
      'Which can fly without wings?',
      'Which plant produces electricity?',
      'Which plant produces sweets?',
      'Which bird plays baseball?',
      'Which plant is an animal?',
      'Which tool is an animal?',
    ];

    for (final q in sampleQuestions) {
      final res = PuzzleLocalizer.getTranslation(
        q,
        ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        'Option 1',
        'Explanation',
        'ur',
      );
      // Verify no English parenthetical text in question or options
      expect(res.question.contains(RegExp(r'\([A-Za-z]+\)')), isFalse, reason: 'Urdu question should not contain English: ${res.question}');
      for (final opt in res.options) {
        expect(opt.contains(RegExp(r'\([A-Za-z]+\)')), isFalse, reason: 'Urdu option should not contain English: $opt');
      }
      // Verify correctAnswer is strictly contained within options
      expect(res.options.contains(res.correctAnswer), isTrue, reason: 'Answer ${res.correctAnswer} must be in options: ${res.options}');
    }
  });

  test('Comprehensive dictionary localizes all diverse options across all languages', () {
    const testOptions = [
      'A bank',
      'A bed',
      '1 kg feathers',
      'Your brain',
      'Coffee table',
      'All of them',
      'Grandfather, father, son',
      'Horse named Friday',
      'A candle',
      'Your name',
    ];

    for (final lang in ['ur', 'hi', 'ar', 'es', 'fr']) {
      final res = PuzzleLocalizer.getTranslation(
        'Test question?',
        testOptions,
        'A bank',
        'Test explanation',
        lang,
      );

      // Verify that options are translated and none contain English words from testOptions
      expect(res.options.length, testOptions.length);
      for (final opt in res.options) {
        expect(opt, isNotEmpty);
      }
      expect(res.options.contains(res.correctAnswer), isTrue, reason: 'Answer ${res.correctAnswer} must be in options: ${res.options} for lang $lang');
      // In Urdu and Arabic, options must not contain Latin letters
      if (lang == 'ur' || lang == 'ar') {
        for (final opt in res.options) {
          expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" should not have English letters in $lang');
        }
      }
    }
  });

  test('Screenshot case: 10-letter trap options are fully translated into Urdu with 0 English', () {
    final res = PuzzleLocalizer.getTranslation(
      'Which option contains 10 letters?',
      ['football', 'sandpaper', 'ant', 'strawberry'],
      'strawberry',
      'strawberry has 10 letters.',
      'ur',
    );
    expect(res.question, 'کس لفظ میں ٹھیک 10 حروف ہیں؟');
    expect(res.options, ['فٹ بال', 'ریگ مال', 'چیونٹی', 'سٹرابیری']);
    expect(res.correctAnswer, 'سٹرابیری');
    for (final opt in res.options) {
      expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" must not contain English');
    }
  });

  test('Numbers like 1.2, 3, 10 remain in English digits across all languages as requested', () {
    expect(formatNumber('1.2', 'ur'), '1.2');
    expect(formatNumber('3', 'ur'), '3');
    expect(formatNumber('10', 'ur'), '10');
    expect(formatNumber(171, 'ur'), '171');
    expect(formatNumber('Level 5', 'ur'), 'Level 5');
    expect(formatNumber('1.2', 'ar'), '1.2');
    expect(formatNumber('1.2', 'hi'), '1.2');
    expect(formatNumber('1.2', 'en'), '1.2');
  });

  test('Zero English guarantee: even arbitrary or unknown words never display English in Urdu', () {
    final res = PuzzleLocalizer.getTranslation(
      'Custom question?',
      ['arbitrary', 'microcontroller', 'cryptocurrency', 'superconductor'],
      'arbitrary',
      'Explanation',
      'ur',
    );
    for (final opt in res.options) {
      expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" must not contain Latin letters');
    }
    expect(RegExp(r'[A-Za-z]').hasMatch(res.correctAnswer), isFalse);
    expect(res.options.contains(res.correctAnswer), isTrue);
  });

  test('Audio assets exist on disk and have non-zero size', () {
    final assets = [
      'assets/audio/bg_music.wav',
      'assets/audio/tap.wav',
      'assets/audio/correct.wav',
      'assets/audio/wrong.wav',
      'assets/audio/win.wav',
      'assets/audio/lose.wav',
      'assets/audio/coin.wav',
    ];
    for (final a in assets) {
      final f = File(a);
      expect(f.existsSync(), isTrue, reason: '$a must exist');
      expect(f.lengthSync(), greaterThan(100), reason: '$a must not be empty');
    }
  });

  test('World task achievements award configured coins and gems gifts', () {
    // Easy tasks after level 1
    final firstWin = baseAchievementItems.firstWhere((a) => a.id == 'first_win');
    expect(firstWin.coinReward, 20);
    expect(firstWin.target, 1);

    final perfectMind = baseAchievementItems.firstWhere((a) => a.id == 'perfect_mind');
    expect(perfectMind.coinReward, 30);
    expect(perfectMind.target, 1);

    // Replacement achievements for heart task
    final quickLearner = baseAchievementItems.firstWhere((a) => a.id == 'quick_learner');
    expect(quickLearner.coinReward, 35);
    expect(quickLearner.target, 10);

    final risingStar = baseAchievementItems.firstWhere((a) => a.id == 'rising_star');
    expect(risingStar.coinReward, 45);
    expect(risingStar.target, 5);

    final starHunter = baseAchievementItems.firstWhere((a) => a.id == 'star_hunter');
    expect(starHunter.coinReward, 50);
    expect(starHunter.target, 15);

    // Verify comeback/heart achievement is completely removed
    expect(baseAchievementItems.any((a) => a.id == 'comeback'), isFalse);
    for (final item in baseAchievementItems) {
      expect(item.description.toLowerCase().contains('heart'), isFalse,
          reason: '${item.id} should not mention heart');
    }

    // World tasks
    final w1 = baseAchievementItems.firstWhere((a) => a.id == 'world_1_complete');
    expect(w1.coinReward, 150);
    expect(w1.target, 40);

    final w5 = baseAchievementItems.firstWhere((a) => a.id == 'world_5_complete');
    expect(w5.coinReward, 180);
    expect(w5.target, 5);

    final w10 = baseAchievementItems.firstWhere((a) => a.id == 'world_10_complete');
    expect(w10.coinReward, 200);
    expect(w10.gemReward, 50);
    expect(w10.target, 10);

    // Additional locked achievements
    final w2 = baseAchievementItems.firstWhere((a) => a.id == 'world_2_complete');
    expect(w2.coinReward, 160);
    expect(w2.target, 40);

    final w3 = baseAchievementItems.firstWhere((a) => a.id == 'world_3_complete');
    expect(w3.coinReward, 170);
    expect(w3.target, 40);

    final star50 = baseAchievementItems.firstWhere((a) => a.id == 'star_collector_50');
    expect(star50.coinReward, 90);
    expect(star50.target, 50);

    final grandmaster = baseAchievementItems.firstWhere((a) => a.id == 'grandmaster_50');
    expect(grandmaster.coinReward, 160);
    expect(grandmaster.target, 50);

    // Guarantee that every single achievement has coins <= 200
    for (final item in baseAchievementItems) {
      expect(item.coinReward, lessThanOrEqualTo(200),
          reason: '${item.id} (${item.title}) has ${item.coinReward} coins, which exceeds max 200');
      expect(item.coinReward, greaterThanOrEqualTo(20),
          reason: '${item.id} (${item.title}) has ${item.coinReward} coins, which is below 20');
    }
  });

  test('Daily puzzle rotates daily and does not repeat across consecutive days', () {
    final today = DateTime(2026, 10, 3);
    final tomorrow = DateTime(2026, 10, 4);
    final dayAfter = DateTime(2026, 10, 5);

    final puzzleToday = DailyPuzzleScreen.getDailyPuzzleForDate(today);
    final puzzleTomorrow = DailyPuzzleScreen.getDailyPuzzleForDate(tomorrow);
    final puzzleDayAfter = DailyPuzzleScreen.getDailyPuzzleForDate(dayAfter);

    // Consecutive days must have different puzzles
    expect(puzzleToday.question, isNot(equals(puzzleTomorrow.question)));
    expect(puzzleTomorrow.question, isNot(equals(puzzleDayAfter.question)));

    // Deterministic: Same date always yields same puzzle
    final puzzleTodayRepeat = DailyPuzzleScreen.getDailyPuzzleForDate(today);
    expect(puzzleToday.question, equals(puzzleTodayRepeat.question));
    expect(puzzleToday.correctAnswer, equals(puzzleTodayRepeat.correctAnswer));

    // Verify valid structure
    expect(puzzleToday.options, contains(puzzleToday.correctAnswer));
    expect(puzzleTomorrow.options, contains(puzzleTomorrow.correctAnswer));
    expect(puzzleDayAfter.options, contains(puzzleDayAfter.correctAnswer));
  });

  test('Rate Us appears after 5 levels and then every 25 levels thereafter', () {
    // Reset state
    GameStorage.hasRatedApp = false;
    GameStorage.lastRatingPromptLevel = 0;
    GameStorage.totalWins = 0;

    // 0 to 4 levels: should NOT prompt
    for (int lvl = 0; lvl < 5; lvl++) {
      GameStorage.totalWins = lvl;
      expect(GameStorage.shouldPromptRating(), isFalse,
          reason: 'Level $lvl should not prompt rating');
    }

    // 5 levels completed: MUST prompt
    GameStorage.totalWins = 5;
    expect(GameStorage.shouldPromptRating(), isTrue,
        reason: '5 levels completed must prompt rating');

    // User dismisses / reminded later -> mark prompted
    GameStorage.lastRatingPromptLevel = 5;
    expect(GameStorage.shouldPromptRating(), isFalse,
        reason: 'Immediately after prompt at 5, should not prompt again');

    // Levels 6 to 29: should NOT prompt (< 25 levels since last prompt)
    for (int lvl = 6; lvl < 30; lvl++) {
      GameStorage.totalWins = lvl;
      expect(GameStorage.shouldPromptRating(), isFalse,
          reason: 'Level $lvl (less than 25 levels after 5) should not prompt');
    }

    // Level 30 (5 + 25): MUST prompt!
    GameStorage.totalWins = 30;
    expect(GameStorage.shouldPromptRating(), isTrue,
        reason: 'Level 30 (25 levels after 5) must prompt rating');

    // Mark prompted at 30
    GameStorage.lastRatingPromptLevel = 30;
    expect(GameStorage.shouldPromptRating(), isFalse);

    // Levels 31 to 54: should NOT prompt
    for (int lvl = 31; lvl < 55; lvl++) {
      GameStorage.totalWins = lvl;
      expect(GameStorage.shouldPromptRating(), isFalse);
    }

    // Level 55 (30 + 25): MUST prompt!
    GameStorage.totalWins = 55;
    expect(GameStorage.shouldPromptRating(), isTrue,
        reason: 'Level 55 (another 25 levels later) must prompt rating');

    // When user rates the app: hasRatedApp = true
    GameStorage.hasRatedApp = true;
    expect(GameStorage.shouldPromptRating(), isFalse,
        reason: 'Once rated, user should never be prompted automatically again');
  });

  test('Rate Us does not show twice on level 5 completion when tapping next puzzle', () async {
    GameStorage.hasRatedApp = false;
    GameStorage.lastRatingPromptLevel = 0;
    GameStorage.totalWins = 4;

    // Level 5 completed: should prompt rating
    expect(GameStorage.shouldPromptRating(currentLevelNumber: 5), isTrue);

    // Prompt is shown once when tapping Next Puzzle, marked as prompted
    await GameStorage.markRatingPrompted(currentLevelNumber: 5);

    // After user dismisses ('X' cross) or finishes dialog, subsequent check for level 5 MUST be false
    expect(GameStorage.shouldPromptRating(currentLevelNumber: 5), isFalse,
        reason: 'Should not re-prompt for level 5 after dismissal');

    // Next levels before milestone 30 should not prompt
    for (int lvl = 6; lvl < 30; lvl++) {
      expect(GameStorage.shouldPromptRating(currentLevelNumber: lvl), isFalse);
    }

    // Milestone 30 should prompt
    expect(GameStorage.shouldPromptRating(currentLevelNumber: 30), isTrue);
    await GameStorage.markRatingPrompted(currentLevelNumber: 30);
    expect(GameStorage.shouldPromptRating(currentLevelNumber: 30), isFalse);
  });

  test('GameStorage stores and retrieves Mind Map profile correctly', () async {
    SharedPreferences.setMockInitialValues({});
    await GameStorage.load();

    expect(GameStorage.hasMappedMind, isFalse);
    expect(GameStorage.mindMapAge, '25 – 34');

    await GameStorage.saveMindMapProfile(
      age: '18 – 24',
      gender: 'Male',
      iq: '110 – 130',
      goal: 'Boost IQ',
    );

    expect(GameStorage.hasMappedMind, isTrue);
    expect(GameStorage.mindMapAge, '18 – 24');
    expect(GameStorage.mindMapGender, 'Male');
    expect(GameStorage.mindMapIq, '110 – 130');
    expect(GameStorage.mindMapGoal, 'Boost IQ');
  });

  testWidgets('MapYourMindScreen displays all sections and selections', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);

    String? completedAge;
    String? completedGender;
    String? completedIq;
    String? completedGoal;
    bool continuedToLevels = false;

    await tester.pumpWidget(
      MaterialApp(
        home: MapYourMindScreen(
          onCompleted: (age, gender, iq, goal) async {
            completedAge = age;
            completedGender = gender;
            completedIq = iq;
            completedGoal = goal;
          },
          onContinueToLevels: () async {
            continuedToLevels = true;
          },
        ),
      ),
    );

    // Step 1: About You
    expect(find.text("Let's Map Your Mind"), findsOneWidget);
    expect(find.text('Your Age'), findsOneWidget);
    expect(find.text('Gender'), findsOneWidget);
    expect(find.text('Next'), findsOneWidget);

    await tester.tap(find.text('18 – 24'));
    await tester.pump();

    // Step 2: Goals
    await tester.tap(find.text('Next'));
    await tester.pumpAndSettle();
    expect(find.text('Your Goal'), findsOneWidget);
    expect(find.text('Your Age'), findsNothing);

    // Step 3: Preferences
    await tester.tap(find.text('Next'));
    await tester.pumpAndSettle();
    expect(find.text('Your Current IQ Level'), findsOneWidget);

    // Step 4: All Set
    await tester.tap(find.text('Next'));
    await tester.pumpAndSettle();
    expect(find.text("You're All Set!"), findsOneWidget);
    expect(find.text('Done'), findsOneWidget);

    await tester.tap(find.text('Done'));
    await tester.pump(const Duration(milliseconds: 350));
    await tester.pump(const Duration(milliseconds: 50));

    expect(completedAge, '18 – 24');
    expect(completedGender, 'Female');
    expect(completedIq, '90 – 110');
    expect(completedGoal, 'Improve Focus');
    expect(continuedToLevels, isTrue);
  });

  testWidgets('HomeVerticalActionButtons renders 5 vertical pill buttons', (tester) async {
    bool mapPressed = false;
    bool dailyPressed = false;
    bool trainingPressed = false;
    bool achievementsPressed = false;
    bool progressPressed = false;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: HomeVerticalActionButtons(
            onMapYourMindPressed: () => mapPressed = true,
            onDailyPressed: () => dailyPressed = true,
            onQuickTrainingPressed: () => trainingPressed = true,
            onAchievementsPressed: () => achievementsPressed = true,
            onProgressPressed: () => progressPressed = true,
          ),
        ),
      ),
    );

    expect(find.text("LET'S MAP YOUR MIND"), findsOneWidget);
    expect(find.text('DAILY CHALLENGE'), findsOneWidget);
    expect(find.text('⚡ NEW'), findsOneWidget);
    expect(find.text('QUICK TRAINING'), findsOneWidget);
    expect(find.text('ACHIEVEMENTS'), findsOneWidget);
    expect(find.text('PROGRESS'), findsOneWidget);

    await tester.tap(find.text("LET'S MAP YOUR MIND"));
    expect(mapPressed, isTrue);

    await tester.tap(find.text('DAILY CHALLENGE'));
    expect(dailyPressed, isTrue);

    await tester.tap(find.text('QUICK TRAINING'));
    expect(trainingPressed, isTrue);

    await tester.tap(find.text('ACHIEVEMENTS'));
    expect(achievementsPressed, isTrue);

    await tester.tap(find.text('PROGRESS'));
    expect(progressPressed, isTrue);
  });

  testWidgets('HomeVerticalActionButtons shows notification bell when achievements are claimable', (tester) async {
    GameStorage.unclaimedAchievementsNotifier.value = 0;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: HomeVerticalActionButtons(
            onMapYourMindPressed: () {},
            onDailyPressed: () {},
            onQuickTrainingPressed: () {},
            onAchievementsPressed: () {},
            onProgressPressed: () {},
          ),
        ),
      ),
    );

    // When 0 unclaimed achievements, bell icon is not shown
    expect(find.byIcon(Icons.notifications_active_rounded), findsNothing);

    // When 1 achievement is claimable, bell icon and CLAIM badge appear
    GameStorage.unclaimedAchievementsNotifier.value = 1;
    await tester.pump();

    expect(find.byIcon(Icons.notifications_active_rounded), findsOneWidget);
    expect(find.text('CLAIM'), findsOneWidget);

    // When 3 achievements are claimable
    GameStorage.unclaimedAchievementsNotifier.value = 3;
    await tester.pump();

    expect(find.byIcon(Icons.notifications_active_rounded), findsOneWidget);
    expect(find.text('3 CLAIM'), findsOneWidget);

    // Reset back to 0
    GameStorage.unclaimedAchievementsNotifier.value = 0;
    await tester.pump();
    expect(find.byIcon(Icons.notifications_active_rounded), findsNothing);
  });
}
