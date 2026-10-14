import '../localization/app_language.dart';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';

import '../main.dart';

/// Shows a professional, engaging Rate Us dialog with 5-star interactive rating,
/// dynamic responses, feedback collection for low ratings, and direct Google Play Store redirection.
Future<void> showRateUsDialog(BuildContext context) {
  HapticFeedback.mediumImpact();

  return showGeneralDialog<void>(
    context: context,
    barrierDismissible: true,
    barrierLabel: 'Dismiss Rate Us',
    barrierColor: Colors.black.withAlpha(120),
    transitionDuration: const Duration(milliseconds: 280),
    pageBuilder: (context, anim1, anim2) {
      return const SizedBox.shrink();
    },
    transitionBuilder: (context, anim1, anim2, child) {
      final curved = CurvedAnimation(parent: anim1, curve: Curves.easeOutBack);

      return BackdropFilter(
        filter: ImageFilter.blur(
          sigmaX: 8 * anim1.value,
          sigmaY: 8 * anim1.value,
        ),
        child: ScaleTransition(
          scale: Tween<double>(begin: 0.85, end: 1.0).animate(curved),
          child: FadeTransition(
            opacity: curved,
            child: const Center(
              child: Material(
                type: MaterialType.transparency,
                child: RateUsDialogCard(),
              ),
            ),
          ),
        ),
      );
    },
  );
}

class RateUsDialogCard extends StatefulWidget {
  const RateUsDialogCard({super.key});

  @override
  State<RateUsDialogCard> createState() => _RateUsDialogCardState();
}

class _RateUsDialogCardState extends State<RateUsDialogCard> {
  int _selectedStars = 5;
  final TextEditingController _feedbackController = TextEditingController();
  bool _isSubmitting = false;

  static const String playStorePackage = 'com.mindtrap.ai';
  static const String playStoreMarketUri = 'market://details?id=$playStorePackage';
  static const String playStoreWebUrl =
      'https://play.google.com/store/apps/details?id=$playStorePackage';

  @override
  void dispose() {
    _feedbackController.dispose();
    super.dispose();
  }

  void _onStarTapped(int star) {
    HapticFeedback.selectionClick();
    setState(() {
      _selectedStars = star;
    });
  }

  Future<void> _handlePrimaryAction() async {
    if (_isSubmitting) return;
    setState(() => _isSubmitting = true);

    await GameStorage.recordUserRating(_selectedStars);

    if (!mounted) return;

    if (_selectedStars >= 4) {
      // 4-5 Stars: Launch Play Store review page
      Navigator.of(context).pop();

      try {
        final marketUri = Uri.parse(playStoreMarketUri);
        final webUri = Uri.parse(playStoreWebUrl);

        if (await canLaunchUrl(marketUri)) {
          await launchUrl(marketUri, mode: LaunchMode.externalApplication);
        } else if (await canLaunchUrl(webUri)) {
          await launchUrl(webUri, mode: LaunchMode.externalApplication);
        }
      } catch (e) {
        debugPrint('Could not launch store url: $e');
      }

      if (mounted) {
        showGameNotification(
          context: context,
          message: 'Thank you for your 5-star support! ⭐',
          icon: Icons.star_rounded,
          accentColor: const Color(0xFFF59E0B),
          iconColor: const Color(0xFFFDE68A),
        );
      }
    } else {
      // 1-3 Stars: Save feedback and thank politely
      Navigator.of(context).pop();

      if (mounted) {
        showGameNotification(
          context: context,
          message: 'Thank you for your feedback! We will improve!',
          icon: Icons.check_circle_rounded,
          accentColor: const Color(0xFF0284C7),
          iconColor: const Color(0xFF7DD3FC),
        );
      }
    }
  }

