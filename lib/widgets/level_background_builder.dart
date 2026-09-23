import 'dart:math';
import 'package:flutter/material.dart';
import '../models/world_model.dart';

class LevelAtmosphere {
  final String styleName;
  final Alignment lightOrigin;
  final List<Color> atmosphereGradient;
  final Color overlayTint;
  final double vignetteStrength;
  final bool hasConstellation;
  final bool hasRays;
  final double glowRadius;

  const LevelAtmosphere({
    required this.styleName,
    required this.lightOrigin,
    required this.atmosphereGradient,
    required this.overlayTint,
    this.vignetteStrength = 0.35,
    this.hasConstellation = false,
    this.hasRays = false,
    this.glowRadius = 0.8,
  });
}

class LevelAtmosphereManager {
  LevelAtmosphereManager._();

  static LevelAtmosphere getAtmosphere(int levelIndex, WorldData world) {
    final idx = (levelIndex % 10).abs();
    final p = world.primaryColor;
    final s = world.secondaryColor;
    final g = world.glowColor;

    switch (idx) {
      case 0:
        return LevelAtmosphere(
          styleName: 'Dawn Awaking',
          lightOrigin: const Alignment(0.0, -0.6),
          atmosphereGradient: [
            g.withAlpha(95),
            p.withAlpha(45),
            Colors.transparent,
          ],
          overlayTint: p.withAlpha(20),
          vignetteStrength: 0.35,
          hasRays: true,
          glowRadius: 0.9,
        );
      case 1:
        return LevelAtmosphere(
          styleName: 'Nebula Mist',
          lightOrigin: const Alignment(-0.7, -0.4),
          atmosphereGradient: [
            s.withAlpha(90),
            g.withAlpha(40),
            Colors.transparent,
          ],
          overlayTint: s.withAlpha(20),
          vignetteStrength: 0.35,
          hasConstellation: true,
          glowRadius: 0.85,
        );
      case 2:
        return LevelAtmosphere(
          styleName: 'Aurora Stream',
          lightOrigin: const Alignment(0.8, -0.5),
          atmosphereGradient: [
            const Color(0xFF00FFC8).withAlpha(85),
            p.withAlpha(45),
            Colors.transparent,
          ],
          overlayTint: const Color(0xFF00E5FF).withAlpha(20),
          vignetteStrength: 0.35,
          hasRays: true,
          glowRadius: 0.8,
        );
      case 3:
        return LevelAtmosphere(
          styleName: 'Crystal Shimmer',
          lightOrigin: const Alignment(0.0, 0.0),
          atmosphereGradient: [
            Colors.white.withAlpha(70),
            g.withAlpha(50),
            Colors.transparent,
          ],
          overlayTint: g.withAlpha(20),
          vignetteStrength: 0.35,
          hasConstellation: true,
          glowRadius: 0.75,
        );
      case 4:
        return LevelAtmosphere(
          styleName: 'Solar Flare',
          lightOrigin: const Alignment(0.0, -0.8),
          atmosphereGradient: [
            const Color(0xFFFFB300).withAlpha(110),
            p.withAlpha(50),
            Colors.transparent,
          ],
          overlayTint: const Color(0xFFFF8A00).withAlpha(25),
          vignetteStrength: 0.38,
          hasRays: true,
          glowRadius: 1.0,
        );
      case 5:
        return LevelAtmosphere(
          styleName: 'Star Cluster',
          lightOrigin: const Alignment(-0.6, 0.3),
          atmosphereGradient: [
            const Color(0xFFE0E7FF).withAlpha(80),
            s.withAlpha(55),
            Colors.transparent,
          ],
          overlayTint: s.withAlpha(20),
          vignetteStrength: 0.35,
          hasConstellation: true,
          glowRadius: 0.8,
        );
      case 6:
        return LevelAtmosphere(
          styleName: 'Cyber Vector',
          lightOrigin: const Alignment(0.7, 0.4),
          atmosphereGradient: [
            const Color(0xFF00FFCC).withAlpha(85),
            p.withAlpha(50),
            Colors.transparent,
          ],
          overlayTint: const Color(0xFF00FFB2).withAlpha(20),
          vignetteStrength: 0.35,
          hasRays: true,
          glowRadius: 0.85,
        );
      case 7:
        return LevelAtmosphere(
          styleName: 'Void Vortex',
          lightOrigin: const Alignment(0.0, -0.2),
          atmosphereGradient: [
            const Color(0xFFEC4899).withAlpha(85),
            s.withAlpha(50),
            Colors.transparent,
          ],
          overlayTint: const Color(0xFFD946EF).withAlpha(20),
          vignetteStrength: 0.4,
          hasConstellation: true,
          glowRadius: 0.7,
        );
      case 8:
        return LevelAtmosphere(
          styleName: 'Dimensional Rift',
          lightOrigin: const Alignment(-0.5, -0.7),
          atmosphereGradient: [
            const Color(0xFF38BDF8).withAlpha(85),
            const Color(0xFFF43F5E).withAlpha(50),
            Colors.transparent,
          ],
          overlayTint: p.withAlpha(25),
          vignetteStrength: 0.38,
          hasRays: true,
          glowRadius: 0.9,
        );
      case 9:
      default:
        return LevelAtmosphere(
          styleName: 'Zenith Pinnacle',
          lightOrigin: const Alignment(0.0, -0.5),
          atmosphereGradient: [
            const Color(0xFFFFD700).withAlpha(120),
            g.withAlpha(65),
            Colors.transparent,
          ],
          overlayTint: const Color(0xFFFFC107).withAlpha(30),
          vignetteStrength: 0.4,
          hasRays: true,
          hasConstellation: true,
          glowRadius: 1.1,
        );
    }
  }
}

