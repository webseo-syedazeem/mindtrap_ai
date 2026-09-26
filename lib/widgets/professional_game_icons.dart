import 'dart:math';
import 'package:flutter/material.dart';
import '../localization/language_controller.dart';

/// Tactile bounce button wrapper providing physical push-button feel and sound.
class TactileBounce extends StatefulWidget {
  final Widget child;
  final VoidCallback? onTap;
  final double pressedScale;
  final Duration duration;

  const TactileBounce({
    super.key,
    required this.child,
    this.onTap,
    this.pressedScale = 0.92,
    this.duration = const Duration(milliseconds: 110),
  });

  @override
  State<TactileBounce> createState() => _TactileBounceState();
}

class _TactileBounceState extends State<TactileBounce>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: widget.duration);
    _scaleAnimation = Tween<double>(begin: 1.0, end: widget.pressedScale).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _handleTapDown(TapDownDetails _) {
    _controller.forward();
  }

  void _handleTapUp(TapUpDetails _) {
    _controller.reverse();
    widget.onTap?.call();
  }

  void _handleTapCancel() {
    _controller.reverse();
  }

  @override
  Widget build(BuildContext context) {
    if (widget.onTap == null) {
      return widget.child;
    }

    return GestureDetector(
      onTapDown: _handleTapDown,
      onTapUp: _handleTapUp,
      onTapCancel: _handleTapCancel,
      behavior: HitTestBehavior.opaque,
      child: ScaleTransition(
        scale: _scaleAnimation,
        child: widget.child,
      ),
    );
  }
}

/// Ultra-professional 3D circular action button with metallic bevel and glossy glass dome.
class ProfessionalCircleButton extends StatelessWidget {
  final Widget? customIcon;
  final IconData? icon;
  final Color? iconColor;
  final double size;
  final VoidCallback? onPressed;
  final String? tooltip;
  final Color baseColor;
  final Color rimColor;
  final bool hasGlow;
  final Color glowColor;

  const ProfessionalCircleButton({
    super.key,
    this.customIcon,
    this.icon,
    this.iconColor,
    this.size = 42.0,
    this.onPressed,
    this.tooltip,
    this.baseColor = Colors.white,
    this.rimColor = const Color(0xFFE2E8F0),
    this.hasGlow = false,
    this.glowColor = const Color(0x3338BDF8),
  }) : assert(customIcon != null || icon != null);

  @override
  Widget build(BuildContext context) {
    Widget buttonContent = Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        // Multi-layer physical 3D button shadow
        boxShadow: [
          // Ambient soft shadow
          BoxShadow(
            color: const Color(0x280F172A),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
          // 3D bottom bevel ridge
          BoxShadow(
            color: const Color(0x35000000),
            blurRadius: 2,
            offset: const Offset(0, 3),
          ),
          if (hasGlow)
            BoxShadow(
              color: glowColor,
              blurRadius: 14,
              spreadRadius: 2,
            ),
        ],
        // Outer metallic rim
        gradient: LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [
            Colors.white,
            rimColor,
            rimColor.withAlpha(200),
          ],
        ),
      ),
      padding: const EdgeInsets.all(2.2), // Rim thickness
      child: Container(
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          // Inner face with top-lit specular glare
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              baseColor,
              Color.lerp(baseColor, const Color(0xFFF1F5F9), 0.7) ?? baseColor,
              Color.lerp(baseColor, const Color(0xFFE2E8F0), 0.9) ?? baseColor,
            ],
            stops: const [0.0, 0.65, 1.0],
          ),
        ),
        child: Stack(
          alignment: Alignment.center,
          children: [
            // Top specular shine arc (glass highlight)
            Positioned(
              top: 1.5,
              child: Container(
                width: size * 0.65,
                height: size * 0.28,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.all(
                    Radius.elliptical(size * 0.65, size * 0.28),
                  ),
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.white.withAlpha(210),
                      Colors.white.withAlpha(0),
                    ],
                  ),
                ),
              ),
            ),
            // The icon
            Center(
              child: customIcon ??
                  Icon(
                    icon,
                    size: size * 0.52,
                    color: iconColor ?? const Color(0xFF1E293B),
                  ),
            ),
          ],
        ),
      ),
    );

    if (tooltip != null) {
      buttonContent = Tooltip(message: tooltip!, child: buttonContent);
    }

    return TactileBounce(
      onTap: onPressed,
      child: buttonContent,
    );
  }
}

/// Custom professional 3-bar hamburger game drawer icon with metallic finish.
class ProfessionalMenuIcon extends StatelessWidget {
  final double size;
  final Color primaryColor;

