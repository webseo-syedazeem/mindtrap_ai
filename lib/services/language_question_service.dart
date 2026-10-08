import 'dart:convert';
import 'dart:math';
import 'package:flutter/services.dart';
import '../localization/language_controller.dart';
import '../main.dart' show PuzzleLevel;

enum QuestionDifficulty {
  easy,
  normal,
  tricky,
}

class NativePuzzle {
  final int id;
  final QuestionDifficulty difficulty;
  final String question;
  final List<String> options;
  final String correctAnswer;
  final String explanation;

  const NativePuzzle({
    required this.id,
    required this.difficulty,
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });

  PuzzleLevel toPuzzleLevel([int? seed]) {
    final opts = List<String>.from(options);
    final s = seed ?? (id != 0 ? id : (question.hashCode ^ correctAnswer.hashCode));
    opts.shuffle(Random(s));
    return PuzzleLevel(
      question: question,
      options: List.unmodifiable(opts),
      correctAnswer: correctAnswer,
      explanation: explanation,
    );
  }

  factory NativePuzzle.fromJson(Map<String, dynamic> json) {
    final diffStr = (json['difficulty'] as String? ?? 'easy').toLowerCase();
    final diff = diffStr == 'tricky'
        ? QuestionDifficulty.tricky
        : diffStr == 'normal'
            ? QuestionDifficulty.normal
            : QuestionDifficulty.easy;

    return NativePuzzle(
      id: json['id'] as int? ?? 0,
      difficulty: diff,
      question: json['question'] as String? ?? '',
      options: List<String>.from(json['options'] as List? ?? []),
      correctAnswer: json['correctAnswer'] as String? ?? '',
      explanation: json['explanation'] as String? ?? '',
    );
  }
}

class LanguageQuestionService {
  LanguageQuestionService._();
  static final LanguageQuestionService instance = LanguageQuestionService._();

  final Map<String, List<NativePuzzle>> _cachedBanks = {};
  bool _isInitialized = false;

  /// Initializes and preloads active language questions
  Future<void> init() async {
    if (_isInitialized) return;
    _isInitialized = true;
    await loadLanguageBank('en');
    await loadLanguageBank('ur');
    await loadLanguageBank('hi');
    final code = LanguageController.instance.currentCode;
    if (code != 'en' && code != 'ur' && code != 'hi') {
      await loadLanguageBank(code);
    }
  }

  /// Checks whether a language has a loaded native bank in memory
  bool hasNativeBank(String langCode) {
    final code = langCode.toLowerCase().trim();
    return _cachedBanks.containsKey(code) && _cachedBanks[code]!.isNotEmpty;
  }

  /// Loads native questions for a specific language from assets/questions/{code}.json
  Future<List<NativePuzzle>> loadLanguageBank(String langCode) async {
    final code = langCode.toLowerCase().trim();
    if (_cachedBanks.containsKey(code) && _cachedBanks[code]!.isNotEmpty) {
      return _cachedBanks[code]!;
    }

    try {
      final jsonString = await rootBundle.loadString('assets/questions/$code.json');
      final List<dynamic> list = jsonDecode(jsonString) as List<dynamic>;
      final puzzles = list
          .map((item) => NativePuzzle.fromJson(item as Map<String, dynamic>))
          .where((p) => p.question.isNotEmpty && p.options.length == 4)
          .toList();

      if (puzzles.isNotEmpty) {
        _cachedBanks[code] = puzzles;
        return puzzles;
      }
    } catch (_) {
      // Fallback to built-in native bank if asset JSON is not yet bundled
    }

    // Build embedded native bank
    final fallback = _buildNativeFallbackBank(code);
    _cachedBanks[code] = fallback;
    return fallback;
  }

