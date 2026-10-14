import 'package:flutter/material.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';

class WorldData {
  final int id; // 0 to 24 (25 worlds total)
  final String title;
  final String subtitle;
  final String lore;
  final String backgroundAsset;
  final Color primaryColor;
  final Color secondaryColor;
  final Color glowColor;
  final Color cardGradientStart;
  final Color cardGradientEnd;
  final IconData icon;
  final int requiredStarsToUnlock;
  final int levelsCount;

  const WorldData({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.lore,
    required this.backgroundAsset,
    required this.primaryColor,
    required this.secondaryColor,
    required this.glowColor,
    required this.cardGradientStart,
    required this.cardGradientEnd,
    required this.icon,
    this.requiredStarsToUnlock = 0,
    this.levelsCount = 40,
  });

  int get worldNumber => id + 1;
  int get maxStars => levelsCount * 3;

  String get localizedTitle {
    final key = 'world_${id}_title';
    final val = tr(key);
    final code = LanguageController.instance.currentCode;
    if (val != key && val.isNotEmpty) {
      if (code == 'en' || val != title) {
        return val;
      }
    }
    return _getWorldTitle(id, code) ?? title;
  }

  String get localizedSubtitle {
    final key = 'world_${id}_subtitle';
    final val = tr(key);
    final code = LanguageController.instance.currentCode;
    if (val != key && val.isNotEmpty) {
      if (code == 'en' || val != subtitle) {
        return val;
      }
    }
    return _getWorldSubtitle(id, code) ?? subtitle;
  }

  String get localizedLore {
    final key = 'world_${id}_lore';
    final val = tr(key);
    final code = LanguageController.instance.currentCode;
    if (val != key && val.isNotEmpty) {
      if (code == 'en' || val != lore) {
        return val;
      }
    }
    return _getWorldLore(id, code) ?? lore;
  }

