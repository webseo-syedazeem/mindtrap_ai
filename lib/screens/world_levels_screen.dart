import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../models/world_model.dart';
import '../screens/language_selection_screen.dart';
import '../widgets/level_background_builder.dart';
import '../widgets/professional_lock_dialog.dart';
import 'worlds_screen.dart';

class WorldLevelsScreen extends StatefulWidget {
  final WorldData world;
  final Map<String, int> Function()? getStarsMap;
  final Future<void> Function(int worldIndex, int levelIndex)? onLevelSelected;

  const WorldLevelsScreen({
    super.key,
    required this.world,
    this.getStarsMap,
    this.onLevelSelected,
  });

  @override
  State<WorldLevelsScreen> createState() => _WorldLevelsScreenState();
}

class _WorldLevelsScreenState extends State<WorldLevelsScreen> {
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

  int _starsForLevel(int levelIndex) {
    final key = '${widget.world.id + 1}-${levelIndex + 1}';
    return _starsMap[key] ?? 0;
  }

  bool _isLevelUnlocked(int levelIndex) {
    if (widget.world.id > 0 && !isWorldUnlocked(widget.world.id, 0, _starsMap)) {
      return false;
    }
    if (levelIndex == 0) return true;
    return _starsForLevel(levelIndex - 1) > 0;
  }

