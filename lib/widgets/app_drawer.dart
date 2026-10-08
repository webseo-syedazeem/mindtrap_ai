<<<<<<< HEAD
import '../screens/map_your_mind_screen.dart';
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
import 'dart:math';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../main.dart';
import '../screens/auth_screen.dart';
import '../screens/store_screen.dart';
import '../screens/worlds_screen.dart';
import '../services/auth_service.dart';
<<<<<<< HEAD
import 'rate_us_dialog.dart';
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f

class AppLanguageDrawer extends StatefulWidget {
  final Future<void> Function(String code)? onLanguageChanged;
  final VoidCallback? onWorldsPressed;
  final VoidCallback? onStorePressed;
  final VoidCallback? onDailyRewardPressed;
  final VoidCallback? onSettingsPressed;

  const AppLanguageDrawer({
    super.key,
    this.onLanguageChanged,
    this.onWorldsPressed,
    this.onStorePressed,
    this.onDailyRewardPressed,
    this.onSettingsPressed,
  });

  @override
  State<AppLanguageDrawer> createState() => _AppLanguageDrawerState();
}

class _AppLanguageDrawerState extends State<AppLanguageDrawer> {
  int _selectedTab = 0; // 0: Game Menu, 1: Languages
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';

  bool _soundEnabled = GameStorage.soundEnabled;
  bool _musicEnabled = GameStorage.musicEnabled;
  bool _vibrationEnabled = GameStorage.vibrationEnabled;

  @override
  void initState() {
    super.initState();
    _loadAudioSettings();
    _searchController.addListener(() {
      setState(() {
        _searchQuery = _searchController.text.trim().toLowerCase();
      });
    });
  }

  Future<void> _loadAudioSettings() async {
    final prefs = await GameStorage.prefs;
    if (!mounted) return;
    setState(() {
      _soundEnabled = GameStorage.savedBool(prefs, GameStorage.soundKey);
      _musicEnabled = GameStorage.savedBool(prefs, GameStorage.musicKey);
      _vibrationEnabled = GameStorage.savedBool(prefs, GameStorage.vibrationKey);
    });
  }