  const ProfessionalMenuIcon({
    super.key,
    this.size = 20,
    this.primaryColor = const Color(0xFF1E293B),
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          _buildBar(width: size, height: 2.6),
          const SizedBox(height: 3.2),
          _buildBar(width: size * 0.76, height: 2.6, alignLeft: true),
          const SizedBox(height: 3.2),
          _buildBar(width: size * 0.92, height: 2.6),
        ],
      ),
    );
  }

  Widget _buildBar({
    required double width,
    required double height,
    bool alignLeft = false,
  }) {
    return Align(
      alignment: alignLeft ? Alignment.centerLeft : Alignment.center,
      child: Container(
        width: width,
        height: height,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(height / 2),
          gradient: LinearGradient(
            colors: [
              primaryColor,
              primaryColor.withAlpha(220),
            ],
          ),
          boxShadow: [
            BoxShadow(
              color: primaryColor.withAlpha(50),
              blurRadius: 1,
              offset: const Offset(0, 1),
            ),
          ],
        ),
      ),
    );
  }
}

/// Custom professional player profile icon with avatar medallion and golden crest.
class ProfessionalProfileIcon extends StatelessWidget {
  final double size;

  const ProfessionalProfileIcon({super.key, this.size = 22});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        alignment: Alignment.center,
        children: [
          // Background aura
          Container(
            width: size * 0.94,
            height: size * 0.94,
            decoration: const BoxDecoration(
              shape: BoxShape.circle,
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [Color(0xFF0284C7), Color(0xFF0369A1)],
              ),
            ),
          ),
          // Stylized avatar silhouette
          Positioned(
            top: size * 0.15,
            child: Container(
              width: size * 0.38,
              height: size * 0.38,
              decoration: const BoxDecoration(
                shape: BoxShape.circle,
                color: Colors.white,
              ),
            ),
          ),
          Positioned(
            bottom: size * 0.08,
            child: Container(
              width: size * 0.65,
              height: size * 0.35,
              decoration: const BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(10),
                  topRight: Radius.circular(10),
                  bottomLeft: Radius.circular(8),
                  bottomRight: Radius.circular(8),
                ),
              ),
            ),
          ),
          // Golden star crest on top-right
          Positioned(
            top: 0,
            right: 0,
            child: Container(
              width: size * 0.36,
              height: size * 0.36,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: const LinearGradient(
                  colors: [Color(0xFFFFDF00), Color(0xFFF59E0B)],
                ),
                border: Border.all(color: Colors.white, width: 0.8),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x40F59E0B),
                    blurRadius: 3,
                    offset: Offset(0, 1),
                  ),
                ],
              ),
              child: Center(
                child: Icon(
                  Icons.star_rounded,
                  color: Colors.white,
                  size: size * 0.26,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Custom professional 3D world globe medallion icon.
class ProfessionalWorldsIcon extends StatelessWidget {
  final double size;

  const ProfessionalWorldsIcon({super.key, this.size = 23});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        alignment: Alignment.center,
        children: [
          // Ocean sphere
          Container(
            width: size * 0.9,
            height: size * 0.9,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: const RadialGradient(
                center: Alignment(-0.3, -0.3),
                radius: 0.85,
                colors: [
                  Color(0xFF38BDF8),
                  Color(0xFF0284C7),
                  Color(0xFF0F766E),
                ],
              ),
              boxShadow: [
                BoxShadow(
                  color: const Color(0xFF0D9488).withAlpha(100),
                  blurRadius: 5,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
          ),
          // Stylized landmass / continents & grid
          CustomPaint(
            size: Size(size * 0.85, size * 0.85),
            painter: _GlobeContinentsPainter(),
          ),
          // Latitude / Orbit ring
          Transform.rotate(
            angle: -pi / 6,
            child: Container(
              width: size * 0.98,
              height: size * 0.42,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.all(
                  Radius.elliptical(size * 0.98, size * 0.42),
                ),
                border: Border.all(
                  color: const Color(0xFFFFD54F).withAlpha(220),
                  width: 1.1,
                ),
              ),
            ),
          ),
          // Mini compass sparkle
          Positioned(
            top: 2,
            right: 2,
            child: Container(
              width: 5,
              height: 5,
              decoration: const BoxDecoration(
                shape: BoxShape.circle,
                color: Color(0xFFFFFBEB),
                boxShadow: [
                  BoxShadow(color: Colors.white, blurRadius: 4, spreadRadius: 1),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _GlobeContinentsPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = const Color(0xFF34D399).withAlpha(235)
      ..style = PaintingStyle.fill;

    // Stylized continent patches
    final path1 = Path();
    path1.addOval(Rect.fromLTWH(size.width * 0.18, size.height * 0.22, size.width * 0.32, size.height * 0.38));
    canvas.drawPath(path1, paint);

    final path2 = Path();
    path2.addOval(Rect.fromLTWH(size.width * 0.52, size.height * 0.38, size.width * 0.34, size.height * 0.36));
    canvas.drawPath(path2, paint);

    // Meridian line
    final linePaint = Paint()
      ..color = Colors.white.withAlpha(90)
      ..strokeWidth = 0.8
      ..style = PaintingStyle.stroke;
    canvas.drawOval(
      Rect.fromCenter(
        center: Offset(size.width / 2, size.height / 2),
        width: size.width * 0.45,
        height: size.height * 0.88,
      ),
      linePaint,
    );
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Custom professional precision 3D gear settings icon.
class ProfessionalSettingsIcon extends StatelessWidget {
  final double size;

  const ProfessionalSettingsIcon({super.key, this.size = 23});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        alignment: Alignment.center,
        children: [
          // Outer gear wheel
          Icon(
            Icons.settings_rounded,
            size: size * 0.98,
            color: const Color(0xFF475569),
          ),
          // Inner metallic specular gear
          Icon(
            Icons.settings_rounded,
            size: size * 0.86,
            color: const Color(0xFF64748B),
          ),
          // Center sapphire / ruby jewel pivot
          Container(
            width: size * 0.32,
            height: size * 0.32,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: const RadialGradient(
                colors: [Color(0xFF38BDF8), Color(0xFF0369A1)],
              ),
              border: Border.all(color: Colors.white, width: 0.9),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x400284C7),
                  blurRadius: 3,
                  offset: Offset(0, 1),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// Ultra-professional Free Daily Gift push-button with 3D ribbon and pulsing FREE badge.
class ProfessionalGiftButton extends StatefulWidget {
  final VoidCallback? onPressed;

  const ProfessionalGiftButton({super.key, this.onPressed});

  @override
  State<ProfessionalGiftButton> createState() => _ProfessionalGiftButtonState();
}

class _ProfessionalGiftButtonState extends State<ProfessionalGiftButton>
    with SingleTickerProviderStateMixin {
  late AnimationController _pulseController;
  late Animation<double> _pulseAnimation;

  @override
  void initState() {
    super.initState();
    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1400),
    )..repeat(reverse: true);
    _pulseAnimation = Tween<double>(begin: 1.0, end: 1.08).animate(
      CurvedAnimation(parent: _pulseController, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _pulseController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return TactileBounce(
      onTap: widget.onPressed,
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          Container(
            width: 44,
            height: 44,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: const LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Color(0xFFFFFBEB),
                  Color(0xFFFEF3C7),
                  Color(0xFFFDE68A),
                ],
              ),
              border: Border.all(color: const Color(0xFFF59E0B), width: 2.0),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x60F59E0B),
                  blurRadius: 12,
                  offset: Offset(0, 4),
                ),
                BoxShadow(
                  color: Color(0x35000000),
                  blurRadius: 2,
                  offset: Offset(0, 3),
                ),
              ],
            ),
            child: Stack(
              alignment: Alignment.center,
              children: [
                // Top glare shine
                Positioned(
                  top: 2,
                  child: Container(
                    width: 26,
                    height: 12,
                    decoration: BoxDecoration(
                      borderRadius: const BorderRadius.all(Radius.elliptical(26, 12)),
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.white.withAlpha(220),
                          Colors.white.withAlpha(0),
                        ],
                      ),
                    ),
                  ),
                ),
                const Icon(
                  Icons.card_giftcard_rounded,
                  color: Color(0xFFDC2626),
                  size: 25,
                ),
              ],
            ),
          ),
          // Pulsing FREE badge
          Positioned(
            top: -3,
            right: -4,
            child: ScaleTransition(
              scale: _pulseAnimation,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [Color(0xFFEF4444), Color(0xFFB91C1C)],
                  ),
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: const Color(0xFFFFD54F), width: 1.4),
                  boxShadow: const [
                    BoxShadow(
                      color: Color(0x70EF4444),
                      blurRadius: 6,
                      offset: Offset(0, 2),
                    ),
                  ],
                ),
                child: const Text(
                  'FREE',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 8.5,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0.6,
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

/// Ultra-professional game currency pill with 3D medallion, gold/cyan/green accenting, and tactile feedback.
class ProfessionalCurrencyPill extends StatelessWidget {
  final String iconAsset;
  final int value;
  final VoidCallback? onTap;
  final VoidCallback? onAddPressed;

  const ProfessionalCurrencyPill({
    super.key,
    required this.iconAsset,
    required this.value,
    this.onTap,
    this.onAddPressed,
  });

  @override
  Widget build(BuildContext context) {
    final isCoin = iconAsset.contains('coin');
    final isGem = iconAsset.contains('gem');

    // Luxurious palette per currency type
    final Color rimColorTop = isCoin
        ? const Color(0xFFFFE082)
        : (isGem ? const Color(0xFFBAE6FD) : const Color(0xFFFEF08A));

    final Color rimColorBottom = isCoin
        ? const Color(0xFFD97706)
        : (isGem ? const Color(0xFF0284C7) : const Color(0xFFCA8A04));

    final Color badgeGlow = isCoin
        ? const Color(0xFFFFB703)
        : (isGem ? const Color(0xFF38BDF8) : const Color(0xFFFACC15));

    final Color textColor = isCoin
        ? const Color(0xFF92400E)
        : (isGem ? const Color(0xFF0369A1) : const Color(0xFF1E293B));

    final Color shadowColor = isCoin
        ? const Color(0x35D97706)
        : (isGem ? const Color(0x350284C7) : const Color(0x3010B981));

    Widget content = Container(
      height: 36,
      padding: EdgeInsets.only(
        left: 4,
        right: onAddPressed == null ? 10 : 4,
      ),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(18),
        // 3D drop shadow
        boxShadow: [
          const BoxShadow(
            color: Color(0x220F172A),
            blurRadius: 8,
            offset: Offset(0, 3),
          ),
          BoxShadow(
            color: shadowColor,
            blurRadius: 6,
            offset: const Offset(0, 2),
          ),
          // 3D bottom bevel
          BoxShadow(
            color: rimColorBottom.withAlpha(90),
            blurRadius: 1,
            offset: const Offset(0, 2.2),
          ),
        ],
        // Multi-stop border gradient for physical rim
        gradient: LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [
            rimColorTop,
            rimColorBottom,
          ],
        ),
      ),
      child: Container(
        margin: const EdgeInsets.all(1.4), // Inner cavity
        padding: const EdgeInsets.symmetric(horizontal: 4),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              Colors.white,
              isCoin
                  ? const Color(0xFFFFFBEB)
                  : (isGem ? const Color(0xFFF0F9FF) : const Color(0xFFFEFCE8)),
              isCoin
                  ? const Color(0xFFFEF3C7)
                  : (isGem ? const Color(0xFFE0F2FE) : const Color(0xFFFEF9C3)),
            ],
            stops: const [0.0, 0.6, 1.0],
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Prominent 3D currency badge medallion with aura glow
            Container(
              width: 25,
              height: 25,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: RadialGradient(
                  colors: [
                    badgeGlow.withAlpha(200),
                    badgeGlow.withAlpha(60),
                  ],
                ),
                boxShadow: [
                  BoxShadow(
                    color: badgeGlow.withAlpha(120),
                    blurRadius: 5,
                    spreadRadius: 1,
                  ),
                ],
              ),
              child: Center(
                child: Image.asset(
                  iconAsset,
                  width: 20,
                  height: 20,
                  fit: BoxFit.contain,
                ),
              ),
            ),
            const SizedBox(width: 5),
            // High-contrast, beautifully kerned number
            Text(
              _formatCurrency(value),
              style: TextStyle(
                color: textColor,
                fontSize: 13,
                fontWeight: FontWeight.w900,
                letterSpacing: 0.3,
                shadows: const [
                  Shadow(
                    color: Color(0x30FFFFFF),
                    offset: Offset(0, 1),
                    blurRadius: 1,
                  ),
                ],
              ),
            ),
            // Tactile 3D emerald plus button
            if (onAddPressed != null) ...[
              const SizedBox(width: 5),
              TactileBounce(
                onTap: onAddPressed,
                pressedScale: 0.88,
                child: Container(
                  width: 24,
                  height: 24,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: const LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Color(0xFF4ADE80),
                        Color(0xFF22C55E),
                        Color(0xFF15803D),
                      ],
                      stops: [0.0, 0.5, 1.0],
                    ),
                    border: Border.all(color: Colors.white, width: 1.4),
                    boxShadow: const [
                      BoxShadow(
                        color: Color(0x5015803D),
                        blurRadius: 4,
                        offset: Offset(0, 2),
                      ),
                      BoxShadow(
                        color: Color(0x30000000),
                        blurRadius: 1,
                        offset: Offset(0, 1),
                      ),
                    ],
                  ),
                  child: const Center(
                    child: Icon(
                      Icons.add_rounded,
                      color: Colors.white,
                      size: 16,
                    ),
                  ),
                ),
              ),
            ],
          ],
        ),
      ),
    );

    if (onTap != null && onAddPressed == null) {
      return TactileBounce(
        onTap: onTap,
        pressedScale: 0.94,
        child: content,
      );
    }

    return content;
  }

  static String _formatCurrency(int val) {
    String text;
    if (val >= 1000000) {
      text = '${(val / 1000000).toStringAsFixed(1)}M';
    } else if (val >= 10000) {
      text = '${(val / 1000).toStringAsFixed(1)}K';
    } else {
      text = '$val';
    }
    return formatNumber(text);
  }
}