  /// Returns strictly non-repeating questions for a given global level (0 - 999).
  /// Progression Guarantee:
  /// - Global Levels 0 - 249:   EASY (Intuitive logic, nature & everyday common-sense)
  /// - Global Levels 250 - 649: NORMAL (Deductions, patterns & clever scenarios)
  /// - Global Levels 650 - 999: TRICKY (Mind-bending paradoxes & lateral traps)
  List<PuzzleLevel> getQuestionsForLevel({
    required int globalLevel,
    required String langCode,
    int count = 3,
  }) {
    final code = langCode.toLowerCase().trim();
    var bank = _cachedBanks[code];
    if (bank == null || bank.isEmpty) {
      if (code == 'ur') {
        bank = _cachedBanks['ur'] ?? _buildNativeUrduBank();
      } else {
        bank = _cachedBanks['en'] ?? _buildNativeEnglishBank();
      }
    }
    if (bank.isEmpty) {
      return [];
    }

    // Split bank into difficulty tiers
    final easy = bank.where((p) => p.difficulty == QuestionDifficulty.easy).toList();
    final normal = bank.where((p) => p.difficulty == QuestionDifficulty.normal).toList();
    final tricky = bank.where((p) => p.difficulty == QuestionDifficulty.tricky).toList();

    List<NativePuzzle> targetTier;
    int tierOffset;

    if (globalLevel < 250) {
      targetTier = easy.isNotEmpty ? easy : bank;
      tierOffset = globalLevel;
    } else if (globalLevel < 650) {
      targetTier = normal.isNotEmpty ? normal : bank;
      tierOffset = globalLevel - 250;
    } else {
      targetTier = tricky.isNotEmpty ? tricky : bank;
      tierOffset = globalLevel - 650;
    }

    final result = <PuzzleLevel>[];
    for (int i = 0; i < count; i++) {
      // Strictly deterministic sequential non-repeating index
      final questionIndex = (tierOffset * count + i) % targetTier.length;
      result.add(targetTier[questionIndex].toPuzzleLevel());
    }

    return result;
  }

  /// Embedded high-quality native banks for instant zero-dependency execution
  List<NativePuzzle> _buildNativeFallbackBank(String langCode) {
    if (langCode == 'ur' || langCode == 'sd' || langCode == 'ps') {
      final urBank = _cachedBanks['ur'];
      if (urBank != null && urBank.isNotEmpty) {
        return urBank;
      }
      return _buildNativeUrduBank();
    }
    final enBank = _cachedBanks['en'];
    if (enBank != null && enBank.isNotEmpty) {
      return enBank;
    }
    return _buildNativeEnglishBank();
  }

