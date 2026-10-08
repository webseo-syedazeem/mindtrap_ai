import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../services/audio_service.dart';

class MapYourMindScreen extends StatefulWidget {
  const MapYourMindScreen({
    super.key,
    this.initialAge,
    this.initialGender,
    this.initialIq,
    this.initialGoal,
    this.onCompleted,
    this.onContinueToLevels,
  });

  final String? initialAge;
  final String? initialGender;
  final String? initialIq;
  final String? initialGoal;
  final Future<void> Function(String age, String gender, String iq, String goal)? onCompleted;
  final Future<void> Function()? onContinueToLevels;

  @override
  State<MapYourMindScreen> createState() => _MapYourMindScreenState();
}

class _MapYourMindScreenState extends State<MapYourMindScreen> {
  static const int _totalSteps = 4;

  late String _selectedAge;
  late String _selectedGender;
  late String _selectedIq;
  late String _selectedGoal;
  bool _isSaving = false;

  /// Current wizard step (1 = About You, 2 = Goals, 3 = Preferences, 4 = All Set).
  int _activeStep = 1;

  /// Direction of the last navigation, used for the slide animation.
  bool _movingForward = true;

  final List<String> _ageOptions = const [
    'Under 13',
    '13 – 17',
    '18 – 24',
    '25 – 34',
    '35 – 44',
    '45+',
  ];

  final List<String> _genderOptions = const [
    'Male',
    'Female',
    'Prefer not to say',
  ];

  final List<String> _iqOptions = const [
    'Not sure',
    'Below 90',
    '90 – 110',
    '110 – 130',
    'Above 130',
  ];

  final List<Map<String, dynamic>> _goalOptions = const [
    {
      'id': 'Improve Focus',
      'title': 'Improve Focus',
      'subtitle': 'Better concentration',
      'icon': Icons.center_focus_strong_rounded,
      'color': Color(0xFF38BDF8),
    },
    {
      'id': 'Boost IQ',
      'title': 'Boost IQ',
      'subtitle': 'Higher cognitive skills',
      'icon': Icons.trending_up_rounded,
      'color': Color(0xFFA855F7),
    },
    {
      'id': 'Sharpen Memory',
      'title': 'Sharpen Memory',
      'subtitle': 'Remember better',
      'icon': Icons.lightbulb_rounded,
      'color': Color(0xFFFBBF24),
    },
    {
      'id': 'Solve Problems',
      'title': 'Solve Problems',
      'subtitle': 'Think more logically',
      'icon': Icons.extension_rounded,
      'color': Color(0xFFF43F5E),
    },
  ];

  @override
  void initState() {
    super.initState();
    _selectedAge = widget.initialAge ?? '25 – 34';
    _selectedGender = widget.initialGender ?? 'Female';
    _selectedIq = widget.initialIq ?? '90 – 110';
    _selectedGoal = widget.initialGoal ?? 'Improve Focus';
  }

  // ---------------------------------------------------------------------------
  // Navigation
  // ---------------------------------------------------------------------------

  void _goToStep(int step) {
    if (step < 1 || step > _totalSteps || step == _activeStep) return;
    AudioService.instance.playClick();
    unawaited(HapticFeedback.lightImpact());
    setState(() {
      _movingForward = step > _activeStep;
      _activeStep = step;
    });
  }

  void _nextStep() {
    if (_activeStep < _totalSteps) {
      _goToStep(_activeStep + 1);
    } else {
      _handleDone();
    }
  }

  void _previousStep() {
    if (_activeStep > 1) {
      _goToStep(_activeStep - 1);
    } else {
      AudioService.instance.playClick();
      Navigator.of(context).pop();
    }
  }

