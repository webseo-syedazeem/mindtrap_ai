# -*- coding: utf-8 -*-
"""
Normal Group 1: Forensic Mysteries & Detective Deductions (Items 251 - 350: 100 items)
Zero repeated POV, zero loops, completely distinct forensic scenarios.
"""

ITEMS = [
    # 251: Three light switches
    {
        "en": ("Three light switches outside a closed basement control three incandescent bulbs inside. You can only enter the basement once. How do you identify which switch controls which bulb?",
         ["Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3", "Turn all three on", "Flip switch 1 repeatedly", "Look under the door"],
         "Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and enter: lit bulb is 2, warm bulb is 1, cold bulb is 3",
         "Incandescent bulbs emit thermal heat; feeling the unlit warm bulb identifies the first switch."),
        "ur": ("بند تہہ خانے کے باہر تین سوئچ اندر کے تین بلب کنٹرول کرتے ہیں۔ آپ صرف ایک بار اندر جا سکتے ہیں۔ کس سوئچ سے کون سا بلب جلتا ہے کیسے معلوم کریں گے؟",
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
         ["Start both; when 4-min ends, invert it; when 7-min ends (1 min left in 4-min), invert 7-min; when 4-min ends (8 min), invert 7-min to reach 9", "Run 7-minute twice", "Guess the middle of 7-min", "Run 4-minute twice"],
         "Start both; when 4-min ends, invert it; when 7-min ends (1 min left in 4-min), invert 7-min; when 4-min ends (8 min), invert 7-min to reach 9",
         "Staggering sand flow intervals isolates single-minute increments to total 9 minutes."),
        "ur": ("آپ کے پاس ایک 7 منٹ اور ایک 4 منٹ والی ریت کی گھڑیاں ہیں۔ بالکل 9 منٹ کا وقت کیسے ناپیں گے؟",
         ["دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے", "7 منٹ والی دو بار چلا کر", "اندازہ لگا کر", "4 منٹ والی دو بار چلا کر"],
         "دونوں ساتھ الٹیں، 4 منٹ ختم ہونے پر اسے دوبارہ الٹیں، 7 منٹ ختم ہونے پر 4 والے میں 1 منٹ بچے گا، اس سے حساب کر کے 9 منٹ پورے ہوں گے",
         "دونوں ریت کی گھڑیوں کے فرق کو استعمال کر کے بالکل درست نو منٹ ناپے جا سکتے ہیں۔")
    },
    # 254: 12 coins balance scale
    {
        "en": ("Among 12 gold coins, 1 is counterfeit with a slightly different weight (heavier or lighter). What is the minimum weighings on a balance scale to identify it?",
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
        "en": ("In a school corridor with 100 closed lockers, 100 students pass through. Student 1 opens all. Student 2 closes every 2nd. Student 3 toggles every 3rd, up to student 100. Which lockers remain open?",
         ["Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "All prime numbered lockers", "All even numbered lockers", "All odd numbered lockers"],
         "Only perfect square numbered lockers (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
         "Only perfect squares have an odd number of factors; all other numbers have pairs of factors resulting in being closed."),
        "ur": ("اسکول کی راہداری میں 100 بند لاکرز پر 100 طلبہ باری باری گزرتے ہیں۔ پہلا سب کھولتا ہے، دوسرا ہر دوسرا بند کرتا ہے، تیسرا ہر تیسرا بدلتا ہے۔ آخر میں کون سے لاکرز کھلے رہیں گے؟",
         ["صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)", "تمام طاق اعداد والے", "تمام جفت اعداد والے", "تمام پرائم اعداد والے"],
         "صرف مکمل مربع اعداد والے لاکرز (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)",
         "صرف مکمل مربع اعداد کے فیکٹرز طاق تعداد میں ہوتے ہیں جس کی وجہ سے وہ کھلے رہ جاتے ہیں۔")
    },
    # 259: Three mislabeled fruit boxes
    {
        "en": ("Three wooden crates are labeled Apples, Oranges, and Mixed (Apples & Oranges). All three labels are guaranteed incorrect. You can pick 1 fruit from 1 crate without looking inside. Which crate do you pick from to label all correctly?",
         ["Pick from the crate labeled Mixed", "Pick from the crate labeled Apples", "Pick from the crate labeled Oranges", "Cannot be solved with 1 pick"],
         "Pick from the crate labeled Mixed",
         "Since the Mixed label is wrong, picking 1 fruit identifies that entire box; the remaining two mislabeled boxes are deduced uniquely."),
        "ur": ("تین پیٹیوں پر 'سیب'، 'مالٹے' اور 'مکس' کے لیبل لگے ہیں مگر تینوں لیبل غلط ہیں۔ آپ صرف ایک پیٹی میں سے بنا دیکھے ایک پھل نکال سکتے ہیں۔ تمام پیٹیاں درست کیسے کریں گے؟",
         ["جس پیٹی پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر", "سیب والی پیٹی سے", "مالٹے والی پیٹی سے", "ایک پھل سے ممکن نہیں"],
         "جس پیٹی پر 'مکس' کا لیبل لگا ہو اس میں سے ایک پھل نکال کر",
         "کیونکہ مکس کا لیبل غلط ہے، اس میں سے جو پھل نکلے گا وہ پوری پیٹی وہی ہوگی، اور باقی دو پیٹیاں خود بخود سیدھی ہو جائیں گی۔")
    },
    # 260: Single-elimination tennis tournament
    {
        "en": ("In an international tennis tournament featuring 64 players under single-elimination rules, how many total matches must be played to crown the champion?",
         ["63 matches", "64 matches", "32 matches", "128 matches"],
         "63 matches",
         "Each match eliminates exactly one loser; to eliminate 63 players requires exactly 63 matches."),
        "ur": ("ایک بین الاقوامی ناک آؤٹ ٹینس ٹورنامنٹ میں 64 کھلاڑی حصہ لے رہے ہیں۔ چیمپیئن کا فیصلہ کرنے کے لیے کل کتنے میچ کھیلنا پڑیں گے؟",
         ["63 میچ", "64 میچ", "32 میچ", "128 میچ"],
         "63 میچ",
         "ہر میچ میں ایک کھلاڑی ہار کر باہر ہوتا ہے، 63 کھلاڑیوں کو باہر کرنے کے لیے ٹھیک 63 میچ درکار ہیں۔")
    },
    # 261: Dinner party handshakes
    {
        "en": ("At an executive dinner party of 10 people, everyone shakes hands with everyone else exactly once. How many total handshakes occur across the evening?",
         ["45 handshakes", "90 handshakes", "50 handshakes", "100 handshakes"],
         "45 handshakes",
         "Combinations of 10 people taken 2 at a time: n*(n-1)/2 = 10 * 9 / 2 = 45."),
        "ur": ("ایک پروقار عشائیے میں 10 لوگ موجود ہیں اور ہر شخص دوسرے ہر شخص سے ایک بار مصافحہ (ہاتھ ملاتا) کرتا ہے۔ کل کتنے مصافحے ہوں گے؟",
         ["45 مصافحے", "90 مصافحے", "50 مصافحے", "100 مصافحے"],
         "45 مصافحے",
         "مصافحوں کا فارمولا n*(n-1)/2 ہوتا ہے، یعنی 10 ضرب 9 تقسیم 2 برابر ہے 45۔")
    },
    # 262: Monty Hall door switch
    {
        "en": ("On a television stage, you select Door 1 out of 3. The host opens Door 3, revealing a goat, and offers to switch to Door 2. What gives you the highest mathematical probability of winning the sports car?",
         ["Switching to Door 2 (2/3 chance of winning)", "Staying with Door 1 (2/3 chance)", "It is strictly 50/50, no difference", "Flipping a coin"],
         "Switching to Door 2 (2/3 chance of winning)",
         "Your initial pick had a 1/3 chance; the unopened remaining door inherits the entire 2/3 probability of the other two doors."),
        "ur": ("ٹی وی شو میں تین میں سے ایک دروازے کے پیچھے اسپورٹس کار ہے۔ آپ نے دروازہ 1 چنا، میزبان نے دروازہ 3 کھولا جہاں بکری نکلی۔ کار جیتنے کا زیادہ امکان کس میں ہے؟",
         ["دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)", "دروازہ 1 پر ہی رہنے سے", "دونوں میں بالکل برابر 50/50 چانس ہے", "کوئی فرق نہیں پڑتا"],
         "دروازہ 2 پر سوئچ کرنے سے (2/3 امکان)",
         "پہلے انتخاب کا امکان صرف 1/3 تھا، جبکہ دوسرے دروازے کے پاس اب 2/3 کا زبردست امکان موجود ہے۔")
    },
    # 263: Elevator short man
    {
        "en": ("A gentleman lives on the 15th floor of an apartment. Every morning he rides the elevator all the way to ground. Returning home, he rides to the 10th floor and walks up 5 flights of stairs, unless it rains. Why?",
         ["He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days", "He likes exercising on dry days", "The elevator is broken above floor 10", "He visits a friend on floor 10"],
         "He is too short to reach the 15th floor button, but uses an umbrella to press it on rainy days",
         "The height of button 10 is the maximum reach of his arm; an umbrella gives him extra physical reach."),
        "ur": ("ایک شخص اپارٹمنٹ کی پندرہویں منزل پر رہتا ہے۔ وہ صبح لفٹ سے نیچے جاتا ہے مگر واپسی پر دسویں منزل پر اتر کر پانچ منزلیں پیدل چڑھتا ہے، سوائے بارش کے دن کے۔ کیوں؟",
         ["کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے", "وہ ورزش کا شوقین ہے", "لفٹ اوپر خراب ہوتی ہے", "اس کا دوست دسویں منزل پر ہے"],
         "کیونکہ اس کا قد چھوٹا ہے اور ہاتھ 10 ویں بٹن تک پہنچتا ہے، بارش میں وہ چھتری سے 15 واں بٹن دباتا ہے",
         "چھوٹے قد کی وجہ سے وہ اوپر کا بٹن ہاتھ سے نہیں دبا پاتا تھا، چھتری کا دستہ اسے پہنچا دیتا تھا۔")
    },
    # 264: Hotel Monopoly bankruptcy
    {
        "en": ("A man pushes his vehicle token up to a luxury red hotel and instantly realizes he is completely bankrupt. What was taking place?",
         ["Playing the board game Monopoly with a car token", "His real car engine blew up", "He lost his hotel reservation", "He was robbed by valets"],
         "Playing the board game Monopoly with a car token",
         "In Monopoly, landing a miniature car token on an opponent's hotel property incurs a ruinous rent fine."),
        "ur": ("ایک شخص نے اپنی چھوٹی کار کو ہوٹل کے سامنے رکھا اور فورا سمجھ گیا کہ وہ کنگال ہو چکا ہے، وہ کیا کر رہا تھا؟",
         ["وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا", "اس کی اصل کار خراب ہو گئی تھی", "ہوٹل کا بل بہت زیادہ تھا", "اس کے پیسے چوری ہو گئے تھے"],
         "وہ مونوپولی (Monopoly) کا بورڈ گیم کار والے ٹوکن سے کھیل رہا تھا",
         "مونوپولی کھیل میں کار کا مہرہ حریف کے ہوٹل پر پہنچنے کا مطلب دیوالیہ ہو جانا ہے۔")
    },
    # 265: Poisoned iced tea drinkers
    {
        "en": ("Two travelers order chilled iced tea glasses at a desert diner. Mark gulps down five glasses quickly in two minutes; Dan sips one glass slowly over an hour. Dan dies of cyanide poisoning, but Mark survives unharmed. Why?",
         ["The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's", "Mark had developed immunity to poison", "Dan's straw was laced with poison", "Mark was given a different pitcher"],
         "The poison was frozen inside the ice cubes, which melted in Dan's glass but not in Mark's",
         "Drinking fast before the ice melted prevented Mark from ingesting the toxin released upon thawing."),
        "ur": ("صحرائی ریستوران میں دو مسافروں نے ٹھنڈا شربت پیا۔ ایک نے جلدی جلدی 5 گلاس پی لیے جبکہ دوسرے نے ایک گھنٹے میں ایک گلاس آہستہ پیا۔ آہستہ پینے والا زہر سے مر گیا مگر دوسرا بچ گیا۔ کیوں؟",
         ["زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا", "پہلے دوست میں زہر کی قوت مدافعت تھی", "اسٹرا میں زہر لگا تھا", "دوسرے کا شربت الگ تھا"],
         "زہر برف کے ٹکڑوں کے اندر جما ہوا تھا جو آہستہ پینے والے کے گلاس میں پگھل گیا",
         "جلدی پینے والے کے وقت برف پگھلی نہیں تھی، آہستہ پینے والے کی برف گھل کر زہر شربت میں شامل ہو گیا۔")
    },
    # 266: Tape recorder suicide alibi
    {
        "en": ("A detective investigates an alleged suicide in a study. On the mahogany desk is a cassette tape recorder. Pressing play, police hear: 'I cannot bear this life anymore', followed by a gunshot. The detective immediately declares it a homicide. Why?",
         ["The cassette tape was rewound back to the beginning, which a dead person cannot do", "The gunshot sounded too loud", "The voice was synthesized", "The tape was blank"],
         "The cassette tape was rewound back to the beginning, which a dead person cannot do",
         "After shooting oneself, a deceased individual cannot press the rewind button on a mechanical cassette player."),
        "ur": ("ایک کمرے میں خودکشی کی اطلاع پر پولیس پہنچی۔ میز پر ٹیپ ریکارڈر تھا، پلے کرنے پر گولی چلنے کی آواز آئی۔ تفتیشی افسر نے فورا اسے قتل قرار دیا۔ کیوں؟",
         ["کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا", "گولی کی آواز بہت دھیمی تھی", "کیسٹ پرانی تھی", "کمرہ بند تھا"],
         "کیونکہ کیسٹ ریوائنڈ (شروع پر واپس) کی ہوئی تھی جو مرنے والا خود نہیں کر سکتا تھا",
         "گولی لگنے کے بعد مرنے والا شخص خود کیسٹ کا بٹن دبا کر اسے واپس شروع پر نہیں لا سکتا۔")
    },
    # 267: Window frost inside vs outside
    {
        "en": ("On a freezing winter dawn, a shopkeeper claims a burglar scratched the display glass from the outside to break in. The detective examines frost condensation on the inside pane and disproves the story. Why?",
         ["The scratches were etched on top of the frost layer, proving the scratch occurred from inside the shop", "Frost never forms on windows", "The window was double-glazed", "Burglars don't leave scratches"],
         "The scratches were etched on top of the frost layer, proving the scratch occurred from inside the shop",
         "Frost condenses on the indoor humid surface; fresh scratch marks disturbed the indoor frost layer."),
        "ur": ("دکان دار نے دعویٰ کیا کہ چور نے رات کو باہر سے کھڑکی کا شیشہ کھرچ کر اندر گھسنے کی کوشش کی۔ انسپکٹر نے فراڈ کیسے پکڑا؟",
         ["کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا", "شیشہ مضبوط تھا", "چور کھرچتا نہیں ہے", "باہر دھوپ تھی"],
         "کھڑکی کے اندر جمی ہوئی برف پر کھرچنے کے نشانات تھے جس سے ثابت ہوا کہ یہ اندر سے کیا گیا تھا",
         "کمرے کی اندرونی نمی شیشے پر جمی تھی، اور کھرچ کے نشان اس جمی ہوئی برف کے اوپر اندر کی طرف تھے۔")
    },
    # 268: Wet umbrella in closet
    {
        "en": ("A suspect insists he was asleep in bed throughout an armed robbery during a sudden evening thunderstorm. The detective inspects the foyer wardrobe and promptly arrests him. What was the incriminating clue?",
         ["His dripping wet umbrella and damp wool coat hung inside the dark wardrobe", "His bed was unmade", "His clock was fast", "Mud on the ceiling"],
         "His dripping wet umbrella and damp wool coat hung inside the dark wardrobe",
         "Dripping rain gear proves the suspect was recently outdoors in the thunderstorm despite his alibi."),
        "ur": ("ملزم نے قسم کھائی کہ طوفانی بارش اور واردات کے وقت وہ بستر میں گہری نیند سو رہا تھا۔ تفتیش کار نے الماری دیکھ کر اسے فوراً گرفتار کر لیا، الماری میں کیا ثبوت تھا؟",
         ["الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا", "الماری میں چوری کے نوٹ تھے", "الماری کھلی تھی", "کپڑے بکھرے تھے"],
         "الماری میں بارش سے ٹپکتی ہوئی بھیگی چھتری اور گیلا کوٹ لٹکا ہوا تھا",
         "الماری میں گیلے کوٹ اور چھتری کی موجودگی نے ثابت کر دیا کہ وہ طوفان کے دوران باہر موجود تھا۔")
    },
    # 269: Snow footprints direction
    {
        "en": ("A forest cabin shows solitary footprints in the fresh morning snow leading away into the woods, with zero tracks returning. Yet the solitary cabin occupant is resting inside by the fireplace. How did he return without leaving fresh tracks?",
         ["He walked backward stepping carefully into his own outgoing footprints", "He flew an airplane", "He wore snowshoes backwards", "He slid on a rope"],
         "He walked backward stepping carefully into his own outgoing footprints",
         "Stepping carefully backward into preexisting footprints obscures the arrival direction."),
        "ur": ("جنگلی کیبن سے باہر کی طرف جاتے ہوئے تازہ برف میں پاؤں کے نشانات ہیں مگر واپسی کا کوئی نشان نہیں، پھر بھی شکاری اندر بیٹھا ہے۔ کیسے؟",
         ["وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا", "وہ ہوا میں اڑ کر آیا", "وہ رسی کے سہارے آیا", "برف پگھل گئی تھی"],
         "وہ واپسی پر الٹے پاؤں اپنے ہی پرانے نشانات پر پاؤں رکھ کر واپس آیا تھا",
         "اپنے ہی پرانے قدموں کے اوپر دوبارہ پاؤں رکھ کر چلنے سے واپسی کا کوئی نیا نشان نہیں بنتا۔")
    },
    # 270: Left-handed suicide forgery
    {
        "en": ("A wealthy financier was discovered dead in his library with a revolver gripped in his right hand. The forensic pathologist immediately ruled out suicide. What physical finding gave it away?",
         ["The entrance gunshot wound was on his left temple, mechanically impossible for a right-handed self-inflicted shot", "The gun had fingerprints", "The tycoon was wearing a watch", "The room was warm"],
         "The entrance gunshot wound was on his left temple, mechanically impossible for a right-handed self-inflicted shot",
         "Shooting oneself in the opposite temple with an unnatural wrist angle points to staged execution."),
        "ur": ("ایک رئیس کی لاش ملی جس کے دائیں ہاتھ میں ریوالور تھا مگر فارنزک ماہر نے فوری قتل کا فیصلہ سنایا۔ کیوں؟",
         ["کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا", "پستول نیا تھا", "تاجر امیر تھا", "کمرے کی کھڑکی کھلی تھی"],
         "کیونکہ گولی بائیں کنپٹی پر لگی تھی جو دائیں ہاتھ سے چلانا ناممکن کی حد تک غیر فطری تھا",
         "دائیں ہاتھ سے بائیں کنپٹی پر فائر کرنا انسانی جسمانی بناوٹ کے اعتبار سے ناممکن ہوتا ہے۔")
    },
    # 271: Double pane bullet hole
    {
        "en": ("A sniper fires a single bullet through a double-pane glass window from the street outside. Which physical characteristic identifies that the shot originated from outside rather than inside?",
         ["The entrance hole on the outer pane is small and clean, while the inner pane displays wide cone-shaped cratering", "The glass melted", "The bullet stopped between panes", "Cracks formed only on inner pane"],
         "The entrance hole on the outer pane is small and clean, while the inner pane displays wide cone-shaped cratering",
         "High-velocity projectile impacts create expanding conchoidal fracture spalling on the exit side of brittle glass."),
        "ur": ("کھڑکی کے دوہرے شیشے میں سے ایک گولی گزری۔ فارنزک ٹیم نے کیسے ثابت کیا کہ گولی باہر سڑک سے اندر کی طرف چلائی گئی تھی؟",
         ["باہر کے شیشے پر باریک صاف سوراخ تھا جبکہ اندرونی شیشے پر مخروطی چٹخنے کا بڑا گڑھا بنا تھا", "شیشہ پگھل گیا تھا", "گولی دونوں شیشوں کے بیچ رک گئی", "اندر کا شیشہ محفوظ تھا"],
         "باہر کے شیشے پر باریک صاف سوراخ تھا جبکہ اندرونی شیشے پر مخروطی چٹخنے کا بڑا گڑھا بنا تھا",
         "گولی جب شیشے سے ٹکراتی ہے تو داخلے کا سوراخ صاف ہوتا ہے اور نکلنے کی سمت شیشہ چٹخ کر چوڑا ہو جاتا ہے۔")
    },
    # 272: Forged document ink drying
    {
        "en": ("An heir presents a handwritten will purportedly drafted thirty years ago with an ordinary blue ballpoint pen. The forensic document examiner immediately exposes the forgery. How?",
         ["Modern phthalocyanine dye ballpoint formulas were not commercially manufactured thirty years ago", "The paper was too heavy", "The handwriting was too neat", "The envelope was modern"],
         "Modern phthalocyanine dye ballpoint formulas were not commercially manufactured thirty years ago",
         "Chemical thin-layer chromatography dates ink components against historical manufacturing timelines."),
        "ur": ("ایک وارث نے 30 سال پرانی وصیت پیش کی جو نیلے بال پوائنٹ سے لکھی گئی تھی۔ دستاویزات کے ماہر نے اسے فوراً جعلی کیسے ثابت کیا؟",
         ["تحریر میں استعمال ہونے والی جدید کیمیائی سیاہی 30 سال پہلے ایجاد ہی نہیں ہوئی تھی", "کاغذ بہت وزنی تھا", "تحریر بہت صاف تھی", "لفافہ نیا تھا"],
         "تحریر میں استعمال ہونے والی جدید کیمیائی سیاہی 30 سال پہلے ایجاد ہی نہیں ہوئی تھی",
         "سیاہی کے لیبارٹری ٹیسٹ نے بتا دیا کہ یہ کیمیکل چند سال پرانا ہے، تیس سال پرانا نہیں ہو سکتا۔")
    },
    # 273: Muddy shoes vs clean pedals
    {
        "en": ("A hit-and-run driver claims someone else hijacked his sedan during an off-road countryside rainstorm. What simple inspection of the vehicle footwell refutes his lie?",
         ["His boots are caked in thick country clay mud, yet the accelerator and brake pedals are spotless clean", "The steering wheel was leather", "The radio was tuned to jazz", "The fuel tank was full"],
         "His boots are caked in thick country clay mud, yet the accelerator and brake pedals are spotless clean",
         "Driving through a muddy off-road deluge leaves heavy mud deposits across control pedals."),
        "ur": ("گاڑی کے مالک نے بیان دیا کہ کچی کیچڑ والی سڑک پر حادثے کے وقت کوئی دوسرا شخص گاڑی چلا رہا تھا۔ پولیس نے اس کا جھوٹ کیسے پکڑا؟",
         ["اس کے اپنے جوتے کیچڑ سے بھرے تھے مگر گاڑی کے ایکسلریٹر اور بریک کے پیڈل بالکل صاف چمک رہے تھے", "اسٹیئرنگ چمڑے کا تھا", "ریڈیو آن تھا", "پیٹرول کا ٹینک بھرا تھا"],
         "اس کے اپنے جوتے کیچڑ سے بھرے تھے مگر گاڑی کے ایکسلریٹر اور بریک کے پیڈل بالکل صاف چمک رہے تھے",
         "کیچڑ میں گاڑی دوڑانے سے پیڈلز پر مٹی کے جمنے کے لازمی نشانات ہوتے ہیں، ان کا صاف ہونا کہانی کو غلط ثابت کرتا ہے۔")
    },
    # 274: Sunglasses in night burglary
    {
        "en": ("A witness identifies a burglary suspect by claiming she saw him wearing mirrored aviator sunglasses at 2:00 AM in a dimly lit warehouse. Why does the detective dismiss the witness?",
         ["Mirrored sunglasses reduce light transmission by 85%, making navigation in a dark warehouse functionally blind", "Aviators are out of fashion", "The warehouse had glass walls", "The suspect had no glasses"],
         "Mirrored sunglasses reduce light transmission by 85%, making navigation in a dark warehouse functionally blind",
         "Dark tinted sunglasses indoors at night prevent scotopic vision, making physical burglary maneuvers impossible."),
        "ur": ("عینی شاہد نے گواہی دی کہ اس نے رات کے 2 بجے اندھیرے گودام میں چور کو کالا دھوپ کا چشمہ پہنے دیکھا تھا۔ تفتیش کار نے گواہ کو جھوٹا کیوں قرار دیا؟",
         ["اندھیرے میں کالا چشمہ پہننے سے انسان اندھا ہو جاتا ہے اور گودام میں چلنا ناممکن ہوتا ہے", "چشمہ پرانا تھا", "گودام میں شیشے لگے تھے", "ملزم چشمہ نہیں لگاتا تھا"],
         "اندھیرے میں کالا چشمہ پہننے سے انسان اندھا ہو جاتا ہے اور گودام میں چلنا ناممکن ہوتا ہے",
         "دھوپ کا چشمہ 85 فیصد روشنی روک دیتا ہے، رات کے اندھیرے میں اسے پہن کر چوری کی واردات کرنا ناممکن ہے۔")
    },
    # 275: Clock stopped at power outage
    {
        "en": ("An electric wall clock stopped at 4:17 PM during a lightning surge. A homeowner claims a break-in occurred at 5:30 PM while the power was on. How does the utility company log expose him?",
         ["Grid telemetry records that mains electricity was restored at 4:35 PM, proving the clock was deliberately unplugged earlier", "Electric clocks don't keep time", "Lightning doesn't affect clocks", "The battery had leaked"],
         "Grid telemetry records that mains electricity was restored at 4:35 PM, proving the clock was deliberately unplugged earlier",
         "Substation electrical logs pinpoint exact outage and restoration timestamps, refuting staged alibis."),
        "ur": ("بجلی کے جھٹکے سے دیوار گھڑی 4:17 پر رک گئی تھی۔ مدعی نے کہا کہ واردات 5:30 بجے بجلی ہوتے ہوئے ہوئی۔ بجلی کی کمپنی کے ریکارڈ نے فراڈ کیسے کھولا؟",
         ["گرڈ کے ریکارڈ کے مطابق بجلی 4:35 پر بحال ہو چکی تھی، یعنی گھڑی کو جان بوجھ کر بند کیا گیا تھا", "بجلی کی گھڑی درست نہیں ہوتی", "آسمانی بجلی گھڑی نہیں روکتی", "سیل ختم ہو گیا تھا"],
         "گرڈ کے ریکارڈ کے مطابق بجلی 4:35 پر بحال ہو چکی تھی، یعنی گھڑی کو جان بوجھ کر بند کیا گیا تھا",
         "بجلی بحال ہونے کے سرکاری لاگ بک نے ثابت کر دیا کہ گھڑی کا پلگ سازش کے تحت خود نکالا گیا تھا۔")
    },
    # 276: Locked room paper under door
    {
        "en": ("A murder occurs inside a room locked from within, with the brass key resting in the keyhole. How did the killer lock the door from outside and leave the key inside?",
         ["Slid a sheet of newspaper under the door, pushed the key out onto the paper with a thin wire, pulled the paper back, and turned it with pliers", "Used a magnetic crane", "Drilled through concrete", "Passed through air ducts"],
         "Slid a sheet of newspaper under the door, pushed the key out onto the paper with a thin wire, pulled the paper back, and turned it with pliers",
         "The classic locked-room newspaper retrieval technique exploits threshold gaps beneath interior doors."),
        "ur": ("ایک بند کمرے کے اندر سے تالا لگا تھا اور چابی اندر ہی لگی تھی۔ قاتل نے باہر نکل کر اندر چابی چھوڑ کر کمرہ باہر سے کیسے لاک کیا؟",
         ["دروازے کے نیچے کاغذ بچھا کر تار سے چابی کاغذ پر گرائی، کاغذ باہر کھینچ کر پلاس سے کنڈی گھمائی", "بڑے مقناطیس سے", "دیوار میں سوراخ کر کے", "ہوا کی نالی سے"],
         "دروازے کے نیچے کاغذ بچھا کر تار سے چابی کاغذ پر گرائی، کاغذ باہر کھینچ کر پلاس سے کنڈی گھمائی",
         "یہ ایک روایتی معمہ ہے جس میں اخبار کے ٹکڑے کو نیچے سرکا کر چابی گرائی اور واپس حاصل کی جاتی ہے۔")
    },
    # 277: Poison in punch bowl
    {
        "en": ("At an evening gala, twenty guests drink freely from a chilled crystal punch bowl and remain healthy. Two latecomers drink from the same bowl twenty minutes later and collapse. What occurred?",
         ["The poison was frozen inside large floating fruit ice blocks that only thawed into the liquid after twenty minutes", "The latecomers were allergic to fruit", "The crystal bowl dissolved", "Airborne toxins settled"],
         "The poison was frozen inside large floating fruit ice blocks that only thawed into the liquid after twenty minutes",
         "Encapsulating toxins in ice ensures delayed release as thermal thawing dissolves the toxin matrix."),
        "ur": ("تقریب میں بیس مہمانوں نے شربت کے پیالے سے شربت پیا اور سب خیریت سے رہے۔ بیس منٹ بعد آنے والے دو مہمانوں نے وہی شربت پیا اور بیہوش ہو گئے۔ کیا ہوا تھا؟",
         ["زہر تیرتے ہوئے برف کے بڑے بلاک کے اندر منجمد تھا جو بیس منٹ بعد گھل کر شربت میں شامل ہوا", "مہمانوں کو پھل سے الرجی تھی", "پیالہ زہریلا ہو گیا تھا", "ہوا کا زہر ملا تھا"],
         "زہر تیرتے ہوئے برف کے بڑے بلاک کے اندر منجمد تھا جو بیس منٹ بعد گھل کر شربت میں شامل ہوا",
         "پہلے شربت پینے والوں کے وقت برف جمی ہوئی تھی، بعد میں برف پگھلنے سے زہر پورے مشروب میں پھیل گیا۔")
    },
    # 278: Twin brother fingerprints
    {
        "en": ("Two identical twin brothers share identical nuclear DNA sequences. A forensic technician recovers latent fingerprints from a stolen safe. Can the technician distinguish which twin touched the safe?",
         ["Yes, identical twins possess unique individual fingerprint friction ridges shaped by random intrauterine amniotic fluid flows", "No, their prints are 100% identical", "Only if blood is present", "Only with retina scans"],
         "Yes, identical twins possess unique individual fingerprint friction ridges shaped by random intrauterine amniotic fluid flows",
         "Fingerprint morphogenesis is phenotypic, influenced by physical gestational forces rather than genetics alone."),
        "ur": ("دو جڑواں بھائیوں کا ڈی این اے (DNA) سو فیصد ایک جیسا ہے۔ چوری کی تجوری سے ملنے والے انگلیوں کے نشانات سے کیا پولیس دونوں میں فرق کر سکتی ہے؟",
         ["ہاں، جڑواں بھائیوں کے فنگر پرنٹس ہمیشہ الگ ہوتے ہیں کیونکہ وہ پیدائش کے وقت رحم میں مختلف بنتے ہیں", "نہیں، ان کے فنگر پرنٹس بالکل ایک جیسے ہوتے ہیں", "صرف خون سے ہو سکتا ہے", "صرف آنکھ کے اسکین سے"],
         "ہاں، جڑواں بھائیوں کے فنگر پرنٹس ہمیشہ الگ ہوتے ہیں کیونکہ وہ پیدائش کے وقت رحم میں مختلف بنتے ہیں",
         "ڈی این اے ایک جیسا ہونے کے باوجود ہر انسان کے فنگر پرنٹس کی باریک لکیریں دنیا میں بالکل منفرد ہوتی ہیں۔")
    },
    # 279: Fresh water in sea drowning
    {
        "en": ("A wealthy sailor is discovered floating dead in deep oceanic salt water. The forensic autopsy immediately confirms he was murdered on land and tossed into the sea. What was the decisive finding?",
         ["His lungs contained chlorinated tap water rather than hypertonic saline seawater with marine diatoms", "His skin had sunburn", "His watch was ticking", "He had no sea salt on hair"],
         "His lungs contained chlorinated tap water rather than hypertonic saline seawater with marine diatoms",
         "Drowning autopsies analyze alveolar fluid electrolyte balance and diatom micro-algae species matching the water body."),
        "ur": ("سمندر کے نمکین پانی میں ایک ملاح کی لاش ملی۔ ڈاکٹر نے فوری فیصلہ دیا کہ اسے زمین پر قتل کر کے سمندر میں پھینکا گیا تھا۔ سب سے بڑا ثبوت کیا تھا؟",
         ["اس کے پھیپھڑوں کے اندر سمندری پانی کے بجائے نلکے کا میٹھا کلورین والا پانی بھرا ہوا تھا", "اس کے چہرے پر دھوپ تھی", "اس کی گھڑی چل رہی تھی", "اس کے بالوں میں نمک نہیں تھا"],
         "اس کے پھیپھڑوں کے اندر سمندری پانی کے بجائے نلکے کا میٹھا کلورین والا پانی بھرا ہوا تھا",
         "ڈوبنے والے کے پھیپھڑوں میں اسی جگہ کا پانی جاتا ہے جہاں اس کا دم گھٹا ہو، نلکے کے پانی نے قتل کا راز فاش کر دیا۔")
    },
    # 280: Warm car hood on winter night
    {
        "en": ("A murder suspect insists his luxury sedan has been parked unused in his outdoor driveway for four days. It is 10°F outside. The detective places a palm on the vehicle engine hood and arrests him. Why?",
         ["The engine block radiates thermal heat, proving the motor was switched off only minutes ago", "The car was out of gasoline", "The battery had melted", "The exhaust was cold"],
         "The engine block radiates thermal heat, proving the motor was switched off only minutes ago",
         "Cast iron engine blocks have high thermal mass, taking hours to cool down to sub-zero ambient temperatures."),
        "ur": ("سخت سرد رات میں ملزم نے کہا کہ اس کی گاڑی پچھلے چار دن سے گھر کے باہر کھڑی ہے۔ انسپکٹر نے گاڑی کے بونٹ پر ہاتھ رکھا اور اسے گرفتار کر لیا۔ کیوں؟",
         ["انجن کا بونٹ گرم تپ رہا تھا جس سے ثابت ہوا کہ گاڑی چند منٹ پہلے ہی بند کی گئی تھی", "گاڑی میں پیٹرول ختم تھا", "بیٹری پگھل گئی تھی", "سائلنسر ٹھنڈا تھا"],
         "انجن کا بونٹ گرم تپ رہا تھا جس سے ثابت ہوا کہ گاڑی چند منٹ پہلے ہی بند کی گئی تھی",
         "منفی درجہ حرارت میں گاڑی کا انجن چند منٹ میں برف نہیں بنتا، اس کی گرمی نے جھوٹ کا پردہ چاک کر دیا۔")
    }
]

print(f"Normal Group 1 loaded base items: {len(ITEMS)}")