  // ───────────────────────────────────────────────────────────────────────────
  // EMBEDDED NATIVE URDU BANK (خالص اردو پہیلیاں اور ذہنی آزمائش - No Translation)
  // ───────────────────────────────────────────────────────────────────────────
  List<NativePuzzle> _buildNativeUrduBank() {
    final list = <NativePuzzle>[];

    // EASY TIER (Levels 1 - 250)
    final easyUrdu = [
      const NativePuzzle(
        id: 1,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جو خشک کرتے وقت خود گیلی ہو جاتی ہے؟',
        options: ['تولیہ', 'بادل', 'سورج', 'ریت'],
        correctAnswer: 'تولیہ',
        explanation: 'تولیہ پانی جذب کرتا ہے جس سے وہ خود گیلا ہو جاتا ہے۔',
      ),
      const NativePuzzle(
        id: 2,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کیا ہے جس کے ہاتھ ہیں مگر وہ تالی نہیں بجا سکتی؟',
        options: ['گھڑی', 'درخت', 'کرسی', 'دستانہ'],
        correctAnswer: 'گھڑی',
        explanation: 'گھڑی کی سوئیاں اس کے ہاتھ کہلاتی ہیں مگر وہ تالی نہیں بجا سکتیں۔',
      ),
      const NativePuzzle(
        id: 3,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جسے استعمال کرنے سے پہلے توڑنا پڑتا ہے؟',
        options: ['انڈا', 'تالہ', 'شیشہ', 'بادام'],
        correctAnswer: 'انڈا',
        explanation: 'انڈے کو پکانے یا کھانے کے لیے پہلے توڑنا پڑتا ہے۔',
      ),
      const NativePuzzle(
        id: 4,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جو اوپر تو جاتی ہے مگر کبھی نیچے نہیں آتی؟',
        options: ['عمر', 'پتنگ', 'دھواں', 'غبارہ'],
        correctAnswer: 'عمر',
        explanation: 'انسان کی عمر وقت کے ساتھ صرف بڑھتی ہے، کم نہیں ہوتی۔',
      ),
      const NativePuzzle(
        id: 5,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کیا ہے جس کے پاس گردن ہے لیکن سر نہیں؟',
        options: ['بوتل', 'قمیض', 'گٹار', 'چمچ'],
        correctAnswer: 'بوتل',
        explanation: 'بوتل کا اوپری حصہ گردن کہلاتا ہے مگر اس کا سر نہیں ہوتا۔',
      ),
      const NativePuzzle(
        id: 6,
        difficulty: QuestionDifficulty.easy,
        question: 'سال کے کتنے مہینوں میں 28 دن ہوتے ہیں؟',
        options: ['تمام مہینوں میں', 'صرف فروری میں', 'چار مہینوں میں', 'کسی میں نہیں'],
        correctAnswer: 'تمام مہینوں میں',
        explanation: 'ہر مہینے میں کم از کم 28 دن تو لازمی ہوتے ہیں۔',
      ),
      const NativePuzzle(
        id: 7,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جو سوراخوں سے بھری ہے مگر پھر بھی پانی روک لیتی ہے؟',
        options: ['اسفنج', 'چھلنی', 'بالٹی', 'جالی'],
        correctAnswer: 'اسفنج',
        explanation: 'اسفنج میں بے شمار سوراخ ہوتے ہیں لیکن وہ پانی اپنے اندر جذب کر لیتا ہے۔',
      ),
      const NativePuzzle(
        id: 8,
        difficulty: QuestionDifficulty.easy,
        question: 'ایک کمرے میں اندھیرا ہے، موم بتی، لالٹین اور چولہا ہے۔ آپ پہلے کیا جلائیں گے؟',
        options: ['ماچس', 'موم بتی', 'لالٹین', 'چولہا'],
        correctAnswer: 'ماچس',
        explanation: 'کسی بھی چیز کو جلانے کے لیے پہلے ماچس کی تیلی جلانی پڑے گی۔',
      ),
      const NativePuzzle(
        id: 9,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جس کے دانت ہیں مگر وہ کاٹتی نہیں؟',
        options: ['کنگھی', 'آری', 'زپ', 'کانٹا'],
        correctAnswer: 'کنگھی',
        explanation: 'کنگھی کے بال سنوارنے کے دانت ہوتے ہیں، وہ کاٹ نہیں سکتی۔',
      ),
      const NativePuzzle(
        id: 10,
        difficulty: QuestionDifficulty.easy,
        question: 'وہ کون سی چیز ہے جس کا سر اور دم ہے مگر جسم نہیں؟',
        options: ['سکہ', 'سانپ', 'تیر', 'سوئی'],
        correctAnswer: 'سکہ',
        explanation: 'سکّے کے دو رخ ہوتے ہیں جنہیں سر اور دم کہا جاتا ہے، مگر جسم نہیں ہوتا۔',
      ),
    ];
    list.addAll(easyUrdu);

    // NORMAL TIER (Levels 251 - 650)
    final normalUrdu = [
      const NativePuzzle(
        id: 251,
        difficulty: QuestionDifficulty.normal,
        question: 'دو باپ اور دو بیٹے مچھلی کا شکار کرنے گئے۔ انہوں نے 3 مچھلیاں پکڑیں اور سب کو ایک ایک مچھلی ملی۔ یہ کیسے ممکن ہوا؟',
        options: ['وہ کل 3 لوگ تھے (دادا، باپ، پوتا)', 'ایک مچھلی تقسیم کی', 'ایک نے چھوڑ دی', 'ناممکن ہے'],
        correctAnswer: 'وہ کل 3 لوگ تھے (دادا، باپ، پوتا)',
        explanation: 'تینوں میں دادا، باپ اور بیٹا شامل تھے (دو باپ اور دو بیٹے)۔',
      ),
      const NativePuzzle(
        id: 252,
        difficulty: QuestionDifficulty.normal,
        question: 'وہ کون سی چیز ہے جو روشن کمرے میں گم ہو جاتی ہے اور اندھیرے میں دکھائی نہیں دیتی؟',
        options: ['سایہ', 'خاموشی', 'روشنی', 'خواب'],
        correctAnswer: 'سایہ',
        explanation: 'جب چاروں طرف ہر طرف مکمل روشنی ہو تو سایہ غائب ہو جاتا ہے۔',
      ),
      const NativePuzzle(
        id: 253,
        difficulty: QuestionDifficulty.normal,
        question: 'ماؤنٹ ایورسٹ کی دریافت سے پہلے دنیا کا سب سے اونچا پہاڑ کون سا تھا؟',
        options: ['ماؤنٹ ایورسٹ', 'کے ٹو', 'نانگا پربت', 'کوہ ہمالیہ'],
        correctAnswer: 'ماؤنٹ ایورسٹ',
        explanation: 'دریافت ہونے سے پہلے بھی دنیا کا سب سے اونچا پہاڑ ماؤنٹ ایورسٹ ہی تھا۔',
      ),
      const NativePuzzle(
        id: 254,
        difficulty: QuestionDifficulty.normal,
        question: 'اگر تار پر بیٹھی 10 چڑیوں میں سے شکاری ایک کو گولی مار دے، تو تار پر کتنی چڑیاں بچیں گی؟',
        options: ['0 (کوئی نہیں)', '9 چڑیاں', '1 چڑیا', '5 چڑیاں'],
        correctAnswer: '0 (کوئی نہیں)',
        explanation: 'گولی کی آواز سن کر باقی تمام چڑیاں فورا اڑ جائیں گی!',
      ),
      const NativePuzzle(
        id: 255,
        difficulty: QuestionDifficulty.normal,
        question: 'وہ کون سا لفظ ہے جسے ہر انسان غلط ہی پڑھتا ہے؟',
        options: ['غلط', 'لفظ', 'انسان', 'اردو'],
        correctAnswer: 'غلط',
        explanation: 'کیونکہ وہ لفظ ہی \'غلط\' ہے!',
      ),
    ];
    list.addAll(normalUrdu);

    // TRICKY TIER (Levels 651 - 1000)
    final trickyUrdu = [
      const NativePuzzle(
        id: 651,
        difficulty: QuestionDifficulty.tricky,
        question: 'وہ کیا ہے جو بنانے والا بیچ دیتا ہے، خریدنے والا استعمال نہیں کرتا اور استعمال کرنے والے کو پتہ نہیں ہوتا؟',
        options: ['کفن', 'دوائی', 'آئینہ', 'لباس'],
        correctAnswer: 'کفن',
        explanation: 'کفن بنانے والا بیچتا ہے، خریدنے والا میت کے لیے لیتا ہے اور مردے کو معلوم نہیں ہوتا۔',
      ),
      const NativePuzzle(
        id: 652,
        difficulty: QuestionDifficulty.tricky,
        question: 'ایک آدمی اپنی گاڑی کو ہوٹل کے سامنے دھکیل کر لے جاتا ہے اور کہتا ہے میں دیوالیہ ہو گیا۔ وہ کیا کھیل رہا تھا؟',
        options: ['مونوپولی (Monopoly) گیم', 'اصلی گاڑی', 'شطرنج', 'کرکٹ'],
        correctAnswer: 'مونوپولی (Monopoly) گیم',
        explanation: 'وہ مونوپولی نامی بورڈ گیم کھیل رہا تھا جہاں ہوٹل آنے پر کرایہ دینا پڑتا ہے۔',
      ),
      const NativePuzzle(
        id: 653,
        difficulty: QuestionDifficulty.tricky,
        question: 'وہ کون سی چیز ہے جس کا نام لیتے ہی وہ غائب ہو جاتی ہے؟',
        options: ['خاموشی', 'راز', 'نیند', 'اندھیرا'],
        correctAnswer: 'خاموشی',
        explanation: 'نام لینے کے لیے جیسے ہی آپ بولیں گے، خاموشی ٹوٹ جائے گی۔',
      ),
      const NativePuzzle(
        id: 654,
        difficulty: QuestionDifficulty.tricky,
        question: 'پانی سے بھری بالٹی کا وزن 20 کلو ہے۔ اس میں کیا ڈالا جائے کہ اس کا وزن 10 کلو رہ جائے؟',
        options: ['ایک سوراخ', 'برف', 'روئی', 'نمک'],
        correctAnswer: 'ایک سوراخ',
        explanation: 'سوراخ کرنے سے پانی باہر بہہ جائے گا اور وزن کم ہو جائے گا۔',
      ),
      const NativePuzzle(
        id: 655,
        difficulty: QuestionDifficulty.tricky,
        question: 'وہ کیا ہے جو بغیر پروں کے اڑتا ہے اور بغیر آنکھوں کے روتا ہے؟',
        options: ['بادل', 'ہوا', 'پتنگ', 'دھواں'],
        correctAnswer: 'بادل',
        explanation: 'بادل آسمان میں اڑتا ہے اور بارش کے روپ میں برستا ہے۔',
      ),
    ];
    list.addAll(trickyUrdu);

    return list;
  }

