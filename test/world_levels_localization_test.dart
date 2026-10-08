import 'package:flutter_test/flutter_test.dart';
import 'package:mindtrap_ai/localization/language_controller.dart';
import 'package:mindtrap_ai/widgets/level_background_builder.dart';
import 'package:mindtrap_ai/models/world_model.dart';

void main() {
  group('World Levels Screen Complete Multilingual Verification', () {
    test('Punjabi (pa) Level Titles, Atmosphere Styles and Lore are 100% native', () {
      LanguageController.instance.init('pa');
      final world0 = WorldThemes.allWorlds[0];

      // World titles and lore
      expect(world0.localizedTitle, isNot('Sunset Meadow'));
      expect(world0.localizedTitle, 'ਸੂਰਜ ਡੁੱਬਣ ਦਾ ਮੈਦਾਨ');
      expect(world0.localizedLore, isNot(contains('where foundational logic begins')));
      expect(world0.localizedLore, contains('ਖਿੜੇ'));

      // Level 1: Dawn Awaking -> ਸਵੇਰ ਦਾ ਜਾਗਣਾ
      final atm0 = LevelAtmosphereManager.getAtmosphere(0, world0);
      expect(atm0.localizedStyleName, isNot('Dawn Awaking'));
      expect(atm0.localizedStyleName, 'ਸਵੇਰ ਦਾ ਜਾਗਣਾ');

      // Level 2: Nebula Mist -> ਨੀਹਾਰਿਕਾ ਧੁੰਦ
      final atm1 = LevelAtmosphereManager.getAtmosphere(1, world0);
      expect(atm1.localizedStyleName, isNot('Nebula Mist'));
      expect(atm1.localizedStyleName, 'ਨੀਹਾਰਿਕਾ ਧੁੰਦ');

      // Level 3: Aurora Stream -> ਧਰੁਵੀ ਰੋਸ਼ਨੀ
      final atm2 = LevelAtmosphereManager.getAtmosphere(2, world0);
      expect(atm2.localizedStyleName, isNot('Aurora Stream'));
      expect(atm2.localizedStyleName, 'ਧਰੁਵੀ ਰੋਸ਼ਨੀ');
    });

    test('Hindi (hi) and Urdu (ur) Atmosphere Styles and Lore are 100% native', () {
      // Hindi
      LanguageController.instance.init('hi');
      final world0 = WorldThemes.allWorlds[0];
      expect(world0.localizedLore, isNot(contains('where foundational logic begins')));
      expect(world0.localizedTitle, 'सूर्यास्त का मैदान');
      final atmHi = LevelAtmosphereManager.getAtmosphere(0, world0);
      expect(atmHi.localizedStyleName, 'भोर का जागरण');

      // Urdu
      LanguageController.instance.init('ur');
      expect(world0.localizedLore, isNot(contains('where foundational logic begins')));
      expect(world0.localizedTitle, 'غروبِ آفتاب کا مرغزار');
      final atmUr = LevelAtmosphereManager.getAtmosphere(0, world0);
      expect(atmUr.localizedStyleName, 'طلوعِ سحر');
    });
  });
}
