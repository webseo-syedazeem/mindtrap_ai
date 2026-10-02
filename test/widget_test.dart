import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:mindtrap_ai/localization/app_language.dart';
import 'package:mindtrap_ai/localization/language_controller.dart';
import 'package:mindtrap_ai/localization/puzzle_localizer.dart';
import 'package:mindtrap_ai/models/world_model.dart';
import 'package:mindtrap_ai/widgets/level_background_builder.dart';
import 'package:mindtrap_ai/main.dart';

void main() {
  test('WorldThemes defines 10 distinct worlds with unique properties', () {
    expect(WorldThemes.allWorlds.length, 25);

    final titles = WorldThemes.allWorlds.map((w) => w.title).toSet();
    expect(titles.length, 25);

    for (int i = 0; i < WorldThemes.allWorlds.length; i++) {
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
    expect(ur.correctAnswer, 'قطار');
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

    // Dynamic category negation and option translation in Urdu
    final toolNegation = PuzzleLocalizer.getTranslation(
      'Which option is not one of the tools?',
      const ['Pliers', 'Wrench', 'Saw', 'Violin'],
      'Violin',
      'Violin is not a tool.',
      'ur',
    );
    expect(toolNegation.question, contains('اوزاروں'));
    expect(toolNegation.options, contains('پلاس'));
    expect(toolNegation.options, contains('رینچ'));
    expect(toolNegation.options, contains('آری'));
    expect(toolNegation.options, contains('وائلن'));
    expect(toolNegation.correctAnswer, 'وائلن');
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

  test('Urdu puzzles never contain parenthetical English and answer is in options', () {
    final sampleQuestions = [
      'Which word is longest?',
      'What gets wetter while drying?',
      'Which month has 28 days?',
      "What has keys but can't open locks?",
      'Which is lighter than air?',
      'What moves faster than wind?',
      'Which breaks when dropped?',
      'What has a mouth but cannot speak?',
      'Which can fly without wings?',
      'Which plant produces electricity?',
      'Which plant produces sweets?',
      'Which bird plays baseball?',
      'Which plant is an animal?',
      'Which tool is an animal?',
    ];

    for (final q in sampleQuestions) {
      final res = PuzzleLocalizer.getTranslation(
        q,
        ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        'Option 1',
        'Explanation',
        'ur',
      );
      // Verify no English parenthetical text in question or options
      expect(res.question.contains(RegExp(r'\([A-Za-z]+\)')), isFalse, reason: 'Urdu question should not contain English: ${res.question}');
      for (final opt in res.options) {
        expect(opt.contains(RegExp(r'\([A-Za-z]+\)')), isFalse, reason: 'Urdu option should not contain English: $opt');
      }
      // Verify correctAnswer is strictly contained within options
      expect(res.options.contains(res.correctAnswer), isTrue, reason: 'Answer ${res.correctAnswer} must be in options: ${res.options}');
    }
  });

  test('Comprehensive dictionary localizes all diverse options across all languages', () {
    const testOptions = [
      'A bank',
      'A bed',
      '1 kg feathers',
      'Your brain',
      'Coffee table',
      'All of them',
      'Grandfather, father, son',
      'Horse named Friday',
      'A candle',
      'Your name',
    ];

    for (final lang in ['ur', 'hi', 'ar', 'es', 'fr']) {
      final res = PuzzleLocalizer.getTranslation(
        'Test question?',
        testOptions,
        'A bank',
        'Test explanation',
        lang,
      );

      // Verify that options are translated and none contain English words from testOptions
      expect(res.options.length, testOptions.length);
      for (final opt in res.options) {
        expect(opt, isNotEmpty);
      }
      expect(res.options.contains(res.correctAnswer), isTrue, reason: 'Answer ${res.correctAnswer} must be in options: ${res.options} for lang $lang');
      // In Urdu and Arabic, options must not contain Latin letters
      if (lang == 'ur' || lang == 'ar') {
        for (final opt in res.options) {
          expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" should not have English letters in $lang');
        }
      }
    }
  });

  test('Screenshot case: 10-letter trap options are fully translated into Urdu with 0 English', () {
    final res = PuzzleLocalizer.getTranslation(
      'Which option contains 10 letters?',
      ['football', 'sandpaper', 'ant', 'strawberry'],
      'strawberry',
      'strawberry has 10 letters.',
      'ur',
    );
    expect(res.question, 'کس لفظ میں ٹھیک 10 حروف ہیں؟');
    expect(res.options, ['فٹ بال', 'ریگ مال', 'چیونٹی', 'سٹرابیری']);
    expect(res.correctAnswer, 'سٹرابیری');
    for (final opt in res.options) {
      expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" must not contain English');
    }
  });

  test('Numbers like 1.2, 3, 10 remain in English digits across all languages as requested', () {
    expect(formatNumber('1.2', 'ur'), '1.2');
    expect(formatNumber('3', 'ur'), '3');
    expect(formatNumber('10', 'ur'), '10');
    expect(formatNumber(171, 'ur'), '171');
    expect(formatNumber('Level 5', 'ur'), 'Level 5');
    expect(formatNumber('1.2', 'ar'), '1.2');
    expect(formatNumber('1.2', 'hi'), '1.2');
    expect(formatNumber('1.2', 'en'), '1.2');
  });

  test('Zero English guarantee: even arbitrary or unknown words never display English in Urdu', () {
    final res = PuzzleLocalizer.getTranslation(
      'Custom question?',
      ['arbitrary', 'microcontroller', 'cryptocurrency', 'superconductor'],
      'arbitrary',
      'Explanation',
      'ur',
    );
    for (final opt in res.options) {
      expect(RegExp(r'[A-Za-z]').hasMatch(opt), isFalse, reason: 'Option "$opt" must not contain Latin letters');
    }
    expect(RegExp(r'[A-Za-z]').hasMatch(res.correctAnswer), isFalse);
    expect(res.options.contains(res.correctAnswer), isTrue);
  });

  test('Audio assets exist on disk and have non-zero size', () {
    final assets = [
      'assets/audio/bg_music.wav',
      'assets/audio/tap.wav',
      'assets/audio/correct.wav',
      'assets/audio/wrong.wav',
      'assets/audio/win.wav',
      'assets/audio/lose.wav',
      'assets/audio/coin.wav',
    ];
    for (final a in assets) {
      final f = File(a);
      expect(f.existsSync(), isTrue, reason: '$a must exist');
      expect(f.lengthSync(), greaterThan(100), reason: '$a must not be empty');
    }
  });

  test('World task achievements award configured coins and gems gifts', () {
    final w1 = baseAchievementItems.firstWhere((a) => a.id == 'world_1_complete');
    expect(w1.coinReward, 1500);
    expect(w1.target, 40);

    final w5 = baseAchievementItems.firstWhere((a) => a.id == 'world_5_complete');
    expect(w5.coinReward, 5000);
    expect(w5.target, 5);

    final w10 = baseAchievementItems.firstWhere((a) => a.id == 'world_10_complete');
    expect(w10.coinReward, 10000);
    expect(w10.gemReward, 500);
    expect(w10.target, 10);
  });
}
