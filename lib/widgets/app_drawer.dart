import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../main.dart';
import '../screens/auth_screen.dart';
import '../screens/store_screen.dart';
import '../screens/worlds_screen.dart';
import '../services/auth_service.dart';

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
    final drawerWidth = min(MediaQuery.of(context).size.width * 0.88, 380.0);

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
            child: Container(
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [
                    Color(0xFF0F172A),
                    Color(0xFF0B1120),
                    Color(0xFF070B14),
                  ],
                ),
                borderRadius: const BorderRadius.horizontal(right: Radius.circular(28)),
                border: Border(
                  right: BorderSide(
                    color: const Color(0xFF38BDF8).withAlpha(60),
                    width: 1.5,
                  ),
                ),
                boxShadow: const [
                  BoxShadow(
                    color: Colors.black87,
                    blurRadius: 30,
                    spreadRadius: 6,
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
            color: const Color(0xFF1E293B).withAlpha(140),
            borderRadius: BorderRadius.circular(22),
            border: Border.all(
              color: loggedIn
                  ? const Color(0xFF10B981).withAlpha(90)
                  : const Color(0xFF38BDF8).withAlpha(70),
              width: 1.2,
            ),
            boxShadow: [
              BoxShadow(
                color: (loggedIn ? const Color(0xFF10B981) : const Color(0xFF0284C7)).withAlpha(40),
                blurRadius: 16,
                offset: const Offset(0, 4),
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
                        width: 50,
                        height: 50,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          gradient: LinearGradient(
                            colors: loggedIn
                                ? [const Color(0xFF10B981), const Color(0xFF059669)]
                                : [const Color(0xFF0284C7), const Color(0xFF6366F1)],
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: (loggedIn ? const Color(0xFF10B981) : const Color(0xFF0284C7)).withAlpha(90),
                              blurRadius: 10,
                            ),
                          ],
                        ),
                        child: Center(
                          child: Icon(
                            loggedIn ? Icons.verified_user_rounded : Icons.person_rounded,
                            color: Colors.white,
                            size: 26,
                          ),
                        ),
                      ),
                      Positioned(
                        bottom: -2,
                        right: -2,
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1.5),
                          decoration: BoxDecoration(
                            color: loggedIn ? const Color(0xFF10B981) : const Color(0xFF38BDF8),
                            borderRadius: BorderRadius.circular(6),
                            border: Border.all(color: const Color(0xFF0F172A), width: 1.5),
                          ),
                          child: Text(
                            loggedIn ? 'PRO' : 'GUEST',
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
                            color: Colors.white,
                            fontSize: 15,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.2,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          loggedIn
                              ? AuthService.instance.userEmail.value
                              : 'Tap to sync cloud progress',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            color: loggedIn ? const Color(0xFF7DD3FC) : Colors.white54,
                            fontSize: 11,
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
                      icon: const Icon(Icons.logout_rounded, color: Colors.white70, size: 20),
                      onPressed: () async {
                        await AuthService.instance.signOut();
                        if (context.mounted) {
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              content: const Text('Signed out successfully'),
                              backgroundColor: const Color(0xFF0F172A),
                              behavior: SnackBarBehavior.floating,
                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                            ),
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
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        elevation: 4,
                      ),
                      child: Text(
                        tr('sign_in'),
                        style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w900),
                      ),
                    ),
                ],
              ),

              const SizedBox(height: 12),

              // Player Mini Stats Ribbon
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                decoration: BoxDecoration(
                  color: Colors.black.withAlpha(120),
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: Colors.white.withAlpha(15)),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildStatPill(
                      icon: Image.asset('assets/images/Golden_Star_Icon.png', width: 15, height: 15),
                      value: '$totalStars',
                      color: const Color(0xFFFFD700),
                    ),
                    _buildDivider(),
                    _buildStatPill(
                      icon: Image.asset('assets/images/coin.webp', width: 14, height: 14),
                      value: '${GameStorage.coinBalance}',
                      color: const Color(0xFFFFB703),
                    ),
                    _buildDivider(),
                    _buildStatPill(
                      icon: Image.asset('assets/images/gem.webp', width: 14, height: 14),
                      value: '${GameStorage.gemBalance}',
                      color: const Color(0xFF38BDF8),
                    ),
                    _buildDivider(),
                    _buildStatPill(
                      icon: const Icon(Icons.track_changes_rounded, size: 14, color: Color(0xFF34D399)),
                      value: '$completedLevels/1K',
                      color: const Color(0xFF34D399),
                    ),
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildDivider() {
    return Container(width: 1, height: 16, color: Colors.white12);
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
            fontSize: 11.5,
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
        color: const Color(0xFF1E293B).withAlpha(120),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.white.withAlpha(20)),
      ),
      child: Row(
        children: [
          Expanded(
            child: _buildTabButton(
              title: 'GAME MENU',
              icon: Icons.explore_rounded,
              isSelected: _selectedTab == 0,
              onTap: () => setState(() => _selectedTab = 0),
            ),
          ),
          const SizedBox(width: 6),
          Expanded(
            child: _buildTabButton(
              title: 'LANGUAGES ($langCount)',
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
                  colors: [Color(0xFF0284C7), Color(0xFF0369A1)],
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
              color: isSelected ? Colors.white : Colors.white60,
            ),
            const SizedBox(width: 6),
            Text(
              title,
              style: TextStyle(
                color: isSelected ? Colors.white : Colors.white60,
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
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [Color(0xFF1E293B), Color(0xFF0F172A)],
              ),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: const Color(0xFF38BDF8).withAlpha(50)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Row(
                      children: [
                        Icon(Icons.military_tech_rounded, color: Color(0xFFFFD700), size: 16),
                        SizedBox(width: 6),
                        Text(
                          '1,000 LEVELS ODYSSEY',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.6,
                          ),
                        ),
                      ],
                    ),
                    Text(
                      '$completedLevels / 1000',
                      style: const TextStyle(
                        color: Color(0xFF38BDF8),
                        fontSize: 11,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                ClipRRect(
                  borderRadius: BorderRadius.circular(8),
                  child: LinearProgressIndicator(
                    value: progress,
                    minHeight: 7,
                    backgroundColor: Colors.white12,
                    valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF38BDF8)),
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 12),

          // 1. Worlds Odyssey (1,000 Levels)
          _buildNavTile(
            title: tr('worlds'),
            subtitle: '25 Worlds • 1,000 Levels Map',
            badgeText: '25 WORLDS',
            icon: Icons.public_rounded,
            iconColors: const [Color(0xFF0284C7), Color(0xFF0EA5E9)],
            onTap: () {
              Navigator.of(context).pop();
              if (widget.onWorldsPressed != null) {
                widget.onWorldsPressed!();
              } else {
                Navigator.push(
                  context,
                  smoothPageRoute(
                    WorldsScreen(getStarsMap: () => GameStorage.stageLevelStars),
                  ),
                );
              }
            },
          ),

          const SizedBox(height: 8),

          // 2. Diamond & Coin Store
          _buildNavTile(
            title: tr('store'),
            subtitle: 'Gems, Coins & Hint Boosters',
            badgeText: 'HOT DEALS',
            badgeColor: const Color(0xFFEAB308),
            icon: Icons.diamond_rounded,
            iconColors: const [Color(0xFF7C3AED), Color(0xFFA855F7)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const StoreScreen()));
            },
          ),

          const SizedBox(height: 8),

          // 3. Daily Mystery Reward
          _buildNavTile(
            title: 'Daily Rewards',
            subtitle: 'Claim free coins & gems every 24h',
            badgeText: 'FREE',
            badgeColor: const Color(0xFF10B981),
            icon: Icons.card_giftcard_rounded,
            iconColors: const [Color(0xFFEA580C), Color(0xFFF59E0B)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const DailyRewardScreen()));
            },
          ),

          const SizedBox(height: 8),

          // 4. Active Language Selector Shortcut
          _buildNavTile(
            title: 'Language: ${currentLanguage.englishName}',
            subtitle: '${currentLanguage.flagEmoji} ${currentLanguage.nativeName} (Tap to change)',
            badgeText: '56 >',
            badgeColor: const Color(0xFF0D9488),
            icon: Icons.translate_rounded,
            iconColors: const [Color(0xFF0D9488), Color(0xFF14B8A6)],
            onTap: () {
              setState(() => _selectedTab = 1);
            },
          ),

          const SizedBox(height: 8),

          // 5. Game Settings
          _buildNavTile(
            title: tr('settings'),
            subtitle: 'Audio, vibration & game data',
            badgeText: 'CONFIG',
            icon: Icons.settings_rounded,
            iconColors: const [Color(0xFF475569), Color(0xFF64748B)],
            onTap: () {
              Navigator.of(context).pop();
              Navigator.push(context, smoothPageRoute(const SettingsScreen()));
            },
          ),

          const SizedBox(height: 14),

          // Quick Audio Controls Strip
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
            decoration: BoxDecoration(
              color: const Color(0xFF1E293B).withAlpha(120),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: Colors.white.withAlpha(18)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'QUICK AUDIO & HAPTICS',
                  style: TextStyle(
                    color: Colors.white70,
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
                        label: 'Sound',
                        icon: _soundEnabled ? Icons.volume_up_rounded : Icons.volume_off_rounded,
                        isEnabled: _soundEnabled,
                        onTap: () => _toggleAudio(GameStorage.soundKey, _soundEnabled),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: _buildAudioQuickToggle(
                        label: 'Music',
                        icon: _musicEnabled ? Icons.music_note_rounded : Icons.music_off_rounded,
                        isEnabled: _musicEnabled,
                        onTap: () => _toggleAudio(GameStorage.musicKey, _musicEnabled),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: _buildAudioQuickToggle(
                        label: 'Vibrate',
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
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          color: const Color(0xFF1E293B).withAlpha(120),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.white.withAlpha(20)),
        ),
        child: Row(
          children: [
            Container(
              width: 42,
              height: 42,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(12),
                gradient: LinearGradient(
                  colors: iconColors,
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                boxShadow: [
                  BoxShadow(
                    color: iconColors.first.withAlpha(80),
                    blurRadius: 8,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Icon(icon, color: Colors.white, size: 21),
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
                      color: Colors.white,
                      fontSize: 13.5,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      color: Colors.white54,
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 8),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
              decoration: BoxDecoration(
                color: badgeColor.withAlpha(35),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: badgeColor.withAlpha(120)),
              ),
              child: Text(
                badgeText,
                style: TextStyle(
                  color: badgeColor,
                  fontSize: 9.5,
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
      borderRadius: BorderRadius.circular(12),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 8),
        decoration: BoxDecoration(
          color: isEnabled
              ? const Color(0xFF0284C7).withAlpha(45)
              : Colors.black.withAlpha(60),
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: isEnabled
                ? const Color(0xFF38BDF8).withAlpha(120)
                : Colors.white12,
          ),
        ),
        child: Column(
          children: [
            Icon(
              icon,
              size: 18,
              color: isEnabled ? const Color(0xFF38BDF8) : Colors.white38,
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(
                color: isEnabled ? Colors.white : Colors.white38,
                fontSize: 10,
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
            height: 42,
            decoration: BoxDecoration(
              color: const Color(0xFF1E293B),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: const Color(0xFF0284C7).withAlpha(80)),
            ),
            child: TextField(
              controller: _searchController,
              style: const TextStyle(color: Colors.white, fontSize: 13),
              decoration: InputDecoration(
                hintText: tr('search_language'),
                hintStyle: const TextStyle(color: Colors.white38, fontSize: 12.5),
                prefixIcon: const Icon(Icons.search_rounded, color: Color(0xFF38BDF8), size: 18),
                suffixIcon: _searchQuery.isNotEmpty
                    ? IconButton(
                        icon: const Icon(Icons.close_rounded, color: Colors.white38, size: 16),
                        onPressed: () => _searchController.clear(),
                      )
                    : null,
                border: InputBorder.none,
                contentPadding: const EdgeInsets.symmetric(vertical: 11),
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
                      const Icon(Icons.search_off_rounded, color: Color(0xFF38BDF8), size: 38),
                      const SizedBox(height: 8),
                      Text(
                        tr('no_languages_found'),
                        style: const TextStyle(color: Colors.white38, fontSize: 13),
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
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                        decoration: BoxDecoration(
                          color: isSelected
                              ? const Color(0xFF0369A1).withAlpha(190)
                              : const Color(0xFF1E293B).withAlpha(100),
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(
                            color: isSelected
                                ? const Color(0xFF38BDF8)
                                : Colors.white.withAlpha(15),
                            width: isSelected ? 1.6 : 1.0,
                          ),
                          boxShadow: isSelected
                              ? [
                                  BoxShadow(
                                    color: const Color(0xFF0284C7).withAlpha(60),
                                    blurRadius: 8,
                                    offset: const Offset(0, 2),
                                  ),
                                ]
                              : null,
                        ),
                        child: Row(
                          children: [
                            Container(
                              width: 36,
                              height: 36,
                              decoration: BoxDecoration(
                                color: Colors.white.withAlpha(15),
                                borderRadius: BorderRadius.circular(10),
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
                                      color: Colors.white,
                                      fontWeight: isSelected ? FontWeight.w900 : FontWeight.w700,
                                      fontSize: 13.5,
                                    ),
                                  ),
                                  Text(
                                    lang.nativeName,
                                    style: TextStyle(
                                      color: isSelected ? const Color(0xFF7DD3FC) : Colors.white54,
                                      fontSize: 11.5,
                                      fontWeight: FontWeight.w500,
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
                                  color: Color(0xFF10B981),
                                ),
                                child: const Icon(Icons.check_rounded, color: Colors.white, size: 14),
                              )
                            else
                              Container(
                                width: 22,
                                height: 22,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  border: Border.all(color: Colors.white24, width: 1.5),
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
      decoration: const BoxDecoration(
        border: Border(top: BorderSide(color: Colors.white12, width: 1)),
      ),
      child: const Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Icon(Icons.psychology_rounded, color: Color(0xFF38BDF8), size: 16),
              SizedBox(width: 6),
              Text(
                'MindTrap AI',
                style: TextStyle(
                  color: Colors.white70,
                  fontSize: 11,
                  fontWeight: FontWeight.w800,
                ),
              ),
            ],
          ),
          Text(
            'v1.2.0 • 1,000 Levels',
            style: TextStyle(
              color: Colors.white38,
              fontSize: 10,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }
}