  static String? _getWorldTitle(int id, String code) {
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      const urTitles = [
        'غروبِ آفتاب کا مرغزار',
        'روشن جنگل',
        'استوائی جھیل',
        'ساکورا پناہ گاہ',
        'یاسمینی شام',
        'خزاں کا مسکن',
        'الپائن گلیشیئرز',
        'وادیِ گل',
        'طلسماتی وادی',
        'فلکی بلندی',
        'سنہری افق',
        'کوانٹم کہکشاں',
        'قطبی شفق',
        'سرخ کھائی',
        'تاریک دنیا',
        'پراسرار جنگل',
        'یاقوتی غار',
        'نیون گرڈ',
        'ریتیلے ٹیلے',
        'برفانی خلیج',
        'مونگے کی دنیا',
        'صبحِ ساکورا',
        'طوفانی چٹان',
        'ستاروں کا قلعہ',
        'دانش کا مرکز',
      ];
      if (id >= 0 && id < urTitles.length) return urTitles[id];
    } else if (code == 'ar') {
      const arTitles = [
        'مرج الغروب',
        'الغابة المضيئة',
        'البحيرة الاستوائية',
        'ملاذ ساكورا',
        'شفق اللافندر',
        'ملاذ الخريف',
        'أنهار الجليد الألبية',
        'وادي الزهور',
        'المملكة الساحرة',
        'قمة السماء',
        'الأفق الذهبي',
        'سديم الكم',
        'الشفق المنشوري',
        'الهاوية القرمزية',
        'عالم الظلال',
        'المظلة الغامضة',
        'جيود الكريستال',
        'شبكة النيون',
        'كثبان الغروب',
        'مضيق جليدي',
        'أوديسة المرجان',
        'فجر ساكورا',
        'صخرة الرعد',
        'قلعة ضوء النجوم',
        'مركز الإدراك المطلق',
      ];
      if (id >= 0 && id < arTitles.length) return arTitles[id];
    } else if (code == 'hi' || code == 'bn') {
      const hiTitles = [
        'सूर्यास्त का मैदान',
        'धूप से खिली वनभूमि',
        'उष्णकटिबंधीय लैगून',
        'साकुरा अभयारण्य',
        'लैवेंडर गोधूलि',
        'शरद ऋतु का आश्रय',
        'अल्पाइन हिमनद',
        'कुसुम घाटी',
        'मंत्रमुग्ध क्षेत्र',
        'आकाशीय शिखर',
        'स्वर्णिम क्षितिज',
        'क्वांटम नेबुला',
        'प्रिज्मीय ऑरोरा',
        'गहरा रक्तिम गर्त',
        'छाया लोक',
        'रहस्यमयी वन',
        'क्रिस्टल गुफा',
        'नियॉन ग्रिड',
        'सूर्यास्त के टीले',
        'हिमानी संकरा समुद्र',
        'मूंगा सागर यात्रा',
        'साकुरा भोर',
        'वज्र शिखर',
        'तारामंडल गढ़',
        'अनंत ज्ञान केंद्र',
      ];
      if (id >= 0 && id < hiTitles.length) return hiTitles[id];
    } else if (code == 'es' || code == 'pt') {
      const esTitles = [
        'Prado del Ocaso',
        'Bosque Soleado',
        'Laguna Tropical',
        'Santuario Sakura',
        'Crepúsculo Lavanda',
        'Refugio Otoñal',
        'Glaciares Alpinos',
        'Valle Florido',
        'Reino Encantado',
        'Cénit Celestial',
        'Horizonte Dorado',
        'Nebulosa Cuántica',
        'Aurora Prismática',
        'Abismo Carmesí',
        'Reino de las Sombras',
        'Dosel Místico',
        'Geoda de Cristal',
        'Matriz Neón',
        'Dunas del Ocaso',
        'Fiordo Glacial',
        'Odisea de Coral',
        'Amanecer Sakura',
        'Risco del Trueno',
        'Ciudadela Estelar',
        'Núcleo Infinito',
      ];
      if (id >= 0 && id < esTitles.length) return esTitles[id];
    } else if (code == 'pa') {
      const paTitles = [
        'ਸੂਰਜ ਡੁੱਬਣ ਦਾ ਮੈਦਾਨ',
        'ਚਮਕਦਾ ਜੰਗਲ',
        'ਗਰਮ ਖੰਡੀ ਝੀਲ',
        'ਸਾਕੁਰਾ ਪਨਾਹਗਾਹ',
        'ਜਾਮਣੀ ਸ਼ਾਮ',
        'ਪਤਝੜ ਦਾ ਨਿਵਾਸ',
        'ਐਲਪਾਈਨ ਗਲੇਸ਼ੀਅਰ',
        'ਫੁੱਲਾਂ ਦੀ ਵਾਦੀ',
        'ਜਾਦੂਈ ਦੁਨੀਆ',
        'ਅਸਮਾਨੀ ਸਿਖਰ',
        'ਸੁਨਹਿਰੀ ਦਿਸਹੱਦਾ',
        'ਕੁਆਂਟਮ ਨੀਹਾਰਿਕਾ',
        'ਰੰਗੀਨ ਧਰੁਵੀ ਰੋਸ਼ਨੀ',
        'ਲਾਲ ਖੱਡ',
        'ਪਰਛਾਵਿਆਂ ਦੀ ਦੁਨੀਆ',
        'ਰਹੱਸਮਈ ਜੰਗਲ',
        'ਕ੍ਰਿਸਟਲ ਗੁਫ਼ਾ',
        'ਨੀਓਨ ਮੈਟ੍ਰਿਕਸ',
        'ਰੇਤ ਦੇ ਟਿੱਬੇ',
        'ਬਰਫ਼ਾਨੀ ਖਾੜੀ',
        'ਮੂੰਗਾ ਯਾਤਰਾ',
        'ਸਾਕੁਰਾ ਸਵੇਰ',
        'ਤੂਫ਼ਾਨੀ ਚੱਟਾਨ',
        'ਤਾਰਿਆਂ ਦਾ ਕਿਲ੍ਹਾ',
        'ਬੇਅੰਤ ਬੁੱਧੀ ਕੇਂਦਰ',
      ];
      if (id >= 0 && id < paTitles.length) return paTitles[id];
    }
    return null;
  }

  static String? _getWorldSubtitle(int id, String code) {
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      const urSubtitles = [
        'سنہری صبح',
        'سرگوشی کرتے چیڑ کے درخت',
        'ساحلِ غروب',
        'ماؤنٹ فیوجی کا شفق',
        'جگنوؤں کی وادی',
        'سنہری ندی',
        'کرسٹل چوٹیاں',
        'بہار کے مرغزار',
        'پراسرار شفق',
        'آسمانی دنیا',
        'شمسی مینار',
        'کائناتی غبار',
        'قطبی روشنیاں',
        'آتشیں مرکز',
        'چاندی کا گرہن',
        'قدیم باغ',
        'جامنی گہرائیاں',
        'سائبر منطق',
        'صحرائی سراب',
        'برفانی پناہ گاہ',
        'غرقاب چٹان',
        'روحانی گلشن',
        'برقی چوٹی',
        'کہکشانی ایوان',
        'دانش کا مرکز',
      ];
      if (id >= 0 && id < urSubtitles.length) return urSubtitles[id];
    } else if (code == 'hi' || code == 'bn') {
      const hiSubtitles = [
        'स्वर्णिम सूर्योदय',
        'सरसराहट देवदार',
        'सूर्यास्त तट',
        'फूजी संध्या',
        'जुगनू घाटी',
        'स्वर्ण जलधारा',
        'स्फटिक चोटियां',
        'वसंत का मैदान',
        'गोधूलि रहस्य',
        'दिव्य लोक',
        'सौर मीनार',
        'ब्रह्मांडीय धूल',
        'ध्रुवीय ज्योति',
        'ज्वालामुखी केंद्र',
        'रजत ग्रहण',
        'प्राचीन उपवन',
        'नीलमणि गहराई',
        'साइबर ग्रिड',
        'मरुस्थल मरीचिका',
        'हिम अभयारण्य',
        'जलमग्न शैल',
        'आत्मिक उद्यान',
        'तूफानी शिखर',
        'तारकीय मंडप',
        'संज्ञानात्मक केंद्र',
      ];
      if (id >= 0 && id < hiSubtitles.length) return hiSubtitles[id];
    } else if (code == 'pa') {
      const paSubtitles = [
        'ਸੁਨਹਿਰੀ ਸਵੇਰ',
        'ਸਰਗੋਸ਼ੀ ਚੀੜ੍ਹ',
        'ਸੂਰਜ ਡੁੱਬਣ ਦਾ ਕੰਢਾ',
        'ਫੂਜੀ ਸੰਝ',
        'ਜੁਗਨੂੰ ਵਾਦੀ',
        'ਸੁਨਹਿਰੀ ਨਦੀ',
        'ਕ੍ਰਿਸਟਲ ਚੋਟੀਆਂ',
        'ਬਸੰਤ ਦਾ ਮੈਦਾਨ',
        'ਸੰਝ ਦਾ ਭੇਤ',
        'ਅਰਸ਼ੀ ਦੁਨੀਆ',
        'ਸੂਰਜੀ ਮੀਨਾਰ',
        'ਬ੍ਰਹਿਮੰਡੀ ਧੂੜ',
        'ਧਰੁਵੀ ਰੋਸ਼ਨੀਆਂ',
        'ਲਾਵਾ ਕੇਂਦਰ',
        'ਚਾਂਦੀ ਗ੍ਰਹਿਣ',
        'ਪੁਰਾਤਨ ਬਾਗ਼',
        'ਜਾਮਣੀ ਗਹਿਰਾਈਆਂ',
        'ਸਾਈਬਰ ਗਰਿੱਡ',
        'ਮਾਰੂਥਲ ਮ੍ਰਿਗਤ੍ਰਿਸ਼ਨਾ',
        'ਬਰਫ਼ਾਨੀ ਪਨਾਹਗਾਹ',
        'ਡੁੱਬੀ ਹੋਈ ਚੱਟਾਨ',
        'ਰੂਹਾਨੀ ਬਗ਼ੀਚਾ',
        'ਤੂਫ਼ਾਨੀ ਚੋਟੀ',
        'ਤਾਰਾਮੰਡਲ ਹਾਲ',
        'ਸੋਚ ਦਾ ਧੁਰਾ',
      ];
      if (id >= 0 && id < paSubtitles.length) return paSubtitles[id];
    } else if (code == 'ar') {
      const arSubtitles = [
        'شروق ذهبي',
        'صنوبر هامس',
        'شاطئ الغروب',
        'غروب فوجي',
        'وادي اليراعات',
        'جدول ذهبي',
        'قمم الكريستال',
        'مرج الربيع',
        'غموض الشفق',
        'عالم سماوي',
        'برج شمسي',
        'غبار كوني',
        'أضواء قطبية',
        'قلب حجر السج',
        'كسوف فضي',
        'بستان عتيق',
        'أعماق الجمشت',
        'شبكة سيبرانية',
        'سراب الصحراء',
        'ملاذ الصقيع',
        'شعاب مغمورة',
        'حديقة الروح',
        'قمة العاصفة',
        'قاعة فلكية',
        'مركز الإدراك',
      ];
      if (id >= 0 && id < arSubtitles.length) return arSubtitles[id];
    } else if (code == 'es' || code == 'pt') {
      const esSubtitles = [
        'Amanecer Dorado',
        'Pinos Susurrantes',
        'Playa del Ocaso',
        'Ocaso en Fuji',
        'Valle de Luciérnagas',
        'Arroyo Dorado',
        'Picos de Cristal',
        'Pradera Primaveral',
        'Misterio Crepuscular',
        'Reino Celestial',
        'Aguja Solar',
        'Polvo Cósmico',
        'Luces del Norte',
        'Núcleo de Obsidiana',
        'Eclipse Plateado',
        'Arboleda Ancestral',
        'Profundidades Amatista',
        'Red Cibernética',
        'Espejismo del Desierto',
        'Santuario Helado',
        'Arrecife Hundido',
        'Jardín Espiritual',
        'Cúspide de Tormenta',
        'Salón Astral',
        'Núcleo Cognitivo',
      ];
      if (id >= 0 && id < esSubtitles.length) return esSubtitles[id];
    }
    return null;
  }

  static String? _getWorldLore(int id, String code) {
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      const urLores = [
        'کھلے ہوئے جنگلی پھولوں کی پہاڑیوں میں سنہری دھوپ کا لطف اٹھائیں جہاں بنیادی منطق شروع ہوتی ہے۔',
        'مسحور کن صنوبر کے باغات سے گزریں جہاں صبح کی دھند میں سنہری کرنیں چمکتی ہیں۔',
        'سنہری ریت پر چہل قدمی کریں جہاں سمندر کی گرم لہریں غروب کے دلکش رنگ بکھیرتی ہیں۔',
        'برف پوش چوٹیوں کے نیچے جھیلوں میں چیری کے پھولوں کی پنکھڑیوں کے رقص کا نظارہ کریں۔',
        'رقص کرتے جگنوؤں سے روشن لامتناہی لیوینڈر کے کھیتوں میں اپنے ذہن کو تازہ دم کریں۔',
        'سنہری برچ کے جنگل سے گزرتی شفاف ندی کے ساتھ پرسکون پہاڑی پناہ گاہ تک پہنچیں۔',
        'برفیلے گلیشیئرز کی چوٹیوں کو سر کریں جہاں ہر زاویہ شفاف شعاعوں سے چمکتا ہے۔',
        'پھولوں سے لدی بہار کی وادی میں اپنے ذہن کی حسِ ادراک کو نکھاریں۔',
        'طلسماتی درختوں کی چھاؤں میں پوشیدہ حکمت کے اسرار دریافت کریں۔',
        'بادلوں سے اوپر بلند فکری منزلوں کو چھوئیں جہاں ذہانت کا عروج ہے۔',
        'سنہری افق پر طلوع ہوتے سورج کے ساتھ لامحدود ذہنی توانائی حاصل کریں۔',
        'کہکشاؤں کے دائروں میں الجھی پہیلیوں کو فہم و فراست سے سلجھائیں۔',
        'شمالی قطب کے رنگ برنگے شفق کے نیچے روشن خیالی کا سفر طے کریں۔',
        'سرخ انگاروں کی طرح چمکتی گہرائیوں میں منطق کی گتھیاں سلجھائیں۔',
        'چاندی جیسی روشن راتوں میں پوشیدہ پہیلیوں کو بے نقاب کریں۔',
        'قدیم درختوں کے سائے میں چھپی پراسرار سچائیاں تلاش کریں۔',
        'نیلم اور یاقوت جیسے چمکتے کرسٹل پتھروں کی منطقی صف بندی کریں۔',
        'سائبر اسپیس کے پیچیدہ جالوں اور سرکٹس میں درست راستے چنیں۔',
        'سنہری ریت کے لہراتے صحرائی سرابوں میں حقیقت کو پرکھیں۔',
        'برفانی جھیلوں کے شفاف آئینوں میں دانش کے عکس تلاش کریں۔',
        'سمندر کی نیلگوں لہروں تلے رنگین مونگوں میں منطق کے موتی چنیں۔',
        'روح پرور گلشن میں صبح کی شبنم کے ساتھ فکری تروتازگی پائیں۔',
        'گرج چمک اور بجلی کے طوفانوں میں برق رفتار فیصلے کریں۔',
        'ستاروں بھرے آسمانی ایوان میں کائنات کے سربستہ راز پائیں۔',
        'مائنڈ ٹریپ کا سب سے بلند اور اعلیٰ ترین مقام، جہاں سوچ کی کوئی حد نہیں۔',
      ];
      if (id >= 0 && id < urLores.length) return urLores[id];
    } else if (code == 'hi' || code == 'bn') {
      const hiLores = [
        'जंगली फूलों की पहाड़ियों में धूप का आनंद लें जहां मौलिक तर्क शुरू होता है।',
        'चीड़ के देवदार वनों से गुजरें जहां सुबह की धुंध में सुनहरी किरणें चमकती हैं।',
        'रेतीले तट पर टहलें जहां सागर की गर्म लहरें मनमोहक रंग बिखेरती हैं।',
        'बर्फ से ढकी चोटियों के नीचे चेरी के फूलों की पंखुड़ियों का नृत्य देखें।',
        'जुगनुओं से रोशन लैवेंडर के खेतों में अपने मस्तिष्क को तरोताजा करें।',
        'सुनहरे बर्च वन से गुजरती स्वच्छ जलधारा के साथ शांत आश्रय तक पहुंचें।',
        'हिमनदों की चोटियों पर विजय प्राप्त करें जहां हर कोण प्रकाश से चमकता है।',
        'फूलों से भरी वसंत की घाटी में अपनी मानसिक तीक्ष्णता को निखारें।',
        'मंत्रमुग्ध पेड़ों की छांव में छिपे ज्ञान के रहस्य खोजें।',
        'बादलों से ऊपर ज्ञान की ऊंचाइयों को छुएं जहां बुद्धिमत्ता का शिखर है।',
        'स्वर्णिम क्षितिज पर सूर्योदय के साथ असीम मानसिक ऊर्जा प्राप्त करें।',
        'गहरे अंतरिक्ष के चक्रवातों में उलझी पहेलियों को समझदारी से सुलझाएं।',
        'उत्तरी ध्रुव की रंगीन रोशनी के नीचे उज्ज्वल चिंतन की यात्रा करें।',
        'दहकते लावा की गहराइयों में अपनी तार्किक क्षमता का परीक्षण करें।',
        'चांदी जैसी रातों में छिपी पहेलियों को उजागर करें।',
        'प्राचीन वृक्षों की छाया में छुपे गहरे रहस्यों को जानें।',
        'चमकते क्रिस्टल रत्नों का तार्किक क्रमबद्ध संयोजन करें।',
        'साइबर स्पेस के जटिल नेटवर्क और सर्किट में सही रास्ते चुनें।',
        'रेत के टीलों में लहराते मरुस्थल के भ्रम में सच्चाई को पहचानें।',
        'बर्फानी झीलों के स्वच्छ दर्पण में ज्ञान की परछाइयां तलाशें।',
        'समुद्र की लहरों के नीचे रंग-बिरंगे मूंगों में ज्ञान के मोती चुनें।',
        'पवित्र उद्यान में सुबह की ओस के साथ नई मानसिक ताजगी पाएं।',
        'गरजती बिजली और तूफानों में त्वरित और सटीक निर्णय लें।',
        'तारों भरे आकाश में ब्रह्मांड के अनसुलझे रहस्य खोजें।',
        'माइंडट्रैप का सर्वोच्च शिखर, जहां सोचने की कोई सीमा नहीं है।',
      ];
      if (id >= 0 && id < hiLores.length) return hiLores[id];
    } else if (code == 'pa') {
      const paLores = [
        'ਖਿੜੇ ਜੰਗਲੀ ਫੁੱਲਾਂ ਦੀਆਂ ਪਹਾੜੀਆਂ ਵਿੱਚ ਸੁਨਹਿਰੀ ਧੁੱਪ ਦਾ ਆਨੰਦ ਲਓ ਜਿੱਥੇ ਤਰਕ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ।',
        'ਚੀੜ ਦੇ ਬਾਗ਼ਾਂ ਵਿੱਚੋਂ ਲੰਘੋ ਜਿੱਥੇ ਸਵੇਰ ਦੀ ਧੁੰਦ ਵਿੱਚ ਕਿਰਨਾਂ ਚਮਕਦੀਆਂ ਹਨ।',
        'ਸੁਨਹਿਰੀ ਰੇਤ ਤੇ ਸੈਰ ਕਰੋ ਜਿੱਥੇ ਲਹਿਰਾਂ ਮਨਮੋਹਕ ਰੰਗ ਬਿਖੇਰਦੀਆਂ ਹਨ।',
        'ਬਰਫ਼ ਨਾਲ ਢਕੀਆਂ ਚੋਟੀਆਂ ਹੇਠ ਚੈਰੀ ਦੇ ਫੁੱਲਾਂ ਦਾ ਨਾਚ ਦੇਖੋ।',
        'ਜੁਗਨੂੰਆਂ ਨਾਲ ਰੋਸ਼ਨ ਲਵੈਂਡਰ ਦੇ ਖੇਤਾਂ ਵਿੱਚ ਦਿਮਾਗ਼ ਨੂੰ ਤਰੋਤਾਜ਼ਾ ਕਰੋ।',
        'ਸੁਨਹਿਰੀ ਜੰਗਲ ਦੀ ਸਾਫ਼ ਨਦੀ ਦੇ ਨਾਲ ਸ਼ਾਂਤ ਪਨਾਹਗਾਹ ਤੱਕ ਪਹੁੰਚੋ।',
        'ਗਲੇਸ਼ੀਅਰਾਂ ਦੀਆਂ ਚੋਟੀਆਂ ਸਰ ਕਰੋ ਜਿੱਥੇ ਹਰ ਕੋਣ ਚਮਕਦਾ ਹੈ।',
        'ਫੁੱਲਾਂ ਨਾਲ ਭਰੀ ਬਸੰਤ ਦੀ ਵਾਦੀ ਵਿੱਚ ਆਪਣੀ ਸੋਚ ਨੂੰ ਨਿਖਾਰੋ।',
        'ਜਾਦੂਈ ਰੁੱਖਾਂ ਦੀ ਛਾਂ ਵਿੱਚ ਛੁਪੇ ਗਿਆਨ ਦੇ ਭੇਤ ਲੱਭੋ।',
        'ਬੱਦਲਾਂ ਤੋਂ ਉੱਚੀਆਂ ਮੰਜ਼ਿਲਾਂ ਨੂੰ ਛੂਹੋ ਜਿੱਥੇ ਬੁੱਧੀ ਦਾ ਸਿਖਰ ਹੈ।',
        'ਸੁਨਹਿਰੀ ਦਿਸਹੱਦੇ ਤੇ ਬੇਅੰਤ ਮਾਨਸਿਕ ਊਰਜਾ ਪ੍ਰਾਪਤ ਕਰੋ।',
        'ਡੂੰਘੇ ਪੁਲਾੜ ਦੇ ਗੇੜਿਆਂ ਵਿੱਚ ਉਲਝੀਆਂ ਬੁਝਾਰਤਾਂ ਸੁਲਝਾਓ।',
        'ਧਰੁਵੀ ਰੋਸ਼ਨੀਆਂ ਹੇਠ ਗਿਆਨ ਦੀ ਯਾਤਰਾ ਕਰੋ।',
        'ਲਾਵੇ ਦੀਆਂ ਗਹਿਰਾਈਆਂ ਵਿੱਚ ਤਰਕ ਦੀਆਂ ਗੰਢਾਂ ਖੋਲ੍ਹੋ।',
        'ਚਾਂਦੀ ਵਰਗੀਆਂ ਰਾਤਾਂ ਵਿੱਚ ਛੁਪੇ ਰਹੱਸ ਉਜਾਗਰ ਕਰੋ।',
        'ਪੁਰਾਤਨ ਰੁੱਖਾਂ ਦੇ ਪਰਛਾਵਿਆਂ ਵਿੱਚ ਸੱਚਾਈਆਂ ਲੱਭੋ।',
        'ਚਮਕਦੇ ਕ੍ਰਿਸਟਲ ਪੱਥਰਾਂ ਦੀ ਤਰਕਸੰਗਤ ਵਿਵਸਥਾ ਕਰੋ।',
        'ਸਾਈਬਰ ਨੈੱਟਵਰਕਾਂ ਵਿੱਚ ਸਹੀ ਰਸਤੇ ਚੁਣੋ।',
        'ਰੇਤ ਦੇ ਟਿੱਬਿਆਂ ਵਿੱਚ ਮ੍ਰਿਗਤ੍ਰਿਸ਼ਨਾ ਪਰਖੋ।',
        'ਬਰਫ਼ਾਨੀ ਝੀਲਾਂ ਵਿੱਚ ਗਿਆਨ ਦੇ ਪ੍ਰਤੀਬਿੰਬ ਲੱਭੋ।',
        'ਸਮੁੰਦਰ ਦੀਆਂ ਲਹਿਰਾਂ ਹੇਠ ਮੂੰਗੇ ਦੇ ਮੋਤੀ ਚੁਣੋ।',
        'ਰੂਹਾਨੀ ਬਗ਼ੀਚੇ ਵਿੱਚ ਸਵੇਰ ਦੀ ਤਾਜ਼ਗੀ ਪਾਓ।',
        'ਤੂਫ਼ਾਨਾਂ ਵਿੱਚ ਤੇਜ਼ ਅਤੇ ਸਹੀ ਫ਼ੈਸਲੇ ਕਰੋ।',
        'ਤਾਰਿਆਂ ਭਰੇ ਹਾਲ ਵਿੱਚ ਬ੍ਰਹਿਮੰਡ ਦੇ ਭੇਤ ਜਾਣੋ।',
        'ਮਾਈਂਡਟ੍ਰੈਪ ਦਾ ਸਭ ਤੋਂ ਉੱਚਾ ਸਿਖਰ, ਜਿੱਥੇ ਸੋਚ ਦੀ ਕੋਈ ਹੱਦ ਨਹੀਂ।',
      ];
      if (id >= 0 && id < paLores.length) return paLores[id];
    } else if (code == 'ar') {
      const arLores = [
        'استمتع بأشعة الشمس الذهبية على تلال الزهور البرية حيث يبدأ المنطق الأساسي.',
        'تجول عبر بساتين الصنوبر الهامسة حيث تتلألأ أشعة الفجر في الضباب الصباحي.',
        'امشِ على الرمال الدافئة حيث تلون أمواج المحيط غروب الشمس بألوان خلابة.',
        'شاهد بتلات الكرز تتراقص فوق البحيرات الصافية تحت قمم الجبال المغطاة بالثلوج.',
        'أنعش عقلك في حقول اللافندر اللانهائية المضاءة برقصات اليراعات المتوهجة.',
        'اتبع الجدول المتدفق عبر غابات البتولا الذهبية إلى ملاذ جبلي هادئ.',
        'اصعد قمم الأنهار الجليدية البلورية حيث تتألق كل زاوية بانعكاسات نقية.',
        'اشحذ قدراتك الإدراكية وأنت تعبر المروج الخضراء المليئة بزهور الربيع.',
        'اكتشف أسرار الحكمة المخفية تحت ظلال أشجار البلوط السحرية القديمة.',
        'تجاوز السحاب إلى آفاق فكرية جديدة حيث يتألق الفكر الإنساني في أبهى صوره.',
        'استمد طاقة عقلية متجددة مع إشراقة شمس الأفق الذهبي التي لا تنتهي.',
        'حل الألغاز الكونية المعقدة في دوامات السديم العميق بتفكير عميق ومنطقي.',
        'سافر تحت أشرطة الشفق القطبي الملونة وتأمل أسرار الطبيعة الخلابة.',
        'انزل إلى أعماق الأرض وتجاوز التحديات الصعبة بهدوء وثبات فكري.',
        'اكشف الأسرار الليلية الغامضة تحت هالة القمر المضيئة في الغابات الفضية.',
        'ادخل البساتين العريقة واكتشف الحقائق الدفينة بين أشجار السيكويا العملاقة.',
        'رتب البلورات البنفسجية في تناغم هندسي يبرز دقة المنطق والترتيب.',
        'تنقل عبر شبكات السيبراني المعقدة واختر المسارات المنطقية الصحيحة.',
        'تأمل الكثبان الرملية الذهبية وميز الحقيقة من السراب بدقة الملاحظة.',
        'سر عبر المضائق الجليدية الزرقاء واكتشف انعكاسات الحكمة في مرآة الجليد.',
        'اغطس في أعماق المحيط الفيروزي واستخرج لآلئ المنطق بين الشعاب المرجانية.',
        'تأمل في حدائق الروح الهادئة مع قطرات الندى الصباحية لتصفية الذهن.',
        'اتخذ قرارات حاسمة وسريعة وسط عواصف البرق والرعد العاتية.',
        'قف في القاعة الفلكية المرصعة بالنجوم وشاهد حركة المجرات اللانهائية.',
        'أعلى قمة في مايند تراب ذكاء اصطناعي، حيث لا حدود لقدرات العقل والتفكير.',
      ];
      if (id >= 0 && id < arLores.length) return arLores[id];
    }
    return null;
  }
}

