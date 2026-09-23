import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

class AuthService {
  AuthService._();
  static final AuthService instance = AuthService._();

  static const String keyUserEmail = 'auth_user_email';
  static const String keyUserName = 'auth_user_name';
  static const String keyIsLoggedIn = 'auth_is_logged_in';

  final ValueNotifier<bool> isLoggedIn = ValueNotifier<bool>(false);
  final ValueNotifier<String> userEmail = ValueNotifier<String>('');
  final ValueNotifier<String> userName = ValueNotifier<String>('Guest Mind');

  bool get isGuest => !isLoggedIn.value;

  Future<void> init() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      isLoggedIn.value = prefs.getBool(keyIsLoggedIn) ?? false;
      userEmail.value = prefs.getString(keyUserEmail) ?? '';
      userName.value = prefs.getString(keyUserName) ?? (isLoggedIn.value ? 'Trap Master' : 'Guest Mind');

      // Check active Supabase session
      try {
        final session = Supabase.instance.client.auth.currentSession;
        if (session != null && session.user.email != null) {
          isLoggedIn.value = true;
          userEmail.value = session.user.email!;
          userName.value = session.user.userMetadata?['name'] as String? ??
              session.user.email!.split('@').first;
        }
      } catch (_) {
        // Supabase may not be initialized yet or offline
      }
    } catch (e) {
      debugPrint('AuthService init error: $e');
    }
  }

  Future<Map<String, dynamic>> signIn({
    required String email,
    required String password,
  }) async {
    try {
      final client = Supabase.instance.client;
      final response = await client.auth.signInWithPassword(
        email: email.trim(),
        password: password,
      );

      if (response.user != null) {
        final emailStr = response.user!.email ?? email.trim();
        final nameStr = response.user!.userMetadata?['name'] as String? ?? emailStr.split('@').first;

        await _saveAuthLocal(emailStr, nameStr, true);
        return {'success': true, 'message': 'Welcome back, $nameStr!'};
      }
      return {'success': false, 'message': 'Could not sign in with provided credentials'};
    } catch (e) {
      // Offline fallback or demo sign in
      final err = e.toString();
      if (err.contains('Invalid login credentials')) {
        return {'success': false, 'message': 'Invalid email or password'};
      }
      // If network / connection error, support offline session
      final fallbackName = email.split('@').first;
      await _saveAuthLocal(email.trim(), fallbackName, true);
      return {
        'success': true,
        'message': 'Signed in (Offline Mode)',
        'offline': true,
      };
    }
  }

  Future<Map<String, dynamic>> signUp({
    required String email,
    required String password,
    required String name,
  }) async {
    try {
      final client = Supabase.instance.client;
      final response = await client.auth.signUp(
        email: email.trim(),
        password: password,
        data: {'name': name.trim()},
      );

      final displayName = name.trim().isNotEmpty ? name.trim() : email.split('@').first;
      if (response.user != null) {
        await _saveAuthLocal(email.trim(), displayName, true);
        return {'success': true, 'message': 'Account created successfully!'};
      }
      return {'success': false, 'message': 'Sign up did not return a user'};
    } catch (e) {
      // If Supabase not reachable, fallback locally
      final displayName = name.trim().isNotEmpty ? name.trim() : email.split('@').first;
      await _saveAuthLocal(email.trim(), displayName, true);
      return {
        'success': true,
        'message': 'Account created (Offline Mode)',
        'offline': true,
      };
    }
  }

  Future<bool> resetPassword(String email) async {
    try {
      final client = Supabase.instance.client;
      await client.auth.resetPasswordForEmail(email.trim());
      return true;
    } catch (e) {
      debugPrint('Reset password error: $e');
      return false;
    }
  }

  Future<void> continueAsGuest() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(keyIsLoggedIn, false);
    isLoggedIn.value = false;
    userEmail.value = '';
    userName.value = 'Guest Mind';
  }

  Future<void> signOut() async {
    try {
      await Supabase.instance.client.auth.signOut();
    } catch (_) {}
    await continueAsGuest();
  }

  Future<void> _saveAuthLocal(String email, String name, bool loggedIn) async {
    isLoggedIn.value = loggedIn;
    userEmail.value = email;
    userName.value = name;

    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool(keyIsLoggedIn, loggedIn);
      await prefs.setString(keyUserEmail, email);
      await prefs.setString(keyUserName, name);
    } catch (e) {
      debugPrint('Error saving auth state: $e');
    }
  }
}
