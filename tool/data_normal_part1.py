# -*- coding: utf-8 -*-
"""
Normal Part 1: Items 1 to 112
Everyday physics, mechanics, forensics, and lateral deduction puzzles.
8-tuple format: (q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    # 1: Siphon water hose
    (
        "How does a flexible plastic siphon hose drain water up and over the rim of an aquarium into a lower bucket without an electric pump?",
        ["Liquid cohesion and gravity in the longer discharge leg pull water over the crest continuously", "Capillary action alone", "Air bubbles push it", "Water boils inside tube"],
        "Liquid cohesion and gravity in the longer discharge leg pull water over the crest continuously",
        "The hydrostatic weight difference in the longer discharge tube creates a continuous pressure deficit pulling fluid over the crest.",
        "بغیر کسی موٹر کے ربڑ کے پائپ (سائفن) سے مچھلیوں کے ٹینک کا پانی اوپر کنارے سے گزار کر نیچے بالٹی میں کیسے نکلتا ہے؟",
        ["پانی کے سالماتی ربط اور نچلے سرے پر کشش ثقل کے کھنچاؤ کی وجہ سے", "کیپلیری ایکشن سے", "ہوا کے بلبلوں کے دباؤ سے", "پانی ابلنے سے"],
        "پانی کے سالماتی ربط اور نچلے سرے پر کشش ثقل کے کھنچاؤ کی وجہ سے",
        "پائپ کا نچلا سرا جب پانی کی سطح سے نیچا ہو تو کشش ثقل کا بہاؤ پانی کو اوپر کھینچ کر نکالتا رہتا ہے۔"
    ),
    # 2: Uphill bicycle gears
    (
        "Why does shifting a bicycle into a small front chainring and a large rear cog make pedaling up a steep hill effortless?",
        ["It trades pedaling distance for increased axle torque leverage", "It makes the bicycle lighter", "It speeds up wheel rotation", "It reduces gravity"],
        "It trades pedaling distance for increased axle torque leverage",
        "Mechanical gear advantage multiplies driving axle torque at the expense of higher pedaling cadence revolutions.",
        "سائیکل پر اونچی چڑھائی چڑھتے وقت آگے کا چھوٹا گیئر اور پیچھے کا بڑا گیئر لگانے سے پیڈل مارنا آسان کیوں ہو جاتا ہے؟",
        ["یہ رفتار کی قربانی دے کر پہیے کو گھمانے کا مکینیکل ٹارک (زور) بڑھا دیتا ہے", "سائیکل کا وزن کم ہو جاتا ہے", "پہیے تیزی سے گھومتے ہیں", "کشش ثقل کم ہو جاتی ہے"],
        "یہ رفتار کی قربانی دے کر پہیے کو گھمانے کا مکینیکل ٹارک (زور) بڑھا دیتا ہے",
        "بڑے گیئر کی وجہ سے پیڈل کا زور کئی گنا بڑھ کر پہیے تک پہنچتا ہے جس سے چڑھائی آسان ہو جاتی ہے۔"
    ),
    # 3: Sailboat tacking against headwind
    (
        "How can a modern triangular-rigged sailing boat navigate forward in a zig-zag trajectory against an opposing headwind?",
        ["The curved sail generates aerodynamic lift like an airplane wing, combined with keel water resistance", "Pushing against ocean waves", "Rowing under deck", "Wind turns around the hull"],
        "The curved sail generates aerodynamic lift like an airplane wing, combined with keel water resistance",
        "Sails act as vertical airfoils producing forward lift vectors, while the underwater keel prevents lateral leeway drift.",
        "بادبانی کشتی مخالف سمت سے آنے والی ہوا کے باوجود ٹیڑھے میڑھے راستے پر آگے کیسے بڑھتی ہے؟",
        ["کشتی کا بادبان ہوائی جہاز کے پر کی طرح لفٹ پیدا کرتا ہے اور نیچے کا کِیل پھسلنے سے روکتا ہے", "پانی کی لہروں پر تیر کر", "اندر چپو چلا کر", "ہوا کا رخ بدل کر"],
        "کشتی کا بادبان ہوائی جہاز کے پر کی طرح لفٹ پیدا کرتا ہے اور نیچے کا کِیل پھسلنے سے روکتا ہے",
        "بادبان سے پیدا ہونے والا ایروڈائنامک پریشر اور نیچے کی وزنی پتی مل کر کشتی کو مخالف ہوا میں آگے دھکیلتے ہیں۔"
    ),
    # 4: Fresh vs salt water ship draft
    (
        "When a heavily loaded cargo container vessel sails from the Atlantic Ocean into a freshwater river port, what happens to its waterline draft?",
        ["The ship sinks slightly deeper into the water because freshwater has lower buoyant density", "The ship rises higher", "The draft remains exactly identical", "The ship capsizes"],
        "The ship sinks slightly deeper into the water because freshwater has lower buoyant density",
        "Less dense fresh water requires the displacement of a greater volume to equal the vessel's displacement tonnage.",
        "جب سمندر سے کوئی بھاری مال بردار بحری جہاز میٹھے پانی کے دریا کی بندرگاہ میں داخل ہوتا ہے تو اس پر کیا اثر پڑتا ہے؟",
        ["جہاز پانی میں ذرا زیادہ گہرائی میں دھنس جاتا ہے کیونکہ میٹھے پانی کی کثافت کم ہوتی ہے", "جہاز اوپر اٹھ جاتا ہے", "کوئی فرق نہیں پڑتا", "جہاز الٹ جاتا ہے"],
        "جہاز پانی میں ذرا زیادہ گہرائی میں دھنس جاتا ہے کیونکہ میٹھے پانی کی کثافت کم ہوتی ہے",
        "سمندر کا نمکین پانی وزنی ہوتا ہے جو جہاز کو زیادہ اچھالتا ہے، میٹھے پانی میں جہاز نیچے بیٹھتا ہے۔"
    ),
    # 5: Highway bridge expansion joints
    (
        "Why are jagged steel expansion comb joints built into the concrete roadway decks of long highway viaducts?",
        ["To accommodate thermal expansion and contraction cycles across winter and summer without buckling", "To channel tire rainwater", "To slow down speeding traffic", "To prevent bridge icing"],
        "To accommodate thermal expansion and contraction cycles across winter and summer without buckling",
        "Temperature differentials cause massive concrete spans to expand and contract by several inches annually.",
        "ہائی وے کے لمبے کنکریٹ کے پلوں کے درمیان دندانے دار لوہے کے جوڑ (ایکسپینشن جوائنٹس) کیوں چھوڑے جاتے ہیں؟",
        ["تاکہ گرمی اور سردی میں پل کے پھیلنے اور سکڑنے سے سڑک ٹوٹنے اور ٹیڑھی ہونے سے بچ سکے", "بارش کا پانی نکالنے کے لیے", "گاڑیوں کی رفتار کم کرنے کے لیے", "پل کو ہلکا رکھنے کے لیے"],
        "تاکہ گرمی اور سردی میں پل کے پھیلنے اور سکڑنے سے سڑک ٹوٹنے اور ٹیڑھی ہونے سے بچ سکے",
        "شدید گرمی میں کنکریٹ پھیلتا ہے اور سردی میں سکڑتا ہے، یہ خلا پل کو محفوظ لچک فراہم کرتا ہے۔"
    ),
    # 6: Canyon echo distance
    (
        "If you shout 'Hello!' toward a sheer granite canyon wall and hear the distinct echo return 2.0 seconds later, roughly how far away is the cliff? (Speed of sound ~ 340 m/s)",
        ["340 meters", "680 meters", "170 meters", "500 meters"],
        "340 meters",
        "The sound traveled to the cliff and back in 2.0 seconds (1.0 second each way). Distance = 340 m/s * 1.0 s = 340 meters.",
        "اگر آپ وادی میں آواز لگائیں اور 2 سیکنڈ بعد آپ کو اپنی بازگشت سنائی دے، تو سامنے کی چٹان کتنی دور ہے؟ (آواز کی رفتار 340 میٹر فی سیکنڈ)",
        ["340 میٹر", "680 میٹر", "170 میٹر", "500 میٹر"],
        "340 میٹر",
        "آواز کو جانے اور واپس آنے میں کل 2 سیکنڈ لگے یعنی جانے میں 1 سیکنڈ لگا۔ فاصلہ = 340 ضرب 1 = 340 میٹر۔"
    ),
    # 7: Hydraulic car lift Pascal law
    (
        "How can a mechanic easily lift a 4,000-pound truck using a small hand pump on a hydraulic workshop lift?",
        ["Pascal's principle transmits fluid pressure equally, multiplying lifting force across a wider slave cylinder", "Hydraulic fluid is lighter than air", "Oil has negative gravity", "Air suction pulls the truck"],
        "Pascal's principle transmits fluid pressure equally, multiplying lifting force across a wider slave cylinder",
        "Pressure is constant throughout an enclosed liquid; force equals pressure times piston surface area (F = P * A).",
        "ورکشاپ کا مکینک ایک چھوٹے ہینڈ پمپ سے 4 ہزار پاؤنڈ کا بھاری ٹرک آسانی سے کیسے اوپر اٹھا لیتا ہے؟",
        ["پاسکل کے قانون کے تحت مائع کا دباؤ بڑے پسٹن پر فورس کو کئی گنا بڑھا دیتا ہے", "ہائیڈرولک تیل ہوا سے ہلکا ہوتا ہے", "تیل میں منفی کشش ثقل ہوتی ہے", "ہوا کا دباؤ ٹرک کھینچتا ہے"],
        "پاسکل کے قانون کے تحت مائع کا دباؤ بڑے پسٹن پر فورس کو کئی گنا بڑھا دیتا ہے",
        "بند نالی میں مائع پر لگایا گیا دباؤ چاروں طرف برابر پھیلتا ہے، بڑا پسٹن اس دباؤ سے بھاری وزن اٹھا لیتا ہے۔"
    ),
    # 8: Block and tackle pulley advantage
    (
        "Why does a heavy industrial crane hoist heavy steel girders effortlessly using a quadruple block and tackle pulley system?",
        ["Four load-bearing rope segments divide the suspended load weight by four", "Pulleys generate electricity", "The rope shrinks under load", "Friction pulls the girders"],
        "Four load-bearing rope segments divide the suspended load weight by four",
        "Each supporting line loop shares an equal fraction of the hanging gravitational mass, multiplying mechanical advantage.",
        "بھاری کرین چرخیوں (پللیوں) کے ذریعے وزنی لوہے کے گارڈرز کو اتنی آسانی سے کیسے اوپر اٹھا لیتی ہے؟",
        ["چار رسیوں پر وزن تقسیم ہو کر کھینچنے کی طاقت کو ایک چوتھائی کر دیتا ہے", "چرخیاں بجلی بناتی ہیں", "رسی کا وزن کم ہو جاتا ہے", "رگڑ وزن کھینچتی ہے"],
        "چار رسیوں پر وزن تقسیم ہو کر کھینچنے کی طاقت کو ایک چوتھائی کر دیتا ہے",
        "ہر رسی وزن کا برابر حصہ سنبھالتی ہے جس سے مکینیکل فائدہ ملتا ہے اور کم طاقت سے وزنی بوجھ اٹھ جاتا ہے۔"
    ),
    # 9: Diesel engine compression ignition
    (
        "Why do heavy commercial diesel engines lack spark plugs to ignite fuel in their combustion cylinders?",
        ["Extreme compression ratio heats cylinder air above the auto-ignition temperature of diesel fuel", "Diesel burns at room temperature", "Diesel contains gunpowder", "The battery ignites the gas"],
        "Extreme compression ratio heats cylinder air above the auto-ignition temperature of diesel fuel",
        "Adiabatic compression ratios of 20:1 raise cylinder air temperature above 550°C, instantly igniting injected fuel spray.",
        "بڑے ڈیزل ٹرکوں کے انجن میں پیٹرول انجن کی طرح اسپارک پلگ کیوں نہیں ہوتے؟",
        ["سلنڈر میں ہوا کا شدید دباؤ اتنا درجہ حرارت پیدا کرتا ہے کہ ڈیزل چھڑکتے ہی خود جل اٹھتا ہے", "ڈیزل عام درجہ حرارت پر جلتا ہے", "ڈیزل میں بارود ہوتا ہے", "بیٹری گیس جلاتی ہے"],
        "سلنڈر میں ہوا کا شدید دباؤ اتنا درجہ حرارت پیدا کرتا ہے کہ ڈیزل چھڑکتے ہی خود جل اٹھتا ہے",
        "ہوا کو شدید دبانے سے اس کی حرارت 500 ڈگری سے بڑھ جاتی ہے جس سے ڈیزل چھڑکتے ہی دھماکہ ہو جاتا ہے۔"
    ),
    # 10: Microwave dielectric heating
    (
        "How does a kitchen microwave oven heat cold soup rapidly while the ceramic bowl remains relatively cool?",
        ["2.45 GHz radio waves rotate water dipole molecules back and forth, generating dielectric friction heat", "Infrared lasers burn the soup", "Hot steam is pumped inside", "The turntable generates heat"],
        "2.45 GHz radio waves rotate water dipole molecules back and forth, generating dielectric friction heat",
        "Water molecules are electric dipoles; oscillating electromagnetic fields flip them billions of times per second, dissipating thermal heat.",
        "مائیکرو ویو اوون ٹھنڈے سالن کو منٹوں میں گرم کیسے کر دیتا ہے جبکہ شیشے کا پیالہ خود نسبتاً ٹھنڈا رہتا ہے؟",
        ["ریڈیو لہریں سالن کے پانی کے مالیکیولز کو تیزی سے گھما کر اندرونی رگڑ سے گرمی پیدا کرتی ہیں", "انفراریڈ لیزر سالن کو جلاتی ہے", "اندر گرم بھاپ چھوڑی جاتی ہے", "گھومتی پلیٹ گرمی بناتی ہے"],
        "ریڈیو لہریں سالن کے پانی کے مالیکیولز کو تیزی سے گھما کر اندرونی رگڑ سے گرمی پیدا کرتی ہیں",
        "پانی کے قطبی مالیکیولز مائیکرو ویو لہروں کے ساتھ سیکنڈ میں اربوں بار گھومتے ہیں جس سے رگڑ کی حرارت بنتی ہے۔"
    ),
    # 11: Induction stove magnetic eddy currents
    (
        "Why can you boil water on an induction cooktop in an iron skillet while resting your bare hand safely on the glass next to it?",
        ["High-frequency magnetic fields induce electrical eddy currents exclusively inside ferromagnetic iron cookware", "The glass is frozen", "Induction works by cold light", "Iron absorbs cosmic heat"],
        "High-frequency magnetic fields induce electrical eddy currents exclusively inside ferromagnetic iron cookware",
        "Electromagnetic induction induces circular eddy currents in conductive ferromagnetic metals; glass remains unaffected.",
        "انڈکشن چولہے پر لوہے کے پین میں پانی ابلتا ہے مگر پاس کے شیشے پر ہاتھ رکھنے سے ہاتھ کیوں نہیں جلتا؟",
        ["مقناطیسی لہریں صرف لوہے کے برتن کے اندر بجلی کی لہریں (ایڈی کرنٹ) پیدا کر کے اسے گرم کرتی ہیں", "شیشہ جمانے والا ہوتا ہے", "چولہا ٹھنڈی روشنی سے چلتا ہے", "لوہا قدرتی گرم ہوتا ہے"],
        "مقناطیسی لہریں صرف لوہے کے برتن کے اندر بجلی کی لہریں (ایڈی کرنٹ) پیدا کر کے اسے گرم کرتی ہیں",
        "مقناطیسی فیلڈ صرف لوہے کی دھات میں حرارت پیدا کرتا ہے، نان میٹالک شیشہ خود گرم نہیں ہوتا۔"
    ),
    # 12: Pressure cooker high boiling point
    (
        "Why does tough mutton meat cook twice as fast inside a sealed kitchen pressure cooker compared to an open pot?",
        ["Trapped steam raises interior pressure, elevating water's boiling point to 120°C", "The cooker uses nuclear heat", "Tough meat dissolves in steam", "The metal reflects sound waves"],
        "Trapped steam raises interior pressure, elevating water's boiling point to 120°C",
        "Water's liquid-vapor phase boundary shifts upward with pressure; cooking at 120°C accelerates collagen breakdown exponentially.",
        "پریشر کوکر کے اندر سخت گوشت عام کھلی دیگچی کے مقابلے میں آدھے وقت میں کیوں گل جاتا ہے؟",
        ["بند بھاپ کا دباؤ پانی کے ابلنے کے درجہ حرارت کو 100 سے بڑھا کر 120 ڈگری سینٹی گریڈ کر دیتا ہے", "کوکر ایٹمی حرارت دیتا ہے", "گوشت بھاپ میں پگھلتا ہے", "دھات آواز کی لہریں موڑتی ہے"],
        "بند بھاپ کا دباؤ پانی کے ابلنے کے درجہ حرارت کو 100 سے بڑھا کر 120 ڈگری سینٹی گریڈ کر دیتا ہے",
        "پریشر کوکر میں زیادہ دباؤ کی وجہ سے پانی زیادہ تیز گرمی پر ابلتا ہے جس سے گوشت جلدی گل جاتا ہے۔"
    ),
    # 13: Thermos flask vacuum barrier
    (
        "How does a double-walled glass thermos flask keep hot coffee steaming hot for over twenty-four hours?",
        ["A silvered vacuum barrier eliminates heat transfer via conduction, convection, and radiation", "Internal batteries heat the flask", "The plastic lid boils water", "The flask creates friction"],
        "A silvered vacuum barrier eliminates heat transfer via conduction, convection, and radiation",
        "Vacuums eliminate conductive and convective particle collisions, while reflective mirrored coatings bounce radiant infrared photons back.",
        "تھرماس کے اندر گرم چائے چوبیس گھنٹے تک گرم اور تازہ کیسے رہتی ہے؟",
        ["دوہری دیواروں کے درمیان کا خلاء (ویکیوم) اور چاندی کا پالش شدہ شیشہ گرمی کو باہر نہیں جانے دیتا", "اندر چھوٹی بیٹریاں لگی ہوتی ہیں", "ڈھکن خود گرمی بناتا ہے", "شیشے میں رگڑ ہوتی ہے"],
        "دوہری دیواروں کے درمیان کا خلاء (ویکیوم) اور چاندی کا پالش شدہ شیشہ گرمی کو باہر نہیں جانے دیتا",
        "خلاء کی وجہ سے حرارت کا ایصال اور کنویکشن رک جاتا ہے، اور آئینے کی تہہ ریڈی ایشن کو واپس منعکس کرتی ہے۔"
    ),
    # 14: Bimetallic thermostat strip
    (
        "How does a traditional mechanical room thermostat automatically turn off a furnace when the room reaches 72°F?",
        ["A bimetallic strip made of two bonded metals bends as unequal thermal expansion flexes an electrical contact open", "Mercury expands out of tube", "A digital chip measures room air", "The furnace melts the switch"],
        "A bimetallic strip made of two bonded metals bends as unequal thermal expansion flexes an electrical contact open",
        "Brass expands faster than steel with rising temperature, physically curving the bonded laminate strip to break electrical contact.",
        "کمرے کا روایتی مکینیکل تھرموسٹیٹ درجہ حرارت پورا ہوتے ہی ہیٹر کو خود بخود کیسے بند کر دیتا ہے؟",
        ["دو مختلف دھاتوں کی جڑی ہوئی پتی گرمی سے غیر مساوی پھیل کر مڑ جاتی ہے اور برقی سوئچ کھول دیتی ہے", "پارہ باہر نکل جاتا ہے", "کمپیوٹر ہوا کو دیکھتا ہے", "ہیٹر سوئچ کو پگھلا دیتا ہے"],
        "دو مختلف دھاتوں کی جڑی ہوئی پتی گرمی سے غیر مساوی پھیل کر مڑ جاتی ہے اور برقی سوئچ کھول دیتی ہے",
        "ایک دھات گرمی سے زیادہ پھیلتی ہے اور دوسری کم، اس کھنچاؤ سے پتی کمان کی طرح مڑ کر کرنٹ کاٹ دیتی ہے۔"
    ),
    # 15: Automobile differential gear
    (
        "Why does an automobile need a mechanical differential gear set installed on its driven drive axle?",
        ["To allow the outside drive wheel to spin faster than the inside wheel during turns without slipping tires", "To increase top forward speed", "To brake wheels in reverse", "To balance vehicle weight"],
        "To allow the outside drive wheel to spin faster than the inside wheel during turns without slipping tires",
        "When turning a corner, the outer wheel travels along a larger radius arc, requiring more rotations than the inner wheel.",
        "گاڑی کے پچھلے ایکسل پر ڈیفرینشل گیئر (کراؤن وہیل) کیوں لگایا جاتا ہے؟",
        ["تاکہ موڑ کاٹتے وقت باہر کا پہیہ اندر کے پہیے سے زیادہ تیزی سے گھوم سکے اور ٹائر نہ گھسٹیں", "گاڑی کی اسپیڈ بڑھانے کے لیے", "الٹے گیئر میں بریک لگانے کے لیے", "وزن برابر رکھنے کے لیے"],
        "تاکہ موڑ کاٹتے وقت باہر کا پہیہ اندر کے پہیے سے زیادہ تیزی سے گھوم سکے اور ٹائر نہ گھسٹیں",
        "موڑ پر بیرونی پہیے کو لمبا دائرہ طے کرنا ہوتا ہے، ڈیفرینشل دونوں پہیوں کو مختلف رفتار سے گھومنے دیتا ہے۔"
    ),
    # 16: Convex magnifying glass solar fire
    (
        "How can a simple convex magnifying glass ignite dry wood tinder beneath bright sunlight?",
        ["Refracting parallel solar light rays through the curved lens, concentrating broad energy into a tiny hot focal point", "The glass lens heats up first", "Glass reflects light backward", "The wood absorbs glass chemicals"],
        "Refracting parallel solar light rays through the curved lens, concentrating broad energy into a tiny hot focal point",
        "Biconvex optics bend parallel solar electromagnetic radiation into a pinpoint focal spot, elevating surface temperature above ignition.",
        "عام محدب عدسے (میگنی فائنگ گلاس) سے سورج کی دھوپ میں خشک تنکوں کو آگ کیسے لگائی جا سکتی ہے؟",
        ["شیشہ سورج کی متوازی شعاعوں کو سمیٹ کر ایک باریک فوکل پوائنٹ پر زبردست گرمی میں مرکوز کر دیتا ہے", "شیشہ خود گرم ہو کر پگھلتا ہے", "شیشہ روشنی کو لوٹاتا ہے", "لکڑی شیشے سے کیمیکل لیتی ہے"],
        "شیشہ سورج کی متوازی شعاعوں کو سمیٹ کر ایک باریک فوکل پوائنٹ پر زبردست گرمی میں مرکوز کر دیتا ہے",
        "عدسہ دور دور سے آنے والی روشنی کی تپش کو ایک ہی نقطے پر اکٹھا کر دیتا ہے جہاں درجہ حرارت جلنے کی حد تک پہنچ جاتا ہے۔"
    ),
    # 17: Glass prism spectral dispersion
    (
        "Why does a clear triangular glass prism split a beam of white sunlight into a spectrum of rainbow colors?",
        ["Different wavelengths of light bend by different angles due to chromatic dispersion (blue bends more than red)", "The prism contains rainbow dye", "White light heats the glass", "Prisms reflect light in circles"],
        "Different wavelengths of light bend by different angles due to chromatic dispersion (blue bends more than red)",
        "The refractive index of glass varies inversely with wavelength; short blue waves decelerate and refract more sharply than red waves.",
        "تکونی شیشے کا پرزم سورج کی سفید روشنی کو سات رنگوں کی پٹی میں کیوں بانٹ دیتا ہے؟",
        ["مختلف رنگوں کی لہریں شیشے میں داخل ہونے پر مختلف زاویوں سے مڑتی ہیں (نیلا رنگ زیادہ مڑتا ہے)", "پرزم کے اندر رنگ بھرا ہوتا ہے", "سفید روشنی شیشے کو جلاتی ہے", "پرزم روشنی گھماتا ہے"],
        "مختلف رنگوں کی لہریں شیشے میں داخل ہونے پر مختلف زاویوں سے مڑتی ہیں (نیلا رنگ زیادہ مڑتا ہے)",
        "ہر رنگ کی ویو لینتھ الگ ہوتی ہے، شیشے میں داخل ہوتے ہی نیلا رنگ زیادہ جھکتا ہے اور سرخ کم، جس سے رنگ بکھر جاتے ہیں۔"
    ),
    # 18: Fiber optic total internal reflection
    (
        "How do ultra-fast internet laser light pulses travel around sharp bends inside transparent glass fiber cables without leaking out?",
        ["Light strikes the core-cladding boundary at an angle greater than the critical angle, undergoing total internal reflection", "Fibers are wrapped in aluminum foil", "Glass slows light to zero", "Laser light is magnetic"],
        "Light strikes the core-cladding boundary at an angle greater than the critical angle, undergoing total internal reflection",
        "When entering a medium of lower refractive index beyond the critical angle, 100% of the electromagnetic wavefront reflects inward.",
        "انٹرنیٹ کی فائبر آپٹک تار میں روشنی کی تیز رفتار لہریں شیشے کے اندر مڑتے ہوئے باہر کیوں نہیں نکلتیں؟",
        ["روشنی شیشے کی اندرونی دیوار سے کل داخلی انعکاس (ٹوٹل انٹرنل ریفلیکشن) کے تحت سو فیصد پلٹتی رہتی ہے", "تار پر چاندی کا ورق لپٹا ہوتا ہے", "شیشہ روشنی کو روک لیتا ہے", "لیزر مقناطیسی ہوتی ہے"],
        "روشنی شیشے کی اندرونی دیوار سے کل داخلی انعکاس (ٹوٹل انٹرنل ریفلیکشن) کے تحت سو فیصد پلٹتی رہتی ہے",
        "کریٹیکل اینگل سے بڑے زاویے پر ٹکرانے سے شیشے سے روشنی باہر جھانکنے کے بجائے اندر ہی آئینے کی طرح لوٹتی ہے۔"
    ),
    # 19: Airplane wing airfoil lift
    (
        "How does a Boeing 737 passenger airliner weighing 150,000 pounds achieve aerodynamic lift into the sky?",
        ["Curved airfoil camber accelerates airflow over the top wing, creating low static pressure combined with downward air deflection", "Jet engines blow air upward", "The fuselage is filled with helium", "The wings flap rapidly"],
        "Curved airfoil camber accelerates airflow over the top wing, creating low static pressure combined with downward air deflection",
        "Bernoulli's principle and Newton's third law operate concurrently: upper low pressure lifts the wing while deflected downwash provides momentum thrust.",
        "ہزاروں کلو وزنی بوئنگ ہوائی جہاز فضا میں پرواز کی بلندی پر کیسے اڑتا رہتا ہے؟",
        ["پروں کی خاص خمیدہ بناوٹ اوپر کی ہوا تیز کر کے کم دباؤ بناتی ہے اور نیچے کی ہوا اسے اوپر اچھالتی ہے", "انجن نیچے ہوا پھینکتے ہیں", "جہاز میں ہیلیئم گیس بھری ہوتی ہے", "پر تیزی سے پھڑپھڑاتے ہیں"],
        "پروں کی خاص خمیدہ بناوٹ اوپر کی ہوا تیز کر کے کم دباؤ بناتی ہے اور نیچے کی ہوا اسے اوپر اچھالتی ہے",
        "پر کے اوپر کم ہوا کا دباؤ بنتا ہے اور نیچے کی ہوا کا نیوٹن کا رد عمل مل کر جہاز کے وزن کو ہوا میں اٹھائے رکھتا ہے۔"
    ),
    # 20: Helicopter tail rotor anti-torque
    (
        "Why is a small vertical tail rotor mounted on the tail boom of a single-rotor helicopter essential for flight?",
        ["It provides lateral aerodynamic thrust to counteract the reactionary spin torque of the main overhead rotor", "It steers the helicopter up and down", "It cools the tail engine", "It provides forward thrust"],
        "It provides lateral aerodynamic thrust to counteract the reactionary spin torque of the main overhead rotor",
        "Newton's third law dictates that spinning the main blades clockwise produces counterclockwise fuselage spin unless opposed by tail thrust.",
        "ہیلی کاپٹر کی لمبی دم پر لگا چھوٹا پنکھا پرواز کے لیے کیوں انتہائی لازمی ہوتا ہے؟",
        ["وہ بڑے پنکھے کے گھومنے کے رد عمل میں ہیلی کاپٹر کے جسم کو گول گول گھومنے سے روکتا ہے", "وہ ہیلی کاپٹر کو اوپر نیچے کرتا ہے", "وہ دم کے انجن کو ٹھنڈا کرتا ہے", "وہ آگے کی رفتار دیتا ہے"],
        "وہ بڑے پنکھے کے گھومنے کے رد عمل میں ہیلی کاپٹر کے جسم کو گول گول گھومنے سے روکتا ہے",
        "نیوٹن کے تیسرے قانون کے تحت بڑا پنکھا جس رخ گھومے گا باڈی الٹے رخ گھومے گی، دم کا پنکھا اسے سیدھا رکھتا ہے۔"
    ),
    # 21: Parachute terminal velocity
    (
        "Why does a skydiver reach a safe terminal landing velocity of 12 mph after deploying a fabric parachute canopy?",
        ["Upward aerodynamic drag force increases until it precisely equals downward gravitational force, stopping acceleration", "Gravity turns off under fabric", "Air becomes solid beneath canopy", "The canopy pulls upward into space"],
        "Upward aerodynamic drag force increases until it precisely equals downward gravitational force, stopping acceleration",
        "Terminal velocity occurs when net force is zero; broad parachute surface area maximizes the aerodynamic drag coefficient (Cd).",
        "پیراشوٹ کھولتے ہی اسکائی ڈائیور کی گرنے کی خطرناک رفتار کم ہو کر صرف 15 کلومیٹر فی گھنٹہ پر کیسے رک جاتی ہے؟",
        ["پیراشوٹ کی ہوا کی رگڑ اوپر کی طرف بڑھ کر کشش ثقل کے بالکل برابر ہو جاتی ہے جس سے رفتار یکساں رہتی ہے", "کپڑے کے نیچے کشش ثقل ختم ہو جاتی ہے", "ہوا ٹھوس بن جاتی ہے", "پیراشوٹ اوپر کھینچتا ہے"],
        "پیراشوٹ کی ہوا کی رگڑ اوپر کی طرف بڑھ کر کشش ثقل کے بالکل برابر ہو جاتی ہے جس سے رفتار یکساں رہتی ہے",
        "جب ہوا کی اوپر دھکیلنے والی طاقت گرنے والے کے وزن کے برابر ہو جائے تو رفتار مزید نہیں بڑھتی اور محفوظ ہو جاتی ہے۔"
    ),
    # 22: Submarine ballast tanks
    (
        "How does a massive naval nuclear submarine dive deep beneath the ocean surface and subsequently surface at will?",
        ["Flooding ballast tanks with seawater to increase overall density to dive, and blowing compressed air to surface", "Using giant underwater propellers to pull downward", "Changing hull shape mechanically", "Heating seawater around hull"],
        "Flooding ballast tanks with seawater to increase overall density to dive, and blowing compressed air to surface",
        "Archimedes' buoyancy dictates: venting ballast air fills tanks with sea water (negative buoyancy); blowing high-pressure air restores positive buoyancy.",
        "بھاری بحری آبدوز سمندر کی گہرائی میں غوطہ کیسے لگاتی ہے اور پھر اپنی مرضی سے سطح پر کیسے واپس آتی ہے؟",
        ["ٹینکوں میں سمندری پانی بھر کر وزنی ہو کر ڈوبتی ہے، اور کمپریسڈ ہوا بھر کر پانی نکال کر واپس ابھرتی ہے", "پروں سے نیچے کھینچ کر", "آبدوز کی باڈی سکڑ کر", "پانی کو گرم کر کے"],
        "ٹینکوں میں سمندری پانی بھر کر وزنی ہو کر ڈوبتی ہے، اور کمپریسڈ ہوا بھر کر پانی نکال کر واپس ابھرتی ہے",
        "آرکیمیڈیز کے اصول پر ٹینکوں میں پانی بھرنے سے آبدوز سمندر سے وزنی ہو جاتی ہے، ہوا بھرنے سے ہلکی ہو کر ابھرتی ہے۔"
    ),
    # 23: Hot air balloon buoyancy
    (
        "Why does a giant hot air balloon rise gracefully into the sky when a propane burner fires flame into the envelope?",
        ["Heating air inside expands its volume, decreasing its density below the surrounding cool ambient atmosphere", "Flames produce helium gas", "Propane has negative weight", "Fire pushes against the basket"],
        "Heating air inside expands its volume, decreasing its density below the surrounding cool ambient atmosphere",
        "Charles's law dictates that air expands with rising absolute temperature; lighter interior air generates net upward buoyant lift.",
        "پروپین گیس کا شعلہ جلانے پر گرم ہوا کا بڑا غبارہ آسمان کی طرف خود بخود کیوں اڑنے لگتا ہے؟",
        ["اندر کی ہوا گرم ہو کر پھیلتی ہے اور اس کا وزن باہر کی ٹھنڈی ہوا سے ہلکا ہو جاتا ہے", "شعلہ ہیلیئم گیس بناتا ہے", "پروپین میں منفی وزن ہوتا ہے", "آگ ٹوکری کو دھکیلتی ہے"],
        "اندر کی ہوا گرم ہو کر پھیلتی ہے اور اس کا وزن باہر کی ٹھنڈی ہوا سے ہلکا ہو جاتا ہے",
        "گرم ہوا ہلکی ہو کر اوپر اٹھتی ہے، جب غبارے کی اندرونی ہوا باہر کی فضا سے ہلکی ہو جائے تو غبارہ بلند ہوتا ہے۔"
    ),
    # 24: Hovercraft air cushion skirt
    (
        "How can a 50-ton amphibious hovercraft skim smoothly over swamp mud, sand beaches, and open water waves?",
        ["Lift fans force air beneath the hull, trapped by a flexible rubber skirt into a pressurized low-friction air cushion", "Magnetic repulsion from water", "Hydrophobic paint coating", "Water jets boiling beneath"],
        "Lift fans force air beneath the hull, trapped by a flexible rubber skirt into a pressurized low-friction air cushion",
        "Trapping a high-volume low-pressure air pocket eliminates physical contact friction with underlying terrain surfaces.",
        "50 ٹن وزنی ہوور کرافٹ دلدل، ریت اور سمندر کے پانی پر بغیر رکے ایک جیسی رفتار سے کیسے تیرتا ہے؟",
        ["طاقتور پنکھے نیچے ہوا کا پریشر بنا کر لچکدار ربڑ کے اسکرٹ میں قید کر لیتے ہیں جس پر کشتی تیرتی ہے", "پانی سے مقناطیسی اچھال کی وجہ سے", "واٹر پروف رنگ کی وجہ سے", "ابلتے ہوئے پانی کے جیٹس سے"],
        "طاقتور پنکھے نیچے ہوا کا پریشر بنا کر لچکدار ربڑ کے اسکرٹ میں قید کر لیتے ہیں جس پر کشتی تیرتی ہے",
        "ہوا کا گدا کشتی کو زمین اور پانی سے چند انچ اوپر اٹھا دیتا ہے جس سے رگڑ ختم ہو جاتی ہے اور وہ پھسلتی ہے۔"
    ),
    # 25: Bullet rifling gyroscopic spin
    (
        "Why are spiral helical grooves called rifling machined into the interior steel barrel bore of hunting rifles?",
        ["They impart axial gyroscopic spin to the bullet, stabilizing its aerodynamic trajectory against tumbling", "To clean the barrel during firing", "To make the bullet travel slower", "To cool the gun barrel"],
        "They impart axial gyroscopic spin to the bullet, stabilizing its aerodynamic trajectory against tumbling",
        "Angular momentum conservation keeps the spinning bullet's aerodynamic center of drag aligned with its trajectory path.",
        "رائفل کی نالی کے اندرونی حصے میں چکر دار اسکرو جیسی لکیریں (رائفلنگ) کیوں بنائی جاتی ہیں؟",
        ["وہ گولی کو اپنی جگہ تیزی سے گھماتی ہیں جس سے گولی ہوا میں لڑکھڑائے بغیر سیدھی نشانے پر لگتی ہے", "نالی کی صفائی کے لیے", "گولی کی رفتار کم کرنے کے لیے", "نالی کو ٹھنڈا رکھنے کے لیے"],
        "وہ گولی کو اپنی جگہ تیزی سے گھماتی ہیں جس سے گولی ہوا میں لڑکھڑائے بغیر سیدھی نشانے پر لگتی ہے",
        "گھومتی ہوئی گولی میں جائرواسکوپک استحکام پیدا ہوتا ہے جو ہوا کے جھونکوں میں بھی اسے سیدھا رکھتا ہے۔"
    ),
    # 26: Municipal water tower gravitational head
    (
        "Why do municipal city water utilities pump potable water into elevated steel storage tanks perched on tall towers?",
        ["Gravitational potential energy creates reliable hydrostatic water pressure in home plumbing pipes without continuous pumps", "To keep city water near clouds", "To cool water in wind", "To prevent earth tremors"],
        "Gravitational potential energy creates reliable hydrostatic water pressure in home plumbing pipes without continuous pumps",
        "Hydrostatic pressure equals liquid density * gravity * height (P = rho * g * h); elevating water 100 feet generates ~43 psi head pressure.",
        "شہروں میں پانی سپلائی کرنے کے لیے زمین پر ٹینک بنانے کے بجائے اونچے ٹاور پر بڑا واٹر ٹینک کیوں لگایا جاتا ہے؟",
        ["پانی کی اونچائی قدرتی کشش ثقل سے گھروں کے نلکوں میں بنا موٹر کے مستقل پریشر پیدا کرتی ہے", "پانی کو بادلوں کے قریب رکھنے کے لیے", "ہوا سے ٹھنڈا کرنے کے لیے", "زلزلوں سے بچانے کے لیے"],
        "پانی کی اونچائی قدرتی کشش ثقل سے گھروں کے نلکوں میں بنا موٹر کے مستقل پریشر پیدا کرتی ہے",
        "کشش ثقل کی بلندی سے پائپوں میں زبردست قدرتی دباؤ بنتا ہے جس سے پورے محلے میں پانی تیزی سے پہنچتا ہے۔"
    ),
    # 27: Pendulum clock period mass independence
    (
        "If you replace the 1-pound lead bob of a grandfather clock pendulum with a 5-pound gold bob of the same length, what happens to the clock's speed?",
        ["It ticks at the exact same rate; pendulum period depends solely on length and gravity, not bob mass", "It runs five times faster", "It runs five times slower", "It stops instantly"],
        "It ticks at the exact same rate; pendulum period depends solely on length and gravity, not bob mass",
        "The simple pendulum harmonic period formula T = 2*pi*sqrt(L/g) contains zero mass terms.",
        "اگر کلاک کے لٹکتے ہوئے پنڈولم کا 1 کلو کا باٹ ہٹا کر اسی لمبائی کا 5 کلو کا بھاری باٹ لگا دیں تو گھڑی کی رفتار پر کیا اثر پڑے گا؟",
        ["رفتار بالکل وہی رہے گی، پنڈولم کا وقت صرف لمبائی اور کشش ثقل پر منحصر ہوتا ہے وزن پر نہیں", "وہ پانچ گنا تیز ہو جائے گی", "وہ پانچ گنا سست ہو جائے گی", "وہ فورا بند ہو جائے گی"],
        "رفتار بالکل وہی رہے گی، پنڈولم کا وقت صرف لمبائی اور کشش ثقل پر منحصر ہوتا ہے وزن پر نہیں",
        "گیلیلیو کے پنڈولم کے اصول کے مطابق لٹکنے والے وزن کی کمی بیشی سے جھولنے کا وقت بالکل تبدیل نہیں ہوتا۔"
    ),
    # 28: Flywheel rotational kinetic energy
    (
        "Why does a heavy mechanical tractor engine feature a massive cast iron flywheel bolted to its rotating crankshaft?",
        ["Its high rotational moment of inertia smooths out pulsed power surges between piston firing strokes", "To generate vehicle electricity", "To cool down the radiator", "To act as an emergency anchor"],
        "Its high rotational moment of inertia smooths out pulsed power surges between piston firing strokes",
        "Rotational kinetic energy E = 0.5 * I * omega^2 stores energy during power expansion strokes and delivers it during compression strokes.",
        "ٹریکٹر کے انجن کے ساتھ ایک بھاری گول لوہے کا پہیہ (فلائی وہیل) کیوں لگایا جاتا ہے؟",
        ["اس کا بھاری انرشیا انجن کے پسٹنز کے جھٹکوں کو جذب کر کے رفتار کو بالکل ہموار اور یکساں رکھتا ہے", "گاڑی کی بجلی بنانے کے لیے", "ریڈی ایٹر کو ٹھنڈا کرنے کے لیے", "ایمرجنسی بریک لگانے کے لیے"],
        "اس کا بھاری انرشیا انجن کے پسٹنز کے جھٹکوں کو جذب کر کے رفتار کو بالکل ہموار اور یکساں رکھتا ہے",
        "فلائی وہیل پسٹن کے فائر ہونے پر طاقت جمع کرتا ہے اور اگلے راؤنڈ میں انجن کو بغیر رکے گھماتا رہتا ہے۔"
    ),
    # 29: Anti-lock braking system ABS cadence
    (
        "Why does an automobile's computer-controlled ABS system pump brakes up to fifteen times per second rather than locking tires solid on wet asphalt?",
        ["Static friction of a rolling tire is significantly higher than kinetic sliding friction of a skidding tire", "Pumping cools the brake rotors", "To warn other drivers with pulsing sounds", "To save brake fluid"],
        "Static friction of a rolling tire is significantly higher than kinetic sliding friction of a skidding tire",
        "The coefficient of static road friction exceeds dynamic sliding friction, preventing loss of vehicle steering directional control.",
        "گیلی سڑک پر گاڑی کا اے بی ایس (ABS) سسٹم بریک کو جام کرنے کے بجائے سیکنڈ میں 15 بار تیزی سے کیوں چھوڑتا اور لگاتا ہے؟",
        ["گھومتے ٹائر کی جامد رگڑ پھسلتے ہوئے گھسٹتے ٹائر کی متحرک رگڑ سے کہیں زیادہ مضبوط ہوتی ہے", "بریک کے روٹرز ٹھنڈے رکھنے کے لیے", "دوسروں کو آواز سے ڈرانے کے لیے", "بریک کا تیل بچانے کے لیے"],
        "گھومتے ٹائر کی جامد رگڑ پھسلتے ہوئے گھسٹتے ٹائر کی متحرک رگڑ سے کہیں زیادہ مضبوط ہوتی ہے",
        "پھسلنے والے ٹائر کی گرپ ختم ہو جاتی ہے، اے بی ایس ٹائر کو گھومتے رکھ کر گاڑی کا کنٹرول ڈرائیور کے ہاتھ میں رکھتا ہے۔"
    ),
    # 30: Crumple zones crash impact absorption
    (
        "Why do modern automotive structural engineers design vehicle front ends to accordion-crush upon collision rather than building rigid unbreakable steel frames?",
        ["Elongating crash impact deceleration time drastically lowers peak deceleration g-forces experienced by passengers", "To make cars cheaper to assemble", "To protect the road pavement", "To recycle scrap metal easily"],
        "Elongating crash impact deceleration time drastically lowers peak deceleration g-forces experienced by passengers",
        "Impulse momentum theorem (F = delta p / delta t) dictates that increasing impact duration delta t minimizes peak deceleration force F.",
        "جدید گاڑیوں کے آگے کا حصہ حادثے کے وقت دب کر پچکنے والا (کرمپل زون) کیوں بنایا جاتا ہے بجائے اس کے کہ اسے سخت بنایا جائے؟",
        ["ٹکرانے کا وقت بڑھا کر جھٹکے کے زور کو کم کیا جاتا ہے تاکہ اندر بیٹھے مسافروں پر کم سے کم جان لیوا دباؤ پڑے", "گاڑی سستی بنانے کے لیے", "سڑک کو ٹوٹنے سے بچانے کے لیے", "لوہا آسانی سے ری سائیکل کرنے کے لیے"],
        "ٹکرانے کا وقت بڑھا کر جھٹکے کے زور کو کم کیا جاتا ہے تاکہ اندر بیٹھے مسافروں پر کم سے کم جان لیوا دباؤ پڑے",
        "گاڑی کا آگے کا حصہ صدمہ خود جذب کر لیتا ہے، اگر وہ لوہے کی دیوار بنتا تو اندر بیٹھے مسافر جھٹکے سے مر جاتے۔"
    )
]

print(f"Normal Part 1 loaded {len(ITEMS)} items.")
