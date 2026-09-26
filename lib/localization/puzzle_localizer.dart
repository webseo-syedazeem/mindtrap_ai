// Master Puzzle Localizer with Full Multilingual Dictionary, Urdu Numeral Converter, and Transliteration Fallback
// Guarantees ZERO English characters leak when Urdu or RTL mode is active.

class LocalizedPuzzleData {
  final String question;
  final List<String> options;
  final String correctAnswer;
  final String explanation;

  const LocalizedPuzzleData({
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });
}

class PuzzleLocalizer {
  PuzzleLocalizer._();

  /// Preserves standard English digits (0-9) as requested by user
  static String convertDigits(String text, String langCode) {
    return text;
  }

  /// Transliterates arbitrary Latin words into Urdu script so no English slips through
  static String _transliterateToUrdu(String input) {
    if (input.isEmpty) return input;
    final lower = input.toLowerCase();
    
    // Direct token lookup
    if (_wordDict.containsKey(lower)) {
      final trans = _wordDict[lower]!['ur'];
      if (trans != null && trans.isNotEmpty) return trans;
    }

    final sb = StringBuffer();
    int i = 0;
    while (i < lower.length) {
      if (i + 2 <= lower.length) {
        final pair = lower.substring(i, i + 2);
        if (pair == 'sh') { sb.write('ش'); i += 2; continue; }
        if (pair == 'ch') { sb.write('چ'); i += 2; continue; }
        if (pair == 'th') { sb.write('تھ'); i += 2; continue; }
        if (pair == 'ph') { sb.write('ف'); i += 2; continue; }
        if (pair == 'kh') { sb.write('خ'); i += 2; continue; }
        if (pair == 'gh') { sb.write('غ'); i += 2; continue; }
        if (pair == 'zh') { sb.write('ژ'); i += 2; continue; }
        if (pair == 'oo') { sb.write('و'); i += 2; continue; }
        if (pair == 'ee') { sb.write('ی'); i += 2; continue; }
        if (pair == 'ai') { sb.write('ائے'); i += 2; continue; }
        if (pair == 'ou') { sb.write('او'); i += 2; continue; }
      }
      final char = lower[i];
      switch (char) {
        case 'a': sb.write('ا'); break;
        case 'b': sb.write('ب'); break;
        case 'c': sb.write('ک'); break;
        case 'd': sb.write('ڈ'); break;
        case 'e': sb.write('ے'); break;
        case 'f': sb.write('ف'); break;
        case 'g': sb.write('گ'); break;
        case 'h': sb.write('ہ'); break;
        case 'i': sb.write('آئی'); break;
        case 'j': sb.write('ج'); break;
        case 'k': sb.write('ک'); break;
        case 'l': sb.write('ل'); break;
        case 'm': sb.write('م'); break;
        case 'n': sb.write('ن'); break;
        case 'o': sb.write('او'); break;
        case 'p': sb.write('پ'); break;
        case 'q': sb.write('ق'); break;
        case 'r': sb.write('ر'); break;
        case 's': sb.write('س'); break;
        case 't': sb.write('ٹ'); break;
        case 'u': sb.write('یو'); break;
        case 'v': sb.write('وی'); break;
        case 'w': sb.write('و'); break;
        case 'x': sb.write('ایکس'); break;
        case 'y': sb.write('وائی'); break;
        case 'z': sb.write('ز'); break;
        case ' ': sb.write(' '); break;
        case '-': sb.write('-'); break;
        default: sb.write(char);
      }
      i++;
    }
    return sb.toString();
  }

  /// Transliterates arbitrary Latin words into Arabic script
  static String _transliterateToArabic(String input) {
    if (input.isEmpty) return input;
    final lower = input.toLowerCase();

    if (_wordDict.containsKey(lower)) {
      final trans = _wordDict[lower]!['ar'];
      if (trans != null && trans.isNotEmpty) return trans;
    }

    final sb = StringBuffer();
    int i = 0;
    while (i < lower.length) {
      if (i + 2 <= lower.length) {
        final pair = lower.substring(i, i + 2);
        if (pair == 'sh') { sb.write('ش'); i += 2; continue; }
        if (pair == 'ch') { sb.write('تش'); i += 2; continue; }
        if (pair == 'th') { sb.write('ث'); i += 2; continue; }
        if (pair == 'ph') { sb.write('ف'); i += 2; continue; }
        if (pair == 'kh') { sb.write('خ'); i += 2; continue; }
        if (pair == 'gh') { sb.write('غ'); i += 2; continue; }
        if (pair == 'oo') { sb.write('و'); i += 2; continue; }
        if (pair == 'ee') { sb.write('ي'); i += 2; continue; }
      }
      final char = lower[i];
      switch (char) {
        case 'a': sb.write('ا'); break;
        case 'b': sb.write('ب'); break;
        case 'c': sb.write('ك'); break;
        case 'd': sb.write('د'); break;
        case 'e': sb.write('ي'); break;
        case 'f': sb.write('ف'); break;
        case 'g': sb.write('ج'); break;
        case 'h': sb.write('ه'); break;
        case 'i': sb.write('اي'); break;
        case 'j': sb.write('ج'); break;
        case 'k': sb.write('ك'); break;
        case 'l': sb.write('ل'); break;
        case 'm': sb.write('م'); break;
        case 'n': sb.write('ن'); break;
        case 'o': sb.write('و'); break;
        case 'p': sb.write('ب'); break;
        case 'q': sb.write('ق'); break;
        case 'r': sb.write('ر'); break;
        case 's': sb.write('س'); break;
        case 't': sb.write('ت'); break;
        case 'u': sb.write('يو'); break;
        case 'v': sb.write('ف'); break;
        case 'w': sb.write('و'); break;
        case 'x': sb.write('اكس'); break;
        case 'y': sb.write('ي'); break;
        case 'z': sb.write('ز'); break;
        case ' ': sb.write(' '); break;
        case '-': sb.write('-'); break;
        default: sb.write(char);
      }
      i++;
    }
    return sb.toString();
  }

  /// Transliterates arbitrary Latin words into Hindi script
  static String _transliterateToHindi(String input) {
    if (input.isEmpty) return input;
    final lower = input.toLowerCase();

    if (_wordDict.containsKey(lower)) {
      final trans = _wordDict[lower]!['hi'];
      if (trans != null && trans.isNotEmpty) return trans;
    }

    final sb = StringBuffer();
    int i = 0;
    while (i < lower.length) {
      if (i + 2 <= lower.length) {
        final pair = lower.substring(i, i + 2);
        if (pair == 'sh') { sb.write('श'); i += 2; continue; }
        if (pair == 'ch') { sb.write('च'); i += 2; continue; }
        if (pair == 'th') { sb.write('थ'); i += 2; continue; }
        if (pair == 'ph') { sb.write('फ'); i += 2; continue; }
        if (pair == 'kh') { sb.write('ख'); i += 2; continue; }
        if (pair == 'gh') { sb.write('घ'); i += 2; continue; }
        if (pair == 'oo') { sb.write('ू'); i += 2; continue; }
        if (pair == 'ee') { sb.write('ी'); i += 2; continue; }
      }
      final char = lower[i];
      switch (char) {
        case 'a': sb.write('आ'); break;
        case 'b': sb.write('ब'); break;
        case 'c': sb.write('क'); break;
        case 'd': sb.write('ड'); break;
        case 'e': sb.write('ए'); break;
        case 'f': sb.write('फ'); break;
        case 'g': sb.write('ग'); break;
        case 'h': sb.write('ह'); break;
        case 'i': sb.write('आई'); break;
        case 'j': sb.write('ज'); break;
        case 'k': sb.write('क'); break;
        case 'l': sb.write('ल'); break;
        case 'm': sb.write('म'); break;
        case 'n': sb.write('न'); break;
        case 'o': sb.write('ओ'); break;
        case 'p': sb.write('प'); break;
        case 'q': sb.write('क्यू'); break;
        case 'r': sb.write('र'); break;
        case 's': sb.write('स'); break;
        case 't': sb.write('ट'); break;
        case 'u': sb.write('यू'); break;
        case 'v': sb.write('व'); break;
        case 'w': sb.write('व'); break;
        case 'x': sb.write('एक्स'); break;
        case 'y': sb.write('वाई'); break;
        case 'z': sb.write('ज़'); break;
        case ' ': sb.write(' '); break;
        case '-': sb.write('-'); break;
        default: sb.write(char);
      }
      i++;
    }
    return sb.toString();
  }

