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

  static final Map<String, Map<String, LocalizedPuzzleData>> _translations = {
    // Urdu
    'ur': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'کون سا لفظ سب سے لمبا ہے؟',
        options: ['سانپ (Snake)', 'ٹرین (Train)', 'سڑک (Road)', 'قطار (Queue)'],
        correctAnswer: 'قطار (Queue)',
        explanation: 'لفظ Queue میں پانچ حروف ہیں جو باقی تمام اختیارات سے زیادہ ہیں۔',
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
        question: 'کس کے پاس چابیاں (keys) ہوتی ہیں لیکن وہ تالے نہیں کھول سکتا؟',
        options: ['پیانو', 'دروازہ', 'گاڑی', 'صندوق'],
        correctAnswer: 'پیانو',
        explanation: 'پیانو کے بٹنوں کو چابیاں (keys) کہتے ہیں لیکن وہ تالے نہیں کھولتیں۔',
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
        explanation: 'ڈاک ٹکٹ خط کے کونے پر چپکا رہتا ہے اور سفر کرتا ہے۔',
      ),
      'In a dark room, what do you light first?': const LocalizedPuzzleData(
        question: 'تاریک کمرے میں آپ سب سے پہلے کیا جلاتے ہیں؟',
        options: ['ماچس', 'موم بتی', 'چراغ', 'آتش دان'],
        correctAnswer: 'ماچس',
        explanation: 'کسی بھی چیز کو جلانے سے پہلے ماچس جلانی پڑتی ہے۔',
      ),
      'What has many teeth but cannot bite?': const LocalizedPuzzleData(
        question: 'کس کے بہت سے دانت ہوتے ہیں مگر کاٹ نہیں سکتا؟',
        options: ['کنگھی', 'شارک', 'آری', 'زپ'],
        correctAnswer: 'کنگھی',
        explanation: 'کنگھی کے دانت بال سنوارنے کے لیے ہوتے ہیں، کاٹنے کے لیے نہیں۔',
      ),
      'What goes up but never comes down?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو ہمیشہ بڑھتی ہے مگر کبھی کم نہیں ہوتی؟',
        options: ['عمر', 'غبارہ', 'دھواں', 'لفٹ'],
        correctAnswer: 'عمر',
        explanation: 'وقت گزرنے کے ساتھ عمر ہمیشہ بڑھتی ہے۔',
      ),
      'What has hands but cannot clap?': const LocalizedPuzzleData(
        question: 'کس کے ہاتھ ہوتے ہیں لیکن تالی نہیں بجا سکتا؟',
        options: ['گھڑی', 'بچہ', 'روبوٹ', 'دستانے'],
        correctAnswer: 'گھڑی',
        explanation: 'گھڑی کی سوئیوں کو ہاتھ کہا جاتا ہے۔',
      ),
      'What is full of holes but holds water?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جس میں سوراخ ہوتے ہیں پھر بھی پانی روکتا ہے؟',
        options: ['اسفنج (Sponge)', 'بالٹی', 'جال', 'پیالہ'],
        correctAnswer: 'اسفنج (Sponge)',
        explanation: 'اسفنج سوراخوں کے باوجود پانی جذب کر کے رکھتا ہے۔',
      ),
      'What breaks when you say its name?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو نام لیتے ہی ٹوٹ جاتی ہے؟',
        options: ['خاموشی', 'شیشہ', 'وعدہ', 'کوڈ'],
        correctAnswer: 'خاموشی',
        explanation: 'بولنے سے خاموشی ختم ہو جاتی ہے۔',
      ),
      'Which is heavier?': const LocalizedPuzzleData(
        question: 'کون سا زیادہ وزنی ہے؟',
        options: ['1 کلو پر (Feathers)', '1 کلو پتھر (Rocks)', 'پتھر', 'پر'],
        correctAnswer: '1 کلو پر (Feathers)',
        explanation: 'دونوں کا وزن 1 کلو ہے اس لیے دونوں برابر ہیں۔',
      ),
      'What has one eye but cannot see?': const LocalizedPuzzleData(
        question: 'کس کی ایک آنکھ ہوتی ہے لیکن وہ دیکھ نہیں سکتی؟',
        options: ['سوئی (Needle)', 'سائکلوپس', 'کیمرہ', 'طوفان'],
        correctAnswer: 'سوئی (Needle)',
        explanation: 'سوئی کے سوراخ کو آنکھ کہا جاتا ہے۔',
      ),
      'What can you catch but not throw?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جسے آپ پکڑ سکتے ہیں مگر پھینک نہیں سکتے؟',
        options: ['سردی/زکام (Cold)', 'گیند', 'مچھلی', 'سایہ'],
        correctAnswer: 'سردی/زکام (Cold)',
        explanation: 'آپ زکام یا سردی پکڑ (catch cold) سکتے ہیں مگر پھینک نہیں سکتے۔',
      ),
      'What has a neck but no head?': const LocalizedPuzzleData(
        question: 'کس کی گردن ہوتی ہے لیکن سر نہیں ہوتا؟',
        options: ['بوتل (Bottle)', 'قمیض', 'گٹار', 'چمچ'],
        correctAnswer: 'بوتل (Bottle)',
        explanation: 'بوتل کے اوپری تنگ حصے کو گردن (neck) کہا جاتا ہے۔',
      ),
      'Which word gets shorter when letters are added?': const LocalizedPuzzleData(
        question: 'کون سا لفظ حروف شامل کرنے پر چھوٹا ہو جاتا ہے؟',
        options: ['Short', 'Small', 'Brief', 'Little'],
        correctAnswer: 'Short',
        explanation: 'لفظ "Short" میں "er" شامل کرنے سے "Shorter" بن جاتا ہے۔',
      ),
      'What appears once in minute and twice in moment?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو Minute میں ایک بار اور Moment میں دو بار آتا ہے؟',
        options: ['حرف M', 'سیکنڈ', 'وقت', 'حرف E'],
        correctAnswer: 'حرف M',
        explanation: 'لفظ Minute میں ایک بار M اور Moment میں دو بار M آتا ہے۔',
      ),
      'Which one is not a fruit?': const LocalizedPuzzleData(
        question: 'ان میں سے کون سا پھل نہیں ہے؟',
        options: ['آلو (Potato)', 'ٹماٹر (Tomato)', 'سیب (Apple)', 'کیلا (Banana)'],
        correctAnswer: 'آلو (Potato)',
        explanation: 'آلو ایک سبزی (جڑ) ہے، پھل نہیں۔',
      ),
      'What comes next: 2, 4, 6, ?': const LocalizedPuzzleData(
        question: 'اگلا نمبر کیا ہوگا: 2, 4, 6, ؟',
        options: ['8', '7', '10', '9'],
        correctAnswer: '8',
        explanation: 'ہر بار 2 کا اضافہ ہو رہا ہے، اگلا نمبر 8 ہے۔',
      ),
      'What comes next: A, C, E, ?': const LocalizedPuzzleData(
        question: 'اگلا حرف کیا ہوگا: A, C, E, ؟',
        options: ['G', 'F', 'H', 'D'],
        correctAnswer: 'G',
        explanation: 'ایک ایک حرف چھوڑ کر اگلا حرف G ہے۔',
      ),
      'What is in front of you but unseen?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو آپ کے سامنے ہے مگر دکھائی نہیں دیتا؟',
        options: ['مستقبل (Future)', 'ہوا (Air)', 'خواب (Dream)', 'ماضی (Past)'],
        correctAnswer: 'مستقبل (Future)',
        explanation: 'مستقبل ہمیشہ ہمارے آگے ہوتا ہے مگر اسے دیکھا نہیں جا سکتا۔',
      ),
      'Which one is a planet?': const LocalizedPuzzleData(
        question: 'ان میں سے کون سا سیارہ ہے؟',
        options: ['مریخ (Mars)', 'سورج (Sun)', 'چاند (Moon)', 'قطب تارہ'],
        correctAnswer: 'مریخ (Mars)',
        explanation: 'مریخ ہمارے نظام شمسی کا سیارہ ہے۔',
      ),
      'I speak without a mouth and hear without ears. What am I?': const LocalizedPuzzleData(
        question: 'میں منہ کے بغیر بولتا ہوں اور کانوں کے بغیر سنتا ہوں۔ میں کیا ہوں؟',
        options: ['گونج (Echo)', 'ہوا (Wind)', 'سایہ (Shadow)', 'ریڈیو (Radio)'],
        correctAnswer: 'گونج (Echo)',
        explanation: 'گونج آواز کو لوٹا کر بولتی اور سنتی ہے۔',
      ),
      'A boat is full of people, yet not a single person is on board. Why?': const LocalizedPuzzleData(
        question: 'کشتی لوگوں سے بھری ہے مگر کوئی اکیلا انسان نہیں ہے۔ کیوں؟',
        options: ['سب شادی شدہ تھے (Married)', 'کشتی خالی تھی', 'سب بچے تھے', 'روبوٹ تھے'],
        correctAnswer: 'سب شادی شدہ تھے (Married)',
        explanation: 'سب لوگ جوڑے (شادی شدہ) تھے، اس لیے کوئی "سنگل" نہیں تھا۔',
      ),
      'The person who makes it does not want it. The buyer does not use it. What is it?': const LocalizedPuzzleData(
        question: 'بنانے والا اسے نہیں چاہتا، خریدنے والا استعمال نہیں کرتا۔ وہ کیا ہے؟',
        options: ['تابوت (Coffin)', 'گاڑی', 'گھر', 'کپڑے'],
        correctAnswer: 'تابوت (Coffin)',
        explanation: 'تابوت میت کے لیے خریدا جاتا ہے، خریدار خود استعمال نہیں کرتا۔',
      ),
      'A cowboy rides into town on Friday, stays 2 days, and leaves on Friday. How?': const LocalizedPuzzleData(
        question: 'ایک کاؤ بوائے جمعہ کو شہر آیا، 2 دن رکا، اور جمعہ کو واپس گیا۔ کیسے؟',
        options: ['گھوڑے کا نام جمعہ تھا (Friday)', 'ٹائم ٹریول', 'ہفتہ تبدیل ہوا', 'کاؤنٹنگ غلط تھی'],
        correctAnswer: 'گھوڑے کا نام جمعہ تھا (Friday)',
        explanation: 'اس کے گھوڑے کا نام فرائیڈے (جمعہ) تھا۔',
      ),
      'What runs around the entire yard without ever moving?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو پورے صحن کے گرد گھومتی ہے مگر کبھی حرکت نہیں کرتی؟',
        options: ['باڑ (Fence)', 'راستہ', 'گھاس', 'دیوار'],
        correctAnswer: 'باڑ (Fence)',
        explanation: 'باڑ پورے صحن کے ارد گرد قائم رہتی ہے بغیر ہلے۔',
      ),
      'What begins with T, finishes with T, and has T inside it?': const LocalizedPuzzleData(
        question: 'کون سا لفظ T سے شروع، T پر ختم اور اس کے اندر T (چائے) ہوتی ہے؟',
        options: ['Teapot (چائے دانی)', 'Tent', 'Toast', 'Target'],
        correctAnswer: 'Teapot (چائے دانی)',
        explanation: 'Teapot ٹی سے شروع اور ختم ہوتا ہے اور اندر چائے (Tea) ہوتی ہے۔',
      ),
      'How many letters are in "the alphabet"?': const LocalizedPuzzleData(
        question: 'لفظ "the alphabet" میں کتنے حروف ہیں؟',
        options: ['11', '26', '24', '10'],
        correctAnswer: '11',
        explanation: 'لفظ "t-h-e-a-l-p-h-a-b-e-t" میں 11 حروف ہیں۔',
      ),
      'What has a head and a tail, but no body?': const LocalizedPuzzleData(
        question: 'کس کا سر اور دم (Head & Tail) ہوتی ہے لیکن جسم نہیں ہوتا؟',
        options: ['سکہ (Coin)', 'سانپ', 'تیر', 'چھپکلی'],
        correctAnswer: 'سکہ (Coin)',
        explanation: 'سکے کے دو رخوں کو ہیڈ اور ٹیل کہتے ہیں۔',
      ),
      'What belongs to you, but others use it far more than you do?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو آپ کا ہے مگر دوسرے آپ سے زیادہ استعمال کرتے ہیں؟',
        options: ['آپ کا نام (Your Name)', 'آپ کا فون', 'آپ کا پیسہ', 'آپ کی گاڑی'],
        correctAnswer: 'آپ کا نام (Your Name)',
        explanation: 'آپ کے نام کو دوسرے لوگ پکارنے کے لیے زیادہ استعمال کرتے ہیں۔',
      ),
      'What has words, but never speaks?': const LocalizedPuzzleData(
        question: 'کس میں الفاظ ہوتے ہیں لیکن وہ کبھی بولتی نہیں؟',
        options: ['کتاب (Book)', 'ٹی وی', 'اخبار', 'ریڈیو'],
        correctAnswer: 'کتاب (Book)',
        explanation: 'کتاب میں الفاظ لکھے ہوتے ہیں لیکن وہ خود نہیں بولتی۔',
      ),
      'If you drop me I crack, but smile at me and I smile back. What am I?': const LocalizedPuzzleData(
        question: 'اگر گراؤ تو ٹوٹ جاؤں، مسکراؤ تو مسکراؤں۔ میں کیا ہوں؟',
        options: ['آئینہ (Mirror)', 'گلاس', 'تصویر', 'شیشہ'],
        correctAnswer: 'آئینہ (Mirror)',
        explanation: 'آئینہ گرنے سے ٹوٹ جاتا ہے اور مسکرانے پر آپ کا عکس لوٹاتا ہے۔',
      ),
      'What can fill an entire room without taking up any physical space?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو جگہ گھیرے بغیر پورا کمرہ بھر سکتی ہے؟',
        options: ['روشنی (Light)', 'دھواں', 'ہوا', 'خوشبو'],
        correctAnswer: 'روشنی (Light)',
        explanation: 'روشنی پورے کمرے کو روشن کرتی ہے بغیر مادی جگہ گھیرے۔',
      ),
      'What has cities but no houses, and rivers but no water?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جس میں شہر ہیں مگر مکان نہیں، دریا ہیں مگر پانی نہیں؟',
        options: ['نقشہ (Map)', 'کتاب', 'خواب', 'تصویر'],
        correctAnswer: 'نقشہ (Map)',
        explanation: 'نقشے پر شہر اور دریا دکھائے جاتے ہیں مگر وہ حقیقی نہیں ہوتے۔',
      ),
      'The more there is of this, the less you can see. What is it?': const LocalizedPuzzleData(
        question: 'یہ جتنا زیادہ ہو، اتنا ہی کم دکھائی دیتا ہے۔ وہ کیا ہے؟',
        options: ['اندھیرا (Darkness)', 'روشنی', 'دھواں', 'کہر'],
        correctAnswer: 'اندھیرا (Darkness)',
        explanation: 'اندھیرا جتنا گہرا ہو، بصارت اتنی ہی کم ہو جاتی ہے۔',
      ),
      'I have branches, but no fruit, trunk, or leaves. What am I?': const LocalizedPuzzleData(
        question: 'میری شاخیں (Branches) ہیں مگر پھل، تنا یا پتے نہیں۔ میں کیا ہوں؟',
        options: ['بینک (Bank)', 'درخت', 'دریا', 'سڑک'],
        correctAnswer: 'بینک (Bank)',
        explanation: 'بینک کی مختلف شاخیں (برانچز) ہوتی ہیں۔',
      ),
      'What can you break without ever touching or dropping it?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جسے آپ چھوئے یا گرائے بغیر بھی توڑ سکتے ہیں؟',
        options: ['وعدہ (Promise)', 'دل', 'شیشہ', 'خاموشی'],
        correctAnswer: 'وعدہ (Promise)',
        explanation: 'وعدہ زبانی طور پر توڑا جا سکتا ہے۔',
      ),
      'What architectural invention allows you to look right through a wall?': const LocalizedPuzzleData(
        question: 'وہ کون سی ایجاد ہے جو دیوار کے پار دیکھنے کی اجازت دیتی ہے؟',
        options: ['کھڑکی (Window)', 'دروازہ', 'دوربین', 'آئینہ'],
        correctAnswer: 'کھڑکی (Window)',
        explanation: 'کھڑکی دیوار کے اندر نصب ہو کر پار دیکھنے کی سہولت دیتی ہے۔',
      ),
      'If two is company, and three is a crowd, what are four and five?': const LocalizedPuzzleData(
        question: 'اگر دو کمپنی ہیں اور تین بھیڑ، تو چار اور پانچ کیا ہیں؟',
        options: ['9 (Nine)', 'بھیڑ', 'دوست', 'پارٹی'],
        correctAnswer: '9 (Nine)',
        explanation: 'چار اور پانچ مل کر نو (4 + 5 = 9) بنتے ہیں۔',
      ),
      'What goes up and down constantly but never moves an inch?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو مسلسل اوپر نیچے ہوتی ہے مگر ایک انچ نہیں ہلتی؟',
        options: ['سیڑھیاں (Stairs)', 'لفٹ', 'درجہ حرارت', 'جھولا'],
        correctAnswer: 'سیڑھیاں (Stairs)',
        explanation: 'سیڑھیاں اوپر اور نیچے کی طرف جاتی ہیں مگر اپنی جگہ ساکت رہتی ہیں۔',
      ),
      'Feed me and I live, but give me a drink of water and I die. What am I?': const LocalizedPuzzleData(
        question: 'کھلانے سے زندہ رہتی ہوں، پانی پلانے سے مر جاتی ہوں۔ میں کیا ہوں؟',
        options: ['آگ (Fire)', 'پودا', 'انسان', 'مٹی'],
        correctAnswer: 'آگ (Fire)',
        explanation: 'آگ لکڑی سے بھڑکتی ہے اور پانی سے بجھ جاتی ہے۔',
      ),
      'What has to be broken before you can ever use it?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جسے استعمال کرنے سے پہلے توڑنا لازمی ہے؟',
        options: ['انڈا (Egg)', 'اخروٹ', 'تالہ', 'ناریل'],
        correctAnswer: 'انڈا (Egg)',
        explanation: 'انڈے کا چھلکا توڑے بغیر اسے استعمال نہیں کیا جا سکتا۔',
      ),
      'I am tall when I am young, and short when I am old. What am I?': const LocalizedPuzzleData(
        question: 'نئی ہوں تو لمبی، پرانی ہوں تو چھوٹی ہو جاتی ہوں۔ میں کیا ہوں؟',
        options: ['موم بتی (Candle)', 'پنسل', 'درخت', 'رسی'],
        correctAnswer: 'موم بتی (Candle)',
        explanation: 'موم بتی جلنے کے ساتھ گھلتی جاتی ہے اور چھوٹی ہو جاتی ہے۔',
      ),
      'What begins with an E and contains only one single letter?': const LocalizedPuzzleData(
        question: 'کون سا لفظ E سے شروع ہوتا ہے اور اس میں صرف ایک خط (Letter) ہوتا ہے؟',
        options: ['لفافہ (Envelope)', 'آنکھ (Eye)', 'انڈا (Egg)', 'زمین (Earth)'],
        correctAnswer: 'لفافہ (Envelope)',
        explanation: 'لفافہ (Envelope) E سے شروع ہوتا ہے اور اس کے اندر خط (letter) ہوتا ہے۔',
      ),
      'A man pushes his car to a hotel and immediately declares bankruptcy. Why?': const LocalizedPuzzleData(
        question: 'ایک شخص اپنی کار ہوٹل لے جاتا ہے اور دیوالیہ ہو جاتا ہے۔ کیوں؟',
        options: ['اجارہ داری گیم کھیل رہا تھا (Monopoly)', 'کار خراب تھی', 'ہوٹل مہنگا تھا', 'قرض تھا'],
        correctAnswer: 'اجارہ داری گیم کھیل رہا تھا (Monopoly)',
        explanation: 'وہ مونوپولی (Monopoly) بورڈ گیم کھیل رہا تھا۔',
      ),
      'How can a person go 25 days without sleeping?': const LocalizedPuzzleData(
        question: 'ایک انسان بغیر سوئے 25 دن کیسے گزار سکتا ہے؟',
        options: ['وہ رات کو سوتا ہے (Sleeps at night)', 'کافی پی کر', 'ناممکن ہے', 'آرام کر کے'],
        correctAnswer: 'وہ رات کو سوتا ہے (Sleeps at night)',
        explanation: 'وہ دن میں نہیں سوتا بلکہ رات کو باقاعدہ سوتا ہے۔',
      ),
      'What comes down from the sky but never goes back up?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو آسمان سے نیچے آتی ہے مگر کبھی اوپر واپس نہیں جاتی؟',
        options: ['بارش (Rain)', 'برف', 'بجلی', 'اولے'],
        correctAnswer: 'بارش (Rain)',
        explanation: 'بارش کے قطرے گرنے کے بعد دوبارہ بارش کی شکل میں اوپر نہیں جاتے۔',
      ),
      'Where does today always come before yesterday?': const LocalizedPuzzleData(
        question: 'آج (Today) ہمیشہ کل (Yesterday) سے پہلے کہاں آتا ہے؟',
        options: ['لغت میں (Dictionary)', 'کیلنڈر میں', 'خواب میں', 'گھڑی میں'],
        correctAnswer: 'لغت میں (Dictionary)',
        explanation: 'لغت میں حروفِ تہجی کے لحاظ سے T کا حرف Y سے پہلے آتا ہے۔',
      ),
      'What can you hold in your right hand, but never in your left hand?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جسے آپ دائیں ہاتھ سے پکڑ سکتے ہیں مگر بائیں ہاتھ سے نہیں؟',
        options: ['آپ کا بایاں ہاتھ (Left Hand)', 'دایاں ہاتھ', 'انگوٹھا', 'کلائی'],
        correctAnswer: 'آپ کا بایاں ہاتھ (Left Hand)',
        explanation: 'بایاں ہاتھ اپنے آپ کو خود نہیں پکڑ سکتا۔',
      ),
      'What has legs, but cannot take a single step?': const LocalizedPuzzleData(
        question: 'کس کی ٹانگیں ہوتی ہیں لیکن وہ ایک قدم بھی نہیں چل سکتی؟',
        options: ['میز (Table)', 'کرسی', 'بستر', 'گھڑی'],
        correctAnswer: 'میز (Table)',
        explanation: 'میز کے پایوں کو ٹانگیں کہا جاتا ہے مگر وہ چل نہیں سکتی۔',
      ),
      'What has a thumb and four fingers, but is not alive or human?': const LocalizedPuzzleData(
        question: 'کس کا انگوٹھا اور چار انگلیاں ہوتی ہیں لیکن وہ جاندار نہیں؟',
        options: ['دستانہ (Glove)', 'روبوٹ', 'پتلا', 'مجسمہ'],
        correctAnswer: 'دستانہ (Glove)',
        explanation: 'دستانے میں ہاتھ کی شکل کے انگوٹھے اور انگلیاں بنی ہوتی ہیں۔',
      ),
      'If an electric train travels north at 60 mph, which way does the smoke blow?': const LocalizedPuzzleData(
        question: 'الیکٹرک ٹرین 60 میل فی گھنٹہ شمال جا رہی ہے، دھواں کدھر جائے گا؟',
        options: ['کوئی دھواں نہیں ہوتا (No smoke)', 'جنوب', 'مغرب', 'شمال'],
        correctAnswer: 'کوئی دھواں نہیں ہوتا (No smoke)',
        explanation: 'الیکٹرک ٹرین میں دھواں پیدا ہی نہیں ہوتا۔',
      ),
      'What gets sharper the more you train and challenge it?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جسے جتنا استعمال اور چیلنج کرو اتنا ہی تیز ہوتا ہے؟',
        options: ['دماغ (Brain/Mind)', 'چھری', 'تلوار', 'پنسل'],
        correctAnswer: 'دماغ (Brain/Mind)',
        explanation: 'دماغ کو چیلنج کرنے سے اس کی فکری صلاحیت تیز ہوتی ہے۔',
      ),
      '2 fathers and 2 sons caught 3 fish, 1 each. How is this possible?': const LocalizedPuzzleData(
        question: '2 باپ اور 2 بیٹوں نے 3 مچھلیاں پکڑیں، ہر ایک کو 1 ملی۔ کیسے؟',
        options: ['دادا، باپ اور پوتا تھے (3 people)', 'ایک مچھلی چھوٹی تھی', 'دو مچھلیاں مشترک تھیں', 'جادو تھا'],
        correctAnswer: 'دادا، باپ اور پوتا تھے (3 people)',
        explanation: 'وہ کل 3 لوگ تھے: دادا (باپ)، اس کا بیٹا، اور پوتا۔',
      ),
      'What runs constantly without walking, and has a bed but never sleeps?': const LocalizedPuzzleData(
        question: 'وہ کیا ہے جو بغیر چلے دوڑتا ہے اور بستر ہے مگر سوتا نہیں؟',
        options: ['دریا (River)', 'ہوا', 'گاڑی', 'وقت'],
        correctAnswer: 'دریا (River)',
        explanation: 'دریا کی گزرگاہ کو ریور بیڈ (Riverbed) کہتے ہیں اور وہ مسلسل بہتا ہے۔',
      ),
      'What kind of band never plays musical instruments?': const LocalizedPuzzleData(
        question: 'کون سا بینڈ کبھی موسیقی کے آلات نہیں بجاتا؟',
        options: ['ربڑ بینڈ (Rubber band)', 'راک بینڈ', 'جاز بینڈ', 'مارچنگ بینڈ'],
        correctAnswer: 'ربڑ بینڈ (Rubber band)',
        explanation: 'ربڑ بینڈ لچکدار فیتہ ہوتا ہے، موسیقی کا گروہ نہیں۔',
      ),
      'Which word in every standard English dictionary is spelled incorrectly?': const LocalizedPuzzleData(
        question: 'کون سا لفظ ہر انگریزی لغت میں "غلط" (Incorrectly) لکھا جاتا ہے؟',
        options: ['Incorrectly', 'Wrong', 'Mistake', 'False'],
        correctAnswer: 'Incorrectly',
        explanation: 'لفظ "Incorrectly" کے ہجے ہی "Incorrectly" ہوتے ہیں۔',
      ),
      'A plane crashes on the exact border of US and Canada. Where are survivors buried?': const LocalizedPuzzleData(
        question: 'طیارہ بارڈر پر حادثے کا شکار ہوا، زندہ بچ جانے والوں کو کہاں دفنایا جائے گا؟',
        options: ['زندہ لوگوں کو دفنایا نہیں جاتا (Survivors are alive)', 'امریکہ', 'کینیڈا', 'بارڈر پر'],
        correctAnswer: 'زندہ لوگوں کو دفنایا نہیں جاتا (Survivors are alive)',
        explanation: 'زندہ بچ جانے والے (Survivors) حیات ہوتے ہیں، انہیں دفنایا نہیں جاتا۔',
      ),
      'What body part tastes food much better than it smells?': const LocalizedPuzzleData(
        question: 'جسم کا کون سا حصہ سونگھنے سے کہیں بہتر کھانا چکھتا ہے؟',
        options: ['زبان (Tongue)', 'ناک', 'ہونٹ', 'دانت'],
        correctAnswer: 'زبان (Tongue)',
        explanation: 'زبان پر ذائقے کے غدود ہوتے ہیں جن سے کھانے کا ذائقہ معلوم ہوتا ہے۔',
      ),
      'What object has a spine, but has absolutely no bones inside?': const LocalizedPuzzleData(
        question: 'کس کی ریڑھ کی ہڈی (Spine) ہوتی ہے مگر اندر ہڈی نہیں ہوتی؟',
        options: ['کتاب (Book)', 'سیب', 'سانپ', 'کرسی'],
        correctAnswer: 'کتاب (Book)',
        explanation: 'کتاب کی جلد کی پشت کو کتاب کی اسپائن (Spine) کہا جاتا ہے۔',
      ),
      'What household item loses its head in the morning and gets it back at night?': const LocalizedPuzzleData(
        question: 'وہ کون سی چیز ہے جس کا سر صبح اتر جاتا ہے اور رات کو واپس آتا ہے؟',
        options: ['تکیہ (Pillow)', 'ٹوپی', 'کنگھی', 'بستر'],
        correctAnswer: 'تکیہ (Pillow)',
        explanation: 'صبح اٹھتے ہی سر تکیے سے ہٹ جاتا ہے اور رات کو سر واپس تکیے پر آتا ہے۔',
      ),
      'What celestial or household item has rings, but no fingers?': const LocalizedPuzzleData(
        question: 'کس کے چھلے/حلقے (Rings) ہوتے ہیں لیکن انگلیاں نہیں ہوتیں؟',
        options: ['سیارہ زحل (Saturn)', 'ٹیلیفون', 'گھڑی', 'پردہ'],
        correctAnswer: 'سیارہ زحل (Saturn)',
        explanation: 'سیارہ زحل (Saturn) کے گرد گیسی چھلے ہوتے ہیں۔',
      ),
    },

    // Hindi
    'hi': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'कौन सा शब्द सबसे लंबा है?',
        options: ['Snake', 'Train', 'Road', 'Queue'],
        correctAnswer: 'Queue',
        explanation: 'Queue में 5 अक्षर हैं जो बाकी विकल्पों से अधिक हैं।',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'सुखाते समय क्या और गीला हो जाता है?',
        options: ['तौलिया', 'सूरज', 'आग', 'रेत'],
        correctAnswer: 'तौलिया',
        explanation: 'तौलिया किसी चीज़ को सुखाते हुए पानी सोख लेता है।',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'किस महीने में 28 दिन होते हैं?',
        options: ['फ़रवरी', 'जनवरी', 'सभी महीनों में', 'जून'],
        correctAnswer: 'सभी महीनों में',
        explanation: 'हर महीने में कम से कम 28 दिन होते हैं।',
      ),
      "What has keys but can't open locks?": const LocalizedPuzzleData(
        question: 'किसके पास चाबियां (keys) हैं पर ताला नहीं खोल सकता?',
        options: ['पियानो', 'दरवाजा', 'कार', 'तिजोरी'],
        correctAnswer: 'पियानो',
        explanation: 'पियानो में संगीत की चाबियां होती हैं, ताले की नहीं।',
      ),
      'Which number is half of 8?': const LocalizedPuzzleData(
        question: '8 का आधा क्या है?',
        options: ['4', '3', '0', 'निर्भर करता है'],
        correctAnswer: '4',
        explanation: '8 का आधा 4 होता है।',
      ),
      'What has a face and two hands but no arms?': const LocalizedPuzzleData(
        question: 'किसका चेहरा और दो हाथ होते हैं लेकिन बाहें नहीं होतीं?',
        options: ['घड़ी', 'रोबोट', 'इंसान', 'आईना'],
        correctAnswer: 'घड़ी',
        explanation: 'घड़ी का डायल चेहरा और सुइयां हाथ होती हैं।',
      ),
      'What stays in a corner while traveling?': const LocalizedPuzzleData(
        question: 'सफर करते हुए भी कोने में कौन रहता है?',
        options: ['डाक टिकट', 'विमान', 'नक्शा', 'दिशा सूचक'],
        correctAnswer: 'डाक टिकट',
        explanation: 'डाक टिकट लिफाफे के कोने पर लगा रहता है।',
      ),
      'In a dark room, what do you light first?': const LocalizedPuzzleData(
        question: 'अंधेरे कमरे में सबसे पहले क्या जलाएंगे?',
        options: ['माचिस', 'मोमबत्ती', 'दीपक', 'अंगीठी'],
        correctAnswer: 'माचिस',
        explanation: 'कुछ भी जलाने से पहले माचिस जलानी पड़ती है।',
      ),
      'What has many teeth but cannot bite?': const LocalizedPuzzleData(
        question: 'किसके बहुत सारे दांत होते हैं पर काट नहीं सकता?',
        options: ['कंघी', 'शार्क', 'आरी', 'ज़िप'],
        correctAnswer: 'कंघी',
        explanation: 'कंघी के दांत बाल संवारने के लिए होते हैं।',
      ),
      'What goes up but never comes down?': const LocalizedPuzzleData(
        question: 'वह क्या है जो हमेशा बढ़ता है, घटता नहीं?',
        options: ['उम्र', 'गुब्बारा', 'धुआं', 'लिफ्ट'],
        correctAnswer: 'उम्र',
        explanation: 'समय के साथ उम्र हमेशा बढ़ती है।',
      ),
      'What has hands but cannot clap?': const LocalizedPuzzleData(
        question: 'किसके हाथ हैं पर ताली नहीं बजा सकता?',
        options: ['घड़ी', 'बच्चा', 'रोबोट', 'दस्ताने'],
        correctAnswer: 'घड़ी',
        explanation: 'घड़ी की सुइयों को हाथ कहते हैं।',
      ),
      'What is full of holes but holds water?': const LocalizedPuzzleData(
        question: 'किसमें छेद होते हैं फिर भी पानी रोक लेता है?',
        options: ['स्पंज', 'बाल्टी', 'जाल', 'कप'],
        correctAnswer: 'स्पंज',
        explanation: 'स्पंज छेदों के बावजूद पानी सोख कर रखता है।',
      ),
      'What breaks when you say its name?': const LocalizedPuzzleData(
        question: 'नाम लेते ही क्या टूट जाता है?',
        options: ['खामोशी', 'कांच', 'वादा', 'कोड'],
        correctAnswer: 'खामोशी',
        explanation: 'कुछ भी बोलने पर खामोशी टूट जाती है।',
      ),
      'Which is heavier?': const LocalizedPuzzleData(
        question: 'कौन सा ज्यादा भारी है?',
        options: ['1 किलो पंख (Feathers)', '1 किलो पत्थर (Rocks)', 'पत्थर', 'पंख'],
        correctAnswer: '1 किलो पंख (Feathers)',
        explanation: 'दोनों का वजन 1 किलो है, इसलिए दोनों बराबर हैं।',
      ),
      'What has one eye but cannot see?': const LocalizedPuzzleData(
        question: 'किसकी एक आंख होती है पर वह देख नहीं सकती?',
        options: ['सुई (Needle)', 'तूफान', 'कैमरा', 'साइक्लोप्स'],
        correctAnswer: 'सुई (Needle)',
        explanation: 'सुई के छेद को आंख कहा जाता है।',
      ),
      'What can you catch but not throw?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसे आप पकड़ सकते हैं पर फेंक नहीं सकते?',
        options: ['सर्दी/जुकाम (Cold)', 'गेंद', 'मछली', 'छाया'],
        correctAnswer: 'सर्दी/जुकाम (Cold)',
        explanation: 'आप सर्दी (cold) पकड़ सकते हैं पर उसे फेंक नहीं सकते।',
      ),
      'What has a neck but no head?': const LocalizedPuzzleData(
        question: 'किसकी गर्दन होती है पर सिर नहीं होता?',
        options: ['बोतल (Bottle)', 'शर्ट', 'गिटार', 'चम्मच'],
        correctAnswer: 'बोतल (Bottle)',
        explanation: 'बोतल के संकरे ऊपरी हिस्से को गर्दन कहा जाता है।',
      ),
      'Which word gets shorter when letters are added?': const LocalizedPuzzleData(
        question: 'अक्षर जोड़ने पर कौन सा शब्द छोटा (Shorter) हो जाता है?',
        options: ['Short', 'Small', 'Brief', 'Little'],
        correctAnswer: 'Short',
        explanation: 'Short में "er" जोड़ने से "Shorter" बनता है।',
      ),
      'What appears once in minute and twice in moment?': const LocalizedPuzzleData(
        question: 'Minute में एक बार और Moment में दो बार क्या आता है?',
        options: ['अक्षर M', 'सेकंड', 'समय', 'अक्षर E'],
        correctAnswer: 'अक्षर M',
        explanation: 'Minute में एक M और Moment में दो M होते हैं।',
      ),
      'Which one is not a fruit?': const LocalizedPuzzleData(
        question: 'इनमें से कौन सा फल नहीं है?',
        options: ['आलू (Potato)', 'टमाटर (Tomato)', 'सेब (Apple)', 'केला (Banana)'],
        correctAnswer: 'आलू (Potato)',
        explanation: 'आलू एक कंद (सब्जी) है, फल नहीं।',
      ),
      'What comes next: 2, 4, 6, ?': const LocalizedPuzzleData(
        question: 'अगली संख्या क्या होगी: 2, 4, 6, ?',
        options: ['8', '7', '10', '9'],
        correctAnswer: '8',
        explanation: 'प्रत्येक पद में 2 जोड़ा जा रहा है, अगला 8 है।',
      ),
      'What comes next: A, C, E, ?': const LocalizedPuzzleData(
        question: 'अगला अक्षर क्या होगा: A, C, E, ?',
        options: ['G', 'F', 'H', 'D'],
        correctAnswer: 'G',
        explanation: 'एक अक्षर छोड़कर अगला अक्षर G आता है।',
      ),
      'What is in front of you but unseen?': const LocalizedPuzzleData(
        question: 'वह क्या है जो आपके सामने है पर दिखाई नहीं देता?',
        options: ['भविष्य (Future)', 'हवा (Air)', 'सपना (Dream)', 'अतीत (Past)'],
        correctAnswer: 'भविष्य (Future)',
        explanation: 'भविष्य हमेशा आगे होता है पर दिखता नहीं।',
      ),
      'Which one is a planet?': const LocalizedPuzzleData(
        question: 'इनमें से कौन सा ग्रह है?',
        options: ['मंगल (Mars)', 'सूर्य (Sun)', 'चंद्रमा (Moon)', 'ध्रुव तारा'],
        correctAnswer: 'मंगल (Mars)',
        explanation: 'मंगल हमारे सौरमंडल का ग्रह है।',
      ),
      'I speak without a mouth and hear without ears. What am I?': const LocalizedPuzzleData(
        question: 'मैं बिना मुंह के बोलता हूं और बिना कान के सुनता हूं। मैं क्या हूं?',
        options: ['गूंज (Echo)', 'हवा (Wind)', 'छाया (Shadow)', 'रेडियो'],
        correctAnswer: 'गूंज (Echo)',
        explanation: 'गूंज आवाज को लौटाकर बोलती और सुनती है।',
      ),
      'A boat is full of people, yet not a single person is on board. Why?': const LocalizedPuzzleData(
        question: 'नाव लोगों से भरी है, पर कोई अकेला (single) व्यक्ति नहीं है। क्यों?',
        options: ['सभी विवाहित थे (All married)', 'नाव खाली थी', 'सब बच्चे थे', 'रोबोट थे'],
        correctAnswer: 'सभी विवाहित थे (All married)',
        explanation: 'नाव में सभी जोड़े (विवाहित) थे, कोई सिंगल नहीं था।',
      ),
      'The person who makes it does not want it. The buyer does not use it. What is it?': const LocalizedPuzzleData(
        question: 'बनाने वाला इसे नहीं चाहता, खरीदने वाला इस्तेमाल नहीं करता। वह क्या है?',
        options: ['ताबूत (Coffin)', 'गाड़ी', 'घर', 'कपड़े'],
        correctAnswer: 'ताबूत (Coffin)',
        explanation: 'ताबूत मृतक के लिए खरीदा जाता है, खरीदार खुद उपयोग नहीं करता।',
      ),
      'A cowboy rides into town on Friday, stays 2 days, and leaves on Friday. How?': const LocalizedPuzzleData(
        question: 'एक चरवाहा शुक्रवार को आया, 2 दिन रुका, और शुक्रवार को गया। कैसे?',
        options: ['घोड़े का नाम शुक्रवार (Friday) था', 'टाइम ट्रेवल', 'गिनती गलत थी', 'जादू था'],
        correctAnswer: 'घोड़े का नाम शुक्रवार (Friday) था',
        explanation: 'उसके घोड़े का नाम फ्राइडे (शुक्रवार) था।',
      ),
      'What runs around the entire yard without ever moving?': const LocalizedPuzzleData(
        question: 'वह क्या है जो पूरे आंगन के चारों ओर घूमती है पर कभी हिलती नहीं?',
        options: ['बाड़ (Fence)', 'रास्ता', 'घास', 'दीवार'],
        correctAnswer: 'बाड़ (Fence)',
        explanation: 'बाड़ बिना हिले पूरे आंगन को घेरती है।',
      ),
      'What begins with T, finishes with T, and has T inside it?': const LocalizedPuzzleData(
        question: 'कौन सा शब्द T से शुरू, T पर खत्म और उसके अंदर चाय (Tea) होती है?',
        options: ['Teapot (चायदानी)', 'Tent', 'Toast', 'Target'],
        correctAnswer: 'Teapot (चायदानी)',
        explanation: 'Teapot T से शुरू और खत्म होता है और इसमें चाय (Tea) होती है।',
      ),
      'How many letters are in "the alphabet"?': const LocalizedPuzzleData(
        question: '"the alphabet" शब्द में कितने अक्षर हैं?',
        options: ['11', '26', '24', '10'],
        correctAnswer: '11',
        explanation: '"t-h-e-a-l-p-h-a-b-e-t" में कुल 11 अक्षर हैं।',
      ),
      'What has a head and a tail, but no body?': const LocalizedPuzzleData(
        question: 'किसका सिर और पूंछ (Head & Tail) होती है पर शरीर नहीं होता?',
        options: ['सिक्का (Coin)', 'सांप', 'तीर', 'छिपकली'],
        correctAnswer: 'सिक्का (Coin)',
        explanation: 'सिक्के के दो पहलुओं को हेड और टेल कहा जाता है।',
      ),
      'What belongs to you, but others use it far more than you do?': const LocalizedPuzzleData(
        question: 'वह क्या है जो आपका है पर दूसरे आपसे ज्यादा इस्तेमाल करते हैं?',
        options: ['आपका नाम (Your Name)', 'फोन', 'पैसा', 'गाड़ी'],
        correctAnswer: 'आपका नाम (Your Name)',
        explanation: 'आपके नाम का उपयोग दूसरे लोग पुकारने के लिए करते हैं।',
      ),
      'What has words, but never speaks?': const LocalizedPuzzleData(
        question: 'किसमें शब्द होते हैं पर वह कभी बोलती नहीं?',
        options: ['किताब (Book)', 'टीवी', 'अखबार', 'रेडियो'],
        correctAnswer: 'किताब (Book)',
        explanation: 'किताब में शब्द लिखे होते हैं पर वह बोलती नहीं।',
      ),
      'If you drop me I crack, but smile at me and I smile back. What am I?': const LocalizedPuzzleData(
        question: 'गिराओगे तो टूट जाऊंगा, मुस्कुराओगे तो मुस्कुराऊंगा। मैं क्या हूं?',
        options: ['आईना (Mirror)', 'गिलास', 'तस्वीर', 'कांच'],
        correctAnswer: 'आईना (Mirror)',
        explanation: 'आईना गिरने से टूटता है और मुस्कुराने पर प्रतिबिंब दिखाता है।',
      ),
      'What can fill an entire room without taking up any physical space?': const LocalizedPuzzleData(
        question: 'वह क्या है जो जगह घेरे बिना पूरा कमरा भर देती है?',
        options: ['रोशनी (Light)', 'धुआं', 'हवा', 'खुशबू'],
        correctAnswer: 'रोशनी (Light)',
        explanation: 'रोशनी भौतिक जगह घेरे बिना पूरे कमरे को भर देती है।',
      ),
      'What has cities but no houses, and rivers but no water?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसमें शहर हैं पर घर नहीं, नदियां हैं पर पानी नहीं?',
        options: ['नक्शा (Map)', 'किताब', 'सपना', 'तस्वीर'],
        correctAnswer: 'नक्शा (Map)',
        explanation: 'नक्शे पर भौगोलिक विशेषताएं होती हैं पर असली घर या पानी नहीं।',
      ),
      'The more there is of this, the less you can see. What is it?': const LocalizedPuzzleData(
        question: 'यह जितना अधिक होगा, उतना ही कम दिखाई देगा। वह क्या है?',
        options: ['अंधेरा (Darkness)', 'रोशनी', 'धुआं', 'कोहरा'],
        correctAnswer: 'अंधेरा (Darkness)',
        explanation: 'अंधेरा जितना गहरा होगा, दृश्यता उतनी ही कम होगी।',
      ),
      'I have branches, but no fruit, trunk, or leaves. What am I?': const LocalizedPuzzleData(
        question: 'मेरी शाखाएं (Branches) हैं पर फल, तना या पत्ते नहीं। मैं क्या हूं?',
        options: ['बैंक (Bank)', 'पेड़', 'नदी', 'सड़क'],
        correctAnswer: 'बैंक (Bank)',
        explanation: 'बैंक की शाखाएं (branches) होती हैं।',
      ),
      'What can you break without ever touching or dropping it?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसे बिना छुए या गिराए भी तोड़ा जा सकता है?',
        options: ['वादा (Promise)', 'दिल', 'कांच', 'खामोशी'],
        correctAnswer: 'वादा (Promise)',
        explanation: 'वादा बिना छुए भी तोड़ा जा सकता है।',
      ),
      'What architectural invention allows you to look right through a wall?': const LocalizedPuzzleData(
        question: 'वह कौन सा आविष्कार है जो दीवार के आर-पार देखने देता है?',
        options: ['खिड़की (Window)', 'दरवाजा', 'दूरबीन', 'आईना'],
        correctAnswer: 'खिड़की (Window)',
        explanation: 'खिड़की दीवार में बनी होती है जिससे आर-पार देखा जा सकता है।',
      ),
      'If two is company, and three is a crowd, what are four and five?': const LocalizedPuzzleData(
        question: 'यदि दो कंपनी हैं और तीन भीड़, तो चार और पांच क्या हैं?',
        options: ['9 (Nine)', 'भीड़', 'दोस्त', 'पार्टी'],
        correctAnswer: '9 (Nine)',
        explanation: 'चार और पांच जोड़कर नौ (4 + 5 = 9) होते हैं।',
      ),
      'What goes up and down constantly but never moves an inch?': const LocalizedPuzzleData(
        question: 'वह क्या है जो लगातार ऊपर-नीचे होती है पर एक इंच नहीं हिलती?',
        options: ['सीढ़ियाँ (Stairs)', 'लिफ्ट', 'तापमान', 'झूला'],
        correctAnswer: 'सीढ़ियाँ (Stairs)',
        explanation: 'सीढ़ियां ऊपर-नीचे जाती हैं पर अपनी जगह स्थिर रहती हैं।',
      ),
      'Feed me and I live, but give me a drink of water and I die. What am I?': const LocalizedPuzzleData(
        question: 'खिलाओ तो जीती हूं, पानी पिलाओ तो मर जाती हूं। मैं क्या हूं?',
        options: ['आग (Fire)', 'पौधा', 'इंसान', 'मिट्टी'],
        correctAnswer: 'आग (Fire)',
        explanation: 'आग लकड़ी से जलती है और पानी डालने से बुझ जाती है।',
      ),
      'What has to be broken before you can ever use it?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसे इस्तेमाल करने से पहले तोड़ना जरूरी है?',
        options: ['अंडा (Egg)', 'अखरोट', 'ताला', 'नारियल'],
        correctAnswer: 'अंडा (Egg)',
        explanation: 'अंडे को बिना फोड़े उपयोग नहीं किया जा सकता।',
      ),
      'I am tall when I am young, and short when I am old. What am I?': const LocalizedPuzzleData(
        question: 'नई होने पर लंबी, पुरानी होने पर छोटी हो जाती हूं। मैं क्या हूं?',
        options: ['मोमबत्ती (Candle)', 'पेंसिल', 'पेड़', 'रस्सी'],
        correctAnswer: 'मोमबत्ती (Candle)',
        explanation: 'मोमबत्ती जलते हुए छोटी होती जाती है।',
      ),
      'What begins with an E and contains only one single letter?': const LocalizedPuzzleData(
        question: 'कौन सा शब्द E से शुरू होता है और उसमें सिर्फ एक पत्र (Letter) होता है?',
        options: ['लिफाफा (Envelope)', 'आंख (Eye)', 'अंडा (Egg)', 'पृथ्वी (Earth)'],
        correctAnswer: 'लिफाफा (Envelope)',
        explanation: 'Envelope E से शुरू होता है और इसके अंदर पत्र (letter) होता है।',
      ),
      'A man pushes his car to a hotel and immediately declares bankruptcy. Why?': const LocalizedPuzzleData(
        question: 'एक व्यक्ति अपनी कार होटल ले जाता है और दिवालिया घोषित हो जाता है। क्यों?',
        options: ['मोनोपॉली खेल रहा था (Monopoly)', 'कार खराब थी', 'होटल महंगा था', 'कर्ज था'],
        correctAnswer: 'मोनोपॉली खेल रहा था (Monopoly)',
        explanation: 'वह मोनोपॉली बोर्ड गेम खेल रहा था।',
      ),
      'How can a person go 25 days without sleeping?': const LocalizedPuzzleData(
        question: 'एक व्यक्ति बिना सोए 25 दिन कैसे बिता सकता है?',
        options: ['वह रात में सोता है (Sleeps at night)', 'कॉफी पीकर', 'असंभव है', 'आराम करके'],
        correctAnswer: 'वह रात में सोता है (Sleeps at night)',
        explanation: 'वह दिन में नहीं, रात में सोता है।',
      ),
      'What comes down from the sky but never goes back up?': const LocalizedPuzzleData(
        question: 'वह क्या है जो आसमान से नीचे आती है पर कभी ऊपर वापस नहीं जाती?',
        options: ['बारिश (Rain)', 'बर्फ', 'बिजली', 'ओले'],
        correctAnswer: 'बारिश (Rain)',
        explanation: 'बारिश के बूंद गिरने के बाद बारिश बनकर वापस ऊपर नहीं जाते।',
      ),
      'Where does today always come before yesterday?': const LocalizedPuzzleData(
        question: 'आज (Today) हमेशा कल (Yesterday) से पहले कहां आता है?',
        options: ['शब्दकोश में (Dictionary)', 'कैलेंडर में', 'सपने में', 'घड़ी में'],
        correctAnswer: 'शब्दकोश में (Dictionary)',
        explanation: 'शब्दकोश में वर्णमाला के अनुसार T अक्षर Y से पहले आता है।',
      ),
      'What can you hold in your right hand, but never in your left hand?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसे आप दाएं हाथ से पकड़ सकते हैं पर बाएं से नहीं?',
        options: ['आपका बायां हाथ (Left Hand)', 'दायां हाथ', 'अंगूठा', 'कलाई'],
        correctAnswer: 'आपका बायां हाथ (Left Hand)',
        explanation: 'बायां हाथ खुद को नहीं पकड़ सकता।',
      ),
      'What has legs, but cannot take a single step?': const LocalizedPuzzleData(
        question: 'किसके पैर होते हैं पर वह एक कदम भी नहीं चल सकती?',
        options: ['मेज (Table)', 'कुर्सी', 'बिस्तर', 'घड़ी'],
        correctAnswer: 'मेज (Table)',
        explanation: 'मेज के पायों को पैर कहा जाता है पर वह चल नहीं सकती।',
      ),
      'What has a thumb and four fingers, but is not alive or human?': const LocalizedPuzzleData(
        question: 'किसका एक अंगूठा और चार उंगलियां होती हैं पर वह जीवित नहीं?',
        options: ['दस्ताना (Glove)', 'रोबोट', 'पुतला', 'मूर्ति'],
        correctAnswer: 'दस्ताना (Glove)',
        explanation: 'दस्ताने में हाथ के आकार की उंगलियां बनी होती हैं।',
      ),
      'If an electric train travels north at 60 mph, which way does the smoke blow?': const LocalizedPuzzleData(
        question: 'इलेक्ट्रिक ट्रेन 60 किमी/घंटा उत्तर जा रही है, धुआं किधर जाएगा?',
        options: ['कोई धुआं नहीं होता (No smoke)', 'दक्षिण', 'पश्चिम', 'उत्तर'],
        correctAnswer: 'कोई धुआं नहीं होता (No smoke)',
        explanation: 'इलेक्ट्रिक ट्रेन में धुआं निकलता ही नहीं।',
      ),
      'What gets sharper the more you train and challenge it?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसे जितना चुनौती दो उतना ही तेज होता है?',
        options: ['दिमाग (Brain/Mind)', 'चाकू', 'तलवार', 'पेंसिल'],
        correctAnswer: 'दिमाग (Brain/Mind)',
        explanation: 'दिमाग को चुनौती देने से सोचने की शक्ति तेज होती है।',
      ),
      '2 fathers and 2 sons caught 3 fish, 1 each. How is this possible?': const LocalizedPuzzleData(
        question: '2 पिताओं और 2 बेटों ने 3 मछलियां पकड़ीं, प्रत्येक को 1 मिली। कैसे?',
        options: ['दादा, पिता और पोता थे (3 people)', 'मछली छोटी थी', 'साझा थी', 'जादू था'],
        correctAnswer: 'दादा, पिता और पोता थे (3 people)',
        explanation: 'वे कुल 3 लोग थे: दादा (पिता), पिता (बेटा व पिता), और पोता (बेटा)।',
      ),
      'What runs constantly without walking, and has a bed but never sleeps?': const LocalizedPuzzleData(
        question: 'वह क्या है जो बिना चले दौड़ती है और बिस्तर है पर सोती नहीं?',
        options: ['नदी (River)', 'हवा', 'गाड़ी', 'समय'],
        correctAnswer: 'नदी (River)',
        explanation: 'नदी के तल को रीवरबेड कहते हैं और वह निरंतर बहती है।',
      ),
      'What kind of band never plays musical instruments?': const LocalizedPuzzleData(
        question: 'कौन सा बैंड कभी संगीत वाद्ययंत्र नहीं बजाता?',
        options: ['रबर बैंड (Rubber band)', 'रॉक बैंड', 'जैज़ बैंड', 'बैंड बाजा'],
        correctAnswer: 'रबर बैंड (Rubber band)',
        explanation: 'रबर बैंड एक लचीला छल्ला होता है, संगीत समूह नहीं।',
      ),
      'Which word in every standard English dictionary is spelled incorrectly?': const LocalizedPuzzleData(
        question: 'कौन सा शब्द डिक्शनरी में हमेशा गलत (Incorrectly) लिखा जाता है?',
        options: ['Incorrectly', 'Wrong', 'Mistake', 'False'],
        correctAnswer: 'Incorrectly',
        explanation: 'Incorrectly शब्द की वर्तनी ही "Incorrectly" है।',
      ),
      'A plane crashes on the exact border of US and Canada. Where are survivors buried?': const LocalizedPuzzleData(
        question: 'विमान सीमा पर दुर्घटनाग्रस्त हुआ, जीवित बचे लोगों को कहां दफनाया जाएगा?',
        options: ['जीवित लोगों को नहीं दफनाया जाता (Survivors are alive)', 'अमेरिका', 'कनाडा', 'बॉर्डर'],
        correctAnswer: 'जीवित लोगों को नहीं दफनाया जाता (Survivors are alive)',
        explanation: 'जीवित बचे लोग (survivors) जिंदा होते हैं, उन्हें दफनाते नहीं।',
      ),
      'What body part tastes food much better than it smells?': const LocalizedPuzzleData(
        question: 'शरीर का कौन सा अंग सूंघने से बेहतर भोजन का स्वाद लेता है?',
        options: ['जीभ (Tongue)', 'नाक', 'होंठ', 'दांत'],
        correctAnswer: 'जीभ (Tongue)',
        explanation: 'जीभ पर स्वाद कलिकाएं होती हैं जो स्वाद पहचानती हैं।',
      ),
      'What object has a spine, but has absolutely no bones inside?': const LocalizedPuzzleData(
        question: 'किसकी रीढ़ (Spine) होती है पर अंदर हड्डी नहीं होती?',
        options: ['किताब (Book)', 'सेब', 'सांप', 'कुर्सी'],
        correctAnswer: 'किताब (Book)',
        explanation: 'किताब की जिल्द के पिछले भाग को स्पाइन (Spine) कहा जाता है।',
      ),
      'What household item loses its head in the morning and gets it back at night?': const LocalizedPuzzleData(
        question: 'वह क्या है जिसका सिर सुबह उतर जाता है और रात को वापस आता है?',
        options: ['तकिया (Pillow)', 'टोपी', 'कंघी', 'बिस्तर'],
        correctAnswer: 'तकिया (Pillow)',
        explanation: 'सुबह उठने पर सिर तकिए से हटता है और रात में वापस आता है।',
      ),
      'What celestial or household item has rings, but no fingers?': const LocalizedPuzzleData(
        question: 'किसके छल्ले (Rings) होते हैं पर उंगलियां नहीं होतीं?',
        options: ['शनि ग्रह (Saturn)', 'टेलीफोन', 'घड़ी', 'पर्दा'],
        correctAnswer: 'शनि ग्रह (Saturn)',
        explanation: 'शनि ग्रह (Saturn) के चारों ओर वलय (छल्ले) होते हैं।',
      ),

    },

    // Spanish
    'es': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: '¿Qué palabra es más larga?',
        options: ['Snake', 'Train', 'Road', 'Queue'],
        correctAnswer: 'Queue',
        explanation: 'Queue tiene cinco letras, más que las demás.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: '¿Qué se moja más al secar?',
        options: ['Toalla', 'Sol', 'Fuego', 'Arena'],
        correctAnswer: 'Toalla',
        explanation: 'Una toalla absorbe agua mientras seca otra cosa.',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: '¿Qué mes tiene 28 días?',
        options: ['Febrero', 'Enero', 'Todos ellos', 'Junio'],
        correctAnswer: 'Todos ellos',
        explanation: 'Cada mes tiene al menos 28 días.',
      ),
      "What has keys but can't open locks?": const LocalizedPuzzleData(
        question: '¿Qué tiene teclas/llaves pero no abre cerraduras?',
        options: ['Piano', 'Puerta', 'Coche', 'Cofre'],
        correctAnswer: 'Piano',
        explanation: 'Un piano tiene teclas musicales, no llaves de cerradura.',
      ),
      'Which number is half of 8?': const LocalizedPuzzleData(
        question: '¿Qué número es la mitad de 8?',
        options: ['4', '3', '0', 'Depende'],
        correctAnswer: '4',
        explanation: 'La mitad de 8 es 4.',
      ),
      'What has a face and two hands but no arms?': const LocalizedPuzzleData(
        question: '¿Qué tiene cara y dos manecillas pero no brazos?',
        options: ['Reloj', 'Robot', 'Persona', 'Espejo'],
        correctAnswer: 'Reloj',
        explanation: 'Un reloj tiene esfera y manecillas.',
      ),
      'In a dark room, what do you light first?': const LocalizedPuzzleData(
        question: 'En una habitación oscura, ¿qué enciendes primero?',
        options: ['Cerilla', 'Vela', 'Lámpara', 'Chimenea'],
        correctAnswer: 'Cerilla',
        explanation: 'Debes encender la cerilla antes de encender cualquier otra cosa.',
      ),
      'What breaks when you say its name?': const LocalizedPuzzleData(
        question: '¿Qué se rompe al decir su nombre?',
        options: ['Silencio', 'Cristal', 'Promesa', 'Código'],
        correctAnswer: 'Silencio',
        explanation: 'Al hablar, el silencio desaparece.',
      ),
    },

    // French
    'fr': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'Quel mot est le plus long ?',
        options: ['Snake', 'Train', 'Road', 'Queue'],
        correctAnswer: 'Queue',
        explanation: 'Queue a 5 lettres, plus que les autres.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'Qu’est-ce qui mouille en séchant ?',
        options: ['Serviette', 'Soleil', 'Feu', 'Sable'],
        correctAnswer: 'Serviette',
        explanation: 'Une serviette absorbe l’eau en séchant quelque chose.',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'Quel mois a 28 jours ?',
        options: ['Février', 'Janvier', 'Tous', 'Juin'],
        correctAnswer: 'Tous',
        explanation: 'Chaque mois a au moins 28 jours.',
      ),
      'What breaks when you say its name?': const LocalizedPuzzleData(
        question: 'Qu’est-ce qui se brise quand on prononce son nom ?',
        options: ['Le silence', 'Le verre', 'Une promesse', 'Le code'],
        correctAnswer: 'Le silence',
        explanation: 'Parler met fin au silence.',
      ),
    },

    // Arabic
    'ar': {
      'Which word is longest?': const LocalizedPuzzleData(
        question: 'أي كلمة هي الأطول؟',
        options: ['Snake', 'Train', 'Road', 'Queue'],
        correctAnswer: 'Queue',
        explanation: 'تحتوي Queue على خمسة أحرف أكثر من غيرها.',
      ),
      'What gets wetter while drying?': const LocalizedPuzzleData(
        question: 'ما الذي يبتل أكثر أثناء التجفيف؟',
        options: ['المنشفة', 'الشمس', 'النار', 'الرمل'],
        correctAnswer: 'المنشفة',
        explanation: 'تمتص المنشفة الماء أثناء تجفيف الأشياء.',
      ),
      'Which month has 28 days?': const LocalizedPuzzleData(
        question: 'أي شهر فيه 28 يوماً؟',
        options: ['فبراير', 'يناير', 'كل الشهور', 'يونيو'],
        correctAnswer: 'كل الشهور',
        explanation: 'كل شهر فيه على الأقل 28 يوماً.',
      ),
      'What breaks when you say its name?': const LocalizedPuzzleData(
        question: 'ما الذي ينكسر بمجرد ذكر اسمه؟',
        options: ['الصمت', 'الزجاج', 'الوعد', 'الرمز'],
        correctAnswer: 'الصمت',
        explanation: 'التحدث ينهي الصمت.',
      ),
    },
  };

  static LocalizedPuzzleData getTranslation(
    String originalQuestion,
    List<String> defaultOptions,
    String defaultAnswer,
    String defaultExplanation,
    String langCode,
  ) {
    // 1. Exact match in requested language
    final langDict = _translations[langCode];
    if (langDict != null && langDict.containsKey(originalQuestion)) {
      return langDict[originalQuestion]!;
    }

    // 2. Intelligent language family fallback
    // Indic languages (Hindi script / sister languages) fallback to Hindi first, then Urdu
    const indicLanguages = {'hi', 'bn', 'mr', 'gu', 'te', 'ta', 'kn', 'ml', 'ne', 'si', 'as', 'or', 'sa'};
    if (indicLanguages.contains(langCode)) {
      final hindiDict = _translations['hi'];
      if (hindiDict != null && hindiDict.containsKey(originalQuestion)) {
        return hindiDict[originalQuestion]!;
      }
      final urduDict = _translations['ur'];
      if (urduDict != null && urduDict.containsKey(originalQuestion)) {
        return urduDict[originalQuestion]!;
      }
    }

    // Perso-Arabic / Middle Eastern languages (Urdu, Arabic, Persian, Pashto, Sindhi, Hebrew)
    const arabicScriptLanguages = {'ur', 'ar', 'fa', 'ps', 'sd', 'he', 'ha'};
    if (arabicScriptLanguages.contains(langCode)) {
      if (langCode == 'ur') {
        final urduDict = _translations['ur'];
        if (urduDict != null && urduDict.containsKey(originalQuestion)) {
          return urduDict[originalQuestion]!;
        }
      }
      final arDict = _translations['ar'];
      if (arDict != null && arDict.containsKey(originalQuestion)) {
        return arDict[originalQuestion]!;
      }
      final urduDict = _translations['ur'];
      if (urduDict != null && urduDict.containsKey(originalQuestion)) {
        return urduDict[originalQuestion]!;
      }
    }

    // Romance languages fallback to Spanish or French
    const romanceLanguages = {'es', 'pt', 'pt_BR', 'pt_PT', 'it', 'fr', 'ro', 'ca'};
    if (romanceLanguages.contains(langCode)) {
      final esDict = _translations['es'];
      if (esDict != null && esDict.containsKey(originalQuestion)) {
        return esDict[originalQuestion]!;
      }
      final frDict = _translations['fr'];
      if (frDict != null && frDict.containsKey(originalQuestion)) {
        return frDict[originalQuestion]!;
      }
    }

    // Slavic languages fallback to Russian
    const slavicLanguages = {'ru', 'uk', 'pl', 'cs', 'bg'};
    if (slavicLanguages.contains(langCode)) {
      final ruDict = _translations['ru'];
      if (ruDict != null && ruDict.containsKey(originalQuestion)) {
        return ruDict[originalQuestion]!;
      }
    }

    // 4. Return original default
    return LocalizedPuzzleData(
      question: originalQuestion,
      options: defaultOptions,
      correctAnswer: defaultAnswer,
      explanation: defaultExplanation,
    );
  }
}