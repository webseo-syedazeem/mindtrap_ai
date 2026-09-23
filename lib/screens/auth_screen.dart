import 'dart:ui';
import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
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
  final _formKey = GlobalKey<FormState>();

  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _forgotEmailController = TextEditingController();

  bool _obscurePassword = true;
  bool _isLoading = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(() {
      if (_tabController.indexIsChanging) {
        setState(() {
          _errorMessage = null;
        });
      }
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    _nameController.dispose();
    _forgotEmailController.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    final isSignIn = _tabController.index == 0;
    Map<String, dynamic> result;

    if (isSignIn) {
      result = await AuthService.instance.signIn(
        email: _emailController.text.trim(),
        password: _passwordController.text,
      );
    } else {
      result = await AuthService.instance.signUp(
        email: _emailController.text.trim(),
        password: _passwordController.text,
        name: _nameController.text.trim(),
      );
    }

    if (!mounted) return;

    setState(() {
      _isLoading = false;
    });

    if (result['success'] == true) {
      _showSuccessSnackBar(result['message'] as String? ?? tr('auth_success'));
      if (widget.onAuthSuccess != null) {
        widget.onAuthSuccess!();
      } else {
        Navigator.of(context).pop();
      }
    } else {
      setState(() {
        _errorMessage = result['message'] as String? ?? tr('auth_error');
      });
    }
  }

  void _showSuccessSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle_rounded, color: Color(0xFF4ADE80)),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                message,
                style: const TextStyle(
                  fontWeight: FontWeight.w700,
                  color: Colors.white,
                ),
              ),
            ),
          ],
        ),
        backgroundColor: const Color(0xFF0F172A),
        behavior: SnackBarBehavior.floating,
        margin: const EdgeInsets.all(16),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
    );
  }

  void _showForgotPasswordSheet() {
    _forgotEmailController.text = _emailController.text;
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (ctx) => ClipRRect(
        borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
          child: Container(
            padding: EdgeInsets.fromLTRB(
              24, 20, 24, MediaQuery.of(ctx).viewInsets.bottom + 32,
            ),
            decoration: BoxDecoration(
              color: const Color(0xFF0F172A).withAlpha(245),
              borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
              border: Border(
                top: BorderSide(color: const Color(0xFF38BDF8).withAlpha(90), width: 1.5),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withAlpha(200),
                  blurRadius: 30,
                  offset: const Offset(0, -5),
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
                    height: 4,
                    decoration: BoxDecoration(
                      color: Colors.white24,
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                ),
                const SizedBox(height: 22),
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFF0284C7), Color(0xFF38BDF8)],
                        ),
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF0284C7).withAlpha(120),
                            blurRadius: 12,
                          ),
                        ],
                      ),
                      child: const Icon(
                        Icons.lock_reset_rounded,
                        color: Colors.white,
                        size: 22,
                      ),
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            tr('forgot_password'),
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 19,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                          const SizedBox(height: 3),
                          Text(
                            tr('email'),
                            style: const TextStyle(color: Colors.white60, fontSize: 12),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 22),
                TextField(
                  controller: _forgotEmailController,
                  keyboardType: TextInputType.emailAddress,
                  style: const TextStyle(color: Colors.white, fontSize: 15),
                  decoration: InputDecoration(
                    filled: true,
                    fillColor: const Color(0xFF1E293B),
                    hintText: tr('email'),
                    hintStyle: const TextStyle(color: Colors.white38),
                    prefixIcon: const Icon(
                      Icons.alternate_email_rounded,
                      color: Color(0xFF38BDF8),
                      size: 20,
                    ),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(16),
                      borderSide: BorderSide(color: Colors.white.withAlpha(25)),
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(16),
                      borderSide: BorderSide(color: Colors.white.withAlpha(25)),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(16),
                      borderSide: const BorderSide(color: Color(0xFF38BDF8), width: 1.8),
                    ),
                  ),
                ),
                const SizedBox(height: 22),
                SizedBox(
                  height: 52,
                  child: ElevatedButton(
                    onPressed: () async {
                      final email = _forgotEmailController.text.trim();
                      if (email.isNotEmpty && email.contains('@')) {
                        await AuthService.instance.resetPassword(email);
                        if (ctx.mounted) Navigator.of(ctx).pop();
                        if (mounted) {
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              content: Row(
                                children: [
                                  const Icon(Icons.check_circle_rounded, color: Color(0xFF4ADE80)),
                                  const SizedBox(width: 10),
                                  Expanded(
                                    child: Text(
                                      tr('reset_link_sent'),
                                      style: const TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.w700,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                              backgroundColor: const Color(0xFF0F172A),
                              behavior: SnackBarBehavior.floating,
                              margin: const EdgeInsets.all(16),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(16),
                              ),
                            ),
                          );
                        }
                      }
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF0284C7),
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                      elevation: 4,
                    ),
                    child: Text(
                      tr('send_reset_link'),
                      style: const TextStyle(
                        fontWeight: FontWeight.w900,
                        fontSize: 15,
                        letterSpacing: 0.5,
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
              backgroundColor: const Color(0xFF0A0E17),
              body: Stack(
                children: [
                  // 1. Crystal-Clear Alpine Mountain Scenery (Stage-7)
                  const Positioned.fill(
                    child: Image(
                      image: AssetImage('assets/images/Stage-7.webp'),
                      fit: BoxFit.cover,
                      alignment: Alignment.center,
                    ),
                  ),

                  // 2. High-end subtle vignette (No purple, pure crystal contrast)
                  Positioned.fill(
                    child: DecoratedBox(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.black.withAlpha(80),
                            Colors.black.withAlpha(20),
                            Colors.black.withAlpha(160),
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
                        // Top Navigation Header
                        Padding(
                          padding: const EdgeInsets.fromLTRB(16, 8, 16, 0),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              // Back Button
                              _buildCircleButton(
                                icon: Icons.arrow_back_ios_new_rounded,
                                onPressed: () => Navigator.of(context).maybePop(),
                              ),

                              // Brand Center Pill
                              Container(
                                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                                decoration: BoxDecoration(
                                  color: Colors.black.withAlpha(120),
                                  borderRadius: BorderRadius.circular(20),
                                  border: Border.all(color: Colors.white.withAlpha(35)),
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Image.asset(
                                      'assets/images/home_logo.webp',
                                      width: 18,
                                      height: 18,
                                      color: const Color(0xFF38BDF8),
                                      errorBuilder: (_, e, s) => const Icon(
                                        Icons.psychology_rounded,
                                        color: Color(0xFF38BDF8),
                                        size: 18,
                                      ),
                                    ),
                                    const SizedBox(width: 7),
                                    const Text(
                                      'MINDTRAP AI',
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontSize: 12,
                                        fontWeight: FontWeight.w900,
                                        letterSpacing: 1.4,
                                      ),
                                    ),
                                  ],
                                ),
                              ),

                              // Active Language Switcher Pill
                              InkWell(
                                borderRadius: BorderRadius.circular(20),
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
                                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                                  decoration: BoxDecoration(
                                    color: Colors.black.withAlpha(120),
                                    borderRadius: BorderRadius.circular(20),
                                    border: Border.all(color: const Color(0xFF38BDF8).withAlpha(80)),
                                  ),
                                  child: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      Text(
                                        currentLang.flagEmoji,
                                        style: const TextStyle(fontSize: 14),
                                      ),
                                      const SizedBox(width: 5),
                                      Text(
                                        currentLang.code.toUpperCase(),
                                        style: const TextStyle(
                                          color: Color(0xFF38BDF8),
                                          fontSize: 12,
                                          fontWeight: FontWeight.w900,
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),

                        // Scrollable Body
                        Expanded(
                          child: SingleChildScrollView(
                            physics: const BouncingScrollPhysics(),
                            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                            child: ConstrainedBox(
                              constraints: const BoxConstraints(maxWidth: 420),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  const SizedBox(height: 12),

                                  // Hero Icon + App Title + Slogan
                                  _buildHeroSection(),

                                  const SizedBox(height: 22),

                                  // Glassmorphic Auth Card
                                  _buildAuthCard(),

                                  const SizedBox(height: 16),

                                  // Security Trust Badge Row
                                  Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      const Icon(
                                        Icons.shield_outlined,
                                        color: Color(0xFF38BDF8),
                                        size: 14,
                                      ),
                                      const SizedBox(width: 6),
                                      Text(
                                        '256-Bit SSL Encrypted • Cloud Sync',
                                        style: TextStyle(
                                          color: Colors.white.withAlpha(140),
                                          fontSize: 11,
                                          fontWeight: FontWeight.w600,
                                          letterSpacing: 0.3,
                                        ),
                                      ),
                                    ],
                                  ),

                                  const SizedBox(height: 8),

                                  // Terms & Privacy
                                  Padding(
                                    padding: const EdgeInsets.symmetric(horizontal: 16),
                                    child: Text(
                                      tr('terms_privacy'),
                                      textAlign: TextAlign.center,
                                      style: TextStyle(
                                        color: Colors.white.withAlpha(110),
                                        fontSize: 10.5,
                                        fontWeight: FontWeight.w500,
                                      ),
                                    ),
                                  ),

                                  const SizedBox(height: 12),
                                ],
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

  Widget _buildCircleButton({
    required IconData icon,
    required VoidCallback onPressed,
  }) {
    return Material(
      color: Colors.black.withAlpha(120),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: Container(
          width: 40,
          height: 40,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            border: Border.all(color: Colors.white.withAlpha(35)),
          ),
          child: Icon(icon, color: Colors.white, size: 18),
        ),
      ),
    );
  }

  Widget _buildHeroSection() {
    return Column(
      children: [
        // Sleek Glowing Brain Logo
        Container(
          width: 76,
          height: 76,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            gradient: const LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Color(0xFF0284C7), Color(0xFF0369A1)],
            ),
            border: Border.all(color: const Color(0xFF38BDF8), width: 2),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF0284C7).withAlpha(140),
                blurRadius: 24,
                spreadRadius: 2,
              ),
            ],
          ),
          child: Center(
            child: Image.asset(
              'assets/images/home_logo.webp',
              width: 44,
              height: 44,
              color: Colors.white,
              errorBuilder: (_, e, s) => const Icon(
                Icons.psychology_rounded,
                color: Colors.white,
                size: 44,
              ),
            ),
          ),
        ),

        const SizedBox(height: 14),

        // Brand Name
        Text(
          tr('app_title'),
          style: const TextStyle(
            color: Colors.white,
            fontSize: 28,
            fontWeight: FontWeight.w900,
            letterSpacing: 1.2,
            shadows: [
              Shadow(color: Color(0xFF0284C7), blurRadius: 18, offset: Offset(0, 2)),
              Shadow(color: Colors.black87, blurRadius: 10, offset: Offset(0, 3)),
            ],
          ),
        ),

        const SizedBox(height: 6),

        // Elegant Slogan
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24),
          child: Text(
            tr('slogan'),
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Colors.white.withAlpha(220),
              fontSize: 13.5,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.3,
              shadows: const [
                Shadow(color: Colors.black, blurRadius: 10, offset: Offset(0, 1)),
              ],
            ),
          ),
        ),

        const SizedBox(height: 8),

        // Elegant category tag
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
          decoration: BoxDecoration(
            color: const Color(0xFF0284C7).withAlpha(40),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: const Color(0xFF38BDF8).withAlpha(90), width: 0.8),
          ),
          child: const Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.auto_awesome_rounded, color: Color(0xFF38BDF8), size: 12),
              SizedBox(width: 5),
              Text(
                'AI COGNITIVE PUZZLES',
                style: TextStyle(
                  color: Color(0xFF38BDF8),
                  fontSize: 10,
                  fontWeight: FontWeight.w900,
                  letterSpacing: 1.2,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildAuthCard() {
    return ClipRRect(
      borderRadius: BorderRadius.circular(28),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 16, sigmaY: 16),
        child: Container(
          decoration: BoxDecoration(
            color: const Color(0xFF0F172A).withAlpha(195),
            borderRadius: BorderRadius.circular(28),
            border: Border.all(
              color: const Color(0xFF38BDF8).withAlpha(45),
              width: 1.2,
            ),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withAlpha(160),
                blurRadius: 30,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          padding: const EdgeInsets.fromLTRB(20, 22, 20, 22),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisSize: MainAxisSize.min,
              children: [
                // Tab Bar — Sign In / Sign Up
                Container(
                  height: 48,
                  padding: const EdgeInsets.all(4),
                  decoration: BoxDecoration(
                    color: const Color(0xFF1E293B).withAlpha(160),
                    borderRadius: BorderRadius.circular(24),
                    border: Border.all(color: Colors.white.withAlpha(15)),
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
                          color: const Color(0xFF0284C7).withAlpha(110),
                          blurRadius: 10,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    dividerColor: Colors.transparent,
                    indicatorSize: TabBarIndicatorSize.tab,
                    labelColor: Colors.white,
                    unselectedLabelColor: Colors.white60,
                    labelStyle: const TextStyle(
                      fontWeight: FontWeight.w900,
                      fontSize: 13.5,
                      letterSpacing: 0.4,
                    ),
                    tabs: [
                      Tab(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            const Icon(Icons.login_rounded, size: 16),
                            const SizedBox(width: 6),
                            Text(tr('sign_in')),
                          ],
                        ),
                      ),
                      Tab(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            const Icon(Icons.person_add_rounded, size: 16),
                            const SizedBox(width: 6),
                            Text(tr('sign_up')),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 20),

                // Error Banner
                if (_errorMessage != null) ...[
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                    decoration: BoxDecoration(
                      color: const Color(0xFFEF4444).withAlpha(30),
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: const Color(0xFFEF4444).withAlpha(120)),
                    ),
                    child: Row(
                      children: [
                        const Icon(
                          Icons.error_outline_rounded,
                          color: Color(0xFFF87171),
                          size: 18,
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Text(
                            _errorMessage!,
                            style: const TextStyle(
                              color: Color(0xFFFCA5A5),
                              fontSize: 12.5,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                        GestureDetector(
                          onTap: () => setState(() => _errorMessage = null),
                          child: const Icon(
                            Icons.close_rounded,
                            color: Color(0xFFF87171),
                            size: 16,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),
                ],

                // Name Field (Sign Up only)
                if (_tabController.index == 1) ...[
                  _buildInputField(
                    controller: _nameController,
                    hintText: tr('name'),
                    icon: Icons.person_outline_rounded,
                    textInputAction: TextInputAction.next,
                    autofillHints: const [AutofillHints.name],
                    validator: (val) {
                      if (_tabController.index == 1 &&
                          (val == null || val.trim().isEmpty)) {
                        return 'Please enter your full name';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 12),
                ],

                // Email Field
                _buildInputField(
                  controller: _emailController,
                  hintText: tr('email'),
                  icon: Icons.alternate_email_rounded,
                  keyboardType: TextInputType.emailAddress,
                  textInputAction: TextInputAction.next,
                  autofillHints: const [AutofillHints.email],
                  validator: (val) {
                    if (val == null || val.trim().isEmpty || !val.contains('@')) {
                      return tr('enter_valid_email');
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 12),

                // Password Field
                _buildInputField(
                  controller: _passwordController,
                  hintText: tr('password'),
                  icon: Icons.lock_outline_rounded,
                  obscureText: _obscurePassword,
                  textInputAction: TextInputAction.done,
                  autofillHints: const [AutofillHints.password],
                  onFieldSubmitted: (_) => _submit(),
                  suffixIcon: IconButton(
                    icon: AnimatedSwitcher(
                      duration: const Duration(milliseconds: 200),
                      child: Icon(
                        _obscurePassword
                            ? Icons.visibility_off_outlined
                            : Icons.visibility_outlined,
                        key: ValueKey<bool>(_obscurePassword),
                        color: Colors.white54,
                        size: 19,
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

                // Forgot Password link
                if (_tabController.index == 0) ...[
                  Align(
                    alignment: AlignmentDirectional.centerEnd,
                    child: TextButton(
                      onPressed: _showForgotPasswordSheet,
                      style: TextButton.styleFrom(
                        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 4),
                        minimumSize: Size.zero,
                        tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                      ),
                      child: Text(
                        tr('forgot_password'),
                        style: const TextStyle(
                          color: Color(0xFF38BDF8),
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 12),
                ] else
                  const SizedBox(height: 16),

                // Submit Button
                SizedBox(
                  height: 50,
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _submit,
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
                          colors: [Color(0xFF0284C7), Color(0xFF0EA5E9)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        borderRadius: BorderRadius.circular(16),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF0284C7).withAlpha(120),
                            blurRadius: 16,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Container(
                        alignment: Alignment.center,
                        child: _isLoading
                            ? const SizedBox(
                                width: 22,
                                height: 22,
                                child: CircularProgressIndicator(
                                  color: Colors.white,
                                  strokeWidth: 2.2,
                                ),
                              )
                            : Row(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Icon(
                                    _tabController.index == 0
                                        ? Icons.login_rounded
                                        : Icons.person_add_rounded,
                                    color: Colors.white,
                                    size: 18,
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    _tabController.index == 0
                                        ? tr('sign_in')
                                        : tr('create_account'),
                                    style: const TextStyle(
                                      color: Colors.white,
                                      fontSize: 15,
                                      fontWeight: FontWeight.w900,
                                      letterSpacing: 0.5,
                                    ),
                                  ),
                                ],
                              ),
                      ),
                    ),
                  ),
                ),

                const SizedBox(height: 16),

                // "OR" Divider
                Row(
                  children: [
                    Expanded(
                      child: Divider(color: Colors.white.withAlpha(25)),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      child: Text(
                        'OR',
                        style: TextStyle(
                          color: Colors.white.withAlpha(120),
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 1.0,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Divider(color: Colors.white.withAlpha(25)),
                    ),
                  ],
                ),

                const SizedBox(height: 14),

                // Continue as Guest Button (Integrated cleanly inside card)
                Material(
                  color: Colors.transparent,
                  child: InkWell(
                    borderRadius: BorderRadius.circular(16),
                    onTap: () async {
                      final nav = Navigator.of(context);
                      await AuthService.instance.continueAsGuest();
                      if (mounted) {
                        if (widget.onAuthSuccess != null) {
                          widget.onAuthSuccess!();
                        } else {
                          nav.pop();
                        }
                      }
                    },
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 11),
                      decoration: BoxDecoration(
                        color: Colors.white.withAlpha(12),
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: Colors.white.withAlpha(25)),
                      ),
                      child: Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(6),
                            decoration: BoxDecoration(
                              color: const Color(0xFFFFB703).withAlpha(35),
                              shape: BoxShape.circle,
                            ),
                            child: const Icon(
                              Icons.bolt_rounded,
                              color: Color(0xFFFFB703),
                              size: 18,
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  tr('continue_as_guest'),
                                  style: const TextStyle(
                                    color: Color(0xFFE2E8F0),
                                    fontWeight: FontWeight.w800,
                                    fontSize: 13.5,
                                    letterSpacing: 0.3,
                                  ),
                                ),
                                const SizedBox(height: 1),
                                Text(
                                  'Play instantly • Cloud sync later',
                                  style: TextStyle(
                                    color: Colors.white.withAlpha(130),
                                    fontSize: 10.5,
                                    fontWeight: FontWeight.w500,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Icon(
                            Icons.arrow_forward_ios_rounded,
                            color: Colors.white.withAlpha(120),
                            size: 13,
                          ),
                        ],
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

  Widget _buildInputField({
    required TextEditingController controller,
    required String hintText,
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
      keyboardType: keyboardType,
      textInputAction: textInputAction,
      autofillHints: autofillHints,
      onFieldSubmitted: onFieldSubmitted,
      obscureText: obscureText,
      validator: validator,
      style: const TextStyle(
        color: Colors.white,
        fontWeight: FontWeight.w600,
        fontSize: 14.5,
      ),
      decoration: InputDecoration(
        filled: true,
        fillColor: const Color(0xFF1E293B).withAlpha(160),
        hintText: hintText,
        hintStyle: TextStyle(
          color: Colors.white.withAlpha(90),
          fontSize: 13.5,
          fontWeight: FontWeight.w500,
        ),
        prefixIcon: Icon(icon, color: const Color(0xFF38BDF8), size: 19),
        suffixIcon: suffixIcon,
        contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: BorderSide(color: Colors.white.withAlpha(20)),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: BorderSide(color: Colors.white.withAlpha(25)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFF38BDF8), width: 1.8),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFEF4444)),
        ),
        focusedErrorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: const BorderSide(color: Color(0xFFEF4444), width: 1.8),
        ),
        errorStyle: const TextStyle(color: Color(0xFFFCA5A5), fontSize: 11),
      ),
    );
  }
}
