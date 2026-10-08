import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../models/world_model.dart';
import '../widgets/professional_lock_dialog.dart';
import 'language_selection_screen.dart';
import 'world_levels_screen.dart';

int getWorldStars(int worldIndex, Map<String, int> stageLevelStars) {
  int total = 0;
  for (int levelIndex = 0; levelIndex < WorldThemes.levelsPerWorld; levelIndex++) {
    final key = '${worldIndex + 1}-${levelIndex + 1}';
    total += stageLevelStars[key] ?? 0;
  }
  return total;
}

int getWorldCompletedLevels(int worldIndex, Map<String, int> stageLevelStars) {
  int completed = 0;
  for (int levelIndex = 0; levelIndex < WorldThemes.levelsPerWorld; levelIndex++) {
    final key = '${worldIndex + 1}-${levelIndex + 1}';
    if ((stageLevelStars[key] ?? 0) > 0) {
      completed++;
    }
  }
  return completed;
}

bool isWorldUnlocked(int worldIndex, int totalStarsAcrossGame, Map<String, int> stageLevelStars) {
  if (worldIndex == 0) return true;
  // A world unlocks ONLY when ALL 40 levels of the previous world are completed!
  return getWorldCompletedLevels(worldIndex - 1, stageLevelStars) >= WorldThemes.levelsPerWorld;
}

class WorldsScreen extends StatefulWidget {
  final Map<String, int> Function()? getStarsMap;
  final Future<void> Function(int worldIndex, int levelIndex)? onLevelSelected;

  const WorldsScreen({super.key, this.getStarsMap, this.onLevelSelected});

  @override
  State<WorldsScreen> createState() => _WorldsScreenState();
}

class _WorldsScreenState extends State<WorldsScreen> {
  Map<String, int> _starsMap = {};

  @override
  void initState() {
    super.initState();
    _refreshStars();
  }

  void _refreshStars() {
    if (widget.getStarsMap != null) {
      setState(() {
        _starsMap = widget.getStarsMap!();
      });
    }
  }