  Future<void> _handleDone() async {
    if (_isSaving) return;
    setState(() => _isSaving = true);

    AudioService.instance.playClick();
    unawaited(HapticFeedback.mediumImpact());

    try {
      if (widget.onCompleted != null) {
        await widget.onCompleted!(
          _selectedAge,
          _selectedGender,
          _selectedIq,
          _selectedGoal,
        );
      }

      if (!mounted) return;

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          behavior: SnackBarBehavior.floating,
          backgroundColor: const Color(0xFF1E293B),
          elevation: 8,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
            side: const BorderSide(color: Color(0xFF38BDF8), width: 1.2),
          ),
          content: Row(
            children: [
              const Icon(Icons.check_circle_rounded, color: Color(0xFF38BDF8), size: 24),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  tr('mind_mapped_success'),
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.w600,
                    fontSize: 13,
                  ),
                ),
              ),
            ],
          ),
          duration: const Duration(seconds: 2),
        ),
      );

      await Future<void>.delayed(const Duration(milliseconds: 300));
      if (!mounted) return;

      if (widget.onContinueToLevels != null) {
        await widget.onContinueToLevels!();
      } else {
        Navigator.of(context).pop();
      }
    } finally {
      if (mounted) {
        setState(() => _isSaving = false);
      }
    }
  }

  // ---------------------------------------------------------------------------
  // Build
  // ---------------------------------------------------------------------------

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, activeLang, _) {
        return PopScope(
          canPop: _activeStep == 1,
          onPopInvokedWithResult: (didPop, _) {
            // Android back button walks back through the steps first.
            if (!didPop) _previousStep();
          },
          child: Scaffold(
            body: Stack(
              children: [
                // Background scenic image
                const Positioned.fill(
                  child: Image(
                    image: AssetImage('assets/images/home_background.webp'),
                    fit: BoxFit.cover,
                    alignment: Alignment.topCenter,
                  ),
                ),
                // Soft ambient vignette for contrast & clarity
                Positioned.fill(
                  child: DecoratedBox(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.white.withValues(alpha: 0.12),
                          Colors.transparent,
                          Colors.white.withValues(alpha: 0.22),
                        ],
                      ),
                    ),
                  ),
                ),
                SafeArea(
                  bottom: false,
                  child: Column(
                    children: [
                      _buildTopBar(),
                      _buildHeader(),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        child: _buildStepperRow(),
                      ),
                      const SizedBox(height: 18),
                      // Step content
                      Expanded(
                        child: AnimatedSwitcher(
                          duration: const Duration(milliseconds: 320),
                          switchInCurve: Curves.easeOutCubic,
                          switchOutCurve: Curves.easeInCubic,
                          transitionBuilder: (child, animation) {
                            final isIncoming = child.key == ValueKey<int>(_activeStep);
                            final dx = (_movingForward == isIncoming) ? 0.25 : -0.25;
                            return FadeTransition(
                              opacity: animation,
                              child: SlideTransition(
                                position: Tween<Offset>(
                                  begin: Offset(dx, 0),
                                  end: Offset.zero,
                                ).animate(animation),
                                child: child,
                              ),
                            );
                          },
                          child: SingleChildScrollView(
                            key: ValueKey<int>(_activeStep),
                            physics: const BouncingScrollPhysics(),
                            padding: const EdgeInsets.fromLTRB(20, 0, 20, 16),
                            child: _buildStepContent(),
                          ),
                        ),
                      ),
                      // Bottom navigation (Back / Next / Done)
                      Padding(
                        padding: EdgeInsets.fromLTRB(20, 4, 20, max(16.0, safePadding.bottom + 8)),
                        child: _buildBottomNav(),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildTopBar() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 8),
      child: Row(
        children: [
          GestureDetector(
            onTap: _previousStep,
            child: Container(
              width: 38,
              height: 38,
              decoration: const BoxDecoration(
                color: Colors.white,
                shape: BoxShape.circle,
                boxShadow: [
                  BoxShadow(
                    color: Color(0x332178BA),
                    blurRadius: 6,
                    offset: Offset(0, 2),
                  ),
                ],
              ),
              child: Icon(
                (Directionality.of(context) == TextDirection.rtl)
                    ? Icons.arrow_forward_rounded
                    : Icons.arrow_back_rounded,
                size: 24,
                color: const Color(0xFF244169),
              ),
            ),
          ),
          const Spacer(),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.white.withValues(alpha: 0.9),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Text(
              '${tr('step')} ${formatNumber(_activeStep)} ${tr('of')} ${formatNumber(_totalSteps)}',
              style: const TextStyle(
                color: Color(0xFF2563EB),
                fontSize: 12,
                fontWeight: FontWeight.w800,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHeader() {
    return Column(
      children: [
        Stack(
          alignment: Alignment.center,
          clipBehavior: Clip.none,
          children: [
            Container(
              width: 70,
              height: 70,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                boxShadow: [
                  BoxShadow(
                    color: const Color(0xFFFBBF24).withValues(alpha: 0.4),
                    blurRadius: 28,
                    spreadRadius: 6,
                  ),
                ],
              ),
            ),
            const Image(
              image: AssetImage('assets/images/home_logo.webp'),
              width: 76,
              height: 60,
              fit: BoxFit.contain,
            ),
            const Positioned(
              top: 0,
              right: -6,
              child: Icon(Icons.auto_awesome, size: 16, color: Color(0xFFFDE047)),
            ),
          ],
        ),
        const SizedBox(height: 6),
        const Text(
          'MindTrap AI',
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.w900,
            letterSpacing: 0.2,
            color: Color(0xFF1E293B),
          ),
        ),
        const SizedBox(height: 2),
        Text(
          tr('map_your_mind_title'),
          textAlign: TextAlign.center,
          style: const TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.w600,
            color: Color(0xFF64748B),
          ),
        ),
        const SizedBox(height: 14),
      ],
    );
  }

  Widget _buildStepContent() {
    switch (_activeStep) {
      case 1:
        return _buildAboutYouStep();
      case 2:
        return _buildGoalsStep();
      case 3:
        return _buildPreferencesStep();
      default:
        return _buildAllSetStep();
    }
  }

  // ---------------------------------------------------------------------------
  // Step 1: About You (Age + Gender)
  // ---------------------------------------------------------------------------

  Widget _buildAboutYouStep() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        _buildSectionCard(
          icon: Icons.calendar_month_rounded,
          iconBgColor: const Color(0xFF2563EB),
          title: tr('your_age'),
          subtitle: tr('your_age_sub'),
          child: Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _ageOptions.map((age) {
              final label = age == 'Under 13' ? tr('under_13') : age;
              return _buildChip(
                label: label,
                isSelected: _selectedAge == age,
                selectedGradient: const [Color(0xFF38BDF8), Color(0xFF2563EB)],
                glowColor: const Color(0xFF38BDF8),
                onTap: () {
                  AudioService.instance.playClick();
                  setState(() => _selectedAge = age);
                },
              );
            }).toList(),
          ),
        ),
        const SizedBox(height: 14),
        _buildSectionCard(
          icon: Icons.person_rounded,
          iconBgColor: const Color(0xFF8B5CF6),
          title: tr('gender'),
          subtitle: tr('gender_sub'),
          child: Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _genderOptions.map((gender) {
              String label = gender;
              if (gender == 'Male') label = '♂ ${tr('male')}';
              if (gender == 'Female') label = '♀ ${tr('female')}';
              if (gender == 'Prefer not to say') label = '⊝ ${tr('prefer_not_to_say')}';

              final List<Color> gradient;
              final Color glow;
              if (gender == 'Male') {
                gradient = const [Color(0xFF38BDF8), Color(0xFF0284C7)];
                glow = const Color(0xFF38BDF8);
              } else if (gender == 'Female') {
                gradient = const [Color(0xFFA855F7), Color(0xFF7C3AED)];
                glow = const Color(0xFFA855F7);
              } else {
                gradient = const [Color(0xFF6366F1), Color(0xFF4338CA)];
                glow = const Color(0xFF6366F1);
              }

              return _buildChip(
                label: label,
                isSelected: _selectedGender == gender,
                selectedGradient: gradient,
                glowColor: glow,
                onTap: () {
                  AudioService.instance.playClick();
                  setState(() => _selectedGender = gender);
                },
              );
            }).toList(),
          ),
        ),
      ],
    );
  }

  // ---------------------------------------------------------------------------
  // Step 2: Goals
  // ---------------------------------------------------------------------------

  Widget _buildGoalsStep() {
    return _buildSectionCard(
      icon: Icons.track_changes_rounded,
      iconBgColor: const Color(0xFFF97316),
      title: tr('your_goal'),
      subtitle: tr('your_goal_sub'),
      child: LayoutBuilder(
        builder: (context, box) {
          final itemWidth = (box.maxWidth - 10) / 2;
          return Wrap(
            spacing: 10,
            runSpacing: 10,
            children: _goalOptions.map((g) {
              final id = g['id'] as String;
              final localizedTitle = id == 'Improve Focus'
                  ? tr('improve_focus')
                  : id == 'Boost IQ'
                      ? tr('boost_iq')
                      : id == 'Sharpen Memory'
                          ? tr('sharpen_memory')
                          : tr('solve_problems');
              final localizedSubtitle = id == 'Improve Focus'
                  ? tr('better_concentration')
                  : id == 'Boost IQ'
                      ? tr('higher_cognitive')
                      : id == 'Sharpen Memory'
                          ? tr('remember_better')
                          : tr('think_logically');
              return GestureDetector(
                onTap: () {
                  AudioService.instance.playClick();
                  setState(() => _selectedGoal = id);
                },
                child: SizedBox(
                  width: itemWidth,
                  child: _buildGoalCard(
                    title: localizedTitle,
                    subtitle: localizedSubtitle,
                    icon: g['icon'] as IconData,
                    iconColor: g['color'] as Color,
                    isSelected: _selectedGoal == id,
                  ),
                ),
              );
            }).toList(),
          );
        },
      ),
    );
  }

  // ---------------------------------------------------------------------------
  // Step 3: Preferences (IQ level)
  // ---------------------------------------------------------------------------

  Widget _buildPreferencesStep() {
    return _buildSectionCard(
      icon: Icons.psychology_outlined,
      iconBgColor: const Color(0xFF10B981),
      title: tr('current_iq_level'),
      subtitle: tr('iq_sub'),
      child: Wrap(
        spacing: 8,
        runSpacing: 8,
        children: _iqOptions.map((iq) {
          final label = iq == 'Not sure'
              ? tr('not_sure')
              : iq == 'Below 90'
                  ? tr('below_90')
                  : iq == 'Above 130'
                      ? tr('above_130')
                      : iq;
          return _buildChip(
            label: label,
            isSelected: _selectedIq == iq,
            selectedGradient: const [Color(0xFF34D399), Color(0xFF059669)],
            glowColor: const Color(0xFF34D399),
            onTap: () {
              AudioService.instance.playClick();
              setState(() => _selectedIq = iq);
            },
          );
        }).toList(),
      ),
    );
  }

  // ---------------------------------------------------------------------------
  // Step 4: All Set (summary)
  // ---------------------------------------------------------------------------

  Widget _buildAllSetStep() {
    final goal = _goalOptions.firstWhere(
      (g) => g['id'] == _selectedGoal,
      orElse: () => _goalOptions.first,
    );

    final localizedGoal = _selectedGoal == 'Improve Focus'
        ? tr('improve_focus')
        : _selectedGoal == 'Boost IQ'
            ? tr('boost_iq')
            : _selectedGoal == 'Sharpen Memory'
                ? tr('sharpen_memory')
                : tr('solve_problems');

    final localizedGender = _selectedGender == 'Male'
        ? tr('male')
        : _selectedGender == 'Female'
            ? tr('female')
            : tr('prefer_not_to_say');

    final localizedIq = _selectedIq == 'Not sure'
        ? tr('not_sure')
        : _selectedIq == 'Below 90'
            ? tr('below_90')
            : _selectedIq == 'Above 130'
                ? tr('above_130')
                : _selectedIq;

    final localizedAge = _selectedAge == 'Under 13' ? tr('under_13') : _selectedAge;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Container(
          padding: const EdgeInsets.all(18),
          decoration: BoxDecoration(
            color: Colors.white.withValues(alpha: 0.95),
            borderRadius: BorderRadius.circular(22),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF0F172A).withValues(alpha: 0.08),
                blurRadius: 18,
                offset: const Offset(0, 6),
              ),
            ],
          ),
          child: Column(
            children: [
              Container(
                width: 64,
                height: 64,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: const LinearGradient(
                    colors: [Color(0xFF34D399), Color(0xFF059669)],
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF10B981).withValues(alpha: 0.4),
                      blurRadius: 16,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: const Icon(Icons.check_rounded, color: Colors.white, size: 36),
              ),
              const SizedBox(height: 12),
              Text(
                tr('you_are_all_set'),
                style: const TextStyle(
                  color: Color(0xFF0F172A),
                  fontSize: 20,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 4),
              Text(
                tr('plan_ready'),
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF64748B),
                  fontSize: 13,
                  fontWeight: FontWeight.w500,
                ),
              ),
              const SizedBox(height: 16),
              _buildSummaryRow(
                icon: Icons.calendar_month_rounded,
                color: const Color(0xFF2563EB),
                label: tr('age'),
                value: localizedAge,
                editStep: 1,
              ),
              _buildSummaryRow(
                icon: Icons.person_rounded,
                color: const Color(0xFF8B5CF6),
                label: tr('gender'),
                value: localizedGender,
                editStep: 1,
              ),
              _buildSummaryRow(
                icon: goal['icon'] as IconData,
                color: const Color(0xFFF97316),
                label: tr('goal'),
                value: localizedGoal,
                editStep: 2,
              ),
              _buildSummaryRow(
                icon: Icons.psychology_outlined,
                color: const Color(0xFF10B981),
                label: tr('iq_level'),
                value: localizedIq,
                editStep: 3,
                showDivider: false,
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildSummaryRow({
    required IconData icon,
    required Color color,
    required String label,
    required String value,
    required int editStep,
    bool showDivider = true,
  }) {
    return InkWell(
      onTap: () => _goToStep(editStep),
      borderRadius: BorderRadius.circular(12),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 4),
        decoration: BoxDecoration(
          border: showDivider
              ? const Border(bottom: BorderSide(color: Color(0xFFE2E8F0)))
              : null,
        ),
        child: Row(
          children: [
            Container(
              width: 34,
              height: 34,
              decoration: BoxDecoration(
                color: color.withValues(alpha: 0.12),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, color: color, size: 18),
            ),
            const SizedBox(width: 12),
            Text(
              label,
              style: const TextStyle(
                color: Color(0xFF64748B),
                fontSize: 13,
                fontWeight: FontWeight.w600,
              ),
            ),
            const Spacer(),
            Text(
              value,
              style: const TextStyle(
                color: Color(0xFF0F172A),
                fontSize: 14,
                fontWeight: FontWeight.w800,
              ),
            ),
            const SizedBox(width: 6),
            const Icon(Icons.edit_rounded, size: 14, color: Color(0xFF94A3B8)),
          ],
        ),
      ),
    );
  }

  // ---------------------------------------------------------------------------
  // Bottom navigation
  // ---------------------------------------------------------------------------

  Widget _buildBottomNav() {
    final isLast = _activeStep == _totalSteps;

    return Row(
      children: [
        if (_activeStep > 1) ...[
          GestureDetector(
            onTap: _isSaving ? null : _previousStep,
            child: Container(
              height: 54,
              padding: const EdgeInsets.symmetric(horizontal: 20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(27),
                border: Border.all(color: const Color(0xFFBFDBFE), width: 1.5),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0xFF0F172A).withValues(alpha: 0.08),
                    blurRadius: 10,
                    offset: const Offset(0, 3),
                  ),
                ],
              ),
              alignment: Alignment.center,
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.arrow_back_rounded, color: Color(0xFF2563EB), size: 24),
                  const SizedBox(width: 6),
                  Text(
                    tr('back'),
                    style: const TextStyle(
                      color: Color(0xFF2563EB),
                      fontSize: 15,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(width: 12),
        ],
        Expanded(
          child: GestureDetector(
            onTap: _isSaving ? null : _nextStep,
            child: Container(
              height: 54,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(27),
                gradient: LinearGradient(
                  colors: isLast
                      ? const [Color(0xFF34D399), Color(0xFF10B981), Color(0xFF059669)]
                      : const [Color(0xFF38BDF8), Color(0xFF2563EB), Color(0xFF1D4ED8)],
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                ),
                border: Border.all(
                  color: Colors.white.withValues(alpha: 0.85),
                  width: 2,
                ),
                boxShadow: [
                  BoxShadow(
                    color: (isLast ? const Color(0xFF059669) : const Color(0xFF2563EB))
                        .withValues(alpha: 0.5),
                    blurRadius: 16,
                    offset: const Offset(0, 5),
                  ),
                ],
              ),
              alignment: Alignment.center,
              child: _isSaving
                  ? const SizedBox(
                      width: 22,
                      height: 22,
                      child: CircularProgressIndicator(
                        strokeWidth: 2.5,
                        valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                      ),
                    )
                  : Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          isLast ? tr('done') : tr('next'),
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.5,
                          ),
                        ),
                        const SizedBox(width: 8),
                        Icon(
                          isLast ? Icons.check_circle_rounded : Icons.arrow_forward_rounded,
                          color: Colors.white,
                          size: 20,
                        ),
                      ],
                    ),
            ),
          ),
        ),
      ],
    );
  }

  // ---------------------------------------------------------------------------
  // Stepper
  // ---------------------------------------------------------------------------

  Widget _buildStepperRow() {
    const steps = ['About You', 'Goals', 'Preferences', 'All Set'];

    return Row(
      children: List.generate(steps.length * 2 - 1, (index) {
        if (index.isOdd) {
          final leftStepNum = (index ~/ 2) + 1;
          final isLinePassed = _activeStep > leftStepNum;
          return Expanded(
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 250),
              height: 2.5,
              margin: const EdgeInsets.only(bottom: 18),
              color: isLinePassed ? const Color(0xFF38BDF8) : const Color(0xFFCBD5E1),
            ),
          );
        }

        final stepNum = (index ~/ 2) + 1;
        final isActive = _activeStep == stepNum;
        final isCompleted = _activeStep > stepNum;
        final highlighted = isActive || isCompleted;

        return GestureDetector(
          // Only allow jumping back to already visited steps.
          onTap: stepNum <= _activeStep ? () => _goToStep(stepNum) : null,
          behavior: HitTestBehavior.opaque,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                width: isActive ? 34 : 30,
                height: isActive ? 34 : 30,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: highlighted
                      ? const LinearGradient(
                          colors: [Color(0xFF38BDF8), Color(0xFF2563EB)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        )
                      : null,
                  color: highlighted ? null : const Color(0xFFE2E8F0),
                  border: isActive ? Border.all(color: Colors.white, width: 2) : null,
                  boxShadow: highlighted
                      ? [
                          BoxShadow(
                            color: const Color(0xFF2563EB).withValues(alpha: 0.35),
                            blurRadius: 8,
                            offset: const Offset(0, 2),
                          ),
                        ]
                      : null,
                ),
                alignment: Alignment.center,
                child: isCompleted
                    ? const Icon(Icons.check_rounded, color: Colors.white, size: 16)
                    : Text(
                        '$stepNum',
                        style: TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.bold,
                          color: isActive ? Colors.white : const Color(0xFF64748B),
                        ),
                      ),
              ),
              const SizedBox(height: 6),
              Text(
                steps[stepNum - 1],
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: highlighted ? FontWeight.w700 : FontWeight.w600,
                  color: highlighted ? const Color(0xFF2563EB) : const Color(0xFF64748B),
                ),
              ),
            ],
          ),
        );
      }),
    );
  }

  // ---------------------------------------------------------------------------
  // Shared UI helpers
  // ---------------------------------------------------------------------------

  Widget _buildSectionCard({
    required IconData icon,
    required Color iconBgColor,
    required String title,
    String? subtitle,
    required Widget child,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white.withValues(alpha: 0.95),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF0F172A).withValues(alpha: 0.08),
            blurRadius: 18,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 38,
                height: 38,
                decoration: BoxDecoration(
                  color: iconBgColor,
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: [
                    BoxShadow(
                      color: iconBgColor.withValues(alpha: 0.35),
                      blurRadius: 8,
                      offset: const Offset(0, 3),
                    ),
                  ],
                ),
                child: Icon(icon, color: Colors.white, size: 20),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(
                        color: Color(0xFF0F172A),
                        fontSize: 16,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
                    if (subtitle != null) ...[
                      const SizedBox(height: 2),
                      Text(
                        subtitle,
                        style: const TextStyle(
                          color: Color(0xFF64748B),
                          fontSize: 12,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          child,
        ],
      ),
    );
  }

  Widget _buildChip({
    required String label,
    required bool isSelected,
    required List<Color> selectedGradient,
    required Color glowColor,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(22),
          gradient: isSelected
              ? LinearGradient(
                  colors: selectedGradient,
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                )
              : null,
          color: isSelected ? null : const Color(0xFFF1F5F9),
          border: Border.all(
            color: isSelected ? Colors.white.withValues(alpha: 0.6) : const Color(0xFFE2E8F0),
            width: isSelected ? 1.4 : 1.0,
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: glowColor.withValues(alpha: 0.4),
                    blurRadius: 10,
                    offset: const Offset(0, 3),
                  ),
                ]
              : null,
        ),
        child: Text(
          label,
          style: TextStyle(
            color: isSelected ? Colors.white : const Color(0xFF334155),
            fontSize: 13,
            fontWeight: isSelected ? FontWeight.w700 : FontWeight.w600,
          ),
        ),
      ),
    );
  }

  Widget _buildGoalCard({
    required String title,
    required String subtitle,
    required IconData icon,
    required Color iconColor,
    required bool isSelected,
  }) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 180),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(16),
        color: isSelected ? const Color(0xFFEFF6FF) : const Color(0xFFF8FAFC),
        border: Border.all(
          color: isSelected ? const Color(0xFF2563EB) : const Color(0xFFE2E8F0),
          width: isSelected ? 1.8 : 1.0,
        ),
        boxShadow: isSelected
            ? [
                BoxShadow(
                  color: const Color(0xFF2563EB).withValues(alpha: 0.25),
                  blurRadius: 10,
                  offset: const Offset(0, 3),
                ),
              ]
            : null,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  color: iconColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: iconColor, size: 20),
              ),
              if (isSelected)
                Container(
                  width: 22,
                  height: 22,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Color(0xFF2563EB),
                  ),
                  child: const Icon(Icons.check_rounded, size: 14, color: Colors.white),
                )
              else
                const SizedBox(width: 22, height: 22),
            ],
          ),
          const SizedBox(height: 8),
          Text(
            title,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(
              color: Color(0xFF0F172A),
              fontWeight: FontWeight.w800,
              fontSize: 13,
            ),
          ),
          const SizedBox(height: 2),
          Text(
            subtitle,
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
              color: isSelected ? const Color(0xFF2563EB) : const Color(0xFF64748B),
              fontSize: 11,
              fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }
}
