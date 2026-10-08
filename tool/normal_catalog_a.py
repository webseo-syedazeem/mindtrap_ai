# -*- coding: utf-8 -*-
"""
Normal Catalog A (Items 251 to 350: 100 items)
Detective investigations, forensics, classic lateral thinking, and deduction enigmas.
Each item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    # 251: Three light switches
    (
        "Three light switches outside a closed basement control three incandescent bulbs inside. You can only enter the basement once. How do you identify which switch controls which bulb?",
        ["Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3", "Turn all three on", "Flip switch 1 repeatedly", "Look under the door"],
        "Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3",
        "Incandescent bulbs emit thermal heat; feeling the unlit warm bulb identifies the first switch.",
        "بند تہہ خانے کے باہر تین سوئچ اندر کے تین بلب کنٹرول کرتے ہیں۔ آپ صرف ایک بار اندر جا سکتے ہیں۔ کس سوئچ سے کون سا بلب جلتا ہے کیسے معلوم کریں گے؟",
        ["پہلا سوئچ 10 منٹ آن رکھ کر بند کریں، دوسرا آن کریں اور اندر جائیں: جلتا بلب 2، گرم بلب 1، ٹھنڈا بلب 3 ہے", "تینوں سوئچ آن کر کے", "سوئچ تیزی سے بند کر کے", "دروازے کے نیچے سے دیکھ کر"],
        "پہلا سوئچ 10 منٹ آن رکھ کر بند کریں، دوسرا آن کریں اور اندر جائیں: جلتا بلب 2، گرم بلب 1، ٹھنڈا بلب 3 ہے",
        "پہلا بلب جلنے کی وجہ سے گرم ہو چکا ہوگا جبکہ دوسرا بلب اس وقت جل رہا ہوگا۔"
    ),
    # 252: Water jugs 3 and 5 gallons
    (
        "With an unmarked 3-gallon jug and an unmarked 5-gallon jug at an endless water fountain, how can you measure out exactly 4 gallons?",
        ["Fill 5-gallon, pour into 3-gallon leaving 2; empty 3-gallon, transfer 2 into 3-gallon; fill 5-gallon, top off 3-gallon leaving 4 in 5-gallon", "Fill both jugs halfway", "Guess the midpoint", "Weigh them on a scale"],
        "Fill 5-gallon, pour into 3-gallon leaving 2; empty 3-gallon, transfer 2 into 3-gallon; fill 5-gallon, top off 3-gallon leaving 4 in 5-gallon",
        "Pouring 1 gallon from a full 5-gallon jug into the 3-gallon jug containing 2 gallons leaves exactly 4 gallons.",
        "ایک 3 لیٹر اور ایک 5 لیٹر کا خالی برتن لے کر نہر سے ٹھیک 4 لیٹر پانی کیسے ناپیں گے؟",
        ["5 لیٹر والے سے 3 لیٹر بھر کر باقی 2 لیٹر بچائیں، اسے خالی 3 والے میں ڈالیں، پھر 5 والا بھر کر 3 والے میں 1 لیٹر ڈالیں تو 4 لیٹر بچے گا", "دونوں کو آدھا بھر کر", "اندازے سے ناپ کر", "ترازو پر تول کر"],
        "5 لیٹر والے سے 3 لیٹر بھر کر باقی 2 لیٹر بچائیں، اسے خالی 3 والے میں ڈالیں، پھر 5 والا بھر کر 3 والے میں 1 لیٹر ڈالیں تو 4 لیٹر بچے گا",
        "اس کلاسیکی حسابی طریقے سے 5 لیٹر کے برتن میں بالکل درست 4 لیٹر پانی بچ جاتا ہے۔"
    ),
    # 253: Two hourglasses 7 and 4 minutes
    (
        "You have a 7-minute sand hourglass and a 4-minute sand hourglass. How do you time exactly 9 minutes to cook a delicacy?",
        ["Start both; when 4-min ends, invert it; when 7-min ends (1 min left in 4-min), invert 7-min; when 4-min ends (8 min), invert 7-min to reach 9", "Run 7-minute twice", "Guess the middle of 7-min", "Run 4-minute twice"],
        "Start both; when 4-min ends, invert it; when 7-min ends (1 min left in 4-min), invert 7-min; when 4-min ends (8 min), invert 7-min to reach 9",
        "Staggering sand flow intervals isolates single-minute increments to total 9 minutes.",
        "آپ کے پاس ایک 7 منٹ اور ایک 4 منٹ والی ریت کی گھڑیاں ہیں۔ بالکل 9 منٹ کا وقت کیسے ناپیں گے؟",
        ["دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے", "7 منٹ والی دو بار چلا کر", "اندازہ لگا کر", "4 منٹ والی دو بار چلا کر"],
        "دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے",
        "دونوں ریت کی گھڑیوں کے فرق کو استعمال کر کے بالکل درست نو منٹ ناپے جا سکتے ہیں۔"
    ),
    # 254: 12 coins balance scale
    (
        "Among 12 gold coins, 1 is counterfeit with a slightly different weight (heavier or lighter). What is the minimum weighings on a balance scale to identify it?",
        ["Three weighings", "Four weighings", "Two weighings", "Six weighings"],
        "Three weighings",
        "Ternary decision trees allow 3^3 = 27 outcome branches, sufficient to identify 1 of 12 coins and determine if heavier or lighter.",
        "12 سونے کے سکوں میں سے ایک سکہ نقلی ہے جس کا وزن باقیوں سے مختلف ہے، دو پلڑوں والے ترازو پر کم از کم کتنی بار تول کر وہ سکہ تلاش کیا جا سکتا ہے؟",
        ["تین بار", "چار بار", "دو بار", "چھ بار"],
        "تین بار",
        "تین بار تولنے سے کل 27 ممکنہ نتائج نکلتے ہیں جو 12 سکوں میں سے نقلی سکہ پہچاننے کے لیے کافی ہیں۔"
    ),
    # 255: 9 balls balance scale
    (
        "You have 9 identical-looking billiard balls, 1 of which is slightly heavier. What is the minimum weighings on a balance scale to find it?",
        ["Two weighings", "Three weighings", "Four weighings", "One weighing"],
        "Two weighings",
        "Weigh 3 against 3: if balanced, the heavy ball is in remaining 3; then weigh 1 against 1 from the heavy trio.",
        "9 ایک جیسی گیندوں میں سے ایک گیند وزنی ہے۔ ترازو کے دو پلڑوں سے کم سے کم کتنی بار تول کر وزنی گیند کا پتہ لگایا جا سکتا ہے؟",
        ["صرف دو بار", "تین بار", "چار بار", "ایک بار"],
        "صرف دو بار",
        "پہلے 3 اور 3 تولیں، جس سے وزنی گروپ کا پتہ چلے گا، پھر اس گروپ کی 1 اور 1 تولنے سے وزنی گیند مل جائے گی۔"
    ),
    # 256: Bridge torch crossing
    (
        "Four travelers need to cross a narrow rope bridge at night with 1 torch that burns for 17 minutes. Speeds are 1, 2, 5, and 10 minutes. At most 2 can cross together. How do all four cross in 17 minutes?",
        ["1 and 2 cross (2 min), 1 returns (3 min), 5 and 10 cross (13 min), 2 returns (15 min), 1 and 2 cross (17 min)", "1 escorts each person across one by one", "Fastest runs across carrying the others", "They cross without the torch"],
        "1 and 2 cross (2 min), 1 returns (3 min), 5 and 10 cross (13 min), 2 returns (15 min), 1 and 2 cross (17 min)",
        "Pairing the two slowest travelers (5 and 10) together avoids wasting fast trips returning the torch.",
        "رات کے اندھیرے میں چار مسافروں کو ایک مشعل کے ساتھ پل پار کرنا ہے جس کے جلنے کا وقت 17 منٹ ہے۔ ان کی رفتار 1، 2، 5 اور 10 منٹ ہے۔ وہ 17 منٹ میں کیسے پار کریں گے؟",
        ["1 اور 2 جائیں (2 منٹ)، 1 مشعل لائے (3)، پھر 5 اور 10 جائیں (13)، 2 مشعل لائے (15)، پھر 1 اور 2 جائیں (17 منٹ)", "1 سب کو باری باری لے جائے", "سب بغیر مشعل کے دوڑیں", "سب سے تیز والا باقیوں کو اٹھا لے"],
        "1 اور 2 جائیں (2 منٹ)، 1 مشعل لائے (3)، پھر 5 اور 10 جائیں (13)، 2 مشعل لائے (15)، پھر 1 اور 2 جائیں (17 منٹ)",
        "دو سست ترین مسافروں (5 اور 10) کو ایک ساتھ بھیجنے سے مشعل واپس لانے کا قیمتی وقت بچ جاتا ہے۔"
    ),
    # 257: Two doors guards
    (
        "Two doors lead to freedom and execution. One guard always tells the truth, and the other always lies. What single question asked to one guard reveals the door to freedom?",
        ["Which door would the other guard say leads to freedom?", "Which door is freedom?", "Are you lying?", "Do you guard the good door?"],
        "Which door would the other guard say leads to freedom?",
        "Both guards will inevitably point to the door of execution, so you choose the opposite door.",
        "دو دروازوں میں سے ایک آزادی اور دوسرا قید کا ہے۔ دو پہریداروں میں سے ایک ہمیشہ سچ بولتا ہے اور دوسرا ہمیشہ جھوٹ۔ ایک ہی سوال سے آزادی کا راستہ کیسے معلوم ہوگا؟",
        ["اگر میں دوسرے پہریدار سے پوچھوں تو وہ آزادی کا دروازہ کون سا بتائے گا؟", "آزادی کا دروازہ کون سا ہے؟", "کیا تم سچ بول رہے ہو؟", "تم کون ہو؟"],
        "اگر میں دوسرے پہریدار سے پوچھوں تو وہ آزادی کا دروازہ کون سا بتائے گا؟",
        "سچ اور جھوٹ مل کر ہمیشہ جھوٹا دروازہ بتائیں گے، اس لیے آپ بتائے گئے دروازے کے الٹ جائیں۔"
    ),
    # 258: 100 lockers puzzle
    (
        "In a school corridor with 100 closed lockers, 100 students pass through. Student 1 opens all. Student 2 closes every 2nd. Student 3 toggles every 3rd, up to student 100. Which lockers remain open?",
        ["Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "All prime numbered lockers", "All even numbered lockers", "All odd numbered lockers"],
        "Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
        "Only perfect squares have an odd number of factors; all other numbers have pairs of factors resulting in being closed.",
        "اسکول کی راہداری میں 100 بند لاکرز پر 100 طلبہ باری باری گزرتے ہیں۔ پہلا سب کھولتا ہے، دوسرا ہر دوسرا بند کرتا ہے، تیسرا ہر تیسرا بدلتا ہے۔ آخر میں کون سے لاکرز کھلے رہیں گے؟",
        ["صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "تمام طاق اعداد والے", "تمام جفت اعداد والے", "تمام پرائم اعداد والے"],
        "صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
        "صرف مکمل مربع اعداد کے فیکٹرز طاق تعداد میں ہوتے ہیں جس کی وجہ سے وہ کھلے رہ جاتے ہیں۔"
    ),
    # 259: Three mislabeled fruit boxes
    (
        "Three wooden crates are labeled Apples, Oranges, and Mixed (Apples & Oranges). All three labels are guaranteed incorrect. You can pick 1 fruit from 1 crate without looking inside. Which crate do you pick from to label all correctly?",
        ["Pick from the crate labeled Mixed", "Pick from the crate labeled Apples", "Pick from the crate labeled Oranges", "Cannot be solved with 1 pick"],
        "Pick from the crate labeled Mixed",
        "Since the Mixed label is wrong, picking 1 fruit identifies that entire box; the remaining two mislabeled boxes are deduced uniquely.",
        "تین پیٹیوں پر 'سیب'، 'مالٹے' اور 'مکس' کے لیبل لگے ہیں مگر تینوں لیبل غلط ہیں۔ آپ صرف ایک پیٹی میں سے بنا دیکھے ایک پھل نکال سکتے ہیں۔ تمام پیٹیاں درست کیسے کریں گے؟",
        ["جس پیٹی پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر", "سیب والی پیٹی سے", "مالٹے والی پیٹی سے", "ایک پھل سے ممکن نہیں"],
        "جس پیٹی پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر",
        "کیونکہ مکس کا لیبل غلط ہے، اس میں سے جو پھل نکلے گا وہ پوری پیٹی وہی ہوگی، اور باقی دو پیٹیاں خود بخود سیدھی ہو جائیں گی۔"
    ),
    # 260: Single-elimination tennis tournament
    (
        "In an international tennis tournament featuring 64 players under single-elimination rules, how many total matches must be played to crown the champion?",
        ["63 matches", "64 matches", "32 matches", "128 matches"],
        "63 matches",
        "Each match eliminates exactly one loser; to eliminate 63 players requires exactly 63 matches.",
        "ایک بین الاقوامی ناک آؤٹ ٹینس ٹورنامنٹ میں 64 کھلاڑی حصہ لے رہے ہیں۔ چیمپیئن کا فیصلہ کرنے کے لیے کل کتنے میچ کھیلنا پڑیں گے؟",
        ["63 میچ", "64 میچ", "32 میچ", "128 میچ"],
        "63 میچ",
        "ہر میچ میں ایک کھلاڑی ہار کر باہر ہوتا ہے، 63 کھلاڑیوں کو باہر کرنے کے لیے ٹھیک 63 میچ درکار ہیں۔"
    ),
    # 261: Dinner party handshakes
    (
        "At an executive dinner party of 10 people, everyone shakes hands with everyone else exactly once. How many total handshakes occur across the evening?",
        ["45 handshakes", "90 handshakes", "50 handshakes", "100 handshakes"],
        "45 handshakes",
        "Combinations of 10 people taken 2 at a time: n*(n-1)/2 = 10 * 9 / 2 = 45.",
        "ایک پروقار عشائیے میں 10 لوگ موجود ہیں اور ہر شخص دوسرے ہر شخص سے ایک بار مصافحہ (ہاتھ ملاتا) کرتا ہے۔ کل کتنے مصافحے ہوں گے؟",
        ["45 مصافحے", "90 مصافحے", "50 مصافحے", "100 مصافحے"],
        "45 مصافحے",
        "مصافحوں کا فارمولا n*(n-1)/2 ہوتا ہے، یعنی 10 ضرب 9 تقسیم 2 برابر ہے 45۔"
    ),
    # 262: Monty Hall door switch
    (
        "On a television stage, you select Door 1 out of 3. The host opens Door 3, revealing a goat, and offers to switch to Door 2. What gives you the highest mathematical probability of winning the sports car?",
        ["Switching to Door 2 (2/3 chance of winning)", "Staying with Door 1 (2/3 chance)", "It is strictly 50/50, no difference", "Flipping a coin"],
        "Switching to Door 2 (2/3 chance of winning)",
        "Your initial pick had a 1/3 chance; the unopened remaining door inherits the entire 2/3 probability of the other two doors.",
        "ٹی وی شو میں تین میں سے ایک دروازے کے پیچھے اسپورٹس کار ہے۔ آپ نے دروازہ 1 چنا، میزبان نے دروازہ 3 کھولا جہاں بکری نکلی۔ کار جیتنے کا زیادہ امکان کس میں ہے؟",
        ["دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)", "دروازہ 1 پر ہی رہنے سے", "دونوں میں بالکل برابر 50/50 چانس ہے", "کوئی فرق نہیں پڑتا"],
        "دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)",
        "پہلے انتخاب کا امکان صرف 1/3 تھا، جبکہ دوسرے دروازے کے پاس اب 2/3 کا زبردست امکان موجود ہے۔"
    ),
    # 263: Elevator short man
    (
        "A gentleman lives on the 15th floor of an apartment. Every morning he rides the elevator all the way to ground. Returning home, he rides to the 10th floor and walks up 5 flights of stairs, unless it rains. Why?",
        ["He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days", "He likes exercising on dry days", "The elevator is broken above floor 10", "He visits a friend on floor 10"],
        "He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days",
        "The height of button 10 is the maximum reach of his arm; an umbrella gives him extra physical reach.",
        "ایک شخص اپارٹمنٹ کی پندرہویں منزل پر رہتا ہے۔ وہ صبح لفٹ سے نیچے جاتا ہے مگر واپسی پر دسویں منزل پر اتر کر پانچ منزلیں پیدل چڑھتا ہے، سوائے بارش کے دن کے۔ کیوں؟",
        ["کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے", "وہ ورزش کا شوقین ہے", "لفٹ اوپر خراب ہوتی ہے", "اس کا دوست دسویں منزل پر ہے"],
        "کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے",
        "چھوٹے قد کی وجہ سے وہ اوپر کا بٹن ہاتھ سے نہیں دبا پاتا تھا، چھتری کا دستہ اسے پہنچا دیتا تھا۔"
    ),
    # 264: Hotel Monopoly bankruptcy
    (
        "A man pushes his vehicle token up to a luxury red hotel and instantly realizes he is completely bankrupt. What was taking place?",
        ["Playing the board game Monopoly with a car token", "His real car engine blew up", "He lost his hotel reservation", "He was robbed by valets"],
        "Playing the board game Monopoly with a car token",
        "In Monopoly, landing a miniature car token on an opponent's hotel property incurs a ruinous rent fine.",
        "ایک شخص نے اپنی چھوٹی کار کو ہوٹل کے سامنے رکھا اور فورا سمجھ گیا کہ وہ کنگال ہو چکا ہے، وہ کیا کر رہا تھا؟",
        ["وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا", "اس کی اصل کار خراب ہو گئی تھی", "ہوٹل کا بل بہت زیادہ تھا", "اس کے پیسے چوری ہو گئے تھے"],
        "وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا",
        "مونوپولی کھیل میں کار کا مہرہ حریف کے ہوٹل پر پہنچنے کا مطلب دیوالیہ ہو جانا ہے۔"
    ),
    # 265: Poisoned iced tea drinkers
    (
        "Two travelers order chilled iced tea glasses at a desert diner. Mark gulps down five glasses quickly in two minutes; Dan sips one glass slowly over an hour. Dan dies of cyanide poisoning, but Mark survives unharmed. Why?",
        ["The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's", "Mark had developed immunity to poison", "Dan's straw was laced with poison", "Mark was given a different pitcher"],
        "The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's",
        "Drinking fast before the ice melted prevented Mark from ingesting the toxin released upon thawing.",
        "صحرائی ریستوران میں دو مسافروں نے ٹھنڈا شربت پیا۔ ایک نے جلدی جلدی 5 گلاس پی لیے جبکہ دوسرے نے ایک گھنٹے میں ایک گلاس آہستہ پیا۔ آہستہ پینے والا زہر سے مر گیا مگر دوسرا بچ گیا۔ کیوں؟",
        ["زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا", "پہلے دوست میں زہر کی قوت مدافعت تھی", "اسٹرا میں زہر لگا تھا", "دوسرے کا شربت الگ تھا"],
        "زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا",
        "جلدی پینے والے کے وقت برف پگھلی نہیں تھی، آہستہ پینے والے کی برف گھل کر زہر شربت میں شامل ہو گیا۔"
    ),
    # 266: Tape recorder suicide alibi
    (
        "A detective investigates an alleged suicide in a study. On the mahogany desk is a cassette tape recorder. Pressing play, police hear: 'I cannot bear this life anymore', followed by a gunshot. The detective immediately declares it a homicide. Why?",
        ["The cassette tape was rewound back to the beginning, which a dead person cannot do", "The gunshot sounded too loud", "The voice was synthesized", "The tape was blank"],
        "The cassette tape was rewound back to the beginning, which a dead person cannot do",
        "After shooting oneself, a deceased individual cannot press the rewind button on a mechanical cassette player.",
        "ایک کمرے میں خودکشی کی اطلاع پر پولیس پہنچی۔ میز پر ٹیپ ریکارڈر تھا، پلے کرنے پر گولی چلنے کی آواز آئی۔ تفتیشی افسر نے فورا اسے قتل قرار دیا۔ کیوں؟",
        ["کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا", "گولی کی آواز بہت دھیمی تھی", "کیسٹ پرانی تھی", "کمرہ بند تھا"],
        "کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا",
        "گولی لگنے کے بعد مرنے والا شخص خود کیسٹ کا بٹن دبا کر اسے واپس شروع پر نہیں لا سکتا۔"
    ),
    # 267: Window frost inside vs outside
    (
        "On a freezing winter dawn, a shopkeeper claims a burglar scratched the display glass from the outside to break in. The detective examines frost condensation on the inside pane and disproves the story. Why?",
        ["The scratches were etched on top of the frost layer, proving the scratch occurred from inside the shop", "Frost never forms on windows", "The window was double-glazed", "Burglars don't leave scratches"],
        "The scratches were etched on top of the frost layer, proving the scratch occurred from inside the shop",
        "Frost condenses on the indoor humid surface; fresh scratch marks disturbed the indoor frost layer.",
        "دکان دار نے دعویٰ کیا کہ چور نے رات کو باہر سے کھڑکی کا شیشہ کھرچ کر اندر گھسنے کی کوشش کی۔ انسپکٹر نے فراڈ کیسے پکڑا؟",
        ["کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا", "شیشہ مضبوط تھا", "چور کھرچتا نہیں ہے", "باہر دھوپ تھی"],
        "کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا",
        "کمرے کی اندرونی نمی شیشے پر جمی تھی، اور کھرچ کے نشان اس جمی ہوئی برف کے اوپر اندر کی طرف تھے۔"
    ),
    # 268: Wet umbrella in closet
    (
        "A suspect insists he was asleep in bed throughout an armed robbery during a sudden evening thunderstorm. The detective inspects the foyer wardrobe and promptly arrests him. What was the incriminating clue?",
        ["His dripping wet umbrella and damp wool coat hung inside the dark wardrobe", "His bed was unmade", "His clock was fast", "Mud on the ceiling"],
        "His dripping wet umbrella and damp wool coat hung inside the dark wardrobe",
        "Dripping rain gear proves the suspect was recently outdoors in the thunderstorm despite his alibi.",
        "ملزم نے قسم کھائی کہ طوفانی بارش اور واردات کے وقت وہ بستر میں گہری نیند سو رہا تھا۔ تفتیش کار نے الماری دیکھ کر اسے فوراً گرفتار کر لیا، الماری میں کیا ثبوت تھا؟",
        ["الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا", "الماری میں چوری کے نوٹ تھے", "الماری کھلی تھی", "کپڑے بکھرے تھے"],
        "الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا",
        "الماری میں گیلے کوٹ اور چھتری کی موجودگی نے ثابت کر دیا کہ وہ طوفان کے دوران باہر موجود تھا۔"
    ),
    # 269: Snow footprints direction
    (
        "A forest cabin shows solitary footprints in the fresh morning snow leading away into the woods, with zero tracks returning. Yet the solitary cabin occupant is resting inside by the fireplace. How did he return without leaving fresh tracks?",
        ["He walked backward stepping carefully into his own outgoing footprints", "He flew an airplane", "He wore snowshoes backwards", "He slid on a rope"],
        "He walked backward stepping carefully into his own outgoing footprints",
        "Stepping carefully backward into preexisting footprints obscures the arrival direction.",
        "جنگلی کیبن سے باہر کی طرف جاتے ہوئے تازہ برف میں پاؤں کے نشانات ہیں مگر واپسی کا کوئی نشان نہیں، پھر بھی شکاری اندر بیٹھا ہے۔ کیسے؟",
        ["وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا", "وہ ہوا میں اڑ کر آیا", "وہ رسی کے سہارے آیا", "برف پگھل گئی تھی"],
        "وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا",
        "اپنے ہی پرانے قدموں کے اوپر دوبارہ پاؤں رکھ کر چلنے سے واپسی کا کوئی نیا نشان نہیں بنتا۔"
    ),
    # 270: Left-handed suicide forgery
    (
        "A wealthy financier was discovered dead in his library with a revolver gripped in his right hand. The forensic pathologist immediately ruled out suicide. What physical finding gave it away?",
        ["The entrance gunshot wound was on his left temple, mechanically impossible for a right-handed self-inflicted shot", "The gun had fingerprints", "The tycoon was wearing a watch", "The room was warm"],
        "The entrance gunshot wound was on his left temple, mechanically impossible for a right-handed self-inflicted shot",
        "Shooting oneself in the opposite temple with an unnatural wrist angle points to staged execution.",
        "ایک رئیس کی لاش ملی جس کے دائیں ہاتھ میں ریوالور تھا مگر فارنزک ماہر نے فوری قتل کا فیصلہ سنایا۔ کیوں؟",
        ["کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا", "پستول نیا تھا", "تاجر امیر تھا", "کمرے کی کھڑکی کھلی تھی"],
        "کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا",
        "دائیں ہاتھ سے بائیں کنپٹی پر فائر کرنا انسانی جسمانی بناوٹ کے اعتبار سے ناممکن ہوتا ہے۔"
    ),
    # 271: Double pane bullet hole
    (
        "A sniper fires a single bullet through a double-pane glass window from the street outside. Which physical characteristic identifies that the shot originated from outside rather than inside?",
        ["The entrance hole on the outer pane is small and clean, while the inner pane displays wide cone-shaped cratering", "The glass melted", "The bullet stopped between panes", "Cracks formed only on inner pane"],
        "The entrance hole on the outer pane is small and clean, while the inner pane displays wide cone-shaped cratering",
        "High-velocity projectile impacts create expanding conchoidal fracture spalling on the exit side of brittle glass.",
        "کھڑکی کے دوہرے شیشے میں سے ایک گولی گزری۔ فارنزک ٹیم نے کیسے ثابت کیا کہ گولی باہر سڑک سے اندر کی طرف چلائی گئی تھی؟",
        ["باہر کے شیشے پر باریک صاف سوراخ تھا جبکہ اندرونی شیشے پر مخروطی چٹخنے کا بڑا گڑھا بنا تھا", "شیشہ پگھل گیا تھا", "گولی دونوں شیشوں کے بیچ رک گئی", "اندر کا شیشہ محفوظ تھا"],
        "باہر کے شیشے پر باریک صاف سوراخ تھا جبکہ اندرونی شیشے پر مخروطی چٹخنے کا بڑا گڑھا بنا تھا",
        "گولی جب شیشے سے ٹکراتی ہے تو داخلے کا سوراخ صاف ہوتا ہے اور نکلنے کی سمت شیشہ چٹخ کر چوڑا ہو جاتا ہے۔"
    ),
    # 272: Forged document ink drying
    (
        "An heir presents a handwritten will purportedly drafted thirty years ago with an ordinary blue ballpoint pen. The forensic document examiner immediately exposes the forgery. How?",
        ["Modern phthalocyanine dye ballpoint formulas were not commercially manufactured thirty years ago", "The paper was too heavy", "The handwriting was too neat", "The envelope was modern"],
        "Modern phthalocyanine dye ballpoint formulas were not commercially manufactured thirty years ago",
        "Chemical thin-layer chromatography dates ink components against historical manufacturing timelines.",
        "ایک وارث نے 30 سال پرانی وصیت پیش کی جو نیلے بال پوائنٹ سے لکھی گئی تھی۔ دستاویزات کے ماہر نے اسے فوراً جعلی کیسے ثابت کیا؟",
        ["تحریر میں استعمال ہونے والی جدید کیمیائی سیاہی 30 سال پہلے ایجاد ہی نہیں ہوئی تھی", "کاغذ بہت وزنی تھا", "تحریر بہت صاف تھی", "لفافہ نیا تھا"],
        "تحریر میں استعمال ہونے والی جدید کیمیائی سیاہی 30 سال پہلے ایجاد ہی نہیں ہوئی تھی",
        "سیاہی کے لیبارٹری ٹیسٹ نے بتا دیا کہ یہ کیمیکل چند سال پرانا ہے، تیس سال پرانا نہیں ہو سکتا۔"
    ),
    # 273: Muddy shoes vs clean pedals
    (
        "A hit-and-run driver claims someone else hijacked his sedan during an off-road countryside rainstorm. What simple inspection of the vehicle footwell refutes his lie?",
        ["His boots are caked in thick country clay mud, yet the accelerator and brake pedals are spotless clean", "The steering wheel was leather", "The radio was tuned to jazz", "The fuel tank was full"],
        "His boots are caked in thick country clay mud, yet the accelerator and brake pedals are spotless clean",
        "Driving through a muddy off-road deluge leaves heavy mud deposits across control pedals.",
        "گاڑی کے مالک نے بیان دیا کہ کچی کیچڑ والی سڑک پر حادثے کے وقت کوئی دوسرا شخص گاڑی چلا رہا تھا۔ پولیس نے اس کا جھوٹ کیسے پکڑا؟",
        ["اس کے اپنے جوتے کیچڑ سے بھرے تھے مگر گاڑی کے ایکسلریٹر اور بریک کے پیڈل بالکل صاف چمک رہے تھے", "اسٹیئرنگ چمڑے کا تھا", "ریڈیو آن تھا", "پیٹرول کا ٹینک بھرا تھا"],
        "اس کے اپنے جوتے کیچڑ سے بھرے تھے مگر گاڑی کے ایکسلریٹر اور بریک کے پیڈل بالکل صاف چمک رہے تھے",
        "کیچڑ میں گاڑی دوڑانے سے پیڈلز پر مٹی کے جمنے کے لازمی نشانات ہوتے ہیں، ان کا صاف ہونا کہانی کو غلط ثابت کرتا ہے۔"
    ),
    # 274: Sunglasses in night burglary
    (
        "A witness identifies a burglary suspect by claiming she saw him wearing mirrored aviator sunglasses at 2:00 AM in a dimly lit warehouse. Why does the detective dismiss the witness?",
        ["Mirrored sunglasses reduce light transmission by 85%, making navigation in a dark warehouse functionally blind", "Aviators are out of fashion", "The warehouse had glass walls", "The suspect had no glasses"],
        "Mirrored sunglasses reduce light transmission by 85%, making navigation in a dark warehouse functionally blind",
        "Dark tinted sunglasses indoors at night prevent scotopic vision, making physical burglary maneuvers impossible.",
        "عینی شاہد نے گواہی دی کہ اس نے رات کے 2 بجے اندھیرے گودام میں چور کو کالا دھوپ کا چشمہ پہنے دیکھا تھا۔ تفتیش کار نے گواہ کو جھوٹا کیوں قرار دیا؟",
        ["اندھیرے میں کالا چشمہ پہننے سے انسان اندھا ہو جاتا ہے اور گودام میں چلنا ناممکن ہوتا ہے", "چشمہ پرانا تھا", "گودام میں شیشے لگے تھے", "ملزم چشمہ نہیں لگاتا تھا"],
        "اندھیرے میں کالا چشمہ پہننے سے انسان اندھا ہو جاتا ہے اور گودام میں چلنا ناممکن ہوتا ہے",
        "دھوپ کا چشمہ 85 فیصد روشنی روک دیتا ہے، رات کے اندھیرے میں اسے پہن کر چوری کی واردات کرنا ناممکن ہے۔"
    ),
    # 275: Clock stopped at power outage
    (
        "An electric wall clock stopped at 4:17 PM during a lightning surge. A homeowner claims a break-in occurred at 5:30 PM while the power was on. How does the utility company log expose him?",
        ["Grid telemetry records that mains electricity was restored at 4:35 PM, proving the clock was deliberately unplugged earlier", "Electric clocks don't keep time", "Lightning doesn't affect clocks", "The battery had leaked"],
        "Grid telemetry records that mains electricity was restored at 4:35 PM, proving the clock was deliberately unplugged earlier",
        "Substation electrical logs pinpoint exact outage and restoration timestamps, refuting staged alibis.",
        "بجلی کے جھٹکے سے دیوار گھڑی 4:17 پر رک گئی تھی۔ مدعی نے کہا کہ واردات 5:30 بجے بجلی ہوتے ہوئے ہوئی۔ بجلی کی کمپنی کے ریکارڈ نے فراڈ کیسے کھولا؟",
        ["گرڈ کے ریکارڈ کے مطابق بجلی 4:35 پر بحال ہو چکی تھی، یعنی گھڑی کو جان بوجھ کر بند کیا گیا تھا", "بجلی کی گھڑی درست نہیں ہوتی", "آسمانی بجلی گھڑی نہیں روکتی", "سیل ختم ہو گیا تھا"],
        "گرڈ کے ریکارڈ کے مطابق بجلی 4:35 پر بحال ہو چکی تھی، یعنی گھڑی کو جان بوجھ کر بند کیا گیا تھا",
        "بجلی بحال ہونے کے سرکاری لاگ بک نے ثابت کر دیا کہ گھڑی کا پلگ سازش کے تحت خود نکالا گیا تھا۔"
    ),
    # 276: Locked room paper under door
    (
        "A murder occurs inside a room locked from within, with the brass key resting in the keyhole. How did the killer lock the door from outside and leave the key inside?",
        ["Slid a sheet of newspaper under the door, pushed the key out onto the paper with a thin wire, pulled the paper back, and turned it with pliers", "Used a magnetic crane", "Drilled through concrete", "Passed through air ducts"],
        "Slid a sheet of newspaper under the door, pushed the key out onto the paper with a thin wire, pulled the paper back, and turned it with pliers",
        "The classic locked-room newspaper retrieval technique exploits threshold gaps beneath interior doors.",
        "ایک بند کمرے کے اندر سے تالا لگا تھا اور چابی اندر ہی لگی تھی۔ قاتل نے باہر نکل کر اندر چابی چھوڑ کر کمرہ باہر سے کیسے لاک کیا؟",
        ["دروازے کے نیچے کاغذ بچھا کر تار سے چابی کاغذ پر گرائی، کاغذ باہر کھینچ کر پلاس سے کنڈی گھمائی", "بڑے مقناطیس سے", "دیوار میں سوراخ کر کے", "ہوا کی نالی سے"],
        "دروازے کے نیچے کاغذ بچھا کر تار سے چابی کاغذ پر گرائی، کاغذ باہر کھینچ کر پلاس سے کنڈی گھمائی",
        "یہ ایک روایتی معمہ ہے جس میں اخبار کے ٹکڑے کو نیچے سرکا کر چابی گرائی اور واپس حاصل کی جاتی ہے۔"
    ),
    # 277: Poison in punch bowl
    (
        "At an evening gala, twenty guests drink freely from a chilled crystal punch bowl and remain healthy. Two latecomers drink from the same bowl twenty minutes later and collapse. What occurred?",
        ["The poison was frozen inside large floating fruit ice blocks that only thawed into the liquid after twenty minutes", "The latecomers were allergic to fruit", "The crystal bowl dissolved", "Airborne toxins settled"],
        "The poison was frozen inside large floating fruit ice blocks that only thawed into the liquid after twenty minutes",
        "Encapsulating toxins in ice ensures delayed release as thermal thawing dissolves the toxin matrix.",
        "تقریب میں بیس مہمانوں نے شربت کے پیالے سے شربت پیا اور سب خیریت سے رہے۔ بیس منٹ بعد آنے والے دو مہمانوں نے وہی شربت پیا اور بیہوش ہو گئے۔ کیا ہوا تھا؟",
        ["زہر تیرتے ہوئے برف کے بڑے بلاک کے اندر منجمد تھا جو بیس منٹ بعد گھل کر شربت میں شامل ہوا", "مہمانوں کو پھل سے الرجی تھی", "پیالہ زہریلا ہو گیا تھا", "ہوا کا زہر ملا تھا"],
        "زہر تیرتے ہوئے برف کے بڑے بلاک کے اندر منجمد تھا جو بیس منٹ بعد گھل کر شربت میں شامل ہوا",
        "پہلے شربت پینے والوں کے وقت برف جمی ہوئی تھی، بعد میں برف پگھلنے سے زہر پورے مشروب میں پھیل گیا۔"
    ),
    # 278: Twin brother fingerprints
    (
        "Two identical twin brothers share identical nuclear DNA sequences. A forensic technician recovers latent fingerprints from a stolen safe. Can the technician distinguish which twin touched the safe?",
        ["Yes, identical twins possess unique individual fingerprint friction ridges shaped by random intrauterine amniotic fluid flows", "No, their prints are 100% identical", "Only if blood is present", "Only with retina scans"],
        "Yes, identical twins possess unique individual fingerprint friction ridges shaped by random intrauterine amniotic fluid flows",
        "Fingerprint morphogenesis is phenotypic, influenced by physical gestational forces rather than genetics alone.",
        "دو جڑواں بھائیوں کا ڈی این اے (DNA) سو فیصد ایک جیسا ہے۔ چوری کی تجوری سے ملنے والے انگلیوں کے نشانات سے کیا پولیس دونوں میں فرق کر سکتی ہے؟",
        ["ہاں، جڑواں بھائیوں کے فنگر پرنٹس ہمیشہ الگ ہوتے ہیں کیونکہ وہ پیدائش کے وقت رحم میں مختلف بنتے ہیں", "نہیں، ان کے فنگر پرنٹس بالکل ایک جیسے ہوتے ہیں", "صرف خون سے ہو سکتا ہے", "صرف آنکھ کے اسکین سے"],
        "ہاں، جڑواں بھائیوں کے فنگر پرنٹس ہمیشہ الگ ہوتے ہیں کیونکہ وہ پیدائش کے وقت رحم میں مختلف بنتے ہیں",
        "ڈی این اے ایک جیسا ہونے کے باوجود ہر انسان کے فنگر پرنٹس کی باریک لکیریں دنیا میں بالکل منفرد ہوتی ہیں۔"
    ),
    # 279: Fresh water in sea drowning
    (
        "A wealthy sailor is discovered floating dead in deep oceanic salt water. The forensic autopsy immediately confirms he was murdered on land and tossed into the sea. What was the decisive finding?",
        ["His lungs contained chlorinated tap water rather than hypertonic saline seawater with marine diatoms", "His skin had sunburn", "His watch was ticking", "He had no sea salt on hair"],
        "His lungs contained chlorinated tap water rather than hypertonic saline seawater with marine diatoms",
        "Drowning autopsies analyze alveolar fluid electrolyte balance and diatom micro-algae species matching the water body.",
        "سمندر کے نمکین پانی میں ایک ملاح کی لاش ملی۔ ڈاکٹر نے فوری فیصلہ دیا کہ اسے زمین پر قتل کر کے سمندر میں پھینکا گیا تھا۔ سب سے بڑا ثبوت کیا تھا؟",
        ["اس کے پھیپھڑوں کے اندر سمندری پانی کے بجائے نلکے کا میٹھا کلورین والا پانی بھرا ہوا تھا", "اس کے چہرے پر دھوپ تھی", "اس کی گھڑی چل رہی تھی", "اس کے بالوں میں نمک نہیں تھا"],
        "اس کے پھیپھڑوں کے اندر سمندری پانی کے بجائے نلکے کا میٹھا کلورین والا پانی بھرا ہوا تھا",
        "ڈوبنے والے کے پھیپھڑوں میں اسی جگہ کا پانی جاتا ہے جہاں اس کا دم گھٹا ہو، نلکے کے پانی نے قتل کا راز فاش کر دیا۔"
    ),
    # 280: Warm car hood on winter night
    (
        "A murder suspect insists his luxury sedan has been parked unused in his outdoor driveway for four days. It is 10°F outside. The detective places a palm on the vehicle engine hood and arrests him. Why?",
        ["The engine block radiates thermal heat, proving the motor was switched off only minutes ago", "The car was out of gasoline", "The battery had melted", "The exhaust was cold"],
        "The engine block radiates thermal heat, proving the motor was switched off only minutes ago",
        "Cast iron engine blocks have high thermal mass, taking hours to cool down to sub-zero ambient temperatures.",
        "سخت سرد رات میں ملزم نے کہا کہ اس کی گاڑی پچھلے چار دن سے گھر کے باہر کھڑی ہے۔ انسپکٹر نے گاڑی کے بونٹ پر ہاتھ رکھا اور اسے گرفتار کر لیا۔ کیوں؟",
        ["انجن کا بونٹ گرم تپ رہا تھا جس سے ثابت ہوا کہ گاڑی چند منٹ پہلے ہی بند کی گئی تھی", "گاڑی میں پیٹرول ختم تھا", "بیٹری پگھل گئی تھی", "سائلنسر ٹھنڈا تھا"],
        "انجن کا بونٹ گرم تپ رہا تھا جس سے ثابت ہوا کہ گاڑی چند منٹ پہلے ہی بند کی گئی تھی",
        "منفی درجہ حرارت میں گاڑی کا انجن چند منٹ میں برف نہیں بنتا، اس کی گرمی نے جھوٹ کا پردہ چاک کر دیا۔"
    ),
    # 281: Broken watch impact time
    (
        "A victim hit by a vehicle is found by the highway with a shattered mechanical analog watch stopped at 11:42 PM. Why is this forensic evidence critical for establishing the collision time?",
        ["Mechanical balance wheel escapements lock and freeze immediately upon violent physical impact shock", "Watches lose power at night", "The battery drained", "The hands spun backwards"],
        "Mechanical balance wheel escapements lock and freeze immediately upon violent physical impact shock",
        "Physical inertia shears fragile balance pivots or jams gear trains instantly, freezing the exact collision minute.",
        "سڑک کنارے حادثے کے شکار شخص کی کلائی پر میکانیکل گھڑی کا شیشہ ٹوٹا تھا اور وہ ٹھیک 11:42 پر رکی ہوئی تھی۔ یہ ثبوت اہم کیوں ہے؟",
        ["شدید چوٹ لگنے کے جھٹکے سے گھڑی کا بیلنس وہیل اور گیئرز فوراً جام ہو کر وقت قید کر لیتے ہیں", "گھڑی رات کو خود بند ہو جاتی ہے", "سیل ختم ہو گیا تھا", "سوئیاں الٹی گھوم گئی تھیں"],
        "شدید چوٹ لگنے کے جھٹکے سے گھڑی کا بیلنس وہیل اور گیئرز فوراً جام ہو کر وقت قید کر لیتے ہیں",
        "میکانیکل گھڑی زمین یا گاڑی سے ٹکرانے کے شدید جھٹکے سے اسی لمحے رک جاتی ہے جس سے حادثے کا درست وقت ملتا ہے۔"
    ),
    # 282: Sun shadow contradicts alibi
    (
        "A suspect produces a photograph claiming he was relaxing in a public park at noon on the day of a robbery. The detective observes long tree shadows pointing toward the northeast and disproves him. Why?",
        ["At solar noon, shadows are at their shortest minimum length, not long elongated projections", "Trees cast no shadows at noon", "The sun sets in the north", "Cameras distort shadows"],
        "At solar noon, shadows are at their shortest minimum length, not long elongated projections",
        "Solar elevation angle peaks at solar noon; long shadows occur exclusively in early morning or late afternoon.",
        "ملزم نے ایک تصویر دکھائی کہ وہ واردات کے وقت عین دوپہر 12 بجے پارک میں بیٹھا تھا۔ انسپکٹر نے درختوں کے لمبے سائے دیکھ کر جھوٹ کیسے پکڑا؟",
        ["عین دوپہر کے وقت سائے سب سے چھوٹے اور پاؤں کے نیچے ہوتے ہیں، اتنے لمبے سائے شام یا صبح کے ہوتے ہیں", "دوپہر کو سایہ غائب ہو جاتا ہے", "سورج شمال میں غروب ہوتا ہے", "کیمرہ غلط سایہ بناتا ہے"],
        "عین دوپہر کے وقت سائے سب سے چھوٹے اور پاؤں کے نیچے ہوتے ہیں، اتنے لمبے سائے شام یا صبح کے ہوتے ہیں",
        "دوپہر کے وقت سورج عین سر پر ہونے سے سایہ انتہائی مختصر ہوتا ہے، لمبے سائے نے ثابت کیا کہ تصویر شام کی ہے۔"
    ),
    # 283: Ice tray cubes round vs square
    (
        "A homeowner claims his home power was uninterrupted during a summer heatwave while he was away on holiday. What inspection inside the freezer compartment reveals power failed for three days?",
        ["The ice cubes melted into a flat frozen sheet at the bottom of the tray and refroze out of shape", "The freezer smelled like lemon", "The lightbulb was dark", "The door gasket was dry"],
        "The ice cubes melted into a flat frozen sheet at the bottom of the tray and refroze out of shape",
        "Melted ice pools into an amorphous sheet; when power returns, it refreezes as a flat puddle rather than cubes.",
        "مالک مکان نے دعویٰ کیا کہ چھٹیوں کے دوران اس کے گھر کی بجلی کبھی بند نہیں ہوئی۔ فریزر دیکھ کر کیسے پتہ چلا کہ بجلی تین دن بند رہی تھی؟",
        ["برف کی چوکور کیوبز پگھل کر نیچے پانی بن گئی تھیں اور بجلی آنے پر پیندے میں چپٹی برف جمی تھی", "فریزر سے خوشبو آ رہی تھی", "بلب بند تھا", "دروازے پر مٹی تھی"],
        "برف کی چوکور کیوبز پگھل کر نیچے پانی بن گئی تھیں اور بجلی آنے پر پیندے میں چپٹی برف جمی تھی",
        "اگر برف پگھل کر دوبارہ جمے تو کیوبز کی اصل چوکور شکل ختم ہو جاتی ہے اور وہ فرش پر ایک ہی پلیٹ کی طرح جمتی ہے۔"
    ),
    # 284: Blood transfusion type compatibility
    (
        "A trauma patient with type O-negative blood arrives at an emergency department. Why can this patient only receive packed red blood cells from another O-negative donor?",
        ["Type O plasma contains anti-A and anti-B antibodies that agglutinate and destroy any foreign donor antigens", "O-negative blood is too thick", "O-negative blood lacks hemoglobin", "Universal donors cannot receive blood"],
        "Type O plasma contains anti-A and anti-B antibodies that agglutinate and destroy any foreign donor antigens",
        "Type O blood lacks A and B surface glycoproteins; its plasma naturally possesses antibodies against both foreign types.",
        "ایمرجنسی میں او نیگیٹو (O-negative) خون والے مریض کو صرف او نیگیٹو خون ہی کیوں دیا جا سکتا ہے؟",
        ["کیونکہ اس کے پلازما میں اے اور بی دونوں کے خلاف اینٹی باڈیز ہوتی ہیں جو دوسرے خون کو تباہ کر دیتی ہیں", "اس کا خون بہت گاڑھا ہوتا ہے", "اس میں ہیموگلوبن نہیں ہوتا", "اس کے خلیے مر جاتے ہیں"],
        "کیونکہ اس کے پلازما میں اے اور بی دونوں کے خلاف اینٹی باڈیز ہوتی ہیں جو دوسرے خون کو تباہ کر دیتی ہیں",
        "او گروپ کے خون میں اے اور بی دونوں اینٹی جنز کے خلاف مدافعت ہوتی ہے، لہٰذا وہ کسی دوسرے گروپ کو قبول نہیں کرتا۔"
    ),
    # 285: Poisoned letter flap lick
    (
        "A corrupt politician dies suddenly after receiving and opening a confidential sealed letter in his private office. No drink or food was consumed. How was the poison administered?",
        ["Toxins coated the dried envelope adhesive flap, which the victim moistened with his tongue", "Poison gas leaked through paper", "The ink absorbed through fingers", "The stamp fell off"],
        "Toxins coated the dried envelope adhesive flap, which the victim moistened with his tongue",
        "Sublingual buccal mucosa absorbs lethal compounds rapidly when victims lick envelope gum layers.",
        "ایک سیاست دان اپنے بند کمرے میں بند لفافہ کھولتے ہی پراسرار طور پر ہلاک ہو گیا۔ اس نے کچھ کھایا پیا بھی نہیں تھا۔ زہر کیسے دیا گیا تھا؟",
        ["لفافے کی گوند پر زہر لگا ہوا تھا جسے بند کرتے یا کھولتے وقت زبان سے چاٹا گیا تھا", "کاغذ سے زہریلی گیس نکلی تھی", "سیاہی انگلیوں میں جذب ہوئی تھی", "ٹکٹ زہریلا تھا"],
        "لفافے کی گوند پر زہر لگا ہوا تھا جسے بند کرتے یا کھولتے وقت زبان سے چاٹا گیا تھا",
        "زبان کے مسام زہر کو خون میں تیزی سے پہنچاتے ہیں، لفافے کی گوند کو چاٹنا جان لیوا ثابت ہوا۔"
    ),
    # 286: Glass shards fall outside in staged burglary
    (
        "A jeweler reports a break-in, claiming thieves smashed his street display window from the outside sidewalk. The detective finds ninety-five percent of the shattered glass on the exterior sidewalk and arrests the jeweler for insurance fraud. Why?",
        ["Force applied from the outside pushes kinetic fragments inward, whereas smashing from inside scatters glass outside", "Glass always falls on sidewalks", "Thieves sweep glass up", "Diamond cutters leave no glass"],
        "Force applied from the outside pushes kinetic fragments inward, whereas smashing from inside scatters glass outside",
        "Impact momentum projects fractured glass particles in the direction of the applied striking force vector.",
        "سنار نے دعویٰ کیا کہ چوروں نے باہر فٹ پاتھ سے ہتھوڑا مار کر دکان کا شوکیس توڑا۔ تفتیش کار نے شیشے کے 95 فیصد ٹکڑے باہر فٹ پاتھ پر دیکھ کر سنار کو ہی گرفتار کیوں کیا؟",
        ["باہر سے چوٹ لگے تو شیشہ اندر گرتا ہے، شیشے کا باہر گرنا ثابت کرتا ہے کہ اسے اندر سے توڑا گیا تھا", "شیشہ ہمیشہ باہر ہی گرتا ہے", "چور شیشہ صاف کر گئے تھے", "ہتھوڑا چھوٹا تھا"],
        "باہر سے چوٹ لگے تو شیشہ اندر گرتا ہے، شیشے کا باہر گرنا ثابت کرتا ہے کہ اسے اندر سے توڑا گیا تھا",
        "فزکس کا اصول ہے کہ چوٹ جس رخ سے لگے شیشہ اسی سمت گرتا ہے، باہر گرے ٹکڑوں نے اندرونی سازش کا پردہ چاک کیا۔"
    ),
    # 287: Car odometer commute discrepancy
    (
        "A murder suspect claims he drove directly from downtown to his suburban house, a verified route of twelve miles. What dashboard odometer discovery disproves his timeline?",
        ["The trip meter odometer recorded forty-seven additional miles driven since the last logged commute", "The speedometer was needle-stuck", "The tachometer was low", "The fuel gauge was empty"],
        "The trip meter odometer recorded forty-seven additional miles driven since the last logged commute",
        "Mechanical and electronic hub odometers record wheel axle rotations accurately, exposing detour diversions.",
        "ملزم نے بیان دیا کہ وہ دفتر سے سیدھا گھر گیا جو صرف 12 کلومیٹر کا راستہ ہے۔ ڈیش بورڈ کے اوڈومیٹر نے اس کا جھوٹ کیسے پکڑا؟",
        ["ٹرپ میٹر پر 12 کے بجائے 47 کلومیٹر کا اضافی فاصلہ ریکارڈ تھا جس کا مطلب وہ کہیں اور بھی گیا تھا", "اسپیڈومیٹر کی سوئی اٹکی تھی", "انجن کی رفتار کم تھی", "پیٹرول ختم تھا"],
        "ٹرپ میٹر پر 12 کے بجائے 47 کلومیٹر کا اضافی فاصلہ ریکارڈ تھا جس کا مطلب وہ کہیں اور بھی گیا تھا",
        "اوڈومیٹر کے کلومیٹرز نے ثابت کر دیا کہ ملزم سیدھا گھر نہیں گیا بلکہ 35 کلومیٹر کا لمبا چکر کاٹ کر آیا تھا۔"
    ),
    # 288: Wet raincoat over dry coat
    (
        "A detective investigates a suspect's hall closet and observes a sodden wet trenchcoat hung directly on top of a bone-dry winter jacket. What deduction does this sequence reveal?",
        ["The suspect returned home from the torrential storm and hung the coat recently, contradicting his claims of being home all day", "The dry coat is water repellent", "The closet leaked from above", "The coat was washed"],
        "The suspect returned home from the torrential storm and hung the coat recently, contradicting his claims of being home all day",
        "Layering order in closets preserves sequential timelines; wet outer items prove recent entry from outdoors.",
        "تفتیش کار نے الماری میں دیکھا کہ بالکل خشک کوٹ کے اوپر بارش سے بھیگا ہوا گیلا رین کوٹ لٹکا ہے۔ اس سے کیا نتیجہ نکلا؟",
        ["ملزم بارش میں باہر گیا تھا اور ابھی ابھی آ کر کوٹ لٹکایا ہے، گھر میں رہنے کا دعویٰ جھوٹا ہے", "خشک کوٹ واٹر پروف تھا", "الماری کی چھت ٹپک رہی تھی", "کوٹ دھویا گیا تھا"],
        "ملزم بارش میں باہر گیا تھا اور ابھی ابھی آ کر کوٹ لٹکایا ہے، گھر میں رہنے کا دعویٰ جھوٹا ہے",
        "خشک کوٹ کے اوپر گیلے کوٹ کا ہونا ظاہر کرتا ہے کہ ملزم طوفانی بارش میں باہر گیا تھا اور واپسی پر کوٹ اوپر ٹانگا۔"
    ),
    # 289: Cigarette brand discrepancy
    (
        "An eccentric author who smokes exclusively unfiltered Turkish tobacco is found asphyxiated. The detective notices three menthol filter cigarette butts in the ashtray. What is the immediate deduction?",
        ["At least one other person was present in the study prior to the author's demise", "The author changed smoking habits", "Menthol prevents asphyxiation", "The ashtray was antique"],
        "At least one other person was present in the study prior to the author's demise",
        "Physical consumption artifacts mismatched with established personal habits identify third-party visitor presence.",
        "ایک مصنف صرف بغیر فلٹر کا روایتی تمباکو پیتا تھا، اس کے کمرے کی ایش ٹرے میں تین منٹ والے فلٹر سگریٹ کے ٹکڑے ملے۔ فوراً کیا ثابت ہوا؟",
        ["قتل کے وقت کمرے میں کوئی دوسرا شخص لازمی موجود تھا جس نے وہ سگریٹ پیئے تھے", "مصنف نے عادت بدل لی تھی", "فلٹر سگریٹ خود بخود جل گیا", "ایش ٹرے پرانی تھی"],
        "قتل کے وقت کمرے میں کوئی دوسرا شخص لازمی موجود تھا جس نے وہ سگریٹ پیئے تھے",
        "مقتول کی پکی عادت کے برعکس سگریٹ کے ٹکڑوں کی موجودگی نے کسی غیر ملکی یا مہمان قاتل کا پتہ دیا۔"
    ),
    # 290: Mirror reflection viewing angle
    (
        "A witness claims that while washing dishes in the kitchen, she looked into a wall mirror and watched the suspect stab the victim in the adjacent dining alcove. The investigator disproves her. How?",
        ["The law of reflection (angle of incidence equals angle of reflection) proves the alcove is outside the line of sight", "The mirror was dirty", "Mirrors cannot reflect crime", "The kitchen was dark"],
        "The law of reflection (angle of incidence equals angle of reflection) proves the alcove is outside the line of sight",
        "Geometric optics dictates that incident and reflected angles must align with the observer's eye to reflect a target zone.",
        "عینی شاہدہ نے کہا کہ کچن میں برتن دھوتے ہوئے اس نے آئینے میں ملزم کو ڈائننگ روم میں وار کرتے دیکھا۔ تفتیش کار نے اسے جھوٹا کیسے ثابت کیا؟",
        ["روشنی کے انعکاس کے زاویے کے مطابق اس آئینے سے اس کمرے کا وہ کونا دیکھنا بصری طور پر ناممکن تھا", "آئینہ میلا تھا", "آئینے میں جرم نظر نہیں آتا", "کچن میں اندھیرا تھا"],
        "روشنی کے انعکاس کے زاویے کے مطابق اس آئینے سے اس کمرے کا وہ کونا دیکھنا بصری طور پر ناممکن تھا",
        "زاویہ وقوع اور زاویہ انعکاس کے ہندسی اصول نے ثابت کیا کہ کھڑے ہونے کی جگہ سے وہ کونا آئینے میں آ ہی نہیں سکتا تھا۔"
    ),
    # 291: Poisoned sugar cube in coffee
    (
        "Two executives drink from the same freshly brewed pot of Colombian coffee served by a secretary. Executive A drinks his black coffee and suffers zero harm; Executive B adds two sugar cubes and dies of poisoning. What held the toxin?",
        ["The sugar cubes were laced with concentrated poison", "The black coffee neutralized poison", "Executive A was immune", "The cup ceramic dissolved"],
        "The sugar cubes were laced with concentrated poison",
        "Solid porous sugar cubes absorb liquid crystalline toxins easily, delivering targeted doses upon dissolution.",
        "دو افسروں نے ایک ہی کیتلی کی تازہ کافی پی۔ ایک نے بغیر چینی کی کالی کافی پی اور خیریت سے رہا، دوسرے نے دو شکر کی ڈلیاں ملائیں اور زہر سے مر گیا۔ زہر کس میں تھا؟",
        ["شکر کی ڈلیوں کے اندر زہر بھرا ہوا تھا", "کالی کافی نے زہر ختم کر دیا تھا", "پہلے افسر میں مدافعت تھی", "کپ کا مٹیریل خراب تھا"],
        "شکر کی ڈلیوں کے اندر زہر بھرا ہوا تھا",
        "ایک ہی کیتلی کی کافی میں فرق صرف چینی کا تھا، شکر کی ڈلی گھلتے ہی زہر کافی میں شامل ہو گیا۔"
    ),
    # 292: Diver empty tank valve shut
    (
        "A diver drowns twenty feet below sea level with eighty percent of his compressed breathing air still remaining in his scuba cylinder. What mechanical oversight caused his asphyxiation?",
        ["His cylinder manifold valve was turned off, starving his demand regulator of air despite a full tank", "The air was nitrogen only", "Water entered the gauge", "His fins snapped"],
        "His cylinder manifold valve was turned off, starving his demand regulator of air despite a full tank",
        "Failing to open the tank valve or accidentally bumping it closed isolates high-pressure gas from the regulator.",
        "ایک غوطہ خور کے سلنڈر میں 80 فیصد آکسیجن باقی ہونے کے باوجود وہ پانی میں دم گھٹنے سے مر گیا۔ کیا تکنیکی غلطی ہوئی تھی؟",
        ["سلنڈر کا والو بند تھا جس کی وجہ سے سلنڈر بھرا ہونے کے باوجود منہ کے ماسک تک ہوا نہیں پہنچ رہی تھی", "سلنڈر میں صرف نائٹروجن تھی", "گیج میں پانی چلا گیا تھا", "پر ٹوٹ گئے تھے"],
        "سلنڈر کا والو بند تھا جس کی وجہ سے سلنڈر بھرا ہونے کے باوجود منہ کے ماسک تک ہوا نہیں پہنچ رہی تھی",
        "سلنڈر بھرا ہوا تھا مگر اس کا مین والو بند رہ جانے کی وجہ سے غوطہ خور کو سانس لینے کے لیے ہوا نہ مل سکی۔"
    ),
    # 293: Burglary footprint depth
    (
        "Police track two sets of footprints in soft garden soil made by the exact same pair of boots. One set has twice the indentation depth into the loam. What does this tell the detective?",
        ["The suspect was carrying heavy loot or a body when making the deeper set of footprints", "The suspect ran faster", "The suspect jumped", "The soil was warmer"],
        "The suspect was carrying heavy loot or a body when making the deeper set of footprints",
        "Soil compressive displacement is proportional to total downward gravitational force (body weight + carried load).",
        "باغ کی نرم مٹی میں ایک ہی جوتے کے نشانات کی دو قطاریں ملیں۔ ایک قطار کے نشانات زمین میں دو گنا زیادہ گہرے دھنسے ہوئے تھے۔ تفتیش کار نے کیا نتیجہ نکالا؟",
        ["واپسی پر ملزم نے بھاری تجوری یا وزنی مال اٹھا رکھا تھا جس سے اس کا وزن دگنا ہو گیا تھا", "ملزم تیز دوڑ رہا تھا", "ملزم نے چھلانگ لگائی تھی", "مٹی گرم تھی"],
        "واپسی پر ملزم نے بھاری تجوری یا وزنی مال اٹھا رکھا تھا جس سے اس کا وزن دگنا ہو گیا تھا",
        "وزن جتنا زیادہ ہوگا مٹی پر جوتے کا دباؤ اور گہرائی اتنی ہی بڑھ جائے گی، گہرے نشانات نے وزنی مال کا پتہ دیا۔"
    ),
    # 294: Gunpowder stippling tattooing
    (
        "A forensic coroner inspects a gunshot entry wound surrounded by dense circular gunpowder stippling and unburnt powder grains tattooed into the dermis. What does this establish about firing distance?",
        ["The firearm was discharged at close range (typically within one to three feet of the target)", "The shot came from a distant sniper rifle", "The weapon was fired in a vacuum", "The bullet had no powder"],
        "The firearm was discharged at close range (typically within one to three feet of the target)",
        "Burning powder flakes and vaporized lead travel only a few feet before dissipating in ambient air.",
        "مقتول کے گولی کے زخم کے ارد گرد جلد پر بارود کے جلنے کے باریک سیاہ دھبے اور دانے جمے ہوئے تھے۔ اس سے گولی کے فاصلے کا کیا پتہ چلا؟",
        ["گولی انتہائی قریب سے یعنی ایک سے تین فٹ کے فاصلے سے چلائی گئی تھی", "گولی میل دور سے اسنائپر نے ماری تھی", "پستول میں بارود نہیں تھا", "گولی ہوا میں لگی تھی"],
        "گولی انتہائی قریب سے یعنی ایک سے تین فٹ کے فاصلے سے چلائی گئی تھی",
        "بارود کے جلتے ہوئے ذرات صرف چند فٹ تک ہی سفر کر کے جلد میں دھنستے ہیں، جس سے قریبی فاصلے کا ثبوت ملا۔"
    ),
    # 295: Window screen cut inside
    (
        "A homeowner reports a break-in, showing police a sliced patio window screen. The forensic examiner notes that the frayed wire mesh burrs flare outward toward the garden. What does this reveal?",
        ["The screen was sliced from inside the residence, indicating a staged burglary", "A burglar cut it from outside", "Rats chewed through the screen", "Wind blew the screen open"],
        "The screen was sliced from inside the residence, indicating a staged burglary",
        "Cutting tools push displaced wire metal burrs in the direction of the penetrating blade stroke.",
        "مالک مکان نے دعویٰ کیا کہ چور نے باہر سے کھڑکی کی جالی کاٹ کر اندر چوری کی۔ پولیس نے جالی کے تار باہر مڑے ہوئے دیکھ کر کیا فیصلہ دیا؟",
        ["جالی کو گھر کے اندر سے کاٹا گیا تھا، چوری کا ڈراما خود مالک نے رچایا تھا", "چور نے باہر سے کاٹا تھا", "چوہے نے کتری تھی", "ہوا سے کٹ گئی تھی"],
        "جالی کو گھر کے اندر سے کاٹا گیا تھا، چوری کا ڈراما خود مالک نے رچایا تھا",
        "چھری کا رخ جس طرف ہوگا جالی کے کٹے ہوئے تار اسی طرف مڑیں گے، باہر کی طرف مڑے تاروں نے اندرونی واردات ثابت کی۔"
    ),
    # 296: Dog barking at midnight
    (
        "A ferocious guard dog sleeps in the courtyard of an estate where a midnight burglary took place. No poison or sedative was administered to the dog, yet it barked zero times. What is Sherlock Holmes' classic deduction?",
        ["The midnight intruder was someone well-known and familiar to the guard dog", "The dog had lost its voice", "Burglars wore animal skin", "Dogs sleep through all noises"],
        "The midnight intruder was someone well-known and familiar to the guard dog",
        "Territorial guard dogs bark aggressively at unfamiliar scents and strangers, remaining calm only around household familiars.",
        "ایک بنگلے میں آدھی رات کو چوری ہوئی مگر صحن میں بندھا خونخوار کتا ایک بار بھی نہیں بھونکا اور نہ اسے بے ہوش کیا گیا تھا۔ شیرلاک ہومز کا نتیجہ کیا تھا؟",
        ["چور کوئی باہر کا اجنبی نہیں تھا بلکہ گھر کا ہی کوئی جانا پہچانا فرد تھا جسے دیکھ کر کتا خاموش رہا", "کتے کی آواز بند ہو گئی تھی", "چور نے جانور کا لباس پہنا تھا", "کتے رات کو نہیں جاگتے"],
        "چور کوئی باہر کا اجنبی نہیں تھا بلکہ گھر کا ہی کوئی جانا پہچانا فرد تھا جسے دیکھ کر کتا خاموش رہا",
        "کتا صرف اجنبی کو دیکھ کر بھونکتا ہے، اس کا چپ رہنا اس بات کا کھلا ثبوت تھا کہ آنے والا اس کا شناسا تھا۔"
    ),
    # 297: Poisoned apple cut in half
    (
        "A wicked assassin cuts a fresh red apple in half before an associate. Both eat their respective halves immediately. The associate dies of poison, but the assassin remains unhurt. How was this achieved?",
        ["The knife blade was coated with lethal contact poison on only one side of its cutting edge", "The assassin swallowed an antidote tablet", "Half the apple was plastic", "The associate was allergic to fruit"],
        "The knife blade was coated with lethal contact poison on only one side of its cutting edge",
        "Single-sided blade coating transfers chemical toxins exclusively to the slice contacting that face.",
        "ایک شخص نے تازہ سیب کو چھری سے بیچ میں سے دو ٹکڑے کیا اور ایک ٹکڑا خود کھایا اور دوسرا ساتھی کو دیا۔ ساتھی زہر سے مر گیا مگر وہ خود بچ گیا۔ کیسے؟",
        ["چھری کی دھار کے صرف ایک رخ پر زہر لگا ہوا تھا جس سے سیب کا صرف ایک ٹکڑا زہریلا ہوا", "اس نے پہلے تریاق پی لیا تھا", "آدھا سیب پلاسٹک کا تھا", "ساتھی کو الرجی تھی"],
        "چھری کی دھار کے صرف ایک رخ پر زہر لگا ہوا تھا جس سے سیب کا صرف ایک ٹکڑا زہریلا ہوا",
        "چھری کے ایک طرف زہر لگانے سے کٹتے وقت زہر صرف ایک ہی آدھے حصے پر لگا جبکہ دوسرا رخ بالکل محفوظ رہا۔"
    ),
    # 298: Frozen meat weapon roast
    (
        "A detective investigates the blunt-force skull trauma murder of a husband. The police search the home thoroughly but find zero blunt weapons. The smiling widow serves the detectives a hot leg of lamb roast. What was the weapon?",
        ["A frozen rock-hard leg of lamb, which the widow subsequent roasted and served as dinner to destroy the evidence", "An iron skillet hidden under stove", "A block of lead melted in oven", "A heavy wooden rolling pin"],
        "A frozen rock-hard leg of lamb, which the widow subsequent roasted and served as dinner to destroy the evidence",
        "Roald Dahl's classic 'Lamb to the Slaughter': frozen bone-in meat acts as a lethal bludgeon and is consumed upon cooking.",
        "ایک شخص کو کسی وزنی اور سخت چیز سے سر پر وار کر کے قتل کیا گیا۔ پولیس کو کوئی ہتھوڑا یا ڈنڈا نہ ملا۔ بیوہ نے تفتیش کاروں کو رات کے کھانے میں پکا ہوا مٹن کھلایا۔ ہتھیار کیا تھا؟",
        ["فریزر کا پتھر جیسا جما ہوا گوشت (ران) جس سے وار کیا گیا اور بعد میں پکا کر ثبوت ہی مٹا دیا گیا", "لوہے کا توا", "لکڑی کا بیلن", "پانی کی بوتل"],
        "فریزر کا پتھر جیسا جما ہوا گوشت (ران) جس سے وار کیا گیا اور بعد میں پکا کر ثبوت ہی مٹا دیا گیا",
        "جمے ہوئے گوشت کی ران ہتھوڑے جیسی سخت ہوتی ہے، پکانے کے بعد ہتھیار کا نام و نشان ہی ختم ہو گیا۔"
    ),
    # 299: Toll booth timestamp alibi
    (
        "A suspect produces a receipt proving he paid cash at a toll booth two hundred miles away at 8:00 PM, claiming he couldn't have committed an 8:30 PM crime in the capital. How does the camera disprove him?",
        ["Automated license plate recognition camera captured a different vehicle; he merely picked up a dropped discarded ticket", "Toll booths have no clocks", "Toll booths use solar time", "His car was electric"],
        "Automated license plate recognition camera captured a different vehicle; he merely picked up a dropped discarded ticket",
        "ALPR highway overhead cameras match physical timestamps with high-resolution plate imaging and driver profile photos.",
        "ملزم نے 200 میل دور کے ٹول پلازہ کی 8:00 بجے کی کیش پرچی دکھا کر دعویٰ کیا کہ وہ 8:30 کے دارالحکومت کے قتل میں شریک نہیں ہو سکتا۔ کیمرے نے فراڈ کیسے کھولا؟",
        ["ٹول پلازہ کے کیمرے نے تصویر میں دوسری کار اور ڈرائیور کو دکھایا، ملزم نے گری ہوئی پرچی اٹھائی تھی", "ٹول پر گھڑی نہیں ہوتی", "گاڑی بجلی کی تھی", "پرچی پر تاریخ نہیں تھی"],
        "ٹول پلازہ کے کیمرے نے تصویر میں دوسری کار اور ڈرائیور کو دکھایا، ملزم نے گری ہوئی پرچی اٹھائی تھی",
        "کیمرے کے ریکارڈ نے ثابت کیا کہ اس پرچی کے وقت نکلنے والی گاڑی کا نمبر ملزم کی گاڑی سے بالکل الگ تھا۔"
    ),
    # 300: Stolen gold bars painted black
    (
        "A dockworker smuggles twenty heavy bullion gold bars past customs checkpoints without concealment in bags. What simple optical disguise allowed him to load them openly as gym equipment?",
        ["He painted the high-density gold bars with matte black enamel paint, labeling them as heavy cast iron gym weights", "He covered them in clear foil", "He bleached them white", "He disguised them as bread"],
        "He painted the high-density gold bars with matte black enamel paint, labeling them as heavy cast iron gym weights",
        "Enamel paint masks gold's characteristic luster, while heavy mass naturally mimics dense exercise iron weights.",
        "ایک اسمگلر نے سونے کی 20 وزنی اینٹیں کسٹم والوں کے سامنے سے کھلے عام کیسے نکال لیں؟",
        ["اس نے سونے پر کالا میٹ پینٹ کر دیا تھا جس سے وہ ورزش کے ڈمبل اور لوہے کے باٹ لگ رہے تھے", "اس نے کاغذ میں لپیٹا تھا", "اس نے سفید رنگ کیا تھا", "اس نے روٹی کی شکل دی تھی"],
        "اس نے سونے پر کالا میٹ پینٹ کر دیا تھا جس سے وہ ورزش کے ڈمبل اور لوہے کے باٹ لگ رہے تھے",
        "سونے کا وزن بہت زیادہ ہوتا ہے، کالا رنگ کرنے سے سب نے سمجھا کہ یہ ورزش کے لیے ڈھلے ہوئے لوہے کے وزنی باٹ ہیں۔"
    )
]

print(f"Normal Catalog A loaded {len(ITEMS)} items.")