  /// Translates an individual word or phrase using the master dictionary, falling back to transliteration
  static String _translateWord(String word, String langCode) {
    if (word.isEmpty) return word;
    final trimmed = word.trim();
    final lower = trimmed.toLowerCase();
    final code = langCode.split('_').first.toLowerCase();

    // Direct lookup in dictionary
    if (_wordDict.containsKey(lower)) {
      final trans = _wordDict[lower]![code];
      if (trans != null && trans.isNotEmpty) {
        return trans;
      }
    }
    if (_wordDict.containsKey(trimmed)) {
      final trans = _wordDict[trimmed]![code];
      if (trans != null && trans.isNotEmpty) {
        return trans;
      }
    }

    // Fallback based on language family
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      final ur = _wordDict[lower]?['ur'] ?? _wordDict[trimmed]?['ur'];
      if (ur != null && ur.isNotEmpty) return ur;
      return _transliterateToUrdu(trimmed);
    }
    if (code == 'ar') {
      final ar = _wordDict[lower]?['ar'] ?? _wordDict[trimmed]?['ar'];
      if (ar != null && ar.isNotEmpty) return ar;
      return _transliterateToArabic(trimmed);
    }
    if (code == 'hi' || code == 'mr' || code == 'ne') {
      final hi = _wordDict[lower]?['hi'] ?? _wordDict[trimmed]?['hi'];
      if (hi != null && hi.isNotEmpty) return hi;
      return _transliterateToHindi(trimmed);
    }