class LevelBackgroundBuilder extends StatelessWidget {
  final int worldIndex;
  final int levelIndex;
  final Widget? child;

  const LevelBackgroundBuilder({
    super.key,
    required this.worldIndex,
    required this.levelIndex,
    this.child,
  });

  @override
  Widget build(BuildContext context) {
    final world = WorldThemes.getWorld(worldIndex);
    final atmosphere = LevelAtmosphereManager.getAtmosphere(levelIndex, world);

    return Stack(
      fit: StackFit.expand,
      children: [
        // 1. World distinct base background image (CLEAR & VIBRANT)
        Image(
          image: AssetImage(world.backgroundAsset),
          fit: BoxFit.cover,
          alignment: Alignment.topCenter,
          gaplessPlayback: true,
          errorBuilder: (context, error, stackTrace) {
            return Container(color: const Color(0xFF0F0826));
          },
        ),

        // 2. Level distinct atmospheric lighting & color grading (Luminous aura)
        DecoratedBox(
          decoration: BoxDecoration(
            gradient: RadialGradient(
              center: atmosphere.lightOrigin,
              radius: atmosphere.glowRadius,
              colors: atmosphere.atmosphereGradient,
              stops: const [0.0, 0.45, 1.0],
            ),
          ),
        ),

        // 3. Level ambient tint overlay
        DecoratedBox(
          decoration: BoxDecoration(
            color: atmosphere.overlayTint,
            backgroundBlendMode: BlendMode.screen,
          ),
        ),

        // 4. Distinct ambient geometry (rays or constellation stars)
        CustomPaint(
          painter: _AtmospherePainter(
            hasRays: atmosphere.hasRays,
            hasConstellation: atmosphere.hasConstellation,
            origin: atmosphere.lightOrigin,
            primaryColor: world.primaryColor,
            glowColor: world.glowColor,
            seed: (worldIndex * 13) + (levelIndex * 29),
          ),
        ),

        // 5. Cinema vignette for high UI readability without muddying the scenery
        DecoratedBox(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [
                Colors.black.withAlpha(70),
                Colors.transparent,
                Colors.black.withAlpha(
                  (255 * atmosphere.vignetteStrength).toInt(),
                ),
              ],
              stops: const [0.0, 0.4, 1.0],
            ),
          ),
        ),

        // 6. Child content if provided
        ?child,
      ],
    );
  }
}

class _AtmospherePainter extends CustomPainter {
  final bool hasRays;
  final bool hasConstellation;
  final Alignment origin;
  final Color primaryColor;
  final Color glowColor;
  final int seed;

  _AtmospherePainter({
    required this.hasRays,
    required this.hasConstellation,
    required this.origin,
    required this.primaryColor,
    required this.glowColor,
    required this.seed,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final random = Random(seed);

    // Light rays if enabled
    if (hasRays) {
      final rayPaint = Paint()
        ..color = glowColor.withAlpha(28)
        ..style = PaintingStyle.fill
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 16);

      final ox = size.width * (origin.x + 1) / 2;
      final oy = size.height * (origin.y + 1) / 2;

      for (int i = 0; i < 5; i++) {
        final angle = (i * (pi / 3.2)) + (random.nextDouble() * 0.2);
        final length = size.height * (0.6 + random.nextDouble() * 0.5);
        final spread = 0.10 + random.nextDouble() * 0.08;

        final path = Path()
          ..moveTo(ox, oy)
          ..lineTo(
            ox + cos(angle - spread) * length,
            oy + sin(angle - spread) * length,
          )
          ..lineTo(
            ox + cos(angle + spread) * length,
            oy + sin(angle + spread) * length,
          )
          ..close();

        canvas.drawPath(path, rayPaint);
      }
    }

    // Constellations / ambient dust
    if (hasConstellation) {
      final starPaint = Paint()..style = PaintingStyle.fill;
      final linePaint = Paint()
        ..color = glowColor.withAlpha(35)
        ..strokeWidth = 1.0
        ..style = PaintingStyle.stroke;

      final points = <Offset>[];
      for (int i = 0; i < 16; i++) {
        final x = random.nextDouble() * size.width;
        final y = random.nextDouble() * (size.height * 0.7);
        points.add(Offset(x, y));

        final radius = 1.0 + random.nextDouble() * 2.0;
        starPaint.color = Colors.white.withAlpha(
          (90 + random.nextInt(150)),
        );
        canvas.drawCircle(Offset(x, y), radius, starPaint);
      }

      // Connect nearest stars
      for (int i = 0; i < points.length - 1; i += 2) {
        if (i + 1 < points.length) {
          final dist = (points[i] - points[i + 1]).distance;
          if (dist < 130) {
            canvas.drawLine(points[i], points[i + 1], linePaint);
          }
        }
      }
    }
  }

  @override
  bool shouldRepaint(covariant _AtmospherePainter oldDelegate) {
    return oldDelegate.seed != seed ||
        oldDelegate.hasRays != hasRays ||
        oldDelegate.hasConstellation != hasConstellation;
  }
}
