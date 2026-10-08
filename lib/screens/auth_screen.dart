import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../main.dart';
import '../services/auth_service.dart';
import 'language_selection_screen.dart';

class AuthScreen extends StatefulWidget {
  final VoidCallback? onAuthSuccess;

  const AuthScreen({super.key, this.onAuthSuccess});

  @override
  State<AuthScreen> createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final _signInFormKey = GlobalKey<FormState>();
  final _signUpFormKey = GlobalKey<FormState>();

  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _confirmPasswordController =
      TextEditingController();
  final TextEditingController _forgotEmailController = TextEditingController();

  final FocusNode _emailFocus = FocusNode();
  final FocusNode _passwordFocus = FocusNode();
  final FocusNode _nameFocus = FocusNode();
  final FocusNode _signUpEmailFocus = FocusNode();
  final FocusNode _signUpPasswordFocus = FocusNode();
  final FocusNode _confirmPasswordFocus = FocusNode();

  bool _obscurePassword = true;
  bool _obscureSignUpPassword = true;
  bool _obscureConfirmPassword = true;
  bool _rememberMe = true;
  bool _agreeToTerms = false;
  bool _isLoading = false;
  bool _isSocialLoading = false;
  String? _errorMessage;

  // Dynamic Password Strength
  int _passwordScore = 0; // 0 to 4
  bool _hasMinLength = false;
  bool _hasNumber = false;
  bool _hasSpecialOrUpper = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(_handleTabChange);
    _passwordController.addListener(_evaluatePasswordStrength);
    _emailController.addListener(() => setState(() {}));
    _nameController.addListener(() => setState(() {}));
    _confirmPasswordController.addListener(() => setState(() {}));