  int get _totalGameStars {
    return _starsMap.values.fold(0, (sum, stars) => sum + stars);
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        final worlds = WorldThemes.allWorlds;
        final totalStars = _totalGameStars;

        return Scaffold(
          backgroundColor: const Color(0xFF0A0E17),
          body: Stack(
            children: [
              // Professional Alpine Mountain Lake Background (Stage-7) - 100% Crystal Clear
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/Stage-7.webp'),
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
                child: Column(
                  children: [
                    // Top App Bar
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16, 10, 16, 8),
                      child: Row(
                        children: [
                          _buildCircleButton(
                            icon: Icons.arrow_back_rounded,
                            onPressed: () => Navigator.of(context).maybePop(),
                          ),
                          const SizedBox(width: 14),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  tr('worlds'),
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 22,
                                    fontWeight: FontWeight.w900,
                                    letterSpacing: 1.4,
                                    shadows: [
                                      Shadow(
                                        color: Color(0xFF0284C7),
                                        blurRadius: 16,
                                      ),
                                    ],
                                  ),
                                ),
                                Text(
                                  tr('select_world'),
                                  style: const TextStyle(
                                    color: Color(0xFF7DD3FC),
                                    fontSize: 12,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          // Language Button
                          _buildCircleButton(
                            icon: Icons.translate_rounded,
                            onPressed: () async {
                              await Navigator.push(
                                context,
                                MaterialPageRoute(
                                  builder: (_) => const LanguageSelectionScreen(
                                    isFromSettings: true,
                                  ),
                                ),
                              );
                              if (mounted) setState(() {});
                            },
                          ),
                          const SizedBox(width: 8),
                          // 3D Star Counter Pill
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
                            decoration: BoxDecoration(
                              gradient: const LinearGradient(
                                colors: [Color(0xFF0369A1), Color(0xFF0EA5E9)],
                              ),
                              borderRadius: BorderRadius.circular(24),
                              border: Border.all(
                                color: const Color(0xFF38BDF8).withAlpha(140),
                                width: 1.5,
                              ),
                              boxShadow: [
                                BoxShadow(
                                  color: const Color(0xFF0284C7).withAlpha(100),
                                  blurRadius: 14,
                                  offset: const Offset(0, 3),
                                ),
                              ],
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Image.asset(
                                  'assets/images/Golden_Star_Icon.png',
                                  width: 22,
                                  height: 22,
                                ),
                                const SizedBox(width: 6),
                                Text(
                                  '$totalStars / ${WorldThemes.totalLevelsCount * 3}',
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontWeight: FontWeight.w900,
                                    fontSize: 14,
                                    letterSpacing: 0.5,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),


                    const SizedBox(height: 4),

                    // Worlds List
                    Expanded(
                      child: ListView.builder(
                        padding: const EdgeInsets.fromLTRB(16, 6, 16, 24),
                        physics: const BouncingScrollPhysics(),
                        itemCount: worlds.length,
                        itemBuilder: (context, index) {
                          final world = worlds[index];
                          final unlocked = isWorldUnlocked(index, totalStars, _starsMap);
                          final worldStars = getWorldStars(index, _starsMap);
                          final completed = getWorldCompletedLevels(index, _starsMap);
                          final prevCompleted = index > 0 ? getWorldCompletedLevels(index - 1, _starsMap) : 40;

                          return _WorldCard(
                            world: world,
                            isUnlocked: unlocked,
                            worldStars: worldStars,
                            completedLevels: completed,
                            prevWorldCompleted: prevCompleted,
                            onTap: unlocked
                                ? () async {
                                    await Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                        builder: (_) => WorldLevelsScreen(
                                          world: world,
                                          getStarsMap: widget.getStarsMap,
                                          onLevelSelected: widget.onLevelSelected,
                                        ),
                                      ),
                                    );
                                    _refreshStars();
                                  }
                                : () {
                                    showProfessionalLockDialog(
                                      context,
                                      title: tr('world_locked'),
                                      subtitle: world.localizedTitle,
                                      message: tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),
                                      currentProgress: prevCompleted,
                                      targetProgress: WorldThemes.levelsPerWorld,
                                    );
                                  },
                          );
                        },
                      ),
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

  Widget _buildCircleButton({required IconData icon, required VoidCallback onPressed}) {
    final isRtl = Directionality.of(context) == TextDirection.rtl;
    final displayIcon = (icon == Icons.arrow_back_rounded && isRtl)
        ? Icons.arrow_forward_rounded
        : icon;
    return Material(
      color: Colors.white.withAlpha(25),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: SizedBox(
          width: 38,
          height: 38,
          child: Icon(displayIcon, color: Colors.white, size: 24),
        ),
      ),
    );
  }
}

class _WorldCard extends StatelessWidget {
  final WorldData world;
  final bool isUnlocked;
  final int worldStars;
  final int completedLevels;
  final int prevWorldCompleted;
  final VoidCallback onTap;

  const _WorldCard({
    required this.world,
    required this.isUnlocked,
    required this.worldStars,
    required this.completedLevels,
    this.prevWorldCompleted = 0,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      height: 185,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(24),
        border: Border.all(
          color: isUnlocked
              ? world.glowColor.withAlpha(160)
              : Colors.white.withAlpha(35),
          width: isUnlocked ? 2.0 : 1.0,
        ),
        boxShadow: [
          if (isUnlocked)
            BoxShadow(
              color: world.glowColor.withAlpha(70),
              blurRadius: 18,
              offset: const Offset(0, 5),
            )
          else
            BoxShadow(
              color: Colors.black.withAlpha(90),
              blurRadius: 10,
              offset: const Offset(0, 4),
            ),
        ],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(23),
        child: Stack(
          children: [
            // 1. Crystal-clear scenic background image (VIBRANT & VISIBLE)
            Positioned.fill(
              child: Image(
                image: AssetImage(world.backgroundAsset),
                fit: BoxFit.cover,
                alignment: Alignment.center,
                errorBuilder: (context, error, stackTrace) => Container(color: world.cardGradientEnd),
              ),
            ),

            // 2. High-contrast gradient vignette: Left side readable for text, Right side wide open for scenery!
            Positioned.fill(
              child: DecoratedBox(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.centerLeft,
                    end: Alignment.centerRight,
                    colors: [
                      Colors.black.withAlpha(isUnlocked ? 175 : 185),
                      Colors.black.withAlpha(isUnlocked ? 90 : 120),
                      Colors.black.withAlpha(isUnlocked ? 0 : 25),
                    ],
                    stops: const [0.0, 0.50, 1.0],
                  ),
                ),
              ),
            ),

            // 3. Subtle bottom shadow for card depth
            Positioned.fill(
              child: DecoratedBox(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.black.withAlpha(25),
                      Colors.transparent,
                      Colors.black.withAlpha(110),
                    ],
                    stops: const [0.0, 0.4, 1.0],
                  ),
                ),
              ),
            ),

            // 4. Subtle overlay for locked state
            if (!isUnlocked)
              Positioned.fill(
                child: Container(
                  color: Colors.black.withAlpha(35),
                ),
              ),

            // 5. Card Content
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Top Row: World Number Badge & Stars / Lock Cost
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      // World Number Pill
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: isUnlocked
                                ? [world.primaryColor, world.secondaryColor]
                                : [Colors.white24, Colors.white10],
                          ),
                          borderRadius: BorderRadius.circular(12),
                          boxShadow: isUnlocked
                              ? [
                                  BoxShadow(
                                    color: world.primaryColor.withAlpha(120),
                                    blurRadius: 8,
                                  ),
                                ]
                              : [],
                        ),
                        child: Text(
                          '${tr('world').toUpperCase()} ${world.worldNumber}',
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 1.0,
                          ),
                        ),
                      ),