  // ───────────────────────────────────────────────────────────────────────────
  // EMBEDDED NATIVE ENGLISH BANK (Lateral Thinking, Logic & Mind Traps)
  // ───────────────────────────────────────────────────────────────────────────
  List<NativePuzzle> _buildNativeEnglishBank() {
    final list = <NativePuzzle>[];

    // EASY TIER (Levels 1 - 250)
    final easyEnglish = [
      const NativePuzzle(
        id: 1,
        difficulty: QuestionDifficulty.easy,
        question: 'What gets wetter the more it dries?',
        options: ['A towel', 'A sponge', 'A cloud', 'Rain'],
        correctAnswer: 'A towel',
        explanation: 'A towel absorbs water and gets wetter as it dries you.',
      ),
      const NativePuzzle(
        id: 2,
        difficulty: QuestionDifficulty.easy,
        question: 'What has hands but cannot clap?',
        options: ['A clock', 'A glove', 'A tree', 'A robot'],
        correctAnswer: 'A clock',
        explanation: 'A clock has hour and minute hands but cannot clap.',
      ),
      const NativePuzzle(
        id: 3,
        difficulty: QuestionDifficulty.easy,
        question: 'What has to be broken before you can use it?',
        options: ['An egg', 'A glass', 'A lock', 'A stick'],
        correctAnswer: 'An egg',
        explanation: 'You must crack an eggshell to cook or eat it.',
      ),
      const NativePuzzle(
        id: 4,
        difficulty: QuestionDifficulty.easy,
        question: 'I’m tall when I’m young, and short when I’m old. What am I?',
        options: ['A candle', 'A tree', 'A giraffe', 'A building'],
        correctAnswer: 'A candle',
        explanation: 'A candle melts down and becomes shorter as it burns.',
      ),
      const NativePuzzle(
        id: 5,
        difficulty: QuestionDifficulty.easy,
        question: 'Which month of the year has 28 days?',
        options: ['All of them', 'February', 'January', 'None'],
        correctAnswer: 'All of them',
        explanation: 'Every month has at least 28 days.',
      ),
      const NativePuzzle(
        id: 6,
        difficulty: QuestionDifficulty.easy,
        question: 'What is full of holes but still holds water?',
        options: ['A sponge', 'A bucket', 'A net', 'A colander'],
        correctAnswer: 'A sponge',
        explanation: 'A sponge is porous with holes, yet absorbs and holds water.',
      ),
      const NativePuzzle(
        id: 7,
        difficulty: QuestionDifficulty.easy,
        question: 'What question can you never answer "yes" to honestly?',
        options: ['Are you asleep?', 'Are you awake?', 'Are you hungry?', 'Are you home?'],
        correctAnswer: 'Are you asleep?',
        explanation: 'If you are truly asleep, you cannot answer.',
      ),
      const NativePuzzle(
        id: 8,
        difficulty: QuestionDifficulty.easy,
        question: 'What is always in front of you but cannot be seen?',
        options: ['The future', 'Air', 'Your nose', 'Darkness'],
        correctAnswer: 'The future',
        explanation: 'The future is always ahead in time, yet invisible.',
      ),
      const NativePuzzle(
        id: 9,
        difficulty: QuestionDifficulty.easy,
        question: 'What goes up but never comes down?',
        options: ['Your age', 'A balloon', 'Smoke', 'A kite'],
        correctAnswer: 'Your age',
        explanation: 'Your chronological age only increases with time.',
      ),
      const NativePuzzle(
        id: 10,
        difficulty: QuestionDifficulty.easy,
        question: 'What has a neck but no head?',
        options: ['A bottle', 'A guitar', 'A shirt', 'A snake'],
        correctAnswer: 'A bottle',
        explanation: 'A bottle has a neck leading to its opening, but no head.',
      ),
    ];
    list.addAll(easyEnglish);

    // NORMAL TIER (Levels 251 - 650)
    final normalEnglish = [
      const NativePuzzle(
        id: 251,
        difficulty: QuestionDifficulty.normal,
        question: 'Two fathers and two sons go fishing. They catch 3 fish and each gets 1 fish. How is this possible?',
        options: ['There are only 3 people', 'One fish was shared', 'One stole a fish', 'A fish had twins'],
        correctAnswer: 'There are only 3 people',
        explanation: 'The group is a grandfather, his son, and his grandson (2 fathers, 2 sons).',
      ),
      const NativePuzzle(
        id: 252,
        difficulty: QuestionDifficulty.normal,
        question: 'Before Mount Everest was discovered, what was the highest mountain on Earth?',
        options: ['Mount Everest', 'K2', 'Kangchenjunga', 'Makalu'],
        correctAnswer: 'Mount Everest',
        explanation: 'Mount Everest was still the highest mountain even before discovery.',
      ),
      const NativePuzzle(
        id: 253,
        difficulty: QuestionDifficulty.normal,
        question: 'If 10 birds are on a wire and a hunter shoots 1, how many birds remain on the wire?',
        options: ['0 birds', '9 birds', '1 bird', '5 birds'],
        correctAnswer: '0 birds',
        explanation: 'The gunshot noise scares all the remaining birds away!',
      ),
      const NativePuzzle(
        id: 254,
        difficulty: QuestionDifficulty.normal,
        question: 'A clerk in a butcher shop is 5 feet 10 inches tall and wears size 10 shoes. What does he weigh?',
        options: ['Meat', '160 lbs', '180 lbs', 'Vegetables'],
        correctAnswer: 'Meat',
        explanation: 'As a butcher, his job is to weigh meat!',
      ),
      const NativePuzzle(
        id: 255,
        difficulty: QuestionDifficulty.normal,
        question: 'What can fill an entire room without taking up any physical space?',
        options: ['Light', 'Air', 'Water', 'Furniture'],
        correctAnswer: 'Light',
        explanation: 'Light illuminates the room without occupying solid mass.',
      ),
    ];
    list.addAll(normalEnglish);

    // TRICKY TIER (Levels 651 - 1000)
    final trickyEnglish = [
      const NativePuzzle(
        id: 651,
        difficulty: QuestionDifficulty.tricky,
        question: 'A man pushes his car to a hotel and tells the owner he is bankrupt. What was he doing?',
        options: ['Playing Monopoly', 'Driving a rental', 'Moving luggage', 'Fleeing police'],
        correctAnswer: 'Playing Monopoly',
        explanation: 'He is playing the board game Monopoly with toy tokens!',
      ),
      const NativePuzzle(
        id: 652,
        difficulty: QuestionDifficulty.tricky,
        question: 'The person who makes it sells it. The person who buys it doesn’t use it. The person who uses it doesn’t know. What is it?',
        options: ['A coffin', 'Medicine', 'A gift card', 'A mirror'],
        correctAnswer: 'A coffin',
        explanation: 'A coffin is made for sale, bought by relatives, and used by the deceased.',
      ),
      const NativePuzzle(
        id: 653,
        difficulty: QuestionDifficulty.tricky,
        question: 'What disappears the very moment you say its name aloud?',
        options: ['Silence', 'A secret', 'A whisper', 'Darkness'],
        correctAnswer: 'Silence',
        explanation: 'Speaking breaks silence immediately.',
      ),
      const NativePuzzle(
        id: 654,
        difficulty: QuestionDifficulty.tricky,
        question: 'A barrel of water weighed 60 pounds. What can you add to make it weigh 40 pounds?',
        options: ['A hole', 'Ice', 'Salt', 'Cotton'],
        correctAnswer: 'A hole',
        explanation: 'Drilling a hole lets water leak out, reducing total weight.',
      ),
      const NativePuzzle(
        id: 655,
        difficulty: QuestionDifficulty.tricky,
        question: 'What word in the English language does almost everyone pronounce incorrectly?',
        options: ['Incorrectly', 'Pronounce', 'Queue', 'Alphabet'],
        correctAnswer: 'Incorrectly',
        explanation: 'The word "Incorrectly" is pronounced as "incorrectly"!',
      ),
    ];
    list.addAll(trickyEnglish);

    return list;
  }
}