  void _handleRemindLater() {
    HapticFeedback.lightImpact();
    // Do not mark hasRatedApp, so it prompts again after the next 25 levels
    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    final isPositive = _selectedStars >= 4;

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 24),
      constraints: const BoxConstraints(maxWidth: 360),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            Color(0xFFFFFFFF),
            Color(0xFFF8FAFC),
            Color(0xFFF1F5F9),
          ],
        ),
        borderRadius: BorderRadius.circular(28),
        border: Border.all(
          color: Colors.white,
          width: 2.2,
        ),
        boxShadow: [
          BoxShadow(
            color: (isPositive ? const Color(0xFFF59E0B) : const Color(0xFF0284C7))
                .withAlpha(45),
            blurRadius: 36,
            spreadRadius: 2,
            offset: const Offset(0, 12),
          ),
          BoxShadow(
            color: const Color(0xFF0F172A).withAlpha(20),
            blurRadius: 20,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(26),
        child: SingleChildScrollView(
          physics: const BouncingScrollPhysics(),
          child: Padding(
            padding: const EdgeInsets.fromLTRB(22, 20, 22, 22),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // Header Row with Close Button
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const SizedBox(width: 32),
                    // Animated Mascot / Star Badge
                    _buildAnimatedHeaderIcon(isPositive),
                    GestureDetector(
                      onTap: () => Navigator.of(context).pop(),
                      child: Container(
                        width: 32,
                        height: 32,
                        decoration: BoxDecoration(
                          color: const Color(0xFFE2E8F0).withAlpha(160),
                          shape: BoxShape.circle,
                        ),
                        child: const Icon(
                          Icons.close_rounded,
                          size: 18,
                          color: Color(0xFF64748B),
                        ),
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 16),

                // Title
                AnimatedSwitcher(
                  duration: const Duration(milliseconds: 240),
                  child: Text(
                    _titleForStars(_selectedStars),
                    key: ValueKey('title_$_selectedStars'),
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.w900,
                      color: Color(0xFF0F172A),
                      letterSpacing: -0.3,
                    ),
                  ),
                ),

                const SizedBox(height: 8),

                // Subtitle
                AnimatedSwitcher(
                  duration: const Duration(milliseconds: 240),
                  child: Text(
                    _subtitleForStars(_selectedStars),
                    key: ValueKey('sub_$_selectedStars'),
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      fontSize: 13.5,
                      fontWeight: FontWeight.w500,
                      color: Color(0xFF475569),
                      height: 1.35,
                    ),
                  ),
                ),

                const SizedBox(height: 18),

                // 5 Interactive Stars
                _buildStarRatingRow(),

                const SizedBox(height: 16),

                // Optional Feedback Input for <= 3 Stars
                if (!isPositive) ...[
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: const Color(0xFFCBD5E1),
                        width: 1.3,
                      ),
                      boxShadow: const [
                        BoxShadow(
                          color: Color(0x080F172A),
                          blurRadius: 8,
                          offset: Offset(0, 2),
                        ),
                      ],
                    ),
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                    child: TextField(
                      controller: _feedbackController,
                      maxLines: 2,
                      maxLength: 140,
                      style: const TextStyle(
                        fontSize: 13,
                        color: Color(0xFF0F172A),
                        fontWeight: FontWeight.w500,
                      ),
                      decoration: InputDecoration(
                        border: InputBorder.none,
                        counterText: '',
                        hintText: tr('feedback_hint'),
                        hintStyle: TextStyle(
                          color: Color(0xFF94A3B8),
                          fontSize: 12.5,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 14),
                ],

                // Primary Action Button
                SizedBox(
                  width: double.infinity,
                  height: 52,
                  child: ElevatedButton(
                    onPressed: _isSubmitting ? null : _handlePrimaryAction,
                    style: ElevatedButton.styleFrom(
                      padding: EdgeInsets.zero,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(18),
                      ),
                      elevation: 6,
                      shadowColor: (isPositive
                              ? const Color(0xFFF59E0B)
                              : const Color(0xFF0284C7))
                          .withAlpha(90),
                    ),
                    child: Ink(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: isPositive
                              ? const [
                                  Color(0xFFF59E0B),
                                  Color(0xFFEA580C),
                                ]
                              : const [
                                  Color(0xFF0284C7),
                                  Color(0xFF0369A1),
                                ],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        borderRadius: BorderRadius.circular(18),
                      ),
                      child: Container(
                        alignment: Alignment.center,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              isPositive
                                  ? Icons.star_rounded
                                  : Icons.send_rounded,
                              color: Colors.white,
                              size: 20,
                            ),
                            const SizedBox(width: 8),
                            Text(
                              isPositive
                                  ? tr('rate_google_play')
                                  : tr('submit_feedback'),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 15.5,
                                fontWeight: FontWeight.w800,
                                letterSpacing: 0.3,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),

                const SizedBox(height: 10),

                // Remind Me Later Button
                TextButton(
                  onPressed: _handleRemindLater,
                  style: TextButton.styleFrom(
                    foregroundColor: const Color(0xFF64748B),
                    padding: const EdgeInsets.symmetric(
                      horizontal: 16,
                      vertical: 6,
                    ),
                  ),
                  child: Text(
                    tr('remind_me_later'),
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w700,
                      color: Color(0xFF64748B),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildAnimatedHeaderIcon(bool isPositive) {
    return Container(
      width: 72,
      height: 72,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: isPositive
              ? const [
                  Color(0xFFFEF3C7),
                  Color(0xFFFDE68A),
                ]
              : const [
                  Color(0xFFE0F2FE),
                  Color(0xFFBAE6FD),
                ],
        ),
        boxShadow: [
          BoxShadow(
            color: (isPositive
                    ? const Color(0xFFF59E0B)
                    : const Color(0xFF0284C7))
                .withAlpha(50),
            blurRadius: 18,
            offset: const Offset(0, 6),
          ),
        ],
        border: Border.all(
          color: Colors.white,
          width: 2.5,
        ),
      ),
      child: Center(
        child: Icon(
          isPositive ? Icons.star_rounded : Icons.thumb_up_alt_rounded,
          size: 40,
          color: isPositive ? const Color(0xFFF59E0B) : const Color(0xFF0284C7),
        ),
      ),
    );
  }

  Widget _buildStarRatingRow() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: List.generate(5, (index) {
        final starNumber = index + 1;
        final isSelected = starNumber <= _selectedStars;

        return GestureDetector(
          onTap: () => _onStarTapped(starNumber),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4),
            child: TweenAnimationBuilder<double>(
              tween: Tween<double>(
                begin: isSelected ? 0.8 : 1.0,
                end: isSelected ? 1.08 : 1.0,
              ),
              duration: const Duration(milliseconds: 200),
              curve: Curves.easeOutBack,
              builder: (context, scale, child) {
                return Transform.scale(
                  scale: scale,
                  child: Icon(
                    isSelected ? Icons.star_rounded : Icons.star_outline_rounded,
                    size: 38,
                    color: isSelected
                        ? const Color(0xFFF59E0B)
                        : const Color(0xFFCBD5E1),
                    shadows: isSelected
                        ? [
                            BoxShadow(
                              color: const Color(0xFFF59E0B).withAlpha(100),
                              blurRadius: 10,
                              offset: const Offset(0, 2),
                            ),
                          ]
                        : null,
                  ),
                );
              },
            ),
          ),
        );
      }),
    );
  }

  String _titleForStars(int stars) {
    switch (stars) {
      case 5:
        return tr('rate_title_5');
      case 4:
        return tr('rate_title_4');
      case 3:
        return tr('rate_title_3');
      case 2:
      case 1:
        return tr('rate_title_1_2');
      default:
        return tr('rate_us');
    }
  }

  String _subtitleForStars(int stars) {
    switch (stars) {
      case 5:
        return tr('rate_sub_5');
      case 4:
        return tr('rate_sub_4');
      case 3:
        return tr('rate_sub_3');
      case 2:
      case 1:
        return tr('rate_sub_1_2');
      default:
        return tr('rate_us_subtitle');
    }
  }
}
