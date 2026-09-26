import 'package:flutter/material.dart';
import 'app_language.dart';

class LanguageController {
  LanguageController._();
  static final LanguageController instance = LanguageController._();

  final ValueNotifier<String> activeLanguage = ValueNotifier<String>('en');

  String get currentCode => activeLanguage.value;

  static const Set<String> rtlLanguageCodes = {'ur', 'ar', 'fa', 'ps', 'sd', 'he'};

  bool get isRtl => rtlLanguageCodes.contains(activeLanguage.value);

  TextDirection get directionality => isRtl ? TextDirection.rtl : TextDirection.ltr;

  AppLanguage get currentLanguage {
    return AppStrings.supportedLanguages.firstWhere(
      (lang) => lang.code == activeLanguage.value,
      orElse: () => AppStrings.supportedLanguages.first,
    );
  }

  Future<void> Function(String code)? onLanguageSaved;

  void init(String? savedCode) {
    final code = (savedCode != null && savedCode.isNotEmpty) ? savedCode : 'en';
    AppStrings.currentCode = code;
    activeLanguage.value = code;
  }

  Future<void> setLanguage(String code, {Future<void> Function(String)? onSave}) async {
    AppStrings.currentCode = code;
    activeLanguage.value = code;
    if (onSave != null) {
      await onSave(code);
    } else if (onLanguageSaved != null) {
      await onLanguageSaved!(code);
    }
  }

  /// Formats numbers to standard digits as requested by user
  static String formatNumber(dynamic value, [String? langCode]) {
    if (value == null) return '';
    return value.toString();
  }
}

/// Convenience global helper to format numbers according to active language
String formatNumber(dynamic value, [String? langCode]) =>
    LanguageController.formatNumber(value, langCode);
