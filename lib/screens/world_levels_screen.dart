import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../models/world_model.dart';
import '../screens/language_selection_screen.dart';
import '../widgets/level_background_builder.dart';
import '../widgets/professional_lock_dialog.dart';
<<<<<<< HEAD
import '../main.dart' show PuzzleScreen, smoothPageRoute;
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
<<<<<<< HEAD
                            icon: Icons.arrow_back_rounded,
=======
                            icon: Icons.arrow_back_ios_new_rounded,
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
<<<<<<< HEAD
                              if (mounted) setState(() {});
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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

<<<<<<< HEAD
                    // Levels List (single full-width column)
                    Expanded(
                      child: ListView.separated(
                        padding: const EdgeInsets.fromLTRB(16, 6, 16, 24),
                        physics: const BouncingScrollPhysics(),
                        separatorBuilder: (context, index) => const SizedBox(height: 14),
=======
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
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
<<<<<<< HEAD
                                } else {
                                  await Navigator.push(
                                    context,
                                    smoothPageRoute(
                                      PuzzleScreen(
                                        stageIndex: world.id,
                                        levelIndex: levelIndex,
                                      ),
                                    ),
                                  );
                                }
                                _refreshStars();
=======
                                  _refreshStars();
                                }
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                              } else {
                                final isWorldLocked = world.id > 0 && !isWorldUnlocked(world.id, 0, _starsMap);
                                if (isWorldLocked) {
                                  showProfessionalLockDialog(
                                    context,
<<<<<<< HEAD
                                    title: tr('world_locked'),
                                    subtitle: world.localizedTitle,
                                    message: tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),
=======
                                    title: 'World Locked',
                                    subtitle: world.localizedTitle,
                                    message: 'Complete all 40 levels of World ${world.worldNumber - 1} to unlock this world!',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                                    currentProgress: getWorldCompletedLevels(world.id - 1, _starsMap),
                                    targetProgress: WorldThemes.levelsPerWorld,
                                  );
                                } else {
                                  final msg = tr('unlock_level_msg')
                                      .replaceAll('{prev}', '$levelIndex')
                                      .replaceAll('{next}', '${levelIndex + 1}');
                                  showProfessionalLockDialog(
                                    context,
<<<<<<< HEAD
                                    title: tr('level_locked'),
=======
                                    title: 'Level Locked',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
<<<<<<< HEAD
    final isRtl = Directionality.of(context) == TextDirection.rtl;
    final displayIcon = (icon == Icons.arrow_back_rounded && isRtl)
        ? Icons.arrow_forward_rounded
        : icon;
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
    return Material(
      color: Colors.white.withAlpha(25),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: SizedBox(
<<<<<<< HEAD
          width: 38,
          height: 38,
          child: Icon(displayIcon, color: Colors.white, size: 24),
=======
          width: 44,
          height: 44,
          child: Icon(icon, color: Colors.white, size: 20),
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
<<<<<<< HEAD
      height: 112,
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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

<<<<<<< HEAD
            // 2b. Left-to-right readability gradient
            Positioned.fill(
              child: DecoratedBox(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.centerLeft,
                    end: Alignment.centerRight,
                    colors: [
                      Colors.black.withAlpha(150),
                      Colors.black.withAlpha(40),
                      Colors.transparent,
                    ],
                    stops: const [0.0, 0.55, 1.0],
                  ),
                ),
              ),
            ),

            // 3. Card Content (horizontal banner)
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              child: Row(
                children: [
                  // Level number badge
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
                          : null,
                      color: isUnlocked ? null : Colors.white10,
                      border: Border.all(
                        color: isUnlocked ? Colors.white.withAlpha(200) : Colors.white24,
                        width: 2,
                      ),
                      boxShadow: isUnlocked
                          ? [
                              BoxShadow(
                                color: world.glowColor.withAlpha(110),
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
                                fontSize: 22,
                                fontWeight: FontWeight.w900,
                              ),
                            )
                          : const Icon(Icons.lock_rounded, color: Colors.white38, size: 24),
                    ),
                  ),
                  const SizedBox(width: 14),

                  // Title, atmosphere name, stars
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
=======
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
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                          '${tr('level').toUpperCase()} ${formatNumber(levelNumber)}',
                          style: TextStyle(
                            color: isUnlocked ? Colors.white : Colors.white60,
                            fontWeight: FontWeight.w900,
<<<<<<< HEAD
                            fontSize: 16,
                            letterSpacing: 0.8,
                            shadows: const [Shadow(color: Colors.black, blurRadius: 6)],
                          ),
                        ),
                        const SizedBox(height: 2),
=======
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
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                        Text(
                          styleName,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
<<<<<<< HEAD
                            color: isUnlocked ? Colors.white.withAlpha(220) : Colors.white38,
                            fontSize: 12.5,
                            fontWeight: FontWeight.w600,
                            shadows: const [Shadow(color: Colors.black, blurRadius: 6)],
                          ),
                        ),
                        const SizedBox(height: 6),
                        Row(
                          children: List.generate(3, (starIdx) {
                            final hasStar = isUnlocked && starIdx < stars;
                            return Padding(
                              padding: const EdgeInsets.only(right: 4),
                              child: hasStar
                                  ? Image.asset(
                                      'assets/images/Golden_Star_Icon.png',
                                      width: 20,
                                      height: 20,
                                    )
                                  : Icon(
                                      Icons.star_border_rounded,
                                      color: Colors.white.withAlpha(90),
                                      size: 20,
                                    ),
                            );
                          }),
                        ),
=======
                            color: isUnlocked ? Colors.white : Colors.white38,
                            fontSize: 10.5,
                            fontWeight: FontWeight.w700,
                            shadows: const [Shadow(color: Colors.black, blurRadius: 6)],
                          ),
                        ),
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
                      ],
                    ),
                  ),

<<<<<<< HEAD
                  // Status on the right
                  if (!isUnlocked)
                    const Icon(Icons.lock_rounded, color: Color(0xFFFFB703), size: 24)
                  else if (stars > 0)
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                      decoration: BoxDecoration(
                        color: const Color(0xFF10B981).withAlpha(110),
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: const Color(0xFF34D399), width: 1.0),
                      ),
                      child: Text(
                        tr('cleared').toUpperCase(),
                        style: const TextStyle(
                          color: Color(0xFFD1FAE5),
                          fontSize: 10,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    )
                  else
                    Container(
                      width: 40,
                      height: 40,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        gradient: const LinearGradient(
                          colors: [Color(0xFF38BDF8), Color(0xFF2563EB)],
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                        ),
                        border: Border.all(color: Colors.white, width: 2),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF2563EB).withAlpha(120),
                            blurRadius: 10,
                          ),
                        ],
                      ),
                      child: const Icon(Icons.play_arrow_rounded, color: Colors.white, size: 24),
                    ),
=======
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
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
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
