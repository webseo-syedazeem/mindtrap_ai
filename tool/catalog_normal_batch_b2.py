# -*- coding: utf-8 -*-
"""
Normal tier batch B2 (67 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why do cats almost invariably land on their feet when dropped upside down from a modest height?",
        ["The cat flexes its spine and rotates the front and back halves of its body in opposite directions to conserve zero net angular momentum", "Cats have wings under their fur", "Air resistance flips the cat automatically", "Magnetic fields align feline claws"],
        "The cat flexes its spine and rotates the front and back halves of its body in opposite directions to conserve zero net angular momentum",
        "The feline righting reflex allows the cat to twist front and rear body segments in counter-rotation, reorienting without external torque.",
        "بلی کو الٹا چھوڑنے پر وہ ہمیشہ اپنے چاروں پنجوں پر سیدھی ہو کر زمین پر کیسے اترتی ہے؟",
        ["بلی اپنی لچکدار ریڑھ کی ہڈی کو موڑ کر جسم کے اگلے اور پچھلے حصے کو مخالف سمتوں میں گھماتی ہے تاکہ بغیر بیرونی قوت کے توازن حاصل کر سکے", "بلی کی کھال تلے پر ہوتے ہیں", "ہوا کا دباؤ خود بخود بلی کو الٹ دیتا ہے", "زمین کی مقناطیسی کشش پنجوں کو کھینچتی ہے"],
        "بلی اپنی لچکدار ریڑھ کی ہڈی کو موڑ کر جسم کے اگلے اور پچھلے حصے کو مخالف سمتوں میں گھماتی ہے تاکہ بغیر بیرونی قوت کے توازن حاصل کر سکے",
        "بلی اپنے اگلے بازو سمیٹ کر جسم کا اگلا حصہ تیزی سے گھماتی ہے اور پھر پچھلا حصہ مخالف رخ موڑتی ہے، جس سے وہ بغیر کسی سہارے فضا میں سیدھی ہو جاتی ہے۔"
    ),
    (
        "Why do distant stars in the night sky twinkle (scintillate) constantly, while planets in the same sky shine with a steady, unblinking light?",
        ["Stars are pinpoint light sources disrupted by turbulent atmospheric pockets, whereas planets present wider angular disks that average out fluctuations", "Stars run out of nuclear fuel periodically", "Planets emit their own internal light", "Clouds only cross in front of stars"],
        "Stars are pinpoint light sources disrupted by turbulent atmospheric pockets, whereas planets present wider angular disks that average out fluctuations",
        "Stars subtend a fraction of an arcsecond; moving thermal air cells bend the single pencil beam. Planets subtend larger disks, averaging out blinks.",
        "رات کے آسمان پر ستارے مسلسل ٹمٹماتے ہوئے کیوں نظر آتے ہیں جبکہ سیارے بغیر ٹمٹمائے بالکل ساکن چمکتے ہیں؟",
        ["ستارے ایک باریک نقطے کی طرح ہوتے ہیں جن کی روشنی فضا کی ہوا سے ہلتی ہے، جبکہ سیارے چوڑے دائرے ہوتے ہیں جن کی چمک برابر رہتی ہے", "ستاروں کا ایندھن رک رک کر جلتا ہے", "سیارے اپنی ذاتی روشنی پیدا کرتے ہیں", "بادل صرف ستاروں کے آگے آتے ہیں"],
        "ستارے ایک باریک نقطے کی طرح ہوتے ہیں جن کی روشنی فضا کی ہوا سے ہلتی ہے، جبکہ سیارے چوڑے دائرے ہوتے ہیں جن کی چمک برابر رہتی ہے",
        "ستارے کھربوں میل دور ہونے سے سوئی کی نوک جتنے نظر آتے ہیں جس کی شعاع ہوا کے ہلکے جھونکے سے مڑتی ہے، جبکہ سیارے قریب ہونے کی وجہ سے ٹمٹماتے نہیں۔"
    ),
    (
        "Why does dry ice (solid carbon dioxide) turn directly into vapor without leaving any puddle of liquid on the table?",
        ["Atmospheric pressure at sea level (1 atm) is well below carbon dioxide's triple-point pressure (5.1 atm), causing direct sublimation", "Dry ice is made of compressed air", "The liquid evaporates in nanoseconds", "Room heat destroys liquid carbon"],
        "Atmospheric pressure at sea level (1 atm) is well below carbon dioxide's triple-point pressure (5.1 atm), causing direct sublimation",
        "Substances can only exist in liquid phase above their triple-point pressure. At standard pressure, solid CO2 sublimes directly into gas at -78.5°C.",
        "خشک برف (Dry ice) پگھل کر گیلا پانی چھوڑنے کی بجائے میز پر پڑے پڑے سیدھی دھوئیں (گیس) میں کیوں غائب ہو جاتی ہے؟",
        ["عام فضا کا دباؤ کاربن ڈائی آکسائیڈ کے ٹرپل پوائنٹ پریشر سے کم ہے، اس لیے وہ مائع بنے بغیر سیدھی گیس بن جاتی ہے (Sublimation)", "خشک برف ہوا سے بنی ہوتی ہے", "اس کا پانی ایک سیکنڈ میں اڑ جاتا ہے", "کمرے کی حرارت مائع کاربن کو جلا دیتی ہے"],
        "عام فضا کا دباؤ کاربن ڈائی آکسائیڈ کے ٹرپل پوائنٹ پریشر سے کم ہے، اس لیے وہ مائع بنے بغیر سیدھی گیس بن جاتی ہے (Sublimation)",
        "مائع بننے کے لیے کاربن ڈائی آکسائیڈ کو عام ہوا سے 5 گنا زیادہ دباؤ درکار ہوتا ہے۔ عام دباؤ پر وہ ٹھوس سے سیدھی گیس میں تبدیل ہو جاتی ہے۔"
    ),
    (
        "Why does a microwave oven heat a damp sponge or a cup of soup in minutes, but leaves dry glass bowls and plastic plates completely cool?",
        ["2.45 GHz microwaves specifically oscillate polar water and fat molecules via dielectric heating, whereas non-polar glass and plastic do not absorb them", "Glass conducts radiation away", "Plastic reflects 100 percent of microwaves", "Microwaves only heat liquids above boiling"],
        "2.45 GHz microwaves specifically oscillate polar water and fat molecules via dielectric heating, whereas non-polar glass and plastic do not absorb them",
        "Microwaves induce alternating electric fields that flip water dipoles billions of times per second; dry ceramics and non-polar polymers lack dipoles.",
        "مائیکرو ویو اوون سالن اور گیلے کپڑے کو منٹوں میں گرم کر دیتا ہے مگر شیشے کے برتن اور خشک پلیٹ بالکل ٹھنڈی کیوں رہتی ہے؟",
        ["مائیکرو ویو کی لہریں صرف پانی اور چکنائی کے پولر مالیکیولز کو تیزی سے ہلا کر رگڑ سے گرمی پیدا کرتی ہیں، خشک شیشہ لہروں کو نہیں پکڑتا", "شیشہ تمام لہروں کو جذب کر کے ٹھنڈا کر دیتا ہے", "پلاسٹک لہروں کو اچھال دیتا ہے", "مائیکرو ویو صرف ابلتی چیزوں پر اثر کرتی ہے"],
        "مائیکرو ویو کی لہریں صرف پانی اور چکنائی کے پولر مالیکیولز کو تیزی سے ہلا کر رگڑ سے گرمی پیدا کرتی ہیں، خشک شیشہ لہروں کو نہیں پکڑتا",
        "پانی کے مالیکیولز کا قطبی توازن ہوتا ہے، مائیکرو ویو لہریں انہیں ایک سیکنڈ میں دو ارب بار گھماتی ہیں جس سے رگڑ کی حرارت بنتی ہے، خشک برتن میں پانی نہ ہونے سے وہ ٹھنڈا رہتا ہے۔"
    ),
    (
        "Why does an ocean ship sail forward even when the wind is blowing diagonally from the side (tacking against the wind)?",
        ["The curved sails act like vertical airplane wings creating forward aerodynamic lift while the deep underwater keel resists sideways sliding", "Wind pushes the deck directly", "Tides pull ships against wind", "The crew rows with underwater oars"],
        "The curved sails act like vertical airplane wings creating forward aerodynamic lift while the deep underwater keel resists sideways sliding",
        "Bernoulli lift across trimmed sails creates a force with a forward vector component; the keel provides massive lateral hydrodynamic resistance.",
        "بادبانی جہاز ہوا سامنے یا پہلو سے آنے کے باوجود ہوا کے رخ کے مخالف آگے کیسے بڑھ جاتا ہے؟",
        ["بادبان عمودی پروں کی طرح آگے کی طرف ائیروڈائنامک لفٹ بناتے ہیں اور پیندے کا تختہ (Keel) جہاز کو پہلو میں بہنے سے روکتا ہے", "ہوا جہاز کے ڈیک کو دھکیلتی ہے", "لہریں جہاز کو کھینچتی ہیں", "جہاز کے ملاح زیر آب چپو چلاتے ہیں"],
        "بادبان عمودی پروں کی طرح آگے کی طرف ائیروڈائنامک لفٹ بناتے ہیں اور پیندے کا تختہ (Keel) جہاز کو پہلو میں بہنے سے روکتا ہے",
        "بادبان ہوائی جہاز کے پر کی طرح کام کرتا ہے جو کم دباؤ سے آگے کھینچتا ہے۔ پیندے کا لمبا تختہ پانی کو کاٹ کر جہاز کو سیدھا آگے جانے پر مجبور کرتا ہے۔"
    ),
    (
        "Why does a person using an ordinary pair of scissors cut tough fabric easily near the hinge pivot, but struggles when cutting at the very tips of the blades?",
        ["Shorter distance from the pivot provides greater mechanical advantage and higher clamping shear force (Torque = Force * Distance)", "Blades are sharper near the hinge", "Tips have higher friction", "Fabric stretches at the tips"],
        "Shorter distance from the pivot provides greater mechanical advantage and higher clamping shear force (Torque = Force * Distance)",
        "Scissors act as a class-1 lever. The load arm is shortest near the fulcrum, yielding the maximum mechanical cutting force ratio.",
        "قینچی سے موٹا کپڑا کاٹتے وقت قبضے (جوڑ) کے قریب سے کاٹنا آسان کیوں ہوتا ہے جبکہ نوک سے کاٹنا بہت مشکل اور سخت ہوتا ہے؟",
        ["جوڑ کے قریب فاصلہ کم ہونے سے میکانکی فائدہ (Mechanical advantage) بڑھ جاتا ہے اور کٹائی کا زور کئی گنا زیادہ ہو جاتا ہے", "قینچی جوڑ کے پاس زیادہ تیز دھار ہوتی ہے", "نوک پر رگڑ زیادہ ہوتی ہے", "کپڑا نوک پر زیادہ کھنچتا ہے"],
        "جوڑ کے قریب فاصلہ کم ہونے سے میکانکی فائدہ (Mechanical advantage) بڑھ جاتا ہے اور کٹائی کا زور کئی گنا زیادہ ہو جاتا ہے",
        "قینچی ایک لیور ہے۔ جوڑ کے جتنے قریب چیز رکھی جائے، ہاتھ کی طاقت اتنے ہی زیادہ کٹنگ پریشر میں تبدیل ہوتی ہے۔"
    ),
    (
        "Why does a drop of gasoline placed on a calm puddle of water spread out rapidly into a shimmering multi-colored film?",
        ["Gasoline has lower surface tension than water, and optical thin-film interference creates vivid iridescent color fringes", "Gasoline contains liquid rainbow dyes", "Water dissolves gasoline into minerals", "Sunlight burns the gasoline into smoke"],
        "Gasoline has lower surface tension than water, and optical thin-film interference creates vivid iridescent color fringes",
        "The Marangoni stress spreads the volatile hydrocarbon into a nanometer-thin slick. Light reflecting from the top and bottom interfaces interferes constructively.",
        "پانی کے جوہڑ پر پیٹرول یا ڈیزل کا ایک قطرہ گرتے ہی وہ دھنک (Rainbow) کے خوبصورت رنگوں کی باریک جھلی میں کیوں بدل جاتا ہے؟",
        ["پیٹرول کا سطحی تناؤ کم ہوتا ہے اور اس کی باریک تہہ سے ٹکرا کر لوٹنے والی روشنی کی لہریں رنگین انٹرفیرنس پیدا کرتی ہیں", "پیٹرول میں رنگین کیمیکل ہوتے ہیں", "پانی پیٹرول کو گھول دیتا ہے", "دھوپ سے پیٹرول جلنے لگتا ہے"],
        "پیٹرول کا سطحی تناؤ کم ہوتا ہے اور اس کی باریک تہہ سے ٹکرا کر لوٹنے والی روشنی کی لہریں رنگین انٹرفیرنس پیدا کرتی ہیں",
        "پیٹرول کی تہہ چند نینو میٹر پتلی ہو جاتی ہے۔ جب روشنی اس کی اوپری اور نچلی سطح سے منعکس ہو کر آپس میں ملتی ہے تو مختلف رنگوں کی لہریں ابھرتی ہیں۔"
    ),
    (
        "Why does a person feeling an itch scratch the skin, and why does scratching provide immediate temporary relief?",
        ["Scratching induces mild noxious pain signals that activate inhibitory interneurons in the spinal cord, blocking itch transmission", "Scratching kills microscopic skin bacteria", "Fingernails inject natural painkillers", "Scratching cools skin temperature"],
        "Scratching induces mild noxious pain signals that activate inhibitory interneurons in the spinal cord, blocking itch transmission",
        "Pain and itch share spinal pathways. Gate control theory dictates that mild mechanical pain from scratching stimulates Bhlhb5 interneurons, silencing itch neurons.",
        "خارش ہونے پر ناخن سے کھجانے سے فوری طور پر عارضی سکون کیوں ملتا ہے؟",
        ["کھجانے کا ہلکا سا درد ریڑھ کی ہڈی کے راستے پر خارش کے اعصابی سگنلز کو دبا کر روک دیتا ہے (Gate control theory)", "کھجانے سے جلد کے جراثیم مر جاتے ہیں", "ناخنوں سے قدرتی دوا نکلتی ہے", "کھجانے سے جلد ٹھنڈی ہو جاتی ہے"],
        "کھجانے کا ہلکا سا درد ریڑھ کی ہڈی کے راستے پر خارش کے اعصابی سگنلز کو دبا کر روک دیتا ہے (Gate control theory)",
        "درد اور خارش ایک ہی راستے سے دماغ تک جاتے ہیں۔ ہلکا سا درد دماغ کو خارش کے سگنل سے ہٹا دیتا ہے، جس سے وقتی طور پر خارش محسوس ہونا بند ہو جاتی ہے۔"
    ),
    (
        "Why does an ordinary automobile alternator generate alternating current (AC) internally, even though the car's electrical battery is direct current (DC)?",
        ["AC is far easier and more reliable to generate mechanically using rotating magnetic fields, which diodes then rectify into DC", "DC generators explode at high speeds", "Car batteries prefer AC charging", "Alternator belts only spin in AC"],
        "AC is far easier and more reliable to generate mechanically using rotating magnetic fields, which diodes then rectify into DC",
        "A brushless alternator rotor spins past stationary stator windings without heavy wear; a built-in diode bridge rectifier converts the 3-phase AC into 12V DC.",
        "گاڑی کا الٹرنیٹر (Alternator) اندر سے اے سی (AC) کرنٹ پیدا کرتا ہے حالانکہ گاڑی کی بیٹری اور پورا سسٹم ڈی سی (DC) پر چلتا ہے، کیوں؟",
        ["گھومتے ہوئے مقناطیس سے اے سی بنانا انتہائی پائیدار اور آسان ہوتا ہے، جسے ڈائیوڈز کی مدد سے ڈی سی میں بدل لیا جاتا ہے", "ڈی سی جنریٹر تیز رفتاری پر پھٹ جاتے ہیں", "بیٹری اے سی کرنٹ مانگتی ہے", "بیلٹ صرف اے سی گھومتی ہے"],
        "گھومتے ہوئے مقناطیس سے اے سی بنانا انتہائی پائیدار اور آسان ہوتا ہے، جسے ڈائیوڈز کی مدد سے ڈی سی میں بدل لیا جاتا ہے",
        "ڈی سی جنریٹر میں رگڑ والے برش جلد گھس جاتے ہیں، جبکہ اے سی الٹرنیٹر سالہا سال بغیر دیکھ بھال چلتا ہے اور اس کا ریکٹیفائر کرنٹ کو ڈی سی بنا دیتا ہے۔"
    ),
    (
        "Why does a large cargo barge travel faster when fully loaded down in the water than an identical empty barge in a strong headwind?",
        ["The immense aerodynamic windage resistance on the high slab-sided empty hull exceeds the added hydrodynamic friction of the submerged loaded hull", "Heavy barges sink to fast currents", "Empty barges lose engine traction", "Water pushes loaded barges forward"],
        "The immense aerodynamic windage resistance on the high slab-sided empty hull exceeds the added hydrodynamic friction of the submerged loaded hull",
        "An empty barge exposes a massive vertical flat surface to headwinds like a parachute; a laden hull sits low in the water, presenting minimal wind cross-section.",
        "سامنے سے چلتی تیز آندھی میں سامان سے لدا ہوا بھاری جہاز خالی جہاز کے مقابلے میں زیادہ آسانی اور تیزی سے آگے کیسے نکل جاتا ہے؟",
        ["خالی جہاز کی اونچی دیواریں آندھی میں پیراشوٹ کی طرح ہوا کو روکتی ہیں جبکہ لدا ہوا جہاز پانی میں نیچے بیٹھ کر ہوا سے بچ جاتا ہے", "بھاری جہاز تیز لہروں میں ڈوب جاتا ہے", "خالی جہاز کے انجن پھسلتے ہیں", "پانی لدے ہوئے جہاز کو دھکیلتا ہے"],
        "خالی جہاز کی اونچی دیواریں آندھی میں پیراشوٹ کی طرح ہوا کو روکتی ہیں جبکہ لدا ہوا جہاز پانی میں نیچے بیٹھ کر ہوا سے بچ جاتا ہے",
        "خالی جہاز کا بڑا حصہ پانی سے باہر نکل کر ہوا کے لیے ایک بڑی دیوار بن جاتا ہے جو اسے پیچھے دھکیلتی ہے، جبکہ بھاری جہاز پانی میں چھپ کر ہوا کی رکاوٹ کم کر دیتا ہے۔"
    ),
    (
        "Why do birds flying in a flock in a 'V' formation conserve significant metabolic energy during long migratory flights?",
        ["Trailing birds fly in the upwash wingtip vortex created by the leading bird, gaining aerodynamic free lift", "The leader cuts through clouds", "Birds push each other with air gusts", "The V-shape blocks geomagnetic pull"],
        "Trailing birds fly in the upwash wingtip vortex created by the leading bird, gaining aerodynamic free lift",
        "Wingtip vortices generate an upwash field just outside the wingtip; positioning in this zone reduces the induced drag and heart rate of trailing birds.",
        "ہجرت کرنے والے پرندے آسمان پر 'V' کی شکل بنا کر اڑتے ہوئے اپنی توانائی کی زبردست بچت کیسے کرتے ہیں؟",
        ["پیچھے اڑنے والا ہر پرندہ آگے والے کے پروں کے سرے سے بننے والی اٹھتی ہوئی ہوا (Upwash vortex) سے مفت لفٹ حاصل کرتا ہے", "آگے والا پرندہ بادلوں کو کاٹتا ہے", "پرندے ایک دوسرے کو ہوا سے دھکیلتے ہیں", "یہ شکل زمین کی مقناطیسیت روکتی ہے"],
        "پیچھے اڑنے والا ہر پرندہ آگے والے کے پروں کے سرے سے بننے والی اٹھتی ہوئی ہوا (Upwash vortex) سے مفت لفٹ حاصل کرتا ہے",
        "پر کے کنارے سے ہوا اوپر کی طرف چکر کاٹتی ہے، پیچھے والا پرندہ اس ابھرتی ہوا پر سوار ہو کر بغیر زیادہ پر ہلائے پرواز کرتا رہتا ہے۔"
    ),
    (
        "Why does an ordinary lead-pencil eraser become stiff, hard, and prone to smudging paper when stored in a hot, dry drawer for several years?",
        ["Plasticizers in the synthetic rubber evaporate over time, causing cross-linking polymer chains to lose flexibility and turn brittle", "Lead in the pencil poisons the eraser", "The rubber absorbs carbon from air", "Dry air magnetizes the rubber"],
        "Plasticizers in the synthetic rubber evaporate over time, causing cross-linking polymer chains to lose flexibility and turn brittle",
        "Erasers rely on volatile phthalate or vegetable oil plasticizers to keep elastomers supple; their loss leaves brittle rubber that smears instead of abrading.",
        "کئی سال دراز میں رکھی رہنے والی پنسل کی ربڑ (Eraser) سخت، کڑک اور مٹانے کی بجائے کاغذ کو کالا کرنے والی کیوں بن جاتی ہے؟",
        ["ربڑ کو نرم رکھنے والے کیمیکلز (Plasticizers) وقت کے ساتھ اڑ جاتے ہیں جس سے ربڑ کے مالیکیولز سخت اور کڑک ہو جاتے ہیں", "پنسل کا سکہ ربڑ کو زہریلا کر دیتا ہے", "ربڑ ہوا سے کاربن چوس لیتی ہے", "خشک ہوا ربڑ کو مقناطیس بناتی ہے"],
        "ربڑ کو نرم رکھنے والے کیمیکلز (Plasticizers) وقت کے ساتھ اڑ جاتے ہیں جس سے ربڑ کے مالیکیولز سخت اور کڑک ہو جاتے ہیں",
        "ربڑ کی لچک اس کے اندر موجود تیل اور نرم کرنے والے مرکبات پر ہوتی ہے۔ گرمی میں ان کے اڑتے ہی ربڑ پتھر بن کر کاغذ کو رگڑنے کی بجائے گھس جاتی ہے۔"
    ),
    (
        "Why does a person feeling carsick find almost instant relief by rolling down the vehicle window and breathing cool rushing fresh air?",
        ["Cool facial airflow stimulates trigeminal thermoreceptors, dampening autonomic nauseating reflexes in the brainstem vestibular nuclei", "Fresh air contains pure ozone", "Window noise cancels ear vibrations", "Cabin air pressure equals outside"],
        "Cool facial airflow stimulates trigeminal thermoreceptors, dampening autonomic nauseating reflexes in the brainstem vestibular nuclei",
        "Cutaneous cooling of the face, mediated by trigeminal nerve cold receptors, activates central parasympathetic suppression of vestibular emetic pathways.",
        "گاڑی میں سفر کے دوران طبیعت خراب ہونے پر شیشہ نیچے کر کے ٹھنڈی تازی ہوا چہرے پر لگنے سے فوری سکون کیوں ملتا ہے؟",
        ["چہرے پر لگنے والی ٹھنڈی ہوا چہرے کے اعصاب (Trigeminal nerve) کے ذریعے دماغ میں متلی کے خودکار سگنل کو دبا دیتی ہے", "تازی ہوا میں خالص اوزون ہوتی ہے", "کھڑکی کا شور کانوں کو بند کر دیتا ہے", "گاڑی کا دباؤ باہر کے برابر ہو جاتا ہے"],
        "چہرے پر لگنے والی ٹھنڈی ہوا چہرے کے اعصاب (Trigeminal nerve) کے ذریعے دماغ میں متلی کے خودکار سگنل کو دبا دیتی ہے",
        "چہرے کی جلد پر ٹھنڈک کا احساس دماغ کے اس حصے کو پرسکون کرتا ہے جو متلی پیدا کرتا ہے۔ یہ ایک طاقتور قدرتی عصبی ردعمل ہے۔"
    ),
    (
        "Why does an ocean tsunami cause seawater at the beach to suddenly recede and expose hundreds of yards of seabed minutes before the giant wave hits?",
        ["If the tsunami wave crest is preceded by its leading trough, the oceanic depression draws coastal water seaward to feed the wave amplitude", "The seafloor opens up massive cracks", "Evaporation boils the coast dry", "Ocean winds push water backwards"],
        "If the tsunami wave crest is preceded by its leading trough, the oceanic depression draws coastal water seaward to feed the wave amplitude",
        "A tsunami is a wave train; when a subduction earthquake causes initial downward crustal displacement, the leading trough arrives first, sucking the shoreline dry.",
        "سونامی کی دیوہیکل لہر ٹکرانے سے چند منٹ پہلے ساحل کا سمندر اچانک پیچھے ہٹ کر سیکڑوں گز تک سمندر کی تہہ کو ننگا کیوں کر دیتا ہے؟",
        ["اگر سونامی لہر کا نچلا گڑھا (Trough) چوٹی سے پہلے ساحل پر پہنچے تو وہ پانی کو لہر کی طرف پیچھے چوس لیتا ہے", "سمندر کی تہہ میں بڑی دراڑ کھل جاتی ہے", "شدید بخارات ساحل کا پانی سکھا دیتے ہیں", "طوفانی ہوا پانی کو پیچھے اڑا لے جاتی ہے"],
        "اگر سونامی لہر کا نچلا گڑھا (Trough) چوٹی سے پہلے ساحل پر پہنچے تو وہ پانی کو لہر کی طرف پیچھے چوس لیتا ہے",
        "لہر کی ایک چوٹی اور ایک گہرائی ہوتی ہے۔ جب زلزلے سے سمندر میں نیچے خلا بنتا ہے تو لہر کا گہرا حصہ ساحل پر پہلے پہنچ کر سمندر کو پیچھے کھینچ لیتا ہے۔"
    ),
    (
        "Why does an ordinary automobile tire screech loudly on dry pavement during an emergency hard braking stop?",
        ["Tread rubber rapidly cycles between sticking to the road and slipping, vibrating the tire carcass at audible acoustic frequencies", "The brake pads grind against rims", "Air escapes the tire tread rapidly", "Road asphalt melts into hot tar"],
        "Tread rubber rapidly cycles between sticking to the road and slipping, vibrating the tire carcass at audible acoustic frequencies",
        "Frictional stick-slip oscillation of elastic polymer blocks against asphalt excites natural resonant vibrational modes in the tire carcass.",
        "ایمرجنسی بریک لگانے پر گاڑی کے ٹائر خشک سڑک پر تیز چیخنے کی آواز کیوں پیدا کرتے ہیں؟",
        ["ربڑ کا سڑک سے چپکنے اور پھسلنے کا تیز چکر ٹائر کے خول میں ارتعاش پیدا کرتا ہے جس سے آواز بنتی ہے (Stick-slip)", "بریک پیڈ رِم سے ٹکراتے ہیں", "ٹائر کی ہوا باہر نکلتی ہے", "سڑک کی تارکول پگھل جاتی ہے"],
        "ربڑ کا سڑک سے چپکنے اور پھسلنے کا تیز چکر ٹائر کے خول میں ارتعاش پیدا کرتا ہے جس سے آواز بنتی ہے (Stick-slip)",
        "پہیہ جام ہونے پر ٹائر کا ربڑ سڑک کو پکڑتا ہے اور چھوڑتا ہے، اس تیز ترین ارتعاش سے ہوا میں چنگھاڑتی ہوئی آواز گونجتی ہے۔"
    ),
    (
        "Why does striking an iron rod repeatedly with a hammer while aligning it north-south cause the iron rod to become magnetized?",
        ["Mechanical shock frees magnetic domains in the iron, allowing Earth's geomagnetic field to align them in parallel orientation", "Hammering creates nuclear fission", "Friction heats iron into liquid", "The hammer transfers electricity to iron"],
        "Mechanical shock frees magnetic domains in the iron, allowing Earth's geomagnetic field to align them in parallel orientation",
        "Iron contains magnetic domains pinned by lattice defects; mechanical energy overcomes pinning barriers, letting ambient geomagnetic flux align the domains.",
        "لوہے کی راڈ کو شمالاً جنوباً رکھ کر ہتھوڑے سے بار بار چوٹیں مارنے پر وہ خود بخود مقناطیس کیوں بن جاتی ہے؟",
        ["ہتھوڑے کی چوٹ لوہے کے اندرونی ایٹمی ڈومینز کو آزاد کرتی ہے جس سے زمین کا مقناطیسی میدان انہیں ایک سمت میں سیدھا کر دیتا ہے", "چوٹ سے ایٹمی دھماکہ ہوتا ہے", "رگڑ لوہے کو پگھلا دیتی ہے", "ہتھوڑا راڈ میں بجلی بھر دیتا ہے"],
        "ہتھوڑے کی چوٹ لوہے کے اندرونی ایٹمی ڈومینز کو آزاد کرتی ہے جس سے زمین کا مقناطیسی میدان انہیں ایک سمت میں سیدھا کر دیتا ہے",
        "لوہے کے اندر بے شمار چھوٹے مقناطیسی خانے ہوتے ہیں جو بے ترتیب پڑے ہوتے ہیں۔ چوٹ ان کے بندھن ڈھیلے کرتی ہے اور زمین کی قدرتی مقناطیسیت انہیں سیدھا کر دیتی ہے۔"
    ),
    (
        "Why does a glass bottle filled completely to the brim with water and sealed tightly with a cap shatter into pieces when left inside a freezer?",
        ["Water expands by roughly 9 percent upon freezing into ice, generating thousands of atmospheres of hydrostatic pressure against rigid glass", "Ice generates corrosive acids", "Glass contracts and explodes inward", "Freezing boils the bottle bottom"],
        "Water expands by roughly 9 percent upon freezing into ice, generating thousands of atmospheres of hydrostatic pressure against rigid glass",
        "Water's anomalous volumetric expansion upon crystalline solidification exerts pressures exceeding 2,000 atmospheres, shattering rigid containers.",
        "پانی سے لبالب بھر کر مضبوطی سے بند کی گئی شیشے کی بوتل فریزر میں رکھنے پر پھٹ کر ٹکڑے ٹکڑے کیوں ہو جاتی ہے؟",
        ["پانی جم کر برف بنتے وقت 9 فیصد پھیلتا ہے جس سے شیشے پر ہزاروں کلو کا زبردست اندرونی دباؤ بنتا ہے جو بوتل توڑ دیتا ہے", "برف شیشے کو تیزاب سے جلا دیتی ہے", "شیشہ سردی میں سکڑ کر پھٹ جاتا ہے", "برف شیشے کے پیندے کو ابال دیتی ہے"],
        "پانی جم کر برف بنتے وقت 9 فیصد پھیلتا ہے جس سے شیشے پر ہزاروں کلو کا زبردست اندرونی دباؤ بنتا ہے جو بوتل توڑ دیتا ہے",
        "برف بنتے وقت پانی کا حجم بڑھتا ہے۔ اگر برتن میں ہوا کی خالی جگہ نہ ہو تو برف کی طاقتور قوت شیشے کو بغیر کسی مزاحمت کے توڑ کر رکھ دیتی ہے۔"
    ),
    (
        "Why does a metallic spoon feel freezing cold when removed from ice cream, while a wooden spoon at the exact same temperature feels comfortable?",
        ["Metals have high thermal conductivity, conducting heat away from your fingertips hundreds of times faster than wood", "The metal spoon is physically colder in degrees", "Wood produces internal heat through friction", "Metal absorbs human skin oils"],
        "Metals have high thermal conductivity, conducting heat away from your fingertips hundreds of times faster than wood",
        "Human temperature receptors sense the rate of heat flux leaving the skin (d Q/d t), not absolute temperature.",
        "آئس کریم سے نکالا گیا لوہے کا چمچ ہاتھ کو برف کی طرح ٹھنڈا لگتا ہے جبکہ لکڑی کا چمچ اسی درجہ حرارت پر ٹھنڈا کیوں نہیں لگتا؟",
        ["دھات کی تھرمل کنڈکٹیویٹی انگلیوں سے حرارت کو لکڑی کے مقابلے میں سینکڑوں گنا زیادہ تیزی سے چوس لیتی ہے", "لوہے کا چمچ درحقیقت زیادہ ٹھنڈا ہوتا ہے", "لکڑی اندرونی حرارت بناتی ہے", "دھات جلد کا تیل پی لیتی ہے"],
        "دھات کی تھرمل کنڈکٹیویٹی انگلیوں سے حرارت کو لکڑی کے مقابلے میں سینکڑوں گنا زیادہ تیزی سے چوس لیتی ہے",
        "ہماری جلد درجہ حرارت نہیں ناپتی بلکہ یہ دیکھتی ہے کہ حرارت کتنی تیزی سے جسم سے نکل رہی ہے۔ لوہا حرارت تیزی سے کھینچتا ہے اس لیے شدید ٹھنڈا لگتا ہے۔"
    ),
    (
        "Why does an airplane cabin feel dry and cause passengers' throats and skin to dehydrate rapidly during a long intercontinental flight?",
        ["Outside air drawn into the cabin at cruising altitude (-50°C) contains virtually zero absolute humidity, which remains parched when heated", "Air conditioning absorbs human moisture", "Jet fuel combustion dries out the air", "Cabin air pressure evaporates sweat instantly"],
        "Outside air drawn into the cabin at cruising altitude (-50°C) contains virtually zero absolute humidity, which remains parched when heated",
        "At 35,000 feet, ambient air is frigid and cannot hold moisture; heating it to 22°C drops relative cabin humidity below 10-15%, drier than most deserts.",
        "لمبی بین البراعظمی پرواز کے دوران ہوائی جہاز کا کیبن اتنا خشک کیوں محسوس ہوتا ہے اور مسافروں کے گلے اور جلد سوکھنے کیوں لگتی ہے؟",
        ["بلندی پر باہر کی منفی 50 ڈگری سرد ہوا میں نمی بالکل صفر ہوتی ہے، گرم کرنے کے بعد کیبن کی ہوا صحرا سے بھی زیادہ خشک ہو جاتی ہے", "ائیر کنڈیشنر انسانوں کی نمی چوس لیتا ہے", "پیٹرول کا دھواں ہوا خشک کرتا ہے", "کیبن کا دباؤ پسینہ اڑا دیتا ہے"],
        "بلندی پر باہر کی منفی 50 ڈگری سرد ہوا میں نمی بالکل صفر ہوتی ہے، گرم کرنے کے بعد کیبن کی ہوا صحرا سے بھی زیادہ خشک ہو جاتی ہے",
        "بلندی پر شدید سردی میں ہوا نمی برقرار نہیں رکھ سکتی۔ جب یہ خشک ہوا اندر لا کر گرم کی جاتی ہے تو کیبن میں نمی 10 فیصد سے بھی کم رہ جاتی ہے۔"
    ),
    (
        "Why does a diver in deep ocean waters feel pressure in their ears during descent that can be relieved by swallowing or yawning?",
        ["Swallowing opens the Eustachian tubes, equalizing middle-ear cavity air pressure with external hydrostatic water pressure", "Swallowing drains water from the ears", "Yawning cools the auditory canals", "Swallowing resets ear balance"],
        "Swallowing opens the Eustachian tubes, equalizing middle-ear cavity air pressure with external hydrostatic water pressure",
        "Water pressure pushes the tympanic membrane inward; opening the pharyngotympanic tubes allows air from the nasopharynx to re-pressurize the middle ear.",
        "سمندر میں غوطہ لگاتے ہوئے جیسے جیسے انسان گہرائی میں اترتا ہے اس کے کانوں پر شدید دباؤ بنتا ہے جسے تھوک نگلنے سے سکون کیسے ملتا ہے؟",
        ["تھوک نگلنے سے یوسٹاچین نالیاں (Eustachian tubes) کھل جاتی ہیں جو کان کے درمیانی حصے کی ہوا کو پانی کے دباؤ کے برابر کر دیتی ہیں", "تھوک نگلنے سے کان سے پانی باہر نکلتا ہے", "جمائی لینے سے کان ٹھنڈے ہوتے ہیں", "نگلنے سے کان کا توازن بحال ہوتا ہے"],
        "تھوک نگلنے سے یوسٹاچین نالیاں (Eustachian tubes) کھل جاتی ہیں جو کان کے درمیانی حصے کی ہوا کو پانی کے دباؤ کے برابر کر دیتی ہیں",
        "پانی کا دباؤ کان کے پردے کو اندر دباتا ہے جس سے درد ہوتا ہے۔ تھوک نگلنے سے حلق سے ہوا کان کے پردے کے پیچھے پہنچ کر دباؤ برابر کر دیتی ہے۔"
    ),
    (
        "Why does a person using an ordinary hand lens see a magnified virtual image of an object when holding it closer than the focal length, but sees an inverted image when holding it further away?",
        ["Inside the focal point, diverging rays project an upright virtual image; beyond the focal point, rays converge and cross, forming an inverted real image", "Lenses flip polarity at focal distance", "Light changes speed beyond focal length", "Lenses filter out upside-down photons"],
        "Inside the focal point, diverging rays project an upright virtual image; beyond the focal point, rays converge and cross, forming an inverted real image",
        "Geometric optics dictates: object distance d_o < f yields magnified upright virtual rays; d_o > f yields real inverted rays crossing in space.",
        "محدب عدسے (Magnifying glass) کو چیز کے قریب رکھیں تو سیدھا اور بڑا عکس دکھتا ہے، مگر دور لے جائیں تو عکس الٹا کیوں ہو جاتا ہے؟",
        ["فوکل پوائنٹ کے اندر شعاعیں پھیل کر بڑا سیدھا عکس بناتی ہیں، مگر فوکل پوائنٹ سے باہر شعاعیں ایک دوسرے کو کراس کر کے عکس الٹ دیتی ہیں", "عدسہ فوکل پوائنٹ پر مقناطیس بدلتا ہے", "روشنی کی رفتار فوکل پوائنٹ پر بدلتی ہے", "عدسہ الٹی شعاعوں کو روکتا ہے"],
        "فوکل پوائنٹ کے اندر شعاعیں پھیل کر بڑا سیدھا عکس بناتی ہیں، مگر فوکل پوائنٹ سے باہر شعاعیں ایک دوسرے کو کراس کر کے عکس الٹ دیتی ہیں",
        "جب چیز عدسے کے فوکس کے اندر ہو تو بڑا مجازی عکس نظر آتا ہے۔ جیسے ہی چیز فوکس سے دور جاتی ہے، روشنی کی کرنیں آپس میں ٹکرا کر الٹ جاتی ہیں۔"
    ),
    (
        "Why does an ocean lighthouse beam sweep across the water in a circular motion rather than simply flashing on and off as a stationary strobe light?",
        ["A continuously rotating continuous light source using a Fresnel lens produces a brighter, more focused beam using far less electrical wattage", "Flashing strobes shatter from heat", "Stationary lights confuse seagulls", "Ocean winds extinguish stationary lamps"],
        "A continuously rotating continuous light source using a Fresnel lens produces a brighter, more focused beam using far less electrical wattage",
        "Revolving giant Fresnel lens prisms around a steady lamp concentrates omnidirectional light into colossal piercing beams sweeping the horizon.",
        "لائٹ ہاؤس کے اندر بلب کو بار بار جلانے اور بجھانے کی بجائے مستقل جلتے ہوئے بلب کو گھومتے ہوئے لینز سے دائرے میں کیوں گھمایا جاتا ہے؟",
        ["گھومتا ہوا فریسنل لینز (Fresnel lens) بلب کی تمام روشنی کو ایک طاقتور شعاع میں جمع کر کے انتہائی کم بجلی میں درجنوں میل دور دکھاتا ہے", "جلنے بجھنے سے بلب گرمی سے ٹوٹ جاتا ہے", "ساکن روشنی پرندوں کو الجھاتی ہے", "سمندری ہوائیں ساکن بلب بجھا دیتی ہیں"],
        "گھومتا ہوا فریسنل لینز (Fresnel lens) بلب کی تمام روشنی کو ایک طاقتور شعاع میں جمع کر کے انتہائی کم بجلی میں درجنوں میل دور دکھاتا ہے",
        "فریسنل لینز کے شیشے روشنی کو ایک متوازی بیم میں فوکس کرتے ہیں، گھومنے سے وہ سمندر میں دور جہازوں کو ایک دیوہیکل فلیش کے طور پر نظر آتی ہے۔"
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
        "Why does a person feeling faint or dizzy naturally recover faster when lying flat on their back with legs elevated?",
        ["Gravity assists venous blood return from lower limbs to the brain, restoring cerebral perfusion pressure", "Lying down cools the forehead", "Leg elevation stretches the spine", "It allows deeper diaphragmatic breaths only"],
        "Gravity assists venous blood return from lower limbs to the brain, restoring cerebral perfusion pressure",
        "Orthostatic hypotension deprives the brain of oxygen; elevating lower limbs uses gravity to refill central circulation.",
        "چکر آنے یا بے ہوش ہونے والے شخص کو سیدھا لٹا کر ٹانگیں اوپر اٹھانے سے فوری افاقہ کیوں ہوتا ہے؟",
        ["کشش ثقل کی مدد سے خون تیزی سے واپس دل اور دماغ کی طرف لوٹتا ہے جس سے آکسیجن بحال ہوتی ہے", "لیٹنے سے ماتھا ٹھنڈا ہو جاتا ہے", "ریڑھ کی ہڈی سیدھی ہوتی ہے", "صرف گہرے سانس لینے کے لیے"],
        "کشش ثقل کی مدد سے خون تیزی سے واپس دل اور دماغ کی طرف لوٹتا ہے جس سے آکسیجن بحال ہوتی ہے",
        "جب دماغ کو خون کی سپلائی کم ہوتی ہے تو انسان گرتا ہے، ٹانگیں اٹھانے سے سارا خون فوری طور پر دماغ میں پہنچ جاتا ہے۔"
    ),
    (
        "Why does a drop of olive oil stay intact on a dry tabletop but spread out flat when soap is added to the oil?",
        ["Soap molecules lower the interfacial tension between the oil and the surface, increasing wetting capability", "Soap dissolves the table surface", "Soap generates heat that melts oil", "Oil evaporates in presence of soap"],
        "Soap molecules lower the interfacial tension between the oil and the surface, increasing wetting capability",
        "Surfactants disrupt cohesive forces within the oil droplet, reducing contact angle and promoting liquid spreading.",
        "خشک میز پر تیل کا قطرہ گول رہتا ہے مگر صابن چھوتے ہی وہ فورا پھیل کر چپٹا کیوں ہو جاتا ہے؟",
        ["صابن تیل کے اندرونی سطحی تناؤ کو توڑ کر اسے سطح پر پھیلنے کی اجازت دیتا ہے", "صابن لکڑی کو پگھلا دیتا ہے", "صابن سے حرارت پیدا ہوتی ہے", "تیل بخارات بن کر اڑنے لگتا ہے"],
        "صابن تیل کے اندرونی سطحی تناؤ کو توڑ کر اسے سطح پر پھیلنے کی اجازت دیتا ہے",
        "صابن تیل کے مالیکیولز کا باہمی کھنچاؤ کم کر دیتا ہے جس سے قطرہ اپنی گول شکل قائم نہیں رکھ پاتا اور پھیل جاتا ہے۔"
    ),
    (
        "Why does a metallic spoon reflect an upside-down image of your face when looking at its concave front bowl?",
        ["Parallel rays bounce off the concave surface and cross at the focal point before reaching your eyes", "Light rays invert color wavelengths", "Metal absorbs the top half of light", "The spoon bends magnetic fields"],
        "Parallel rays bounce off the concave surface and cross at the focal point before reaching your eyes",
        "A concave reflector focuses light rays to a point between the viewer and mirror; beyond this focal length, rays cross and produce an inverted real image.",
        "چمچ کے اندرونی گہرے رخ (Concave) میں دیکھنے پر انسان کا اپنا چہرہ الٹا کیوں دکھائی دیتا ہے؟",
        ["گہرے رخ سے ٹکرا کر روشنی کی کرنیں فوکل پوائنٹ پر ایک دوسرے کو کراس کر کے الٹ جاتی ہیں", "روشنی کا رنگ الٹ جاتا ہے", "چمچ اوپری روشنی نگل لیتا ہے", "چمچ مقناطیسی عکس بناتا ہے"],
        "گہرے رخ سے ٹکرا کر روشنی کی کرنیں فوکل پوائنٹ پر ایک دوسرے کو کراس کر کے الٹ جاتی ہیں",
        "مقعر آئینہ روشنی کی شعاعوں کو اندر کی طرف موڑتا ہے جو آنکھوں تک پہنچنے سے پہلے الٹ جاتی ہیں، جس سے الٹا عکس بنتا ہے۔"
    ),
    (
        "Why does a person feeling cold develop 'goosebumps' on their arms and legs?",
        ["Arrector pili muscles contract to raise hair follicles, an evolutionary reflex meant to trap an insulating layer of warm air", "Blood vessels burst near pores", "Sweat glands solidify in cold", "Skin shrinks and folds"],
        "Arrector pili muscles contract to raise hair follicles, an evolutionary reflex meant to trap an insulating layer of warm air",
        "Piloerection in furry animals fluffs the coat for thermal insulation; in humans with sparse hair, it manifests as visible skin bumps.",
        "سردی لگنے پر انسان کے جسم کے رونگٹے (Goosebumps) کیوں کھڑے ہو جاتے ہیں؟",
        ["جلد کے باریک پٹھے سکڑ کر بالوں کو کھڑا کرتے ہیں تاکہ گرم ہوا کی ایک تہہ کو روک کر سردی سے بچایا جا سکے", "مساموں کے قریب خون جم جاتا ہے", "پسینے کے غدود بند ہو جاتے ہیں", "جلد سکڑ کر سلوٹیں بناتی ہے"],
        "جلد کے باریک پٹھے سکڑ کر بالوں کو کھڑا کرتے ہیں تاکہ گرم ہوا کی ایک تہہ کو روک کر سردی سے بچایا جا سکے",
        "یہ جسم کا قدیم دفاعی نظام ہے جو بالوں کو پھلا کر گرم ہوا کو قید کرتا ہے تاکہ جسم کی حرارت محفوظ رہے۔"
    ),
    (
        "Why does an acoustic guitar sound so much louder than an unplugged solid-body electric guitar, even though identical strings are plucked?",
        ["The hollow wooden soundboard vibrates with high surface area, coupling string vibrations efficiently to ambient air", "Acoustic strings are wound with magnets", "Electric guitar wood absorbs acoustic frequencies", "Soundboard contains trapped echoes"],
        "The hollow wooden soundboard vibrates with high surface area, coupling string vibrations efficiently to ambient air",
        "Thin vibrating strings slice through air with poor acoustic impedance matching; the large resonant wooden soundboard acts as an acoustic amplifier.",
        "روایتی صوتی گٹار کی آواز بغیر ایمپلیفائر والی برقی گٹار سے کہیں زیادہ اونچی اور گونج دار کیوں ہوتی ہے؟",
        ["لکڑی کا کھوکھلا ساؤنڈ بورڈ بڑے رقبے پر ارتعاش پیدا کر کے ہوا کو زوردار آواز فراہم کرتا ہے", "صوتی گٹار کی تاروں میں مقناطیس ہوتا ہے", "برقی گٹار کی لکڑی آواز نگل جاتی ہے", "ساؤنڈ بورڈ کے اندر مستقل گونج ہوتی ہے"],
        "لکڑی کا کھوکھلا ساؤنڈ بورڈ بڑے رقبے پر ارتعاش پیدا کر کے ہوا کو زوردار آواز فراہم کرتا ہے",
        "باریک تار اکیلے ہوا کو ہلا نہیں سکتے، مگر جب وہ گٹار کے لکڑی کے تختے کو ہلاتے ہیں تو پورا بورڈ مل کر ہوا میں آواز پھیلا دیتا ہے۔"
    ),
    (
        "Why do birds migrate thousands of miles along exact flight paths without GPS or navigational equipment?",
        ["They utilize Earth's geomagnetic field via cryptochrome proteins in their retinas, alongside celestial and solar cues", "They follow ocean highways", "They smell food from thousands of miles away", "Older birds carry maps in memory only"],
        "They utilize Earth's geomagnetic field via cryptochrome proteins in their retinas, alongside celestial and solar cues",
        "Magnetoreception paired with solar azimuth and polarized light patterns provides birds with an innate biological navigation suite.",
        "پرندے بغیر کسی نقشے یا جی پی ایس کے ہزاروں میل کا فاصلہ بالکل درست سمت میں کیسے طے کر لیتے ہیں؟",
        ["وہ زمین کے مقناطیسی میدان، سورج کی پوزیشن اور ستاروں کے نظام سے راستہ پہچانتے ہیں", "وہ سمندری سڑکوں کے پیچھے چلتے ہیں", "وہ ہزاروں میل دور سے کھانے کی خوشبو سونگھتے ہیں", "پرانے پرندوں کو زبانی یاد ہوتا ہے"],
        "وہ زمین کے مقناطیسی میدان، سورج کی پوزیشن اور ستاروں کے نظام سے راستہ پہچانتے ہیں",
        "پرندوں کی آنکھوں میں خاص پروٹین زمین کے مقناطیسی میدان کو دیکھ یا محسوس کر سکتے ہیں، جس سے وہ قطب نما کی طرح رہنمائی پاتے ہیں۔"
    ),
    (
        "Why does a bicycle rider remain balanced easily while rolling forward, but quickly falls over when standing completely still?",
        ["Steering corrections create centrifugal acceleration that keeps the center of mass above the contact patch", "Wheels become heavy like gyroscopes", "Wind pushes the frame upright", "Pneumatic air creates vertical buoyancy"],
        "Steering corrections create centrifugal acceleration that keeps the center of mass above the contact patch",
        "While rolling, small intuitive turns of the handlebars continuously steer the bicycle's tire contact points back beneath the falling center of mass.",
        "سائیکل چلاتے ہوئے انسان آسانی سے توازن بنا لیتا ہے مگر رکی ہوئی سائیکل پر فوراً کیوں گر جاتا ہے؟",
        ["چلتی سائیکل پر ہینڈل گھما کر ٹائروں کو گرتے ہوئے جسم کے نیچے لایا جاتا ہے جس سے توازن برقرار رہتا ہے", "ٹائر گائروسکوپ بن کر وزنی ہو جاتے ہیں", "ہوا سائیکل کو سیدھا رکھتی ہے", "ٹائر کی ہوا اوپر اچھالتی ہے"],
        "چلتی سائیکل پر ہینڈل گھما کر ٹائروں کو گرتے ہوئے جسم کے نیچے لایا جاتا ہے جس سے توازن برقرار رہتا ہے",
        "حرکت کے دوران جب سائیکل ایک طرف جھکتی ہے تو سوار لاشعوری طور پر اسی طرف موڑ کر پہیوں کو جسم کے مرکز کے نیچے لے آتا ہے۔"
    ),
    (
        "Why does an ocean ship anchor hold a massive vessel securely in place against strong tidal currents?",
        ["The heavy chain lies flat along the seafloor, generating enormous seabed friction and pulling the anchor flukes into the sand horizontally", "The anchor magnetizes the ocean bedrock", "The anchor pierces down to Earth's mantle", "The vessel floats completely still"],
        "The heavy chain lies flat along the seafloor, generating enormous seabed friction and pulling the anchor flukes into the sand horizontally",
        "It is the catenary weight of the chain lying horizontal on the seabed that pulls the anchor flukes deeper into sediment, not a vertical hold.",
        "سمندری لنگر (Anchor) اتنے بڑے بحری جہاز کو تیز لہروں کے باوجود اپنی جگہ پر کیسے روک لیتا ہے؟",
        ["بھاری زنجیر سمندر کی تہہ پر لیٹ کر افقی کھنچاؤ پیدا کرتی ہے جو لنگر کے پنجوں کو ریت میں مزید گہرا دھنسا دیتی ہے", "لنگر زمین کی تہہ سے مقناطیس بن کر جڑتا ہے", "لنگر زمین کے اندر سوراخ کر دیتا ہے", "جہاز خود بخود رک جاتا ہے"],
        "بھاری زنجیر سمندر کی تہہ پر لیٹ کر افقی کھنچاؤ پیدا کرتی ہے جو لنگر کے پنجوں کو ریت میں مزید گہرا دھنسا دیتی ہے",
        "لنگر کا اصل کمال اس کی بھاری زنجیر ہے جو افقی ہو کر ریت میں پنجوں کو اندر گھساتی ہے، جس سے جہاز لہروں میں آگے نہیں بہہ پاتا۔"
    ),
    (
        "Why does an airplane fly more smoothly on a cold winter morning than during a scorching summer afternoon?",
        ["Cold dense air provides stable laminar lift, whereas solar heating of the ground creates turbulent thermal updrafts in summer", "Winter air has lower gravity", "Aircraft engines run slower in winter", "Clouds freeze solid and buffer the flight"],
        "Cold dense air provides stable laminar lift, whereas solar heating of the ground creates turbulent thermal updrafts in summer",
        "Sunlight heats the terrain unevenly, spawning convective thermal plumes that toss aircraft; cold winter air produces calm uniform density.",
        "ہوائی جہاز سخت گرم دوپہر کے مقابلے میں سردیوں کی صبح اتنی ہموار اور پرسکون پرواز کیوں کرتا ہے؟",
        ["سرد ہوا کثیف اور یکساں ہوتی ہے جبکہ گرمیوں میں سورج کی تپش زمین سے بے قاعدہ گرم ہوائیں اٹھاتی ہے جو ہچکولے دیتی ہیں", "سرد ہوا میں کشش ثقل کم ہوتی ہے", "انجن سردیوں میں سست چلتے ہیں", "بادل جم کر جہاز کو سہارا دیتے ہیں"],
        "سرد ہوا کثیف اور یکساں ہوتی ہے جبکہ گرمیوں میں سورج کی تپش زمین سے بے قاعدہ گرم ہوائیں اٹھاتی ہے جو ہچکولے دیتی ہیں",
        "گرمیوں میں زمین سے اٹھنے والے گرم ہوا کے بگولے جہاز کو اوپر نیچے اچھالتے ہیں، جبکہ سردیوں میں ہوا بالکل ہموار اور کثیف ہوتی ہے۔"
    ),
    (
        "Why does a diver in deep ocean waters hear sounds coming from all directions at once without being able to pinpoint the sound source?",
        ["Sound travels four times faster in water, making the interaural time difference too short for human brain processing", "Water fills human auditory ear canals", "Underwater sounds only travel in circles", "Ear drums lock tight under water pressure"],
        "Sound travels four times faster in water, making the interaural time difference too short for human brain processing",
        "Sound velocity in water is ~1,500 m/s. The time delay between reaching the left and right ear shrinks to microseconds, defeating localization.",
        "سمندر میں غوطہ خور کو زیر آب آنے والی آواز کی درست سمت (کہ آواز دائیں سے آئی یا بائیں سے) کیوں معلوم نہیں ہو پاتی؟",
        ["پانی میں آواز اتنی تیز سفر کرتی ہے کہ دونوں کانوں تک پہنچنے کا درمیانی فرق دماغ کے لیے ناقابل فہم ہو جاتا ہے", "کانوں میں پانی بھر جاتا ہے", "پانی میں آواز گول گھومتی ہے", "کان کے پردے جام ہو جاتے ہیں"],
        "پانی میں آواز اتنی تیز سفر کرتی ہے کہ دونوں کانوں تک پہنچنے کا درمیانی فرق دماغ کے لیے ناقابل فہم ہو جاتا ہے",
        "خشک ہوا میں آواز ایک کان تک دوسرے سے معمولی تاخیر سے پہنچتی ہے جس سے دماغ سمت جانتا ہے۔ پانی میں آواز 4 گنا تیز ہونے سے یہ تاخیر غائب ہو جاتی ہے۔"
    ),
    (
        "Why does an electric generator produce electricity when its metal wire coil is spun inside a magnetic field?",
        ["Changing magnetic flux through the rotating coil induces an electromotive force (Faraday's Law of Electromagnetic Induction)", "The magnet heats the wire until sparks fly", "Friction between copper and iron makes electricity", "Air ionization powers the circuit"],
        "Changing magnetic flux through the rotating coil induces an electromotive force (Faraday's Law of Electromagnetic Induction)",
        "Faraday's Law dictates that the time-varying magnetic field exerts Lorentz forces on mobile electrons, generating electrical voltage.",
        "جب تانبے کے تاروں کا کوائل مقناطیسی فیلڈ میں گھمایا جاتا ہے تو جنریٹر بجلی کیسے پیدا کرتا ہے؟",
        ["گھومتے ہوئے کوائل میں مقناطیسی فیلڈ کی تبدیلی تار کے الیکٹرانز کو دھکیل کر وولٹیج پیدا کرتی ہے (Faraday's Law)", "مقناطیس تار کو جلا کر چنگاریاں بناتا ہے", "لوہے کی رگڑ سے بجلی بنتی ہے", "ہوا کی گیسیں کرنٹ بناتی ہیں"],
        "گھومتے ہوئے کوائل میں مقناطیسی فیلڈ کی تبدیلی تار کے الیکٹرانز کو دھکیل کر وولٹیج پیدا کرتی ہے (Faraday's Law)",
        "مائیکل فیراڈے نے دریافت کیا کہ جب بھی کوئی موصل مقناطیسی لہروں کو کاٹتا ہے تو اس کے اندر الیکٹرانز بہنے لگتے ہیں، جو بجلی کہلاتی ہے۔"
    ),
    (
        "Why does a thin paper tissue absorb spilled water rapidly, while a plastic sheet allows water to bead up without absorbing a drop?",
        ["Paper fibers contain hydrophilic cellulose with capillary micro-channels that draw water in via adhesion", "Plastic dissolves in water molecules", "Paper creates electrostatic attraction to water", "Plastic is completely porous"],
        "Paper fibers contain hydrophilic cellulose with capillary micro-channels that draw water in via adhesion",
        "Cellulose hydroxyl groups form hydrogen bonds with water molecules, driving spontaneous capillary action through porous fibers.",
        "ٹشو پیپر گرے ہوئے پانی کو فوراً چوس لیتا ہے جبکہ پلاسٹک کی شیٹ پر پانی کا قطرہ ویسے ہی پڑا رہتا ہے، کیوں؟",
        ["کاغذ کے ریشوں میں موجود سیلولوز کی کیپلری نالیاں پانی کو کشش کے تحت تیزی سے اندر کھینچتی ہیں", "پلاسٹک پانی میں گھل جاتا ہے", "کاغذ بجلی سے پانی کھینچتا ہے", "پلاسٹک میں سوراخ ہوتے ہیں"],
        "کاغذ کے ریشوں میں موجود سیلولوز کی کیپلری نالیاں پانی کو کشش کے تحت تیزی سے اندر کھینچتی ہیں",
        "سیلولوز پانی کے مالیکیولز کو پسند کرتا ہے، اور کاغذ کے باریک مسام کیپلری عمل سے پانی کو اپنے اندر چوس لیتے ہیں۔"
    ),
    (
        "Why does an ordinary automobile engine overheat quickly if the radiator water pump belt snaps during driving?",
        ["Without forced coolant circulation, heat produced by internal combustion accumulates in engine cylinder walls without dissipation", "Engine oil catches fire immediately", "The radiator fan reverses direction", "Air pressure in cylinders drops to zero"],
        "Without forced coolant circulation, heat produced by internal combustion accumulates in engine cylinder walls without dissipation",
        "The water pump pumps liquid coolant between the scorching engine block and the cooling radiator fins; stopping circulation traps extreme heat.",
        "گاڑی چلاتے وقت اگر واٹر پمپ کا بیلٹ ٹوٹ جائے تو انجن چند منٹوں میں کھول کیوں جاتا ہے؟",
        ["کولنٹ پانی کی گردش رکنے سے انجن کی دہکتی حرارت ریڈی ایٹر تک نہیں پہنچ پاتی اور بلاک میں قید ہو جاتی ہے", "انجن کا آئل فوراً جل اٹھتا ہے", "ریڈی ایٹر کا پنکھا الٹا چلنے لگتا ہے", "سلنڈر میں ہوا ختم ہو جاتی ہے"],
        "کولنٹ پانی کی گردش رکنے سے انجن کی دہکتی حرارت ریڈی ایٹر تک نہیں پہنچ پاتی اور بلاک میں قید ہو جاتی ہے",
        "واٹر پمپ ٹھنڈے پانی کو انجن کے گرد گھما کر ریڈی ایٹر تک لے جاتا ہے۔ گردش رکتے ہی انجن کی آگ پانی کو فوراً ابال کر انجن کو جام کر دیتی ہے۔"
    ),
    (
        "Why does a steel ship float gracefully on ocean waters, whereas a tiny solid steel ball of the exact same material sinks instantly to the seabed?",
        ["The hollow hull encloses vast pockets of empty air, lowering the ship's average overall density well below the density of seawater", "Seawater repels hollow steel shapes", "The ship's engines push upward", "Ships are painted with buoyant coating"],
        "The hollow hull encloses vast pockets of empty air, lowering the ship's average overall density well below the density of seawater",
        "Archimedes' Principle states that average density determines buoyancy. The massive internal air volume gives the ship a low bulk density.",
        "ہزاروں ٹن وزنی لوہے کا جہاز سمندر پر تیرتا رہتا ہے جبکہ لوہے کی چھوٹی سی گولی فوراً تہہ میں کیوں ڈوب جاتی ہے؟",
        ["جہاز کا کھوکھلا ڈھانچہ وسیع ہوا کو قید رکھتا ہے جس سے اس کی اوسط کثافت سمندری پانی سے کم ہو جاتی ہے", "سمندر کھوکھلے لوہے کو اچھالتا ہے", "انجن جہاز کو اوپر اٹھاتے ہیں", "جہاز پر خاص تیرنے والا پینٹ ہوتا ہے"],
        "جہاز کا کھوکھلا ڈھانچہ وسیع ہوا کو قید رکھتا ہے جس سے اس کی اوسط کثافت سمندری پانی سے کم ہو جاتی ہے",
        "اگرچہ لوہا بھاری ہے، مگر جہاز کا بڑا حصہ ہوا پر مشتمل ہوتا ہے۔ اس لیے جہاز کی مجموعی اوسط کثافت پانی سے ہلکی ہو جاتی ہے اور وہ تیرتا ہے۔"
    ),
    (
        "Why does an ocean lighthouse look taller when viewed directly through fog or thick coastal haze?",
        ["Reduced contrast and blurred boundaries trick the human visual system into misjudging distance and perceived object scale", "Fog magnifies light rays like a telescope", "Haze lifts the lighthouse physically", "Moisture bends the viewer's cornea"],
        "Reduced contrast and blurred boundaries trick the human visual system into misjudging distance and perceived object scale",
        "Aerial perspective uses contrast to estimate distance; hazy low-contrast objects appear farther away, prompting the brain to overestimate their size.",
        "دھند اور کہرے میں دور کا لائٹ ہاؤس یا عمارت انسان کو حقیقت سے زیادہ بڑی اور دیوہیکل کیوں دکھائی دیتی ہے؟",
        ["دھند میں مدہم منظر انسانی دماغ کو یہ دھوکہ دیتا ہے کہ عمارت بہت دور ہے، اس لیے دماغ اس کا سائز بڑا تصور کرتا ہے", "دھند دوربین کی طرح کام کرتی ہے", "کہر عمارت کو اونچا اٹھا دیتا ہے", "نمی آنکھ کی پتلی کو موڑ دیتی ہے"],
        "دھند میں مدہم منظر انسانی دماغ کو یہ دھوکہ دیتا ہے کہ عمارت بہت دور ہے، اس لیے دماغ اس کا سائز بڑا تصور کرتا ہے",
        "انسانی دماغ دور کی چیزوں کا سائز ماحولیاتی کنٹراسٹ سے ناپتا ہے۔ دھند میں چیزیں بہت دور لگتی ہیں اس لیے دماغ انہیں غیر معمولی بڑا سمجھتا ہے۔"
    ),
    (
        "Why does an electric hair dryer blow intensely hot air out the front nozzle while keeping its outer plastic housing safe to hold?",
        ["The internal heating element is mounted on mica insulators while a high-velocity fan creates continuous thermal airflow separation", "The plastic is cooled by liquid nitrogen", "Mica coils absorb all electrical heat", "Plastic emits cooling frequencies"],
        "The internal heating element is mounted on mica insulators while a high-velocity fan creates continuous thermal airflow separation",
        "Heat-resistant mica brackets suspend the glowing coil in mid-air, while rapid air intake prevents conductive heat transfer to the exterior shell.",
        "ہیئر ڈرائر (Hair dryer) کے اندر کی تاریں سرخ دہکتی ہیں مگر باہر کا پلاسٹک ہینڈل ہاتھ کو ٹھنڈا اور محفوظ کیوں رہتا ہے؟",
        ["اندرونی کوائل کو میکا شیٹ پر رکھا جاتا ہے اور تیز پنکھا حرارت کو باہر پھینک کر باڈی کو گرم ہونے سے روکتا ہے", "پلاسٹک میں نائٹروجن گیس ہوتی ہے", "میکا حرارت کو ختم کر دیتی ہے", "پلاسٹک ٹھنڈک چھوڑتا ہے"],
        "اندرونی کوائل کو میکا شیٹ پر رکھا جاتا ہے اور تیز پنکھا حرارت کو باہر پھینک کر باڈی کو گرم ہونے سے روکتا ہے",
        "ہیٹنگ کوائل باڈی سے بالکل الگ تھلگ ہوا میں معلق ہوتا ہے، اور پنکھے کا تیز جھونکا ساری گرم ہوا فوراً باہر نکال دیتا ہے۔"
    ),
    (
        "Why does an ordinary automobile windshield wiper leave streak-free clear glass only when the rubber blade is flexible and supple?",
        ["Supple rubber deforms microscopically to maintain continuous uniform contact with the curved glass, wiping water cleanly", "Stiff rubber absorbs water chemically", "Wipers polish glass into diamond", "Rainwater melts supple rubber"],
        "Supple rubber deforms microscopically to maintain continuous uniform contact with the curved glass, wiping water cleanly",
        "A supple blade edge flips its angle on each stroke to squeegee water without skipping across microscopic windshield imperfections.",
        "گاڑی کا وائپر شیشے کو بغیر کسی داغ کے بالکل شفاف تبھی صاف کرتا ہے جب اس کا ربڑ نرم اور لچکدار ہو، کیوں؟",
        ["نرم ربڑ شیشے کے منحنی رخ کے ساتھ چپک کر یکساں رابطہ رکھتا ہے اور پانی کی ہر بوند کو سمیٹ لیتا ہے", "سخت ربڑ پانی کو پی جاتا ہے", "وائپر شیشے کو رگڑ کر ہیرا بناتا ہے", "بارش ربڑ کو نرم کرتی ہے"],
        "نرم ربڑ شیشے کے منحنی رخ کے ساتھ چپک کر یکساں رابطہ رکھتا ہے اور پانی کی ہر بوند کو سمیٹ لیتا ہے",
        "گاڑی کا شیشہ ہلکا سا مڑا ہوا ہوتا ہے۔ سخت ربڑ شیشے کے اتار چڑھاؤ کو چھوڑ دیتا ہے جبکہ نرم ربڑ ہر کونے سے پانی کو مکمل سمیٹتا ہے۔"
    ),
    (
        "Why does an ordinary metal tuning fork produce a pure single musical tone when struck against a rubber pad?",
        ["Its symmetric two-pronged design vibrates in a balanced fundamental mode that suppresses harmonic overtones rapidly", "Rubber creates acoustic echo", "Metal prongs contain tuned electronic chips", "Sound cannot bend through metal arms"],
        "Its symmetric two-pronged design vibrates in a balanced fundamental mode that suppresses harmonic overtones rapidly",
        "The opposing prongs move in opposite directions, canceling out translational forces and quickly damping out all high-frequency overtone modes.",
        "ٹیوننگ فورک (Tuning fork) کو ربڑ کے پیڈ پر مارنے پر وہ شور کی بجائے بالکل خالص اور صاف ایک ہی سر (Tone) کیوں نکالتا ہے؟",
        ["اس کے دونوں متوازی بازو ایک دوسرے کے مخالف جھولتے ہوئے فالتو سروں (Overtones) کو منسوخ کر کے بنیادی سر بناتے ہیں", "ربڑ میں گونج ہوتی ہے", "بازوؤں میں الیکٹرانک چپ ہوتی ہے", "آواز دھات میں مڑ نہیں سکتی"],
        "اس کے دونوں متوازی بازو ایک دوسرے کے مخالف جھولتے ہوئے فالتو سروں (Overtones) کو منسوخ کر کے بنیادی سر بناتے ہیں",
        "ٹیوننگ فورک کا متوازن ڈیزائن شور پیدا کرنے والی غیر ضروری لہروں کو فوراً دبا دیتا ہے اور صرف ایک بنیادی ارتعاش باقی رہتا ہے۔"
    ),
    (
        "Why does a person feeling motion sickness on a boat feel far worse when reading a book inside the windowless cabin?",
        ["Reading fixes eyes on stationary pages while the inner ear senses violent roll and pitch, maximizing sensory conflict", "Books absorb cabin oxygen", "Paper ink emits toxic nauseating vapors", "Reading locks vestibular fluid"],
        "Reading fixes eyes on stationary pages while the inner ear senses violent roll and pitch, maximizing sensory conflict",
        "The visual system informs the brain that the environment is completely motionless, while vestibular canals signal heavy motion, triggering nausea.",
        "کشتی کے کیبن میں بیٹھ کر کتاب پڑھنے سے انسان کو سمندری بیماری (Motion sickness) اور متلی کی شدت کئی گنا زیادہ کیوں ہو جاتی ہے؟",
        ["آنکھیں کتاب کے ساکن صفحے کو دیکھتی ہیں جبکہ اندرونی کان کشتی کی تیز حرکت محسوس کرتے ہیں، جس سے شدید تضاد بنتا ہے", "کتاب آکسیجن نگل لیتی ہے", "سیاہی زہریلی ہوتی ہے", "پڑھنے سے کان کا مائع جم جاتا ہے"],
        "آنکھیں کتاب کے ساکن صفحے کو دیکھتی ہیں جبکہ اندرونی کان کشتی کی تیز حرکت محسوس کرتے ہیں، جس سے شدید تضاد بنتا ہے",
        "جب آنکھیں دماغ کو کہیں کہ سب کچھ ساکن ہے اور کان کہیں کہ ہم گھوم رہے ہیں، تو دماغ سمجھتا ہے کہ جسم میں زہر چلا گیا ہے اور قے کراتا ہے۔"
    ),
    (
        "Why does an airplane require a longer takeoff runway when operating from an airport located high in the mountains?",
        ["Lower atmospheric air density at high elevations produces less aerodynamic lift and reduces engine thrust", "Mountain gravity is stronger", "Runways are inclined uphill", "Aircraft tires deform more"],
        "Lower atmospheric air density at high elevations produces less aerodynamic lift and reduces engine thrust",
        "Air density decreases with altitude; the aircraft must achieve higher true airspeed to generate required takeoff lift.",
        "پہاڑی علاقے میں اونچائی پر واقع ہوائی اڈے پر جہاز کو اڑان بھرنے کے لیے زیادہ لمبا رن وے کیوں درکار ہوتا ہے؟",
        ["بلندی پر ہوا کا دباؤ اور کثافت کم ہونے کی وجہ سے پروں کو لفٹ کم ملتی ہے اور انجن کی طاقت گھٹ جاتی ہے", "پہاڑوں میں کشش ثقل زیادہ ہوتی ہے", "رن وے چڑھائی پر ہوتے ہیں", "ٹائر زیادہ دب جاتے ہیں"],
        "بلندی پر ہوا کا دباؤ اور کثافت کم ہونے کی وجہ سے پروں کو لفٹ کم ملتی ہے اور انجن کی طاقت گھٹ جاتی ہے",
        "پتلی ہوا میں پروں کو جہاز کا وزن اٹھانے کے لیے زیادہ رفتار درکار ہوتی ہے، اس لیے جہاز کو زیادہ لمبا دوڑنا پڑتا ہے۔"
    ),
    (
        "Why does a person using an ordinary hand pump feel it become much harder to push down as the bicycle tire becomes fully inflated?",
        ["Higher internal tire pressure pushes back against the pump plunger face with greater opposing pneumatic force (F = P * A)", "Pump metal expands from heat", "Tire rubber absorbs pump oil", "Air turns into solid friction"],
        "Higher internal tire pressure pushes back against the pump plunger face with greater opposing pneumatic force (F = P * A)",
        "To open the tire valve, the pump cylinder pressure must exceed tire pressure; pushing against high backpressure requires greater force.",
        "سائیکل کے ٹائر میں پمپ سے ہوا بھرتے وقت جوں جوں ٹائر بھرتا جاتا ہے، پمپ کا ہینڈل دبانا اتنا سخت کیوں ہو جاتا ہے؟",
        ["ٹائر کے اندر بڑھتا ہوا ہوا کا دباؤ پمپ کے پسٹن کے خلاف اتنی ہی زیادہ مخالف قوت لگاتا ہے (F = P * A)", "پمپ کا لوہا گرم ہو کر پھیلتا ہے", "ربڑ پمپ کا تیل پی جاتا ہے", "ہوا ٹھوس بن جاتی ہے"],
        "ٹائر کے اندر بڑھتا ہوا ہوا کا دباؤ پمپ کے پسٹن کے خلاف اتنی ہی زیادہ مخالف قوت لگاتا ہے (F = P * A)",
        "ٹائر کا والو کھولنے کے لیے پمپ کے اندر ٹائر سے زیادہ دباؤ بنانا پڑتا ہے، جس کے لیے ہاتھوں کا پورا زور لگانا پڑتا ہے۔"
    ),
    (
        "A thief attempts to pick a mechanical pin-tumbler cylinder lock using two metal tension picks. How does the lock mechanism actually get picked open?",
        ["Rotational shear torque catches misaligned brass pins one by one along the shear line of the cylinder plug", "The pick melts the brass pins", "Picks magnetize the springs", "The plug cracks open by brute force"],
        "Rotational shear torque catches misaligned brass pins one by one along the shear line of the cylinder plug",
        "Manufacturing tolerances mean one pin binds before others; slight rotational torque holds each key pin at the shear line as it is picked.",
        "چور پن ٹمبلر تالے (Pin tumbler lock) کو دو باریک تاروں سے کیسے کھول لیتا ہے؟",
        ["ہلکا سا گھماؤ ڈال کر وہ تالے کے اندرونی پیتل کے پنوں کو ایک ایک کر کے شیئر لائن (Shear line) پر پھنسا لیتا ہے", "تاریں پنوں کو پگھلا دیتی ہیں", "تاریں اسپرنگ کو مقناطیس بناتی ہیں", "تالے کا سلنڈر ٹوٹ جاتا ہے"],
        "ہلکا سا گھماؤ ڈال کر وہ تالے کے اندرونی پیتل کے پنوں کو ایک ایک کر کے شیئر لائن (Shear line) پر پھنسا لیتا ہے",
        "تالے کے سوراخوں میں ایک ملی میٹر کے ہزارویں حصے کا فرق ہوتا ہے۔ ہلکا موڑ دینے پر ایک پن پھنس جاتا ہے، اسے اوپر اٹھاتے ہی تالا کلک کر کے کھل جاتا ہے۔"
    ),
    (
        "A forensic investigator finds two distinct footprints in soft mud: one indented deep at the heel and toe, one indented uniformly flat across the sole. Which footprint belongs to someone running?",
        ["The deep heel and toe indentation, because running generates high dynamic impact forces at strike and push-off", "The flat uniform print", "Neither print indicates speed", "Both prints belong to walking"],
        "The deep heel and toe indentation, because running generates high dynamic impact forces at strike and push-off",
        "Running concentrates body weight dynamically on the rear heel strike and forefoot propulsive toe-off, digging deeply into compliant soil.",
        "کیچڑ میں دو قدموں کے نشان ملے: ایک میں ایڑی اور پنجہ گہرا دھنسا ہوا تھا، دوسرے میں پورا تلوہ بالکل برابر دبا ہوا تھا۔ دوڑنے والے کا نشان کون سا ہے؟",
        ["ایڑی اور پنجے کا گہرا نشان، کیونکہ دوڑتے وقت ٹیک اور دھکا لگانے سے زمین پر شدید متحرک دباؤ پڑتا ہے", "برابر دبا ہوا نشان", "کوئی بھی نشان رفتار نہیں بتاتا", "دونوں چلنے کے نشان ہیں"],
        "ایڑی اور پنجے کا گہرا نشان، کیونکہ دوڑتے وقت ٹیک اور دھکا لگانے سے زمین پر شدید متحرک دباؤ پڑتا ہے",
        "دوڑتے وقت انسان پورا پیر نہیں رکھتا بلکہ ایڑی کی تیز چوٹ لگتی ہے اور پنجے سے اگلا زوردار دھکا لگتا ہے جو مٹی کو گہرا کھود دیتا ہے۔"
    ),
    (
        "A bank vault combination dial has 40 numbers. How many possible combinations exist for a standard 3-number lock?",
        ["64,000 combinations (40 * 40 * 40)", "120 combinations", "400 combinations", "1,600 combinations"],
        "64,000 combinations (40 * 40 * 40)",
        "Each of the 3 independent positions has 40 possibilities: 40^3 = 64,000 discrete combinations.",
        "بینک کی تجوری کے گھومنے والے ڈائل پر 40 ہندسے (0 سے 39) ہیں۔ تین ہندسوں کے خفیہ کوڈ کی کل کتنی ممکنہ ترتیبات (Combinations) ہو سکتی ہیں؟",
        ["64,000 ممکنہ ترتیبات (40 × 40 × 40)", "120 ترتیبات", "400 ترتیبات", "1,600 ترتیبات"],
        "64,000 ممکنہ ترتیبات (40 × 40 × 40)",
        "تین ہندسوں میں سے ہر ایک کے لیے 40 امکانات ہوتے ہیں، یعنی 40 × 40 × 40 = 64,000 ممکنہ خفیہ کوڈ بنتے ہیں۔"
    ),
    (
        "A detective discovers a room where a man hanged himself from a ceiling beam 12 feet high. There is no chair, ladder, or table in the empty room, but a large puddle of water is centered directly beneath the hanging body. How did he reach the rope?",
        ["He stood atop a giant block of solid ice that melted away into water", "He jumped from the window", "Someone lifted him", "He climbed the bare wall"],
        "He stood atop a giant block of solid ice that melted away into water",
        "A giant block of ice supported his weight while tying the noose, then liquefied into room-temperature water.",
        "بارہ فٹ اونچی چھت سے ایک لاش لٹکی ہوئی ملی۔ کمرے میں کوئی کرسی، میز یا سیڑھی نہ تھی، مگر لاش کے عین نیچے فرش پر پانی کا بڑا تالاب بنا ہوا تھا۔ وہ پھندے تک کیسے پہنچا؟",
        ["وہ برف کی ایک بڑی وزنی سلی پر کھڑا ہوا تھا جو پگھل کر پانی بن گئی", "اس نے کھڑکی سے چھلانگ لگائی", "کسی نے اسے اٹھایا", "وہ سیدھی دیوار پر چڑھا"],
        "وہ برف کی ایک بڑی وزنی سلی پر کھڑا ہوا تھا جو پگھل کر پانی بن گئی",
        "پھندا ڈالنے کے لیے وہ برف کی اونچی چٹان پر چڑھا تھا، جس کے پگھلنے کے بعد صرف پانی کا تالاب رہ گیا اور تمام شواہد غائب ہو گئے۔"
    ),
    (
        "A submarine commander navigates undersea for three months without surfacing. How do atomic submarines generate fresh breathable oxygen for the crew from seawater?",
        ["Electrolysis of desalinated water splits H2O molecules into breathable oxygen gas and discharged hydrogen (2 H2O -> 2 H2 + O2)", "They carry compressed air tanks only", "Chemical algae absorbs CO2", "They filter oxygen dissolved in fish"],
        "Electrolysis of desalinated water splits H2O molecules into breathable oxygen gas and discharged hydrogen (2 H2O -> 2 H2 + O2)",
        "Nuclear reactor electricity powers electrolytic cells, cracking water molecules to provide an unlimited supply of pure oxygen.",
        "ایٹمی آبدوزیں تین ماہ تک سطح پر آئے بغیر زیر آب رہتی ہیں۔ وہ عملے کے سانس لینے کے لیے سمندری پانی سے آکسیجن کیسے بناتی ہیں؟",
        ["میٹھے کیے گئے پانی کی الیکٹرولائسز (Electrolysis) کے ذریعے پانی کے مالیکیولز کو توڑ کر آکسیجن گیس بنائی جاتی ہے (2 H2O -> 2 H2 + O2)", "وہ صرف ہوا کے ٹینک لے جاتی ہیں", "کائی کاربن ڈائی آکسائیڈ پیتی ہے", "وہ مچھلیوں کی آکسیجن چھانتی ہیں"],
        "میٹھے کیے گئے پانی کی الیکٹرولائسز (Electrolysis) کے ذریعے پانی کے مالیکیولز کو توڑ کر آکسیجن گیس بنائی جاتی ہے (2 H2O -> 2 H2 + O2)",
        "ایٹمی ری ایکٹر کی وافر بجلی سے پانی میں برقی رو گزاری جاتی ہے جس سے ہائیڈروجن باہر خارج ہو جاتی ہے اور خالص آکسیجن کیبن میں بھر دی جاتی ہے۔"
    ),
    (
        "Why does a person who drinks sea water when stranded on an ocean life raft die of severe dehydration faster than drinking nothing at all?",
        ["Seawater's hypertonic salinity forces human kidneys to excrete more water in urine than was ingested to flush excess sodium", "Salt cuts stomach lining", "Seawater turns blood into solid crystals", "Seawater contains bacterial venom"],
        "Seawater's hypertonic salinity forces human kidneys to excrete more water in urine than was ingested to flush excess sodium",
        "Human kidneys can only concentrate urine to ~2% salt, whereas seawater is ~3.5% salt. Drinking it draws internal body water to excrete the salt.",
        "سمندر میں پھنسا پیاسا انسان نمکین پانی پینے سے بغیر کچھ پیے رہنے کے مقابلے میں زیادہ تیزی سے پیاس اور پانی کی کمی (Dehydration) سے کیوں مر جاتا ہے؟",
        ["سمندری پانی کا نمک گردوں کو اس نمک کو پیشاب کے راستے خارج کرنے کے لیے پئے گئے پانی سے زیادہ جسمانی پانی ضائع کرنے پر مجبور کرتا ہے", "نمک معدے کو کاٹ دیتا ہے", "خون جم کر قلمیں بن جاتا ہے", "پانی میں زہر ہوتا ہے"],
        "سمندری پانی کا نمک گردوں کو اس نمک کو پیشاب کے راستے خارج کرنے کے لیے پئے گئے پانی سے زیادہ جسمانی پانی ضائع کرنے پر مجبور کرتا ہے",
        "انسانی گردے سمندری نمک جتنا گاڑھا پیشاب نہیں بنا سکتے۔ اضافی نمک نکالنے کے لیے گردے خلیات کا بچا کچا پانی بھی نچوڑ لیتے ہیں جس سے انسان فوراً مر جاتا ہے۔"
    ),
    (
        "Why do birds perched on telephone wires space themselves at roughly equal distances from one another?",
        ["Individual visual personal space (individual distance) balances social flocking instinct with peck-avoidance territorial margin", "Electrical repulsion separates their feathers", "Wires have equal magnetic notches", "To balance the wire's physical load"],
        "Individual visual personal space (individual distance) balances social flocking instinct with peck-avoidance territorial margin",
        "Ethological individual distance ensures each bird stays just outside the pecking reach of its neighbor while retaining flock safety.",
        "تار پر بیٹھے پرندے ایک دوسرے سے تقریباً برابر فاصلے پر لائن بنا کر کیوں بیٹھتے ہیں؟",
        ["ہر پرندہ ایک مخصوص ذاتی فاصلہ (Individual distance) برقرار رکھتا ہے تاکہ پڑوسی کی چونچ کی مار سے محفوظ رہ سکے", "تار کی بجلی ان کے پروں کو دور دھکیلتی ہے", "تار میں مقناطیسی نشان ہوتے ہیں", "تار کا وزن برابر رکھنے کے لیے"],
        "ہر پرندہ ایک مخصوص ذاتی فاصلہ (Individual distance) برقرار رکھتا ہے تاکہ پڑوسی کی چونچ کی مار سے محفوظ رہ سکے",
        "جانوروں کی نفسیات میں ہر پرندے کی اپنی ایک ذاتی حد ہوتی ہے۔ وہ ایک دوسرے کے اتنے قریب بیٹھتے ہیں جہاں حملہ نہ ہو سکے مگر جھنڈ کی حفاظت بھی ملے۔"
    ),
    (
        "A bank teller is handed a stack of one hundred $100 bills. The teller flips through them with wet fingers and instantly flags one bill as counterfeit without holding it to UV light. How?",
        ["The counterfeit bill lacked the distinctive tactile intaglio raised-ink texture and genuine rag cotton-linen paper snap", "The bill smelled of petroleum", "The serial number had 13 digits", "The president's face was smiling"],
        "The counterfeit bill lacked the distinctive tactile intaglio raised-ink texture and genuine rag cotton-linen paper snap",
        "Authentic currency is printed on 75% cotton / 25% linen using high-pressure intaglio presses, leaving distinctive raised ink ridges recognizable by touch.",
        "بینک کیشیئر نے نوٹوں کی گڈی گنتے ہی بغیر الٹرا وائلٹ لائٹ کے ایک نوٹ کو ہاتھ کے لمس سے جعلی قرار دے دیا۔ اس نے کیا محسوس کیا؟",
        ["اصلی نوٹ کے ابھرے ہوئے حروف کی کھردرائی (Intaglio print) اور سوتی کپڑے کے کاغذ کی مخصوص کھنک غائب تھی", "نوٹ سے پیٹرول کی بو آ رہی تھی", "سیریل نمبر میں 13 ہندسے تھے", "نوٹ پر بنی تصویر مسکرا رہی تھی"],
        "اصلی نوٹ کے ابھرے ہوئے حروف کی کھردرائی (Intaglio print) اور سوتی کپڑے کے کاغذ کی مخصوص کھنک غائب تھی",
        "اصلی کرنسی عام لکڑی کے کاغذ پر نہیں بلکہ 75 فیصد کاٹن اور لنن کے کپڑے پر شدید دباؤ کے ساتھ چھاپی جاتی ہے جس کی کھردرائی انگلیاں فوراً پہچان لیتی ہیں۔"
    ),
    (
        "Why does an ordinary automobile engine hesitate and stall if you accidentally pour diesel fuel into a standard gasoline engine tank?",
        ["Diesel fuel has a much higher flash point and lower volatility, failing to vaporize and ignite via gasoline spark plugs", "Diesel fuel freezes into solid wax at room temperature", "Diesel melts the rubber fuel lines instantly", "Gasoline spark plugs repel diesel chemically"],
        "Diesel fuel has a much higher flash point and lower volatility, failing to vaporize and ignite via gasoline spark plugs",
        "Gasoline engines require easily vaporized fuel ignited by electric sparks; diesel requires high cylinder compression heat (15:1 to 20:1) to auto-ignite.",
        "پیٹرول والی عام کار میں اگر غلطی سے ڈیزل بھر دیا جائے تو انجن چند گز بعد ہچکولے کھا کر بند کیوں ہو جاتا ہے؟",
        ["ڈیزل گاڑھا اور کم اڑنے والا ہوتا ہے جو پیٹرول انجن کے سپارک پلگ کی ہلکی چنگاری سے آگ نہیں پکڑ پاتا", "ڈیزل کمرے کے درجہ حرارت پر جم جاتا ہے", "ڈیزل نالیوں کو پگھلا دیتا ہے", "پلگ ڈیزل کو دھکیل دیتے ہیں"],
        "ڈیزل گاڑھا اور کم اڑنے والا ہوتا ہے جو پیٹرول انجن کے سپارک پلگ کی ہلکی چنگاری سے آگ نہیں پکڑ پاتا",
        "پیٹرول بخارات بن کر چنگاری سے جلتا ہے، جبکہ ڈیزل کو جلنے کے لیے شدید دباؤ اور گرمی درکار ہوتی ہے۔ پلگ کی چنگاری ڈیزل کو جلانے میں ناکام رہتی ہے۔"
    ),
    (
        "Why does an arch bridge get stronger as more weight is placed directly on top of its center keystone?",
        ["The downward weight forces the arch stones into tighter compression", "Concrete expands under pressure", "The foundations move closer together", "Friction turns into adhesive glue"],
        "The downward weight forces the arch stones into tighter compression",
        "Arches channel vertical loads into compressive lateral forces, pressing stone blocks tightly together.",
        "محرابی پل کے درمیانی پتھر (Keystone) پر جب زیادہ وزن پڑتا ہے تو وہ زیادہ مضبوط کیوں ہو جاتا ہے؟",
        ["اوپر کا وزن محراب کے پتھروں کو مزید دبا کر جوڑ دیتا ہے", "دباؤ سے کنکریٹ پھیلتا ہے", "پل کی بنیادیں قریب آ جاتی ہیں", "رگڑ گوند کا کام کرتی ہے"],
        "اوپر کا وزن محراب کے پتھروں کو مزید دبا کر جوڑ دیتا ہے",
        "محراب عمودی وزن کو بغلی دباؤ میں بدل دیتی ہے جس سے تمام پتھر آپس میں مزید سختی سے جڑ جاتے ہیں۔"
    ),
    (
        "Why do suspension bridge cables hang in a parabolic curve rather than a straight line?",
        ["The cable supports a uniformly distributed horizontal deck load", "Gravity pulls the center down only", "Wind resistance forces that shape", "Thermal expansion stretches the steel"],
        "The cable supports a uniformly distributed horizontal deck load",
        "A cable supporting a deck of uniform weight per horizontal length naturally assumes a parabola.",
        "معلق پل (Suspension bridge) کے وزنی تار سیدھی لکیر کی بجائے محرابی منحنی (Parabola) کیوں بناتے ہیں؟",
        ["کیونکہ وہ افقی پل کا یکساں بوجھ سنبھالتے ہیں", "کشش ثقل صرف مرکز کو کھینچتی ہے", "ہوا کا دباؤ اس شکل پر مجبور کرتا ہے", "گرمی سے تار لٹک جاتے ہیں"],
        "کیونکہ وہ افقی پل کا یکساں بوجھ سنبھالتے ہیں",
        "جب تار پر افقی طور پر یکساں وزن ڈالا جائے تو ریاضیاتی طور پر وہ پیرابولا کی شکل اختیار کرتا ہے۔"
    ),
    (
        "In a forensic investigation, why do tiny spherical blood droplets indicate an impact angle close to 90 degrees?",
        ["Surface tension maintains a circular perimeter when kinetic force strikes perpendicular to the surface", "Gravity flattens droplets sideways", "Speed causes blood to elongate", "Coagulation rounds the edges"],
        "Surface tension maintains a circular perimeter when kinetic force strikes perpendicular to the surface",
        "At a right angle impact, liquid surface tension disperses symmetrically into a circle with an aspect ratio of 1.0.",
        "فرانزک تفتیش میں خون کے گول قطرے کس بات کا ثبوت ہوتے ہیں کہ وہ فرش پر 90 ڈگری کے زاویے سے گرے؟",
        ["سطحی تناؤ (Surface tension) عمودی ٹکراؤ پر گولائی برقرار رکھتا ہے", "کشش ثقل قطروں کو پہلو سے چپٹا کرتی ہے", "رفتار خون کو لمبوترا کر دیتی ہے", "جمنے کی وجہ سے کنارے گول ہوتے ہیں"],
        "سطحی تناؤ (Surface tension) عمودی ٹکراؤ پر گولائی برقرار رکھتا ہے",
        "جب خون کا قطرہ بالکل سیدھا اوپر سے نیچے گرتا ہے تو رقبہ یکساں پھیل کر بالکل دائرہ نما رہتا ہے۔"
    ),
    (
        "Why does an audio recording of your own voice sound higher-pitched and unfamiliar when played back?",
        ["You normally hear your voice through vibrating skull bones that emphasize deep bass frequencies", "The microphone records at wrong frequency", "Speakers invert audio polarity", "Ambient room echo alters the pitch"],
        "You normally hear your voice through vibrating skull bones that emphasize deep bass frequencies",
        "Bone conduction transmits lower acoustic resonances directly to the inner ear; external recordings capture only airborne sound.",
        "ریکارڈنگ میں اپنی آواز سن کر انسان کو عجیب اور زیادہ باریک کیوں لگتی ہے؟",
        ["کیونکہ بولتے وقت ہم اپنی آواز کھوپڑی کی ہڈیوں کے اندرونی ارتعاش سے گہری سنتے ہیں", "مائیکروفون غلط فریکوئنسی ریکارڈ کرتا ہے", "سپیکر آواز کو الٹ دیتا ہے", "کمرے کی گونج آواز بدل دیتی ہے"],
        "کیونکہ بولتے وقت ہم اپنی آواز کھوپڑی کی ہڈیوں کے اندرونی ارتعاش سے گہری سنتے ہیں",
        "بولتے ہوئے کھوپڑی کی ہڈیاں نچلی اور بھاری آوازیں اندرونی کان تک پہنچاتی ہیں، جبکہ ہوا کے ذریعے صرف بیرونی آواز ریکارڈ ہوتی ہے۔"
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
        "Why does an ocean ship sail forward even when the wind is blowing diagonally from the side (tacking against the wind)?",
        ["The curved sails act like vertical airplane wings creating forward aerodynamic lift while the deep underwater keel resists sideways sliding", "Wind pushes the deck directly", "Tides pull ships against wind", "The crew rows with underwater oars"],
        "The curved sails act like vertical airplane wings creating forward aerodynamic lift while the deep underwater keel resists sideways sliding",
        "Bernoulli lift across trimmed sails creates a force with a forward vector component; the keel provides massive lateral hydrodynamic resistance.",
        "بادبانی جہاز ہوا سامنے یا پہلو سے آنے کے باوجود ہوا کے رخ کے مخالف آگے کیسے بڑھ جاتا ہے؟",
        ["بادبان عمودی پروں کی طرح آگے کی طرف ائیروڈائنامک لفٹ بناتے ہیں اور پیندے کا تختہ (Keel) جہاز کو پہلو میں بہنے سے روکتا ہے", "ہوا جہاز کے ڈیک کو دھکیلتی ہے", "لہریں جہاز کو کھینچتی ہیں", "جہاز کے ملاح زیر آب چپو چلاتے ہیں"],
        "بادبان عمودی پروں کی طرح آگے کی طرف ائیروڈائنامک لفٹ بناتے ہیں اور پیندے کا تختہ (Keel) جہاز کو پہلو میں بہنے سے روکتا ہے",
        "بادبان ہوائی جہاز کے پر کی طرح کام کرتا ہے جو کم دباؤ سے آگے کھینچتا ہے۔ پیندے کا لمبا تختہ پانی کو کاٹ کر جہاز کو سیدھا آگے جانے پر مجبور کرتا ہے۔"
    ),
    (
        "Why does an ordinary automobile alternator generate alternating current (AC) internally, even though the car's electrical battery is direct current (DC)?",
        ["AC is far easier and more reliable to generate mechanically using rotating magnetic fields, which diodes then rectify into DC", "DC generators explode at high speeds", "Car batteries prefer AC charging", "Alternator belts only spin in AC"],
        "AC is far easier and more reliable to generate mechanically using rotating magnetic fields, which diodes then rectify into DC",
        "A brushless alternator rotor spins past stationary stator windings without heavy wear; a built-in diode bridge rectifier converts the 3-phase AC into 12V DC.",
        "گاڑی کا الٹرنیٹر (Alternator) اندر سے اے سی (AC) کرنٹ پیدا کرتا ہے حالانکہ گاڑی کی بیٹری اور پورا سسٹم ڈی سی (DC) پر چلتا ہے، کیوں؟",
        ["گھومتے ہوئے مقناطیس سے اے سی بنانا انتہائی پائیدار اور آسان ہوتا ہے، جسے ڈائیوڈز کی مدد سے ڈی سی میں بدل لیا جاتا ہے", "ڈی سی جنریٹر تیز رفتاری پر پھٹ جاتے ہیں", "بیٹری اے سی کرنٹ مانگتی ہے", "بیلٹ صرف اے سی گھومتی ہے"],
        "گھومتے ہوئے مقناطیس سے اے سی بنانا انتہائی پائیدار اور آسان ہوتا ہے، جسے ڈائیوڈز کی مدد سے ڈی سی میں بدل لیا جاتا ہے",
        "ڈی سی جنریٹر میں رگڑ والے برش جلد گھس جاتے ہیں، جبکہ اے سی الٹرنیٹر سالہا سال بغیر دیکھ بھال چلتا ہے اور اس کا ریکٹیفائر کرنٹ کو ڈی سی بنا دیتا ہے۔"
    ),
    (
        "Why does a large cargo barge travel faster when fully loaded down in the water than an identical empty barge in a strong headwind?",
        ["The immense aerodynamic windage resistance on the high slab-sided empty hull exceeds the added hydrodynamic friction of the submerged loaded hull", "Heavy barges sink to fast currents", "Empty barges lose engine traction", "Water pushes loaded barges forward"],
        "The immense aerodynamic windage resistance on the high slab-sided empty hull exceeds the added hydrodynamic friction of the submerged loaded hull",
        "An empty barge exposes a massive vertical flat surface to headwinds like a parachute; a laden hull sits low in the water, presenting minimal wind cross-section.",
        "سامنے سے چلتی تیز آندھی میں سامان سے لدا ہوا بھاری جہاز خالی جہاز کے مقابلے میں زیادہ آسانی اور تیزی سے آگے کیسے نکل جاتا ہے؟",
        ["خالی جہاز کی اونچی دیواریں آندھی میں پیراشوٹ کی طرح ہوا کو روکتی ہیں جبکہ لدا ہوا جہاز پانی میں نیچے بیٹھ کر ہوا سے بچ جاتا ہے", "بھاری جہاز تیز لہروں میں ڈوب جاتا ہے", "خالی جہاز کے انجن پھسلتے ہیں", "پانی لدے ہوئے جہاز کو دھکیلتا ہے"],
        "خالی جہاز کی اونچی دیواریں آندھی میں پیراشوٹ کی طرح ہوا کو روکتی ہیں جبکہ لدا ہوا جہاز پانی میں نیچے بیٹھ کر ہوا سے بچ جاتا ہے",
        "خالی جہاز کا بڑا حصہ پانی سے باہر نکل کر ہوا کے لیے ایک بڑی دیوار بن جاتا ہے جو اسے پیچھے دھکیلتی ہے، جبکہ بھاری جہاز پانی میں چھپ کر ہوا کی رکاوٹ کم کر دیتا ہے۔"
    ),
    (
        "Why do birds flying in a flock in a 'V' formation conserve significant metabolic energy during long migratory flights?",
        ["Trailing birds fly in the upwash wingtip vortex created by the leading bird, gaining aerodynamic free lift", "The leader cuts through clouds", "Birds push each other with air gusts", "The V-shape blocks geomagnetic pull"],
        "Trailing birds fly in the upwash wingtip vortex created by the leading bird, gaining aerodynamic free lift",
        "Wingtip vortices generate an upwash field just outside the wingtip; positioning in this zone reduces the induced drag and heart rate of trailing birds.",
        "ہجرت کرنے والے پرندے آسمان پر 'V' کی شکل بنا کر اڑتے ہوئے اپنی توانائی کی زبردست بچت کیسے کرتے ہیں؟",
        ["پیچھے اڑنے والا ہر پرندہ آگے والے کے پروں کے سرے سے بننے والی اٹھتی ہوئی ہوا (Upwash vortex) سے مفت لفٹ حاصل کرتا ہے", "آگے والا پرندہ بادلوں کو کاٹتا ہے", "پرندے ایک دوسرے کو ہوا سے دھکیلتے ہیں", "یہ شکل زمین کی مقناطیسیت روکتی ہے"],
        "پیچھے اڑنے والا ہر پرندہ آگے والے کے پروں کے سرے سے بننے والی اٹھتی ہوئی ہوا (Upwash vortex) سے مفت لفٹ حاصل کرتا ہے",
        "پر کے کنارے سے ہوا اوپر کی طرف چکر کاٹتی ہے، پیچھے والا پرندہ اس ابھرتی ہوا پر سوار ہو کر بغیر زیادہ پر ہلائے پرواز کرتا رہتا ہے۔"
    ),
    (
        "Why does an ocean tsunami cause seawater at the beach to suddenly recede and expose hundreds of yards of seabed minutes before the giant wave hits?",
        ["If the tsunami wave crest is preceded by its leading trough, the oceanic depression draws coastal water seaward to feed the wave amplitude", "The seafloor opens up massive cracks", "Evaporation boils the coast dry", "Ocean winds push water backwards"],
        "If the tsunami wave crest is preceded by its leading trough, the oceanic depression draws coastal water seaward to feed the wave amplitude",
        "A tsunami is a wave train; when a subduction earthquake causes initial downward crustal displacement, the leading trough arrives first, sucking the shoreline dry.",
        "سونامی کی دیوہیکل لہر ٹکرانے سے چند منٹ پہلے ساحل کا سمندر اچانک پیچھے ہٹ کر سیکڑوں گز تک سمندر کی تہہ کو ننگا کیوں کر دیتا ہے؟",
        ["اگر سونامی لہر کا نچلا گڑھا (Trough) چوٹی سے پہلے ساحل پر پہنچے تو وہ پانی کو لہر کی طرف پیچھے چوس لیتا ہے", "سمندر کی تہہ میں بڑی دراڑ کھل جاتی ہے", "شدید بخارات ساحل کا پانی سکھا دیتے ہیں", "طوفانی ہوا پانی کو پیچھے اڑا لے جاتی ہے"],
        "اگر سونامی لہر کا نچلا گڑھا (Trough) چوٹی سے پہلے ساحل پر پہنچے تو وہ پانی کو لہر کی طرف پیچھے چوس لیتا ہے",
        "لہر کی ایک چوٹی اور ایک گہرائی ہوتی ہے۔ جب زلزلے سے سمندر میں نیچے خلا بنتا ہے تو لہر کا گہرا حصہ ساحل پر پہلے پہنچ کر سمندر کو پیچھے کھینچ لیتا ہے۔"
    ),
    (
        "Why does a glass bottle filled completely to the brim with water and sealed tightly with a cap shatter into pieces when left inside a freezer?",
        ["Water expands by roughly 9 percent upon freezing into ice, generating thousands of atmospheres of hydrostatic pressure against rigid glass", "Ice generates corrosive acids", "Glass contracts and explodes inward", "Freezing boils the bottle bottom"],
        "Water expands by roughly 9 percent upon freezing into ice, generating thousands of atmospheres of hydrostatic pressure against rigid glass",
        "Water's anomalous volumetric expansion upon crystalline solidification exerts pressures exceeding 2,000 atmospheres, shattering rigid containers.",
        "پانی سے لبالب بھر کر مضبوطی سے بند کی گئی شیشے کی بوتل فریزر میں رکھنے پر پھٹ کر ٹکڑے ٹکڑے کیوں ہو جاتی ہے؟",
        ["پانی جم کر برف بنتے وقت 9 فیصد پھیلتا ہے جس سے شیشے پر ہزاروں کلو کا زبردست اندرونی دباؤ بنتا ہے جو بوتل توڑ دیتا ہے", "برف شیشے کو تیزاب سے جلا دیتی ہے", "شیشہ سردی میں سکڑ کر پھٹ جاتا ہے", "برف شیشے کے پیندے کو ابال دیتی ہے"],
        "پانی جم کر برف بنتے وقت 9 فیصد پھیلتا ہے جس سے شیشے پر ہزاروں کلو کا زبردست اندرونی دباؤ بنتا ہے جو بوتل توڑ دیتا ہے",
        "برف بنتے وقت پانی کا حجم بڑھتا ہے۔ اگر برتن میں ہوا کی خالی جگہ نہ ہو تو برف کی طاقتور قوت شیشے کو بغیر کسی مزاحمت کے توڑ کر رکھ دیتی ہے۔"
    ),
    (
        "Why does an airplane cabin feel dry and cause passengers' throats and skin to dehydrate rapidly during a long intercontinental flight?",
        ["Outside air drawn into the cabin at cruising altitude (-50°C) contains virtually zero absolute humidity, which remains parched when heated", "Air conditioning absorbs human moisture", "Jet fuel combustion dries out the air", "Cabin air pressure evaporates sweat instantly"],
        "Outside air drawn into the cabin at cruising altitude (-50°C) contains virtually zero absolute humidity, which remains parched when heated",
        "At 35,000 feet, ambient air is frigid and cannot hold moisture; heating it to 22°C drops relative cabin humidity below 10-15%, drier than most deserts.",
        "لمبی بین البراعظمی پرواز کے دوران ہوائی جہاز کا کیبن اتنا خشک کیوں محسوس ہوتا ہے اور مسافروں کے گلے اور جلد سوکھنے کیوں لگتی ہے؟",
        ["بلندی پر باہر کی منفی 50 ڈگری سرد ہوا میں نمی بالکل صفر ہوتی ہے، گرم کرنے کے بعد کیبن کی ہوا صحرا سے بھی زیادہ خشک ہو جاتی ہے", "ائیر کنڈیشنر انسانوں کی نمی چوس لیتا ہے", "پیٹرول کا دھواں ہوا خشک کرتا ہے", "کیبن کا دباؤ پسینہ اڑا دیتا ہے"],
        "بلندی پر باہر کی منفی 50 ڈگری سرد ہوا میں نمی بالکل صفر ہوتی ہے، گرم کرنے کے بعد کیبن کی ہوا صحرا سے بھی زیادہ خشک ہو جاتی ہے",
        "بلندی پر شدید سردی میں ہوا نمی برقرار نہیں رکھ سکتی۔ جب یہ خشک ہوا اندر لا کر گرم کی جاتی ہے تو کیبن میں نمی 10 فیصد سے بھی کم رہ جاتی ہے۔"
    ),
    (
        "Why does a diver in deep ocean waters feel pressure in their ears during descent that can be relieved by swallowing or yawning?",
        ["Swallowing opens the Eustachian tubes, equalizing middle-ear cavity air pressure with external hydrostatic water pressure", "Swallowing drains water from the ears", "Yawning cools the auditory canals", "Swallowing resets ear balance"],
        "Swallowing opens the Eustachian tubes, equalizing middle-ear cavity air pressure with external hydrostatic water pressure",
        "Water pressure pushes the tympanic membrane inward; opening the pharyngotympanic tubes allows air from the nasopharynx to re-pressurize the middle ear.",
        "سمندر میں غوطہ لگاتے ہوئے جیسے جیسے انسان گہرائی میں اترتا ہے اس کے کانوں پر شدید دباؤ بنتا ہے جسے تھوک نگلنے سے سکون کیسے ملتا ہے؟",
        ["تھوک نگلنے سے یوسٹاچین نالیاں (Eustachian tubes) کھل جاتی ہیں جو کان کے درمیانی حصے کی ہوا کو پانی کے دباؤ کے برابر کر دیتی ہیں", "تھوک نگلنے سے کان سے پانی باہر نکلتا ہے", "جمائی لینے سے کان ٹھنڈے ہوتے ہیں", "نگلنے سے کان کا توازن بحال ہوتا ہے"],
        "تھوک نگلنے سے یوسٹاچین نالیاں (Eustachian tubes) کھل جاتی ہیں جو کان کے درمیانی حصے کی ہوا کو پانی کے دباؤ کے برابر کر دیتی ہیں",
        "پانی کا دباؤ کان کے پردے کو اندر دباتا ہے جس سے درد ہوتا ہے۔ تھوک نگلنے سے حلق سے ہوا کان کے پردے کے پیچھے پہنچ کر دباؤ برابر کر دیتی ہے۔"
    ),
    (
        "Why does an ordinary lead-acid car battery lose significant cranking power on a freezing winter morning?",
        ["Low temperature slows internal chemical electrochemical kinetics and increases the internal resistance of the liquid sulfuric acid electrolyte", "Cold freezes the lead plates solid", "Gasoline evaporates into the battery", "Car alternator drains battery in cold"],
        "Low temperature slows internal chemical electrochemical kinetics and increases the internal resistance of the liquid sulfuric acid electrolyte",
        "Arrhenius reaction rates decrease with temperature; at -18°C, a battery delivers less than half its room-temperature cranking amps.",
        "سردیوں کی ٹھنڈی صبح گاڑی کی بیٹری کا سلف (Cranking power) اتنا کمزور اور سست کیوں ہو جاتا ہے؟",
        ["سردی سے بیٹری کے اندر الیکٹرو کیمیائی ردعمل کی رفتار سست ہو جاتی ہے اور تیزاب کی اندرونی برقی مزاحمت بڑھ جاتی ہے", "سردی سے لیڈ کی پلیٹیں جم جاتی ہیں", "پیٹرول بیٹری کے اندر گھس جاتا ہے", "الٹرنیٹر بیٹری کو چوس لیتا ہے"],
        "سردی سے بیٹری کے اندر الیکٹرو کیمیائی ردعمل کی رفتار سست ہو جاتی ہے اور تیزاب کی اندرونی برقی مزاحمت بڑھ جاتی ہے",
        "کیمیائی تعاملات سردی میں سست پڑ جاتے ہیں۔ منفی درجہ حرارت پر بیٹری عام طاقت کے مقابلے میں آدھی سے بھی کم بجلی خارج کر پاتی ہے۔"
    )
]

print(f"Normal Batch B2 loaded: {len(ITEMS)} items.")