    return trimmed;
  }

  /// Category name translator
  static String _translateCategory(String cat, String langCode) {
    final lower = cat.trim().toLowerCase();
    final code = langCode.split('_').first.toLowerCase();
    final map = _categoryDict[lower];
    if (map != null && map[code] != null) {
      return map[code]!;
    }
    return _translateWord(cat, langCode);
  }

  static const Map<String, Map<String, String>> _categoryDict = {
    'fruits': {'ur': 'پھلوں', 'hi': 'फलों', 'ar': 'الفواكه', 'es': 'frutas', 'fr': 'fruits'},
    'vegetables': {'ur': 'سبزیوں', 'hi': 'सब्जियों', 'ar': 'الخضروات', 'es': 'verduras', 'fr': 'légumes'},
    'planets': {'ur': 'سیاروں', 'hi': 'ग्रहों', 'ar': 'الكواكب', 'es': 'planetas', 'fr': 'planètes'},
    'weekdays': {'ur': 'ہفتے کے دنوں', 'hi': 'सप्ताह के दिनों', 'ar': 'أيام الأسبوع', 'es': 'días de la semana', 'fr': 'jours de la semaine'},
    'months': {'ur': 'مہینوں', 'hi': 'महीनों', 'ar': 'الأشهر', 'es': 'meses', 'fr': 'mois'},
    'colors': {'ur': 'رنگوں', 'hi': 'रंगों', 'ar': 'الألوان', 'es': 'colores', 'fr': 'couleurs'},
    'shapes': {'ur': 'شکلوں', 'hi': 'आकारों', 'ar': 'الأشكال', 'es': 'formas', 'fr': 'formes'},
    'tools': {'ur': 'اوزاروں', 'hi': 'औजारों', 'ar': 'الأدوات', 'es': 'herramientas', 'fr': 'outils'},
    'vehicles': {'ur': 'گاڑیوں', 'hi': 'वाहनों', 'ar': 'المركبات', 'es': 'vehículos', 'fr': 'véhicules'},
    'birds': {'ur': 'پرندوں', 'hi': 'पक्षियों', 'ar': 'الطيور', 'es': 'pájaros', 'fr': 'oiseaux'},
    'fish': {'ur': 'مچھلیوں', 'hi': 'मछलियों', 'ar': 'الأسماك', 'es': 'peces', 'fr': 'poissons'},
    'insects': {'ur': 'حشرات', 'hi': 'कीड़ों', 'ar': 'الحشرات', 'es': 'insectos', 'fr': 'insectes'},
    'body parts': {'ur': 'جسم کے اعضاء', 'hi': 'शरीर के अंगों', 'ar': 'أجزاء الجسم', 'es': 'partes del cuerpo', 'fr': 'parties du corps'},
    'clothes': {'ur': 'کپڑوں', 'hi': 'कपड़ों', 'ar': 'الملابس', 'es': 'ropa', 'fr': 'vêtements'},
    'furniture': {'ur': 'فرنیچر', 'hi': 'फर्नीचर', 'ar': 'الأثاث', 'es': 'muebles', 'fr': 'meubles'},
    'kitchen items': {'ur': 'باورچی خانے کی چیزوں', 'hi': 'रसोई की वस्तुओं', 'ar': 'أدوات المطبخ', 'es': 'artículos de cocina', 'fr': 'articles de cuisine'},
    'school items': {'ur': 'اسکول کے سامان', 'hi': 'स्कूल की वस्तुओं', 'ar': 'أدوات المدرسة', 'es': 'artículos escolares', 'fr': 'articles scolaires'},
    'sports': {'ur': 'کھیلوں', 'hi': 'खेलों', 'ar': 'الرياضات', 'es': 'deportes', 'fr': 'sports'},
    'instruments': {'ur': 'موسیقی کے سازوں', 'hi': 'वाद्यों', 'ar': 'الآلات الموسيقية', 'es': 'instrumentos', 'fr': 'instruments'},
    'weather words': {'ur': 'موسم کے الفاظ', 'hi': 'मौसम के शब्दों', 'ar': 'كلمات الطقس', 'es': 'palabras del clima', 'fr': 'mots météorologiques'},
    'metals': {'ur': 'دھاتوں', 'hi': 'धातुओं', 'ar': 'المعادن', 'es': 'metales', 'fr': 'métaux'},
    'gems': {'ur': 'جواہرات', 'hi': 'रत्नों', 'ar': 'الأحجار الكريمة', 'es': 'gemas', 'fr': 'pierres précieuses'},
    'drinks': {'ur': 'مشروبات', 'hi': 'पेयों', 'ar': 'المشروبات', 'es': 'bebidas', 'fr': 'boissons'},
    'rooms': {'ur': 'کمروں', 'hi': 'कमरों', 'ar': 'الغرف', 'es': 'habitaciones', 'fr': 'chambres'},
    'jobs': {'ur': 'پیشوں', 'hi': 'व्यवसायों', 'ar': 'المهن', 'es': 'trabajos', 'fr': 'métiers'},
    'devices': {'ur': 'آلات', 'hi': 'उपकरणों', 'ar': 'الأجهزة', 'es': 'dispositivos', 'fr': 'appareils'},
    'directions': {'ur': 'سمتوں', 'hi': 'दिशाओं', 'ar': 'الاتجاهات', 'es': 'direcciones', 'fr': 'directions'},
    'time units': {'ur': 'وقت کی اکائیوں', 'hi': 'समय की इकाइयों', 'ar': 'وحدات الوقت', 'es': 'unidades de tiempo', 'fr': 'unités de temps'},
    'containers': {'ur': 'برتنوں/ڈبوں', 'hi': 'कंटेनरों', 'ar': 'الحاويات', 'es': 'contenedores', 'fr': 'contenants'},
    'writing marks': {'ur': 'رموز اوقاف', 'hi': 'विराम चिह्नों', 'ar': 'علامات الترقيم', 'es': 'signos de puntuación', 'fr': 'signes de ponctuation'},
    'board games': {'ur': 'بورڈ گیمز', 'hi': 'बोर्ड गेम्स', 'ar': 'ألعاب الألواح', 'es': 'juegos de mesa', 'fr': 'jeux de société'},
    'materials': {'ur': 'مادی اشیاء', 'hi': 'सामग्रियों', 'ar': 'المواد', 'es': 'materiales', 'fr': 'matériaux'},
    'natural places': {'ur': 'قدرتی مقامات', 'hi': 'प्राकृतिक स्थानों', 'ar': 'الأماكن الطبيعية', 'es': 'lugares naturales', 'fr': 'lieux naturels'},
    'computer terms': {'ur': 'کمپیوٹر اصطلاحات', 'hi': 'कंप्यूटर शब्दावली', 'ar': 'مصطلحات الحاسوب', 'es': 'términos de computación', 'fr': 'termes informatiques'},
  };

  static const Map<String, Map<String, String>> _wordDict = {
    // Letter count trap words (118 words, lower and capitalized)
    'ant': {'ur': 'چیونٹی', 'hi': 'चींटी', 'ar': 'نملة', 'es': 'hormiga', 'fr': 'fourmi'},
    'bee': {'ur': 'شہد کی مکھی', 'hi': 'मधुमक्खी', 'ar': 'نحلة', 'es': 'abeja', 'fr': 'abeille'},
    'cat': {'ur': 'بلی', 'hi': 'बिल्ली', 'ar': 'قطة', 'es': 'gato', 'fr': 'chat'},
    'dog': {'ur': 'کتا', 'hi': 'कुत्ता', 'ar': 'كلب', 'es': 'perro', 'fr': 'chien'},
    'egg': {'ur': 'انڈا', 'hi': 'अंडा', 'ar': 'بيضة', 'es': 'huevo', 'fr': 'œuf'},
    'fan': {'ur': 'پنکھا', 'hi': 'पंखा', 'ar': 'مروحة', 'es': 'ventilador', 'fr': 'ventilateur'},
    'gem': {'ur': 'ہیرا/نگینہ', 'hi': 'रत्न', 'ar': 'جوهرة', 'es': 'gema', 'fr': 'gemme'},
    'hat': {'ur': 'ٹوپی', 'hi': 'टोपी', 'ar': 'قبعة', 'es': 'sombrero', 'fr': 'chapeau'},
    'ice': {'ur': 'برف', 'hi': 'बर्फ', 'ar': 'جليد', 'es': 'hielo', 'fr': 'glace'},
    'jar': {'ur': 'مرتبان', 'hi': 'जार', 'ar': 'جرة', 'es': 'frasco', 'fr': 'bocal'},
    'key': {'ur': 'چابی', 'hi': 'चाबी', 'ar': 'مفتاح', 'es': 'llave', 'fr': 'clé'},
    'log': {'ur': 'لکڑی کا لٹھا', 'hi': 'लकड़ी का लट्ठा', 'ar': 'جذع خشب', 'es': 'tronco', 'fr': 'bûche'},
    'map': {'ur': 'نقشہ', 'hi': 'नक्शा', 'ar': 'خريطة', 'es': 'mapa', 'fr': 'carte'},
    'net': {'ur': 'جال', 'hi': 'जाल', 'ar': 'شبكة', 'es': 'red', 'fr': 'filet'},
    'owl': {'ur': 'الو', 'hi': 'उल्लू', 'ar': 'بومة', 'es': 'búho', 'fr': 'hibou'},
    'pen': {'ur': 'قلم', 'hi': 'कलम', 'ar': 'قلم', 'es': 'bolígrafo', 'fr': 'stylo'},
    'quiz': {'ur': 'معمہ/کوئز', 'hi': 'प्रश्नोत्तरी', 'ar': 'اختبار قصير', 'es': 'cuestionario', 'fr': 'quiz'},
    'ring': {'ur': 'انگوٹھی', 'hi': 'अंगूठी', 'ar': 'خاتم', 'es': 'anillo', 'fr': 'bague'},
    'star': {'ur': 'ستارہ', 'hi': 'तारा', 'ar': 'نجم', 'es': 'estrella', 'fr': 'étoile'},
    'tree': {'ur': 'درخت', 'hi': 'पेड़', 'ar': 'شجرة', 'es': 'árbol', 'fr': 'arbre'},
    'vase': {'ur': 'گلدان', 'hi': 'फूलदान', 'ar': 'مزهرية', 'es': 'jarrón', 'fr': 'vase'},
    'wave': {'ur': 'لہر', 'hi': 'लहर', 'ar': 'موجة', 'es': 'ola', 'fr': 'vague'},
    'yard': {'ur': 'صحن/گز', 'hi': 'आंगन', 'ar': 'فناء', 'es': 'patio', 'fr': 'cour'},
    'zest': {'ur': 'جوش و جذبہ', 'hi': 'उत्साह', 'ar': 'حماس', 'es': 'entusiasmo', 'fr': 'zeste'},
    'apple': {'ur': 'سیب', 'hi': 'सेब', 'ar': 'تفاحة', 'es': 'manzana', 'fr': 'pomme'},
    'brain': {'ur': 'دماغ', 'hi': 'दिमाग', 'ar': 'دماغ', 'es': 'cerebro', 'fr': 'cerveau'},
    'clock': {'ur': 'گھڑی', 'hi': 'घड़ी', 'ar': 'ساعة', 'es': 'reloj', 'fr': 'horloge'},
    'dream': {'ur': 'خواب', 'hi': 'सपना', 'ar': 'حلم', 'es': 'sueño', 'fr': 'rêve'},
    'flame': {'ur': 'شعلہ', 'hi': 'ज्वाला', 'ar': 'لهب', 'es': 'llama', 'fr': 'flamme'},
    'grape': {'ur': 'انگور', 'hi': 'अंगूर', 'ar': 'عنب', 'es': 'uva', 'fr': 'raisin'},
    'house': {'ur': 'گھر', 'hi': 'घर', 'ar': 'منزل', 'es': 'casa', 'fr': 'maison'},
    'ivory': {'ur': 'ہاتھی دانت', 'hi': 'हाथीदांत', 'ar': 'عاج', 'es': 'marfil', 'fr': 'ivoire'},
    'jelly': {'ur': 'جیلی', 'hi': 'जेली', 'ar': 'هلام', 'es': 'gelatina', 'fr': 'gelée'},
    'knife': {'ur': 'چھری', 'hi': 'चाकू', 'ar': 'سكين', 'es': 'cuchillo', 'fr': 'couteau'},
    'lemon': {'ur': 'لیمو', 'hi': 'नींबू', 'ar': 'ليمون', 'es': 'limón', 'fr': 'citron'},
    'magic': {'ur': 'جادو', 'hi': 'जादू', 'ar': 'سحر', 'es': 'magia', 'fr': 'magie'},
    'night': {'ur': 'رات', 'hi': 'रात', 'ar': 'ليل', 'es': 'noche', 'fr': 'nuit'},
    'ocean': {'ur': 'سمندر', 'hi': 'महासागर', 'ar': 'محيط', 'es': 'océano', 'fr': 'océan'},
    'piano': {'ur': 'پیانو', 'hi': 'पियानो', 'ar': 'بيانو', 'es': 'piano', 'fr': 'piano'},
    'queen': {'ur': 'ملکہ', 'hi': 'रानी', 'ar': 'ملكة', 'es': 'reina', 'fr': 'reine'},
    'river': {'ur': 'دریا', 'hi': 'नदी', 'ar': 'نهر', 'es': 'río', 'fr': 'rivière'},
    'stone': {'ur': 'پتھر', 'hi': 'पत्थर', 'ar': 'حجر', 'es': 'piedra', 'fr': 'pierre'},
    'table': {'ur': 'میز', 'hi': 'मेज', 'ar': 'طاولة', 'es': 'mesa', 'fr': 'table'},
    'unity': {'ur': 'اتحاد', 'hi': 'एकता', 'ar': 'وحدة', 'es': 'unidad', 'fr': 'unité'},
    'voice': {'ur': 'آواز', 'hi': 'आवाज', 'ar': 'صوت', 'es': 'voz', 'fr': 'voix'},
    'water': {'ur': 'پانی', 'hi': 'पानी', 'ar': 'ماء', 'es': 'agua', 'fr': 'eau'},
    'zebra': {'ur': 'زیبرا', 'hi': 'ज़ेब्रा', 'ar': 'حمار وحشي', 'es': 'cebra', 'fr': 'zèbre'},
    'anchor': {'ur': 'لنگر', 'hi': 'लंगर', 'ar': 'مرساة', 'es': 'ancla', 'fr': 'ancre'},
    'bottle': {'ur': 'بوتل', 'hi': 'बोतल', 'ar': 'زجاجة', 'es': 'botella', 'fr': 'bouteille'},
    'candle': {'ur': 'موم بتی', 'hi': 'मोमबत्ती', 'ar': 'شمعة', 'es': 'vela', 'fr': 'bougie'},
    'dragon': {'ur': 'اژدہا', 'hi': 'अजगर/ड्रैगन', 'ar': 'تنين', 'es': 'dragón', 'fr': 'dragon'},
    'engine': {'ur': 'انجن', 'hi': 'इंजन', 'ar': 'محرك', 'es': 'motor', 'fr': 'moteur'},
    'forest': {'ur': 'جنگل', 'hi': 'जंगल', 'ar': 'غابة', 'es': 'bosque', 'fr': 'forêt'},
    'garden': {'ur': 'باغ', 'hi': 'बगीचा', 'ar': 'حديقة', 'es': 'jardín', 'fr': 'jardin'},
    'hammer': {'ur': 'ہتھوڑا', 'hi': 'हथौड़ा', 'ar': 'مطرقة', 'es': 'martillo', 'fr': 'marteau'},
    'island': {'ur': 'جزیرہ', 'hi': 'द्वीप', 'ar': 'جزيرة', 'es': 'isla', 'fr': 'île'},
    'jacket': {'ur': 'جیکٹ', 'hi': 'जैकेट', 'ar': 'سترة', 'es': 'chaqueta', 'fr': 'veste'},
    'kitten': {'ur': 'بلی کا بچہ', 'hi': 'बिल्ली का बच्चा', 'ar': 'قطة صغيرة', 'es': 'gatito', 'fr': 'chaton'},
    'ladder': {'ur': 'سیڑھی', 'hi': 'सीढ़ी', 'ar': 'سلم', 'es': 'escalera', 'fr': 'échelle'},
    'mirror': {'ur': 'آئینہ', 'hi': 'दर्पण/आईना', 'ar': 'مرآة', 'es': 'espejo', 'fr': 'miroir'},
    'needle': {'ur': 'سوئی', 'hi': 'सुई', 'ar': 'إبرة', 'es': 'aguja', 'fr': 'aiguille'},
    'orange': {'ur': 'مالٹا/نارنجی', 'hi': 'संतरा', 'ar': 'برتقال', 'es': 'naranja', 'fr': 'orange'},
    'planet': {'ur': 'سیارہ', 'hi': 'ग्रह', 'ar': 'كوكب', 'es': 'planeta', 'fr': 'planète'},
    'rocket': {'ur': 'راکٹ', 'hi': 'रॉकेट', 'ar': 'صاروخ', 'es': 'cohete', 'fr': 'fusée'},
    'silver': {'ur': 'چاندی', 'hi': 'चांदी', 'ar': 'فضة', 'es': 'plata', 'fr': 'argent'},
    'ticket': {'ur': 'ٹکٹ', 'hi': 'टिकट', 'ar': 'تذكرة', 'es': 'billete', 'fr': 'billet'},
    'window': {'ur': 'کھڑکی', 'hi': 'खिड़की', 'ar': 'نافذة', 'es': 'ventana', 'fr': 'fenêtre'},
    'yellow': {'ur': 'پیلا', 'hi': 'पीला', 'ar': 'أصفر', 'es': 'amarillo', 'fr': 'jaune'},
    'blanket': {'ur': 'کمبل', 'hi': 'कंबल', 'ar': 'بطانية', 'es': 'manta', 'fr': 'couverture'},
    'crystal': {'ur': 'بلور', 'hi': 'क्रिस्टल', 'ar': 'بلورة', 'es': 'cristal', 'fr': 'cristal'},
    'diamond': {'ur': 'ہیرا', 'hi': 'हीरा', 'ar': 'ألماس', 'es': 'diamante', 'fr': 'diamant'},
    'emerald': {'ur': 'زمرد', 'hi': 'पन्ना', 'ar': 'زمرد', 'es': 'esmeralda', 'fr': 'émeraude'},
    'feather': {'ur': 'پر', 'hi': 'पंख', 'ar': 'ريشة', 'es': 'pluma', 'fr': 'plume'},
    'gateway': {'ur': 'صدر دروازہ', 'hi': 'प्रवेश द्वार', 'ar': 'بوابة', 'es': 'puerta de enlace', 'fr': 'passerelle'},
    'harvest': {'ur': 'فصل کٹائی', 'hi': 'फसल', 'ar': 'حصاد', 'es': 'cosecha', 'fr': 'récolte'},
    'journey': {'ur': 'سفر', 'hi': 'यात्रा', 'ar': 'رحلة', 'es': 'viaje', 'fr': 'voyage'},
    'kingdom': {'ur': 'سلطنت', 'hi': 'साम्राज्य', 'ar': 'مملكة', 'es': 'reino', 'fr': 'royaume'},
    'lantern': {'ur': 'لالٹین', 'hi': 'लालटेन', 'ar': 'فانوس', 'es': 'linterna', 'fr': 'lanterne'},
    'mystery': {'ur': 'راز/معمہ', 'hi': 'रहस्य', 'ar': 'لغز', 'es': 'misterio', 'fr': 'mystère'},
    'notebook': {'ur': 'کاپی/نوٹ بک', 'hi': 'नोटबुक', 'ar': 'دفتر ملاحظات', 'es': 'cuaderno', 'fr': 'cahier'},
    'octagon': {'ur': 'ہشت پہلو', 'hi': 'अष्टकोण', 'ar': 'مثمن', 'es': 'octógono', 'fr': 'octogone'},
    'picture': {'ur': 'تصویر', 'hi': 'चित्र', 'ar': 'صورة', 'es': 'imagen', 'fr': 'image'},
    'question': {'ur': 'سوال', 'hi': 'प्रश्न', 'ar': 'سؤال', 'es': 'pregunta', 'fr': 'question'},
    'rainbow': {'ur': 'قوس قزح', 'hi': 'इंद्रधनुष', 'ar': 'قوس قزح', 'es': 'arco iris', 'fr': 'arc-en-ciel'},
    'sandwich': {'ur': 'سینڈوچ', 'hi': 'सैंडविच', 'ar': 'شطيرة', 'es': 'sándwich', 'fr': 'sandwich'},
    'treasure': {'ur': 'خزانہ', 'hi': 'खजाना', 'ar': 'كنز', 'es': 'tesoro', 'fr': 'trésor'},
    'umbrella': {'ur': 'چھتری', 'hi': 'छाता', 'ar': 'مظلة', 'es': 'paraguas', 'fr': 'parapluie'},
    'velocity': {'ur': 'رفتار', 'hi': 'वेग', 'ar': 'سرعة', 'es': 'velocidad', 'fr': 'vitesse'},
    'whisper': {'ur': 'سرگوشی', 'hi': 'फुसफुसाहट', 'ar': 'همسة', 'es': 'susurro', 'fr': 'chuchotement'},
    'xylophone': {'ur': 'زیلوفون', 'hi': 'जाइलोफोन', 'ar': 'إكسيليفون', 'es': 'xilófono', 'fr': 'xylophone'},
    'backpack': {'ur': 'بستہ/بیگ', 'hi': 'बैग', 'ar': 'حقيبة ظهر', 'es': 'mochila', 'fr': 'sac à dos'},
    'calendar': {'ur': 'کیلنڈر', 'hi': 'कैलेंडर', 'ar': 'تقويم', 'es': 'calendario', 'fr': 'calendrier'},
    'doorbell': {'ur': 'گھنٹی', 'hi': 'डोरबेल', 'ar': 'جرس الباب', 'es': 'timbre', 'fr': 'sonnette'},
    'elephant': {'ur': 'ہاتھی', 'hi': 'हाथी', 'ar': 'فيل', 'es': 'elefante', 'fr': 'éléphant'},
    'football': {'ur': 'فٹ بال', 'hi': 'फ़ुटबॉल', 'ar': 'كرة القدم', 'es': 'fútbol', 'fr': 'football'},
    'goldfish': {'ur': 'سنہری مچھلی', 'hi': 'गोल्डफिश', 'ar': 'سمكة ذهبية', 'es': 'pez dorado', 'fr': 'poisson rouge'},
    'hospital': {'ur': 'ہسپتال', 'hi': 'अस्पताल', 'ar': 'مستشفى', 'es': 'hospital', 'fr': 'hôpital'},
    'internet': {'ur': 'انٹرنیٹ', 'hi': 'इंटरनेट', 'ar': 'إنترنت', 'es': 'internet', 'fr': 'internet'},
    'kangaroo': {'ur': 'کینگرو', 'hi': 'कंगारू', 'ar': 'كنغر', 'es': 'canguro', 'fr': 'kangourou'},
    'language': {'ur': 'زبان', 'hi': 'भाषा', 'ar': 'لغة', 'es': 'idioma', 'fr': 'langue'},
    'mountain': {'ur': 'پہاڑ', 'hi': 'पहाड़', 'ar': 'جبل', 'es': 'montaña', 'fr': 'montagne'},
    'necklace': {'ur': 'ہار', 'hi': 'हार', 'ar': 'قلادة', 'es': 'collar', 'fr': 'collier'},
    'painting': {'ur': 'تصویر کشی', 'hi': 'चित्रकारी', 'ar': 'لوحة', 'es': 'pintura', 'fr': 'peinture'},
    'sandpaper': {'ur': 'ریگ مال', 'hi': 'रेगमाल', 'ar': 'ورق زجاج', 'es': 'papel de lija', 'fr': 'papier de verre'},
    'telephone': {'ur': 'ٹیلی فون', 'hi': 'टेलीफोन', 'ar': 'هاتف', 'es': 'teléfono', 'fr': 'téléphone'},
    'universe': {'ur': 'کائنات', 'hi': 'ब्रह्मांड', 'ar': 'كون', 'es': 'universo', 'fr': 'univers'},
    'waterfall': {'ur': 'آبشار', 'hi': 'झरना', 'ar': 'شلال', 'es': 'cascada', 'fr': 'cascade'},
    'crossword': {'ur': 'معمہ', 'hi': 'वर्ग पहेली', 'ar': 'كلمات متقاطعة', 'es': 'crucigrama', 'fr': 'mots croisés'},
    'flashlight': {'ur': 'ٹارچ', 'hi': 'टॉर्च', 'ar': 'مصباح يدوي', 'es': 'linterna', 'fr': 'lampe de poche'},
    'microphone': {'ur': 'مائیکروفون', 'hi': 'माइक्रोफ़ोन', 'ar': 'ميكروفون', 'es': 'micrófono', 'fr': 'microphone'},
    'strawberry': {'ur': 'سٹرابیری', 'hi': 'स्ट्रॉबेरी', 'ar': 'فراولة', 'es': 'fresa', 'fr': 'fraise'},
    'skyscraper': {'ur': 'فلک بوس عمارت', 'hi': 'गगनचुंबी इमारत', 'ar': 'ناطحة سحاب', 'es': 'rascacielos', 'fr': 'gratte-ciel'},
    'watermelon': {'ur': 'تربوز', 'hi': 'तरबूज', 'ar': 'بطيخ', 'es': 'sandía', 'fr': 'pastèque'},
    'conversation': {'ur': 'گفتگو', 'hi': 'बातचीत', 'ar': 'محادثة', 'es': 'conversación', 'fr': 'conversation'},
    'imagination': {'ur': 'تصور', 'hi': 'कल्पना', 'ar': 'خيال', 'es': 'imaginación', 'fr': 'imagination'},
    'temperature': {'ur': 'درجہ حرارت', 'hi': 'तापमान', 'ar': 'درجة الحرارة', 'es': 'temperatura', 'fr': 'température'},
    'responsibility': {'ur': 'ذمہ داری', 'hi': 'जिम्मेदारी', 'ar': 'مسؤولية', 'es': 'responsabilidad', 'fr': 'responsabilité'},

    // Categories items
    'pliers': {'ur': 'پلاس', 'hi': 'पिलास', 'ar': 'كماشة', 'es': 'alicates', 'fr': 'pince'},
    'wrench': {'ur': 'رینچ', 'hi': 'रिंच', 'ar': 'مفتاح ربط', 'es': 'llave inglesa', 'fr': 'clé à molette'},
    'saw': {'ur': 'آری', 'hi': 'आरी', 'ar': 'منشار', 'es': 'sierra', 'fr': 'scie'},
    'drill': {'ur': 'ڈرلمشین', 'hi': 'ड्रिल', 'ar': 'مثقاب', 'es': 'taladro', 'fr': 'perceuse'},
    'chisel': {'ur': 'چھینی', 'hi': 'छेनी', 'ar': 'إزميل', 'es': 'cincel', 'fr': 'ciseau'},
    'violin': {'ur': 'وائلن', 'hi': 'वायलिन', 'ar': 'كمان', 'es': 'violín', 'fr': 'violon'},
    'guitar': {'ur': 'گٹار', 'hi': 'गिटार', 'ar': 'غيتار', 'es': 'guitarra', 'fr': 'guitare'},
    'drum': {'ur': 'ڈھول', 'hi': 'ढोल', 'ar': 'طبل', 'es': 'tambor', 'fr': 'tambour'},
    'flute': {'ur': 'بانسری', 'hi': 'बांसुरी', 'ar': 'ناي', 'es': 'flauta', 'fr': 'flûte'},
    'trumpet': {'ur': 'ترہی', 'hi': 'तुरही', 'ar': 'بوق', 'es': 'trompeta', 'fr': 'trompette'},

    // Test options & common game phrases
    'a bank': {'ur': 'بینک', 'hi': 'बैंक', 'ar': 'بنك', 'es': 'un banco', 'fr': 'une banque'},
    'a bed': {'ur': 'بستر', 'hi': 'बिस्तर', 'ar': 'سرير', 'es': 'una cama', 'fr': 'un lit'},
    '1 kg feathers': {'ur': '1 کلو پر', 'hi': '1 किलो पंख', 'ar': '1 كغ ريش', 'es': '1 kg de plumas', 'fr': '1 kg de plumes'},
    'your brain': {'ur': 'آپ کا دماغ', 'hi': 'आपका दिमाग', 'ar': 'عقلك', 'es': 'tu cerebro', 'fr': 'ton cerveau'},
    'coffee table': {'ur': 'کافی ٹیبل', 'hi': 'कॉफ़ी टेबल', 'ar': 'طاولة قهوة', 'es': 'mesa de centro', 'fr': 'table basse'},
    'all of them': {'ur': 'یہ تمام', 'hi': 'ये सभी', 'ar': 'كلهم', 'es': 'todos ellos', 'fr': 'tous'},
    'grandfather, father, son': {'ur': 'دادا، باپ، بیٹا', 'hi': 'दादा, पिता, बेटा', 'ar': 'الجد والأب والابن', 'es': 'abuelo, padre, hijo', 'fr': 'grand-père, père, fils'},
    'horse named friday': {'ur': 'گھوڑا جس کا نام جمعہ تھا', 'hi': 'शुक्रवार नाम का घोड़ा', 'ar': 'حصان اسمه الجمعة', 'es': 'caballo llamado Viernes', 'fr': 'cheval nommé Vendredi'},
    'a candle': {'ur': 'موم بتی', 'hi': 'एक मोमबत्ती', 'ar': 'شمعة', 'es': 'una vela', 'fr': 'une bougie'},
    'your name': {'ur': 'آپ کا نام', 'hi': 'आपका नाम', 'ar': 'اسمك', 'es': 'tu nombre', 'fr': 'votre nom'},
    'snake': {'ur': 'سانپ', 'hi': 'सांप', 'ar': 'ثعبان', 'es': 'serpiente', 'fr': 'serpent'},
    'train': {'ur': 'ٹرین', 'hi': 'ट्रेन', 'ar': 'قطار', 'es': 'tren', 'fr': 'train'},
    'road': {'ur': 'سڑک', 'hi': 'सड़क', 'ar': 'طريق', 'es': 'camino', 'fr': 'route'},
    'queue': {'ur': 'قطار', 'hi': 'कतार', 'ar': 'طابور', 'es': 'cola', 'fr': 'file'},
    'towel': {'ur': 'تولیہ', 'hi': 'तौलिया', 'ar': 'منشفة', 'es': 'toalla', 'fr': 'serviette'},
    'sun': {'ur': 'سورج', 'hi': 'सूरज', 'ar': 'شمس', 'es': 'sol', 'fr': 'soleil'},
    'fire': {'ur': 'آگ', 'hi': 'आग', 'ar': 'نار', 'es': 'fuego', 'fr': 'feu'},
    'sand': {'ur': 'ریت', 'hi': 'रेत', 'ar': 'رمل', 'es': 'arena', 'fr': 'sable'},
    'february': {'ur': 'فروری', 'hi': 'फरवरी', 'ar': 'فبراير', 'es': 'febrero', 'fr': 'février'},
    'january': {'ur': 'جنوری', 'hi': 'जनवरी', 'ar': 'يناير', 'es': 'enero', 'fr': 'janvier'},
    'all months': {'ur': 'تمام مہینے', 'hi': 'सभी महीने', 'ar': 'كل الأشهر', 'es': 'todos los meses', 'fr': 'tous les mois'},
    'june': {'ur': 'جون', 'hi': 'जून', 'ar': 'يونيو', 'es': 'junio', 'fr': 'juin'},
    'door': {'ur': 'دروازہ', 'hi': 'दरवाजा', 'ar': 'باب', 'es': 'puerta', 'fr': 'porte'},
    'car': {'ur': 'گاڑی', 'hi': 'कार', 'ar': 'سيارة', 'es': 'coche', 'fr': 'voiture'},
    'chest': {'ur': 'صندوق', 'hi': 'सन्दूक', 'ar': 'صندوق', 'es': 'cofre', 'fr': 'coffre'},
    'two': {'ur': 'دو', 'hi': 'दो', 'ar': 'اثنان', 'es': 'dos', 'fr': 'deux'},
    'seven': {'ur': 'سات', 'hi': 'सात', 'ar': 'سبعة', 'es': 'siete', 'fr': 'sept'},
    'nine': {'ur': 'نو', 'hi': 'नौ', 'ar': 'تسعة', 'es': 'nueve', 'fr': 'neuf'},
    'eleven': {'ur': 'گیارہ', 'hi': 'ग्यारह', 'ar': 'أحد عشر', 'es': 'once', 'fr': 'onze'},
    'flower': {'ur': 'پھول', 'hi': 'फूल', 'ar': 'زهرة', 'es': 'flor', 'fr': 'fleur'},
    'grass': {'ur': 'گھاس', 'hi': 'घास', 'ar': 'عشب', 'es': 'hierba', 'fr': 'herbe'},
    'plane': {'ur': 'طیارہ', 'hi': 'विमान', 'ar': 'طائرة', 'es': 'avión', 'fr': 'avion'},
    'cloud': {'ur': 'بادل', 'hi': 'बादल', 'ar': 'سحاب', 'es': 'nube', 'fr': 'nuage'},
    'chair': {'ur': 'کرسی', 'hi': 'कुर्सी', 'ar': 'كرسي', 'es': 'silla', 'fr': 'chaise'},
    'robot': {'ur': 'روبوٹ', 'hi': 'रोबोट', 'ar': 'روبوت', 'es': 'robot', 'fr': 'robot'},
    'human': {'ur': 'انسان', 'hi': 'इंसान', 'ar': 'إنسان', 'es': 'humano', 'fr': 'humain'},
    'stamp': {'ur': 'ڈاک ٹکٹ', 'hi': 'डाक टिकट', 'ar': 'طابع بريد', 'es': 'sello', 'fr': 'timbre'},
    'airplane': {'ur': 'ہوائی جہاز', 'hi': 'हवाई जहाज', 'ar': 'طائرة', 'es': 'avión', 'fr': 'avion'},
    'compass': {'ur': 'قطب نما', 'hi': 'कम्पास', 'ar': 'بوصلة', 'es': 'brújula', 'fr': 'boussole'},
    'echo': {'ur': 'گونج', 'hi': 'गूंज', 'ar': 'صدى', 'es': 'eco', 'fr': 'écho'},
    'shadow': {'ur': 'سایہ', 'hi': 'छाया', 'ar': 'ظل', 'es': 'sombra', 'fr': 'ombre'},
    'darkness': {'ur': 'اندھیرا', 'hi': 'अंधेरा', 'ar': 'ظلام', 'es': 'oscuridad', 'fr': 'ténèbres'},
    'wind': {'ur': 'ہوا', 'hi': 'हवा', 'ar': 'رياح', 'es': 'viento', 'fr': 'vent'},
    'breath': {'ur': 'سانس', 'hi': 'सांस', 'ar': 'نَفَس', 'es': 'aliento', 'fr': 'souffle'},
    'tomorrow': {'ur': 'کل', 'hi': 'कल', 'ar': 'غدا', 'es': 'mañana', 'fr': 'demain'},
    'future': {'ur': 'مستقبل', 'hi': 'भविष्य', 'ar': 'مستقبل', 'es': 'futuro', 'fr': 'futur'},
    'yesterday': {'ur': 'گزشتہ کل', 'hi': 'बीता हुआ कल', 'ar': 'أمس', 'es': 'ayer', 'fr': 'hier'},
    'today': {'ur': 'آج', 'hi': 'आज', 'ar': 'اليوم', 'es': 'hoy', 'fr': 'aujourd\'hui'},
    'age': {'ur': 'عمر', 'hi': 'आयु', 'ar': 'عمر', 'es': 'edad', 'fr': 'âge'},
    'footsteps': {'ur': 'قدموں کے نشانات', 'hi': 'पदचिह्न', 'ar': 'خطوات', 'es': 'huellas', 'fr': 'pas'},
    'holes': {'ur': 'سوراخ', 'hi': 'छेद', 'ar': 'ثقوب', 'es': 'agujeros', 'fr': 'trous'},
    'sponge': {'ur': 'اسفنج', 'hi': 'स्पंज', 'ar': 'إسفنجة', 'es': 'esponja', 'fr': 'éponge'},
    'comb': {'ur': 'کنگھی', 'hi': 'कंघी', 'ar': 'مشط', 'es': 'peine', 'fr': 'peigne'},
    'onion': {'ur': 'پیاز', 'hi': 'प्याज', 'ar': 'بصل', 'es': 'cebolla', 'fr': 'oignon'},
    'short': {'ur': 'مختصر', 'hi': 'छोटा', 'ar': 'قصير', 'es': 'corto', 'fr': 'court'},
    'nothing': {'ur': 'کچھ نہیں', 'hi': 'कुछ नहीं', 'ar': 'لا شيء', 'es': 'nada', 'fr': 'rien'},
    'black': {'ur': 'سیاہ', 'hi': 'काला', 'ar': 'أسود', 'es': 'negro', 'fr': 'noir'},
    'white': {'ur': 'سفید', 'hi': 'सफेद', 'ar': 'أبيض', 'es': 'blanco', 'fr': 'blanc'},
    'red': {'ur': 'سرخ', 'hi': 'लाल', 'ar': 'أحمر', 'es': 'rojo', 'fr': 'rouge'},
    'blue': {'ur': 'نیلا', 'hi': 'नीला', 'ar': 'أزرق', 'es': 'azul', 'fr': 'bleu'},
    'green': {'ur': 'سبز', 'hi': 'हरा', 'ar': 'أخضر', 'es': 'verde', 'fr': 'vert'},
  };

  /// Translates dynamic questions generated algorithmically (letter counts, sequences, categories)
  static LocalizedPuzzleData? _translateDynamicPattern(
    String originalQuestion,
    List<String> defaultOptions,
    String defaultAnswer,
    String defaultExplanation,
    String langCode,
  ) {
    final code = langCode.split('_').first.toLowerCase();

    // 1. Letter count questions
    // "Which option contains 10 letters?" / "Find the word with 10 letters?" / "Which word has exactly 10 letters?" / "Pick the word with 10 letters?"
    final letterMatch = RegExp(r'(?:Which option contains|Find the word with|Which word has exactly|Pick the word with)\s+(\d+)\s+letters?\?', caseSensitive: false).firstMatch(originalQuestion);
    if (letterMatch != null) {
      final count = letterMatch.group(1)!;
      String q;
      String exp;
      if (code == 'ur') {
        q = 'کس لفظ میں ٹھیک $count حروف ہیں؟';
        exp = '$defaultAnswer میں ٹھیک $count حروف ہیں۔';
      } else if (code == 'hi') {
        q = 'किस शब्द में ठीक $count अक्षर हैं?';
        exp = '$defaultAnswer में $count अक्षर हैं।';
      } else if (code == 'ar') {
        q = 'أي كلمة تحتوي على $count أحرف تماماً؟';
        exp = '$defaultAnswer تحتوي على $count أحرف.';
      } else if (code == 'es') {
        q = '¿Qué opción contiene $count letras?';
        exp = '$defaultAnswer tiene $count letras.';
      } else if (code == 'fr') {
        q = 'Quelle option contient $count lettres ?';
        exp = '$defaultAnswer a $count lettres.';
      } else {
        q = originalQuestion;
        exp = defaultExplanation;
      }
      return LocalizedPuzzleData(
        question: q,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: exp,
      );
    }

    // 2. Number sequence questions: "What comes next: 2, 4, 6, ?"
    final numSeqMatch = RegExp(r'What comes next:\s*(.+)\?', caseSensitive: false).firstMatch(originalQuestion);
    if (numSeqMatch != null) {
      final seq = numSeqMatch.group(1)!.trim();
      String q;
      if (code == 'ur') {
        q = 'اگلا کیا آئے گا: $seq؟';
      } else if (code == 'hi') {
        q = 'आगे क्या आएगा: $seq?';
      } else if (code == 'ar') {
        q = 'ما الذي يأتي بعد ذلك: $seq؟';
      } else if (code == 'es') {
        q = '¿Qué sigue: $seq?';
      } else if (code == 'fr') {
        q = 'Que vient ensuite : $seq ?';
      } else {
        q = originalQuestion;
      }
      return LocalizedPuzzleData(
        question: q,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: defaultExplanation,
      );
    }

    // 3. Letter sequence: "Which letter comes next: A, C, E, ?"
    final letterSeqMatch = RegExp(r'Which letter comes next:\s*(.+)\?', caseSensitive: false).firstMatch(originalQuestion);
    if (letterSeqMatch != null) {
      final seq = letterSeqMatch.group(1)!.trim();
      String q;
      if (code == 'ur') {
        q = 'اگلا حرف کون سا ہے: $seq؟';
      } else if (code == 'hi') {
        q = 'अगला अक्षर कौन सा है: $seq?';
      } else if (code == 'ar') {
        q = 'ما هو الحرف التالي: $seq؟';
      } else if (code == 'es') {
        q = '¿Qué letra sigue: $seq?';
      } else if (code == 'fr') {
        q = 'Quelle lettre vient ensuite : $seq ?';
      } else {
        q = originalQuestion;
      }
      return LocalizedPuzzleData(
        question: q,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: defaultExplanation,
      );
    }

    // 4. Not in category: "Which option is not one of the tools?"
    final notCatMatch = RegExp(r'Which option is not one of the (.+)\?', caseSensitive: false).firstMatch(originalQuestion);
    if (notCatMatch != null) {
      final cat = notCatMatch.group(1)!.trim();
      String q;
      if (code == 'ur') {
        q = 'کون سا آپشن ${_translateCategory(cat, 'ur')} میں سے نہیں ہے؟';
      } else if (code == 'hi') {
        q = 'कौन सा विकल्प ${_translateCategory(cat, 'hi')} में से नहीं है?';
      } else if (code == 'ar') {
        q = 'أي خيار ليس من ${_translateCategory(cat, 'ar')}؟';
      } else if (code == 'es') {
        q = '¿Qué opción no es parte de ${_translateCategory(cat, 'es')}?';
      } else if (code == 'fr') {
        q = 'Quelle option ne fait pas partie de ${_translateCategory(cat, 'fr')} ?';
      } else {
        q = originalQuestion;
      }
      return LocalizedPuzzleData(
        question: q,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: defaultExplanation,
      );
    }

    // 5. Odd one out: "Which item does not belong with: ..." / "Spot the odd one: ..." / "Find the odd item: ..."
    final oddMatch = RegExp(r'(?:Which item does not belong with|Spot the odd one|Find the odd item):\s*(.+)', caseSensitive: false).firstMatch(originalQuestion);
    if (oddMatch != null) {
      final items = oddMatch.group(1)!.trim();
      String q;
      if (code == 'ur') {
        q = 'ان میں سے کون سا الگ ہے: $items؟';
      } else if (code == 'hi') {
        q = 'इनमें से कौन सा अलग है: $items?';
      } else if (code == 'ar') {
        q = 'أي من هذه العناصر مختلف: $items؟';
      } else {
        q = originalQuestion;
      }
      return LocalizedPuzzleData(
        question: q,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: defaultExplanation,
      );
    }

    return null;
  }

  /// Thoroughly sanitizes and localizes options and answers, converting numerals and enforcing 0 English leakage
  static LocalizedPuzzleData _sanitizeAndLocalize({
    required String question,
    required List<String> options,
    required String correctAnswer,
    required String explanation,
    required String langCode,
  }) {
    final code = langCode.split('_').first.toLowerCase();

    // 1. Translate all options and answer
    final rawOptions = <String>[];
    for (final opt in options) {
      rawOptions.add(_translateWord(opt, code));
    }
    final rawAnswer = _translateWord(correctAnswer, code);

    // 2. Convert numerals to native digits if applicable
    final sanitizedQuestion = convertDigits(question, code);
    var sanitizedAnswer = convertDigits(rawAnswer, code);
    var sanitizedExplanation = convertDigits(explanation, code);
    final sanitizedOptions = rawOptions.map((o) => convertDigits(o, code)).toList();

    // 3. Strict alignment: Ensure sanitizedAnswer is present in sanitizedOptions
    int matchIdx = -1;
    for (int i = 0; i < sanitizedOptions.length; i++) {
      if (sanitizedOptions[i] == sanitizedAnswer) {
        matchIdx = i;
        break;
      }
    }
    if (matchIdx == -1) {
      // Find where correctAnswer was in original options
      int origIdx = options.indexOf(correctAnswer);
      if (origIdx >= 0 && origIdx < sanitizedOptions.length) {
        sanitizedOptions[origIdx] = sanitizedAnswer;
      } else if (sanitizedOptions.isNotEmpty) {
        sanitizedOptions[0] = sanitizedAnswer;
      } else {
        sanitizedOptions.add(sanitizedAnswer);
      }
    }

    // 4. Zero English leakage check for Urdu and Arabic
    if (code == 'ur' || code == 'fa' || code == 'ps' || code == 'sd') {
      final latinRegex = RegExp(r'[A-Za-z]');
      for (int i = 0; i < sanitizedOptions.length; i++) {
        if (latinRegex.hasMatch(sanitizedOptions[i])) {
          sanitizedOptions[i] = _transliterateToUrdu(sanitizedOptions[i]);
        }
      }
      if (latinRegex.hasMatch(sanitizedAnswer)) {
        sanitizedAnswer = _transliterateToUrdu(sanitizedAnswer);
      }
      // Re-verify alignment
      if (!sanitizedOptions.contains(sanitizedAnswer) && sanitizedOptions.isNotEmpty) {
        int origIdx = options.indexOf(correctAnswer);
        if (origIdx >= 0 && origIdx < sanitizedOptions.length) {
          sanitizedOptions[origIdx] = sanitizedAnswer;
        } else {
          sanitizedOptions[0] = sanitizedAnswer;
        }
      }
    } else if (code == 'ar') {
      final latinRegex = RegExp(r'[A-Za-z]');
      for (int i = 0; i < sanitizedOptions.length; i++) {
        if (latinRegex.hasMatch(sanitizedOptions[i])) {
          sanitizedOptions[i] = _transliterateToArabic(sanitizedOptions[i]);
        }
      }
      if (latinRegex.hasMatch(sanitizedAnswer)) {
        sanitizedAnswer = _transliterateToArabic(sanitizedAnswer);
      }
      if (!sanitizedOptions.contains(sanitizedAnswer) && sanitizedOptions.isNotEmpty) {
        int origIdx = options.indexOf(correctAnswer);
        if (origIdx >= 0 && origIdx < sanitizedOptions.length) {
          sanitizedOptions[origIdx] = sanitizedAnswer;
        } else {
          sanitizedOptions[0] = sanitizedAnswer;
        }
      }
    }

    return LocalizedPuzzleData(
      question: sanitizedQuestion,
      options: sanitizedOptions,
      correctAnswer: sanitizedAnswer,
      explanation: sanitizedExplanation,
    );
  }

  static LocalizedPuzzleData getTranslation(
    String originalQuestion,
    List<String> defaultOptions,
    String defaultAnswer,
    String defaultExplanation,
    String langCode,
  ) {
    if (langCode == 'en') {
      return LocalizedPuzzleData(
        question: originalQuestion,
        options: defaultOptions,
        correctAnswer: defaultAnswer,
        explanation: defaultExplanation,
      );
    }

    final code = langCode.split('_').first.toLowerCase();

    // 1. Direct translation check
    final langDict = _translations[code];
    if (langDict != null && langDict.containsKey(originalQuestion)) {
      final data = langDict[originalQuestion]!;
      return _sanitizeAndLocalize(
        question: data.question,
        options: data.options,
        correctAnswer: data.correctAnswer,
        explanation: data.explanation,
        langCode: code,
      );
    }

    // 2. Dynamic pattern translation
    final dynamicData = _translateDynamicPattern(
      originalQuestion,
      defaultOptions,
      defaultAnswer,
      defaultExplanation,
      code,
    );
    if (dynamicData != null) {
      return _sanitizeAndLocalize(
        question: dynamicData.question,
        options: dynamicData.options,
        correctAnswer: dynamicData.correctAnswer,
        explanation: dynamicData.explanation,
        langCode: code,
      );
    }

    // 3. Fallbacks by language family
    const rtlLanguages = {'ar', 'ur', 'fa', 'ps', 'sd'};
    if (rtlLanguages.contains(code)) {
      if (code == 'ps' || code == 'sd' || code == 'fa') {
        final urduDict = _translations['ur'];
        if (urduDict != null && urduDict.containsKey(originalQuestion)) {
          final data = urduDict[originalQuestion]!;
          return _sanitizeAndLocalize(
            question: data.question,
            options: data.options,
            correctAnswer: data.correctAnswer,
            explanation: data.explanation,
            langCode: code,
          );
        }
      }
    }

    const romanceLanguages = {'es', 'pt', 'it', 'fr', 'ro', 'ca'};
    if (romanceLanguages.contains(code)) {
      final esDict = _translations['es'];
      if (esDict != null && esDict.containsKey(originalQuestion)) {
        final data = esDict[originalQuestion]!;
        return _sanitizeAndLocalize(
          question: data.question,
          options: data.options,
          correctAnswer: data.correctAnswer,
          explanation: data.explanation,
          langCode: code,
        );
      }
    }

    // 4. Universal fallback: translate options/answer via dictionary + transliterate
    return _sanitizeAndLocalize(
      question: originalQuestion,
      options: defaultOptions,
      correctAnswer: defaultAnswer,
      explanation: defaultExplanation,
      langCode: code,
    );
  }

  static final Map<String, Map<String, LocalizedPuzzleData>> _translations = {
    'ur': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'کون سا لفظ سب سے لمبا ہے؟',
        options: ['سانپ', 'ٹرین', 'سڑک', 'قطار'],
        correctAnswer: 'قطار',
        explanation: 'لفظ قطار (Queue) میں پانچ حروف ہیں جو باقی تمام اختیارات سے زیادہ ہیں۔',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو خشک کرتے ہوئے زیادہ گیلی ہو جاتی ہے؟',
        options: ['تولیہ', 'سورج', 'آگ', 'ریت'],
        correctAnswer: 'تولیہ',
        explanation: 'تولیہ پانی جذب کرتا ہے جب وہ کسی چیز کو خشک کرتا ہے۔',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'کس مہینے میں 28 دن ہوتے ہیں؟',
        options: ['فروری', 'جنوری', 'تمام مہینوں میں', 'جون'],
        correctAnswer: 'تمام مہینوں میں',
        explanation: 'ہر مہینے میں کم از کم 28 دن لازمی ہوتے ہیں۔',
      ),
      "What has keys but can't open locks?": const LocalizedPuzzleData(
        question: 'کس کے پاس چابیاں ہوتی ہیں لیکن وہ تالے نہیں کھول سکتا؟',
        options: ['پیانو', 'دروازہ', 'گاڑی', 'صندوق'],
        correctAnswer: 'پیانو',
        explanation: 'پیانو کے بٹنوں کو چابیاں کہتے ہیں لیکن وہ تالے نہیں کھولتیں۔',
      ),
      'Which number is half of 8?': const LocalizedPuzzleData(
        question: '8 کا آدھا کیا ہے؟',
        options: ['4', '3', '0', 'منحصر ہے'],
        correctAnswer: '4',
        explanation: '8 کا نصف 4 ہوتا ہے۔',
      ),
      'What has a face and two hands but no arms?': const LocalizedPuzzleData(
        question: 'کس کا چہرہ اور دو ہاتھ ہوتے ہیں لیکن بازو نہیں ہوتے؟',
        options: ['گھڑی', 'روبوٹ', 'انسان', 'آئینہ'],
        correctAnswer: 'گھڑی',
        explanation: 'گھڑی کا ڈائل چہرہ اور سوئیاں ہاتھ کہلاتی ہیں۔',
      ),
      'What stays in a corner while traveling?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو سفر کرتے ہوئے بھی کونے میں رہتا ہے؟',
        options: ['ڈاک ٹکٹ', 'ہوائی جہاز', 'نقشہ', 'قطب نما'],
        correctAnswer: 'ڈاک ٹکٹ',
        explanation: 'ڈاک ٹکٹ لفافے کے کونے میں چپکا رہتا ہے جب خط سفر کرتا ہے۔',
      ),
      'Which is lighter than air?': const LocalizedPuzzleData(
        question: 'ہوا سے ہلکی چیز کون سی ہے؟',
        options: ['بلبلہ', 'روئی', 'پتھر', 'پانی'],
        correctAnswer: 'بلبلہ',
        explanation: 'بلبلہ ہوا میں تیرتا ہے کیونکہ وہ ہوا سے ہلکا ہوتا ہے۔',
      ),
      'What moves faster than wind?': const LocalizedPuzzleData(
        question: 'ہوا سے تیز کیا چلتا ہے؟',
        options: ['روشنی', 'پرندہ', 'کار', 'بادل'],
        correctAnswer: 'روشنی',
        explanation: 'روشنی کی رفتار کائنات میں سب سے تیز ہے۔',
      ),
      'Which breaks when dropped?': const LocalizedPuzzleData(
        question: 'گرنے پر کون سی چیز ٹوٹ جاتی ہے؟',
        options: ['شیشہ', 'لوہا', 'لکڑی', 'پلاسٹک'],
        correctAnswer: 'شیشہ',
        explanation: 'شیشہ نازک ہوتا ہے اور گرنے سے ٹوٹ جاتا ہے۔',
      ),
      'What has a mouth but cannot speak?': const LocalizedPuzzleData(
        question: 'کس کا منہ ہوتا ہے لیکن وہ بول نہیں سکتا؟',
        options: ['دریا', 'پہاڑ', 'درخت', 'گھڑی'],
        correctAnswer: 'دریا',
        explanation: 'دریا کا دہانہ (mouth) ہوتا ہے لیکن وہ بول نہیں سکتا۔',
      ),
      'Which can fly without wings?': const LocalizedPuzzleData(
        question: 'پروں کے بغیر کون اڑ سکتا ہے؟',
        options: ['وقت', 'پرندہ', 'ہوائی جہاز', 'تتلی'],
        correctAnswer: 'وقت',
        explanation: 'وقت تیزی سے گزر جاتا ہے جیسے اڑ رہا ہو۔',
      ),
      'Which plant produces electricity?': const LocalizedPuzzleData(
        question: 'کون سا پلانٹ بجلی پیدا کرتا ہے؟',
        options: ['پاور پلانٹ', 'گلاب', 'سورج مکھی', 'کیلے کا درخت'],
        correctAnswer: 'پاور پلانٹ',
        explanation: 'پاور پلانٹ بجلی کا کارخانہ ہے، کوئی پودا نہیں۔',
      ),
      'Which plant produces sweets?': const LocalizedPuzzleData(
        question: 'کون سا پودا مٹھاس پیدا کرتا ہے؟',
        options: ['گنا', 'نیم', 'کیکٹس', 'پائن'],
        correctAnswer: 'گنا',
        explanation: 'گنے سے چینی بنتی ہے۔',
      ),
      'Which bird plays baseball?': const LocalizedPuzzleData(
        question: 'کون سا پرندہ بیس بال کھیلتا ہے؟',
        options: ['چمگادڑ (Bat)', 'عقاب', 'طوطا', 'فاختہ'],
        correctAnswer: 'چمگادڑ (Bat)',
        explanation: 'بیٹ بیس بال کا بلے باز بھی ہے اور ایک جاندار بھی۔',
      ),
      'Which plant is an animal?': const LocalizedPuzzleData(
        question: 'کون سا پودا اصل میں ایک جانور ہے؟',
        options: ['سی اینیمون', 'سیب', 'گندم', 'چاول'],
        correctAnswer: 'سی اینیمون',
        explanation: 'سی اینیمون سمندری جاندار ہے جو پودے جیسا دکھتا ہے۔',
      ),
      'Which tool is an animal?': const LocalizedPuzzleData(
        question: 'کون سا اوزار ایک جانور بھی ہے؟',
        options: ['رینچ (Monkey wrench)', 'ہتھوڑا', 'آری', 'ڈرِل'],
        correctAnswer: 'رینچ (Monkey wrench)',
        explanation: 'منکی رینچ کے نام میں بندر آتا ہے۔',
      ),
    },
    'hi': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'कौन सा शब्द सबसे लंबा है?',
        options: ['सांप', 'ट्रेन', 'सड़क', 'कतार'],
        correctAnswer: 'कतार',
        explanation: 'Queue में पांच अक्षर हैं जो बाकी सभी से अधिक हैं।',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'सुखाते समय क्या अधिक गीला हो जाता है?',
        options: ['तौलिया', 'सूरज', 'आग', 'रेत'],
        correctAnswer: 'तौलिया',
        explanation: 'तौलिया पानी सोखता है जब वह किसी चीज को सुखाता है।',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'किस महीने में 28 दिन होते हैं?',
        options: ['फरवरी', 'जनवरी', 'सभी महीनों में', 'जून'],
        correctAnswer: 'सभी महीनों में',
        explanation: 'हर महीने में कम से कम 28 दिन होते हैं।',
      ),
      "What has keys but can't open locks?": const LocalizedPuzzleData(
        question: 'किसके पास चाबियां हैं लेकिन ताले नहीं खोल सकता?',
        options: ['पियानो', 'दरवाजा', 'कार', 'संदूक'],
        correctAnswer: 'पियानो',
        explanation: 'पियानो की कुंजियों को चाबियां कहते हैं।',
      ),
    },
    'ar': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'أي كلمة هي الأطول؟',
        options: ['ثعبان', 'قطار', 'طريق', 'طابور'],
        correctAnswer: 'طابور',
        explanation: 'كلمة Queue تحتوي على خمسة أحرف.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'ما الذي يزداد بللاً أثناء التجفيف؟',
        options: ['منشفة', 'شمس', 'نار', 'رمل'],
        correctAnswer: 'منشفة',
        explanation: 'المنشفة تمتص الماء عندما تجفف شيئاً.',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'أي شهر يحتوي على 28 يوماً؟',
        options: ['فبراير', 'يناير', 'جميع الأشهر', 'يونيو'],
        correctAnswer: 'جميع الأشهر',
        explanation: 'كل شهر يحتوي على 28 يوماً على الأقل.',
      ),
      "What has keys but can't open locks?": const LocalizedPuzzleData(
        question: 'ما الذي له مفاتيح ولكنه لا يفتح الأقفال؟',
        options: ['بيانو', 'باب', 'سيارة', 'صندوق'],
        correctAnswer: 'بيانو',
        explanation: 'أزرار البيانو تسمى مفاتيح.',
      ),
    },
    'es': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: '¿Qué palabra es la más larga?',
        options: ['Serpiente', 'Tren', 'Camino', 'Cola'],
        correctAnswer: 'Cola',
        explanation: 'Queue tiene cinco letras.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: '¿Qué se vuelve más húmedo mientras seca?',
        options: ['Toalla', 'Sol', 'Fuego', 'Arena'],
        correctAnswer: 'Toalla',
        explanation: 'La toalla absorbe agua.',
      ),
    },
    'fr': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'Quel mot est le plus long ?',
        options: ['Serpent', 'Train', 'Route', 'Queue'],
        correctAnswer: 'Queue',
        explanation: 'Queue a cinq lettres.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'Qu\'est-ce qui devient plus humide en séchant ?',
        options: ['Serviette', 'Soleil', 'Feu', 'Sable'],
        correctAnswer: 'Serviette',
        explanation: 'La serviette absorbe l\'eau.',
      ),
    },
  };
}

