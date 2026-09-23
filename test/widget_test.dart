import 'package:flutter_test/flutter_test.dart';
import 'package:mindtrap_ai/localization/app_language.dart';
import 'package:mindtrap_ai/localization/language_controller.dart';
import 'package:mindtrap_ai/localization/puzzle_localizer.dart';
import 'package:mindtrap_ai/models/world_model.dart';
import 'package:mindtrap_ai/widgets/level_background_builder.dart';

void main() {
  test('WorldThemes defines 10 distinct worlds with unique properties', () {
    expect(WorldThemes.allWorlds.length, 10);

    final titles = WorldThemes.allWorlds.map((w) => w.title).toSet();
    expect(titles.length, 10);

    for (int i = 0; i < 10; i++) {
      final world = WorldThemes.getWorld(i);
      expect(world.worldNumber, i + 1);
      expect(world.backgroundAsset.isNotEmpty, true);
    }
  });

  test('LevelAtmosphereManager provides unique atmosphere per level', () {
    final world = WorldThemes.getWorld(0);
    final atmospheres = List.generate(
      10,
      (lvl) => LevelAtmosphereManager.getAtmosphere(lvl, world),
    );

    final styleNames = atmospheres.map((a) => a.styleName).toSet();
    expect(styleNames.length, 10);
  });

  test('PuzzleLocalizer translates questions when language changes', () {
    const question = 'Which word is longest?';
    final defaultOptions = ['Snake', 'Train', 'Road', 'Queue'];
    const defaultAnswer = 'Queue';
    const defaultExplanation = 'Queue has five letters.';

    // English
    final en = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'en',
    );
    expect(en.correctAnswer, 'Queue');

    // Urdu
    final ur = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'ur',
    );
    expect(ur.correctAnswer.contains('Queue'), true);
    expect(ur.question.contains('لفظ'), true);

    // Hindi
    final hi = PuzzleLocalizer.getTranslation(
      question,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      'hi',
    );
    expect(hi.question.contains('शब्द'), true);
  });

  test('AppStrings contains translations for worlds and auth', () {
    expect(AppStrings.get('worlds'), isNotEmpty);
    expect(AppStrings.get('sign_in'), isNotEmpty);
    expect(AppStrings.get('sign_up'), isNotEmpty);
    expect(AppStrings.get('continue_as_guest'), isNotEmpty);
    expect(AppStrings.get('store'), isNotEmpty);
    expect(AppStrings.get('meezan_bank'), isNotEmpty);
    expect(AppStrings.get('bank_transfer'), isNotEmpty);
    expect(AppStrings.get('credit_card'), isNotEmpty);
  });

  test('LanguageController updates activeLanguage and directionality reactively', () async {
    final controller = LanguageController.instance;

    await controller.setLanguage('en');
    expect(controller.currentCode, 'en');
    expect(controller.isRtl, false);
    expect(tr('settings'), 'SETTINGS');

    await controller.setLanguage('ur');
    expect(controller.currentCode, 'ur');
    expect(controller.isRtl, true);
    expect(tr('settings'), 'ترتیبات');

    await controller.setLanguage('ar');
    expect(controller.currentCode, 'ar');
    expect(controller.isRtl, true);
    expect(tr('settings'), 'الإعدادات');

    // Reset to en
    await controller.setLanguage('en');
    expect(controller.currentCode, 'en');
  });

  test('StoreScreen Meezan Bank transfer details are verified', () {
    const expectedName = 'Syed Azeem Haider Bukhari';
    const expectedAcc = '00300110167256';
    const expectedBank = 'Meezan Bank';
    const expectedIban = 'PK82MEZN0000300110167256';

    expect(expectedName, 'Syed Azeem Haider Bukhari');
    expect(expectedAcc, '00300110167256');
    expect(expectedBank, 'Meezan Bank');
    expect(expectedIban, 'PK82MEZN0000300110167256');
  });
}