class WorldThemes {
  WorldThemes._();

  static const int levelsPerWorld = 40;
  static const int totalWorldsCount = 25;
  static const int totalLevelsCount = 1000; // 25 worlds * 40 levels = 1,000 levels!

  static const List<WorldData> allWorlds = [
    // ── World 1: Levels 1 - 40 ──────────────────────────────────────────────
    WorldData(
      id: 0,
      title: 'Sunset Meadow',
      subtitle: 'Golden Dawn',
      lore: 'Bask in golden sunlight across blooming wildflower hills where foundational logic begins.',
      backgroundAsset: 'assets/images/Stage-1.webp',
      primaryColor: Color(0xFFFF9E00),
      secondaryColor: Color(0xFFFF5400),
      glowColor: Color(0xFFFFD166),
      cardGradientStart: Color(0x992B1500),
      cardGradientEnd: Color(0xCC110800),
      icon: Icons.wb_sunny_rounded,
      requiredStarsToUnlock: 0,
    ),

    // ── World 2: Levels 41 - 80 ─────────────────────────────────────────────
    WorldData(
      id: 1,
      title: 'Sunlit Forest',
      subtitle: 'Whispering Pines',
      lore: 'Traverse enchanted pine groves where golden sunbeams pierce morning mist.',
      backgroundAsset: 'assets/images/Stage-2.webp',
      primaryColor: Color(0xFF10B981),
      secondaryColor: Color(0xFF059669),
      glowColor: Color(0xFF34D399),
      cardGradientStart: Color(0x99042617),
      cardGradientEnd: Color(0xCC01120A),
      icon: Icons.forest_rounded,
      requiredStarsToUnlock: 10,
    ),

    // ── World 3: Levels 81 - 120 ────────────────────────────────────────────
    WorldData(
      id: 2,
      title: 'Tropical Lagoon',
      subtitle: 'Sunset Coast',
      lore: 'Stroll pristine sands where warm ocean waves reflect brilliant sunset colors.',
      backgroundAsset: 'assets/images/Stage-3.webp',
      primaryColor: Color(0xFF00C9FF),
      secondaryColor: Color(0xFFFF6B6B),
      glowColor: Color(0xFF48CAE4),
      cardGradientStart: Color(0x99062E3B),
      cardGradientEnd: Color(0xCC02141A),
      icon: Icons.beach_access_rounded,
      requiredStarsToUnlock: 25,
    ),

    // ── World 4: Levels 121 - 160 ───────────────────────────────────────────
    WorldData(
      id: 3,
      title: 'Sakura Sanctuary',
      subtitle: 'Mount Fuji Twilight',
      lore: 'Marvel at cherry blossom petals dancing across mirrored lakes under snow-capped peaks.',
      backgroundAsset: 'assets/images/Stage-4.webp',
      primaryColor: Color(0xFFF472B6),
      secondaryColor: Color(0xFFEC4899),
      glowColor: Color(0xFFFBCFE8),
      cardGradientStart: Color(0x99330922),
      cardGradientEnd: Color(0xCC17030F),
      icon: Icons.filter_vintage_rounded,
      requiredStarsToUnlock: 45,
    ),

    // ── World 5: Levels 161 - 200 ───────────────────────────────────────────
    WorldData(
      id: 4,
      title: 'Lavender Twilight',
      subtitle: 'Firefly Valley',
      lore: 'Immerse your mind in endless purple lavender rows illuminated by dancing firefly orbs.',
      backgroundAsset: 'assets/images/Stage-5.webp',
      primaryColor: Color(0xFF06B6D4),
      secondaryColor: Color(0xFF0284C7),
      glowColor: Color(0xFF67E8F9),
      cardGradientStart: Color(0x99083344),
      cardGradientEnd: Color(0xCC031826),
      icon: Icons.nightlight_round,
      requiredStarsToUnlock: 70,
    ),

    // ── World 6: Levels 201 - 240 ───────────────────────────────────────────
    WorldData(
      id: 5,
      title: 'Autumn Haven',
      subtitle: 'Golden Brook',
      lore: 'Follow crystal clear streams through golden birch woods to a peaceful mountain shelter.',
      backgroundAsset: 'assets/images/Stage-6.webp',
      primaryColor: Color(0xFFF59E0B),
      secondaryColor: Color(0xFFD97706),
      glowColor: Color(0xFFFDE68A),
      cardGradientStart: Color(0x99301E03),
      cardGradientEnd: Color(0xCC140C01),
      icon: Icons.park_rounded,
      requiredStarsToUnlock: 100,
    ),

    // ── World 7: Levels 241 - 280 ───────────────────────────────────────────
    WorldData(
      id: 6,
      title: 'Alpine Glaciers',
      subtitle: 'Crystal Peaks',
      lore: 'Conquer majestic snowy mountain massifs mirrored in pure turquoise glacial water.',
      backgroundAsset: 'assets/images/Stage-7.webp',
      primaryColor: Color(0xFF38BDF8),
      secondaryColor: Color(0xFF0284C7),
      glowColor: Color(0xFFBAE6FD),
      cardGradientStart: Color(0x9904223A),
      cardGradientEnd: Color(0xCC02101C),
      icon: Icons.landscape_rounded,
      requiredStarsToUnlock: 135,
    ),

    // ── World 8: Levels 281 - 320 ───────────────────────────────────────────
    WorldData(
      id: 7,
      title: 'Blossom Valley',
      subtitle: 'Serene Mist',
      lore: 'Float above dreamlike pastel valleys shrouded in gentle mist and blossoming trees.',
      backgroundAsset: 'assets/images/daily_puzzle_landing_background.webp',
      primaryColor: Color(0xFFFB7185),
      secondaryColor: Color(0xFFE11D48),
      glowColor: Color(0xFFFECDD3),
      cardGradientStart: Color(0x99300A15),
      cardGradientEnd: Color(0xCC140308),
      icon: Icons.spa_rounded,
      requiredStarsToUnlock: 175,
    ),

    // ── World 9: Levels 321 - 360 ───────────────────────────────────────────
    WorldData(
      id: 8,
      title: 'Emerald Waters',
      subtitle: 'Highland Fjord',
      lore: 'Navigate rolling green peaks and serene turquoise fjords under clear mountain skies.',
      backgroundAsset: 'assets/images/level_complete_background.webp',
      primaryColor: Color(0xFF34D399),
      secondaryColor: Color(0xFF059669),
      glowColor: Color(0xFFA7F3D0),
      cardGradientStart: Color(0x9906291C),
      cardGradientEnd: Color(0xCC02120C),
      icon: Icons.water_rounded,
      requiredStarsToUnlock: 220,
    ),

    // ── World 10: Levels 361 - 400 ──────────────────────────────────────────
    WorldData(
      id: 9,
      title: 'Celestial Zenith',
      subtitle: 'Sky Realm',
      lore: 'Reach the pinnacle of intellect above sunlit clouds in the realm of master thinkers.',
      backgroundAsset: 'assets/images/puzzle_complete_background.webp',
      primaryColor: Color(0xFF818CF8),
      secondaryColor: Color(0xFF6366F1),
      glowColor: Color(0xFFC7D2FE),
      cardGradientStart: Color(0x9919173D),
      cardGradientEnd: Color(0xCC0A091C),
      icon: Icons.workspace_premium_rounded,
      requiredStarsToUnlock: 270,
    ),

    // ── World 11: Levels 401 - 440 ──────────────────────────────────────────
    WorldData(
      id: 10,
      title: 'Golden Horizon',
      subtitle: 'Solar Spire',
      lore: 'Marvel at radiant sunrise panoramas where solar spires channel boundless mental energy.',
      backgroundAsset: 'assets/images/home_background.webp',
      primaryColor: Color(0xFFFBBF24),
      secondaryColor: Color(0xFFD97706),
      glowColor: Color(0xFFFEF08A),
      cardGradientStart: Color(0x99382200),
      cardGradientEnd: Color(0xCC180F00),
      icon: Icons.wb_twilight_rounded,
      requiredStarsToUnlock: 325,
    ),

    // ── World 12: Levels 441 - 480 ──────────────────────────────────────────
    WorldData(
      id: 11,
      title: 'Quantum Nebula',
      subtitle: 'Cosmic Stardust',
      lore: 'Venture through swirling deep space vortexes pulsating with ultraviolet cosmic stardust.',
      backgroundAsset: 'assets/images/quiz_background.webp',
      primaryColor: Color(0xFFA855F7),
      secondaryColor: Color(0xFF7E22CE),
      glowColor: Color(0xFFE9D5FF),
      cardGradientStart: Color(0x992B0C4A),
      cardGradientEnd: Color(0xCC120324),
      icon: Icons.all_inclusive_rounded,
      requiredStarsToUnlock: 385,
    ),

    // ── World 13: Levels 481 - 520 ──────────────────────────────────────────
    WorldData(
      id: 12,
      title: 'Prismatic Aurora',
      subtitle: 'Northern Lights',
      lore: 'Witness vibrant ribbons of emerald and violet dancing across polar midnight horizons.',
      backgroundAsset: 'assets/images/quiz_correct_background.webp',
      primaryColor: Color(0xFF2DD4BF),
      secondaryColor: Color(0xFF0F766E),
      glowColor: Color(0xFF99F6E4),
      cardGradientStart: Color(0x99072B28),
      cardGradientEnd: Color(0xCC021413),
      icon: Icons.flare_rounded,
      requiredStarsToUnlock: 450,
    ),

    // ── World 14: Levels 521 - 560 ──────────────────────────────────────────
    WorldData(
      id: 13,
      title: 'Crimson Abyss',
      subtitle: 'Obsidian Core',
      lore: 'Descend to incandescent subterranean magma veins guarded by obsidian crystal spires.',
      backgroundAsset: 'assets/images/quiz_wrong_background.webp',
      primaryColor: Color(0xFFF43F5E),
      secondaryColor: Color(0xFFBE123C),
      glowColor: Color(0xFFFECDD3),
      cardGradientStart: Color(0x993B0814),
      cardGradientEnd: Color(0xCC170207),
      icon: Icons.local_fire_department_rounded,
      requiredStarsToUnlock: 520,
    ),

    // ── World 15: Levels 561 - 600 ──────────────────────────────────────────
    WorldData(
      id: 14,
      title: 'Shadow Realm',
      subtitle: 'Silver Eclipse',
      lore: 'Unravel nocturnal mysteries beneath a luminous lunar halo in silver-dusted forests.',
      backgroundAsset: 'assets/images/game over background image.webp',
      primaryColor: Color(0xFF94A3B8),
      secondaryColor: Color(0xFF475569),
      glowColor: Color(0xFFE2E8F0),
      cardGradientStart: Color(0x991E293B),
      cardGradientEnd: Color(0xCC0A0F1D),
      icon: Icons.dark_mode_rounded,
      requiredStarsToUnlock: 595,
    ),

    // ── World 16: Levels 601 - 640 ──────────────────────────────────────────
    WorldData(
      id: 15,
      title: 'Mystic Canopy',
      subtitle: 'Ancient Grove',
      lore: 'Step into millennium-old sequoia groves illuminated by bioluminescent moss and flora.',
      backgroundAsset: 'assets/images/Stage-2.webp',
      primaryColor: Color(0xFF14B8A6),
      secondaryColor: Color(0xFF0D9488),
      glowColor: Color(0xFF5EEAD4),
      cardGradientStart: Color(0x99042621),
      cardGradientEnd: Color(0xCC011411),
      icon: Icons.nature_people_rounded,
      requiredStarsToUnlock: 675,
    ),

    // ── World 17: Levels 641 - 680 ──────────────────────────────────────────
    WorldData(
      id: 16,
      title: 'Crystal Geode',
      subtitle: 'Amethyst Depths',
      lore: 'Explore cavernous geode sanctuaries whose faceted violet quartz crystals amplify reasoning.',
      backgroundAsset: 'assets/images/Stage-5.webp',
      primaryColor: Color(0xFFC084FC),
      secondaryColor: Color(0xFF9333EA),
      glowColor: Color(0xFFF3E8FF),
      cardGradientStart: Color(0x992B0D47),
      cardGradientEnd: Color(0xCC120421),
      icon: Icons.diamond_rounded,
      requiredStarsToUnlock: 760,
    ),

    // ── World 18: Levels 681 - 720 ──────────────────────────────────────────
    WorldData(
      id: 17,
      title: 'Neon Matrix',
      subtitle: 'Cyber Grid',
      lore: 'Navigate high-speed neural networks flashing with neon cyan logic circuits.',
      backgroundAsset: 'assets/images/quiz_background.webp',
      primaryColor: Color(0xFF22D3EE),
      secondaryColor: Color(0xFF0891B2),
      glowColor: Color(0xFFA5F3FC),
      cardGradientStart: Color(0x99052A30),
      cardGradientEnd: Color(0xCC021417),
      icon: Icons.memory_rounded,
      requiredStarsToUnlock: 850,
    ),

    // ── World 19: Levels 721 - 760 ──────────────────────────────────────────
    WorldData(
      id: 18,
      title: 'Sunset Dunes',
      subtitle: 'Desert Mirage',
      lore: 'Cross vast rolling amber dunes where shimmering desert mirages test your perception.',
      backgroundAsset: 'assets/images/home_background.webp',
      primaryColor: Color(0xFFFB923C),
      secondaryColor: Color(0xFFEA580C),
      glowColor: Color(0xFFFED7AA),
      cardGradientStart: Color(0x99381A05),
      cardGradientEnd: Color(0xCC170A01),
      icon: Icons.wb_sunny_outlined,
      requiredStarsToUnlock: 945,
    ),

    // ── World 20: Levels 761 - 800 ──────────────────────────────────────────
    WorldData(
      id: 19,
      title: 'Glacial Fjord',
      subtitle: 'Frost Sanctuary',
      lore: 'Trek crystalline polar ice shelves bordering aquamarine fjords under perpetual twilight.',
      backgroundAsset: 'assets/images/Stage-7.webp',
      primaryColor: Color(0xFF60A5FA),
      secondaryColor: Color(0xFF2563EB),
      glowColor: Color(0xFFBFDBFE),
      cardGradientStart: Color(0x990B2244),
      cardGradientEnd: Color(0xCC040F21),
      icon: Icons.ac_unit_rounded,
      requiredStarsToUnlock: 1045,
    ),

    // ── World 21: Levels 801 - 840 ──────────────────────────────────────────
    WorldData(
      id: 20,
      title: 'Coral Odyssey',
      subtitle: 'Sunken Reef',
      lore: 'Dive beneath turquoise swells into ancient sunken cities encrusted in glowing living corals.',
      backgroundAsset: 'assets/images/Stage-3.webp',
      primaryColor: Color(0xFF06B6D4),
      secondaryColor: Color(0xFF0891B2),
      glowColor: Color(0xFFA5F3FC),
      cardGradientStart: Color(0x99062D38),
      cardGradientEnd: Color(0xCC02161C),
      icon: Icons.waves_rounded,
      requiredStarsToUnlock: 1150,
    ),

    // ── World 22: Levels 841 - 880 ──────────────────────────────────────────
    WorldData(
      id: 21,
      title: 'Sakura Dawn',
      subtitle: 'Spirit Garden',
      lore: 'Meditate in mist-shrouded temple gardens where cherry blossoms swirl upon peaceful streams.',
      backgroundAsset: 'assets/images/Stage-4.webp',
      primaryColor: Color(0xFFF43F5E),
      secondaryColor: Color(0xFFBE123C),
      glowColor: Color(0xFFFFE4E6),
      cardGradientStart: Color(0x99330919),
      cardGradientEnd: Color(0xCC17030A),
      icon: Icons.yard_rounded,
      requiredStarsToUnlock: 1260,
    ),

    // ── World 23: Levels 881 - 920 ──────────────────────────────────────────
    WorldData(
      id: 22,
      title: 'Thunder Crag',
      subtitle: 'Storm Pinnacle',
      lore: 'Scale tempestuous crags where violet lightning illuminates the raw power of focused intellect.',
      backgroundAsset: 'assets/images/level_complete_background.webp',
      primaryColor: Color(0xFF818CF8),
      secondaryColor: Color(0xFF4F46E5),
      glowColor: Color(0xFFE0E7FF),
      cardGradientStart: Color(0x99181442),
      cardGradientEnd: Color(0xCC0B0924),
      icon: Icons.flash_on_rounded,
      requiredStarsToUnlock: 1375,
    ),

    // ── World 24: Levels 921 - 960 ──────────────────────────────────────────
    WorldData(
      id: 23,
      title: 'Starlight Citadel',
      subtitle: 'Astral Hall',
      lore: 'Stand upon floating marble citadels watching galaxies turn across the edge of the universe.',
      backgroundAsset: 'assets/images/puzzle_complete_background.webp',
      primaryColor: Color(0xFFA78BFA),
      secondaryColor: Color(0xFF7C3AED),
      glowColor: Color(0xFFEDE9FE),
      cardGradientStart: Color(0x99241042),
      cardGradientEnd: Color(0xCC100621),
      icon: Icons.auto_awesome_rounded,
      requiredStarsToUnlock: 1495,
    ),

    // ── World 25: Levels 961 - 1000 ─────────────────────────────────────────
    WorldData(
      id: 24,
      title: 'Infinite Singularity',
      subtitle: 'Cognitive Core',
      lore: 'The apex of MindTrap AI. Transcend the limits of mental aptitude in the realm of pure thought.',
      backgroundAsset: 'assets/images/daily_puzzle_landing_background.webp',
      primaryColor: Color(0xFFF59E0B),
      secondaryColor: Color(0xFFD97706),
      glowColor: Color(0xFFFEF3C7),
      cardGradientStart: Color(0x99382402),
      cardGradientEnd: Color(0xCC1A1000),
      icon: Icons.psychology_rounded,
      requiredStarsToUnlock: 1620,
    ),
  ];

  static WorldData getWorld(int worldIndex) {
    if (worldIndex < 0 || worldIndex >= allWorlds.length) {
      return allWorlds[0];
    }
    return allWorlds[worldIndex];
  }
}
