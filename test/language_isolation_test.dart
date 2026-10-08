import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:mindtrap_ai/main.dart';
import 'package:mindtrap_ai/localization/app_language.dart';
import 'package:mindtrap_ai/localization/language_controller.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() async {
    SharedPreferences.setMockInitialValues({});
    await GameStorage.load();
    LanguageController.instance.init('en');
  });

  test('Per-language level progress isolation and persistence', () async {
    // 1. Start in English
    await GameStorage.setSelectedLanguageCode('en');
    expect(GameStorage.selectedLanguageCode, 'en');

    // 2. Play 10 levels in English (levels 0 to 9 in stage 0)
    for (int i = 0; i < 10; i++) {
      await GameStorage.saveStageLevelStars(stageIndex: 0, levelIndex: i, stars: 3);
    }
    expect(GameStorage.starsForStageLevel(0, 0), 3);
    expect(GameStorage.starsForStageLevel(0, 9), 3);
    expect(GameStorage.isStageLevelUnlocked(0, 10), isTrue);
    expect(LevelSelectScreen.currentGlobalLevelIndex, 10);

    // 3. Switch to Urdu ('ur')
    await GameStorage.setSelectedLanguageCode('ur');
    expect(GameStorage.selectedLanguageCode, 'ur');
    expect(LanguageController.instance.currentCode, 'ur');

    // In Urdu, level progress should be fresh (level 0 / global level index 0)
    expect(GameStorage.stageLevelStars.isEmpty, isTrue);
    expect(GameStorage.starsForStageLevel(0, 0), 0);
    expect(GameStorage.isStageLevelUnlocked(0, 0), isTrue);
    expect(GameStorage.isStageLevelUnlocked(0, 1), isFalse);
    expect(LevelSelectScreen.currentGlobalLevelIndex, 0);

    // 4. Play 3 levels in Urdu
    for (int i = 0; i < 3; i++) {
      await GameStorage.saveStageLevelStars(stageIndex: 0, levelIndex: i, stars: 2);
    }
    expect(GameStorage.starsForStageLevel(0, 0), 2);
    expect(GameStorage.starsForStageLevel(0, 2), 2);
    expect(LevelSelectScreen.currentGlobalLevelIndex, 3);

    // 5. Switch back to English ('en')
    await GameStorage.setSelectedLanguageCode('en');
    expect(GameStorage.selectedLanguageCode, 'en');
    expect(GameStorage.starsForStageLevel(0, 0), 3);
    expect(GameStorage.starsForStageLevel(0, 9), 3);
    expect(LevelSelectScreen.currentGlobalLevelIndex, 10);

    // 6. Switch back to Urdu ('ur')
    await GameStorage.setSelectedLanguageCode('ur');
    expect(GameStorage.selectedLanguageCode, 'ur');
    expect(GameStorage.starsForStageLevel(0, 0), 2);
    expect(GameStorage.starsForStageLevel(0, 2), 2);
    expect(LevelSelectScreen.currentGlobalLevelIndex, 3);
  });

  test('Dynamic screen translations for achievements, stats, and daily challenge', () async {
    // English
    await GameStorage.setSelectedLanguageCode('en');
    expect(tr('total_achievements'), 'Total Achievements');
    expect(tr('total_score'), 'Total Score');
    expect(tr('daily_puzzle'), 'Daily Puzzle');

    // Urdu
    await GameStorage.setSelectedLanguageCode('ur');
    expect(tr('total_achievements'), 'کل کامیابیاں');
    expect(tr('total_score'), 'کل اسکور');
    expect(tr('daily_puzzle'), 'روزانہ کی پہیلی');

    // Spanish
    await GameStorage.setSelectedLanguageCode('es');
    expect(tr('total_achievements'), 'Logros Totales');
    expect(tr('total_score'), 'Puntuación Total');
    expect(tr('daily_puzzle'), 'Acertijo Diario');

    // French
    await GameStorage.setSelectedLanguageCode('fr');
    expect(tr('total_achievements'), 'Total des Succès');
    expect(tr('total_score'), 'Score Total');
    expect(tr('daily_puzzle'), 'Puzzle Quotidien');
  });
}