                      // Stars Earned or Required Stars Pill
                      if (isUnlocked)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                          decoration: BoxDecoration(
                            color: Colors.black.withAlpha(160),
                            borderRadius: BorderRadius.circular(14),
                            border: Border.all(color: const Color(0xFFFFD700).withAlpha(120)),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Image.asset(
                                'assets/images/Golden_Star_Icon.png',
                                width: 16,
                                height: 16,
                              ),
                              const SizedBox(width: 4),
                              Text(
                                '$worldStars/${world.maxStars}',
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontWeight: FontWeight.w900,
                                  fontSize: 12,
                                ),
                              ),
                            ],
                          ),
                        )
                      else
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: Colors.black.withAlpha(180),
                            borderRadius: BorderRadius.circular(14),
                            border: Border.all(color: const Color(0xFFFFB703).withAlpha(160)),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              const Icon(Icons.lock_rounded, color: Color(0xFFFFB703), size: 14),
                              const SizedBox(width: 4),
                              Text(
                                '${tr("world")} ${world.worldNumber - 1} ($prevWorldCompleted/40)',
                                style: const TextStyle(
                                  color: Color(0xFFFFB703),
                                  fontWeight: FontWeight.w900,
                                  fontSize: 11,
                                ),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),

                  // Middle Row: Title, Subtitle & Icon
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      // Floating 3D-styled theme badge (Only single lock when locked!)
                      Container(
                        width: 58,
                        height: 58,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          gradient: isUnlocked
                              ? LinearGradient(
                                  colors: [world.primaryColor, world.secondaryColor],
                                  begin: Alignment.topLeft,
                                  end: Alignment.bottomRight,
                                )
                              : const LinearGradient(
                                  colors: [Color(0xFF374151), Color(0xFF1F2937)],
                                ),
                          border: Border.all(
                            color: isUnlocked ? world.glowColor : Colors.white24,
                            width: 2.0,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: isUnlocked
                                  ? world.glowColor.withAlpha(140)
                                  : Colors.black.withAlpha(120),
                              blurRadius: 14,
                              offset: const Offset(0, 3),
                            ),
                          ],
                        ),
                        child: Center(
                          child: Icon(
                            world.icon,
                            color: isUnlocked ? Colors.white : Colors.white70,
                            size: 28,
                          ),
                        ),
                      ),
                      const SizedBox(width: 14),

                      // Title & Subtitle
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              world.localizedTitle,
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: TextStyle(
                                color: isUnlocked ? Colors.white : Colors.white70,
                                fontSize: 19,
                                fontWeight: FontWeight.w900,
                                letterSpacing: 0.5,
                                shadows: const [
                                  Shadow(color: Colors.black, blurRadius: 10, offset: Offset(0, 2)),
                                ],
                              ),
                            ),
                            const SizedBox(height: 2),
                            Text(
                              world.localizedSubtitle,
                              maxLines: 1,
                              style: TextStyle(
                                color: isUnlocked ? world.glowColor : Colors.white38,
                                fontSize: 13,
                                fontWeight: FontWeight.w700,
                                shadows: const [
                                  Shadow(color: Colors.black, blurRadius: 8),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),

                      // Enter / Action Chevron
                      if (isUnlocked)
                        Container(
                          width: 38,
                          height: 38,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: Colors.white.withAlpha(35),
                            border: Border.all(color: Colors.white.withAlpha(60)),
                          ),
                          child: const Center(
                            child: Icon(
                              Icons.arrow_forward_ios_rounded,
                              color: Colors.white,
                              size: 16,
                            ),
                          ),
                        ),
                    ],
                  ),

                  // Bottom Row: Progress bar & Level stats OR Lock prompt
                  if (isUnlocked)
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              '${formatNumber(completedLevels)} / ${formatNumber(world.levelsCount)} ${tr('levels_cleared')}',
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                shadows: [Shadow(color: Colors.black, blurRadius: 6)],
                              ),
                            ),
                            Text(
                              '${((completedLevels / world.levelsCount) * 100).toInt()}%',
                              style: TextStyle(
                                color: world.glowColor,
                                fontSize: 11,
                                fontWeight: FontWeight.w900,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 4),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(6),
                          child: SizedBox(
                            height: 6,
                            child: LinearProgressIndicator(
                              value: (completedLevels / world.levelsCount).clamp(0.0, 1.0),
                              backgroundColor: Colors.white.withAlpha(40),
                              valueColor: AlwaysStoppedAnimation<Color>(world.primaryColor),
                            ),
                          ),
                        ),
                      ],
                    )
                  else
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
                      decoration: BoxDecoration(
                        color: Colors.black.withAlpha(140),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: Colors.white.withAlpha(20)),
                      ),
                      child: Text(
                        tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),
                        style: const TextStyle(
                          color: Color(0xFFFDE68A),
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ),
                ],
              ),
            ),

            // Tap Ripple
            Positioned.fill(
              child: Material(
                color: Colors.transparent,
                child: InkWell(
                  onTap: onTap,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
