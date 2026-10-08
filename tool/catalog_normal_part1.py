# -*- coding: utf-8 -*-
"""
Catalog Normal - Part 1 (Items 251 to 450: 200 items)
Detective mysteries, forensic logic, classic dilemmas, and lateral deduction puzzles.
Zero template loops, zero repeated POVs.
"""

ITEMS = [
    # 251: Three light switches
    {
        "en": ("Three light switches outside a closed room control three incandescent bulbs inside. You can only enter the room once. How do you identify which switch controls which bulb?",
         ["Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3", "Turn all three on", "Flip switch 1 repeatedly", "Look under the door"],
         "Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3",
         "Incandescent bulbs emit thermal heat; feeling the unlit warm bulb identifies the first switch."),
        "ur": ("بند کمرے کے باہر تین سوئچ ہیں جو اندر کے تین بلب کنٹرول کرتے ہیں۔ آپ صرف ایک بار کمرے میں جا سکتے ہیں۔ کس سوئچ سے کون سا بلب جلتا ہے کیسے معلوم کریں گے؟",
         ["پہلا سوئچ 10 منٹ آن رکھ کر بند کریں، دوسرا آن کریں اور اندر جائیں: جلتا بلب 2، گرم بلب 1، ٹھنڈا بلب 3 ہے", "تینوں سوئچ آن کر کے", "سوئچ تیزی سے بند کر کے", "دروازے کے نیچے سے دیکھ کر"],
         "پہلا سوئچ 10 منٹ آن رکھ کر بند کریں، دوسرا آن کریں اور اندر جائیں: جلتا بلب 2، گرم بلب 1، ٹھنڈا بلب 3 ہے",
         "پہلا بلب جلنے کی وجہ سے گرم ہو چکا ہوگا جبکہ دوسرا بلب اس وقت جل رہا ہوگا۔")
    },
    # 252: Water jugs 3 and 5 gallons
    {
        "en": ("With an unmarked 3-gallon jug and an unmarked 5-gallon jug at an endless water fountain, how can you measure out exactly 4 gallons?",
         ["Fill 5-gallon, pour into 3-gallon leaving 2; empty 3-gallon, transfer 2 into 3-gallon; fill 5-gallon, top off 3-gallon leaving 4 in 5-gallon", "Fill both jugs halfway", "Guess the midpoint", "Weigh them on a scale"],
         "Fill 5-gallon, pour into 3-gallon leaving 2; empty 3-gallon, transfer 2 into 3-gallon; fill 5-gallon, top off 3-gallon leaving 4 in 5-gallon",
         "Pouring 1 gallon from a full 5-gallon jug into the 3-gallon jug containing 2 gallons leaves exactly 4 gallons."),
        "ur": ("ایک 3 لیٹر اور ایک 5 لیٹر کا خالی برتن لے کر نہر سے ٹھیک 4 لیٹر پانی کیسے ناپیں گے؟",
         ["5 لیٹر والے سے 3 لیٹر بھر کر باقی 2 لیٹر بچائیں، اسے خالی 3 والے میں ڈالیں، پھر 5 والا بھر کر 3 والے میں 1 لیٹر ڈالیں تو 4 لیٹر بچے گا", "دونوں کو آدھا بھر کر", "اندازے سے ناپ کر", "ترازو پر تول کر"],
         "5 لیٹر والے سے 3 لیٹر بھر کر باقی 2 لیٹر بچائیں، اسے خالی 3 والے میں ڈالیں، پھر 5 والا بھر کر 3 والے میں 1 لیٹر ڈالیں تو 4 لیٹر بچے گا",
         "اس کلاسیکی حسابی طریقے سے 5 لیٹر کے برتن میں بالکل درست 4 لیٹر پانی بچ جاتا ہے۔")
    },
    # 253: Two hourglasses 7 and 4 minutes
    {
        "en": ("You have a 7-minute sand hourglass and a 4-minute sand hourglass. How do you time exactly 9 minutes to cook a delicacy?",
         ["Start both; when 4-min runs out, invert it; when 7-min runs out (1 min left in 4-min), invert 7-min; when 4-min finishes (8 min), 7-min has 1 min of sand, invert it to reach 9", "Run 7-minute twice", "Guess the middle of 7-min", "Run 4-minute twice"],
         "Start both; when 4-min runs out, invert it; when 7-min runs out (1 min left in 4-min), invert 7-min; when 4-min finishes (8 min), 7-min has 1 min of sand, invert it to reach 9",
         "Staggering sand flow intervals isolates single-minute increments to total 9 minutes."),
        "ur": ("آپ کے پاس ایک 7 منٹ اور ایک 4 منٹ والی ریت کی گھڑیاں ہیں۔ بالکل 9 منٹ کا وقت کیسے ناپیں گے؟",
         ["دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے", "7 منٹ والی دو بار چلا کر", "اندازہ لگا کر", "4 منٹ والی دو بار چلا کر"],
         ["دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے", "7 منٹ والی دو بار چلا کر", "اندازہ لگا کر", "4 منٹ والی دو بار چلا کر"][0],
         "دونوں ریت کی گھڑیوں کے فرق کو استعمال کر کے بالکل درست نو منٹ ناپے جا سکتے ہیں۔")
    },
    # 254: 12 coins balance scale
    {
        "en": ("Among 12 gold coins, 1 is counterfeit with a slightly different weight (heavier or lighter). What is the minimum weighings on a balance scale to find it?",
         ["Three weighings", "Four weighings", "Two weighings", "Six weighings"],
         "Three weighings",
         "Ternary decision trees allow 3^3 = 27 outcome branches, sufficient to identify 1 of 12 coins and determine if heavier or lighter."),
        "ur": ("12 سونے کے سکوں میں سے ایک سکہ نقلی ہے جس کا وزن باقیوں سے مختلف ہے، دو پلڑوں والے ترازو پر کم از کم کتنی بار تول کر وہ سکہ تلاش کیا جا سکتا ہے؟",
         ["تین بار", "چار بار", "دو بار", "چھ بار"],
         "تین بار",
         "تین بار تولنے سے کل 27 ممکنہ نتائج نکلتے ہیں جو 12 سکوں میں سے نقلی سکہ پہچاننے کے لیے کافی ہیں۔")
    },
    # 255: 9 balls balance scale
    {
        "en": ("You have 9 identical-looking billiard balls, 1 of which is slightly heavier. What is the minimum weighings on a balance scale to find it?",
         ["Two weighings", "Three weighings", "Four weighings", "One weighing"],
         "Two weighings",
         "Weigh 3 against 3: if balanced, the heavy ball is in remaining 3; then weigh 1 against 1 from the heavy trio."),
        "ur": ("9 ایک جیسی گیندوں میں سے ایک گیند وزنی ہے۔ ترازو کے دو پلڑوں سے کم سے کم کتنی بار تول کر وزنی گیند کا پتہ لگایا جا سکتا ہے؟",
         ["صرف دو بار", "تین بار", "چار بار", "ایک بار"],
         "صرف دو بار",
         "پہلے 3 اور 3 تولیں، جس سے وزنی گروپ کا پتہ چلے گا، پھر اس گروپ کی 1 اور 1 تولنے سے وزنی گیند مل جائے گی۔")
    },
    # 256: Bridge torch crossing
    {
        "en": ("Four travelers need to cross a narrow rope bridge at night with 1 torch that burns for 17 minutes. Speeds are 1, 2, 5, and 10 minutes. At most 2 can cross together. How do all four cross in 17 minutes?",
         ["1 and 2 cross (2 min), 1 returns (3 min), 5 and 10 cross (13 min), 2 returns (15 min), 1 and 2 cross (17 min)", "1 escorts each person across one by one", "Fastest runs across carrying the others", "They cross without the torch"],
         "1 and 2 cross (2 min), 1 returns (3 min), 5 and 10 cross (13 min), 2 returns (15 min), 1 and 2 cross (17 min)",
         "Pairing the two slowest travelers (5 and 10) together avoids wasting fast trips returning the torch."),
        "ur": ("رات کے اندھیرے میں چار مسافروں کو ایک مشعل کے ساتھ پل پار کرنا ہے جس کے جلنے کا وقت 17 منٹ ہے۔ ان کی رفتار 1، 2، 5 اور 10 منٹ ہے۔ وہ 17 منٹ میں کیسے پار کریں گے؟",
         ["1 اور 2 جائیں (2 منٹ)، 1 مشعل لائے (3)، پھر 5 اور 10 جائیں (13)، 2 مشعل لائے (15)، پھر 1 اور 2 جائیں (17 منٹ)", "1 سب کو باری باری لے جائے", "سب بغیر مشعل کے دوڑیں", "سب سے تیز والا باقیوں کو اٹھا لے"],
         "1 اور 2 جائیں (2 منٹ)، 1 مشعل لائے (3)، پھر 5 اور 10 جائیں (13)، 2 مشعل لائے (15)، پھر 1 اور 2 جائیں (17 منٹ)",
         "دو سست ترین مسافروں (5 اور 10) کو ایک ساتھ بھیجنے سے مشعل واپس لانے کا قیمتی وقت بچ جاتا ہے۔")
    },
    # 257: Two doors guards
    {
        "en": ("Two doors lead to freedom and execution. One guard always tells the truth, and the other always lies. What single question asked to one guard reveals the door to freedom?",
         ["Which door would the other guard say leads to freedom?", "Which door is freedom?", "Are you lying?", "Do you guard the good door?"],
         "Which door would the other guard say leads to freedom?",
         "Both guards will inevitably point to the door of execution, so you choose the opposite door."),
        "ur": ("دو دروازوں میں سے ایک آزادی اور دوسرا قید کا ہے۔ دو پہریداروں میں سے ایک ہمیشہ سچ بولتا ہے اور دوسرا ہمیشہ جھوٹ۔ ایک ہی سوال سے آزادی کا راستہ کیسے معلوم ہوگا؟",
         ["اگر میں دوسرے پہریدار سے پوچھوں تو وہ آزادی کا دروازہ کون سا بتائے گا؟", "آزادی کا دروازہ کون سا ہے؟", "کیا تم سچ بول رہے ہو؟", "تم کون ہو؟"],
         "اگر میں دوسرے پہریدار سے پوچھوں تو وہ آزادی کا دروازہ کون سا بتائے گا؟",
         "سچ اور جھوٹ مل کر ہمیشہ جھوٹا دروازہ بتائیں گے، اس لیے آپ بتائے گئے دروازے کے الٹ جائیں۔")
    },
    # 258: 100 lockers puzzle
    {
        "en": ("In a school hall with 100 closed lockers, 100 students pass through. Student 1 opens all. Student 2 closes every 2nd. Student 3 toggles every 3rd, up to student 100. Which lockers remain open?",
         ["Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "All prime numbered lockers", "All even numbered lockers", "All odd numbered lockers"],
         "Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
         "Only perfect squares have an odd number of factors; all other numbers have pairs of factors resulting in being closed."),
        "ur": ("اسکول کے 100 بند لاکرز پر 100 طلبہ باری باری گزرتے ہیں۔ پہلا سب کھولتا ہے، دوسرا ہر دوسرا بند کرتا ہے، تیسرا ہر تیسرا بدلتا ہے۔ آخر میں کون سے لاکرز کھلے رہیں گے؟",
         ["صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "تمام طاق اعداد والے", "تمام جفت اعداد والے", "تمام پرائم اعداد والے"],
         "صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
         "صرف مکمل مربع اعداد کے فیکٹرز طاق تعداد میں ہوتے ہیں جس کی وجہ سے وہ کھلے رہ جاتے ہیں۔")
    },
    # 259: Three mislabeled fruit boxes
    {
        "en": ("Three boxes are labeled Apples, Oranges, and Mixed (Apples & Oranges). All three labels are guaranteed incorrect. You can pick 1 fruit from 1 box without looking inside. Which box do you pick from to label all correctly?",
         ["Pick from the box labeled Mixed", "Pick from the box labeled Apples", "Pick from the box labeled Oranges", "Cannot be solved with 1 pick"],
         "Pick from the box labeled Mixed",
         "Since the Mixed label is wrong, picking 1 fruit identifies that entire box; the remaining two mislabeled boxes are deduced uniquely."),
        "ur": ("تین ڈبوں پر 'سیب'، 'مالٹے' اور 'مکس' کے لیبل لگے ہیں مگر تینوں لیبل غلط ہیں۔ آپ صرف ایک ڈبے میں سے بنا دیکھے ایک پھل نکال سکتے ہیں۔ تمام ڈبے درست کیسے کریں گے؟",
         ["جس ڈبے پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر", "سیب والے ڈبے سے", "مالٹے والے ڈبے سے", "ایک پھل سے ممکن نہیں"],
         "جس ڈبے پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر",
         "کیونکہ مکس کا لیبل غلط ہے، اس میں سے جو پھل نکلے گا وہ پورا ڈبہ وہی ہوگا، اور باقی دو ڈبے خود بخود سیدھے ہو جائیں گے۔")
    },
    # 260: Single-elimination tennis tournament
    {
        "en": ("In a single-elimination knockout tournament featuring 64 players, how many total matches must be played to crown the champion?",
         ["63 matches", "64 matches", "32 matches", "128 matches"],
         "63 matches",
         "Each match eliminates exactly one loser; to eliminate 63 players requires exactly 63 matches."),
        "ur": ("ایک ناک آؤٹ ٹینس ٹورنامنٹ میں 64 کھلاڑی حصہ لے رہے ہیں۔ چیمپیئن کا فیصلہ کرنے کے لیے کل کتنے میچ کھیلنا پڑیں گے؟",
         ["63 میچ", "64 میچ", "32 میچ", "128 میچ"],
         "63 میچ",
         "ہر میچ میں ایک کھلاڑی ہار کر باہر ہوتا ہے، 63 کھلاڑیوں کو باہر کرنے کے لیے ٹھیک 63 میچ درکار ہیں۔")
    },
    # 261: Dinner party handshakes
    {
        "en": ("At a diplomatic dinner party of 10 people, everyone shakes hands with everyone else exactly once. How many total handshakes occur?",
         ["45 handshakes", "90 handshakes", "50 handshakes", "100 handshakes"],
         "45 handshakes",
         "Combinations of 10 people taken 2 at a time: n*(n-1)/2 = 10 * 9 / 2 = 45."),
        "ur": ("ایک دعوت میں 10 لوگ موجود ہیں اور ہر شخص دوسرے ہر شخص سے ایک بار مصافحہ (ہاتھ ملاتا) کرتا ہے۔ کل کتنے مصافحے ہوں گے؟",
         ["45 مصافحے", "90 مصافحے", "50 مصافحے", "100 مصافحے"],
         "45 مصافحے",
         "مصافحوں کا فارمولا n*(n-1)/2 ہوتا ہے، یعنی 10 ضرب 9 تقسیم 2 برابر ہے 45۔")
    },
    # 262: Monty Hall door switch
    {
        "en": ("On a game show, you choose Door 1 out of 3. The host opens Door 3, revealing a goat, and offers you Door 2. What gives you the highest mathematical probability of winning the car?",
         ["Switching to Door 2 (2/3 chance of winning)", "Staying with Door 1 (2/3 chance)", "It is strictly 50/50, no difference", "Flipping a coin"],
         "Switching to Door 2 (2/3 chance of winning)",
         "Your initial pick had a 1/3 chance; the unopened remaining door inherits the entire 2/3 probability of the other two doors."),
        "ur": ("ایک گیم شو میں تین میں سے ایک دروازے کے پیچھے کار ہے۔ آپ نے دروازہ 1 چنا، میزبان نے دروازہ 3 کھولا جہاں بکری نکلی۔ کار جیتنے کا زیادہ امکان کس میں ہے؟",
         ["دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)", "دروازہ 1 پر ہی رہنے سے", "دونوں میں بالکل برابر 50/50 چانس ہے", "کوئی فرق نہیں پڑتا"],
         "دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)",
         "پہلے انتخاب کا امکان صرف 1/3 تھا، جبکہ دوسرے دروازے کے پاس اب 2/3 کا زبردست امکان موجود ہے۔")
    },
    # 263: Elevator short man
    {
        "en": ("A man lives on the 15th floor. Every morning he rides the elevator all the way to ground. Returning home, he rides to the 10th floor and walks up 5 flights of stairs, unless it rains. Why?",
         ["He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days", "He likes exercising on dry days", "The elevator is broken above floor 10", "He visits a friend on floor 10"],
         "He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days",
         "The height of button 10 is the maximum reach of his arm; an umbrella gives him extra physical reach."),
        "ur": ("ایک شخص پندرہویں منزل پر رہتا ہے۔ وہ صبح لفٹ سے نیچے جاتا ہے مگر واپسی پر دسویں منزل پر اتر کر پانچ منزلیں پیدل چڑھتا ہے، سوائے بارش کے دن کے۔ کیوں؟",
         ["کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے", "وہ ورزش کا شوقین ہے", "لفٹ اوپر خراب ہوتی ہے", "اس کا دوست دسویں منزل پر ہے"],
         "کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے",
         "چھوٹے قد کی وجہ سے وہ اوپر کا بٹن ہاتھ سے نہیں دبا پاتا تھا، چھتری کا دستہ اسے پہنچا دیتا تھا۔")
    },
    # 264: Hotel Monopoly bankruptcy
    {
        "en": ("A man pushes his car up to a luxury hotel and instantly realizes he is completely bankrupt. What was he doing?",
         ["Playing the board game Monopoly with a car token", "His real car engine blew up", "He lost his hotel reservation", "He was robbed by valets"],
         "Playing the board game Monopoly with a car token",
         "In Monopoly, landing a miniature car token on an opponent's hotel property incurs a ruinous rent fine."),
        "ur": ("ایک شخص نے اپنی کار کو ہوٹل کے سامنے دھکیلا اور فورا سمجھ گیا کہ وہ کنگال ہو چکا ہے، وہ کیا کر رہا تھا؟",
         ["وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا", "اس کی اصل کار خراب ہو گئی تھی", "ہوٹل کا بل بہت زیادہ تھا", "اس کے پیسے چوری ہو گئے تھے"],
         "وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا",
         "مونوپولی کھیل میں کار کا مہرہ حریف کے ہوٹل پر پہنچنے کا مطلب دیوالیہ ہو جانا ہے۔")
    },
    # 265: Poisoned iced tea drinkers
    {
        "en": ("Two thirsty men order identical iced tea glasses at a desert saloon. Mark drinks five glasses quickly in two minutes; Dan drinks one glass slowly over an hour. Dan dies of poison, but Mark survives. Why?",
         ["The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's", "Mark had developed immunity to poison", "Dan's straw was laced with poison", "Mark was given a different pitcher"],
         "The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's",
         "Drinking fast before the ice melted prevented Mark from ingesting the toxin released upon thawing."),
        "ur": ("دو دوستوں نے ایک جیسا ٹھنڈا شربت پیا۔ ایک نے جلدی جلدی 5 گلاس پی لیے جبکہ دوسرے نے ایک گھنٹے میں ایک گلاس آہستہ پیا۔ آہستہ پینے والا زہر سے مر گیا مگر دوسرا بچ گیا۔ کیوں؟",
         ["زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا", "پہلے دوست میں زہر کی قوت مدافعت تھی", "اسٹرا میں زہر لگا تھا", "دوسرے کا شربت الگ تھا"],
         "زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا",
         "جلدی پینے والے کے وقت برف پگھلی نہیں تھی، آہستہ پینے والے کی برف گھل کر زہر شربت میں شامل ہو گیا۔")
    },
    # 266: Tape recorder suicide alibi
    {
        "en": ("A detective investigates a supposed suicide. On the desk is a cassette tape recorder. Pressing play, they hear: 'I cannot go on living', followed by a gunshot. The detective immediately rules it a homicide. Why?",
         ["The cassette tape was rewound back to the beginning, which a dead person cannot do", "The gunshot sounded too loud", "The voice was synthesized", "The tape was blank"],
         "The cassette tape was rewound back to the beginning, which a dead person cannot do",
         "After shooting oneself, a deceased individual cannot press the rewind button on a mechanical cassette player."),
        "ur": ("ایک کمرے میں خودکشی کا شبہ تھا۔ میز پر ٹیپ ریکارڈر تھا، پلے کرنے پر گولی چلنے کی آواز آئی۔ تفتیشی افسر نے فورا اسے قتل قرار دیا۔ کیوں؟",
         ["کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا", "گولی کی آواز بہت دھیمی تھی", "کیسٹ پرانی تھی", "کمرہ بند تھا"],
         "کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا",
         "گولی لگنے کے بعد مرنے والا شخص خود کیسٹ کا بٹن دبا کر اسے واپس شروع پر نہیں لا سکتا۔")
    },
    # 267: Window frost inside vs outside
    {
        "en": ("On a freezing winter morning, a home owner claims a burglar scratched the window glass from the outside to break in. The detective notices frost condensation on the inside pane and disproves the story. Why?",
         ["The scratches were etched on top of the frost, proving the scratch occurred from the inside room", "Frost never forms on windows", "The window was double-glazed", "Burglars don't leave scratches"],
         "The scratches were etched on top of the frost, proving the scratch occurred from the inside room",
         "Frost condenses on the indoor humid surface; fresh scratch marks disturbed the indoor frost layer."),
        "ur": ("سردی کی صبح مالک مکان نے دعویٰ کیا کہ چور نے باہر سے کھڑکی کا شیشہ کھرچ کر اندر گھسنے کی کوشش کی۔ انسپکٹر نے فراڈ کیسے پکڑا؟",
         ["کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا", "شیشہ مضبوط تھا", "چور کھرچتا نہیں ہے", "باہر دھوپ تھی"],
         "کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا",
         "کمرے کی اندرونی نمی شیشے پر جمی تھی، اور کھرچ کے نشان اس جمی ہوئی برف کے اوپر اندر کی طرف تھے۔")
    },
    # 268: Wet umbrella in closet
    {
        "en": ("A suspect claims he was asleep in bed during an armed robbery during a sudden evening thunderstorm. The detective inspects the front hall coat closet and arrests him. What was the clue?",
         ["His dripping wet umbrella and damp overcoat hung inside the closet", "His bed was unmade", "His clock was fast", "Mud on the ceiling"],
         "His dripping wet umbrella and damp overcoat hung inside the closet",
         "Dripping rain gear proves the suspect was recently outdoors in the thunderstorm despite his alibi."),
        "ur": ("ملزم نے بیان دیا کہ طوفانی بارش اور ڈکیتی کے وقت وہ بستر میں سو رہا تھا۔ تفتیش کار نے الماری دیکھ کر اسے فوراً گرفتار کر لیا، الماری میں کیا ثبوت تھا؟",
         ["الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا", "الماری میں چوری کے نوٹ تھے", "الماری کھلی تھی", "کپڑے بکھرے تھے"],
         "الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا",
         "الماری میں گیلے کوٹ اور چھتری کی موجودگی نے ثابت کر دیا کہ وہ طوفان کے دوران باہر موجود تھا۔")
    },
    # 269: Snow footprints direction
    {
        "en": ("A mountain cabin has fresh footprints in the snow leading away toward the forest, but none returning. Yet the resident is inside. How did he leave no return tracks?",
         ["He walked backward in his own outgoing footprints", "He flew an airplane", "He wore snowshoes backwards", "He slid on a rope"],
         "He walked backward in his own outgoing footprints",
         "Stepping carefully backward into preexisting footprints obscures the arrival direction."),
        "ur": ("برفباری کے بعد کیبن سے جنگل کی طرف جاتے ہوئے قدموں کے نشانات ہیں مگر واپسی کا کوئی نشان نہیں، پھر بھی آدمی اندر بیٹھا ہے۔ کیسے؟",
         ["وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا", "وہ ہوا میں اڑ کر آیا", "وہ رسی کے سہارے آیا", "برف پگھل گئی تھی"],
         "وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا",
         "اپنے ہی پرانے قدموں کے اوپر دوبارہ پاؤں رکھ کر چلنے سے واپسی کا کوئی نیا نشان نہیں بنتا۔")
    },
    # 270: Left-handed suicide forgery
    {
        "en": ("A business tycoon was found dead with a pistol in his right hand. The coroner immediately suspects murder rather than suicide. What simple fact gave it away?",
         ["The entrance bullet wound was on his left temple, inconsistent with a right-handed shot", "The gun had fingerprints", "The tycoon was wearing a watch", "The room was warm"],
         "The entrance bullet wound was on his left temple, inconsistent with a right-handed shot",
         "Shooting oneself in the opposite temple with an unnatural wrist angle points to staged execution."),
        "ur": ("ایک تاجر کی لاش ملی جس کے دائیں ہاتھ میں پستول تھا مگر ڈاکٹر نے فوری قتل کا شبہ ظاہر کیا۔ کیوں؟",
         ["کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا", "پستول نیا تھا", "تاجر امیر تھا", "کمرے کی کھڑکی کھلی تھی"],
         "کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا",
         "دائیں ہاتھ سے بائیں کنپٹی پر فائر کرنا انسانی جسمانی بناوٹ کے اعتبار سے ناممکن ہوتا ہے۔")
    },
    # 271: Car headlights in fog
    {
        "en": ("Why does turning car headlights to high beam in dense fog severely reduce a driver's forward visibility?",
         ["High-angle light backscatters off water droplets straight into the driver's eyes, creating blinding glare", "Fog absorbs all light", "The bulbs overheat in fog", "Fog bends light downward"],
         "High-angle light backscatters off water droplets straight into the driver's eyes, creating blinding glare",
         "Mie scattering reflects high-beam photons directly back into the driver's line of sight; low beams illuminate pavement beneath."),
        "ur": ("گہری دھند میں گاڑی کی ہیڈ لائٹس کو ہائی بیم (تیز روشنی) پر کرنے سے آگے کا راستہ دکھائی دینا بند کیوں ہو جاتا ہے؟",
         ["پانی کے قطرے تیز روشنی کو منعکس کر کے سیدھا ڈرائیور کی آنکھوں میں چکا چوندھ پیدا کرتے ہیں", "دھند روشنی پی جاتی ہے", "بلب فیوز ہو جاتے ہیں", "دھند روشنی کو نیچے دبا دیتی ہے"],
         "پانی کے قطرے تیز روشنی کو منعکس کر کے سیدھا ڈرائیور کی آنکھوں میں چکا چوندھ پیدا کرتے ہیں",
         "دھند کے قطرے سفید شیشے کی طرح تیز روشنی کو واپس ڈرائیور کی آنکھوں پر مارتے ہیں جس سے اندھا پن پیدا ہوتا ہے۔")
    },
    # 272: Photographer darkroom red light
    {
        "en": ("Why do traditional film darkrooms illuminate workspaces with dim red safety lamps rather than green or white light?",
         ["Black-and-white silver halide photographic emulsion is not sensitive to long red wavelengths", "Red light is cheaper", "Photographers prefer red color", "Red light keeps paper warm"],
         "Black-and-white silver halide photographic emulsion is not sensitive to long red wavelengths",
         "Orthochromatic gelatin emulsions lack photosensitivity to lower-energy red photons, preventing chemical fogging."),
        "ur": ("روایتی فوٹوگرافی کے ڈارک روم میں تصویریں دھوتے وقت لال رنگ کی مدہم بتی کیوں جلائی جاتی ہے؟",
         ["فوٹوگرافک کاغذ اور فلم پر لگا کیمیکل لال رنگ کی روشنی سے خراب نہیں ہوتا", "لال بتی سستی ہوتی ہے", "آنکھوں کو سکون دینے کے لیے", "کاغذ کو گرم رکھنے کے لیے"],
         "فوٹوگرافک کاغذ اور فلم پر لگا کیمیکل لال رنگ کی روشنی سے خراب نہیں ہوتا",
         "سیاہ و سفید فلم سلور ہیلائیڈ سے بنتی ہے جو سرخ رنگ کی طویل لہروں پر کوئی کیمیائی رد عمل نہیں دکھاتی۔")
    },
    # 273: Scuba diver in forest fire
    {
        "en": ("After a massive mountain wildfire, firefighters discover the corpse of a man wearing full scuba diving gear in a burned treetop. What bizarre accident occurred?",
         ["He was scooped up from a lake by a firefighting aerial water tanker scooper plane and dropped on the fire", "He jumped out of a helicopter", "He climbed the tree to dive", "It was a staged stunt"],
         "He was scooped up from a lake by a firefighting aerial water tanker scooper plane and dropped on the fire",
         "High-capacity water scooper aircraft skimming lake reservoirs can inadvertently suction swimmers into cargo tanks."),
        "ur": ("جنگل کی بھیانک آگ بجھانے کے بعد ایک درخت کی شاخوں سے غوطہ خور (اسکوبا ڈائیور) کی لاش برآمد ہوئی، یہ انوکھا واقعہ کیسے ہوا؟",
         ["آگ بجھانے والے جہاز نے جھیل سے پانی بھرتے وقت اسے بھی اٹھا کر آگ پر گرا دیا تھا", "وہ ہیلی کاپٹر سے کودا تھا", "وہ درخت پر چڑھ کر غوطہ لگا رہا تھا", "وہ پیراشوٹ سے اترا تھا"],
         "آگ بجھانے والے جہاز نے جھیل سے پانی بھرتے وقت اسے بھی اٹھا کر آگ پر گرا دیا تھا",
         "پانی بھرنے والے فائرفائٹر طیارے جھیل کی سطح سے پانی کھینچتے ہیں جس میں بدقسمت تیراک بھی آ گیا۔")
    },
    # 274: Ball and bat $1.10
    {
        "en": ("A baseball bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?",
         ["$0.05 (5 cents)", "$0.10 (10 cents)", "$0.01 (1 cent)", "$0.50 (50 cents)"],
         "$0.05 (5 cents)",
         "Bat + Ball = 1.10; Bat = Ball + 1.00; therefore 2*Ball + 1.00 = 1.10, so Ball = $0.05 and Bat = $1.05."),
        "ur": ("ایک بلے اور گیند کی کل قیمت 110 روپے ہے۔ بلا گیند سے 100 روپے زیادہ مہنگا ہے۔ بتائیں گیند کی اصل قیمت کیا ہے؟",
         ["5 روپے", "10 روپے", "1 روپیہ", "15 روپے"],
         "5 روپے",
         "اگر گیند 5 روپے کی ہو تو بلا 105 روپے کا ہوگا (100 روپے مہنگا)، دونوں مل کر 110 روپے بنیں گے۔")
    },
    # 275: Lily pads doubling
    {
        "en": ("A patch of water lily pads in a pond doubles in surface area every day. If it covers the entire pond in 48 days, on what day does it cover exactly half the pond?",
         ["Day 47", "Day 24", "Day 12", "Day 40"],
         "Day 47",
         "Since it doubles daily, the pond was half-covered the day immediately preceding full coverage (Day 48 - 1 = Day 47)."),
        "ur": ("جھیل میں کنول کے پتے روزانہ دگنے رقبے پر پھیلتے ہیں۔ اگر 48 ویں دن پوری جھیل پتوں سے بھر جاتی ہے تو جھیل آدھی کس دن بھری تھی؟",
         ["47 ویں دن", "24 ویں دن", "12 ویں دن", "46 ویں دن"],
         "47 ویں دن",
         "کیونکہ رقبہ ہر روز دگنا ہوتا ہے، اس لیے 48 ویں دن سے ٹھیک ایک دن پہلے یعنی 47 ویں دن جھیل آدھی بھری تھی۔")
    },
    # 276: Cutting log into pieces
    {
        "en": ("If it takes a carpenter 6 minutes to saw a timber log into 3 equal pieces, how many minutes will it take him to saw an identical log into 6 pieces?",
         ["15 minutes", "12 minutes", "18 minutes", "10 minutes"],
         "15 minutes",
         "Cutting into 3 pieces requires 2 saw cuts (6 min / 2 = 3 min per cut). Cutting into 6 pieces requires 5 cuts (5 * 3 = 15 minutes)."),
        "ur": ("ایک لکڑی کے لٹھے کے 3 ٹکڑے کرنے میں بڑھئی کو 6 منٹ لگتے ہیں۔ اسی طرح کے لٹھے کے 6 ٹکڑے کرنے میں اسے کتنے منٹ لگیں گے؟",
         ["15 منٹ", "12 منٹ", "18 منٹ", "10 منٹ"],
         "15 منٹ",
         "3 ٹکڑوں کے لیے 2 کٹ لگانے پڑتے ہیں یعنی فی کٹ 3 منٹ۔ 6 ٹکڑوں کے لیے 5 کٹ لگیں گے جس میں 15 منٹ لگیں گے۔")
    },
    # 277: Snail climbing well
    {
        "en": ("A snail at the bottom of a 30-foot stone well climbs up 3 feet each day, but slips down 2 feet each night. On which day does the snail reach the top?",
         ["Day 28", "Day 30", "Day 29", "Day 27"],
         "Day 28",
         "At the end of day 27, it reaches 27 feet. On day 28, it climbs 3 feet to reach 30 feet and exits before slipping."),
        "ur": ("30 فٹ گہرے کنوئیں سے ایک گھونگھا دن میں 3 فٹ چڑھتا ہے اور رات کو سوتے میں 2 فٹ پھسل جاتا ہے۔ وہ کس دن کنوئیں سے باہر نکل آئے گا؟",
         ["28 ویں دن", "30 ویں دن", "29 ویں دن", "27 ویں دن"],
         "28 ویں دن",
         "27 ویں دن کے اختتام پر وہ 27 فٹ پر پہنچے گا، اور 28 ویں دن کی چھلانگ سے سیدھا 30 فٹ پر پہنچ کر باہر آ جائے گا اور پھسلے گا نہیں۔")
    },
    # 278: Farmer 17 sheep
    {
        "en": ("A sheep farmer has 17 sheep grazing in a field. A sudden epidemic strikes and all but 9 sheep die. How many sheep does the farmer have remaining?",
         ["9 sheep", "8 sheep", "0 sheep", "17 sheep"],
         "9 sheep",
         "'All but 9' explicitly means that exactly 9 sheep survived the epidemic."),
        "ur": ("ایک کسان کے پاس 17 بھیڑیں تھیں۔ اچانک بیماری سے 9 کے علاوہ باقی سب مر گئیں۔ کسان کے پاس اب کتنی بھیڑیں زندہ ہیں؟",
         ["9 بھیڑیں", "8 بھیڑیں", "کوئی بھی نہیں", "17 بھیڑیں"],
         "9 بھیڑیں",
         "جملے میں صاف کہا گیا ہے کہ '9 کے علاوہ سب مر گئیں'، یعنی 9 بھیڑیں اب بھی زندہ موجود ہیں۔")
    },
    # 279: Runner overtaking second place
    {
        "en": ("You are sprinting in a marathon and pass the runner who is currently in second place. What position are you in now?",
         ["Second place", "First place", "Third place", "Fourth place"],
         "Second place",
         "By passing the runner in second place, you take over their spot in second place, while the leader remains ahead."),
        "ur": ("دوڑ کے مقابلے میں آپ دوسرے نمبر پر دوڑنے والے کھلاڑی سے آگے نکل جاتے ہیں۔ اب آپ کس پوزیشن پر ہیں؟",
         ["دوسرے نمبر پر", "پہلے نمبر پر", "تیسرے نمبر پر", "آخری نمبر پر"],
         "دوسرے نمبر پر",
         "دوسرے نمبر والے کو پیچھے چھوڑنے پر آپ خود دوسرے نمبر پر آ جاتے ہیں جبکہ پہلا اب بھی آگے ہے۔")
    },
    # 280: Doctor prescription pills
    {
        "en": ("A physician gives you three medicine pills and instructs you to take one pill every 30 minutes. How many minutes will the pills last?",
         ["60 minutes (1 hour)", "90 minutes", "30 minutes", "120 minutes"],
         "60 minutes (1 hour)",
         "You swallow pill 1 at minute 0, pill 2 at minute 30, and pill 3 at minute 60; total elapsed time is 60 minutes."),
        "ur": ("ڈاکٹر آپ کو 3 گولیاں دیتا ہے اور کہتا ہے کہ ہر آدھے گھنٹے بعد ایک گولی کھاؤ۔ یہ گولیاں کتنے وقت میں ختم ہوں گی؟",
         ["60 منٹ (ایک گھنٹہ)", "90 منٹ", "30 منٹ", "120 منٹ"],
         "60 منٹ (ایک گھنٹہ)",
         "پہلی گولی فورا 0 منٹ پر، دوسری 30 منٹ پر اور تیسری 60 منٹ پر لی جائے گی، کل وقت 60 منٹ بنے گا۔")
    },
    # 281: Grandfather clock chiming
    {
        "en": ("A pendulum grandfather clock takes 5 seconds to chime 6 o'clock (6 strikes). How many seconds will it take to chime 12 o'clock (12 strikes)?",
         ["11 seconds", "10 seconds", "12 seconds", "9 seconds"],
         "11 seconds",
         "6 strikes have 5 intervals between them (5 seconds / 5 = 1 sec per interval). 12 strikes have 11 intervals (11 * 1 = 11 seconds)."),
        "ur": ("ایک کلاک کو 6 بجے 6 بار گھنٹیاں بجانے میں 5 سیکنڈ لگتے ہیں۔ 12 بجے 12 بار گھنٹیاں بجانے میں اسے کتنے سیکنڈ لگیں گے؟",
         ["11 سیکنڈ", "10 سیکنڈ", "12 سیکنڈ", "14 سیکنڈ"],
         "11 سیکنڈ",
         "6 گھنٹیوں کے درمیان 5 وقفے ہوتے ہیں (فی وقفہ 1 سیکنڈ)۔ 12 گھنٹیوں کے درمیان 11 وقفے ہوں گے جو 11 سیکنڈ لیں گے۔")
    },
    # 282: Bee between approaching trains
    {
        "en": ("Two trains 100 miles apart travel toward each other at 50 mph each. A bee flies back and forth between them at 75 mph until they collide. How many miles does the bee fly?",
         ["75 miles", "100 miles", "50 miles", "150 miles"],
         "75 miles",
         "Relative approach speed is 100 mph, so the trains collide in 1 hour (100 / 100). In 1 hour, the bee flies 75 miles (75 mph * 1 hr)."),
        "ur": ("دو ٹرینیں 100 میل کی دوری سے 50 میل فی گھنٹہ کی رفتار سے آمنے سامنے آ رہی ہیں۔ ایک مکھی 75 میل کی رفتار سے ان کے درمیان اڑتی رہتی ہے۔ ٹکرانے تک مکھی کتنا فاصلہ طے کرے گی؟",
         ["75 میل", "100 میل", "50 میل", "125 میل"],
         "75 میل",
         "دونوں ٹرینیں 1 گھنٹے میں ملیں گی (50+50=100)۔ اس ایک گھنٹے میں 75 میل فی گھنٹہ کی مکھی کل 75 میل اڑے گی۔")
    },
    # 283: Envy-free cake cutting
    {
        "en": ("How can two siblings divide a frosted birthday cake fairly so that neither believes the other received the larger slice?",
         ["One sibling cuts the cake into two pieces, and the other sibling chooses their piece first ('I cut, you choose')", "Weigh each piece on a postal scale", "Have a parent cut it blindfolded", "Eat the entire cake together"],
         "One sibling cuts the cake into two pieces, and the other sibling chooses their piece first ('I cut, you choose')",
         "The cutter is motivated to make both halves as identical as possible, while the chooser guarantees their preferred slice."),
        "ur": ("دو بھائی کیک کو آپس میں کیسے تقسیم کریں کہ دونوں میں سے کسی کو یہ شکوہ نہ ہو کہ دوسرے کو بڑا ٹکڑا ملا ہے؟",
         ["ایک بھائی کیک کے دو ٹکڑے کرے اور دوسرا بھائی اپنی مرضی کا ٹکڑا پہلے اٹھائے (ایک کاٹے، دوسرا چنے)", "ترازو پر تول کر", "آنکھیں بند کر کے", "دونوں مل کر کھائیں"],
         "ایک بھائی کیک کے دو ٹکڑے کرے اور دوسرا بھائی اپنی مرضی کا ٹکڑا پہلے اٹھائے (ایک کاٹے، دوسرا چنے)",
         "کاٹنے والا پوری کوشش سے برابر کاٹے گا اور اٹھانے والا اپنی پسند کا بڑا حصہ چن کر مطمئن رہے گا۔")
    },
    # 284: Russian roulette probability
    {
        "en": ("In Russian roulette with a 6-chamber revolver loaded with 2 adjacent bullets, player 1 pulls the trigger on an empty chamber. Should player 2 spin the cylinder or pull the trigger directly?",
         ["Pull the trigger directly without spinning (1/4 chance of firing vs 2/6 = 1/3 if spun)", "Spin the cylinder to scramble the chambers", "It makes no mathematical difference", "Remove the bullets"],
         "Pull the trigger directly without spinning (1/4 chance of firing vs 2/6 = 1/3 if spun)",
         "Four empty chambers remain in sequence; of the 4 chambers following an empty, only 1 leads to a bullet (25% vs 33%)."),
        "ur": ("چھ خانوں والی ریوالور میں ساتھ ساتھ دو گولیاں ہیں۔ پہلے شخص نے فائر کیا تو خالی چیمبر نکلا۔ اب دوسرے کھلاڑی کے لیے سلنڈر گھمانا بہتر ہے یا بنا گھمائے فائر کرنا؟",
         ["بنا گھمائے فائر کرنا زیادہ محفوظ ہے (خطرہ 25% جبکہ گھمانے پر 33% ہوگا)", "سلنڈر گھما دینا", "دونوں میں بالکل برابر خطرہ ہے", "گولیاں نکال لینا"],
         "بنا گھمائے فائر کرنا زیادہ محفوظ ہے (خطرہ 25% جبکہ گھمانے پر 33% ہوگا)",
         "کیونکہ گولیاں جڑی ہوئی تھیں، اس لیے خالی نکلنے کے بعد اگلا چیمبر خالی ہونے کا امکان 75 فیصد ہے۔")
    },
    # 285: Siphon water tube
    {
        "en": ("How does a flexible plastic siphon hose drain water up and out of an aquarium without an electric motor?",
         ["Atmospheric pressure and liquid cohesion pull water through the crest toward the lower discharge outlet", "Capillary action", "Water boils inside tube", "Air bubbles push it"],
         "Atmospheric pressure and liquid cohesion pull water through the crest toward the lower discharge outlet",
         "The weight of water in the longer discharge leg creates a pressure deficit at the summit, pulling fluid continuously."),
        "ur": ("بغیر کسی موٹر کے ربڑ کے پائپ (سائفن) سے ایکویریم کا پانی اوپر چڑھا کر باہر بالٹی میں کیسے نکلتا ہے؟",
         ["پانی کے سالماتی ربط اور بیرونی نچلے سرے کے کشش ثقل کے دباؤ کی وجہ سے", "کیپلیری ایکشن سے", "پائپ کے اندر ہوا بننے سے", "پانی ابلنے سے"],
         "پانی کے سالماتی ربط اور بیرونی نچلے سرے کے کشش ثقل کے دباؤ کی وجہ سے",
         "پائپ کا نچلا سرا جب پانی کی سطح سے نیچا ہو تو کشش ثقل کا بہاؤ پانی کو اوپر کھینچ کر نکالتا رہتا ہے۔")
    },
    # 286: Uphill bicycle gears
    {
        "en": ("Why does shifting a bicycle into a small front chainring and a large rear cog make pedaling up a steep hill effortless?",
         ["It trades mechanical pedaling distance for increased axle torque leverage", "It makes the bicycle lighter", "It speeds up wheel rotation", "It reduces gravity"],
         "It trades mechanical pedaling distance for increased axle torque leverage",
         "Mechanical advantage increases torque at the rear wheel hub at the expense of higher cadence revolutions."),
        "ur": ("سائیکل پر اونچی چڑھائی چڑھتے وقت آگے کا چھوٹا گیئر اور پیچھے کا بڑا گیئر لگانے سے پیڈل مارنا آسان کیوں ہو جاتا ہے؟",
         ["یہ رفتار کی قربانی دے کر پہیے کو گھمانے کا مکینیکل ٹارک (زور) بڑھا دیتا ہے", "سائیکل کا وزن کم ہو جاتا ہے", "ہوا مدد دیتی ہے", "کشش ثقل کم ہو جاتی ہے"],
         "یہ رفتار کی قربانی دے کر پہیے کو گھمانے کا مکینیکل ٹارک (زور) بڑھا دیتا ہے",
         "بڑے گیئر کی وجہ سے پیڈل کا زور کئی گنا بڑھ کر پہیے تک پہنچتا ہے جس سے چڑھائی آسان ہو جاتی ہے۔")
    },
    # 287: Sailboat tacking against wind
    {
        "en": ("How can a modern triangular-rigged sailing boat navigate forward in a zig-zag trajectory against an opposing headwind?",
         ["The curved sail generates aerodynamic lift like an airplane wing, combined with keel water resistance", "Pushing against ocean waves", "Rowing under deck", "Wind turns around the hull"],
         "The curved sail generates aerodynamic lift like an airplane wing, combined with keel water resistance",
         "Sails act as vertical airfoils producing forward lift vectors, while the underwater keel prevents lateral leeway drift."),
        "ur": ("بادبانی کشتی مخالف سمت سے آنے والی ہوا کے باوجود ٹیڑھے میڑھے (زگ زیگ) راستے پر آگے کیسے بڑھتی ہے؟",
         ["کشتی کا بادبان ہوائی جہاز کے پر کی طرح لفٹ پیدا کرتا ہے اور نیچے کا کِیل پھسلنے سے روکتا ہے", "پانی کی لہروں پر تیر کر", "اندر چپو چلا کر", "ہوا کا رخ بدل کر"],
         "کشتی کا بادبان ہوائی جہاز کے پر کی طرح لفٹ پیدا کرتا ہے اور نیچے کا کِیل پھسلنے سے روکتا ہے",
         "بادبان سے پیدا ہونے والا ایروڈائنامک پریشر اور نیچے کی وزنی پتی مل کر کشتی کو مخالف ہوا میں آگے دھکیلتے ہیں۔")
    },
    # 288: Fresh vs salt water ship draft
    {
        "en": ("When a heavily loaded cargo container vessel sails from the Atlantic Ocean into a freshwater river port, what happens to its waterline draft?",
         ["The ship sinks slightly deeper into the water because freshwater has lower buoyant density", "The ship rises higher", "The draft remains exactly identical", "The ship capsizes"],
         "The ship sinks slightly deeper into the water because freshwater has lower buoyant density",
         "Less dense fresh water requires the displacement of a greater volume to equal the vessel's displacement tonnage."),
        "ur": ("جب سمندر سے کوئی بھاری مال بردار بحری جہاز میٹھے پانی کے دریا کی بندرگاہ میں داخل ہوتا ہے تو اس پر کیا اثر پڑتا ہے؟",
         ["جہاز پانی میں ذرا زیادہ گہرائی میں دھنس جاتا ہے کیونکہ میٹھے پانی کی کثافت کم ہوتی ہے", "جہاز اوپر اٹھ جاتا ہے", "کوئی فرق نہیں پڑتا", "جہاز الٹ جاتا ہے"],
         "جہاز پانی میں ذرا زیادہ گہرائی میں دھنس جاتا ہے کیونکہ میٹھے پانی کی کثافت کم ہوتی ہے",
         "سمندر کا نمکین پانی وزنی ہوتا ہے جو جہاز کو زیادہ اچھالتا ہے، میٹھے پانی میں جہاز نیچے بیٹھتا ہے۔")
    },
    # 289: Highway bridge expansion joints
    {
        "en": ("Why are jagged steel expansion comb joints built into the concrete roadway decks of long highway viaducts?",
         ["To accommodate thermal expansion and contraction cycles across winter and summer without buckling", "To channel tire rainwater", "To slow down speeding traffic", "To prevent bridge icing"],
         "To accommodate thermal expansion and contraction cycles across winter and summer without buckling",
         "Temperature differentials cause massive concrete spans to expand and contract by several inches annually."),
        "ur": ("ہائی وے کے لمبے کنکریٹ کے پلوں کے درمیان دندانے دار لوہے کے جوڑ (ایکسپینشن جوائنٹس) کیوں چھوڑے جاتے ہیں؟",
         ["تاکہ گرمی اور سردی میں پل کے پھیلنے اور سکڑنے سے سڑک ٹوٹنے اور ٹیڑھی ہونے سے بچ سکے", "بارش کا پانی نکالنے کے لیے", "گاڑیوں کی رفتار کم کرنے کے لیے", "پل کو ہلکا رکھنے کے لیے"],
         "تاکہ گرمی اور سردی میں پل کے پھیلنے اور سکڑنے سے سڑک ٹوٹنے اور ٹیڑھی ہونے سے بچ سکے",
         "شدید گرمی میں کنکریٹ پھیلتا ہے اور سردی میں سکڑتا ہے، یہ خلا پل کو محفوظ لچک فراہم کرتا ہے۔")
    },
    # 290: Canyon echo distance
    {
        "en": ("If you shout 'Hello!' toward a sheer granite canyon wall and hear the distinct echo return 2.0 seconds later, roughly how far away is the cliff? (Speed of sound ~ 340 m/s)",
         ["340 meters", "680 meters", "170 meters", "500 meters"],
         "340 meters",
         "The sound traveled to the cliff and back in 2.0 seconds (1.0 second each way). Distance = 340 m/s * 1.0 s = 340 meters."),
        "ur": ("اگر آپ وادی میں آواز لگائیں اور 2 سیکنڈ بعد آپ کو اپنی بازگشت سنائی دے، تو سامنے کی چٹان کتنی دور ہے؟ (آواز کی رفتار 340 میٹر فی سیکنڈ)",
         ["340 میٹر", "680 میٹر", "170 میٹر", "500 میٹر"],
         "340 میٹر",
         "آواز کو جانے اور واپس آنے میں کل 2 سیکنڈ لگے یعنی جانے میں 1 سیکنڈ لگا۔ فاصلہ = 340 ضرب 1 = 340 میٹر۔")
    }
]

print(f"Catalog Normal Part 1 loaded base items: {len(ITEMS)}")
