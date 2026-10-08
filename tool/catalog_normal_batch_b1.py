# -*- coding: utf-8 -*-
"""
Normal tier batch B1 (63 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "A detective enters a mansion where a millionaire was found shot at his desk. The tape recorder on the desk played: 'I cannot go on, goodbye,' followed by a gunshot. The detective immediately declared it murder. Why?",
        ["Who rewound the tape recorder after the shot was fired?", "The desk was too neat", "The window was open", "The millionaire had no debts"],
        "Who rewound the tape recorder after the shot was fired?",
        "If the victim shot himself while recording, the tape would have kept running until the end. A dead person cannot press rewind.",
        "ایک کروڑ پتی کی لاش اس کے دفتر میں ملی۔ میز پر موجود ٹیپ ریکارڈر پر اس کی آواز آئی: 'میں مزید زندہ نہیں رہ سکتا، الوداع' اور پھر گولی کی آواز۔ تفتیش کار نے سنتے ہی کہا یہ قتل ہے، خودکشی نہیں۔ کیوں؟",
        ["گولی چلنے کے بعد کیسٹ کو واپس شروع پر کس نے ریوائنڈ (Rewind) کیا؟", "میز بہت زیادہ صاف تھی", "کھڑکی کھلی ہوئی تھی", "مقتول پر کوئی قرض نہیں تھا"],
        "گولی چلنے کے بعد کیسٹ کو واپس شروع پر کس نے ریوائنڈ (Rewind) کیا؟",
        "اگر انسان خودکشی کرتے وقت آخری بات ریکارڈ کرے تو مرنے کے بعد ٹیپ کو خود بخود ریوائنڈ بٹن دبا کر شروع پر کون لایا؟ قاتل نے یہ حرکت کی۔"
    ),
    (
        "A man is found dead in an open snowy field with no footprints anywhere near his body except his own ending at his feet. A closed, unopened backpack lies on his back. How did he die?",
        ["His parachute failed to open during a skydiving jump", "He froze to death walking", "He was struck by a meteorite", "He was buried in an avalanche"],
        "His parachute failed to open during a skydiving jump",
        "The unopened backpack was his failed parachute pack; he fell from an airplane onto the snow.",
        "برف کے کھلے میدان میں ایک شخص مردہ پایا گیا، اس کے اپنے قدموں کے علاوہ دور دور تک کسی انسان یا جانور کے نشانات نہیں تھے۔ اس کی پیٹھ پر ایک بند بیگ تھا۔ وہ کیسے مرا؟",
        ["ہوائی جہاز سے چھلانگ لگاتے ہوئے اس کا پیراشوٹ نہیں کھل سکا", "وہ چلتے چلتے سردی سے جم گیا", "اس پر آسمانی شہابیہ گرا", "وہ برف کے تودے میں دب گیا تھا"],
        "ہوائی جہاز سے چھلانگ لگاتے ہوئے اس کا پیراشوٹ نہیں کھل سکا",
        "پیٹھ پر بند بیگ دراصل اس کا پیراشوٹ تھا جو نہ کھلنے کی وجہ سے وہ آسمان سے سیدھا برف کے میدان میں گر کر ہلاک ہو گیا۔"
    ),
    (
        "Two women order iced tea at a cafe. Alice drinks five glasses rapidly in two minutes. Beatrice sips only one glass slowly over an hour. Beatrice dies of poison; Alice survives unharmed. How?",
        ["The poison was frozen inside the ice cubes, which had not melted when Alice drank", "Alice was immune to poison", "Beatrice drank from a cracked glass", "The waiter put poison in the straw"],
        "The poison was frozen inside the ice cubes, which had not melted when Alice drank",
        "Alice drank so fast the ice remained solid; Beatrice's slow drinking allowed poisoned ice to melt completely into her drink.",
        "دو سہیلیوں نے کیفے میں برف والی ٹھنڈی چائے منگوائی۔ ایک نے دو منٹ میں جلدی سے پانچ گلاس پی لیے، دوسری گھنٹہ بھر آہستہ آہستہ ایک ہی گلاس پیتی رہی۔ آہستہ پینے والی زہر سے مر گئی جبکہ دوسری بالکل محفوظ رہی۔ کیوں؟",
        ["زہر برف کی کیوبز کے اندر جما ہوا تھا جو جلدی پینے والی کے گلاس میں پگھل نہیں پایا تھا", "پہلی لڑکی زہر کی عادی تھی", "دوسری کا گلاس ٹوٹا ہوا تھا", "سٹرا میں زہر لگا ہوا تھا"],
        "زہر برف کی کیوبز کے اندر جما ہوا تھا جو جلدی پینے والی کے گلاس میں پگھل نہیں پایا تھا",
        "زہر برف کے اندر تھا، تیز پینے والی کے گلاس میں برف پگھلی ہی نہیں، جبکہ گھنٹہ بھر بیٹھنے والی کی برف پگھل کر زہر چائے میں گھل گیا۔"
    ),
    (
        "A jeweler is robbed. The thief entered through an unbroken second-floor skylight and left through the front door, leaving no fingerprints, taking only diamonds and ignoring gold bars. Why did he ignore the heavy gold bars?",
        ["Gold is far too heavy to carry while escaping on foot", "Gold was locked in a safe", "Gold was fake", "The thief had a metal allergy"],
        "Gold is far too heavy to carry while escaping on foot",
        "Gold has a density of 19.3 g/cm^3; gold bars of equivalent value would weigh hundreds of pounds, impossible for a stealth escape.",
        "ایک چور نے زیورات کی دکان سے صرف ہیرے چرائے مگر سامنے پڑے سونے کے بھاری بسکٹوں کو ہاتھ تک نہ لگایا۔ اس نے سونا کیوں چھوڑ دیا؟",
        ["سونے کا وزن اتنا زیادہ تھا کہ بھاگتے ہوئے اٹھا کر لے جانا ناممکن تھا", "سونا تجوری میں بند تھا", "سونا نقلی تھا", "چور کو دھات سے الرجی تھی"],
        "سونے کا وزن اتنا زیادہ تھا کہ بھاگتے ہوئے اٹھا کر لے جانا ناممکن تھا",
        "سونے کی کثافت بہت زیادہ ہوتی ہے، کروڑوں کا سونا سینکڑوں کلو وزنی ہوتا ہے جسے اٹھا کر خاموشی سے فرار ہونا ممکن نہیں تھا، جبکہ ہیرے جیب میں آ جاتے ہیں۔"
    ),
    (
        "A driver was pulled over on a highway at midnight with all exterior lights functioning. The police officer noticed the speedometer read 0 mph despite the car traveling at 60 mph. What was wrong?",
        ["The vehicle was being towed on a flatbed trailer", "The speedometer cable was cut", "The driver was reversing", "The car was sliding on black ice"],
        "The vehicle was being towed on a flatbed trailer",
        "The car itself was riding stationary on the deck of a moving flatbed recovery vehicle.",
        "رات کو ہائی وے پر چلتی ہوئی کار کا سپیڈومیٹر صفر کی رفتار دکھا رہا تھا جبکہ گاڑی 60 میل فی گھنٹہ کی رفتار سے آگے جا رہی تھی۔ یہ کیسے ممکن تھا؟",
        ["گاڑی خود نہیں چل رہی تھی بلکہ ٹرک کے اوپر لاد کر لے جائی جا رہی تھی", "سپیڈومیٹر کی تار کٹی ہوئی تھی", "ڈرائیور گاڑی ریورس چلا رہا تھا", "گاڑی برف پر پھسل رہی تھی"],
        "گاڑی خود نہیں چل رہی تھی بلکہ ٹرک کے اوپر لاد کر لے جائی جا رہی تھی",
        "گاڑی ایک بڑے ٹو ٹرک کے فلیٹ بیڈ پر کھڑی تھی، اس لیے اس کے پہیے ساکن تھے اور میٹر صفر پر تھا مگر ٹرک کی رفتار 60 میل تھی۔"
    ),
    (
        "A man purchases a pair of new shoes, goes to work, and dies three hours later. What was his profession?",
        ["A circus knife thrower's assistant or tightrope walker", "A coal miner", "A professional scuba diver", "A commercial pilot"],
        "A circus knife thrower's assistant or tightrope walker",
        "New shoes with different heel height or slick soles caused him to misjudge foot placement during a perilous acrobatic act.",
        "ایک شخص نے صبح نئے جوتے خریدے، کام پر گیا، اور تین گھنٹے بعد وہ مر گیا۔ اس کا پیشہ کیا تھا؟",
        ["سرکس میں رسی پر چلنے والا بازی گر یا چاقو کا نشانہ بننے والا معاون", "کوئلے کی کان کا مزدور", "سمندری غوطہ خور", "ہوائی جہاز کا پائلٹ"],
        "سرکس میں رسی پر چلنے والا بازی گر یا چاقو کا نشانہ بننے والا معاون",
        "نئے جوتوں کے تلوے کی پھسلن یا ایڑی کے معمولی فرق نے اونچی رسی پر چلتے ہوئے اس کا توازن بگاڑ دیا جس سے وہ نیچے گر گیا۔"
    ),
    (
        "A woman buys a parrot that the pet store owner guarantees can repeat every word it hears. A week later, the parrot has not uttered a single word, yet the owner did not lie. How?",
        ["The parrot is completely deaf", "The woman never spoke to it", "The parrot only speaks French", "The parrot was sleeping"],
        "The parrot is completely deaf",
        "A deaf parrot repeats every word it hears—which is precisely zero words.",
        "دکان دار نے دعویٰ کیا کہ یہ طوطا جو لفظ بھی سنے گا ہو بہو دہرا دے گا۔ گاہک نے خریدا مگر ایک ہفتے میں طوطے نے ایک لفظ بھی نہ بولا، حالانکہ دکان دار نے جھوٹ نہیں بولا تھا۔ کیسے؟",
        ["طوطا پیدائشی طور پر بالکل بہرا تھا", "عورت نے اس کے سامنے بات نہیں کی تھی", "طوطا صرف فرانسیسی سمجھتا تھا", "طوطا سو رہا تھا"],
        "طوطا پیدائشی طور پر بالکل بہرا تھا",
        "طوطا جو لفظ سنے گا وہی بولے گا، چونکہ وہ بہرا تھا اس لیے اس نے کچھ نہیں سنا اور کچھ نہیں بولا۔ دکان دار کی بات لفظی طور پر سچ تھی۔"
    ),
    (
        "A king wanted to execute a sage. He allowed the sage one final statement: 'If you speak a truth, you will be hanged; if you speak a lie, you will be drowned.' What statement saved the sage's life?",
        ["'I will be drowned'", "'I am an honest man'", "'The king is merciful'", "'Tomorrow it will rain'"],
        "'I will be drowned'",
        "If the king drowns him, the statement is true, meaning he should have been hanged. If he hangs him, the statement was false, meaning he should have been drowned. A logical paradox.",
        "بادشاہ نے دانا وزیر سے کہا: 'ایک آخری جملہ بولو، اگر سچ بولا تو پھانسی ہوگی، اگر جھوٹ بولا تو سمندر میں ڈبو دیا جائے گا'۔ دانا نے کیا جملہ بولا کہ بادشاہ اسے سزا نہ دے سکا؟",
        ["'مجھے سمندر میں ڈبویا جائے گا'", "'میں سچا انسان ہوں'", "'بادشاہ سلامت رحم دل ہیں'", "'کل بارش ہوگی'"],
        "'مجھے سمندر میں ڈبویا جائے گا'",
        "اگر بادشاہ اسے ڈبوتا تو اس کا جملہ سچ ہو جاتا جس پر پھانسی ہونی چاہیے تھی، اور اگر پھانسی دیتا تو جملہ جھوٹ بن جاتا جس پر ڈبونا تھا۔ بادشاہ الجھ کر رہ گیا۔"
    ),
    (
        "A man pushes his bicycle across the border every week carrying two bags of sand. Border guards sift the sand meticulously but find zero contraband. After ten years, what was he actually smuggling?",
        ["Bicycles", "Sand", "Gold dust", "Currency notes"],
        "Bicycles",
        "The sand bags were a decoy diversion; the valuable smuggled commodity was the new bicycle each trip.",
        "ایک شخص ہر ہفتے سائیکل پر ریت کے دو تھیلے لاد کر سرحد پار کرتا تھا۔ کسٹم والے ہر بار ریت چھانتے مگر کچھ نہ ملتا۔ دس سال بعد معلوم ہوا وہ اسمگلنگ کر رہا تھا، کس چیز کی؟",
        ["سائیکلوں کی اسمگلنگ", "ریت کی", "سونے کے ذرّات کی", "کرنسی نوٹوں کی"],
        "سائیکلوں کی اسمگلنگ",
        "ریت کے تھیلے صرف توجہ ہٹانے کا بہانہ تھے، وہ ہر ہفتے نئی غیر ملکی سائیکلیں سرحد پار اسمگل کر رہا تھا۔"
    ),
    (
        "A locked metal box contains three ordinary light bulbs inside: red, blue, green. From outside the box, you can only see a single glass viewing hole displaying the blended color. If the hole shows yellow light, which bulbs are powered?",
        ["Red and green bulbs only", "Blue and green bulbs only", "Red and blue bulbs only", "All three bulbs"],
        "Red and green bulbs only",
        "In additive color mixing of light, combining red light and green light produces yellow light.",
        "ایک بند دھاتی ڈبے میں تین بلب ہیں: سرخ، نیلا، اور سبز۔ ڈبے کے باہر شیشے کے سوراخ سے مخلوط رنگ نظر آتا ہے۔ اگر سوراخ سے زرد (Yellow) روشنی نکل رہی ہے تو اندر کون سے بلب جل رہے ہیں؟",
        ["صرف سرخ اور سبز بلب", "صرف نیلا اور سبز بلب", "صرف سرخ اور نیلا بلب", "تینوں بلب ایک ساتھ"],
        "صرف سرخ اور سبز بلب",
        "روشنی کے بنیادی رنگوں کے ملاپ (Additive color mixing) میں سرخ اور سبز روشنی مل کر زرد روشنی پیدا کرتی ہیں۔"
    ),
    (
        "A clockmaker builds a clock that has no numbers, no tick marks, and identical hour and minute hands. How many times between 12:00 and 1:00 is it impossible to determine the time?",
        ["Only when both hands perfectly overlap at 12:00 is it unambiguous, but there are multiple hand-swap ambiguous configurations throughout the day", "Never ambiguous", "Every minute", "Exactly 12 times"],
        "Only when both hands perfectly overlap at 12:00 is it unambiguous, but there are multiple hand-swap ambiguous configurations throughout the day",
        "When swapping the two identical hands produces another valid clock reading, the time is ambiguous. There are 132 such mathematical positions in a 12-hour period.",
        "ایک گھڑی ساز نے ایک ایسی گھڑی بنائی جس پر کوئی ہندسہ نہیں اور گھنٹے اور منٹ کی دونوں سوئیاں بالکل ایک جیسی ہیں۔ دن میں کتنے ایسے لمحات آتے ہیں جہاں سوئیاں دیکھ کر وقت بتانا ناممکن ہو جاتا ہے؟",
        ["جب دونوں سوئیوں کے باہمی تبادلے سے گھڑی کا ایک اور درست وقت بن رہا ہو تو وقت مبہم ہو جاتا ہے (تقریباً 132 مقامات)", "کبھی مبہم نہیں ہوتا", "ہر منٹ بعد", "صرف بارہ بجے"],
        "جب دونوں سوئیوں کے باہمی تبادلے سے گھڑی کا ایک اور درست وقت بن رہا ہو تو وقت مبہم ہو جاتا ہے (تقریباً 132 مقامات)",
        "ریاضیاتی طور پر جب دونوں سوئیوں کو آپس میں بدلنے سے گھڑی پر ایک جائز وقت بن سکے، تو شناخت کرنا ناممکن ہوتا ہے کہ کون سی سوئی گھنٹے کی ہے اور کون سی منٹ کی۔"
    ),
    (
        "A ship leaves harbor in Japan on Tuesday morning and sails due east across the Pacific Ocean for 24 hours. When it arrives at its destination, what day of the week is it on the local calendar?",
        ["Tuesday morning (or Monday)", "Wednesday morning", "Thursday morning", "Friday morning"],
        "Tuesday morning (or Monday)",
        "Crossing the International Date Line eastward subtracts an entire calendar day (24 hours), causing the vessel to repeat the same calendar date.",
        "ایک بحری جہاز منگل کی صبح جاپان سے روانہ ہوا اور بحر الکاہل میں 24 گھنٹے مشرق کی طرف سفر کر کے اپنی منزل پہنچا۔ مقامی کیلنڈر کے مطابق وہاں کون سا دن تھا؟",
        ["منگل کا دن (تاریخ پیچھے ہٹ گئی)", "بدھ کا دن", "جمعرات کا دن", "جمعہ کا دن"],
        "منگل کا دن (تاریخ پیچھے ہٹ گئی)",
        "بین الاقوامی خط تاریخ (International Date Line) کو مغرب سے مشرق عبور کرتے ہی کیلنڈر میں ایک دن پیچھے جانا پڑتا ہے، جس سے مسافر وہی دن دوبارہ جیتے ہیں۔"
    ),
    (
        "A safe has a 3-dial combination lock, each dial numbered 0 to 9. A thief knows the correct combination digits sum to 25 and all three digits are odd numbers. How many possible combinations must he try?",
        ["Only 3 combinations (9-9-7, 9-7-9, 7-9-9)", "10 combinations", "27 combinations", "1 combination"],
        "Only 3 combinations (9-9-7, 9-7-9, 7-9-9)",
        "The single-digit odd numbers are 1, 3, 5, 7, 9. The maximum sum of three odd single digits is 9+9+9=27. The only way three odd single digits sum to 25 is {9, 9, 7} in three permutations.",
        "ایک تجوری کا تین ہندسوں کا کوڈ ہے۔ چور کو معلوم ہے کہ تینوں ہندسے طاق (Odd) ہیں اور ان کا مجموعہ 25 بنتا ہے۔ چور کو زیادہ سے زیادہ کتنے کوڈ آزمانے پڑیں گے؟",
        ["صرف 3 کوڈ (9-9-7، 9-7-9، اور 7-9-9)", "10 کوڈ", "27 کوڈ", "صرف 1 کوڈ"],
        "صرف 3 کوڈ (9-9-7، 9-7-9، اور 7-9-9)",
        "اکائی کے طاق ہندسوں (1، 3، 5، 7، 9) میں سے 25 کا مجموعہ صرف 9 + 9 + 7 سے ہی بن سکتا ہے۔ اس کی صرف 3 ممکنہ ترتیبات بنتی ہیں۔"
    ),
    (
        "In a famous experiment, subjects watching a video of basketball players passing a ball completely fail to notice a person in a gorilla suit walking across the screen. What is this psychological phenomenon called?",
        ["Inattentional blindness", "Confirmation bias", "Prosopagnosia", "The Stroop effect"],
        "Inattentional blindness",
        "Intense selective focus on a specific task (counting passes) causes the human visual cortex to filter out unexpected, prominent stimuli.",
        "ایک مشہور نفسیاتی تجربے میں لوگ باسکٹ بال کے پاس گننے میں اتنے مگن ہو گئے کہ اسکرین پر گوریلا کا لباس پہن کر ناچنے والے انسان کو بالکل نہ دیکھ سکے۔ اس کیفیت کو کیا کہتے ہیں؟",
        ["توجہ کی لاعلمی (Inattentional blindness)", "تصدیقی تعصب", "چہرہ نہ پہچاننا", "اسٹروپ کا اثر"],
        "توجہ کی لاعلمی (Inattentional blindness)",
        "جب انسانی دماغ کسی ایک کام پر شدید توجہ مرکوز کرتا ہے تو بصری نظام سامنے نظر آنے والی حیران کن چیز کو بھی نظر انداز کر دیتا ہے۔"
    ),
    (
        "Why does reading the word 'BLUE' printed in bright red ink cause human subjects to hesitate significantly before naming the ink color aloud?",
        ["The brain processes automatic word reading faster than color perception, creating cognitive interference (The Stroop Effect)", "Red and blue are complementary colors", "The optic nerve inverts red light", "Human speech motor centers are delayed by colors"],
        "The brain processes automatic word reading faster than color perception, creating cognitive interference (The Stroop Effect)",
        "Automated semantic text processing interferes with the slower sensory task of identifying pigment hue, slowing reaction times.",
        "جب لفظ 'نیلا' سرخ سیاہی میں لکھا ہو تو انسان سے سیاہی کا رنگ پوچھنے پر وہ بولنے میں ہچکچاہٹ کا شکار کیوں ہو جاتا ہے؟",
        ["دماغ لفظ کو رنگ سے پہلے پڑھ لیتا ہے جس سے دماغ میں تضاد اور رکاوٹ پیدا ہوتی ہے (Stroop Effect)", "سرخ اور نیلا متضاد رنگ ہیں", "بصری عصب سرخ کو الٹ دیتا ہے", "بولنے والے اعصاب رنگ سے الجھتے ہیں"],
        "دماغ لفظ کو رنگ سے پہلے پڑھ لیتا ہے جس سے دماغ میں تضاد اور رکاوٹ پیدا ہوتی ہے (Stroop Effect)",
        "اسٹروپ اثر بتاتا ہے کہ انسان لاشعوری طور پر لکھا ہوا لفظ فوراً پڑھتا ہے، جب لکھا ہوا لفظ اور سیاہی کا رنگ متضاد ہوں تو دماغ میں فیصلہ کرنے کی رفتار سست ہو جاتی ہے۔"
    ),
    (
        "A detective discovers a broken wristwatch at a crime scene. The hour hand is broken off completely, but the minute hand points precisely at 48 minutes past the hour. What was the exact position of the missing hour hand?",
        ["Four-fifths of the way between two numbers (precisely 288 degrees of the hour cycle)", "Directly on the number 9", "Halfway between two numbers", "Directly on the number 10"],
        "Four-fifths of the way between two numbers (precisely 288 degrees of the hour cycle)",
        "48 minutes represents 48/60 = 4/5 (0.8) of a complete hour; the hour hand moves proportionally 4/5 of the angular distance to the next hour.",
        "واردات کی جگہ سے ٹوٹی گھڑی ملی جس کی گھنٹے والی سوئی غائب تھی مگر منٹ والی سوئی بالکل 48 منٹ پر تھی۔ گھنٹے والی سوئی کی صحیح پوزیشن کیا تھی؟",
        ["دو ہندسوں کے درمیانی فاصلے کے پانچویں حصے کے چار بٹا پانچ (4/5) پر", "بالکل ہندسہ 9 پر", "دو ہندسوں کے بالکل درمیان میں", "بالکل ہندسہ 10 پر"],
        "دو ہندسوں کے درمیانی فاصلے کے پانچویں حصے کے چار بٹا پانچ (4/5) پر",
        "48 منٹ ایک گھنٹے کا 80 فیصد (4/5) حصہ ہوتا ہے، اس لیے گھنٹے کی سوئی موجودہ گھنٹے سے اگلے ہندسے کی طرف 80 فیصد فاصلہ طے کر چکی تھی۔"
    ),
    (
        "A bridge has a maximum load limit of 10 tons. A truck weighing exactly 10 tons starts crossing. Halfway across, a sparrow lands on the cab roof. Why does the bridge not collapse?",
        ["The truck burned enough fuel driving onto and across the bridge to offset the sparrow's weight", "Sparrows have hollow bones with zero mass", "Air currents supported the bird", "The bridge had a safety tolerance margin of zero"],
        "The truck burned enough fuel driving onto and across the bridge to offset the sparrow's weight",
        "Heavy diesel engines consume hundreds of grams of fuel per minute, losing far more mass than a 30-gram sparrow adds.",
        "ایک پل کا آخری بوجھ سنبھالنے کی حد 10 ٹن ہے۔ عین 10 ٹن کا ٹرک پل پر چڑھا، پل کے عین وسط میں ایک چڑیا ٹرک کی چھت پر آ بیٹھی۔ پل کیوں نہیں ٹوٹا؟",
        ["ٹرک نے پل پر چڑھتے اور چلتے ہوئے اتنا ایندھن جلا دیا تھا جس کا وزن چڑیا کے وزن سے زیادہ کم ہو چکا تھا", "چڑیا کی ہڈیاں کھوکھلی ہوتی ہیں اس لیے اس کا وزن صفر تھا", "ہوا نے چڑیا کا بوجھ سنبھال لیا", "پل پر کشش ثقل کم ہو گئی تھی"],
        "ٹرک نے پل پر چڑھتے اور چلتے ہوئے اتنا ایندھن جلا دیا تھا جس کا وزن چڑیا کے وزن سے زیادہ کم ہو چکا تھا",
        "ڈیزل انجن پل پر چلتے ہوئے سینکڑوں گرام ایندھن جلا دیتا ہے، جس سے ٹرک کا کل وزن چڑیا کے چند گرام وزن کے مقابلے میں کہیں زیادہ کم ہو چکا تھا۔"
    ),
    (
        "A prisoner is presented with two identical urns and 50 white marbles and 50 black marbles. The executioner will randomly pick one urn, and then randomly draw one marble. If white, the prisoner is freed; if black, executed. How should the prisoner distribute the marbles to maximize his survival chance?",
        ["Put 1 white marble in Urn A, and all remaining 99 marbles (49 white, 50 black) in Urn B", "Put 25 white and 25 black in each urn", "Put all 50 white in Urn A and all 50 black in Urn B", "Put 50 black in Urn A and 50 white in Urn B"],
        "Put 1 white marble in Urn A, and all remaining 99 marbles (49 white, 50 black) in Urn B",
        "This gives: 0.5 * (1/1) + 0.5 * (49/99) = 0.5 + 0.247 = ~74.7% survival probability, compared to 50% for equal splits.",
        "ایک قیدی کو 50 سفید اور 50 سیاہ کنکریاں دی گئیں اور دو خالی پیالے۔ جلاد کسی ایک پیالے سے بغیر دیکھے ایک کنکری نکالے گا۔ سفید نکلی تو رہائی، کالی نکلی تو موت۔ قیدی اپنی رہائی کا امکان زیادہ سے زیادہ (75%) کیسے بنا سکتا ہے؟",
        ["ایک پیالے میں صرف 1 سفید کنکری رکھے، اور دوسرے میں باقی تمام 99 کنکریاں (49 سفید اور 50 سیاہ) ڈال دے", "دونوں میں 25 سفید اور 25 سیاہ ڈالے", "ایک میں تمام سفید اور دوسرے میں تمام سیاہ ڈالے", "تمام کنکریاں ایک ہی پیالے میں ڈال دے"],
        "ایک پیالے میں صرف 1 سفید کنکری رکھے، اور دوسرے میں باقی تمام 99 کنکریاں (49 سفید اور 50 سیاہ) ڈال دے",
        "اس ترکیب سے پہلے پیالے کے چنے جانے پر رہائی کا امکان 100% ہو جاتا ہے، اور دوسرے پیالے میں تقریباً 50%۔ مجموعی امکان 74.7% تک پہنچ جاتا ہے۔"
    ),
    (
        "Why do ancient Roman aqueducts built of unreinforced stone arches still stand intact after two thousand years, while modern iron bridges require constant repainting and rust maintenance?",
        ["Stone arches remain permanently in compression and do not oxidize, whereas ferrous metals rust and suffer tensile fatigue", "Roman mortar was radioactive", "Stone absorbs atmospheric nitrogen", "Modern bridges are intentionally built fragile"],
        "Stone arches remain permanently in compression and do not oxidize, whereas ferrous metals rust and suffer tensile fatigue",
        "Compressive stone architecture suffers no rust degradation, and volcanic pozzolanic Roman concrete self-heals hairline fractures over centuries.",
        "رومن دور کے دو ہزار سال پرانے پتھریلی محرابوں والے پل آج بھی قائم ہیں جبکہ جدید لوہے کے پل چند دہائیوں میں زنگ آلود ہو کر مرمت مانگتے ہیں، کیوں؟",
        ["پتھر کی محرابیں ہمیشہ دباؤ (Compression) میں رہتی ہیں اور ان پر زنگ یا دھاتی تھکن کا اثر نہیں ہوتا", "رومن گارے میں تابکاری تھی", "پتھر ہوا کی نائٹروجن جذب کرتا ہے", "جدید پل جان بوجھ کر کمزور بنائے جاتے ہیں"],
        "پتھر کی محرابیں ہمیشہ دباؤ (Compression) میں رہتی ہیں اور ان پر زنگ یا دھاتی تھکن کا اثر نہیں ہوتا",
        "پتھر نہ تو زنگ کھاتا ہے اور نہ ہی لچکدار جھولنے سے ٹوٹتا ہے۔ رومن سیمنٹ میں چونے کے ذرات وقت کے ساتھ دراڑوں کو خود بخود بھرتے رہتے ہیں۔"
    ),
    (
        "A forensic pathologist notes that a body found in an unheated room in winter has no rigor mortis (stiffness), but the internal body temperature is 18°C (room ambient). Did the person die 2 hours ago or 3 days ago?",
        ["Approximately 3 days ago, because rigor mortis sets in within hours, peaks at 12 hours, and completely dissipates after 36-72 hours", "2 hours ago", "Within the last 30 minutes", "Time of death cannot be inferred"],
        "Approximately 3 days ago, because rigor mortis sets in within hours, peaks at 12 hours, and completely dissipates after 36-72 hours",
        "Rigor mortis is a temporary physiological state caused by ATP depletion. After 36-48 hours, autolytic decomposition breaks actin-myosin cross-bridges, restoring flaccidity.",
        "سردیوں میں ایک لاش ملی جس کا جسم بالکل نرم تھا (اکڑاؤ نہیں تھا) مگر لاش کا درجہ حرارت کمرے جتنا ٹھنڈا تھا۔ اس کی موت 2 گھنٹے پہلے ہوئی تھی یا 3 دن پہلے؟",
        ["تقریباً 3 دن پہلے، کیونکہ جسم کا اکڑاؤ 36 سے 48 گھنٹوں بعد گلنے کے عمل سے خود بخود ختم ہو جاتا ہے", "2 گھنٹے پہلے ہوئی تھی", "پچھلے آدھے گھنٹے میں", "موت کا وقت معلوم نہیں ہو سکتا"],
        "تقریباً 3 دن پہلے، کیونکہ جسم کا اکڑاؤ 36 سے 48 گھنٹوں بعد گلنے کے عمل سے خود بخود ختم ہو جاتا ہے",
        "موت کے 12 گھنٹے بعد جسم سخت اکڑ جاتا ہے، مگر 2 سے 3 دن بعد پٹھے گلنے سے اکڑاؤ مکمل ختم ہو جاتا ہے اور لاش دوبارہ بالکل نرم ہو جاتی ہے۔"
    ),
    (
        "A thief swaps a valuable painting in a museum gallery with a photographic forgery. The gallery guard notices the forgery immediately from 20 feet away under normal lighting without using magnifying glasses. What gave it away?",
        ["Specular highlights on the oil paint surface brushstrokes were completely flat and uniform on the printed photograph", "The photo had the wrong artist name", "The photograph frame was plastic", "The painting was upside down"],
        "Specular highlights on the oil paint surface brushstrokes were completely flat and uniform on the printed photograph",
        "Real impasto oil paintings have three-dimensional textured relief that reflects light dynamically; flat photos show static, painted highlights.",
        "میوزیم میں چور نے آئل پینٹنگ چرا کر اس کی جگہ ہائی ریزولوشن تصویر فریم میں لگا دی۔ گارڈ نے بیس فٹ دور سے دیکھتے ہی فوراً پکڑ لیا۔ اس نے کیا خامی دیکھی؟",
        ["اصلی آئل پینٹنگ کے رنگوں کا ابھار (Impasto) روشنی میں چمکتا ہے جبکہ فوٹو پر روشنی بالکل چپٹی پڑ رہی تھی", "فوٹو پر مصور کا نام غلط تھا", "تصویر کا فریم سستا پلاسٹک تھا", "پینٹنگ الٹی لٹکی ہوئی تھی"],
        "اصلی آئل پینٹنگ کے رنگوں کا ابھار (Impasto) روشنی میں چمکتا ہے جبکہ فوٹو پر روشنی بالکل چپٹی پڑ رہی تھی",
        "تیل کے رنگوں کے برش کے ابھار تین جہتی ہوتے ہیں جو مختلف زاویوں سے چمکتے ہیں، جبکہ فلیٹ پرنٹ شدہ کاغذ پر روشنی بالکل بے جان اور یکساں لگتی ہے۔"
    ),
    (
        "A diver drops a sealed glass jar full of air into a deep lake. At a depth of 10 meters (roughly 2 atmospheres of pressure), what happens to the internal air pressure inside the sealed rigid glass jar?",
        ["It remains exactly 1 atmosphere, because the rigid glass does not deform or compress under hydrostatic pressure", "It doubles to 2 atmospheres", "It drops to zero", "It quadruples to 4 atmospheres"],
        "It remains exactly 1 atmosphere, because the rigid glass does not deform or compress under hydrostatic pressure",
        "Unless the rigid vessel deforms or breaches, the enclosed gas volume and moles are constant, maintaining 1 atm internal pressure.",
        "ہوا سے بند شیشے کے مضبوط جار کو جھیل میں 10 میٹر گہرائی (جہاں بیرونی دباؤ دوگنا ہوتا ہے) میں ڈبویا گیا۔ جار کے اندر ہوا کا دباؤ کتنا ہوگا؟",
        ["بالکل 1 ایٹموسفیئر رہے گا کیونکہ سخت شیشہ بیرونی دباؤ سے اندر کی ہوا کو دبنے نہیں دیتا", "دگنا ہو کر 2 ایٹموسفیئر ہو جائے گا", "صفر ہو جائے گا", "چار گنا ہو جائے گا"],
        "بالکل 1 ایٹموسفیئر رہے گا کیونکہ سخت شیشہ بیرونی دباؤ سے اندر کی ہوا کو دبنے نہیں دیتا",
        "اگر برتن لچکدار (جیسے غبارہ) ہوتا تو سکڑ جاتا، مگر شیشہ اپنی شکل برقرار رکھتا ہے اس لیے اندرونی ہوا پر کوئی اضافی دباؤ نہیں پڑتا۔"
    ),
    (
        "A coin is flipped 9 times and lands on heads every single time. What is the exact mathematical probability that the 10th flip will land on heads, assuming an honest, fair coin?",
        ["Exactly 50 percent (1 in 2)", "Less than 1 percent", "90 percent", "75 percent"],
        "Exactly 50 percent (1 in 2)",
        "The Gambler's Fallacy leads people to believe tails is 'due'. Independent random trials have no memory; each flip remains 50/50.",
        "ایک منصفانہ سکے کو 9 بار اچھالا گیا اور نو کی نو بار 'ہیڈز' (Heads) آیا۔ دسویں بار سکے کے 'ہیڈز' آنے کا حقیقی ریاضیاتی امکان کتنا ہے؟",
        ["بالکل 50 فیصد (آدھا امکان)", "ایک فیصد سے بھی کم", "90 فیصد", "75 فیصد"],
        "بالکل 50 فیصد (آدھا امکان)",
        "جواریوں کا مغالطہ (Gambler's Fallacy) لوگوں کو یہ سوچنے پر مجبور کرتا ہے کہ اب ٹیل آنا لازمی ہے، حالانکہ سکے کی کوئی یادداشت نہیں ہوتی، ہر ٹاس آزادانہ 50/50 ہوتا ہے۔"
    ),
    (
        "Why do antique cast-iron frying pans become non-stick and naturally glossy black after years of proper culinary use?",
        ["Fats and cooking oils undergo high-temperature thermal polymerization, forming a cross-linked hydrophobic polymer coating bonded to iron", "Iron rusts into black carbon", "Charred food layers accumulate", "The iron absorbs black atmospheric minerals"],
        "Fats and cooking oils undergo high-temperature thermal polymerization, forming a cross-linked hydrophobic polymer coating bonded to iron",
        "Unsaturated fatty acids oxidize and cross-link when heated past their smoke point, polymerizing into a durable, slick plastic-like resin matrix.",
        "لوہے کا پرانا فرائنگ پین برسوں کے استعمال کے بعد چمکدار کالا اور نان اسٹک (Non-stick) کیسے بن جاتا ہے؟",
        ["کھانے کے تیل گرمی پا کر پولیمرائز (Polymerize) ہو کر لوہے کی سطح پر قدرتی نان اسٹک پلاسٹک جیسی تہہ جما دیتے ہیں", "لوہا کالے کاربن میں بدل جاتا ہے", "جلے ہوئے کھانے کی راکھ جمتی ہے", "لوہا ہوا سے سیاہی چوس لیتا ہے"],
        "کھانے کے تیل گرمی پا کر پولیمرائز (Polymerize) ہو کر لوہے کی سطح پر قدرتی نان اسٹک پلاسٹک جیسی تہہ جما دیتے ہیں",
        "اسے سیزننگ (Seasoning) کہتے ہیں۔ تیل کے فیٹی ایسڈز شدید حرارت میں لوہے کے مساموں کے ساتھ جڑ کر ایک قدرتی، چکنی اور واٹر پروف تہہ بنا لیتے ہیں۔"
    ),
    (
        "A clock in a tower strikes 6 o'clock in exactly 15 seconds (from the start of the first chime to the end of the sixth chime). How many seconds does it take to strike 12 o'clock?",
        ["33 seconds", "30 seconds", "36 seconds", "24 seconds"],
        "33 seconds",
        "Striking 6 involves 5 time intervals between 6 chimes: 15 / 5 = 3 seconds per interval. Striking 12 involves 11 intervals: 11 * 3 = 33 seconds.",
        "ایک گھنٹہ گھر کی گھنٹی 6 بجے 6 بار بجنے میں عین 15 سیکنڈ لیتی ہے (پہلی سے چھٹی گھنٹی تک)۔ 12 بجے 12 بار بجنے میں اسے کتنے سیکنڈ لگیں گے؟",
        ["33 سیکنڈ", "30 سیکنڈ", "36 سیکنڈ", "24 سیکنڈ"],
        "33 سیکنڈ",
        "چھ گھنٹیوں کے درمیان 5 وقفے ہوتے ہیں، یعنی ہر وقفہ 3 سیکنڈ کا ہے (15 / 5 = 3)۔ بارہ گھنٹیوں کے درمیان 11 وقفے ہوں گے، اس لیے 11 × 3 = 33 سیکنڈ لگیں گے۔"
    ),
    (
        "Why does a person looking at an illuminated computer screen in a pitch-black room experience significant eye strain compared to having a warm lamp on in the background?",
        ["Pupils must continuously fluctuate between high contrast luminance levels, exhausting the ciliary and pupillary muscles", "Computer screens emit toxic radioactive photons", "Darkness dries out tear ducts permanently", "The retina stops producing rhodopsin"],
        "Pupils must continuously fluctuate between high contrast luminance levels, exhausting the ciliary and pupillary muscles",
        "Extreme luminance contrast between the bright display and dark ambient surroundings causes visual fatigue and glare discomfort.",
        "گھپ اندھیرے کمرے میں موبائل یا کمپیوٹر اسکرین دیکھنے سے آنکھوں پر ہلکی لائٹ والے کمرے کے مقابلے میں اتنا شدید دباؤ کیوں پڑتا ہے؟",
        ["تیز اسکرین اور گھپ اندھیرے کے زبردست تضاد (Contrast) کی وجہ سے آنکھ کی پتلی کے پٹھے مسلسل تھک جاتے ہیں", "اسکرین تابکاری خارج کرتی ہے", "اندھیرے میں آنسو سوکھ جاتے ہیں", "آنکھیں دیکھنا بند کر دیتی ہیں"],
        "تیز اسکرین اور گھپ اندھیرے کے زبردست تضاد (Contrast) کی وجہ سے آنکھ کی پتلی کے پٹھے مسلسل تھک جاتے ہیں",
        "آنکھ کی پتلی کو اندھیرے اور روشنی کے درمیان بار بار سکڑنا اور پھیلنا پڑتا ہے، کمرے میں ہلکی بیک گراؤنڈ لائٹ اس تضاد کو ختم کر کے سکون دیتی ہے۔"
    ),
    (
        "A detective interviews three witnesses to a hit-and-run crash. Witness A says the car was blue; Witness B says it was dark grey; Witness C says it was dark blue. The collision happened at 2:00 AM under low-pressure sodium yellow streetlights. What was the true color of the car?",
        ["Blue (sodium monochromatic yellow light renders pure blue as very dark or charcoal grey)", "Bright yellow", "White", "Bright red"],
        "Blue (sodium monochromatic yellow light renders pure blue as very dark or charcoal grey)",
        "Low-pressure sodium vapor lamps emit narrow monochromatic light around 589 nm; blue pigments reflect no yellow light, appearing nearly black or dark grey.",
        "رات دو بجے زرد اسٹریٹ لائٹس کے نیچے ایک کار حادثہ ہوا۔ ایک گواہ نے کہا کار نیلی تھی، دوسرے نے کہا گہری سرمئی تھی، تیسرے نے کہا گہری نیلی تھی۔ کار کا اصل رنگ کیا تھا؟",
        ["نیلا رنگ (زرد روشنی میں نیلا رنگ روشنی واپس نہیں پلٹاتا اور گہرا سرمئی یا سیاہ لگتا ہے)", "چمکیلا زرد", "سفید", "سرخ"],
        "نیلا رنگ (زرد روشنی میں نیلا رنگ روشنی واپس نہیں پلٹاتا اور گہرا سرمئی یا سیاہ لگتا ہے)",
        "سوڈیم اسٹریٹ لائٹس صرف ایک ہی زرد طول موج خارج کرتی ہیں۔ نیلی کار پر جب نیلی روشنی نہیں پڑتی تو وہ روشنی منعکس نہیں کر پاتی اور سرمئی نظر آتی ہے۔"
    ),
    (
        "Why do birds sitting on power lines fly away in unison seconds before an earthquake tremor is felt by humans on the ground?",
        ["Avian leg somatosensory mechanoreceptors (Herbst corpuscles) detect fast high-frequency primary P-waves long before destructive S-waves arrive", "Birds see electromagnetic radiation from faults", "Birds smell ozone released by cracked soil", "Birds hear infrasound from Earth's core"],
        "Avian leg somatosensory mechanoreceptors (Herbst corpuscles) detect fast high-frequency primary P-waves long before destructive S-waves arrive",
        "Primary compressive seismic P-waves travel nearly twice as fast as shearing S-waves, triggering alert behaviors in sensitive animal sensors.",
        "زلزلے کا جھٹکا انسانوں کو محسوس ہونے سے چند لمحے پہلے تاروں پر بیٹھے پرندے اچانک ایک ساتھ کیوں اڑ جاتے ہیں؟",
        ["پرندوں کے پنجوں میں موجود حساس حسیں زلزلے کی تیز رفتار پی ویوز (P-waves) کو انسانوں سے پہلے محسوس کر لیتی ہیں", "پرندے زمین سے نکلتی روشنی دیکھ لیتے ہیں", "وہ زمین کی اوزون سونگھ لیتے ہیں", "وہ زمین کے مرکز کی آواز سنتے ہیں"],
        "پرندوں کے پنجوں میں موجود حساس حسیں زلزلے کی تیز رفتار پی ویوز (P-waves) کو انسانوں سے پہلے محسوس کر لیتی ہیں",
        "زلزلے کی بنیادی لہریں (P-waves) تباہ کن ثانوی لہروں سے دگنی رفتار سے سفر کرتی ہیں۔ جانور ان باریک ارتعاشات کو فوراً بھانپ لیتے ہیں۔"
    ),
    (
        "A courier is tasked with delivering a package across a desert in 4 days. One person can only carry 3 days of water rations. How many people minimum are needed to deliver the package safely with everyone returning alive?",
        ["2 people (helper walks out 1 day, transfers 1 day ration to courier, keeps 1 day to return)", "3 people", "1 person", "4 people"],
        "2 people (helper walks out 1 day, transfers 1 day ration to courier, keeps 1 day to return)",
        "Day 1: Both consume 1 day water. Helper transfers 1 ration to courier (courier full with 3). Helper uses remaining 1 to walk back. Courier crosses remaining 3 days.",
        "ایک صحرا پار کرنے میں 4 دن لگتے ہیں۔ ایک شخص اپنے ساتھ صرف 3 دن کے پانی کا راشن اٹھا سکتا ہے۔ تمام ساتھیوں کے زندہ واپس لوٹنے کے ساتھ پارسل پہنچانے کے لیے کم از کم کتنے افراد درکار ہوں گے؟",
        ["2 افراد (معاون ایک دن ساتھ چلے گا، ایک دن کا راشن قاصد کو دے کر ایک دن کے راشن سے واپس آ جائے گا)", "3 افراد", "اکیلا 1 شخص", "4 افراد"],
        "2 افراد (معاون ایک دن ساتھ چلے گا، ایک دن کا راشن قاصد کو دے کر ایک دن کے راشن سے واپس آ جائے گا)",
        "پہلے دن دونوں ایک ایک بوتل پی لیں گے۔ معاون اپنی ایک بوتل قاصد کو دے دے گا (قاصد کے پاس 3 دن کا راشن پورا ہو جائے گا) اور آخری بوتل پی کر خود واپس لوٹ جائے گا۔"
    ),
    (
        "Why does an ordinary lead pencil leave a dark, erasable mark on paper without needing any liquid ink?",
        ["Graphite consists of stacked sheets of carbon atoms bonded weakly by van der Waals forces, shearing off onto paper fibers", "Lead melts from writing friction", "Paper chemical acid dissolves graphite", "Pencils contain powdered charcoal glue"],
        "Graphite consists of stacked sheets of carbon atoms bonded weakly by van der Waals forces, shearing off onto paper fibers",
        "Layers of sp2 carbon slide over one another easily; mechanical friction delaminates microscopic graphene flakes onto cellulose.",
        "سیسے کی عام پنسل (Pencil) بغیر کسی مائع سیاہی کے کاغذ پر گہرا مٹنے والا نشان کیسے چھوڑ دیتی ہے؟",
        ["گریفائٹ کی کاربن تہیں آپس میں کمزور بندھنوں سے جڑی ہوتی ہیں جو رگڑ سے الگ ہو کر کاغذ کے ریشوں پر چپک جاتی ہیں", "پنسل کا سکہ رگڑ سے پگھلتا ہے", "کاغذ کا تیزاب پنسل کو گھولتا ہے", "پنسل میں گوند بھری ہوتی ہے"],
        "گریفائٹ کی کاربن تہیں آپس میں کمزور بندھنوں سے جڑی ہوتی ہیں جو رگڑ سے الگ ہو کر کاغذ کے ریشوں پر چپک جاتی ہیں",
        "گریفائٹ کی ایٹمی تہیں تاش کے پتوں کی طرح ایک دوسرے پر پھسلتی ہیں، جب پنسل کاغذ پر چلتی ہے تو رگڑ ان باریک تہوں کو کاغذ پر اتار دیتی ہے۔"
    ),
    (
        "A homeowner notices that a basement door sticks tightly in the doorframe during humid summer months, but swings freely and loosely in winter. Why?",
        ["Wood absorbs moisture from humid summer air, swelling across its cellular grain", "The foundation rises in summer", "The metal hinges expand more than wood", "Summer gravity compresses the frame"],
        "Wood absorbs moisture from humid summer air, swelling across its cellular grain",
        "Cellulose fibers in wood are hygroscopic, taking up ambient water vapor in high humidity and expanding perpendicular to grain orientation.",
        "تہہ خانے کا لکڑی کا دروازہ سخت گرمیوں اور برسات میں چوکھٹ میں پھنس جاتا ہے جبکہ سردیوں میں بالکل ڈھیلا اور آزاد ہو جاتا ہے، کیوں؟",
        ["لکڑی برسات کی مرطوب ہوا سے نمی جذب کر کے پھیل جاتی ہے اور چوکھٹ میں پھنس جاتی ہے", "مکان کی بنیادیں گرمی میں اوپر اٹھتی ہیں", "قبضے زیادہ پھیل جاتے ہیں", "گرمیوں کی کشش ثقل دروازے کو دبا دیتی ہے"],
        "لکڑی برسات کی مرطوب ہوا سے نمی جذب کر کے پھیل جاتی ہے اور چوکھٹ میں پھنس جاتی ہے",
        "لکڑی کے ریشے فضا کی نمی کو اسفنج کی طرح چوس لیتے ہیں جس سے اس کی چوڑائی بڑھ جاتی ہے۔ سردیوں کی خشک ہوا میں نمی اڑتے ہی وہ دوبارہ سکڑ جاتی ہے۔"
    ),
    (
        "Why does a bicycle wheel feel dramatically heavier and resist changing direction when you hold the axle in your hands while it spins rapidly?",
        ["Conservation of angular momentum exerts gyroscopic resistance against any torque attempting to alter its axis of rotation", "The wheel gains physical mass from spinning", "Centrifugal force increases weight", "Air turbulence pushes against hands"],
        "Conservation of angular momentum exerts gyroscopic resistance against any torque attempting to alter its axis of rotation",
        "Torque equals the time rate of change of angular momentum (tau = dL/dt); pivoting the spinning axis requires substantial perpendicular muscular torque.",
        "گھومتے ہوئے سائیکل کے پہیے کی ایکسل کو ہاتھ میں پکڑ کر اس کا رخ دائیں یا بائیں موڑنے کی کوشش کریں تو وہ غیر معمولی مزاحمت کیوں کرتا ہے؟",
        ["زاویائی مومینٹم (Angular momentum) پہیے کے گھومنے کے محور کو تبدیل ہونے سے سختی سے روکتا ہے (گائروسکوپک اثر)", "تیز گھومنے سے پہیے کا وزن بڑھ جاتا ہے", "مرکز گریز قوت ہاتھوں کو دباتی ہے", "ہوا کا دباؤ پہیے کو روکتا ہے"],
        "زاویائی مومینٹم (Angular momentum) پہیے کے گھومنے کے محور کو تبدیل ہونے سے سختی سے روکتا ہے (گائروسکوپک اثر)",
        "جب کوئی وزنی چیز تیز گھومتی ہے تو اس کا زاویائی مومینٹم اس کی سمت کو قائم رکھنا چاہتا ہے۔ ہاتھ سے موڑنے پر وہ خود کو بچانے کے لیے مخالف زور لگاتا ہے۔"
    ),
    (
        "A chemist places an unopened can of diet cola and an unopened can of regular sugary cola into a bucket of water. The diet cola floats, while the regular cola sinks to the bottom. Why?",
        ["Regular cola contains dense dissolved high-fructose corn syrup (roughly 39 grams of sugar), increasing overall can density above water", "Diet cola contains helium gas", "Regular cola cans use thicker aluminum", "Diet cans contain less liquid volume"],
        "Regular cola contains dense dissolved high-fructose corn syrup (roughly 39 grams of sugar), increasing overall can density above water",
        "The sugar adds roughly 39g of dense mass without expanding can volume, making the bulk density of regular cola greater than 1.0 g/cm^3.",
        "ڈائٹ کولا اور عام میٹھی کولا کے دو بند کین پانی کی بالٹی میں ڈالے گئے۔ ڈائٹ کولا تیرتا رہا جبکہ میٹھا کین تہہ میں ڈوب گیا۔ دونوں کا حجم برابر ہونے کے باوجود کیوں؟",
        ["عام کولا میں تقریباً 39 گرام بھاری چینی گھلی ہوتی ہے جس سے کین کی مجموعی کثافت پانی سے زیادہ ہو جاتی ہے", "ڈائٹ کولا میں ہیلیئم گیس بھری ہوتی ہے", "عام کین کی ایلومینیم موٹی ہوتی ہے", "ڈائٹ کین میں مشروب کم ہوتا ہے"],
        "عام کولا میں تقریباً 39 گرام بھاری چینی گھلی ہوتی ہے جس سے کین کی مجموعی کثافت پانی سے زیادہ ہو جاتی ہے",
        "ڈائٹ کولا میں مصنوعی میٹھا ایک گرام کے دسویں حصے جتنا ہوتا ہے، جبکہ عام کین میں 39 گرام وزنی شکر ہوتی ہے جو کین کا اوسط وزن پانی سے زیادہ کر کے اسے ڈبو دیتی ہے۔"
    ),
    (
        "Why do bubbles inside a freshly poured glass of dark Guinness stout beer appear to sink downward along the glass wall rather than rise?",
        ["Upward convective fluid flow in the wider center drags fluid and bubbles down along the cooler, drag-prone glass walls", "Guinness bubbles are heavier than liquid", "The nitrogen gas has negative buoyancy", "Surface tension pushes foam downward"],
        "Upward convective fluid flow in the wider center drags fluid and bubbles down along the cooler, drag-prone glass walls",
        "Wall drag slows bubbles near the perimeter while central bubbles rise rapidly, setting up a circulating convection roll that carries perimeter bubbles down.",
        "گنیز اسٹاؤٹ (Dark stout) کے گلاس میں فوم کے باریک بلبلے اوپر اٹھنے کی بجائے شیشے کے کنارے نیچے گرتے ہوئے کیوں دکھائی دیتے ہیں؟",
        ["درمیان میں بلبلوں کے تیز ابھار کی وجہ سے کناروں پر مائع کی لہر بلبلوں کو اپنے ساتھ نیچے کھینچتی ہے", "بلبلے مائع سے زیادہ وزنی ہوتے ہیں", "نائٹروجن گیس میں منفی اچھال ہوتا ہے", "جھاگ کا سطحی تناؤ بلبلوں کو دباتا ہے"],
        "درمیان میں بلبلوں کے تیز ابھار کی وجہ سے کناروں پر مائع کی لہر بلبلوں کو اپنے ساتھ نیچے کھینچتی ہے",
        "گلاس کے عین بیچ میں بلبلے اتنی تیزی سے اوپر اٹھتے ہیں کہ مائع کا ایک گرداب بن جاتا ہے جو شیشے کی دیوار کے ساتھ والے بلبلوں کو وقتی طور پر نیچے بہا لے جاتا ہے۔"
    ),
    (
        "A hiker lost in the woods on an overcast day determines north accurately without a compass or visible sun. He checks the moss on tree trunks and finds it uniformly distributed, but notices tree branch growth is consistently thicker on one side. Which side?",
        ["South (in the Northern Hemisphere, trees receive more direct sunlight from the south, promoting vigorous foliage growth)", "North", "East", "West"],
        "South (in the Northern Hemisphere, trees receive more direct sunlight from the south, promoting vigorous foliage growth)",
        "Photosynthetic heliotropism drives branches and leaf density toward the sun's trajectory, which lies to the south in northern temperate latitudes.",
        "شمالی نصف کرہ کے جنگل میں بادلوں والے دن بغیر قطب نما کے ایک مسافر درخت کی شاخوں سے سمت معلوم کرتا ہے۔ شاخیں کس سمت میں زیادہ گھنی اور پھیلی ہوئی ہوں گی؟",
        ["جنوب کی سمت (کیونکہ شمالی نصف کرہ میں سورج جنوب سے زیادہ روشنی اور توانائی دیتا ہے)", "شمال کی سمت", "مشرق کی سمت", "مغرب کی سمت"],
        "جنوب کی سمت (کیونکہ شمالی نصف کرہ میں سورج جنوب سے زیادہ روشنی اور توانائی دیتا ہے)",
        "پودے روشنی کی طرف بڑھتے ہیں۔ خط استوا کی طرف سے آنے والی دھوپ کی وجہ سے درختوں کی جنوبی شاخیں زیادہ لمبی، مضبوط اور پتوں سے بھری ہوتی ہیں۔"
    ),
    (
        "Why does a person who has been spinning on a playground merry-go-round feel their surroundings continue to spin in the opposite direction when they abruptly stop?",
        ["Inertia causes endolymph fluid in the inner ear's semicircular canals to keep moving, bending hair cell cupulae in reverse", "The optic nerve continues spinning", "Brain blood pressure drops", "Eye muscles spasm randomly"],
        "Inertia causes endolymph fluid in the inner ear's semicircular canals to keep moving, bending hair cell cupulae in reverse",
        "Fluid momentum in vestibular canals keeps flowing after the head stops, deflecting stereocilia and signaling perceived rotational motion in reverse.",
        "جھولے پر گول چکر کاٹنے کے بعد جب انسان اچانک رکتا ہے تو اسے دنیا مخالف سمت میں گھومتی ہوئی کیوں نظر آتی ہے؟",
        ["اندرونی کان کے توازن کے مائع کا انرشیا رکنے کے بعد بھی جاری رہتا ہے جو اعصاب کو مخالف سمت کا سگنل بھیجتا ہے", "بصری عصب گھومتا رہتا ہے", "دماغ میں خون کا دباؤ گر جاتا ہے", "آنکھ کے پٹھے کھنچ جاتے ہیں"],
        "اندرونی کان کے توازن کے مائع کا انرشیا رکنے کے بعد بھی جاری رہتا ہے جو اعصاب کو مخالف سمت کا سگنل بھیجتا ہے",
        "کان کے سوراخوں میں موجود مائع جسم کے رکنے کے بعد بھی اپنے مومینٹم کی وجہ سے بہتا رہتا ہے، جس سے دماغ کو لگتا ہے کہ ہم اب الٹی سمت میں گھوم رہے ہیں۔"
    ),
    (
        "Why does an ordinary refrigerator magnet cling tightly to the steel refrigerator door, but slides down slowly if a single sheet of heavy cardboard is placed between them?",
        ["Magnetic field strength drops off dramatically with distance (inversely with roughly the cube or fourth power of separation)", "Cardboard demagnetizes the magnet", "Cardboard creates electromagnetic shielding", "Gravity increases on cardboard"],
        "Magnetic field strength drops off dramatically with distance (inversely with roughly the cube or fourth power of separation)",
        "Dipole magnetic attraction falls rapidly over distance (F ~ 1/r^4); increasing air gap thickness drastically diminishes magnetic holding force.",
        "فریج کا مقناطیس لوہے کے دروازے پر مضبوطی سے چپکتا ہے مگر درمیان میں ایک موٹا گتا رکھنے پر وہ پھسل کر نیچے کیوں گر جاتا ہے؟",
        ["مقناطیسی کشش کا زور فاصلہ بڑھنے سے انتہائی تیزی سے کمزور ہو جاتا ہے (فاصلے کے کیوب کے تناسب سے)", "گتا مقناطیس کی طاقت چوس لیتا ہے", "گتا برقی شیلڈ بنا دیتا ہے", "گتے پر کشش ثقل بڑھ جاتی ہے"],
        "مقناطیسی کشش کا زور فاصلہ بڑھنے سے انتہائی تیزی سے کمزور ہو جاتا ہے (فاصلے کے کیوب کے تناسب سے)",
        "مقناطیسی فیلڈ فاصلے کے ساتھ بہت تیزی سے گھٹتی ہے۔ گتے کی چند ملی میٹر موٹائی مقناطیس اور لوہے کے درمیان فاصلہ بڑھا کر گرفت کو بے اثر کر دیتی ہے۔"
    ),
    (
        "Why does an airplane cabin crew instruct passengers to raise window shades during takeoff and landing operations?",
        ["To allow passengers' eyes to adjust to outdoor lighting and help crew spot external engine fire or structural hazards immediately", "To provide interior lighting and save battery", "To balance cabin air pressure", "To signal air traffic controllers"],
        "To allow passengers' eyes to adjust to outdoor lighting and help crew spot external engine fire or structural hazards immediately",
        "Situational awareness during the critical flight phases ensures rapid cabin evacuation readiness and visual inspection of wing surfaces.",
        "ہوائی جہاز کے ٹیک آف اور لینڈنگ کے دوران ائیر ہوسٹس تمام کھڑکیوں کے پردے اوپر اٹھانے کی ہدایت کیوں کرتی ہیں؟",
        ["تاکہ ہنگامی صورتحال میں آنکھیں بیرونی روشنی کی عادی رہیں اور مسافر یا عملہ انجن کی آگ اور خطرہ فوراً دیکھ سکیں", "کیبن کی لائٹ کی بیٹری بچانے کے لیے", "ہوا کا دباؤ برابر کرنے کے لیے", "کنٹرول ٹاور کو اشارہ دینے کے لیے"],
        "تاکہ ہنگامی صورتحال میں آنکھیں بیرونی روشنی کی عادی رہیں اور مسافر یا عملہ انجن کی آگ اور خطرہ فوراً دیکھ سکیں",
        "ٹیک آف اور لینڈنگ کے چند منٹ سب سے نازک ہوتے ہیں۔ کھڑکیاں کھلی ہونے سے بیرونی حالات صاف نظر آتے ہیں اور ہنگامی انخلاء میں سیکنڈوں کی بچت ہوتی ہے۔"
    ),
    (
        "A submarine descends into the deepest trenches of the ocean. Why are modern submarine hulls designed with a cylindrical circular cross-section rather than an oval or square shape?",
        ["A circle distributes hydrostatic compressive pressure uniformly without localized stress concentrations or weak shear points", "Circles are easier to paint", "Rectangular hulls capsize easily", "Fish avoid circular shapes"],
        "A circle distributes hydrostatic compressive pressure uniformly without localized stress concentrations or weak shear points",
        "Radial symmetry under external hydrostatic pressure ensures purely compressive membrane stress, preventing catastrophic structural buckling.",
        "گہرے سمندر میں اترنے والی آبدوزوں کا خول چوکور یا بیضوی بنانے کی بجائے بالکل گول سلنڈر نما کیوں بنایا جاتا ہے؟",
        ["گولائی پانی کے شدید دباؤ کو چاروں طرف یکساں بانٹ دیتی ہے جس سے کوئی کمزور کونا یا دباؤ کا نقطہ نہیں بنتا", "گول خول پر رنگ کرنا آسان ہوتا ہے", "چوکور آبدوزیں فوراً الٹ جاتی ہیں", "مچھلیاں گول شکل سے دور رہتی ہیں"],
        "گولائی پانی کے شدید دباؤ کو چاروں طرف یکساں بانٹ دیتی ہے جس سے کوئی کمزور کونا یا دباؤ کا نقطہ نہیں بنتا",
        "اگر آبدوز میں کونے ہوں تو پانی کا لاکھوں ٹن دباؤ کونوں پر جمع ہو کر لوہے کو توڑ دے گا۔ گول شکل میں دباؤ ہر طرف یکساں تقسیم ہو جاتا ہے۔"
    ),
    (
        "Why does a sound made inside a swimming pool sound completely muffled and almost inaudible to someone standing right by the edge in open air?",
        ["The immense acoustic impedance mismatch between water and air reflects over 99.9 percent of acoustic sound wave energy back into the water", "Air absorbs water frequencies chemically", "Chlorine filters out sound waves", "Water molecules trap sound permanently"],
        "The immense acoustic impedance mismatch between water and air reflects over 99.9 percent of acoustic sound wave energy back into the water",
        "Because water density and sound speed vastly exceed air's, the boundary acts as an acoustic mirror, reflecting nearly all sound.",
        "سوئمنگ پول کے اندر پانی میں غوطہ لگا کر بولا گیا لفظ پول کے کنارے کھڑے انسان کو باہر ہوا میں کیوں سنائی نہیں دیتا؟",
        ["پانی اور ہوا کی صوتی رکاوٹ (Acoustic impedance) میں اتنے بڑے فرق کی وجہ سے 99.9 فیصد آواز واپس پانی میں ہی پلٹ جاتی ہے", "ہوا پانی کی آواز کو کیمیائی طور پر مار دیتی ہے", "کلورین آواز کو روکتا ہے", "پانی کے مالیکیولز آواز کو قید کر لیتے ہیں"],
        "پانی اور ہوا کی صوتی رکاوٹ (Acoustic impedance) میں اتنے بڑے فرق کی وجہ سے 99.9 فیصد آواز واپس پانی میں ہی پلٹ جاتی ہے",
        "پانی ہوا سے تقریباً 800 گنا زیادہ کثیف ہے۔ آواز جب پانی کی سطح سے ٹکراتی ہے تو وہ ہوا میں داخل ہونے کی بجائے شیشے کے آئینے کی طرح واپس اندر منعکس ہو جاتی ہے۔"
    ),
    (
        "A person throws two identical paper sheets from a second-story balcony: one crumpled tightly into a solid ball, one left flat. Why does the crumpled ball hit the ground far earlier?",
        ["The crumpled ball has a dramatically smaller frontal surface area, minimizing aerodynamic drag and raising terminal velocity", "The ball gains gravitational mass", "Flat paper repels Earth's gravity", "Air pressure pushes flat paper upward permanently"],
        "The crumpled ball has a dramatically smaller frontal surface area, minimizing aerodynamic drag and raising terminal velocity",
        "While gravitational downward force (mg) is identical for both, air drag is proportional to cross-sectional area (F_drag ~ A * v^2).",
        "ایک ہی سائز کے دو کاغذ دوسری منزل سے بیک وقت گرائے گئے: ایک کو موڑ کر گول گیند بنا دیا گیا اور دوسرا سیدھا چھوڑا گیا۔ مڑا ہوا کاغذ پہلے زمین پر کیوں پہنچا؟",
        ["کاغذ کی گیند کا سامنے کا سطحی رقبہ بہت چھوٹا ہو گیا جس سے ہوا کی رکاوٹ (Air drag) نہ ہونے کے برابر رہ گئی", "گیند بننے سے کاغذ کا وزن بڑھ گیا", "سیدھا کاغذ زمین کی کشش کو روکتا ہے", "ہوا سیدھے کاغذ کو مستقل اوپر اٹھاتی ہے"],
        "کاغذ کی گیند کا سامنے کا سطحی رقبہ بہت چھوٹا ہو گیا جس سے ہوا کی رکاوٹ (Air drag) نہ ہونے کے برابر رہ گئی",
        "دونوں کاغذوں پر کشش ثقل بالکل برابر تھی۔ مگر فلیٹ کاغذ بڑے رقبے کی وجہ سے پیراشوٹ کی طرح ہوا پر تیرنے لگا جبکہ گیند نے ہوا کو کاٹ دیا۔"
    ),
    (
        "Why does an ocean ship sailing near a large ice sheet experience calm, wave-free waters even in strong gale winds?",
        ["Floating sea ice fragments physically disrupt wind-wave coupling and dampen surface wave orbital motion through viscous friction", "Ice freezes the wind in place", "Ice sheets lower atmospheric pressure", "The cold water solidifies immediately"],
        "Floating sea ice fragments physically disrupt wind-wave coupling and dampen surface wave orbital motion through viscous friction",
        "The marginal ice zone scatters and dissipates mechanical wave energy, acting as a massive floating hydrodynamic shock absorber.",
        "سمندر میں تیرتے ہوئے برفانی تودوں (Ice floes) کے قریب پہنچتے ہی سمندر کی بڑی لہریں تیز ہوا کے باوجود اچانک پرسکون اور ہموار کیوں ہو جاتی ہیں؟",
        ["تیرتے ہوئے برف کے ٹکڑے لہروں کے جھٹکوں کو آپس میں رگڑ کھا کر جذب کر لیتے ہیں اور لہروں کا بننا روک دیتے ہیں", "برف ہوا کو جما دیتی ہے", "برف کی چٹانیں ہوا کا دباؤ گرا دیتی ہیں", "سرد پانی خود بخود جم جاتا ہے"],
        "تیرتے ہوئے برف کے ٹکڑے لہروں کے جھٹکوں کو آپس میں رگڑ کھا کر جذب کر لیتے ہیں اور لہروں کا بننا روک دیتے ہیں",
        "برف کے بے شمار ٹکڑے پانی کی سطح پر ایک لچکدار رکاوٹ بن جاتے ہیں، جس سے ہوا کا پانی پر دباؤ لہریں نہیں بنا پاتا اور پانی بالکل پرسکون رہتا ہے۔"
    ),
    (
        "Why does a metallic spoon placed inside an oven reach oven temperature in 30 minutes, while an identical mass of raw potato takes over an hour to cook through?",
        ["Potatoes consist mostly of water with high specific heat capacity and undergo evaporative cooling and slow internal thermal conduction", "Metals generate internal atomic heat", "Potatoes reflect radiant infrared rays", "The oven fan only blows on metal"],
        "Potatoes consist mostly of water with high specific heat capacity and undergo evaporative cooling and slow internal thermal conduction",
        "Water has a huge specific heat capacity (4.18 J/g*K) compared to iron (0.45 J/g*K), requiring tenfold more thermal energy per gram to heat up.",
        "اوون میں رکھا لوہے کا چمچ آدھے گھنٹے میں دہک اٹھتا ہے مگر اسی وزن کا آلو اندر تک پکنے میں گھنٹہ بھر سے زیادہ وقت کیوں لیتا ہے؟",
        ["آلو میں پانی کی مقدار زیادہ ہوتی ہے جس کی حرارت مخصوصہ (Specific heat) لوہے سے دس گنا زیادہ ہوتی ہے", "لوہا خود اندر سے حرارت بناتا ہے", "آلو اوون کی شعاعوں کو واپس پلٹاتا ہے", "اوون کا پنکھا صرف دھات پر چلتا ہے"],
        "آلو میں پانی کی مقدار زیادہ ہوتی ہے جس کی حرارت مخصوصہ (Specific heat) لوہے سے دس گنا زیادہ ہوتی ہے",
        "پانی کائنات کے سب سے زیادہ حرارت جذب کرنے والے مادوں میں سے ہے۔ آلو کو گرم کرنے کے لیے لوہے کے مقابلے میں دس گنا زیادہ حرارت اور وقت درکار ہوتا ہے۔"
    ),
    (
        "Why does an antique oil painting develop fine web-like networks of microscopic cracks (craquelure) across its surface over decades?",
        ["The underlying wooden or canvas substrate expands and contracts with humidity while brittle aged oil paint layers cannot stretch", "Termites eat the paint binder", "Air oxidizes canvas into dust", "Sunlight dissolves lead white pigment"],
        "The underlying wooden or canvas substrate expands and contracts with humidity while brittle aged oil paint layers cannot stretch",
        "Differential thermal and hygroscopic expansion between the flexible canvas/wood panel and brittle, polymerized dried paint causes tensile fracture.",
        "پرانی آئل پینٹنگز کی سطح پر وقت گزرنے کے ساتھ مکڑی کے جالے جیسی باریک دراڑیں (Craquelure) کیوں پڑ جاتی ہیں؟",
        ["کینوس یا لکڑی نمی اور درجہ حرارت سے پھیلتی اور سکڑتی ہے جبکہ پینٹ کی سخت تہہ لچکدار نہ ہونے کی وجہ سے چٹخ جاتی ہے", "دیمک پینٹ کو کھا جاتی ہے", "ہوا کینوس کو راکھ بنا دیتی ہے", "دھوپ رنگوں کو پگھلا دیتی ہے"],
        "کینوس یا لکڑی نمی اور درجہ حرارت سے پھیلتی اور سکڑتی ہے جبکہ پینٹ کی سخت تہہ لچکدار نہ ہونے کی وجہ سے چٹخ جاتی ہے",
        "پینٹنگ کا کینوس یا لکڑی کا فریم موسم کے ساتھ بار بار پھیلتا اور سکڑتا ہے۔ سوکھا ہوا پرانا رنگ شیشے کی طرح سخت ہوتا ہے جو کھنچاؤ برداشت نہ کر کے دراڑیں بنا لیتا ہے۔"
    ),
    (
        "Why does an ordinary automobile engine consume more fuel per mile when driven in freezing winter conditions than on a pleasant mild day?",
        ["Cold engine lubricants create higher viscous friction, cold air increases aerodynamic drag, and the engine takes longer to reach optimal operating temperature", "Winter gasoline has half the energy", "Cold spark plugs produce weak sparks", "Tires contract and shrink wheel radius"],
        "Cold engine lubricants create higher viscous friction, cold air increases aerodynamic drag, and the engine takes longer to reach optimal operating temperature",
        "Dense cold air increases aerodynamic resistance, thick engine and transmission oil increases drivetrain drag, and rich fuel-air mixtures run during warmup.",
        "سردیوں کے موسم میں گاڑی عام خوشگوار موسم کے مقابلے میں فی کلومیٹر زیادہ پیٹرول کیوں خرچ کرتی ہے؟",
        ["انجن اور گیئر کا آئل سردی میں گاڑھا ہو کر رگڑ بڑھاتا ہے اور سرد کثیف ہوا گاڑی کے چلنے میں زیادہ رکاوٹ ڈالتی ہے", "سردیوں کے پیٹرول میں طاقت کم ہوتی ہے", "پلگ کمزور چنگاری دیتے ہیں", "ٹائر سکڑ کر چھوٹے ہو جاتے ہیں"],
        "انجن اور گیئر کا آئل سردی میں گاڑھا ہو کر رگڑ بڑھاتا ہے اور سرد کثیف ہوا گاڑی کے چلنے میں زیادہ رکاوٹ ڈالتی ہے",
        "ٹھنڈا انجن صحیح درجہ حرارت پر پہنچنے کے لیے زیادہ پیٹرول جلاتا ہے، تیل گاڑھا ہونے سے پرزوں پر بوجھ بڑھتا ہے، اور کثیف ہوا کو چیرنے کے لیے زیادہ طاقت لگتی ہے۔"
    ),
    (
        "Why do birds perched on tree branches sleep soundly all night without accidentally loosening their grip and falling off?",
        ["Their flexor tendons mechanically lock their talons around the branch automatically under the bird's own relaxed body weight", "They glue their claws to the bark", "Birds do not sleep deeply", "Their feet freeze to the wood"],
        "Their flexor tendons mechanically lock their talons around the branch automatically under the bird's own relaxed body weight",
        "The automatic digital flexor mechanism routes tendons behind the ankle joint; bending the legs pulls the talons tightly closed without conscious muscle effort.",
        "درخت کی شاخ پر بیٹھے پرندے گہری نیند میں سوئے رہنے کے باوجود شاخ سے پھسل کر نیچے کیوں نہیں گرتے؟",
        ["پرندے کے جسم کا وزن خود بخود اس کے پنجوں کے پٹھوں (Flexor tendons) کو تالے کی طرح شاخ کے گرد جکڑ دیتا ہے", "وہ پنجوں کو گوند سے چپکا لیتے ہیں", "پرندے گہری نیند نہیں سوتے", "پنجے لکڑی کے ساتھ جم جاتے ہیں"],
        "پرندے کے جسم کا وزن خود بخود اس کے پنجوں کے پٹھوں (Flexor tendons) کو تالے کی طرح شاخ کے گرد جکڑ دیتا ہے",
        "پرندے کی ٹانگ کی بناوٹ ایسی ہے کہ جب وہ بیٹھتا ہے تو ٹانگ مڑنے سے پنجوں کی رگیں خود بخود کھنچ کر شاخ کو گرفت میں لے لیتی ہیں، جس کے لیے بیدار رہنے کی ضرورت نہیں ہوتی۔"
    ),
    (
        "Why does a person using an ordinary glass thermometer need to vigorously flick their wrist downward before taking a new temperature reading?",
        ["To force the separated mercury or alcohol thread back down through the narrow constriction into the bulb reservoir", "To reset the electronic sensor", "To cool the glass below room temperature", "To remove air bubbles from the stem"],
        "To force the separated mercury or alcohol thread back down through the narrow constriction into the bulb reservoir",
        "Clinical maximum thermometers have a capillary constriction that traps the expanding liquid at peak reading until centrifugal wrist acceleration resets it.",
        "پرانے پارہ والے تھرمامیٹر سے نیا بخار چیک کرنے سے پہلے اسے جھٹکے کے ساتھ زور سے نیچے کیوں ہلایا جاتا ہے؟",
        ["تاکہ اوپر چڑھا ہوا پارہ تنگ نالی (Constriction) سے گزر کر واپس نیچے کے ذخیرے (Bulb) میں آ جائے", "الیکٹرانک سینسر کو ری سیٹ کرنے کے لیے", "شیشے کو کمرے سے ٹھنڈا کرنے کے لیے", "ہوا کے بلبلے صاف کرنے کے لیے"],
        "تاکہ اوپر چڑھا ہوا پارہ تنگ نالی (Constriction) سے گزر کر واپس نیچے کے ذخیرے (Bulb) میں آ جائے",
        "تھرمامیٹر میں ایک باریک موڑ ہوتا ہے جو مریض کے منہ سے نکالنے پر پارے کو خود بخود نیچے گرنے سے روکتا ہے۔ جھٹکا دینے سے مرکز گریز قوت پارے کو واپس نیچے دھکیلتی ہے۔"
    ),
    (
        "Why does an ocean cargo vessel consume substantially less fuel when cruising through deep open waters compared to cruising at identical speed through shallow canals?",
        ["In shallow waters, displaced water cannot escape easily beneath the hull, creating squat, bottom drag, and severe hydrodynamic resistance", "Canal water is fresher and heavier", "Canal walls absorb propeller thrust", "Shallow water has higher gravity"],
        "In shallow waters, displaced water cannot escape easily beneath the hull, creating squat, bottom drag, and severe hydrodynamic resistance",
        "The shallow water effect restricts return flow around the hull, accelerating water velocity beneath the keel and inducing dramatic hydrodynamic drag.",
        "بحری جہاز کھلے گہرے سمندر کے مقابلے میں اتلی نہروں (جیسے نہر سویز) میں وہی رفتار برقرار رکھنے کے لیے بہت زیادہ ایندھن کیوں کھاتا ہے؟",
        ["اتلے پانی میں جہاز کے نیچے سے پانی آسانی سے نکل نہیں پاتا جس سے سکشن بنتی ہے اور جہاز نیچے بیٹھ کر بھاری ہو جاتا ہے (Squat effect)", "نہر کا پانی بھاری ہوتا ہے", "نہر کی دیواریں انجن کی طاقت روکتی ہیں", "اتلے پانی میں کشش ثقل بڑھتی ہے"],
        "اتلے پانی میں جہاز کے نیچے سے پانی آسانی سے نکل نہیں پاتا جس سے سکشن بنتی ہے اور جہاز نیچے بیٹھ کر بھاری ہو جاتا ہے (Squat effect)",
        "کھلے سمندر میں پانی ہر طرف پھیل جاتا ہے، مگر تنگ اور کم گہری نہر میں جہاز اور پیندے کے درمیان پانی کی تیز لہر دباؤ گرا دیتی ہے جو جہاز کو نیچے کھینچتی ہے۔"
    ),
    (
        "Why does an arch bridge keystone remain firmly in place without mortar or glue, even when heavy traffic rolls directly across it?",
        ["Tapered wedge geometry converts vertical downward weight into lateral compressive forces against neighboring voussoirs", "Magnetic forces in masonry", "Friction with the road asphalt", "The keystone is pinned with hidden steel bolts"],
        "Tapered wedge geometry converts vertical downward weight into lateral compressive forces against neighboring voussoirs",
        "The wedge-shaped trapezoid cannot drop through without pushing adjacent stones outward; the abutments hold the arch in rigid static equilibrium.",
        "محرابی پل کا درمیانی کلس پتھر (Keystone) بغیر کسی سیمنٹ یا گوند کے صدیوں تک بھاری ٹریفک کے باوجود نیچے کیوں نہیں گرتا؟",
        ["اس کی پچانی (Wedge) شکل اوپر کے وزن کو دائیں بائیں کے پتھروں پر زبردست دباؤ میں بدل دیتی ہے جو اسے پھنسائے رکھتی ہے", "پتھروں میں قدرتی مقناطیس ہوتا ہے", "سڑک کی تارکول کی رگڑ", "اندر چھپے لوہے کے نٹ بولٹ"],
        "اس کی پچانی (Wedge) شکل اوپر کے وزن کو دائیں بائیں کے پتھروں پر زبردست دباؤ میں بدل دیتی ہے جو اسے پھنسائے رکھتی ہے",
        "درمیانی پتھر اوپر سے چوڑا اور نیچے سے پتلا ہوتا ہے۔ جتنا وزن اوپر سے پڑے گا وہ اتنی ہی سختی سے دائیں بائیں کے پتھروں میں پھنس جائے گا، نیچے گر نہیں سکتا۔"
    ),
    (
        "Why does a person feeling car sickness suffer far less when driving the automobile themselves rather than sitting as a passenger?",
        ["The driver anticipates and initiates every acceleration and turn, allowing the motor cortex to send feed-forward predictive signals to sensory systems", "Drivers breathe cleaner air", "Steering wheels discharge static electricity", "Driving elevates body adrenaline to maximum"],
        "The driver anticipates and initiates every acceleration and turn, allowing the motor cortex to send feed-forward predictive signals to sensory systems",
        "Active motor control generates efference copies in the vestibular nuclei, neutralizing mismatch between expected and experienced vestibular forces.",
        "گاڑی چلاتے وقت انسان کو خود کبھی سفر کی متلی (Motion sickness) کیوں نہیں ہوتی جبکہ مسافر کے طور پر بیٹھنے پر متلی ہو جاتی ہے؟",
        ["ڈرائیور ہر موڑ اور بریک خود لگاتا ہے اس لیے اس کا دماغ جسمانی حرکت کا پہلے سے اندازہ لگا کر توازن قائم رکھتا ہے", "ڈرائیور کو تازہ ہوا ملتی ہے", "اسٹیرنگ بجلی کو خارج کرتا ہے", "ڈرائیونگ سے خوف ختم ہو جاتا ہے"],
        "ڈرائیور ہر موڑ اور بریک خود لگاتا ہے اس لیے اس کا دماغ جسمانی حرکت کا پہلے سے اندازہ لگا کر توازن قائم رکھتا ہے",
        "جب انسان خود گاڑی موڑتا ہے تو دماغ کے پٹھے اور کان کے سگنلز پہلے سے ہم آہنگ ہوتے ہیں۔ مسافر پر غیر متوقع قوتیں لگتی ہیں جو متلی بناتی ہیں۔"
    ),
    (
        "Why does an acoustic guitar sound significantly different when plucked near the bridge compared to plucking over the soundhole?",
        ["Plucking near the rigid bridge excites high-frequency harmonic modes (treble), while center plucking excites warm fundamental frequencies", "The strings are thicker near the bridge", "Fingers warm the strings at the bridge", "Bridge plucking uses magnetic pickup only"],
        "Plucking near the rigid bridge excites high-frequency harmonic modes (treble), while center plucking excites warm fundamental frequencies",
        "Initial string displacement geometry determines Fourier harmonic coefficients; boundary proximity favors short wavelengths (bright, tinny timbre).",
        "گٹار کی تار کو لکڑی کے نچلے پل (Bridge) کے قریب چھیڑنے سے تیز باریک آواز نکلتی ہے جبکہ درمیان میں چھیڑنے سے گہری اور بھاری آواز کیوں نکلتی ہے؟",
        ["پل کے قریب چھیڑنے سے باریک ہارمونکس (Overtones) پیدا ہوتے ہیں جبکہ درمیان میں بنیادی سر (Fundamental) نمایاں ہوتا ہے", "پل کے قریب تار موٹی ہوتی ہے", "انگلیاں تار کو پل پر گرم کرتی ہیں", "پل پر مقناطیسی اثر ہوتا ہے"],
        "پل کے قریب چھیڑنے سے باریک ہارمونکس (Overtones) پیدا ہوتے ہیں جبکہ درمیان میں بنیادی سر (Fundamental) نمایاں ہوتا ہے",
        "تار کے سرے کے قریب لچک کم ہوتی ہے جہاں تیز اور باریک لہریں ابھرتی ہیں، جبکہ درمیان میں تار کھل کر جھولتی ہے جس سے بھاری اور میٹھے سر نکلتے ہیں۔"
    ),
    (
        "Why does a piece of dry chalk squeak with a piercing screech when dragged at a steep angle across a clean blackboard?",
        ["The stick-slip phenomenon causes the chalk to oscillate rapidly between sticking and snapping forward at high acoustic frequency", "The blackboard contains trapped sound waves", "Friction creates electrical sparks", "Chalk powder expands explosively"],
        "The stick-slip phenomenon causes the chalk to oscillate rapidly between sticking and snapping forward at high acoustic frequency",
        "Dynamic friction instability causes periodic microscopic buckling and slipping of the chalk tip, exciting bending resonant modes in the chalk body.",
        "بلیک بورڈ پر چاک کو خاص زاویے سے رگڑنے پر کان کے پردے پھاڑ دینے والی چبھتی ہوئی چیخ (Squeak) کیوں پیدا ہوتی ہے؟",
        ["چاک کا کنارہ بورڈ پر بار بار پھنسنے اور چھوٹنے (Stick-slip) کے تیز چکر سے گزرتا ہے جو اونچی فریکوئنسی کا ارتعاش بناتا ہے", "بورڈ کے اندر گونج قید ہوتی ہے", "رگڑ سے برقی چنگاریاں نکلتی ہیں", "چاک کا پاؤڈر دھماکہ کرتا ہے"],
        "چاک کا کنارہ بورڈ پر بار بار پھنسنے اور چھوٹنے (Stick-slip) کے تیز چکر سے گزرتا ہے جو اونچی فریکوئنسی کا ارتعاش بناتا ہے",
        "جب چاک پھسلنے کی بجائے کھردری سطح پر بار بار مڑتا اور جھٹکے سے چھوٹتا ہے، تو یہ تیز ترین ارتعاش سیکنڈ میں ہزاروں بار ہو کر چبھتی ہوئی چیخ بناتا ہے۔"
    ),
    (
        "Why does an old pendulum clock gain time and run fast when carried to the summit of a high mountain?",
        ["Actually, it runs slower at high mountain altitude because gravitational acceleration g decreases with distance from Earth's center (T = 2*pi*sqrt(L/g))", "It runs fast because air is thinner", "Cold mountain air shrinks the gears", "Atmospheric pressure pulls the pendulum"],
        "Actually, it runs slower at high mountain altitude because gravitational acceleration g decreases with distance from Earth's center (T = 2*pi*sqrt(L/g))",
        "Gravitational pull g weakens with altitude; because period T is inversely proportional to sqrt(g), the period lengthens, slowing the clock down.",
        "پہاڑ کی اونچی چوٹی پر لے جانے پر پرانے پینڈولم والی گھڑی پر کیا اثر پڑتا ہے؟",
        ["وہ سست ہو جاتی ہے اور پیچھے رہ جاتی ہے کیونکہ زمین کے مرکز سے دوری کی وجہ سے کشش ثقل (g) کمزور ہو جاتی ہے", "وہ ہوا پتلی ہونے کی وجہ سے تیز چلتی ہے", "سرد ہوا سے گیئرز سکڑ جاتے ہیں", "ہوا کا دباؤ پینڈولم کو کھینچتا ہے"],
        "وہ سست ہو جاتی ہے اور پیچھے رہ جاتی ہے کیونکہ زمین کے مرکز سے دوری کی وجہ سے کشش ثقل (g) کمزور ہو جاتی ہے",
        "پینڈولم کے جھولنے کا دارومدار زمین کی کشش ثقل پر ہے۔ چوٹی پر کشش کمزور ہونے سے پینڈولم آہستہ جھولتا ہے جس سے گھڑی روزانہ سست ہو جاتی ہے۔"
    ),
    (
        "Why does a modern skyscraper feature high-speed elevators equipped with aerodynamic nose cones on their cab roofs?",
        ["To reduce aerodynamic piston drag and air buffeting inside narrow vertical elevator shafts at speeds up to 45 mph", "To prevent falling debris from denting the cab", "To improve Wi-Fi signal reception", "To cool the elevator cables"],
        "To reduce aerodynamic piston drag and air buffeting inside narrow vertical elevator shafts at speeds up to 45 mph",
        "A cab moving rapidly in an enclosed shaft acts like a loose syringe plunger; fairings streamline displaced air, minimizing noise and power drain.",
        "بلند ترین عمارتوں کی انتہائی تیز رفتار لفٹوں کی چھت پر نوکیلے ائیروڈائنامک کون (Nose cone) کیوں لگائے جاتے ہیں؟",
        ["تنگ شافٹ کے اندر ہوا کے پسٹن نما دباؤ اور شور کو کم کرنے کے لیے جب لفٹ 40 میل فی گھنٹہ کی رفتار سے دوڑتی ہے", "اوپر سے گرتا ملبہ روکنے کے لیے", "وائی فائی سگنل تیز کرنے کے لیے", "لفٹ کی تاروں کو ٹھنڈا کرنے کے لیے"],
        "تنگ شافٹ کے اندر ہوا کے پسٹن نما دباؤ اور شور کو کم کرنے کے لیے جب لفٹ 40 میل فی گھنٹہ کی رفتار سے دوڑتی ہے",
        "تنگ عمودی سرنگ میں تیز رفتار لفٹ ہوا کے لیے پسٹن کا کام کرتی ہے۔ نوکیلا ڈیزائن ہوا کو آسانی سے سائیڈ سے گزار کر جھٹکوں اور شور کو ختم کرتا ہے۔"
    ),
    (
        "Why does an ocean tsunami travel across deep open ocean at the astonishing speed of a jet airliner (500 mph) with barely any visible wave height?",
        ["Tsunamis are shallow-water waves relative to their immense wavelength (hundreds of miles), where wave velocity equals sqrt(g * depth)", "Ocean winds push them at supersonic speeds", "Underwater volcanic heat boils water forward", "Earthquakes tilt the ocean basin"],
        "Tsunamis are shallow-water waves relative to their immense wavelength (hundreds of miles), where wave velocity equals sqrt(g * depth)",
        "Because wavelength spans up to 200 km, ocean depth (4 km) is fractionally shallow. Wave speed v = sqrt(9.8 * 4000) ~ 200 m/s (~720 km/h).",
        "کھلے سمندر میں سونامی کی لہر ہوائی جہاز جتنی تیز رفتار (800 کلومیٹر فی گھنٹہ) سے دوڑتی ہے مگر اس کی اونچائی بمشکل ایک میٹر ہوتی ہے، کیوں؟",
        ["سونامی کا طول موج (Wavelength) سینکڑوں کلومیٹر طویل ہوتا ہے جس کی گہرے سمندر میں رفتار پانی کی گہرائی کے کلیے (sqrt(g*d)) پر چلتی ہے", "طوفانی ہوائیں اسے تیز چلاتی ہیں", "پانی کے نیچے لاوا اسے دھکیلتا ہے", "زلزلہ سمندر کو ٹیڑھا کر دیتا ہے"],
        "سونامی کا طول موج (Wavelength) سینکڑوں کلومیٹر طویل ہوتا ہے جس کی گہرے سمندر میں رفتار پانی کی گہرائی کے کلیے (sqrt(g*d)) پر چلتی ہے",
        "سونامی صرف سطح کی لہر نہیں بلکہ سمندر کے پیندے سے لے کر اوپر تک پورے پانی کی حرکت ہوتی ہے۔ اتنی زیادہ توانائی گہرے سمندر میں جہاز کی رفتار سے سفر کرتی ہے۔"
    ),
    (
        "Why does an ordinary automobile exhaust pipe drip liquid water droplets on a chilly morning right after starting the cold engine?",
        ["Combustion of hydrocarbon fuel naturally produces water vapor (H2O) and carbon dioxide, which condenses on cold metal exhaust walls", "The radiator leaks into the exhaust", "Gasoline is mixed with tap water", "The catalytic converter creates rain"],
        "Combustion of hydrocarbon fuel naturally produces water vapor (H2O) and carbon dioxide, which condenses on cold metal exhaust walls",
        "Complete combustion reaction: C_n H_2n+2 + O2 -> CO2 + H2O. When the exhaust pipe is cold, hot exhaust moisture condenses into liquid drops.",
        "سردیوں کی صبح گاڑی اسٹارٹ کرتے ہی سائلنسر (Exhaust pipe) سے پانی کے قطرے کیوں ٹپکنے لگتے ہیں؟",
        ["پیٹرول کے جلنے سے کیمیائی طور پر بھاپ اور کاربن ڈائی آکسائیڈ بنتی ہے، جو ٹھنڈے سائلنسر سے ٹکرا کر مائع پانی بن جاتی ہے", "ریڈی ایٹر کا پانی سائلنسر میں بہتا ہے", "پیٹرول میں پانی ملایا گیا تھا", "کنورٹر بارش پیدا کرتا ہے"],
        "پیٹرول کے جلنے سے کیمیائی طور پر بھاپ اور کاربن ڈائی آکسائیڈ بنتی ہے، جو ٹھنڈے سائلنسر سے ٹکرا کر مائع پانی بن جاتی ہے",
        "ہائیڈرو کاربن ایندھن جب آکسیجن کے ساتھ جلتا ہے تو خالص پانی کی بھاپ خارج ہوتی ہے۔ ٹھنڈی پائپ سے گزرتے ہی یہ بھاپ قطروں میں تبدیل ہو کر بہتی ہے۔"
    ),
    (
        "Why does a diver in deep ocean waters see everything bathed in deep blue and turquoise hues, with vivid red completely absent?",
        ["Water molecules absorb long wavelengths of light (red, orange, yellow) within the first 10-15 meters of depth", "Underwater goggles filter out red light", "Fish consume red light photons", "Deep ocean water produces blue luminescence"],
        "Water molecules absorb long wavelengths of light (red, orange, yellow) within the first 10-15 meters of depth",
        "Differential absorption of electromagnetic spectrum by liquid water attenuates red wavelengths rapidly; only high-energy blue penetrates deep.",
        "سمندر کی گہرائی میں غوطہ لگانے والے کو ہر چیز نیلی اور فیروزی کیوں نظر آتی ہے جبکہ سرخ رنگ مکمل طور پر غائب ہو جاتا ہے؟",
        ["پانی کے مالیکیولز روشنی کے سرخ اور پیلے رنگوں کو پہلے 10 سے 15 میٹر میں ہی جذب کر کے ختم کر دیتے ہیں", "غوطہ خور کا چشمہ سرخ رنگ روکتا ہے", "مچھلیاں سرخ روشنی کھا جاتی ہیں", "گہرا پانی نیلی روشنی خارج کرتا ہے"],
        "پانی کے مالیکیولز روشنی کے سرخ اور پیلے رنگوں کو پہلے 10 سے 15 میٹر میں ہی جذب کر کے ختم کر دیتے ہیں",
        "روشنی کے رنگوں میں سرخ رنگ کی توانائی سب سے کم ہوتی ہے جو پانی میں داخل ہوتے ہی جذب ہو جاتی ہے۔ صرف نیلی اور سبز لہریں گہرائی تک پہنچ پاتی ہیں۔"
    ),
    (
        "Why does a sharp knife slice soft, squishy bread cleanly when moved back and forth with a sawing motion, but squashes it flat when pressed straight down?",
        ["Sawing motion applies high localized shear stress along microscopic serrations without requiring large normal crushing compressive forces", "Sawing heats the bread crust to melting", "Pressing down generates vacuum pressure", "Bread dough repels moving metal"],
        "Sawing motion applies high localized shear stress along microscopic serrations without requiring large normal crushing compressive forces",
        "A lateral draw stroke engages microscopic teeth like a saw, tearing cellulose fibers sequentially instead of compressing the bulk elastic foam matrix.",
        "نرم ڈبل روٹی پر چھری کو سیدھا نیچے دبانے سے وہ چپٹی اور کچلی جاتی ہے، مگر آگے پیچھے آری کی طرح چلانے سے صاف کیوں کٹ جاتی ہے؟",
        ["آگے پیچھے چلانے سے چھری کے باریک دندانے ریشوں کو کچلنے کی بجائے کاٹ دیتے ہیں بغیر کسی نیچے کے دباؤ کے (Shear stress)", "آری چلانے سے ڈبل روٹی پگھلتی ہے", "نیچے دبانے سے ویکیوم بنتا ہے", "آٹا حرکت کرتی دھات سے دور بھاگتا ہے"],
        "آگے پیچھے چلانے سے چھری کے باریک دندانے ریشوں کو کچلنے کی بجائے کاٹ دیتے ہیں بغیر کسی نیچے کے دباؤ کے (Shear stress)",
        "سیدھا نیچے دبانے پر سارا وزن فوم جیسے نرم ڈھانچے کو دبا دیتا ہے، جبکہ آگے پیچھے چلانے سے دھار کے دندانے بغیر دباؤ ڈالے روٹی کے ریشے کاٹتے چلے جاتے ہیں۔"
    ),
    (
        "Why does a person who has stepped on a bathroom scale see the weight needle jump higher for a split second when they quickly squat down?",
        ["When decelerating the downward squat or exploding upward, the scale must apply an upward force greater than gravity", "Squatting compresses Earth's crust", "Muscles gain mass during contraction", "Air pressure drops in squats"],
        "When decelerating the downward squat or exploding upward, the scale must apply an upward force greater than gravity",
        "Dynamic acceleration modifies normal force. Rapidly stopping the squat or driving upward requires upward acceleration 'a', causing the scale reading to spike.",
        "وزن ناپنے والی مشین پر کھڑا انسان جب اچانک نیچے جھک کر بیٹھنے لگتا ہے تو رکتے وقت یا اوپر اٹھتے وقت سوئی اچانک وزن سے زیادہ کیوں دکھاتی ہے؟",
        ["جسم کی حرکت کو روکنے یا اوپر اٹھانے کے لیے مشین کو کشش ثقل سے اضافی قوت لگانی پڑتی ہے (N = m(g + a))", "جھکنے سے زمین دب جاتی ہے", "پٹھے سکڑنے سے وزنی ہو جاتے ہیں", "جھکنے سے ہوا کا دباؤ گر جاتا ہے"],
        "جسم کی حرکت کو روکنے یا اوپر اٹھانے کے لیے مشین کو کشش ثقل سے اضافی قوت لگانی پڑتی ہے (N = m(g + a))",
        "مشین صرف وزن نہیں ناپتی بلکہ پیروں کا دباؤ ناپتی ہے۔ جب انسان خود کو نیچے گرنے سے روکتا ہے تو ایکسلریشن کے خلاف لگنے والا اضافی زور سوئی کو اوپر چڑھا دیتا ہے۔"
    )
]

print(f"Normal Batch B1 loaded: {len(ITEMS)} items.")
