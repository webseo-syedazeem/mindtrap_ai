import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../screens/auth_screen.dart';
import '../screens/store_screen.dart';
import '../services/auth_service.dart';

class AppLanguageDrawer extends StatefulWidget {
  final Future<void> Function(String code)? onLanguageChanged;
  final VoidCallback? onWorldsPressed;

  const AppLanguageDrawer({
    super.key,
    this.onLanguageChanged,
    this.onWorldsPressed,
  });

  @override
  State<AppLanguageDrawer> createState() => _AppLanguageDrawerState();
}

class _AppLanguageDrawerState extends State<AppLanguageDrawer> {
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';

  @override
  void initState() {
    super.initState();
    _searchController.addListener(() {
      setState(() {
        _searchQuery = _searchController.text.trim().toLowerCase();
      });
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

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, currentCode, _) {
        final filteredLanguages = allLanguages.where((lang) {
          if (_searchQuery.isEmpty) return true;
          return lang.englishName.toLowerCase().contains(_searchQuery) ||
              lang.nativeName.toLowerCase().contains(_searchQuery) ||
              lang.code.toLowerCase().contains(_searchQuery);
        }).toList();

        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: Drawer(
            backgroundColor: const Color(0xFF0B1120),
            width: MediaQuery.of(context).size.width * 0.85,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // ── User Profile Header ──────────────────────────────────
                _buildUserProfileSection(context),

                // ── Quick Navigation Pills ───────────────────────────────
                Padding(
                  padding: const EdgeInsets.fromLTRB(14, 12, 14, 6),
                  child: Row(
                    children: [
                      // Worlds Button
                      if (widget.onWorldsPressed != null)
                        Expanded(
                          child: _buildNavPill(
                            icon: Icons.public_rounded,
                            label: tr('worlds'),
                            colors: [const Color(0xFF0369A1), const Color(0xFF0EA5E9)],
                            onTap: () {
                              Navigator.of(context).pop();
                              widget.onWorldsPressed!();
                            },
                          ),
                        ),
                      if (widget.onWorldsPressed != null) const SizedBox(width: 10),
                      // Store Button
                      Expanded(
                        child: _buildNavPill(
                          icon: Icons.diamond_rounded,
                          label: tr('store'),
                          colors: [const Color(0xFF0284C7), const Color(0xFF38BDF8)],
                          onTap: () {
                            Navigator.of(context).pop();
                            Navigator.push(
                              context,
                              MaterialPageRoute(builder: (_) => const StoreScreen()),
                            );
                          },
                        ),
                      ),
                    ],
                  ),
                ),

                // ── Divider ──────────────────────────────────────────────
                Container(
                  margin: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                  height: 1,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [
                        Colors.transparent,
                        const Color(0xFF38BDF8).withAlpha(80),
                        Colors.transparent,
                      ],
                    ),
                  ),
                ),

                // ── Language Section Header ───────────────────────────────
                Padding(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 6),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: const Color(0xFF0284C7).withAlpha(35),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: const Icon(
                          Icons.language_rounded,
                          color: Color(0xFF38BDF8),
                          size: 16,
                        ),
                      ),
                      const SizedBox(width: 10),
                      Text(
                        tr('select_language'),
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 14,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 0.3,
                        ),
                      ),
                      const Spacer(),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 3),
                        decoration: BoxDecoration(
                          gradient: const LinearGradient(
                            colors: [Color(0xFF0369A1), Color(0xFF0284C7)],
                          ),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Text(
                          '${allLanguages.length}',
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),

                // ── Search Bar ────────────────────────────────────────────
                Padding(
                  padding: const EdgeInsets.fromLTRB(14, 2, 14, 6),
                  child: Container(
                    height: 42,
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E293B),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(
                        color: const Color(0xFF0284C7).withAlpha(60),
                      ),
                    ),
                    child: TextField(
                      controller: _searchController,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 13,
                      ),
                      decoration: InputDecoration(
                        hintText: tr('search_language'),
                        hintStyle: const TextStyle(color: Colors.white38, fontSize: 13),
                        prefixIcon: const Icon(
                          Icons.search_rounded,
                          color: Color(0xFF38BDF8),
                          size: 18,
                        ),
                        suffixIcon: _searchQuery.isNotEmpty
                            ? IconButton(
                                icon: const Icon(
                                  Icons.close_rounded,
                                  color: Colors.white38,
                                  size: 16,
                                ),
                                onPressed: () => _searchController.clear(),
                              )
                            : null,
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.symmetric(vertical: 11),
                      ),
                    ),
                  ),
                ),

                // ── Language List ─────────────────────────────────────────
                Expanded(
                  child: filteredLanguages.isEmpty
                      ? Center(
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              const Icon(
                                Icons.search_off_rounded,
                                color: Color(0xFF38BDF8),
                                size: 40,
                              ),
                              const SizedBox(height: 8),
                              Text(
                                tr('no_languages_found'),
                                style: const TextStyle(
                                  color: Colors.white38,
                                  fontSize: 14,
                                ),
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
                                // 1. Set language & fire ValueNotifier
                                await LanguageController.instance.setLanguage(lang.code);
                                // 2. Persist to storage
                                if (widget.onLanguageChanged != null) {
                                  await widget.onLanguageChanged!(lang.code);
                                }
                                // 3. Close drawer
                                navigator.pop();
                              },
                              child: AnimatedContainer(
                                duration: const Duration(milliseconds: 200),
                                margin: const EdgeInsets.only(bottom: 6),
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 12,
                                  vertical: 9,
                                ),
                                decoration: BoxDecoration(
                                  color: isSelected
                                      ? const Color(0xFF0369A1).withAlpha(180)
                                      : const Color(0xFF1E293B).withAlpha(100),
                                  borderRadius: BorderRadius.circular(14),
                                  border: Border.all(
                                    color: isSelected
                                        ? const Color(0xFF38BDF8)
                                        : Colors.white.withAlpha(15),
                                    width: isSelected ? 1.8 : 1.0,
                                  ),
                                  boxShadow: isSelected
                                      ? [
                                          BoxShadow(
                                            color: const Color(0xFF0284C7).withAlpha(60),
                                            blurRadius: 10,
                                            offset: const Offset(0, 3),
                                          ),
                                        ]
                                      : null,
                                ),
                                child: Row(
                                  children: [
                                    // Flag
                                    Text(
                                      lang.flagEmoji,
                                      style: const TextStyle(fontSize: 22),
                                    ),
                                    const SizedBox(width: 12),
                                    // Names
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Text(
                                            lang.englishName,
                                            style: TextStyle(
                                              color: Colors.white,
                                              fontWeight: isSelected
                                                  ? FontWeight.w900
                                                  : FontWeight.w600,
                                              fontSize: 14,
                                            ),
                                          ),
                                          Text(
                                            lang.nativeName,
                                            style: TextStyle(
                                              color: isSelected
                                                  ? const Color(0xFF7DD3FC)
                                                  : Colors.white54,
                                              fontSize: 12,
                                              fontWeight: FontWeight.w500,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                    // Check mark
                                    if (isSelected)
                                      Container(
                                        width: 24,
                                        height: 24,
                                        decoration: const BoxDecoration(
                                          shape: BoxShape.circle,
                                          color: Color(0xFF10B981),
                                        ),
                                        child: const Icon(
                                          Icons.check_rounded,
                                          color: Colors.white,
                                          size: 14,
                                        ),
                                      )
                                    else
                                      Container(
                                        width: 24,
                                        height: 24,
                                        decoration: BoxDecoration(
                                          shape: BoxShape.circle,
                                          border: Border.all(
                                            color: Colors.white24,
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
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildNavPill({
    required IconData icon,
    required String label,
    required List<Color> colors,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
        decoration: BoxDecoration(
          gradient: LinearGradient(colors: colors),
          borderRadius: BorderRadius.circular(14),
          boxShadow: [
            BoxShadow(
              color: colors[0].withAlpha(80),
              blurRadius: 10,
              offset: const Offset(0, 3),
            ),
          ],
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: Colors.white, size: 18),
            const SizedBox(width: 8),
            Flexible(
              child: Text(
                label,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w900,
                  fontSize: 13,
                  letterSpacing: 0.6,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildUserProfileSection(BuildContext context) {
    return ValueListenableBuilder<bool>(
      valueListenable: AuthService.instance.isLoggedIn,
      builder: (context, loggedIn, _) {
        return Container(
          padding: EdgeInsets.fromLTRB(
            16,
            MediaQuery.of(context).padding.top + 16,
            16,
            16,
          ),
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Color(0xFF0C4A6E), Color(0xFF0F172A)],
            ),
            border: Border(
              bottom: BorderSide(color: Color(0x3338BDF8), width: 1),
            ),
          ),
          child: Row(
            children: [
              // Avatar Circle
              Container(
                width: 52,
                height: 52,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: LinearGradient(
                    colors: loggedIn
                        ? [const Color(0xFF059669), const Color(0xFF0EA5E9)]
                        : [const Color(0xFF0284C7), const Color(0xFF38BDF8)],
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: (loggedIn
                              ? const Color(0xFF059669)
                              : const Color(0xFF0284C7))
                          .withAlpha(80),
                      blurRadius: 14,
                    ),
                  ],
                ),
                child: Icon(
                  loggedIn
                      ? Icons.verified_user_rounded
                      : Icons.person_rounded,
                  color: Colors.white,
                  size: 26,
                ),
              ),
              const SizedBox(width: 14),

              // User Info
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      loggedIn
                          ? AuthService.instance.userName.value
                          : tr('guest_player'),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      loggedIn
                          ? AuthService.instance.userEmail.value
                          : tr('continue_as_guest'),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        color: loggedIn
                            ? const Color(0xFF7DD3FC)
                            : Colors.white54,
                        fontSize: 11,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),

              // Auth Action Button
              if (loggedIn)
                IconButton(
                  tooltip: tr('logout'),
                  icon: const Icon(
                    Icons.logout_rounded,
                    color: Colors.white60,
                    size: 20,
                  ),
                  onPressed: () async {
                    await AuthService.instance.signOut();
                    if (context.mounted) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: const Text('Signed out successfully'),
                          backgroundColor: const Color(0xFF0F172A),
                          behavior: SnackBarBehavior.floating,
                          margin: const EdgeInsets.all(16),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(14),
                          ),
                        ),
                      );
                    }
                  },
                )
              else
                ElevatedButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const AuthScreen()),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF0284C7),
                    padding: const EdgeInsets.symmetric(
                      horizontal: 14,
                      vertical: 8,
                    ),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    elevation: 4,
                    shadowColor: const Color(0xFF0284C7).withAlpha(80),
                  ),
                  child: Text(
                    tr('sign_in'),
                    style: const TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w900,
                      fontSize: 12,
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