    _loadRememberedCredentials();
  }

  void _handleTabChange() {
    if (_tabController.indexIsChanging) {
      setState(() {
        _errorMessage = null;
      });
      FocusScope.of(context).unfocus();
    }
  }

  Future<void> _loadRememberedCredentials() async {
    final remember = await AuthService.instance.getRememberMe();
    final savedEmail = await AuthService.instance.getRememberedEmail();
    if (mounted) {
      setState(() {
        _rememberMe = remember;
        if (remember && savedEmail.isNotEmpty) {
          _emailController.text = savedEmail;
        }
      });
    }
  }

  void _evaluatePasswordStrength() {
    final text = _passwordController.text;
    int score = 0;
    final minLen = text.length >= 8;
    final num = RegExp(r'[0-9]').hasMatch(text);
    final upperOrSpecial = RegExp(r'[A-Z]').hasMatch(text) ||
        RegExp(r'[!@#\$%^&*(),.?":{}|<>]').hasMatch(text);

    if (text.isNotEmpty) {
      if (text.length >= 6) score++;
      if (minLen) score++;
      if (num) score++;
      if (upperOrSpecial) score++;
    }

    if (mounted) {
      setState(() {
        _passwordScore = score;
        _hasMinLength = minLen;
        _hasNumber = num;
        _hasSpecialOrUpper = upperOrSpecial;
      });
    }
  }

  @override
  void dispose() {
    _tabController.removeListener(_handleTabChange);
    _tabController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    _nameController.dispose();
    _confirmPasswordController.dispose();
    _forgotEmailController.dispose();
    _emailFocus.dispose();
    _passwordFocus.dispose();
    _nameFocus.dispose();
    _signUpEmailFocus.dispose();
    _signUpPasswordFocus.dispose();
    _confirmPasswordFocus.dispose();
    super.dispose();
  }

  Future<void> _submitSignIn() async {
    if (!_signInFormKey.currentState!.validate()) return;
    HapticFeedback.lightImpact();

    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    final email = _emailController.text.trim();
    final password = _passwordController.text;

    final result = await AuthService.instance.signIn(
      email: email,
      password: password,
    );

    if (!mounted) return;

    if (result['success'] == true) {
      await AuthService.instance.setRememberMe(_rememberMe, email);
      _handleAuthSuccess(result['message'] as String? ?? tr('auth_success'));
    } else {
      setState(() {
        _isLoading = false;
        _errorMessage = result['message'] as String? ?? tr('auth_error');
      });
      HapticFeedback.mediumImpact();
    }
  }

  Future<void> _submitSignUp() async {
    if (!_signUpFormKey.currentState!.validate()) return;

    if (!_agreeToTerms) {
      HapticFeedback.heavyImpact();
      setState(() {
        _errorMessage = tr('accept_terms_error');
      });
      return;
    }

    HapticFeedback.lightImpact();

    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    final email = _emailController.text.trim();
    final password = _passwordController.text;
    final name = _nameController.text.trim();

    final result = await AuthService.instance.signUp(
      email: email,
      password: password,
      name: name,
    );

    if (!mounted) return;

    if (result['success'] == true) {
      await AuthService.instance.setRememberMe(_rememberMe, email);
      _handleAuthSuccess(result['message'] as String? ?? tr('auth_success'));
    } else {
      setState(() {
        _isLoading = false;
        _errorMessage = result['message'] as String? ?? tr('auth_error');
      });
      HapticFeedback.mediumImpact();
    }
  }

  Future<void> _signInWithGoogle() async {
    HapticFeedback.selectionClick();
    setState(() {
      _isSocialLoading = true;
      _errorMessage = null;
    });

    final res = await AuthService.instance.signInWithGoogle();

    if (!mounted) return;
    setState(() => _isSocialLoading = false);

    if (res['success'] == true) {
      _handleAuthSuccess(res['message'] as String? ?? 'Signed in with Google!');
    } else {
      setState(() => _errorMessage = res['message'] as String? ?? 'Google Sign-in failed');
    }
  }

  Future<void> _signInWithApple() async {
    HapticFeedback.selectionClick();
    setState(() {
      _isSocialLoading = true;
      _errorMessage = null;
    });

    final res = await AuthService.instance.signInWithApple();

    if (!mounted) return;
    setState(() => _isSocialLoading = false);

    if (res['success'] == true) {
      _handleAuthSuccess(res['message'] as String? ?? 'Signed in with Apple!');
    } else {
      setState(() => _errorMessage = res['message'] as String? ?? 'Apple Sign-in failed');
    }
  }

  Future<void> _continueAsGuest() async {
    HapticFeedback.selectionClick();
    setState(() => _isLoading = true);
    await AuthService.instance.continueAsGuest();
    if (!mounted) return;
    setState(() => _isLoading = false);
    _handleAuthSuccess('Welcome, Guest Mind! Play & explore.');
  }

  void _handleAuthSuccess(String message) {
    setState(() => _isLoading = false);
    _showFeedbackSnackBar(
      message: message,
      isSuccess: true,
      icon: Icons.check_circle_rounded,
    );

    if (widget.onAuthSuccess != null) {
      widget.onAuthSuccess!();
    } else {
      Navigator.of(context).pop();
    }
  }

  void _showFeedbackSnackBar({
    required String message,
    required bool isSuccess,
    required IconData icon,
  }) {
    showGameNotification(
      context: context,
      message: message,
      icon: icon,
      accentColor: isSuccess ? const Color(0xFF10B981) : const Color(0xFFEF4444),
      iconColor: isSuccess ? const Color(0xFF34D399) : const Color(0xFFF87171),
    );
  }

  void _showForgotPasswordSheet() {
    _forgotEmailController.text = _emailController.text.trim();
    bool isSending = false;

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (ctx) => StatefulBuilder(
        builder: (ctx, setSheetState) {
          return ClipRRect(
            borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 16, sigmaY: 16),
              child: Container(
                padding: EdgeInsets.fromLTRB(
                  24,
                  18,
                  24,
                  MediaQuery.of(ctx).viewInsets.bottom + 28,
                ),
                decoration: const BoxDecoration(
                  color: Colors.white,
                  borderRadius:
                      BorderRadius.vertical(top: Radius.circular(32)),
                  border: Border(
                    top: BorderSide(
                      color: Color(0xFFBAE6FD),
                      width: 2.0,
                    ),
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: Color(0x250F172A),
                      blurRadius: 40,
                      offset: Offset(0, -10),
                    ),
                  ],
                ),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Center(
                      child: Container(
                        width: 44,
                        height: 5,
                        decoration: BoxDecoration(
                          color: const Color(0xFFCBD5E1),
                          borderRadius: BorderRadius.circular(3),
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(12),
                          decoration: BoxDecoration(
                            gradient: const LinearGradient(
                              colors: [Color(0xFF38BDF8), Color(0xFF0284C7)],
                              begin: Alignment.topLeft,
                              end: Alignment.bottomRight,
                            ),
                            shape: BoxShape.circle,
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xFF0284C7).withAlpha(100),
                                blurRadius: 16,
                                offset: const Offset(0, 4),
                              ),
                            ],
                          ),
                          child: const Icon(
                            Icons.lock_reset_rounded,
                            color: Colors.white,
                            size: 24,
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                tr('forgot_password_title'),
                                style: const TextStyle(
                                  color: Color(0xFF0F172A),
                                  fontSize: 20,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 0.3,
                                ),
                              ),
                              const SizedBox(height: 3),
                              Text(
                                tr('forgot_password_desc'),
                                style: const TextStyle(
                                  color: Color(0xFF64748B),
                                  fontSize: 12,
                                  height: 1.35,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),
                    TextField(
                      controller: _forgotEmailController,
                      keyboardType: TextInputType.emailAddress,
                      style: const TextStyle(
                        color: Color(0xFF0F172A),
                        fontWeight: FontWeight.w700,
                        fontSize: 14.5,
                      ),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: const Color(0xFFF8FAFC),
                        hintText: tr('enter_your_email'),
                        hintStyle: const TextStyle(
                          color: Color(0xFF94A3B8),
                          fontSize: 13.5,
                        ),
                        prefixIcon: const Icon(
                          Icons.alternate_email_rounded,
                          color: Color(0xFF0284C7),
                          size: 20,
                        ),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(16),
                          borderSide:
                              const BorderSide(color: Color(0xFFE2E8F0)),
                        ),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(16),
                          borderSide:
                              const BorderSide(color: Color(0xFFE2E8F0)),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(16),
                          borderSide: const BorderSide(
                            color: Color(0xFF0284C7),
                            width: 1.8,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 22),
                    SizedBox(
                      height: 52,
                      child: ElevatedButton(
                        onPressed: isSending
                            ? null
                            : () async {
                                final email =
                                    _forgotEmailController.text.trim();
                                if (email.isEmpty || !email.contains('@')) {
                                  return;
                                }

                                setSheetState(() => isSending = true);
                                await AuthService.instance.resetPassword(email);
                                if (ctx.mounted) Navigator.of(ctx).pop();
                                if (mounted) {
                                  _showFeedbackSnackBar(
                                    message: tr('reset_link_sent'),
                                    isSuccess: true,
                                    icon: Icons.mark_email_read_rounded,
                                  );
                                }
                              },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.transparent,
                          shadowColor: Colors.transparent,
                          padding: EdgeInsets.zero,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(16),
                          ),
                        ),
                        child: Ink(
                          decoration: BoxDecoration(
                            gradient: const LinearGradient(
                              colors: [Color(0xFF0284C7), Color(0xFF0EA5E9)],
                            ),
                            borderRadius: BorderRadius.circular(16),
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xFF0284C7).withAlpha(120),
                                blurRadius: 14,
                                offset: const Offset(0, 4),
                              ),
                            ],
                          ),
                          child: Center(
                            child: isSending
                                ? const SizedBox(
                                    width: 22,
                                    height: 22,
                                    child: CircularProgressIndicator(
                                      color: Colors.white,
                                      strokeWidth: 2.2,
                                    ),
                                  )
                                : Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      const Icon(Icons.send_rounded,
                                          color: Colors.white, size: 18),
                                      const SizedBox(width: 8),
                                      Text(
                                        tr('send_reset_link'),
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontWeight: FontWeight.w900,
                                          fontSize: 15,
                                          letterSpacing: 0.4,
                                        ),
                                      ),
                                    ],
                                  ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  void _showTermsSheet() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (ctx) => ClipRRect(
        borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
          child: Container(
            constraints: BoxConstraints(
              maxHeight: MediaQuery.of(ctx).size.height * 0.75,
            ),
            padding: const EdgeInsets.fromLTRB(24, 18, 24, 28),
            decoration: const BoxDecoration(
              color: Colors.white,
              borderRadius:
                  BorderRadius.vertical(top: Radius.circular(32)),
              border: Border(
                top: BorderSide(
                  color: Color(0xFFBAE6FD),
                  width: 2.0,
                ),
              ),
              boxShadow: [
                BoxShadow(
                  color: Color(0x250F172A),
                  blurRadius: 40,
                  offset: Offset(0, -10),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Center(
                  child: Container(
                    width: 44,
                    height: 5,
                    decoration: BoxDecoration(
                      color: const Color(0xFFCBD5E1),
                      borderRadius: BorderRadius.circular(3),
                    ),
                  ),
                ),
                const SizedBox(height: 18),
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE0F2FE),
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: const Color(0xFFBAE6FD),
                        ),
                      ),
                      child: const Icon(
                        Icons.verified_user_rounded,
                        color: Color(0xFF0284C7),
                        size: 22,
                      ),
                    ),
                    const SizedBox(width: 14),
                    const Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Terms & Privacy Policy',
                            style: TextStyle(
                              color: Color(0xFF0F172A),
                              fontSize: 19,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                          SizedBox(height: 2),
                          Text(
                            'MindTrap AI • Fair Play & Data Integrity',
                            style: TextStyle(color: Color(0xFF64748B), fontSize: 12, fontWeight: FontWeight.w500),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 16),
                const Divider(color: Color(0xFFE2E8F0)),
                Expanded(
                  child: SingleChildScrollView(
                    physics: const BouncingScrollPhysics(),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        _buildTermsParagraph(
                           title: '1. Player Privacy & Account Security',
                          body:
                              'MindTrap AI respects your privacy. Your email is exclusively used to securely preserve and synchronize your brain scores, hints, diamonds, stars, and level achievements across your devices via encrypted cloud sync.',
                        ),
                        _buildTermsParagraph(
                          title: '2. Fair Play & Cognitive Training',
                          body:
                              'All logical riddles, brain teasers, and puzzles are designed to deliver fair and enriching mental exercise. Automated bot exploitation or unfair manipulation of puzzle timers is strictly discouraged.',
                        ),
                        _buildTermsParagraph(
                          title: '3. Virtual Currency & Purchases',
                          body:
                              'In-game coins, diamonds, and hint packs unlocked through gameplay or secure store checkout are tied to your registered player profile for perpetual access across sessions.',
                        ),
                        _buildTermsParagraph(
                          title: '4. Guest Play Flexibility',
                          body:
                              'You can enjoy MindTrap AI as a Guest anytime. Linking an email simply ensures your earned milestones remain safe in case your device storage is cleared.',
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                Container(
                  height: 48,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    gradient: const LinearGradient(
                      colors: [Color(0xFF38BDF8), Color(0xFF0284C7)],
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: const Color(0xFF0284C7).withAlpha(90),
                        blurRadius: 16,
                        offset: const Offset(0, 4),
                      ),
                    ],
                  ),
                  child: ElevatedButton(
                    onPressed: () {
                      Navigator.of(ctx).pop();
                      setState(() => _agreeToTerms = true);
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.transparent,
                      shadowColor: Colors.transparent,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    child: const Text(
                      'I Accept & Understand',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 14,
                      ),
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

  Widget _buildTermsParagraph({required String title, required String body}) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: Color(0xFF0284C7),
              fontSize: 13.5,
              fontWeight: FontWeight.w800,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            body,
            style: const TextStyle(
              color: Color(0xFF475569),
              fontSize: 12.5,
              height: 1.45,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        final currentLang = LanguageController.instance.currentLanguage;

        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: GestureDetector(
            behavior: HitTestBehavior.translucent,
            onTap: () => FocusScope.of(context).unfocus(),
            child: Scaffold(
              backgroundColor: const Color(0xFFF0F9FF),
              body: Stack(
                children: [
                  // 1. Crystal-Clear Mountain Scenic Backdrop
                  const Positioned.fill(
                    child: Image(
                      image: AssetImage('assets/images/home_background.webp'),
                      fit: BoxFit.cover,
                      alignment: Alignment.center,
                    ),
                  ),

                  // 2. Soft Bright Vignette
                  Positioned.fill(
                    child: DecoratedBox(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.white.withAlpha(40),
                            Colors.transparent,
                            Colors.white.withAlpha(80),
                          ],
                          stops: const [0.0, 0.45, 1.0],
                        ),
                      ),
                    ),
                  ),

                  // 3. Main Content
                  SafeArea(
                    child: Column(
                      children: [
                        // Top Nav Header
                        _buildTopHeader(context, currentLang),

                        // Scrollable Card Container
                        Expanded(
                          child: SingleChildScrollView(
                            physics: const BouncingScrollPhysics(),
                            padding: const EdgeInsets.symmetric(
                              horizontal: 20,
                              vertical: 6,
                            ),
                            child: Center(
                              child: ConstrainedBox(
                                constraints: const BoxConstraints(maxWidth: 440),
                                child: Column(
                                  crossAxisAlignment:
                                      CrossAxisAlignment.center,
                                  children: [
                                    const SizedBox(height: 4),

                                    // Brand Hero Section
                                    _buildBrandHero(),

                                    const SizedBox(height: 18),

                                    // Core Glassmorphic Authentication Card
                                    _buildMainAuthCard(),

                                    const SizedBox(height: 16),

                                    // Security Trust Badge
                                    _buildSecurityBadge(),

                                    const SizedBox(height: 8),

                                    // Legal Terms & Privacy note
                                    _buildTermsFooter(),

                                    const SizedBox(height: 16),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }

  Widget _buildTopHeader(BuildContext context, AppLanguage currentLang) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 8, 16, 6),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          // Back Button
          _buildCircleButton(
            icon: Icons.arrow_back_rounded,
            tooltip: tr('back'),
            onPressed: () => Navigator.of(context).maybePop(),
          ),

          // Brand Center Pill with Neon Indicator
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
            decoration: BoxDecoration(
              color: Colors.white.withAlpha(230),
              borderRadius: BorderRadius.circular(24),
              border: Border.all(
                color: const Color(0xFFBAE6FD),
                width: 1.2,
              ),
              boxShadow: const [
                BoxShadow(
                  color: Color(0x120284C7),
                  blurRadius: 10,
                  offset: Offset(0, 3),
                ),
              ],
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 8,
                  height: 8,
                  decoration: const BoxDecoration(
                    color: Color(0xFF0284C7),
                    shape: BoxShape.circle,
                    boxShadow: [
                      BoxShadow(
                        color: Color(0xFF38BDF8),
                        blurRadius: 6,
                        spreadRadius: 1.5,
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 8),
                const Text(
                  'MINDTRAP AI',
                  style: TextStyle(
                    color: Color(0xFF0F172A),
                    fontSize: 12,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 1.6,
                  ),
                ),
              ],
            ),
          ),

          // Interactive Language Switcher Pill
          InkWell(
            borderRadius: BorderRadius.circular(22),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => const LanguageSelectionScreen(
                    isFromSettings: true,
                  ),
                ),
              );
            },
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 6),
              decoration: BoxDecoration(
                color: Colors.white.withAlpha(230),
                borderRadius: BorderRadius.circular(22),
                border: Border.all(
                  color: const Color(0xFFBAE6FD),
                  width: 1.2,
                ),
                boxShadow: const [
                  BoxShadow(
                    color: Color(0x100284C7),
                    blurRadius: 10,
                    offset: Offset(0, 2),
                  ),
                ],
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    currentLang.flagEmoji,
                    style: const TextStyle(fontSize: 15),
                  ),
                  const SizedBox(width: 5),
                  Text(
                    currentLang.code.toUpperCase(),
                    style: const TextStyle(
                      color: Color(0xFF0284C7),
                      fontSize: 12,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  const SizedBox(width: 3),
                  const Icon(
                    Icons.keyboard_arrow_down_rounded,
                    color: Color(0xFF0284C7),
                    size: 16,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCircleButton({
    required IconData icon,
    required VoidCallback onPressed,
    String? tooltip,
  }) {
    final isRtl = Directionality.of(context) == TextDirection.rtl;
    final displayIcon = (icon == Icons.arrow_back_rounded && isRtl)
        ? Icons.arrow_forward_rounded
        : icon;

    return Material(
      color: Colors.white,
      shape: const CircleBorder(),
      elevation: 2,
      shadowColor: const Color(0x332178BA),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: Tooltip(
          message: tooltip ?? '',
          child: SizedBox(
            width: 38,
            height: 38,
            child: Icon(
              displayIcon,
              color: const Color(0xFF244169),
              size: 24,
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildBrandHero() {
    return Column(
      children: [
        // Original Dual-Tone Gradient Brain Logo (Matching media_1790837940365)
        Container(
          width: 84,
          height: 84,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            color: Colors.white.withAlpha(235),
            border: Border.all(
              color: const Color(0xFFBAE6FD),
              width: 1.8,
            ),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF0284C7).withAlpha(45),
                blurRadius: 20,
                spreadRadius: 2,
                offset: const Offset(0, 4),
              ),
              BoxShadow(
                color: const Color(0xFF8B5CF6).withAlpha(35),
                blurRadius: 24,
                spreadRadius: 1,
              ),
            ],
          ),
          child: Center(
            child: Image.asset(
              'assets/images/home_logo.webp',
              width: 58,
              height: 58,
              fit: BoxFit.contain,
              errorBuilder: (_, e, s) => const Icon(
                Icons.psychology_rounded,
                color: Color(0xFF0284C7),
                size: 52,
              ),
            ),
          ),
        ),

        const SizedBox(height: 14),

        // Brand Title
        Text(
          tr('app_title'),
          style: const TextStyle(
            color: Color(0xFF0F172A),
            fontSize: 29,
            fontWeight: FontWeight.w900,
            letterSpacing: 1.1,
            shadows: [
              Shadow(
                color: Color(0x220284C7),
                blurRadius: 12,
                offset: Offset(0, 3),
              ),
            ],
          ),
        ),

        const SizedBox(height: 6),

        // Slogan / Subtitle
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: Text(
            tr('slogan'),
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Color(0xFF475569),
              fontSize: 13.5,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.2,
            ),
          ),
        ),

        const SizedBox(height: 12),

        // Feature Highlight Pills Row
        Wrap(
          spacing: 8,
          runSpacing: 6,
          alignment: WrapAlignment.center,
          crossAxisAlignment: WrapCrossAlignment.center,
          children: [
            _buildFeaturePill(Icons.psychology_alt_rounded, tr('cognitive_puzzles')),
            _buildFeaturePill(Icons.cloud_done_rounded, tr('cloud_sync')),
            _buildFeaturePill(Icons.emoji_events_rounded, tr('global_ranks')),
          ],
        ),
      ],
    );
  }

  Widget _buildFeaturePill(IconData icon, String label) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 5),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(220),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: const Color(0xFFBAE6FD),
          width: 1.0,
        ),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF0284C7).withAlpha(15),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, color: const Color(0xFF0284C7), size: 13),
          const SizedBox(width: 5),
          Text(
            label,
            style: const TextStyle(
              color: Color(0xFF0F172A),
              fontSize: 11,
              fontWeight: FontWeight.w800,
              letterSpacing: 0.3,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMainAuthCard() {
    return ClipRRect(
      borderRadius: BorderRadius.circular(30),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: Container(
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(235),
            borderRadius: BorderRadius.circular(30),
            border: Border.all(
              color: Colors.white,
              width: 1.5,
            ),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF0F172A).withAlpha(20),
                blurRadius: 32,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          padding: const EdgeInsets.fromLTRB(22, 22, 22, 24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Segmented Tab Bar Switcher
              _buildSegmentedTabBar(),

              const SizedBox(height: 18),

              // Error Banner (if any)
              if (_errorMessage != null) ...[
                _buildErrorBanner(),
                const SizedBox(height: 14),
              ],

              // Animated Transition between Sign In and Sign Up Forms
              AnimatedSize(
                duration: const Duration(milliseconds: 250),
                curve: Curves.easeInOutCubic,
                alignment: Alignment.topCenter,
                child: _tabController.index == 0
                    ? _buildSignInForm()
                    : _buildSignUpForm(),
              ),

              const SizedBox(height: 18),

              // "OR CONTINUE WITH" Divider
              _buildOrDivider(),

              const SizedBox(height: 14),

              // Social Authentication Buttons (Google + Apple)
              _buildSocialLoginRow(),

              const SizedBox(height: 12),

              // Instant Guest Access Option
              _buildGuestButton(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildSegmentedTabBar() {
    return Container(
      height: 48,
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        color: const Color(0xFFF1F5F9),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: const Color(0xFFE2E8F0)),
      ),
      child: TabBar(
        controller: _tabController,
        indicator: BoxDecoration(
          gradient: const LinearGradient(
            colors: [Color(0xFF0284C7), Color(0xFF0EA5E9)],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: const Color(0xFF0284C7).withAlpha(90),
              blurRadius: 8,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        dividerColor: Colors.transparent,
        indicatorSize: TabBarIndicatorSize.tab,
        labelColor: Colors.white,
        unselectedLabelColor: const Color(0xFF64748B),
        labelStyle: const TextStyle(
          fontWeight: FontWeight.w900,
          fontSize: 13.5,
          letterSpacing: 0.4,
        ),
        tabs: [
          Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.login_rounded, size: 16),
                const SizedBox(width: 7),
                Text(tr('sign_in')),
              ],
            ),
          ),
          Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.person_add_rounded, size: 16),
                const SizedBox(width: 7),
                Text(tr('sign_up')),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildErrorBanner() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 11),
      decoration: BoxDecoration(
        color: const Color(0xFFFEF2F2),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFFECACA)),
      ),
      child: Row(
        children: [
          const Icon(
            Icons.error_outline_rounded,
            color: Color(0xFFDC2626),
            size: 20,
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Text(
              _errorMessage!,
              style: const TextStyle(
                color: Color(0xFFB91C1C),
                fontSize: 12.5,
                fontWeight: FontWeight.w600,
                height: 1.3,
              ),
            ),
          ),
          GestureDetector(
            onTap: () => setState(() => _errorMessage = null),
            child: const Icon(
              Icons.close_rounded,
              color: Color(0xFFDC2626),
              size: 18,
            ),
          ),
        ],
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // SIGN IN FORM
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildSignInForm() {
    return Form(
      key: _signInFormKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Email Field
          _buildTextFormField(
            controller: _emailController,
            focusNode: _emailFocus,
            hintText: tr('enter_your_email'),
            labelText: tr('email'),
            icon: Icons.alternate_email_rounded,
            keyboardType: TextInputType.emailAddress,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.email],
            suffixIcon: _emailController.text.isNotEmpty
                ? IconButton(
                    icon: const Icon(Icons.clear_rounded,
                        color: Color(0xFF94A3B8), size: 18),
                    onPressed: () {
                      _emailController.clear();
                      setState(() {});
                    },
                  )
                : null,
            validator: (val) {
              if (val == null || val.trim().isEmpty || !val.contains('@')) {
                return tr('enter_valid_email');
              }
              return null;
            },
          ),

          const SizedBox(height: 14),

          // Password Field
          _buildTextFormField(
            controller: _passwordController,
            focusNode: _passwordFocus,
            hintText: tr('enter_your_password'),
            labelText: tr('password'),
            icon: Icons.lock_outline_rounded,
            obscureText: _obscurePassword,
            textInputAction: TextInputAction.done,
            autofillHints: const [AutofillHints.password],
            onFieldSubmitted: (_) => _submitSignIn(),
            suffixIcon: IconButton(
              icon: AnimatedSwitcher(
                duration: const Duration(milliseconds: 200),
                child: Icon(
                  _obscurePassword
                      ? Icons.visibility_off_rounded
                      : Icons.visibility_rounded,
                  key: ValueKey<bool>(_obscurePassword),
                  color: _obscurePassword
                      ? const Color(0xFF94A3B8)
                      : const Color(0xFF0284C7),
                  size: 20,
                ),
              ),
              onPressed: () =>
                  setState(() => _obscurePassword = !_obscurePassword),
            ),
            validator: (val) {
              if (val == null || val.length < 6) {
                return tr('password_too_short');
              }
              return null;
            },
          ),

          const SizedBox(height: 10),

          // Remember Me & Forgot Password Row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              // Remember Me Checkbox
              InkWell(
                borderRadius: BorderRadius.circular(8),
                onTap: () => setState(() => _rememberMe = !_rememberMe),
                child: Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        width: 19,
                        height: 19,
                        decoration: BoxDecoration(
                          color: _rememberMe
                              ? const Color(0xFF0284C7)
                              : Colors.white,
                          borderRadius: BorderRadius.circular(6),
                          border: Border.all(
                            color: _rememberMe
                                ? const Color(0xFF0284C7)
                                : const Color(0xFFCBD5E1),
                            width: 1.5,
                          ),
                        ),
                        child: _rememberMe
                            ? const Icon(
                                Icons.check_rounded,
                                color: Colors.white,
                                size: 14,
                              )
                            : null,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        tr('remember_me'),
                        style: const TextStyle(
                          color: Color(0xFF475569),
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              // Forgot Password Link
              TextButton(
                onPressed: _showForgotPasswordSheet,
                style: TextButton.styleFrom(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 6, vertical: 4),
                  minimumSize: Size.zero,
                  tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                ),
                child: Text(
                  tr('forgot_password'),
                  style: const TextStyle(
                    color: Color(0xFF0284C7),
                    fontSize: 12.5,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 18),

          // Submit Sign In Button
          _buildPrimaryButton(
            title: tr('sign_in'),
            icon: Icons.login_rounded,
            isLoading: _isLoading,
            onPressed: _submitSignIn,
          ),
        ],
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // SIGN UP FORM
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildSignUpForm() {
    return Form(
      key: _signUpFormKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Full Name Field
          _buildTextFormField(
            controller: _nameController,
            focusNode: _nameFocus,
            hintText: tr('enter_full_name'),
            labelText: tr('name'),
            icon: Icons.person_outline_rounded,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.name],
            suffixIcon: _nameController.text.isNotEmpty
                ? IconButton(
                    icon: const Icon(Icons.clear_rounded,
                        color: Color(0xFF94A3B8), size: 18),
                    onPressed: () {
                      _nameController.clear();
                      setState(() {});
                    },
                  )
                : null,
            validator: (val) {
              if (val == null || val.trim().length < 2) {
                return tr('enter_full_name');
              }
              return null;
            },
          ),

          const SizedBox(height: 14),

          // Email Field
          _buildTextFormField(
            controller: _emailController,
            focusNode: _signUpEmailFocus,
            hintText: tr('enter_your_email'),
            labelText: tr('email'),
            icon: Icons.alternate_email_rounded,
            keyboardType: TextInputType.emailAddress,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.email],
            suffixIcon: _emailController.text.isNotEmpty
                ? IconButton(
                    icon: const Icon(Icons.clear_rounded,
                        color: Color(0xFF94A3B8), size: 18),
                    onPressed: () {
                      _emailController.clear();
                      setState(() {});
                    },
                  )
                : null,
            validator: (val) {
              if (val == null || val.trim().isEmpty || !val.contains('@')) {
                return tr('enter_valid_email');
              }
              return null;
            },
          ),

          const SizedBox(height: 14),

          // Password Field
          _buildTextFormField(
            controller: _passwordController,
            focusNode: _signUpPasswordFocus,
            hintText: tr('enter_your_password'),
            labelText: tr('password'),
            icon: Icons.lock_outline_rounded,
            obscureText: _obscureSignUpPassword,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.newPassword],
            suffixIcon: IconButton(
              icon: AnimatedSwitcher(
                duration: const Duration(milliseconds: 200),
                child: Icon(
                  _obscureSignUpPassword
                      ? Icons.visibility_off_rounded
                      : Icons.visibility_rounded,
                  key: ValueKey<bool>(_obscureSignUpPassword),
                  color: _obscureSignUpPassword
                      ? const Color(0xFF94A3B8)
                      : const Color(0xFF0284C7),
                  size: 20,
                ),
              ),
              onPressed: () => setState(
                  () => _obscureSignUpPassword = !_obscureSignUpPassword),
            ),
            validator: (val) {
              if (val == null || val.length < 6) {
                return tr('password_too_short');
              }
              return null;
            },
          ),

          // Real-time Password Strength Meter
          if (_passwordController.text.isNotEmpty) ...[
            const SizedBox(height: 8),
            _buildPasswordStrengthMeter(),
          ],

          const SizedBox(height: 14),

          // Confirm Password Field
          _buildTextFormField(
            controller: _confirmPasswordController,
            focusNode: _confirmPasswordFocus,
            hintText: tr('confirm_password'),
            labelText: tr('confirm_password'),
            icon: Icons.lock_reset_rounded,
            obscureText: _obscureConfirmPassword,
            textInputAction: TextInputAction.done,
            autofillHints: const [AutofillHints.newPassword],
            onFieldSubmitted: (_) => _submitSignUp(),
            suffixIcon: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                if (_confirmPasswordController.text.isNotEmpty &&
                    _confirmPasswordController.text == _passwordController.text)
                  const Padding(
                    padding: EdgeInsets.only(right: 6),
                    child: Icon(
                      Icons.check_circle_rounded,
                      color: Color(0xFF10B981),
                      size: 20,
                    ),
                  ),
                IconButton(
                  icon: Icon(
                    _obscureConfirmPassword
                        ? Icons.visibility_off_rounded
                        : Icons.visibility_rounded,
                    color: _obscureConfirmPassword
                        ? const Color(0xFF94A3B8)
                        : const Color(0xFF0284C7),
                    size: 20,
                  ),
                  onPressed: () => setState(
                      () => _obscureConfirmPassword = !_obscureConfirmPassword),
                ),
              ],
            ),
            validator: (val) {
              if (val == null || val.isEmpty) {
                return tr('confirm_password');
              }
              if (val != _passwordController.text) {
                return tr('passwords_dont_match');
              }
              return null;
            },
          ),

          const SizedBox(height: 14),

          // Terms Acceptance Checkbox Row
          InkWell(
            borderRadius: BorderRadius.circular(8),
            onTap: () => setState(() => _agreeToTerms = !_agreeToTerms),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  width: 20,
                  height: 20,
                  margin: const EdgeInsets.only(top: 2),
                  decoration: BoxDecoration(
                    color: _agreeToTerms
                        ? const Color(0xFF0284C7)
                        : Colors.white,
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(
                      color: _agreeToTerms
                          ? const Color(0xFF0284C7)
                          : const Color(0xFFCBD5E1),
                      width: 1.5,
                    ),
                  ),
                  child: _agreeToTerms
                      ? const Icon(
                          Icons.check_rounded,
                          color: Colors.white,
                          size: 14,
                        )
                      : null,
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: GestureDetector(
                    onTap: _showTermsSheet,
                    child: RichText(
                      text: TextSpan(
                        text: tr('agree_terms_prefix'),
                        style: const TextStyle(
                          color: Color(0xFF475569),
                          fontSize: 12,
                          height: 1.35,
                        ),
                        children: [
                          TextSpan(
                            text: tr('terms_of_service'),
                            style: const TextStyle(
                              color: Color(0xFF0284C7),
                              fontWeight: FontWeight.w700,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                          TextSpan(text: tr('and_separator')),
                          TextSpan(
                            text: tr('privacy_policy'),
                            style: const TextStyle(
                              color: Color(0xFF0284C7),
                              fontWeight: FontWeight.w700,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 18),

          // Submit Create Account Button
          _buildPrimaryButton(
            title: tr('create_account'),
            icon: Icons.person_add_rounded,
            isLoading: _isLoading,
            onPressed: _submitSignUp,
          ),
        ],
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // PASSWORD STRENGTH METER WIDGET
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildPasswordStrengthMeter() {
    Color activeColor;
    String strengthLabel;

    switch (_passwordScore) {
      case 1:
        activeColor = const Color(0xFFEF4444);
        strengthLabel = tr('weak');
        break;
      case 2:
        activeColor = const Color(0xFFF59E0B);
        strengthLabel = tr('fair');
        break;
      case 3:
        activeColor = const Color(0xFF0284C7);
        strengthLabel = tr('good');
        break;
      case 4:
        activeColor = const Color(0xFF10B981);
        strengthLabel = tr('strong');
        break;
      default:
        activeColor = const Color(0xFFE2E8F0);
        strengthLabel = '';
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              tr('password_strength'),
              style: const TextStyle(
                color: Color(0xFF64748B),
                fontSize: 11,
                fontWeight: FontWeight.w600,
              ),
            ),
            Text(
              strengthLabel,
              style: TextStyle(
                color: activeColor,
                fontSize: 11,
                fontWeight: FontWeight.w900,
                letterSpacing: 0.3,
              ),
            ),
          ],
        ),
        const SizedBox(height: 6),
        Row(
          children: List.generate(4, (index) {
            final isFilled = index < _passwordScore;
            return Expanded(
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                height: 4,
                margin: EdgeInsets.only(right: index == 3 ? 0 : 5),
                decoration: BoxDecoration(
                  color: isFilled ? activeColor : const Color(0xFFE2E8F0),
                  borderRadius: BorderRadius.circular(2),
                  boxShadow: isFilled
                      ? [
                          BoxShadow(
                            color: activeColor.withAlpha(90),
                            blurRadius: 4,
                          ),
                        ]
                      : null,
                ),
              ),
            );
          }),
        ),
        const SizedBox(height: 8),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            _buildRulePill(tr('password_rule_len'), _hasMinLength),
            _buildRulePill(tr('password_rule_num'), _hasNumber),
            _buildRulePill(tr('password_rule_special'), _hasSpecialOrUpper),
          ],
        ),
      ],
    );
  }

  Widget _buildRulePill(String label, bool isSatisfied) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(
          isSatisfied
              ? Icons.check_circle_rounded
              : Icons.radio_button_unchecked_rounded,
          color: isSatisfied ? const Color(0xFF10B981) : const Color(0xFF94A3B8),
          size: 13,
        ),
        const SizedBox(width: 4),
        Text(
          label,
          style: TextStyle(
            color: isSatisfied
                ? const Color(0xFF059669)
                : const Color(0xFF64748B),
            fontSize: 10,
            fontWeight: FontWeight.w600,
          ),
        ),
      ],
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // PRIMARY BUTTON
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildPrimaryButton({
    required String title,
    required IconData icon,
    required bool isLoading,
    required VoidCallback onPressed,
  }) {
    return SizedBox(
      height: 52,
      child: ElevatedButton(
        onPressed: isLoading ? null : onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.transparent,
          shadowColor: Colors.transparent,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
          padding: EdgeInsets.zero,
        ),
        child: Ink(
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              colors: [Color(0xFF0284C7), Color(0xFF0EA5E9), Color(0xFF38BDF8)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF0284C7).withAlpha(140),
                blurRadius: 18,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Container(
            alignment: Alignment.center,
            child: isLoading
                ? Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(
                          color: Colors.white,
                          strokeWidth: 2.2,
                        ),
                      ),
                      const SizedBox(width: 10),
                      Text(
                        tr('authenticating'),
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 14,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ],
                  )
                : Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(icon, color: Colors.white, size: 19),
                      const SizedBox(width: 8),
                      Text(
                        title,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 15,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 0.5,
                        ),
                      ),
                      const SizedBox(width: 6),
                      const Icon(
                        Icons.arrow_forward_rounded,
                        color: Colors.white70,
                        size: 16,
                      ),
                    ],
                  ),
          ),
        ),
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // OR DIVIDER
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildOrDivider() {
    return Row(
      children: [
        Expanded(
          child: Container(
            height: 1,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Colors.transparent, Color(0xFFE2E8F0)],
              ),
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 14),
          child: Text(
            tr('or_continue_with'),
            style: const TextStyle(
              color: Color(0xFF94A3B8),
              fontSize: 10.5,
              fontWeight: FontWeight.w800,
              letterSpacing: 1.2,
            ),
          ),
        ),
        Expanded(
          child: Container(
            height: 1,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFFE2E8F0), Colors.transparent],
              ),
            ),
          ),
        ),
      ],
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // SOCIAL LOGIN ROW (Google + Apple)
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildSocialLoginRow() {
    return Row(
      children: [
        // Google Button
        Expanded(
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              borderRadius: BorderRadius.circular(16),
              onTap: _isSocialLoading ? null : _signInWithGoogle,
              child: Container(
                height: 48,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: const Color(0xFFE2E8F0),
                    width: 1.2,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF0F172A).withAlpha(10),
                      blurRadius: 6,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    CustomPaint(
                      size: const Size(19, 19),
                      painter: GoogleLogoPainter(),
                    ),
                    const SizedBox(width: 8),
                    const Text(
                      'Google',
                      style: TextStyle(
                        color: Color(0xFF0F172A),
                        fontWeight: FontWeight.w800,
                        fontSize: 13.5,
                        letterSpacing: 0.3,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),

        const SizedBox(width: 12),

        // Apple Button
        Expanded(
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              borderRadius: BorderRadius.circular(16),
              onTap: _isSocialLoading ? null : _signInWithApple,
              child: Container(
                height: 48,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: const Color(0xFFE2E8F0),
                    width: 1.2,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF0F172A).withAlpha(10),
                      blurRadius: 6,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(
                      Icons.apple,
                      color: Colors.black,
                      size: 22,
                    ),
                    SizedBox(width: 6),
                    Text(
                      'Apple',
                      style: TextStyle(
                        color: Color(0xFF0F172A),
                        fontWeight: FontWeight.w800,
                        fontSize: 13.5,
                        letterSpacing: 0.3,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // GUEST PLAY BUTTON
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildGuestButton() {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        borderRadius: BorderRadius.circular(18),
        onTap: _isLoading ? null : _continueAsGuest,
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
          decoration: BoxDecoration(
            color: const Color(0xFFFFFBEB),
            borderRadius: BorderRadius.circular(18),
            border: Border.all(
              color: const Color(0xFFFDE68A),
              width: 1.2,
            ),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFFD97706).withAlpha(15),
                blurRadius: 8,
                offset: const Offset(0, 2),
              ),
            ],
          ),
          child: Row(
            children: [
              Container(
                padding: const EdgeInsets.all(7),
                decoration: BoxDecoration(
                  color: const Color(0xFFFEF3C7),
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFFD97706).withAlpha(30),
                      blurRadius: 6,
                    ),
                  ],
                ),
                child: const Icon(
                  Icons.bolt_rounded,
                  color: Color(0xFFD97706),
                  size: 20,
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      tr('play_as_guest'),
                      style: const TextStyle(
                        color: Color(0xFF0F172A),
                        fontWeight: FontWeight.w800,
                        fontSize: 13.5,
                        letterSpacing: 0.3,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      tr('guest_benefits'),
                      style: const TextStyle(
                        color: Color(0xFF78716C),
                        fontSize: 10.5,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
              const Icon(
                Icons.arrow_forward_ios_rounded,
                color: Color(0xFF94A3B8),
                size: 13,
              ),
            ],
          ),
        ),
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // SECURITY BADGE & FOOTER
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildSecurityBadge() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
      decoration: BoxDecoration(
        color: Colors.white.withAlpha(220),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: const Color(0xFFBAE6FD),
          width: 1.0,
        ),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF0284C7).withAlpha(15),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(
            Icons.shield_outlined,
            color: Color(0xFF0284C7),
            size: 14,
          ),
          const SizedBox(width: 7),
          Text(
            tr('ssl_security_badge'),
            style: const TextStyle(
              color: Color(0xFF0284C7),
              fontSize: 11,
              fontWeight: FontWeight.w700,
              letterSpacing: 0.3,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTermsFooter() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      child: Text(
        tr('terms_privacy'),
        textAlign: TextAlign.center,
        style: const TextStyle(
          color: Color(0xFF64748B),
          fontSize: 10.5,
          fontWeight: FontWeight.w500,
          height: 1.4,
        ),
      ),
    );
  }

  // ════════════════════════════════════════════════════════════════════════════
  // REUSABLE TEXT FORM FIELD
  // ════════════════════════════════════════════════════════════════════════════
  Widget _buildTextFormField({
    required TextEditingController controller,
    required FocusNode focusNode,
    required String hintText,
    required String labelText,
    required IconData icon,
    TextInputType keyboardType = TextInputType.text,
    TextInputAction textInputAction = TextInputAction.next,
    Iterable<String>? autofillHints,
    void Function(String)? onFieldSubmitted,
    bool obscureText = false,
    Widget? suffixIcon,
    String? Function(String?)? validator,
  }) {
    return TextFormField(
      controller: controller,
      focusNode: focusNode,
      keyboardType: keyboardType,
      textInputAction: textInputAction,
      autofillHints: autofillHints,
      onFieldSubmitted: onFieldSubmitted,
      obscureText: obscureText,
      validator: validator,
      style: const TextStyle(
        color: Color(0xFF0F172A),
        fontWeight: FontWeight.w600,
        fontSize: 14.5,
      ),
      decoration: InputDecoration(
        filled: true,
        fillColor: const Color(0xFFF8FAFC),
        labelText: labelText,
        labelStyle: const TextStyle(
          color: Color(0xFF64748B),
          fontSize: 13,
          fontWeight: FontWeight.w600,
        ),
        floatingLabelStyle: const TextStyle(
          color: Color(0xFF0284C7),
          fontSize: 13,
          fontWeight: FontWeight.w800,
        ),
        hintText: hintText,
        hintStyle: const TextStyle(
          color: Color(0xFF94A3B8),
          fontSize: 13.5,
          fontWeight: FontWeight.w500,
        ),
        prefixIcon: Icon(icon, color: const Color(0xFF0284C7), size: 20),
        suffixIcon: suffixIcon,
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 16, vertical: 15),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFF0284C7), width: 1.8),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFEF4444)),
        ),
        focusedErrorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFEF4444), width: 1.8),
        ),
        errorStyle: const TextStyle(
          color: Color(0xFFDC2626),
          fontSize: 11,
          fontWeight: FontWeight.w600,
        ),
      ),
    );
  }
}

// ══════════════════════════════════════════════════════════════════════════════
// OFFICIAL VECTOR GOOGLE LOGO PAINTER
// ══════════════════════════════════════════════════════════════════════════════
class GoogleLogoPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final double w = size.width;
    final double h = size.height;
    final center = Offset(w / 2, h / 2);
    final radius = w / 2;

    final redPaint = Paint()
      ..color = const Color(0xFFEA4335)
      ..style = PaintingStyle.fill;
    final yellowPaint = Paint()
      ..color = const Color(0xFFFBBC05)
      ..style = PaintingStyle.fill;
    final greenPaint = Paint()
      ..color = const Color(0xFF34A853)
      ..style = PaintingStyle.fill;
    final bluePaint = Paint()
      ..color = const Color(0xFF4285F4)
      ..style = PaintingStyle.fill;

    // Draw Google 4-color arcs
    final rect = Rect.fromCircle(center: center, radius: radius);
    final innerRadius = radius * 0.55;

    // Red arc (top)
    final redPath = Path()
      ..moveTo(center.dx, center.dy)
      ..arcTo(rect, -2.4, 1.3, false)
      ..close();
    canvas.drawPath(redPath, redPaint);

    // Yellow arc (left)
    final yellowPath = Path()
      ..moveTo(center.dx, center.dy)
      ..arcTo(rect, -1.1 - 3.14, 1.2, false)
      ..close();
    canvas.drawPath(yellowPath, yellowPaint);

    // Green arc (bottom)
    final greenPath = Path()
      ..moveTo(center.dx, center.dy)
      ..arcTo(rect, 0.4, 1.4, false)
      ..close();
    canvas.drawPath(greenPath, greenPaint);

    // Blue arc (right & center bar)
    final bluePath = Path()
      ..moveTo(center.dx, center.dy)
      ..arcTo(rect, -0.7, 1.1, false)
      ..close();
    canvas.drawPath(bluePath, bluePaint);

    // Inner cutout
    final cutoutPaint = Paint()
      ..color = Colors.white
      ..style = PaintingStyle.fill;
    canvas.drawCircle(center, innerRadius, cutoutPaint);

    // Blue horizontal bar
    final barRect = Rect.fromLTRB(
      center.dx,
      center.dy - (radius * 0.22),
      w,
      center.dy + (radius * 0.22),
    );
    canvas.drawRect(barRect, bluePaint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