  @override
  Widget build(BuildContext context) {
    final world = widget.world;

    int totalWorldStars = 0;
    for (int i = 0; i < world.levelsCount; i++) {
      totalWorldStars += _starsForLevel(i);
    }

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          backgroundColor: const Color(0xFF0A0E17),
          body: Stack(
            children: [
              // 1. World's full vibrant scenery - 100% Crystal Clear
              Positioned.fill(
                child: Image(
                  image: AssetImage(world.backgroundAsset),
                  fit: BoxFit.cover,
                  alignment: Alignment.topCenter,
                  errorBuilder: (context, error, stackTrace) => Container(color: world.cardGradientEnd),
                ),
              ),

              // 2. Crystal-Clear Natural Vignette
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
                    // Header Bar
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16, 10, 16, 6),
                      child: Row(
                        children: [
                          _buildCircleButton(
                            icon: Icons.arrow_back_ios_new_rounded,
                            onPressed: () => Navigator.of(context).maybePop(),
                          ),
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
                            },
                          ),
                          const SizedBox(width: 14),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                      decoration: BoxDecoration(
                                        color: world.primaryColor.withAlpha(60),
                                        borderRadius: BorderRadius.circular(6),
                                        border: Border.all(color: world.glowColor),
                                      ),
                                      child: Text(
                                        '${tr('world').toUpperCase()} ${world.worldNumber}',
                                        style: TextStyle(
                                          color: world.glowColor,
                                          fontSize: 10,
                                          fontWeight: FontWeight.w900,
                                          letterSpacing: 1.0,
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 8),
                                    Expanded(
                                      child: Text(
                                        world.localizedTitle,
                                        maxLines: 1,
                                        overflow: TextOverflow.ellipsis,
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontSize: 19,
                                          fontWeight: FontWeight.w900,
                                          shadows: [
                                            Shadow(color: Colors.black, blurRadius: 10),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  world.localizedSubtitle,
                                  style: TextStyle(
                                    color: world.glowColor,
                                    fontSize: 12,
                                    fontWeight: FontWeight.w700,
                                    shadows: const [
                                      Shadow(color: Colors.black, blurRadius: 8),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                          // World stars badge with 3D star
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                            decoration: BoxDecoration(
                              color: Colors.black.withAlpha(160),
                              borderRadius: BorderRadius.circular(18),
                              border: Border.all(color: const Color(0xFFFFD700).withAlpha(140), width: 1.5),
                              boxShadow: [
                                BoxShadow(
                                  color: Colors.black.withAlpha(100),
                                  blurRadius: 10,
                                ),
                              ],
                            ),
                            child: Row(
                              children: [
                                Image.asset(
                                  'assets/images/Golden_Star_Icon.png',
                                  width: 18,
                                  height: 18,
                                ),
                                const SizedBox(width: 5),
                                Text(
                                  '$totalWorldStars/${world.maxStars}',
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontWeight: FontWeight.w900,
                                    fontSize: 13,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),

                    // Lore pill
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
                        decoration: BoxDecoration(
                          color: Colors.black.withAlpha(130),
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(color: Colors.white.withAlpha(25)),
                        ),
                        child: Row(
                          children: [
                            Icon(world.icon, color: world.glowColor, size: 20),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Text(
                                world.localizedLore,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(
                                  color: Color(0xFFF1F5F9),
                                  fontSize: 11.5,
                                  height: 1.3,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    const SizedBox(height: 6),

                    // Levels Grid (Up to 1000 Total Levels)
                    Expanded(
                      child: GridView.builder(
                        padding: const EdgeInsets.fromLTRB(16, 6, 16, 24),
                        physics: const BouncingScrollPhysics(),
                        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                          crossAxisCount: 2,
                          crossAxisSpacing: 14,
                          mainAxisSpacing: 14,
                          childAspectRatio: 0.94,
                        ),
                        itemCount: world.levelsCount,
                        itemBuilder: (context, levelIndex) {
                          final unlocked = _isLevelUnlocked(levelIndex);
                          final stars = _starsForLevel(levelIndex);
                          final atmosphere = LevelAtmosphereManager.getAtmosphere(levelIndex, world);

                          return _LevelCard(
                            world: world,
                            levelIndex: levelIndex,
                            levelNumber: levelIndex + 1,
                            styleName: atmosphere.localizedStyleName,
                            isUnlocked: unlocked,
                            stars: stars,
                            onTap: () async {
                              if (unlocked) {
                                if (widget.onLevelSelected != null) {
                                  await widget.onLevelSelected!(world.id, levelIndex);
                                  _refreshStars();
                                }
                              } else {
                                final isWorldLocked = world.id > 0 && !isWorldUnlocked(world.id, 0, _starsMap);
                                if (isWorldLocked) {
                                  showProfessionalLockDialog(
                                    context,
                                    title: 'World Locked',
                                    subtitle: world.localizedTitle,
                                    message: 'Complete all 40 levels of World ${world.worldNumber - 1} to unlock this world!',
                                    currentProgress: getWorldCompletedLevels(world.id - 1, _starsMap),
                                    targetProgress: WorldThemes.levelsPerWorld,
                                  );
                                } else {
                                  final msg = tr('unlock_level_msg')
                                      .replaceAll('{prev}', '$levelIndex')
                                      .replaceAll('{next}', '${levelIndex + 1}');
                                  showProfessionalLockDialog(
                                    context,
                                    title: 'Level Locked',
                                    subtitle: '${tr('level')} ${levelIndex + 1}',
                                    message: msg,
                                    currentProgress: levelIndex,
                                    targetProgress: levelIndex + 1,
                                  );
                                }
                              }
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
    return Material(
      color: Colors.white.withAlpha(25),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: SizedBox(
          width: 44,
          height: 44,
          child: Icon(icon, color: Colors.white, size: 20),
        ),
      ),
    );
  }
}

class _LevelCard extends StatelessWidget {
  final WorldData world;
  final int levelIndex;
  final int levelNumber;
  final String styleName;
  final bool isUnlocked;
  final int stars;
  final VoidCallback onTap;

  const _LevelCard({
    required this.world,
    required this.levelIndex,
    required this.levelNumber,
    required this.styleName,
    required this.isUnlocked,
    required this.stars,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: isUnlocked
              ? (stars > 0 ? world.glowColor : Colors.white.withAlpha(80))
              : Colors.white.withAlpha(25),
          width: isUnlocked ? 2.0 : 1.0,
        ),
        boxShadow: isUnlocked
            ? [
                BoxShadow(
                  color: world.glowColor.withAlpha(60),
                  blurRadius: 14,
                  offset: const Offset(0, 4),
                ),
              ]
            : [],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(21),
        child: Stack(
          children: [
            // 1. Level's distinct atmospheric background preview
            Positioned.fill(
              child: LevelBackgroundBuilder(
                worldIndex: world.id,
                levelIndex: levelIndex,
              ),
            ),

            // 2. Lock dim layer
            if (!isUnlocked)
              Positioned.fill(
                child: Container(color: Colors.black.withAlpha(160)),
              ),

            // 3. Card Content
            Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Top row: Level badge & status
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                        decoration: BoxDecoration(
                          color: isUnlocked ? world.primaryColor.withAlpha(90) : Colors.white10,
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(
                            color: isUnlocked ? world.glowColor : Colors.white24,
                          ),
                        ),
                        child: Text(
                          '${tr('level').toUpperCase()} ${formatNumber(levelNumber)}',
                          style: TextStyle(
                            color: isUnlocked ? Colors.white : Colors.white60,
                            fontWeight: FontWeight.w900,
                            fontSize: 11,
                            letterSpacing: 0.8,
                          ),
                        ),
                      ),
                      if (isUnlocked && stars > 0)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                          decoration: BoxDecoration(
                            color: const Color(0xFF10B981).withAlpha(80),
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(color: const Color(0xFF34D399), width: 1.0),
                          ),
                          child: Text(
                            tr('cleared').toUpperCase(),
                            style: const TextStyle(
                              color: Color(0xFF6EE7B7),
                              fontSize: 9,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                        ),
                      if (!isUnlocked)
                        const Icon(Icons.lock_rounded, color: Color(0xFFFFB703), size: 18),
                    ],
                  ),

                  // Center icon / atmosphere name
                  Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Container(
                          width: 48,
                          height: 48,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            gradient: isUnlocked
                                ? LinearGradient(
                                    colors: [world.primaryColor, world.secondaryColor],
                                  )
                                : null,
                            color: isUnlocked ? null : Colors.white10,
                            boxShadow: isUnlocked
                                ? [
                                    BoxShadow(
                                      color: world.glowColor.withAlpha(100),
                                      blurRadius: 14,
                                    ),
                                  ]
                                : [],
                          ),
                          child: Center(
                            child: isUnlocked
                                ? Text(
                                    formatNumber(levelNumber),
                                    style: const TextStyle(
                                      color: Colors.white,
                                      fontSize: 20,
                                      fontWeight: FontWeight.w900,
                                    ),
                                  )
                                : const Icon(Icons.lock_rounded, color: Colors.white38, size: 22),
                          ),
                        ),
                        const SizedBox(height: 5),
                        Text(
                          styleName,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            color: isUnlocked ? Colors.white : Colors.white38,
                            fontSize: 10.5,
                            fontWeight: FontWeight.w700,
                            shadows: const [Shadow(color: Colors.black, blurRadius: 6)],
                          ),
                        ),
                      ],
                    ),
                  ),

                  // Bottom row: 3D Stars (0 to 3)
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: List.generate(3, (starIdx) {
                      final hasStar = isUnlocked && starIdx < stars;
                      return Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 2.5),
                        child: hasStar
                            ? Image.asset(
                                'assets/images/Golden_Star_Icon.png',
                                width: 20,
                                height: 20,
                              )
                            : Icon(
                                Icons.star_border_rounded,
                                color: Colors.white.withAlpha(60),
                                size: 20,
                              ),
                      );
                    }),
                  ),
                ],
              ),
            ),

            // Tap ripple
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
