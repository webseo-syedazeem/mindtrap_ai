import 'dart:math';
import 'package:flutter/material.dart';
<<<<<<< HEAD
import '../localization/app_language.dart';
=======
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
import '../localization/language_controller.dart';
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

  String get localizedStyleName {
<<<<<<< HEAD
    final styleKey = 'style_${styleName.toLowerCase().replaceAll(' ', '_')}';
    final translated = tr(styleKey);
    final code = LanguageController.instance.currentCode;
    if (translated != styleKey && translated.isNotEmpty) {
      if (code == 'en' || translated != styleName) {
        return translated;
      }
    }

=======
    final code = LanguageController.instance.currentCode;
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      const urMap = {
        'Dawn Awaking': 'طلوعِ سحر',
        'Nebula Mist': 'دھندلی کہکشاں',
        'Aurora Stream': 'شفقِ قطبی',
        'Crystal Shimmer': 'کرسٹل چمک',
        'Solar Flare': 'شمسی شعلہ',
<<<<<<< HEAD
        'Star Cluster': 'ستاروں کا جھرمٹ',
        'Cyber Vector': 'سائبر ویکٹر',
        'Void Vortex': 'خلائی گرداب',
        'Dimensional Rift': 'کائناتی شگاف',
        'Zenith Pinnacle': 'فلکی بلندی',
      };
      return urMap[styleName] ?? styleName;
    } else if (code == 'hi' || code == 'bn') {
      const hiMap = {
        'Dawn Awaking': 'भोर का जागरण',
        'Nebula Mist': 'नीहारिका कोहरा',
        'Aurora Stream': 'ध्रुवीय ज्योति',
        'Crystal Shimmer': 'स्फटिक चमक',
        'Solar Flare': 'सौर ज्वाला',
        'Star Cluster': 'तारा गुच्छ',
        'Cyber Vector': 'साइबर वेक्टर',
        'Void Vortex': 'शून्य भंवर',
        'Dimensional Rift': 'आयामी दरार',
        'Zenith Pinnacle': 'शीर्ष शिखर',
      };
      return hiMap[styleName] ?? styleName;
    } else if (code == 'pa') {
      const paMap = {
        'Dawn Awaking': 'ਸਵੇਰ ਦਾ ਜਾਗਣਾ',
        'Nebula Mist': 'ਨੀਹਾਰਿਕਾ ਧੁੰਦ',
        'Aurora Stream': 'ਧਰੁਵੀ ਰੋਸ਼ਨੀ',
        'Crystal Shimmer': 'ਕ੍ਰਿਸਟਲ ਚਮਕ',
        'Solar Flare': 'ਸੂਰਜੀ ਲਾਟ',
        'Star Cluster': 'ਤਾਰਿਆਂ ਦਾ ਝੁਰਮਟ',
        'Cyber Vector': 'ਸਾਈਬਰ ਵੈਕਟਰ',
        'Void Vortex': 'ਖਲਾਅ ਘੁੰਮਣਘੇਰੀ',
        'Dimensional Rift': 'ਬ੍ਰਹਿਮੰਡੀ ਪਾੜਾ',
        'Zenith Pinnacle': 'ਸਿਖਰਲੀ ਚੋਟੀ',
      };
      return paMap[styleName] ?? styleName;
=======
        'Emerald Glade': 'زمردی وادی',
        'Twilight Glow': 'شام کا نور',
        'Celestial Rays': 'آسمانی شعاعیں',
        'Golden Dust': 'سنہری غبار',
        'Midnight Echo': 'نصف شب کی بازگشت',
      };
      return urMap[styleName] ?? styleName;
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
    } else if (code == 'ar') {
      const arMap = {
        'Dawn Awaking': 'صحوة الفجر',
        'Nebula Mist': 'سديم النجوم',
        'Aurora Stream': 'شفق قطبي',
        'Crystal Shimmer': 'بريق الكريستال',
        'Solar Flare': 'توهج شمسي',
<<<<<<< HEAD
        'Star Cluster': 'عنقود النجوم',
        'Cyber Vector': 'متجه سايبر',
        'Void Vortex': 'دوامة الفراغ',
        'Dimensional Rift': 'صدع أبعادي',
        'Zenith Pinnacle': 'قمة الأوج',
      };
      return arMap[styleName] ?? styleName;
=======
        'Emerald Glade': 'مرج الزمرد',
        'Twilight Glow': 'توهج الشفق',
        'Celestial Rays': 'أشعة سماوية',
        'Golden Dust': 'غبار ذهبي',
        'Midnight Echo': 'صدى منتصف الليل',
      };
      return arMap[styleName] ?? styleName;
    } else if (code == 'hi' || code == 'bn') {
      const hiMap = {
        'Dawn Awaking': 'भोर का जागरण',
        'Nebula Mist': 'नीहारिका कोहरा',
        'Aurora Stream': 'ध्रुवीय ज्योति',
        'Crystal Shimmer': 'स्फटिक चमक',
        'Solar Flare': 'सौर ज्वाला',
        'Emerald Glade': 'पन्ना घाटी',
        'Twilight Glow': 'गोधूलि प्रकाश',
        'Celestial Rays': 'दिव्य किरणें',
        'Golden Dust': 'स्वर्ण धूल',
        'Midnight Echo': 'मध्यरात्रि गूंज',
      };
      return hiMap[styleName] ?? styleName;
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
    } else if (code == 'es' || code == 'pt') {
      const esMap = {
        'Dawn Awaking': 'Despertar del Alba',
        'Nebula Mist': 'Niebla Nebulosa',
        'Aurora Stream': 'Torrente de Aurora',
        'Crystal Shimmer': 'Brillo de Cristal',
        'Solar Flare': 'Llamarada Solar',
<<<<<<< HEAD
        'Star Cluster': 'Cúmulo Estelar',
        'Cyber Vector': 'Vector Cibernético',
        'Void Vortex': 'Vórtice del Vacío',
        'Dimensional Rift': 'Fisura Dimensional',
        'Zenith Pinnacle': 'Cénit Celestial',
=======
        'Emerald Glade': 'Claro Esmeralda',
        'Twilight Glow': 'Brillo Crepuscular',
        'Celestial Rays': 'Rayos Celestiales',
        'Golden Dust': 'Polvo Dorado',
        'Midnight Echo': 'Eco de Medianoche',
>>>>>>> 6d559dfe6413366ed60a0eedce09101114d17a9f
      };
      return esMap[styleName] ?? styleName;
    }
    return styleName;
  }
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

  static const List<String> scenicAssets = [
    'assets/images/Stage-1.webp',
    'assets/images/Stage-2.webp',
    'assets/images/Stage-3.webp',
    'assets/images/Stage-4.webp',
    'assets/images/Stage-5.webp',
    'assets/images/Stage-6.webp',
    'assets/images/Stage-7.webp',
    'assets/images/daily_puzzle_landing_background.webp',
    'assets/images/level_complete_background.webp',
    'assets/images/puzzle_complete_background.webp',
    'assets/images/quiz_background.webp',
    'assets/images/home_background.webp',
    'assets/images/quiz_correct_background.webp',
    'assets/images/game over background image.webp',
  ];

  static String getBackgroundAsset(int worldIndex, int levelIndex) {
    final bgIndex = ((worldIndex * 5) + levelIndex) % scenicAssets.length;
    return scenicAssets[bgIndex];
  }

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
    // Unique distinct background image for every level and stage
    final bgAsset = getBackgroundAsset(worldIndex, levelIndex);

    return Stack(
      fit: StackFit.expand,
      children: [
        // 1. Level distinct scenic background image
        Image(
          image: AssetImage(bgAsset),
          fit: BoxFit.cover,
          alignment: Alignment.topCenter,
          gaplessPlayback: true,
          errorBuilder: (context, error, stackTrace) {
            return Container(color: world.cardGradientEnd);
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