  Future<void> _toggleAudio(String key, bool currentVal) async {
    HapticFeedback.lightImpact();
    final newVal = !currentVal;
    await GameStorage.saveSettings(
      sound: key == GameStorage.soundKey ? newVal : null,
      music: key == GameStorage.musicKey ? newVal : null,
      vibration: key == GameStorage.vibrationKey ? newVal : null,
    );
    if (!mounted) return;
    setState(() {
      if (key == GameStorage.soundKey) _soundEnabled = newVal;
      if (key == GameStorage.musicKey) _musicEnabled = newVal;
      if (key == GameStorage.vibrationKey) _vibrationEnabled = newVal;
    });
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final allLanguages = AppStrings.supportedLanguages;
    final drawerWidth = min(MediaQuery.of(context).size.width * 0.84, 345.0);

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, currentCode, _) {
        final currentLanguage = allLanguages.firstWhere(
          (l) => l.code == currentCode,
          orElse: () => allLanguages.first,
        );

        final filteredLanguages = allLanguages.where((lang) {
          if (_searchQuery.isEmpty) return true;
          return lang.englishName.toLowerCase().contains(_searchQuery) ||
              lang.nativeName.toLowerCase().contains(_searchQuery) ||
              lang.code.toLowerCase().contains(_searchQuery);
        }).toList();

        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: Drawer(
            backgroundColor: Colors.transparent,
            elevation: 0,
            width: drawerWidth,
            child: ClipRRect(
              borderRadius: const BorderRadius.horizontal(right: Radius.circular(30)),
              child: BackdropFilter(
                filter: ImageFilter.blur(sigmaX: 18, sigmaY: 18),
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.white.withAlpha(115),
                    borderRadius: const BorderRadius.horizontal(right: Radius.circular(30)),
                    border: Border.all(
                      color: const Color(0xFFBAE6FD),
                      width: 1.8,
                    ),
                    boxShadow: const [
                      BoxShadow(
                        color: Color(0x180284C7),
                        blurRadius: 28,
                        spreadRadius: 2,
                        offset: Offset(4, 0),
                      ),
                      BoxShadow(
                        color: Color(0x100F172A),
                        blurRadius: 16,
                        offset: Offset(2, 0),
                      ),
                    ],
                  ),
                  child: SafeArea(
                    child: Column(
                      children: [
                        // 1. Header Profile & Stats Card
                        _buildProfileSection(context),

                        // 2. Segmented Mode Switcher (Menu vs Languages)
                        _buildSegmentedTabSwitcher(allLanguages.length),

                        // 3. Tab Content
                        Expanded(
                          child: AnimatedSwitcher(
                            duration: const Duration(milliseconds: 250),
                            child: _selectedTab == 0
                                ? _buildGameMenuTab(context, currentLanguage)
                                : _buildLanguagesTab(
                                    context,
                                    filteredLanguages,
                                    currentCode,
                                  ),
                          ),
                        ),

                        // 4. Footer info
                        _buildDrawerFooter(),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),
        );
      },
    );
  }

  Widget _buildProfileSection(BuildContext context) {
    return ValueListenableBuilder<bool>(
      valueListenable: AuthService.instance.isLoggedIn,
      builder: (context, loggedIn, _) {
        final totalStars = GameStorage.stageLevelStars.values.fold(0, (sum, s) => sum + s);
        final completedLevels = GameStorage.stageLevelStars.values.where((s) => s > 0).length;

        return Container(
          margin: const EdgeInsets.fromLTRB(14, 8, 14, 10),
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(22),
            border: Border.all(
              color: loggedIn
                  ? const Color(0xFF86EFAC)
                  : const Color(0xFFBAE6FD),
              width: 1.5,
            ),
            boxShadow: const [
              BoxShadow(
                color: Color(0x150284C7),
                blurRadius: 18,
                offset: Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            children: [
              // Avatar & User Details Row
              Row(
                children: [
                  // Avatar with status ring
                  Stack(
                    clipBehavior: Clip.none,
                    children: [
                      Container(
                        width: 52,
                        height: 52,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          gradient: LinearGradient(
                            colors: loggedIn
                                ? [const Color(0xFF10B981), const Color(0xFF059669)]
                                : [const Color(0xFF38BDF8), const Color(0xFF0284C7)],
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: (loggedIn ? const Color(0xFF10B981) : const Color(0xFF0284C7)).withAlpha(90),
                              blurRadius: 12,
                              offset: const Offset(0, 3),
                            ),
                          ],
                        ),
                        child: Center(
                          child: Icon(
                            loggedIn ? Icons.verified_user_rounded : Icons.person_rounded,
                            color: Colors.white,
                            size: 28,
                          ),
                        ),
                      ),
                      Positioned(
                        bottom: -2,
                        right: -2,
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1.5),
                          decoration: BoxDecoration(
                            color: loggedIn ? const Color(0xFF10B981) : const Color(0xFF0284C7),
                            borderRadius: BorderRadius.circular(6),
                            border: Border.all(color: Colors.white, width: 1.5),
                          ),
                          child: Text(
<<<<<<< HEAD
                            loggedIn ? tr('pro') : tr('guest'),
=======
                            loggedIn ? 'PRO' : 'GUEST',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 8,
                              fontWeight: FontWeight.w900,
                              letterSpacing: 0.5,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(width: 12),

                  // Player Name & Status
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          loggedIn
                              ? (AuthService.instance.userName.value.isNotEmpty
                                  ? AuthService.instance.userName.value
                                  : 'MindTrap Player')
                              : tr('guest_player'),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                            color: Color(0xFF0F172A),
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.2,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          loggedIn
                              ? AuthService.instance.userEmail.value
<<<<<<< HEAD
                              : tr('tap_to_sync'),
=======
                              : 'Tap to sync cloud progress',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                            color: Color(0xFF64748B),
                            fontSize: 11.5,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),

                  // Action Button
                  if (loggedIn)
                    IconButton(
                      tooltip: tr('logout'),
                      icon: const Icon(Icons.logout_rounded, color: Color(0xFFEF4444), size: 22),
                      onPressed: () async {
                        await AuthService.instance.signOut();
                        if (context.mounted) {
                          showGameNotification(
                            context: context,
<<<<<<< HEAD
                            message: tr('signed_out_success'),
=======
                            message: 'Signed out successfully',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                            icon: Icons.logout_rounded,
                            accentColor: const Color(0xFFEF4444),
                            iconColor: const Color(0xFFF87171),
                          );
                        }
                      },
                    )
                  else
                    ElevatedButton(
                      onPressed: () {
                        Navigator.of(context).pop();
                        Navigator.push(context, smoothPageRoute(const AuthScreen()));
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF0284C7),
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                        elevation: 3,
                        shadowColor: const Color(0xFF0284C7).withAlpha(90),
                      ),
                      child: Text(
                        tr('sign_in'),
                        style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w900),
                      ),
                    ),
                ],
              ),

              const SizedBox(height: 12),

              // Player Mini Stats Ribbon
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                decoration: BoxDecoration(
                  color: const Color(0xFFF8FAFC),
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: const Color(0xFFBAE6FD).withAlpha(160), width: 1.2),
                ),
                child: ValueListenableBuilder<int>(
                  valueListenable: GameStorage.currencyNotifier,
                  builder: (context, _, child) {
                    return Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _buildStatPill(
                          icon: Image.asset('assets/images/Golden_Star_Icon.png', width: 16, height: 16),
                          value: '$totalStars',
                          color: const Color(0xFF0F172A),
                        ),
                        _buildDivider(),
                        _buildStatPill(
                          icon: Image.asset('assets/images/coin.webp', width: 15, height: 15),
                          value: '${GameStorage.coinBalance}',
                          color: const Color(0xFF0F172A),
                        ),
                        _buildDivider(),
                        _buildStatPill(
                          icon: Image.asset('assets/images/gem.webp', width: 15, height: 15),
                          value: '${GameStorage.gemBalance}',
                          color: const Color(0xFF0284C7),
                        ),
                        _buildDivider(),
                        _buildStatPill(
                          icon: const Icon(Icons.track_changes_rounded, size: 15, color: Color(0xFF059669)),
                          value: '$completedLevels/1K',
                          color: const Color(0xFF059669),
                        ),
                      ],
                    );
                  },
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildDivider() {
    return Container(width: 1, height: 16, color: const Color(0xFFCBD5E1));
  }

  Widget _buildStatPill({required Widget icon, required String value, required Color color}) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        icon,
        const SizedBox(width: 5),
        Text(
          value,
          style: TextStyle(
            color: color,
            fontSize: 12,
            fontWeight: FontWeight.w900,
          ),
        ),
      ],
    );
  }

  Widget _buildSegmentedTabSwitcher(int langCount) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        color: const Color(0xFFF0F9FF),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFBAE6FD), width: 1.3),
      ),
      child: Row(
        children: [
          Expanded(
            child: _buildTabButton(
<<<<<<< HEAD
              title: tr('game_menu'),
=======
              title: 'GAME MENU',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
              icon: Icons.explore_rounded,
              isSelected: _selectedTab == 0,
              onTap: () => setState(() => _selectedTab = 0),
            ),
          ),
          const SizedBox(width: 6),
          Expanded(
            child: _buildTabButton(
<<<<<<< HEAD
              title: '${tr('languages')} ($langCount)',
=======
              title: 'LANGUAGES ($langCount)',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
              icon: Icons.language_rounded,
              isSelected: _selectedTab == 1,
              onTap: () => setState(() => _selectedTab = 1),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTabButton({
    required String title,
    required IconData icon,
    required bool isSelected,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(vertical: 9),
        decoration: BoxDecoration(
          gradient: isSelected
              ? const LinearGradient(
                  colors: [Color(0xFF38BDF8), Color(0xFF0284C7)],
                )
              : null,
          color: isSelected ? null : Colors.transparent,
          borderRadius: BorderRadius.circular(12),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: const Color(0xFF0284C7).withAlpha(80),
                    blurRadius: 8,
                    offset: const Offset(0, 2),
                  ),
                ]
              : null,
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              icon,
              size: 15,
              color: isSelected ? Colors.white : const Color(0xFF475569),
            ),
            const SizedBox(width: 6),
            Text(
              title,
              style: TextStyle(
                color: isSelected ? Colors.white : const Color(0xFF475569),
                fontSize: 11,
                fontWeight: isSelected ? FontWeight.w900 : FontWeight.w700,
                letterSpacing: 0.5,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildGameMenuTab(BuildContext context, AppLanguage currentLanguage) {
    final completedLevels = GameStorage.stageLevelStars.values.where((s) => s > 0).length;
    final progress = (completedLevels / 1000.0).clamp(0.0, 1.0);

    return SingleChildScrollView(
      key: const ValueKey('menu_tab'),
      padding: const EdgeInsets.fromLTRB(14, 6, 14, 12),
      physics: const BouncingScrollPhysics(),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Global 1,000 Levels Progress Bar
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: const Color(0xFFBAE6FD), width: 1.5),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x100284C7),
                  blurRadius: 14,
                  offset: Offset(0, 3),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
<<<<<<< HEAD
                    Row(
                      children: [
                        const Icon(Icons.military_tech_rounded, color: Color(0xFFF59E0B), size: 18),
                        const SizedBox(width: 6),
                        Text(
                          tr('levels_odyssey'),
=======
                    const Row(
                      children: [
                        Icon(Icons.military_tech_rounded, color: Color(0xFFF59E0B), size: 18),
                        SizedBox(width: 6),
                        Text(
                          '1,000 LEVELS ODYSSEY',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                          style: TextStyle(
                            color: Color(0xFF0F172A),
                            fontSize: 12,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.6,
                          ),
                        ),
                      ],
                    ),
                    Text(
                      '$completedLevels / 1000',
                      style: const TextStyle(
                        color: Color(0xFF0284C7),
                        fontSize: 12,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),
                ClipRRect(
                  borderRadius: BorderRadius.circular(8),
                  child: LinearProgressIndicator(
                    value: progress,
                    minHeight: 7,
                    backgroundColor: const Color(0xFFE2E8F0),
                    valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF0284C7)),
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 10),

          // 1. Worlds Odyssey (1,000 Levels)
          _buildNavTile(
            title: tr('worlds'),
<<<<<<< HEAD
            subtitle: tr('worlds_map_sub'),
            badgeText: tr('worlds_badge'),
=======
            subtitle: '25 Worlds • 1,000 Levels Map',
            badgeText: '25 WORLDS',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
            icon: Icons.public_rounded,
            iconColors: const [Color(0xFF38BDF8), Color(0xFF0284C7)],
            onTap: () {
              Navigator.of(context).pop();
              if (widget.onWorldsPressed != null) {
                widget.onWorldsPressed!();
              } else {
                Navigator.push(
                  context,
                  smoothPageRoute(
<<<<<<< HEAD
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
                      },
                    ),
=======
                    WorldsScreen(getStarsMap: () => GameStorage.stageLevelStars),
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                  ),
                );
              }
            },
          ),

          const SizedBox(height: 8),

          // 2. Diamond & Coin Store
          _buildNavTile(
            title: tr('store'),
<<<<<<< HEAD
            subtitle: tr('store_sub'),
            badgeText: tr('hot_deals'),
=======
            subtitle: 'Gems, Coins & Hint Boosters',
            badgeText: 'HOT DEALS',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
            badgeColor: const Color(0xFFD97706),
            icon: Icons.diamond_rounded,
            iconColors: const [Color(0xFFA855F7), Color(0xFF7C3AED)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const StoreScreen()));
            },
          ),

          const SizedBox(height: 8),

          // 3. Daily Mystery Reward
          _buildNavTile(
<<<<<<< HEAD
            title: tr('daily_rewards'),
            subtitle: tr('daily_rewards_sub'),
            badgeText: tr('free'),
=======
            title: 'Daily Rewards',
            subtitle: 'Claim free coins & gems every 24h',
            badgeText: 'FREE',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
            badgeColor: const Color(0xFF059669),
            icon: Icons.card_giftcard_rounded,
            iconColors: const [Color(0xFFF59E0B), Color(0xFFEA580C)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const DailyRewardScreen()));
            },
          ),

          const SizedBox(height: 8),

<<<<<<< HEAD
          // 3.5. Edit Mind Profile
          _buildNavTile(
            title: tr('edit_mind_profile'),
            subtitle: tr('edit_mind_profile_sub'),
            badgeText: tr('mind_badge'),
            badgeColor: const Color(0xFF8B5CF6),
            icon: Icons.psychology_rounded,
            iconColors: const [Color(0xFF8B5CF6), Color(0xFF6D28D9)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(
                context,
                smoothPageRoute(
                  MapYourMindScreen(
                    initialAge: GameStorage.mindMapAge,
                    initialGender: GameStorage.mindMapGender,
                    initialIq: GameStorage.mindMapIq,
                    initialGoal: GameStorage.mindMapGoal,
                    onCompleted: (age, gender, iq, goal) async {
                      await GameStorage.saveMindMapProfile(
                        age: age,
                        gender: gender,
                        iq: iq,
                        goal: goal,
                      );
                    },
                  ),
                ),
              );
            },
          ),

          const SizedBox(height: 8),

          // 4. Active Language Selector Shortcut
          _buildNavTile(
            title: '${tr('language_label')}: ${currentLanguage.nativeName}',
            subtitle: '${currentLanguage.flagEmoji} ${currentLanguage.nativeName} (${tr('tap_to_change')})',
=======
          // 4. Active Language Selector Shortcut
          _buildNavTile(
            title: 'Language: ${currentLanguage.englishName}',
            subtitle: '${currentLanguage.flagEmoji} ${currentLanguage.nativeName} (Tap to change)',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
            badgeText: '56 >',
            badgeColor: const Color(0xFF0284C7),
            icon: Icons.translate_rounded,
            iconColors: const [Color(0xFF14B8A6), Color(0xFF0D9488)],
            onTap: () {
              setState(() => _selectedTab = 1);
            },
          ),

          const SizedBox(height: 8),

          // 5. Game Settings
          _buildNavTile(
            title: tr('settings'),
<<<<<<< HEAD
            subtitle: tr('settings_sub'),
            badgeText: tr('config_badge'),
=======
            subtitle: 'Audio, vibration & game data',
            badgeText: 'CONFIG',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
            icon: Icons.settings_rounded,
            iconColors: const [Color(0xFF64748B), Color(0xFF475569)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const SettingsScreen()));
            },
          ),

<<<<<<< HEAD
          const SizedBox(height: 8),

          // 6. Rate Us
          _buildNavTile(
            title: tr('rate_us'),
            subtitle: tr('rate_us_subtitle'),
            badgeText: tr('stars_5_badge'),
            badgeColor: const Color(0xFFF59E0B),
            icon: Icons.star_rounded,
            iconColors: const [Color(0xFFF59E0B), Color(0xFFD97706)],
            onTap: () {
              Navigator.of(context).pop();
              showRateUsDialog(context);
            },
          ),

=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
          const SizedBox(height: 14),

          // Quick Audio Controls Strip
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: const Color(0xFFBAE6FD), width: 1.4),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x100284C7),
                  blurRadius: 14,
                  offset: Offset(0, 3),
                ),
                BoxShadow(
                  color: Color(0x080F172A),
                  blurRadius: 8,
                  offset: Offset(0, 1),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
<<<<<<< HEAD
                Text(
                  tr('quick_audio_haptics'),
=======
                const Text(
                  'QUICK AUDIO & HAPTICS',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                  style: TextStyle(
                    color: Color(0xFF64748B),
                    fontSize: 10,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0.8,
                  ),
                ),
                const SizedBox(height: 10),
                Row(
                  children: [
                    Expanded(
                      child: _buildAudioQuickToggle(
<<<<<<< HEAD
                        label: tr('sound'),
=======
                        label: 'Sound',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                        icon: _soundEnabled ? Icons.volume_up_rounded : Icons.volume_off_rounded,
                        isEnabled: _soundEnabled,
                        onTap: () => _toggleAudio(GameStorage.soundKey, _soundEnabled),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: _buildAudioQuickToggle(
<<<<<<< HEAD
                        label: tr('music'),
=======
                        label: 'Music',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                        icon: _musicEnabled ? Icons.music_note_rounded : Icons.music_off_rounded,
                        isEnabled: _musicEnabled,
                        onTap: () => _toggleAudio(GameStorage.musicKey, _musicEnabled),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: _buildAudioQuickToggle(
<<<<<<< HEAD
                        label: tr('vibration'),
=======
                        label: 'Vibrate',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                        icon: _vibrationEnabled ? Icons.vibration_rounded : Icons.smartphone_rounded,
                        isEnabled: _vibrationEnabled,
                        onTap: () => _toggleAudio(GameStorage.vibrationKey, _vibrationEnabled),
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

  Widget _buildNavTile({
    required String title,
    required String subtitle,
    required String badgeText,
    Color badgeColor = const Color(0xFF0284C7),
    required IconData icon,
    required List<Color> iconColors,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: () {
        HapticFeedback.lightImpact();
        onTap();
      },
      borderRadius: BorderRadius.circular(18),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 11),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(18),
          border: Border.all(color: const Color(0xFFBAE6FD), width: 1.4),
          boxShadow: const [
            BoxShadow(
              color: Color(0x100284C7),
              blurRadius: 12,
              offset: Offset(0, 3),
            ),
            BoxShadow(
              color: Color(0x060F172A),
              blurRadius: 6,
              offset: Offset(0, 1),
            ),
          ],
        ),
        child: Row(
          children: [
            Container(
              width: 44,
              height: 44,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(14),
                gradient: LinearGradient(
                  colors: iconColors,
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                boxShadow: [
                  BoxShadow(
                    color: iconColors.first.withAlpha(70),
                    blurRadius: 8,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Icon(icon, color: Colors.white, size: 22),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      color: Color(0xFF0F172A),
                      fontSize: 14,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      color: Color(0xFF64748B),
                      fontSize: 11.5,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 8),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4.5),
              decoration: BoxDecoration(
                color: badgeColor.withAlpha(22),
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: badgeColor.withAlpha(140), width: 1.2),
              ),
              child: Text(
                badgeText,
                style: TextStyle(
                  color: badgeColor,
                  fontSize: 10,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0.5,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildAudioQuickToggle({
    required String label,
    required IconData icon,
    required bool isEnabled,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(14),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 9),
        decoration: BoxDecoration(
          color: isEnabled
              ? const Color(0xFFE0F2FE)
              : const Color(0xFFF8FAFC),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isEnabled
                ? const Color(0xFF0284C7)
                : const Color(0xFFBAE6FD).withAlpha(140),
            width: 1.2,
          ),
        ),
        child: Column(
          children: [
            Icon(
              icon,
              size: 20,
              color: isEnabled ? const Color(0xFF0284C7) : const Color(0xFF94A3B8),
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(
                color: isEnabled ? const Color(0xFF0F172A) : const Color(0xFF94A3B8),
                fontSize: 10.5,
                fontWeight: FontWeight.w800,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLanguagesTab(
    BuildContext context,
    List<AppLanguage> filteredLanguages,
    String currentCode,
  ) {
    return Column(
      key: const ValueKey('languages_tab'),
      children: [
        // Search Input
        Padding(
          padding: const EdgeInsets.fromLTRB(14, 6, 14, 8),
          child: Container(
            height: 44,
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: const Color(0xFFBAE6FD), width: 1.5),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x0C0284C7),
                  blurRadius: 10,
                  offset: Offset(0, 2),
                ),
              ],
            ),
            child: TextField(
              controller: _searchController,
              style: const TextStyle(color: Color(0xFF0F172A), fontSize: 13.5, fontWeight: FontWeight.w600),
              decoration: InputDecoration(
                hintText: tr('search_language'),
                hintStyle: const TextStyle(color: Color(0xFF94A3B8), fontSize: 13),
                prefixIcon: const Icon(Icons.search_rounded, color: Color(0xFF0284C7), size: 19),
                suffixIcon: _searchQuery.isNotEmpty
                    ? IconButton(
                        icon: const Icon(Icons.close_rounded, color: Color(0xFF64748B), size: 18),
                        onPressed: () => _searchController.clear(),
                      )
                    : null,
                border: InputBorder.none,
                contentPadding: const EdgeInsets.symmetric(vertical: 12),
              ),
            ),
          ),
        ),

        // Languages List
        Expanded(
          child: filteredLanguages.isEmpty
              ? Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      const Icon(Icons.search_off_rounded, color: Color(0xFF0284C7), size: 38),
                      const SizedBox(height: 8),
                      Text(
                        tr('no_languages_found'),
                        style: const TextStyle(color: Color(0xFF64748B), fontSize: 13, fontWeight: FontWeight.w600),
                      ),
                    ],
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.fromLTRB(14, 0, 14, 16),
                  physics: const BouncingScrollPhysics(),
                  itemCount: filteredLanguages.length,
                  itemBuilder: (context, index) {
                    final lang = filteredLanguages[index];
                    final isSelected = lang.code == currentCode;

                    return GestureDetector(
                      onTap: () async {
                        final navigator = Navigator.of(context);
                        HapticFeedback.selectionClick();
                        await LanguageController.instance.setLanguage(lang.code);
                        if (widget.onLanguageChanged != null) {
                          await widget.onLanguageChanged!(lang.code);
                        }
                        navigator.pop();
                      },
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 180),
                        margin: const EdgeInsets.only(bottom: 6),
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(
                            color: isSelected
                                ? const Color(0xFF0284C7)
                                : const Color(0xFFBAE6FD).withAlpha(160),
                            width: isSelected ? 1.8 : 1.2,
                          ),
                          boxShadow: isSelected
                              ? [
                                  BoxShadow(
                                    color: const Color(0xFF0284C7).withAlpha(50),
                                    blurRadius: 10,
                                    offset: const Offset(0, 3),
                                  ),
                                ]
                              : const [
                                  BoxShadow(
                                    color: Color(0x080F172A),
                                    blurRadius: 6,
                                    offset: Offset(0, 2),
                                  ),
                                ],
                        ),
                        child: Row(
                          children: [
                            Container(
                              width: 36,
                              height: 36,
                              decoration: BoxDecoration(
                                color: const Color(0xFFF8FAFC),
                                borderRadius: BorderRadius.circular(10),
                                border: Border.all(color: const Color(0xFFBAE6FD).withAlpha(140)),
                              ),
                              child: Center(
                                child: Text(lang.flagEmoji, style: const TextStyle(fontSize: 20)),
                              ),
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    lang.englishName,
                                    style: TextStyle(
                                      color: isSelected ? const Color(0xFF0284C7) : const Color(0xFF0F172A),
                                      fontWeight: isSelected ? FontWeight.w900 : FontWeight.w800,
                                      fontSize: 13.5,
                                    ),
                                  ),
                                  Text(
                                    lang.nativeName,
                                    style: const TextStyle(
                                      color: Color(0xFF64748B),
                                      fontSize: 11.5,
                                      fontWeight: FontWeight.w600,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            if (isSelected)
                              Container(
                                width: 22,
                                height: 22,
                                decoration: const BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: Color(0xFF0284C7),
                                ),
                                child: const Icon(Icons.check_rounded, color: Colors.white, size: 14),
                              )
                            else
                              Container(
                                width: 22,
                                height: 22,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  border: Border.all(color: const Color(0xFFCBD5E1), width: 1.5),
                                ),
                              ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
        ),
      ],
    );
  }

  Widget _buildDrawerFooter() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
      decoration: BoxDecoration(
        border: Border(top: BorderSide(color: const Color(0xFFBAE6FD).withAlpha(160), width: 1.2)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Image.asset(
                'assets/images/home_logo.webp',
                width: 20,
                height: 20,
                fit: BoxFit.contain,
                errorBuilder: (_, e, s) => const Icon(
                  Icons.psychology_rounded,
                  color: Color(0xFF0284C7),
                  size: 20,
                ),
              ),
              const SizedBox(width: 8),
<<<<<<< HEAD
              Text(
                tr('app_title'),
                style: const TextStyle(
=======
              const Text(
                'MindTrap AI',
                style: TextStyle(
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                  color: Color(0xFF0F172A),
                  fontSize: 12,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 0.3,
                ),
              ),
            ],
          ),
          Text(
<<<<<<< HEAD
            '${tr('version')} 1.2.0 • 1,000 ${tr('levels')}',
            style: const TextStyle(
=======
            'v1.2.0 • 1,000 Levels',
            style: TextStyle(
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
              color: Color(0xFF64748B),
              fontSize: 10,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }
}
