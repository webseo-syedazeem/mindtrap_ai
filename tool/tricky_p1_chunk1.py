# -*- coding: utf-8 -*-
"""
Tricky Part 1 Chunk 1 (60 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "A solid steel washer with a circular hole in its center is uniformly heated in an industrial oven. What happens to the diameter of the central hole?",
        ["It expands and becomes larger", "It shrinks and becomes smaller", "It remains exactly identical", "It turns into an oval shape"],
        "It expands and becomes larger",
        "Thermal expansion acts like a photographic enlargement; every linear dimension expands outward, increasing the hole diameter.",
        "لوہے کا ایک گول واشر جس کے عین درمیان میں گول سوراخ ہے، اسے بھٹی میں یکساں گرم کیا جاتا ہے۔ اندرونی سوراخ کے سائز پر کیا اثر پڑے گا؟",
        ["سوراخ پھیل کر بڑا ہو جائے گا", "سوراخ سکڑ کر چھوٹا ہو جائے گا", "سوراخ کا سائز بالکل وہی رہے گا", "سوراخ بیضوی بن جائے گا"],
        "سوراخ پھیل کر بڑا ہو جائے گا",
        "دھات کی تھرمل توسیع (Thermal expansion) ہر سمت میں باہر کی طرف پھیلتی ہے جیسے کسی تصویر کو بڑا کیا جائے، اس لیے سوراخ چھوٹا نہیں بلکہ بڑا ہو جاتا ہے۔"
    ),
    (
        "A large rock rests inside a rowboat floating in a small swimming pool. If a person tosses the rock overboard and it sinks to the bottom, what happens to the water level of the pool?",
        ["The pool water level falls slightly", "The pool water level rises slightly", "The water level remains exactly identical", "The pool overflows immediately"],
        "The pool water level falls slightly",
        "In the boat, the rock displaced its mass in water. Sunk at the bottom, it displaces only its volume, which is smaller because rock is denser than water.",
        "ایک چھوٹی کشتی سوئمنگ پول میں تیر رہی ہے جس میں ایک وزنی پتھر رکھا ہے۔ اگر پتھر کو کشتی سے نکال کر پول کے پانی میں پھینک دیا جائے اور وہ ڈوب جائے، تو پول کے پانی کی سطح پر کیا اثر پڑے گا؟",
        ["پول میں پانی کی سطح تھوڑی سی نیچے گر جائے گی", "پانی کی سطح اوپر اٹھ جائے گی", "پانی کی سطح بالکل وہی رہے گی", "پول کا پانی باہر چھلک جائے گا"],
        "پول میں پانی کی سطح تھوڑی سی نیچے گر جائے گی",
        "کشتی میں رہتے ہوئے پتھر اپنے وزن کے برابر پانی ہٹا رہا تھا۔ جب وہ ڈوب گیا تو اس نے صرف اپنے حجم کے برابر پانی ہٹایا جو کہ پتھر کے بھاری ہونے کی وجہ سے وزن سے کم ہوتا ہے، اس لیے سطح گر جاتی ہے۔"
    ),
    (
        "A helium-filled balloon is floating inside a sealed car with closed windows. When the driver presses the accelerator and the car surges forward, which way does the balloon move?",
        ["It tilts forward toward the windshield", "It jerks backward toward the rear seat", "It stays completely motionless", "It sinks straight to the floor"],
        "It tilts forward toward the windshield",
        "Denser cabin air rushes backward due to inertia, creating a forward pressure gradient that buoys the lighter helium balloon forward.",
        "ہیلیئم گیس سے بھرا غبارہ بند شیشوں والی کار میں تیر رہا ہے۔ جب ڈرائیور ریس دبا کر کار کو تیزی سے آگے بھگاتا ہے تو غبارہ کس طرف جھکے گا؟",
        ["وہ سامنے ونڈ اسکرین کی طرف آگے جھکے گا", "وہ پچھلی سیٹ کی طرف پیچھے جھکے گا", "وہ بالکل ساکن رہے گا", "وہ نیچے فرش پر گر جائے گا"],
        "وہ سامنے ونڈ اسکرین کی طرف آگے جھکے گا",
        "انرشیا کی وجہ سے کار کی بھاری ہوا پیچھے کی طرف جاتی ہے جس سے پچھلے حصے میں ہوا کا دباؤ بڑھ جاتا ہے۔ یہ زیادہ دباؤ ہلکے ہیلیئم کو آگے کی طرف اچھال دیتا ہے۔"
    ),
    (
        "Two raw eggs are on a counter: one is hard-boiled, one is raw. You spin both, tap each with your finger for half a second to stop them, and immediately let go. Which egg starts spinning again?",
        ["The raw egg resumes spinning", "The hard-boiled egg resumes spinning", "Both resume spinning equally", "Neither egg spins again"],
        "The raw egg resumes spinning",
        "Stopping the shell does not stop the fluid yolk inside; upon release, the rotational momentum of the swirling liquid resumes spinning the shell.",
        "میز پر دو انڈے ہیں: ایک کچا اور ایک ابلا ہوا۔ آپ دونوں کو گھماتے ہیں اور پھر انگلی رکھ کر ایک لمحے کے لیے روک کر چھوڑ دیتے ہیں۔ کون سا انڈا دوبارہ خود بخود گھومنے لگے گا؟",
        ["کچا انڈا دوبارہ گھومنے لگے گا", "ابلا ہوا انڈا دوبارہ گھومنے لگے گا", "دونوں انڈے برابر گھومیں گے", "کوئی بھی انڈا دوبارہ نہیں گھومے گا"],
        "کچا انڈا دوبارہ گھومنے لگے گا",
        "انگلی لگانے سے صرف کچے انڈے کا چھلکا رکا تھا، اندر کی مائع زردی اپنے انرشیا سے اندر گھومتی رہی۔ انگلی ہٹاتے ہی اندر کے مائع نے چھلکے کو دوبارہ گھما دیا۔"
    ),
    (
        "In the Monty Hall dilemma, you pick Door 1 out of 3 doors. The host opens Door 3, revealing a goat. Should you switch to Door 2 to maximize your chance of winning the car?",
        ["Yes, switching doubles your winning odds to 2/3", "No, your probability remains exactly 1/2 either way", "It makes zero mathematical difference", "Only if you originally preferred Door 2"],
        "Yes, switching doubles your winning odds to 2/3",
        "Your initial pick had a 1/3 probability of being correct. The remaining 2/3 probability concentrates entirely on Door 2 once the host reveals a goat.",
        "مونٹی ہال کے مشہور کھیل میں تین دروازے ہیں، ایک کے پیچھے گاڑی اور دو کے پیچھے بکریاں ہیں۔ آپ نے دروازہ 1 چنا۔ میزبان نے دروازہ 3 کھولا جہاں بکری نکلی۔ کیا آپ کو دروازہ 2 پر سوئچ کرنا چاہیے؟",
        ["ہاں، سوئچ کرنے سے جیتنے کا امکان دگنا (2/3) ہو جاتا ہے", "نہیں، امکان دونوں صورتوں میں 50/50 ہی رہتا ہے", "ریاضیاتی طور پر کوئی فرق نہیں پڑتا", "صرف اگر آپ کا دل چاہے"],
        "ہاں، سوئچ کرنے سے جیتنے کا امکان دگنا (2/3) ہو جاتا ہے",
        "پہلی بار صحیح دروازہ چننے کا امکان صرف 1/3 تھا۔ چونکہ میزبان جان بوجھ کر بکری والا دروازہ کھولتا ہے، اس لیے باقی بچ جانے والے دروازے میں گاڑی ہونے کا امکان 2/3 (66.7%) ہو جاتا ہے۔"
    ),
    (
        "In a remote village, the barber shaves all men, and only those men, who do not shave themselves. Who shaves the barber?",
        ["It is a logically impossible paradox (Russell's Paradox)", "The barber shaves himself", "The town mayor shaves him", "His apprentice shaves him"],
        "It is a logically impossible paradox (Russell's Paradox)",
        "If he shaves himself, he violates the rule by shaving a man who shaves himself. If he does not, he must shave himself. The premise is self-contradictory.",
        "ایک گاؤں کا حجام صرف ان مردوں کی شیو بناتا ہے جو اپنی شیو خود نہیں بناتے۔ حجام کی شیو کون بناتا ہے؟",
        ["یہ ایک ناممکن منطقی معمہ ہے (رسل کا پیراڈاکس)", "حجام اپنی شیو خود بناتا ہے", "گاؤں کا چوہدری بناتا ہے", "اس کا شاگرد بناتا ہے"],
        "یہ ایک ناممکن منطقی معمہ ہے (رسل کا پیراڈاکس)",
        "اگر حجام اپنی شیو خود بنائے تو وہ اس اصول کو توڑتا ہے کہ وہ صرف ان کی بناتا ہے جو خود نہیں بناتے۔ اور اگر نہ بنائے تو اسے اپنی بنانی پڑے گی۔ یہ ایک منطقی تضاد ہے۔"
    ),
    (
        "An elevator cable snaps at the 40th floor. Can a passenger survive the terminal impact by jumping upward right as the cab hits the ground floor?",
        ["No, human jumping speed (2-3 m/s) barely offsets the catastrophic downward impact speed (30+ m/s)", "Yes, jumping cancels momentum completely", "Only if the elevator is padded with foam", "Yes, if they jump horizontally"],
        "No, human jumping speed (2-3 m/s) barely offsets the catastrophic downward impact speed (30+ m/s)",
        "Free fall from the 40th floor accelerates the cab and passenger to ~35 m/s. An upward jump of 3 m/s leaves a fatal net impact velocity of 32 m/s.",
        "چالیسویں منزل سے لفٹ کی تار ٹوٹ گئی اور وہ نیچے گری۔ کیا مسافر زمین سے ٹکرانے کے عین آخری سیکنڈ میں اوپر چھلانگ لگا کر اپنی جان بچا سکتا ہے؟",
        ["نہیں، انسان کی اوپر چھلانگ کی معمولی رفتار (3 میٹر فی سیکنڈ) نیچے گرنے کی ہولناک رفتار (35 میٹر فی سیکنڈ) کو نہیں روک سکتی", "ہاں، چھلانگ لگانے سے گرنے کی رفتار صفر ہو جائے گی", "صرف اگر فرش پر فوم بچھا ہو", "ہاں، اگر وہ دائیں بائیں چھلانگ لگائے"],
        "نہیں، انسان کی اوپر چھلانگ کی معمولی رفتار (3 میٹر فی سیکنڈ) نیچے گرنے کی ہولناک رفتار (35 میٹر فی سیکنڈ) کو نہیں روک سکتی",
        "گرتے ہوئے انسان کی رفتار 120 کلومیٹر فی گھنٹہ سے زیادہ ہو چکی ہوتی ہے۔ اس رفتار میں اوپر کی چھوٹی سی چھلانگ محض معمولی فرق ڈالتی ہے جو ہلاکت سے نہیں بچا سکتی۔"
    ),
    (
        "Can a container of warm water freeze into solid ice faster than an identical container of cold water under specific conditions?",
        ["Yes, known scientifically as the Mpemba effect", "No, it violates the First Law of Thermodynamics", "Only if heavy salt is added", "Only in the vacuum of space"],
        "Yes, known scientifically as the Mpemba effect",
        "The Mpemba effect occurs due to rapid surface evaporation, dissolved gas expulsion, and convective temperature gradients in warm water.",
        "کیا مخصوص حالات میں گرم پانی کا پیالہ اتنے ہی ٹھنڈے پانی کے پیالے سے پہلے برف میں جم سکتا ہے؟",
        ["ہاں، سائنسی طور پر اسے ایمپیمبا اثر (Mpemba effect) کہا جاتا ہے", "نہیں، یہ تھرموڈائنامکس کے قانون کے خلاف ہے", "صرف اگر پانی میں نمک ملایا جائے", "صرف خلا کے ویکیوم میں"],
        "ہاں، سائنسی طور پر اسے ایمپیمبا اثر (Mpemba effect) کہا جاتا ہے",
        "ایمپیمبا اثر کے تحت گرم پانی کی سطح سے بخارات تیزی سے اڑتے ہیں جس سے پانی کا حجم گھٹتا ہے اور اندرونی لہریں ٹھنڈک کو تیزی سے پھیلا کر اسے جلد جما دیتی ہیں۔"
    ),
    (
        "Why do commercial airplanes fly at high altitudes of 33,000 to 40,000 feet rather than low over the terrain?",
        ["Thinner atmospheric air density drastically reduces aerodynamic parasitic drag, maximizing jet fuel economy", "Gravity is significantly lower at high altitude", "To stay warm above cloud layers", "Jet engines require high carbon dioxide"],
        "Thinner atmospheric air density drastically reduces aerodynamic parasitic drag, maximizing jet fuel economy",
        "Air density at 35,000 ft is roughly one-third of sea-level density. Low drag enables jet airliners to cruise at 550 mph with minimal thrust.",
        "مسافر ہوائی جہاز زمین کے قریب اڑنے کی بجائے 35 سے 40 ہزار فٹ کی شدید بلندی پر پرواز کیوں کرتے ہیں؟",
        ["بلندی پر ہوا کی کثافت انتہائی کم ہوتی ہے جس سے رگڑ اور رکاوٹ (Air drag) گھٹ کر ایندھن کی زبردست بچت ہوتی ہے", "بلندی پر کشش ثقل بہت کم ہو جاتی ہے", "بادلوں کے اوپر گرم رہنے کے لیے", "انجن کو کاربن ڈائی آکسائیڈ چاہیے ہوتی ہے"],
        "بلندی پر ہوا کی کثافت انتہائی کم ہوتی ہے جس سے رگڑ اور رکاوٹ (Air drag) گھٹ کر ایندھن کی زبردست بچت ہوتی ہے",
        "زمین کے قریب ہوا گاڑھی ہوتی ہے جہاں اڑنے کے لیے دگنا پیٹرول جلتا ہے۔ 35 ہزار فٹ پر ہوا اتنی پتلی ہوتی ہے کہ جہاز 900 کلومیٹر فی گھنٹہ کی رفتار سے کم خرچ پر پھسلتا ہے۔"
    ),
    (
        "If you leave an ordinary household refrigerator running continuously with its door wide open inside a sealed, perfectly insulated room, what happens to the room temperature?",
        ["The room temperature increases overall", "The room temperature decreases overall", "The room temperature remains perfectly unchanged", "The room turns into a walk-in freezer"],
        "The room temperature increases overall",
        "The refrigerator compressor converts electrical energy into heat. By thermodynamics, heat rejected at the condenser exceeds heat absorbed at the evaporator.",
        "اگر ایک مکمل بند اور انسولیٹڈ کمرے میں عام فریج کا دروازہ مستقل کھلا چھوڑ دیا جائے تو کمرے کے درجہ حرارت پر کیا اثر پڑے گا؟",
        ["کمرے کا درجہ حرارت مجموعی طور پر بڑھ جائے گا (کمرہ گرم ہو جائے گا)", "کمرہ ٹھنڈا ہو جائے گا", "درجہ حرارت بالکل وہی رہے گا", "کمرہ فریزر بن جائے گا"],
        "کمرے کا درجہ حرارت مجموعی طور پر بڑھ جائے گا (کمرہ گرم ہو جائے گا)",
        "فریج کوئی جادوئی مشین نہیں ہے۔ اس کی موٹر بجلی چلاتی ہے جس سے حرارت بنتی ہے۔ فریج جتنی ٹھنڈک آگے پھینکتا ہے اس سے زیادہ گرمی پیچھے والی جالی سے کمرے میں خارج کرتا ہے۔"
    ),
    (
        "If Earth's rotational speed instantly doubled, what would happen to an individual's measured body weight on a scale at the equator?",
        ["Apparent weight would decrease slightly due to increased outward centrifugal acceleration", "Apparent weight would double", "Apparent weight would remain identical", "Weight would drop to absolute zero"],
        "Apparent weight would decrease slightly due to increased outward centrifugal acceleration",
        "Measured weight W = m(g - omega^2 * R). Doubling angular velocity omega quadruples centrifugal acceleration, reducing net downward scale force.",
        "اگر زمین کی اپنے محور پر گھومنے کی رفتار اچانک دگنی ہو جائے تو خط استوا (Equator) پر وزن کرنے والی مشین پر انسان کا وزن کیا ہوگا؟",
        ["انسان کا ناپا گیا وزن تھوڑا سا کم ہو جائے گا کیونکہ مرکز گریز قوت (Centrifugal force) بڑھ جائے گی", "وزن دگنا ہو جائے گا", "وزن بالکل وہی رہے گا", "وزن صفر ہو جائے گا"],
        "انسان کا ناپا گیا وزن تھوڑا سا کم ہو جائے گا کیونکہ مرکز گریز قوت (Centrifugal force) بڑھ جائے گی",
        "زمین کے تیز گھومنے سے باہر پھینکنے والی مرکز گریز قوت چار گنا بڑھ جائے گی جو نیچے کی کشش ثقل کے اثر کو معمولی کم کر کے وزن کی ریڈنگ کو گرا دے گی۔"
    ),
    (
        "Why does hot coffee cool down significantly faster when you blow gently across the liquid's surface?",
        ["It sweeps away the saturated humid vapor layer, accelerating evaporative cooling", "Your breath is cold like ice", "It forces cooler liquid to the top", "It oxidizes coffee beans chemically"],
        "It sweeps away the saturated humid vapor layer, accelerating evaporative cooling",
        "Blowing displaces the humid boundary layer above the cup, lowering local vapor pressure and allowing high-kinetic-energy molecules to evaporate rapidly.",
        "گرم چائے یا کافی کی پیالی پر منہ سے پھونک مارنے سے وہ اتنی جلدی ٹھنڈی کیوں ہو جاتی ہے؟",
        ["پھونک مارنے سے سطح پر جمی بھاپ کی مرطوب تہہ ہٹ جاتی ہے اور بخارات بننے کا عمل (Evaporation) تیز ہو جاتا ہے", "منہ کی پھونک برف کی طرح ٹھنڈی ہوتی ہے", "ٹھنڈا مائع اوپر آ جاتا ہے", "کافی میں آکسیجن گھل جاتی ہے"],
        "پھونک مارنے سے سطح پر جمی بھاپ کی مرطوب تہہ ہٹ جاتی ہے اور بخارات بننے کا عمل (Evaporation) تیز ہو جاتا ہے",
        "چائے کی سطح پر بھاپ کی ایک گیلی تہہ بن جاتی ہے جو مزید پانی اڑنے نہیں دیتی۔ پھونک اس رکاوٹ کو اڑا دیتی ہے جس سے چائے کے گرم ترین مالیکیولز فوراً ہوا میں اڑ جاتے ہیں۔"
    ),
    (
        "In a complete vacuum chamber, an iron cannonball and a light bird feather are dropped simultaneously from identical heights. Which hits the ground first?",
        ["Both hit the ground at the exact same instant", "The iron cannonball hits first", "The bird feather hits first", "The one dropped with higher velocity"],
        "Both hit the ground at the exact same instant",
        "In vacuum with zero air resistance, gravitational acceleration g = GM/R^2 is completely independent of the falling object's mass.",
        "مکمل خلا (Vacuum) میں ایک بھاری لوہے کا گولہ اور پرندے کا ہلکا پر ایک ساتھ ایک ہی بلندی سے گرائے جائیں تو پہلے کون زمین پر پہنچے گا؟",
        ["دونوں بالکل ایک ہی لمحے میں ایک ساتھ زمین سے ٹکرائیں گے", "لوہے کا گولہ پہلے ٹکرائے گا", "پرندے کا پر پہلے پہنچے گا", "جسے زیادہ زور سے چھوڑا گیا ہو"],
        "دونوں بالکل ایک ہی لمحے میں ایک ساتھ زمین سے ٹکرائیں گے",
        "گیلیلیو کے تجربے کے مطابق ہوا کی رکاوٹ نہ ہو تو کشش ثقل تمام چیزوں کو ایک ہی رفتار (9.8 میٹر فی سیکنڈ اسکوائر) سے نیچے کھینچتی ہے چاہے وزن کتنا ہی مختلف ہو۔"
    ),
    (
        "Why does a highway asphalt road appear like a shimmering pool of reflective water on a hot sunny day (an inferior mirage)?",
        ["Hot, low-density air near the pavement refracts light rays from the sky upward into the driver's eyes", "Water seeps out of hot tar", "Car windshields project reflections", "Heat waves distort eye retinas"],
        "Hot, low-density air near the pavement refracts light rays from the sky upward into the driver's eyes",
        "Ground heat creates an inverted vertical air density gradient. Rays from the blue sky bend upward toward cooler, denser air, mimicking a water reflection.",
        "سخت گرمی کے دن دور تارکول کی سڑک پر پانی کا تالاب چمکتا ہوا کیوں نظر آتا ہے جو قریب جانے پر غائب ہو جاتا ہے (سراب)؟",
        ["سڑک سے لگ کر دہکتی ہوئی گرم ہوا نیلی آسمانی روشنی کو اوپر کی طرف موڑ کر آنکھوں تک پہنچاتی ہے (انعطاف)", "تارکول سے اصلی پانی رس کر نکلتا ہے", "گاڑی کے شیشے کا عکس ہوتا ہے", "گرمی آنکھ کے پردے کو بگاڑ دیتی ہے"],
        "سڑک سے لگ کر دہکتی ہوئی گرم ہوا نیلی آسمانی روشنی کو اوپر کی طرف موڑ کر آنکھوں تک پہنچاتی ہے (انعطاف)",
        "سڑک کے بالکل اوپر ہوا شدید گرم اور ہلکی ہوتی ہے۔ اوپر سے آنے والی نیلی روشنی اس گرم تہہ سے ٹکرا کر مڑتی ہے جسے ہمارا دماغ سڑک پر پانی کا تالاب سمجھتا ہے۔"
    ),
    (
        "Why is diamond completely transparent to visible light, while graphite—composed of pure carbon atoms of the exact same element—is completely black and opaque?",
        ["Diamond's sp3 hybridized electron band gap is too wide to absorb visible photons, while graphite has free delocalized pi electrons", "Diamond is made of crystallized glass", "Graphite absorbs light due to heavy weight", "Diamond reflects 100 percent of light"],
        "Diamond's sp3 hybridized electron band gap is too wide to absorb visible photons, while graphite has free delocalized pi electrons",
        "Diamond has a 5.5 eV band gap, far exceeding visible photon energy (1.8-3.1 eV). Graphite's delocalized pi electron sheets absorb across all visible frequencies.",
        "ہیرا اور گریفائٹ (پنسل کا سکہ) دونوں خالص کاربن سے بنے ہیں، مگر ہیرا بالکل شفاف چمکدار اور گریفائٹ کالا سیاہ کیوں ہوتا ہے؟",
        ["ہیرے کے ایٹمی بانڈز اتنے مضبوط ہیں کہ وہ نظر آنے والی روشنی کو جذب نہیں کرتے، جبکہ گریفائٹ کے آزاد الیکٹرانز تمام روشنی پی جاتے ہیں", "ہیرا شیشے کا بنا ہوتا ہے", "گریفائٹ وزنی ہونے کی وجہ سے کالا ہے", "ہیرا تمام روشنی واپس پلٹاتا ہے"],
        "ہیرے کے ایٹمی بانڈز اتنے مضبوط ہیں کہ وہ نظر آنے والی روشنی کو جذب نہیں کرتے، جبکہ گریفائٹ کے آزاد الیکٹرانز تمام روشنی پی جاتے ہیں",
        "ہیرے کے کاربن ایٹم تین جہتی جڑے ہوتے ہیں جن کا انرجی گیپ روشنی سے بڑا ہوتا ہے اس لیے روشنی آر پار گزر جاتی ہے، گریفائٹ کی تہوں کے آزاد الیکٹران ہر رنگ کی روشنی چوس لیتے ہیں۔"
    ),
    (
        "When visible light enters a glass prism from air, its speed decreases by about 33 percent. Does the light wave's frequency change?",
        ["No, frequency remains constant while wavelength decreases proportionally", "Yes, frequency decreases by 33 percent", "Yes, frequency increases by 33 percent", "Frequency drops to absolute zero"],
        "No, frequency remains constant while wavelength decreases proportionally",
        "Frequency is determined strictly by the oscillating source wave generator. Inside optical media, velocity v and wavelength lambda change (v = f * lambda).",
        "روشنی جب ہوا سے شیشے کے منشور (Prism) میں داخل ہوتی ہے تو اس کی رفتار 33 فیصد کم ہو جاتی ہے۔ کیا روشنی کی فریکوئنسی (Frequency) بھی بدلتی ہے؟",
        ["نہیں، فریکوئنسی بالکل وہی رہتی ہے جبکہ طول موج (Wavelength) کم ہو جاتی ہے", "ہاں، فریکوئنسی 33 فیصد گھٹ جاتی ہے", "ہاں، فریکوئنسی 33 فیصد بڑھ جاتی ہے", "فریکوئنسی صفر ہو جاتی ہے"],
        "نہیں، فریکوئنسی بالکل وہی رہتی ہے جبکہ طول موج (Wavelength) کم ہو جاتی ہے",
        "روشنی کی فریکوئنسی روشنی کے منبع سے طے ہوتی ہے جو کبھی نہیں بدلتی۔ جب رفتار سست ہوتی ہے تو لہریں ایک دوسرے کے قریب آ کر ویو لینتھ چھوٹی کر لیتی ہیں۔"
    ),
    (
        "If you shine a flashlight forward from the front bumper of a spaceship traveling at 99 percent of the speed of light, at what speed does the light beam travel?",
        ["At the speed of light (c) in all inertial reference frames", "At 1.99 times the speed of light", "At 0.99 times the speed of light", "At double the speed of sound"],
        "At the speed of light (c) in all inertial reference frames",
        "Einstein's Special Theory of Relativity postulation: the vacuum speed of light c (300,000 km/s) is invariant across all inertial frames of reference.",
        "اگر ایک خلائی جہاز روشنی کی 99 فیصد رفتار سے اڑ رہا ہو اور اس کے آگے سے ٹارچ جلائی جائے، تو اس ٹارچ کی روشنی کس رفتار سے آگے بڑھے گی؟",
        ["روشنی کی معیاری رفتار (c) سے ہی آگے بڑھے گی، اس سے تیز نہیں", "روشنی کی رفتار سے 1.99 گنا تیز", "روشنی کی رفتار کے 99 فیصد پر", "آواز سے دگنی رفتار پر"],
        "روشنی کی معیاری رفتار (c) سے ہی آگے بڑھے گی، اس سے تیز نہیں",
        "آئن اسٹائن کے نظریہ اضافیت کا بنیادی اصول ہے کہ خلا میں روشنی کی رفتار کائنات کی حتمی حد ہے۔ چاہے پھینکنے والا کتنی ہی تیز رفتار کیوں نہ ہو، روشنی کی رفتار ہمیشہ 3 لاکھ کلومیٹر فی سیکنڈ ہی ناپی جائے گی۔"
    ),
    (
        "Why does a person looking at their watch in a spaceship traveling near light speed experience time normally, while Earth observers see their clock ticking extremely slowly?",
        ["Special relativistic time dilation occurs between relative frames; proper time is invariant in one's own rest frame", "The watch mechanical gears warp from gravity", "Space is too cold for clocks", "Light bends inside watches"],
        "Special relativistic time dilation occurs between relative frames; proper time is invariant in one's own rest frame",
        "Time is relative to the observer's inertial frame: dt' = gamma * dt. In your own rest frame, proper time ticks normally; moving clocks run slow to outside observers.",
        "روشنی کی رفتار کے قریب سفر کرنے والے خلا باز کو اپنی گھڑی بالکل نارمل چلتی محسوس ہوتی ہے، مگر زمین والوں کو اس کی گھڑی انتہائی سست کیوں نظر آتی ہے؟",
        ["وقت کی اضافیت (Time dilation) کی وجہ سے ہر انسان کو اپنا وقت نارمل لگتا ہے مگر دوسرے فریم کے لیے حرکت کرنے والا وقت سست ہو جاتا ہے", "گھڑی کے گیئرز کشش ثقل سے مڑ جاتے ہیں", "خلا گھڑیوں کے لیے بہت سرد ہے", "روشنی گھڑی کے اندر مڑ جاتی ہے"],
        "وقت کی اضافیت (Time dilation) کی وجہ سے ہر انسان کو اپنا وقت نارمل لگتا ہے مگر دوسرے فریم کے لیے حرکت کرنے والا وقت سست ہو جاتا ہے",
        "وقت کا بہاؤ رفتار کے ساتھ جڑا ہے۔ خلا باز اپنے فریم میں ساکن ہے اس لیے اس کا جسم اور گھڑی نارمل رفتار پر چلتے ہیں، مگر زمین کے مشاہدے میں اس کا ہر سیکنڈ پھیل کر طویل ہو چکا ہوتا ہے۔"
    ),
    (
        "Why does a nuclear reactor core glow with an eerie, unearthly blue light underwater (Cherenkov radiation)?",
        ["Charged beta particles travel through water faster than the phase velocity of light in that medium (c / 1.33)", "Uranium emits blue laser light", "Water turns radioactive and glows", "Lead shielding sparks underwater"],
        "Charged beta particles travel through water faster than the phase velocity of light in that medium (c / 1.33)",
        "In water, light travels at 0.75c (~225,000 km/s). Relativistic electrons exceeding this local speed produce an optical shockwave analogous to a sonic boom.",
        "ایٹمی ری ایکٹر کے حوض میں پانی کے نیچے نیلی پراسرار چمک (Cherenkov radiation) کیوں ابھرتی ہے؟",
        ["جب تابکار ذرات پانی میں روشنی کی مقامی رفتار (2.25 لاکھ کلومیٹر فی سیکنڈ) سے بھی زیادہ تیز دوڑتے ہیں تو بصری صوتی دھماکہ (Optical shockwave) بنتا ہے", "یورینیم نیلی لیزر خارج کرتا ہے", "پانی تابکار ہو کر چمکتا ہے", "سیسے کی شیلڈ پانی میں چنگاریاں چھوڑتی ہے"],
        "جب تابکار ذرات پانی میں روشنی کی مقامی رفتار (2.25 لاکھ کلومیٹر فی سیکنڈ) سے بھی زیادہ تیز دوڑتے ہیں تو بصری صوتی دھماکہ (Optical shockwave) بنتا ہے",
        "پانی میں روشنی کی رفتار کم ہو جاتی ہے۔ جب ری ایکٹر کے تیز الیکٹران پانی میں روشنی سے بھی آگے نکل جاتے ہیں تو وہ آواز کے سونک بوم کی طرح روشنی کا ایک نیلگوں شاک ویو پیدا کرتے ہیں۔"
    ),
    (
        "Why do astronauts inside the International Space Station float in weightlessness, even though Earth's gravity at their altitude (400 km) is roughly 90 percent of surface gravity?",
        ["The space station and astronauts are in continuous free fall toward Earth while traveling sideways at orbital speed (17,500 mph)", "Earth's gravity stops at 100 km", "Rocket thrusters constantly push against gravity", "Space station shields block gravity"],
        "The space station and astronauts are in continuous free fall toward Earth while traveling sideways at orbital speed (17,500 mph)",
        "Centripetal acceleration equals local gravitational acceleration (v^2 / R = g). The spacecraft falls around Earth continuously, producing apparent zero-G.",
        "بین الاقوامی خلائی اسٹیشن (ISS) کے اندر خلا باز بے وزنی میں کیوں تیرتے ہیں حالانکہ 400 کلومیٹر کی بلندی پر زمین کی کشش ثقل عام کشش کا تقریباً 90 فیصد موجود ہوتی ہے؟",
        ["خلائی اسٹیشن اور خلا باز مسلسل زمین کی طرف گر رہے ہیں (Free fall) مگر تیز افقی رفتار کی وجہ سے زمین کے گرد چکر میں رہتے ہیں", "زمین کی کشش 100 کلومیٹر پر ختم ہو جاتی ہے", "راکٹ انجن کشش ثقل کو مسلسل روکتے ہیں", "خلائی اسٹیشن کی دیواریں کشش ثقل روکتی ہیں"],
        "خلائی اسٹیشن اور خلا باز مسلسل زمین کی طرف گر رہے ہیں (Free fall) مگر تیز افقی رفتار کی وجہ سے زمین کے گرد چکر میں رہتے ہیں",
        "خلا باز گر رہے ہیں مگر اتنی تیز افقی رفتار سے کہ زمین کی گولائی ان کے نیچے سے اتنی ہی مڑ جاتی ہے۔ لفٹ کی تار ٹوٹنے کی طرح وہ ہر وقت گرنے کی حالت میں تیرتے رہتے ہیں۔"
    ),
    (
        "Why does a spinning T-shaped handle or tennis racket flip its orientation periodically when spun about its intermediate principal axis in zero gravity (Dzhanibekov effect)?",
        ["Rotation around the intermediate principal moment of inertia is mathematically unstable according to Euler's equations", "Zero gravity creates centrifugal torsion", "Air friction twists the handle", "Magnetic poles flip the object"],
        "Rotation around the intermediate principal moment of inertia is mathematically unstable according to Euler's equations",
        "The tennis racket theorem proves that rotation about the axes with maximal or minimal moments of inertia is stable, while the intermediate axis exhibits chaotic flipping.",
        "خلا میں ٹی ہینڈل (T-handle) یا ٹینس ریکیٹ کو درمیانی محور پر گھمانے پر وہ چند چکروں بعد اچانک خود بخود الٹ (Flip) کیوں جاتا ہے (Dzhanibekov effect)؟",
        ["جسم کے تینوں محوروں میں سے درمیانی محور پر گردش اویلر کی مساوات کے مطابق ریاضیاتی طور پر غیر مستحکم ہوتی ہے", "خلا میں مرکز گریز قوت الٹ جاتی ہے", "ہوا کی رگڑ ہینڈل کو مروڑتی ہے", "مقناطیسی قطبین چیز کو گھما دیتے ہیں"],
        "جسم کے تینوں محوروں میں سے درمیانی محور پر گردش اویلر کی مساوات کے مطابق ریاضیاتی طور پر غیر مستحکم ہوتی ہے",
        "ٹینس ریکیٹ تھیورم ثابت کرتا ہے کہ سب سے وزنی اور سب سے ہلکے محور پر گھومنا تو مستحکم رہتا ہے مگر درمیانے محور کی گردش تھرکن پیدا کر کے ہر چند سیکنڈ بعد رخ الٹ دیتی ہے۔"
    ),
    (
        "How can the tiny mantis shrimp strike with enough explosive speed under water to shatter heavy aquarium glass walls?",
        ["Its club accelerates faster than a rifle bullet (10,000 Gs), generating cavitation bubbles whose collapse produces immense acoustic shockwaves and 4,000°C temperatures", "It has electric stun organs like an eel", "It shoots pressurized venom needles", "It cuts glass with diamond teeth"],
        "Its club accelerates faster than a rifle bullet (10,000 Gs), generating cavitation bubbles whose collapse produces immense acoustic shockwaves and 4,000°C temperatures",
        "Spring-loaded biological dactyl clubs release stored elastic energy in microseconds; the hydrodynamic cavitation vacuum bubble collapse creates secondary destructive shockwaves.",
        "مینٹس شرمپ (Mantis shrimp) نامی چھوٹا جھینگا اپنے پنجے سے اتنی ہولناک چوٹ کیسے مارتا ہے کہ ایکوائریئم کا موٹا شیشہ بھی ٹوٹ جاتا ہے؟",
        ["اس کا پنجہ گولی کی رفتار سے چل کر پانی میں کیویٹیشن بلبلے بناتا ہے جن کے پھٹنے سے ہزاروں ڈگری درجہ حرارت اور دھماکہ خیز شاک ویوز پیدا ہوتی ہیں", "اس میں بجلی کے جھٹکے دینے والے اعضا ہوتے ہیں", "وہ زہریلی سوئیاں چلاتا ہے", "اس کے دانت ہیرے کے بنے ہوتے ہیں"],
        "اس کا پنجہ گولی کی رفتار سے چل کر پانی میں کیویٹیشن بلبلے بناتا ہے جن کے پھٹنے سے ہزاروں ڈگری درجہ حرارت اور دھماکہ خیز شاک ویوز پیدا ہوتی ہیں",
        "جھینگا اپنے پنجے کو کمان کی طرح تان کر چھوڑتا ہے جس سے پانی اتنی تیزی سے ہٹتا ہے کہ خلا بن جاتا ہے۔ جب وہ کیویٹیشن بلبلہ پھٹتا ہے تو سورج کی سطح جیسی حرارت اور دھماکہ شیشے کو توڑ دیتا ہے۔"
    ),
    (
        "Why does a spoon curved side placed under a smooth stream of running tap water get sucked strongly into the water stream rather than pushed away?",
        ["Fluid clings to the convex surface, and the deflected flow creates a low-pressure zone that pulls the spoon in (Coandă effect)", "Water magnetizes the stainless steel", "Surface tension pushes the spoon", "Air pressure pushes water out"],
        "Fluid clings to the convex surface, and the deflected flow creates a low-pressure zone that pulls the spoon in (Coandă effect)",
        "The Coandă effect describes fluid adhesion to a curved surface; by Newton's Third Law, deflecting fluid outward exerts an equal inward force on the spoon.",
        "نلکے کے بہتے پانی کے نیچے چمچ کے ابھرے ہوئے رخ کو لانے پر چمچ پانی سے دور بھاگنے کی بجائے پانی کے اندر کیوں کھنچ جاتا ہے؟",
        ["پانی کا بہاؤ مڑی ہوئی سطح کے ساتھ چپک کر مڑتا ہے جس سے کم دباؤ کا خلا بن کر چمچ کو پانی کی طرف کھینچتا ہے (Coandă effect)", "پانی لوہے کو مقناطیس بنا دیتا ہے", "سطحی تناؤ چمچ کو دھکیلتا ہے", "ہوا کا دباؤ پانی کو اچھالتا ہے"],
        "پانی کا بہاؤ مڑی ہوئی سطح کے ساتھ چپک کر مڑتا ہے جس سے کم دباؤ کا خلا بن کر چمچ کو پانی کی طرف کھینچتا ہے (Coandă effect)",
        "کوآنڈا اثر بتاتا ہے کہ بہتا ہوا مائع گول سطح کے ساتھ مڑ جاتا ہے۔ جب پانی باہر کی طرف مڑتا ہے تو نیوٹن کے تیسرے قانون کے تحت وہ چمچ کو اپنے اندر کھینچ لیتا ہے۔"
    ),
    (
        "Why does a baseball pitcher's curveball swerve dramatically sideways in mid-air when thrown with high topspin or sidespin?",
        ["Air travels faster over the side spinning in the direction of flight, lowering pressure and creating lateral aerodynamic force (Magnus effect)", "The pitcher's fingers grease the ball", "Wind currents follow the seams", "Earth's gravity bends the ball sideways"],
        "Air travels faster over the side spinning in the direction of flight, lowering pressure and creating lateral aerodynamic force (Magnus effect)",
        "The Magnus effect: the spinning surface drags a thin air boundary layer, accelerating airflow on one side and decelerating it on the other, creating a net lateral pressure imbalance.",
        "بیس بال یا کرکٹ میں گھومتی ہوئی گیند (Spin/Curveball) ہوا میں اچانک ایک طرف تیز موڑ (Swerve) کیوں کاٹتی ہے؟",
        ["گھومنے کی سمت والے رخ پر ہوا کی رفتار تیز ہونے سے دباؤ گر جاتا ہے جو گیند کو سائیڈ میں کھینچ لیتا ہے (Magnus effect)", "بالر گیند پر چکنائی لگا دیتا ہے", "ہوا صرف سلائی کے پیچھے چلتی ہے", "کشش ثقل گیند کو ٹیڑھا کر دیتی ہے"],
        "گھومنے کی سمت والے رخ پر ہوا کی رفتار تیز ہونے سے دباؤ گر جاتا ہے جو گیند کو سائیڈ میں کھینچ لیتا ہے (Magnus effect)",
        "میگنس اثر بتاتا ہے کہ گھومتی ہوئی گیند ایک طرف کی ہوا کو تیز اور دوسری طرف کی ہوا کو سست کر دیتی ہے۔ برنولی کے اصول سے کم دباؤ کی طرف گیند ہوا میں غوطہ کھاتی ہے۔"
    ),
    (
        "Why does a mixture of cornstarch and water (Oobleck) behave like a runny liquid when stirred gently, but turns into a rock-solid surface when punched with a fist?",
        ["High shear stress forces starch granules to jam mechanically into a rigid interlocked crystalline network (shear-thickening dilatant fluid)", "The water evaporates instantly under pressure", "Friction heats the starch into glue", "Air bubbles expand under impact"],
        "High shear stress forces starch granules to jam mechanically into a rigid interlocked crystalline network (shear-thickening dilatant fluid)",
        "In non-Newtonian dilatant fluids, high strain rates force the lubricating water layer out from between suspended micro-particles, causing physical particle jamming.",
        "کارن اسٹارچ اور پانی کا آمیزہ (Oobleck) آہستہ چھونے پر دودھ جیسا مائع رہتا ہے مگر زور سے گھونسا مارنے پر لوہے کی طرح سخت چٹان کیوں بن جاتا ہے؟",
        ["زوردار جھٹکے (Shear stress) سے نشاستے کے باریک ذرات آپس میں جڑ کر ایک سخت تالہ نما جال بنا لیتے ہیں (Non-Newtonian dilatant fluid)", "دباؤ سے پانی فوری اڑ جاتا ہے", "رگڑ سے آٹا گوند بن جاتا ہے", "ہوا کے بلبلے پھیل جاتے ہیں"],
        "زوردار جھٹکے (Shear stress) سے نشاستے کے باریک ذرات آپس میں جڑ کر ایک سخت تالہ نما جال بنا لیتے ہیں (Non-Newtonian dilatant fluid)",
        "یہ ایک غیر نیوٹنی مائع ہے۔ آہستہ حرکت پر پانی کے مالیکیولز ذرات کے درمیان پھسلتے ہیں، مگر اچانک تیز چوٹ پر پانی سائیڈ میں نکل جاتا ہے اور ذرات آپس میں پھنس کر ٹھوس بن جاتے ہیں۔"
    ),
    (
        "Why does an ordinary flexible plastic siphon hose continue transferring liquid over a high barrier even inside an evacuated vacuum chamber?",
        ["Cohesive intermolecular bonds (liquid tensile strength) pull fluid upward along the hose like a continuous moving chain", "Atmospheric pressure pushes the liquid up", "Gravity pulls the reservoir down", "Capillary action alone drives the siphon"],
        "Cohesive intermolecular bonds (liquid tensile strength) pull fluid upward along the hose like a continuous moving chain",
        "While atmospheric pressure aids siphons in air, experiments prove siphons work in high vacuum through liquid cohesion and gravity imbalance.",
        "سائفن (Siphon) کا پائپ برتن سے اونچی رکاوٹ کے اوپر سے مائع کو کھینچ کر خلا (Vacuum chamber) میں بھی بغیر رکے کیسے بہاتا رہتا ہے؟",
        ["پانی کے مالیکیولز کی باہمی کشش (Liquid tensile strength) ایک لچکدار زنجیر کی طرح مائع کو اوپر کھینچ کر دوسری طرف گراتی ہے", "ہوا کا دباؤ مائع کو دھکیلتا ہے", "کشش ثقل برتن کو سمیٹتی ہے", "صرف کیپلری ایکشن پانی کو چلاتا ہے"],
        "پانی کے مالیکیولز کی باہمی کشش (Liquid tensile strength) ایک لچکدار زنجیر کی طرح مائع کو اوپر کھینچ کر دوسری طرف گراتی ہے",
        "عام طور پر سمجھا جاتا ہے کہ ہوا کا دباؤ سائفن چلاتا ہے، مگر سائنس نے ثابت کیا کہ خلا میں بھی پانی کے اپنے مالیکیولز کی زنجیر وزنی سرے کے پیچھے کھنچتی چلی جاتی ہے۔"
    ),
    (
        "Why does a smoke ring or vortex cannon ring maintain its tight donut shape and travel stable across an entire room without dispersing?",
        ["Toroidal poloidal rotation creates an isolated self-contained pressure vortex boundary that minimizes turbulent mixing with ambient air", "Smoke is heavier than surrounding room air", "Thermal energy forms a hard crust", "Gravity pins the ring horizontally"],
        "Toroidal poloidal rotation creates an isolated self-contained pressure vortex boundary that minimizes turbulent mixing with ambient air",
        "Fluid circulating around the ring core induces an internal velocity field that propels the vortex forward while laminar shear isolates it from room friction.",
        "دھوئیں کا چھلا (Smoke ring) یا ورٹیکس کینن سے نکلا ہوا ہوا کا گول دائرہ پورے کمرے میں بکھرے بغیر اپنی شکل برقرار رکھ کر کیسے سفر کرتا ہے؟",
        ["ڈونٹ نما گردش اپنے اندر ایک گھومتا ہوا کم دباؤ کا حفاظتی گرداب بنا لیتی ہے جو کمرے کی ہوا سے ٹکرانے کو کم سے کم کر دیتا ہے", "دھواں کمرے کی ہوا سے وزنی ہوتا ہے", "حرارت سے سخت خول بن جاتا ہے", "کشش ثقل چھلے کو سیدھا رکھتی ہے"],
        "ڈونٹ نما گردش اپنے اندر ایک گھومتا ہوا کم دباؤ کا حفاظتی گرداب بنا لیتی ہے جو کمرے کی ہوا سے ٹکرانے کو کم سے کم کر دیتا ہے",
        "ورٹیکس رنگ کا مائع اپنے ہی مرکز کے گرد تیزی سے چکر کاٹتا ہے۔ یہ خودکار گھماؤ دائرے کو آگے دھکیلتا ہے اور باہر کی ہوا کو اندر داخل ہونے سے روکے رکھتا ہے۔"
    ),
    (
        "Why does a heavy lead bullet fired into an engine block in a forensic test shatter into fine dust rather than retaining its aerodynamic shape?",
        ["Impact shock wave velocity exceeds the speed of sound in lead, converting kinetic energy into hydrodynamic phase transition and mechanical pulverization", "Lead melts from air friction before impact", "The engine block is magnetized", "Bullet gunpowder ignites again upon impact"],
        "Impact shock wave velocity exceeds the speed of sound in lead, converting kinetic energy into hydrodynamic phase transition and mechanical pulverization",
        "High-velocity impact generates giga-pascal shock pressures far surpassing lead's yield strength; the metal behaves like an incompressible splashing fluid and fragments.",
        "سیسے (Lead) کی وزنی گولی جب گاڑی کے لوہے کے انجن بلاک سے ٹکراتی ہے تو وہ مڑنے کی بجائے دھول بن کر بکھر کیوں جاتی ہے؟",
        ["ٹکراؤ کی شاک ویو کی رفتار سیسے کے اندر آواز کی رفتار سے تجاوز کر جاتی ہے جس سے دھات مائع جیسی بن کر ٹکڑے ٹکڑے ہو جاتی ہے", "گولی ہوا کی رگڑ سے پگھل چکی ہوتی ہے", "انجن بلاک مقناطیسی ہوتا ہے", "ٹکراؤ پر گولی کا بارود دوبارہ پھٹتا ہے"],
        "ٹکراؤ کی شاک ویو کی رفتار سیسے کے اندر آواز کی رفتار سے تجاوز کر جاتی ہے جس سے دھات مائع جیسی بن کر ٹکڑے ٹکڑے ہو جاتی ہے",
        "شدید رفتار پر سیسے کی لچکدار طاقت ختم ہو جاتی ہے۔ ٹکراؤ کا دباؤ اتنا ہولناک ہوتا ہے کہ دھات لمحہ بھر کے لیے مائع بن کر اچھلتی ہے اور ریزہ ریزہ ہو جاتی ہے۔"
    ),
    (
        "Why does breathing helium gas from a party balloon make a human's voice sound high-pitched and cartoonish, even though the vocal cords vibrate at the exact same fundamental frequency?",
        ["Sound travels nearly three times faster in low-density helium, shifting vocal tract acoustic resonance formants to much higher frequencies", "Helium tightens the vocal cord muscles", "Helium paralyzes the larynx nerves", "Helium is an acidic gas"],
        "Sound travels nearly three times faster in low-density helium, shifting vocal tract acoustic resonance formants to much higher frequencies",
        "Vocal cord fundamental frequency remains unchanged; however, acoustic resonant frequencies in the throat cavity scale with sound velocity: v_He = 965 m/s vs v_air = 343 m/s.",
        "ہیلیئم گیس سونگھنے سے انسان کی آواز کارٹون جیسی باریک اور تیز کیوں ہو جاتی ہے حالانکہ گلے کے صوتی پردے (Vocal cords) پہلے والی رفتار سے ہی تھرتھراتے ہیں؟",
        ["ہلکی ہیلیئم گیس میں آواز کی رفتار ہوا سے تین گنا تیز ہو جاتی ہے جس سے گلے کی گونج (Formants) بہت اونچی فریکوئنسی پر چلی جاتی ہے", "ہیلیئم صوتی پردوں کو کھینچ کر سخت کر دیتی ہے", "ہیلیئم گلے کے اعصاب کو سن کر دیتی ہے", "ہیلیئم ایک تیزابی گیس ہے"],
        "ہلکی ہیلیئم گیس میں آواز کی رفتار ہوا سے تین گنا تیز ہو جاتی ہے جس سے گلے کی گونج (Formants) بہت اونچی فریکوئنسی پر چلی جاتی ہے",
        "صوتی پردوں کا ارتعاش نہیں بدلتا، مگر گلے کے پائپ میں آواز کی رفتار 343 میٹر سے بڑھ کر 965 میٹر فی سیکنڈ ہو جاتی ہے، جس سے صوتی گونج باریک ہو کر تیز نکلتی ہے۔"
    ),
    (
        "Why does inhaling dense sulfur hexafluoride (SF6) gas make a person's voice sound dramatically deep, baritone, and demonic?",
        ["Sound travels much slower in heavy SF6 gas (roughly 150 m/s), shifting vocal tract resonant formants downward into deep bass registers", "SF6 paralyzes the vocal cords in an open position", "SF6 cools the larynx to freezing", "SF6 contains audio dampening enzymes"],
        "Sound travels much slower in heavy SF6 gas (roughly 150 m/s), shifting vocal tract resonant formants downward into deep bass registers",
        "SF6 is five times denser than air; lower sound velocity compresses acoustic wavelengths, lowering resonant formant frequencies by over an octave.",
        "سلفر ہیکسا فلورائیڈ (SF6) گیس سونگھنے پر انسان کی آواز اچانک بھاری، گہری اور پراسرار کیوں ہو جاتی ہے؟",
        ["بھاری گیس میں آواز کی رفتار سست (150 میٹر فی سیکنڈ) ہو جاتی ہے جس سے گلے کی گونج نچلے اور گہرے سروں میں تبدیل ہو جاتی ہے", "یہ گیس صوتی پردوں کو کھلا جما دیتی ہے", "یہ گیس گلے کو ٹھنڈا کر دیتی ہے", "اس میں آواز کو موٹا کرنے والے انزائمز ہوتے ہیں"],
        "بھاری گیس میں آواز کی رفتار سست (150 میٹر فی سیکنڈ) ہو جاتی ہے جس سے گلے کی گونج نچلے اور گہرے سروں میں تبدیل ہو جاتی ہے",
        "یہ گیس ہوا سے پانچ گنا زیادہ بھاری ہے۔ اس میں آواز کی لہریں سست پڑ جاتی ہیں، جس سے گلے کی نالی بھاری صوتی لہروں کو ابھار کر آواز کو دیوہیکل بنا دیتی ہے۔"
    ),
    (
        "What unique thermodynamic state allows pure water to exist simultaneously in physical equilibrium as solid ice, liquid water, and water vapor in the same flask?",
        ["The Triple Point of water (0.01°C at 611.65 Pa)", "The Critical Point of water", "Absolute zero temperature", "The Leidenfrost threshold"],
        "The Triple Point of water (0.01°C at 611.65 Pa)",
        "By Gibbs' phase rule, three phases of a pure substance can coexist in equilibrium at precisely zero degrees of freedom: 273.16 K and 0.006 atm.",
        "وہ کون سی منفرد سائنسی حالت ہے جس میں پانی ایک ہی برتن میں بیک وقت ٹھوس برف، مائع پانی اور گیسی بھاپ کی صورت میں توازن میں پایا جاتا ہے؟",
        ["پانی کا ٹرپل پوائنٹ (Triple Point: 0.01 ڈگری سینٹی گریڈ اور 611 پاسکل دباؤ)", "پانی کا کریٹیکل پوائنٹ", "مطلق صفر درجہ حرارت (Absolute zero)", "لائیڈن فروسٹ کی حد"],
        "پانی کا ٹرپل پوائنٹ (Triple Point: 0.01 ڈگری سینٹی گریڈ اور 611 پاسکل دباؤ)",
        "تھرموڈائنامکس کے مطابق ٹرپل پوائنٹ وہ مخصوص دباؤ اور درجہ حرارت ہے جہاں مادے کی تینوں حالتیں (برف، پانی، بھاپ) ایک دوسرے میں تبدیل ہوئے بغیر ایک ساتھ رہتی ہیں۔"
    ),
    (
        "Why does liquid helium-4 cooled below 2.17 Kelvin (superfluid phase) spontaneously climb up and over the glass walls of its container and leak out?",
        ["Zero viscosity and quantum macroscopic coherence allow a sub-microscopic Rollin film to siphon over walls driven by surface tension", "Liquid helium boils into dense gas that condenses outside", "Helium is attracted to glass by nuclear forces", "Gravity reverses sign below 2 Kelvin"],
        "Zero viscosity and quantum macroscopic coherence allow a sub-microscopic Rollin film to siphon over walls driven by surface tension",
        "Below the lambda point, He-4 forms a Bose-Einstein-like superfluid with vanishing shear viscosity; van der Waals wetting drives a 30-nm Rollin film up the container walls.",
        "مائع ہیلیئم کو جب 2.17 کیلون سے نیچے ٹھنڈا کیا جاتا ہے (Superfluid) تو وہ شیشے کے برتن کی دیواروں پر خود بخود اوپر چڑھ کر باہر کیوں بہہ جاتی ہے؟",
        ["اس کی اندرونی لزوجت (Viscosity) صفر ہو جاتی ہے جس سے وہ ایک ایٹم جتنی باریک جھلی (Rollin film) بن کر دیواروں پر رینگ جاتی ہے", "ہیلیئم ابل کر باہر جمتی ہے", "شیشہ ہیلیئم کو ایٹمی کشش سے کھینچتا ہے", "2 کیلون سے نیچے کشش ثقل الٹ جاتی ہے"],
        "اس کی اندرونی لزوجت (Viscosity) صفر ہو جاتی ہے جس سے وہ ایک ایٹم جتنی باریک جھلی (Rollin film) بن کر دیواروں پر رینگ جاتی ہے",
        "سپر فلوئڈ حالت میں رگڑ اور لزوجت مکمل طور پر ختم ہو جاتی ہے۔ سطحی تناؤ مائع کے مالیکیولز کو دیوار پر اوپر کھینچتا ہے اور بغیر کسی رکاوٹ کے برتن خالی ہو جاتا ہے۔"
    ),
    (
        "Why does a high-temperature superconductor expel all magnetic field lines from its interior and levitate above a permanent magnet (Meissner effect)?",
        ["Screening supercurrents form spontaneously on its zero-resistance surface, generating an equal and opposite internal canceling magnetic field", "Superconductors become powerful permanent magnets", "The magnet melts the superconductor surface", "Low temperature destroys magnetic poles"],
        "Screening supercurrents form spontaneously on its zero-resistance surface, generating an equal and opposite internal canceling magnetic field",
        "The Meissner effect is perfect diamagnetism: persistent lossless surface eddy currents induce an interior B-field of zero, locking flux lines in space.",
        "سپر کنڈکٹر (Superconductor) کو مقناطیس کے اوپر رکھنے پر وہ فضا میں معلق (Levitate) ہو کر مقناطیس کے اوپر تیرتا کیوں رہتا ہے (Meissner effect)؟",
        ["سپر کنڈکٹر کی سطح پر بغیر کسی برقی مزاحمت کے ایسے کرنٹ پیدا ہوتے ہیں جو اندرونی مقناطیسی فیلڈ کو مکمل طور پر باہر دھکیل دیتے ہیں", "سپر کنڈکٹر خود ایک مستقل مقناطیس بن جاتا ہے", "مقناطیس سپر کنڈکٹر کو پگھلا دیتا ہے", "سردی مقناطیسی قطبین کو ختم کر دیتی ہے"],
        "سپر کنڈکٹر کی سطح پر بغیر کسی برقی مزاحمت کے ایسے کرنٹ پیدا ہوتے ہیں جو اندرونی مقناطیسی فیلڈ کو مکمل طور پر باہر دھکیل دیتے ہیں",
        "مائسنر اثر کے تحت سپر کنڈکٹر مکمل ڈایا میگنیٹک بن جاتا ہے۔ وہ مقناطیسی لہروں کو اپنے اندر سے گزرنے نہیں دیتا اور مخالف مقناطیسی قوت بنا کر ہوا میں تیرتا رہتا ہے۔"
    ),
    (
        "Why does crushing a wintergreen Lifesaver candy or dry sugar crystal with pliers in pitch darkness produce a vivid flash of visible blue-green light?",
        ["Fracturing asymmetric crystals separates electrical charges that ionize nitrogen in air, exciting fluorescence (triboluminescence)", "Friction ignites miniature sugar explosions", "Pliers spark from static induction", "Sugar turns into radioactive phosphorus"],
        "Fracturing asymmetric crystals separates electrical charges that ionize nitrogen in air, exciting fluorescence (triboluminescence)",
        "Triboluminescence occurs when mechanical fracture shears asymmetric crystalline planes, generating high voltages that discharge like micro-lightning, exciting nitrogen emission.",
        "گھپ اندھیرے میں خشک چینی کے ڈلے یا منٹ کی گولی کو پلاس سے زور سے توڑنے پر نیلے سبز رنگ کی چمکتی ہوئی روشنی (چنگاری) کیوں نکلتی ہے؟",
        ["کرسٹل ٹوٹنے سے مثبت اور منفی برقی چارج الگ ہو کر فضا کی نائٹروجن کو برقی جھٹکا دیتے ہیں جس سے روشنی خارج ہوتی ہے (Triboluminescence)", "رگڑ سے چینی کا بارود پھٹتا ہے", "پلاس کا لوہا چنگاری بناتا ہے", "چینی فاسفورس میں بدل جاتی ہے"],
        "کرسٹل ٹوٹنے سے مثبت اور منفی برقی چارج الگ ہو کر فضا کی نائٹروجن کو برقی جھٹکا دیتے ہیں جس سے روشنی خارج ہوتی ہے (Triboluminescence)",
        "اسے ٹرائیبو لومینیسینس کہتے ہیں۔ جب بے قاعدہ قلمیں ٹوٹتی ہیں تو سطحوں پر لاکھوں وولٹ کا باریک برقی چارج بنتا ہے جو آسمانی بجلی کی طرح فضا میں باریک چمک دکھاتا ہے۔"
    ),
    (
        "Why does a piezo-electric gas grill igniter create a powerful high-voltage spark simply when a spring-loaded mechanical hammer strikes a ceramic crystal?",
        ["Mechanical compressive stress deforms the non-centrosymmetric ceramic crystal lattice, generating kilovolts of piezoelectric voltage", "The hammer strikes flint and steel", "Friction burns ceramic gunpowder", "The hammer generates electromagnetic induction"],
        "Mechanical compressive stress deforms the non-centrosymmetric ceramic crystal lattice, generating kilovolts of piezoelectric voltage",
        "Lead zirconate titanate (PZT) crystals lack inversion symmetry; sudden compressive shock shifts internal dipole moments, creating a 10,000-volt spark gap discharge.",
        "باورچی خانے کے گیس لائٹر کا بٹن دبانے پر ہتھوڑے کی چوٹ سے بغیر کسی بیٹری کے چنگاری کیسے پیدا ہو جاتی ہے؟",
        ["سرامک کرسٹل پر ہتھوڑے کی چوٹ اس کے ایٹمی ڈھانچے کو دبا کر ہزاروں وولٹ کا برقی چارج خارج کرتی ہے (Piezoelectric effect)", "ہتھوڑا پتھر سے ٹکرا کر آگ بناتا ہے", "رگڑ سے بارود جلتا ہے", "ہتھوڑا برقی مقناطیس بناتا ہے"],
        "سرامک کرسٹل پر ہتھوڑے کی چوٹ اس کے ایٹمی ڈھانچے کو دبا کر ہزاروں وولٹ کا برقی چارج خارج کرتی ہے (Piezoelectric effect)",
        "پیزو الیکٹرک کرسٹل کے اندر مثبت اور منفی چارج متوازن ہوتے ہیں۔ ہتھوڑے کی اچانک چوٹ سے ایٹموں کا توازن بگڑتا ہے اور نوک پر دس ہزار وولٹ کی چنگاری اچھلتی ہے۔"
    ),
    (
        "Why did Albert Einstein win the 1921 Nobel Prize in Physics for explaining the Photoelectric Effect rather than for his famous Theory of Relativity?",
        ["He proved that light delivers energy in discrete quantized packets (photons), launching modern quantum mechanics", "The Nobel committee thought Relativity was an optical illusion", "The Photoelectric Effect created atomic bombs", "Relativity had already won earlier"],
        "He proved that light delivers energy in discrete quantized packets (photons), launching modern quantum mechanics",
        "Einstein demonstrated that electron emission depends on incident photon frequency (E = hf), not wave intensity, establishing wave-particle duality.",
        "البرٹ آئن اسٹائن کو نوبل انعام ان کے مشہور نظریہ اضافیت پر نہیں بلکہ 'فوٹو الیکٹرک اثر' (Photoelectric Effect) کی وضاحت پر کیوں دیا گیا تھا؟",
        ["کیونکہ انہوں نے ثابت کیا کہ روشنی لہروں کی بجائے توانائی کے مخصوص پیکٹوں (فوٹونز) کی صورت میں آتی ہے جس نے کوانٹم فزکس کی بنیاد رکھی", "کمیٹی نظریہ اضافیت کو نظر کا دھوکہ سمجھتی تھی", "اس اثر نے ایٹم بم بنایا تھا", "نظریہ اضافیت پہلے جیت چکا تھا"],
        "کیونکہ انہوں نے ثابت کیا کہ روشنی لہروں کی بجائے توانائی کے مخصوص پیکٹوں (فوٹونز) کی صورت میں آتی ہے جس نے کوانٹم فزکس کی بنیاد رکھی",
        "آئن اسٹائن نے دریافت کیا کہ دھات سے الیکٹران نکالنے کے لیے روشنی کی شدت نہیں بلکہ فریکوئنسی ضروری ہے، یعنی روشنی ذرات (فوٹونز) پر مشتمل ہے، جس نے جدید سائنس کا رخ بدل دیا۔"
    ),
    (
        "In the famous quantum double-slit experiment, firing single electrons one at a time through two parallel slits still produces a wavelike interference pattern on the detector screen. Why?",
        ["Each individual electron wave function passes through both slits simultaneously in quantum superposition, interfering with itself", "Electrons collide with air molecules", "The detector screen is magnetized", "Electrons split in half physically"],
        "Each individual electron wave function passes through both slits simultaneously in quantum superposition, interfering with itself",
        "Quantum mechanics dictates particles propagate as probability amplitude waves (psi); the single electron interferes with itself unless a measurement collapses the state.",
        "کوانٹم فزکس کے ڈبل سلٹ تجربے میں اگر ایک وقت میں صرف ایک ہی الیکٹران فائر کیا جائے، تب بھی اسکرین پر لہروں جیسی انٹرفیرنس پٹیاں کیوں بنتی ہیں؟",
        ["ہر اکیلا الیکٹران کوانٹم سپر پوزیشن میں ایک ہی وقت میں دونوں سوراخوں سے گزر کر اپنے آپ کے ساتھ ہی انٹرفیرنس کرتا ہے", "الیکٹران ہوا کے مالیکیولز سے ٹکراتے ہیں", "اسکرین پر مقناطیس لگا ہوتا ہے", "الیکٹران جسمانی طور پر دو ٹکڑے ہو جاتا ہے"],
        "ہر اکیلا الیکٹران کوانٹم سپر پوزیشن میں ایک ہی وقت میں دونوں سوراخوں سے گزر کر اپنے آپ کے ساتھ ہی انٹرفیرنس کرتا ہے",
        "جب تک الیکٹران کو دیکھا یا ناپا نہ جائے وہ مادی گیند نہیں بلکہ امکانات کی لہر ہوتا ہے۔ وہ ایک ساتھ دونوں راستوں سے گزر کر اسکرین پر لہروں کا جال بناتا ہے۔"
    ),
    (
        "What happens in the quantum double-slit experiment if researchers place a physical detector at one of the slits to observe exactly which slit the electron passes through?",
        ["The wave interference pattern instantly vanishes, replaced by two simple ballistic bands of particle hits", "The electrons stop moving completely", "The electrons reflect backward into the gun", "The interference pattern becomes twice as bright"],
        "The wave interference pattern instantly vanishes, replaced by two simple ballistic bands of particle hits",
        "The act of measurement forces wave function collapse, destroying quantum phase coherence and eliminating quantum superposition interference.",
        "اگر ڈبل سلٹ کے ایک سوراخ پر کیمرہ یا ڈیٹیکٹر لگا دیا جائے تاکہ معلوم ہو سکے کہ الیکٹران کس سوراخ سے گزرا، تو اسکرین پر کیا نتیجہ نکلتا ہے؟",
        ["لہروں کا خوبصورت جال فوری طور پر غائب ہو جاتا ہے اور بندوق کی گولیوں کی طرح صرف دو سیدھی لکیریں بن جاتی ہیں", "الیکٹران حرکت کرنا بند کر دیتے ہیں", "الیکٹران واپس گن میں پلٹ جاتے ہیں", "لہروں کا جال دگنا چمکدار ہو جاتا ہے"],
        "لہروں کا خوبصورت جال فوری طور پر غائب ہو جاتا ہے اور بندوق کی گولیوں کی طرح صرف دو سیدھی لکیریں بن جاتی ہیں",
        "مشاہدہ کرنے کا عمل کوانٹم ویو فنکشن کو توڑ دیتا ہے۔ جس لمحے ہم جاننے کی کوشش کرتے ہیں کہ الیکٹران کہاں سے گزرا، وہ لہر کی بجائے عام مادی ذرہ بن کر گرتا ہے۔"
    ),
    (
        "Why did Albert Einstein famously reject the philosophical implications of quantum entanglement, calling it 'spooky action at a distance'?",
        ["Measuring one entangled particle instantly determines the state of the other across light-years, seemingly violating relativistic locality", "He proved entanglement violates energy conservation", "Entangled particles generate infinite heat", "Entanglement is caused by gravity waves"],
        "Measuring one entangled particle instantly determines the state of the other across light-years, seemingly violating relativistic locality",
        "Einstein believed in local realism; Bell's theorem and subsequent experiments proved nature is fundamentally non-local, validating quantum entanglement.",
        "آئن اسٹائن نے کوانٹم الجھاؤ (Quantum Entanglement) کو مسترد کرتے ہوئے اسے 'فاصلے پر بھوتیا اثر' (Spooky action at a distance) کیوں کہا تھا؟",
        ["کیونکہ ایک ذرے کو ناپنے سے نوری سال دور موجود دوسرا ذرہ پلک جھپکتے ہی اپنی حالت بدل لیتا ہے، جو بظاہر روشنی کی رفتار کی حد کے خلاف لگتا تھا", "انہوں نے ثابت کیا کہ اس سے توانائی ضائع ہوتی ہے", "الجھاؤ سے لامحدود حرارت پیدا ہوتی ہے", "یہ کشش ثقل کی لہروں سے ہوتا ہے"],
        "کیونکہ ایک ذرے کو ناپنے سے نوری سال دور موجود دوسرا ذرہ پلک جھپکتے ہی اپنی حالت بدل لیتا ہے، جو بظاہر روشنی کی رفتار کی حد کے خلاف لگتا تھا",
        "آئن اسٹائن کا ماننا تھا کہ کوئی بھی اثر روشنی سے تیز سفر نہیں کر سکتا۔ مگر تجربات نے ثابت کیا کہ الجھے ہوئے ذرات کائنات کے دو کونوں پر بھی ایک دوسرے سے فوری طور پر جڑے رہتے ہیں۔"
    ),
    (
        "Why does Werner Heisenberg's Uncertainty Principle dictate that you can never simultaneously know both the exact position and exact momentum of a subatomic particle?",
        ["Position and momentum are Fourier-transform conjugate variables governed by non-commuting quantum operators (Delta x * Delta p >= h-bar / 2)", "Microscopes are not yet built sharp enough", "Light heat pushes the particle away", "Subatomic particles destroy measuring tools"],
        "Position and momentum are Fourier-transform conjugate variables governed by non-commuting quantum operators (Delta x * Delta p >= h-bar / 2)",
        "The uncertainty principle is not a limitation of measuring instruments, but an intrinsic wave property of matter: a localized wave packet contains a broad spectrum of wavelengths.",
        "ہائزن برگ کا غیر یقینی کا اصول (Uncertainty Principle) یہ کیوں کہتا ہے کہ کسی ایٹمی ذرے کی درست پوزیشن اور رفتار کو بیک وقت ناپنا ناممکن ہے؟",
        ["پوزیشن اور رفتار مادے کی لہر کے کونیاتی متضاد اوصاف ہیں جو ریاضیاتی طور پر ایک ساتھ واضح نہیں ہو سکتے (Delta x * Delta p >= h/4pi)", "خوردبینیں ابھی تک اتنی تیز نہیں بنیں", "روشنی کی گرمی ذرے کو اڑا دیتی ہے", "ایٹمی ذرات آلات کو توڑ دیتے ہیں"],
        "پوزیشن اور رفتار مادے کی لہر کے کونیاتی متضاد اوصاف ہیں جو ریاضیاتی طور پر ایک ساتھ واضح نہیں ہو سکتے (Delta x * Delta p >= h/4pi)",
        "یہ پیمائش کے آلے کی کمزوری نہیں بلکہ کائنات کا فطری اصول ہے۔ ذرے کو ایک مقام پر قید کرنے سے اس کی لہر پھیل جاتی ہے جس سے اس کی رفتار نامعلوم ہو جاتی ہے۔"
    ),
    (
        "How do modern computer flash memory drives and solid-state drives (SSDs) store electrical data across completely impenetrable insulating oxide barriers?",
        ["Electrons pass through the barrier via quantum mechanical tunneling despite having insufficient classical energy to overcome the potential hill", "High voltage melts microscopic holes through the oxide", "The insulator conducts electricity under heat", "Static magnetic fields pull the electrons"],
        "Electrons pass through the barrier via quantum mechanical tunneling despite having insufficient classical energy to overcome the potential hill",
        "Fowler-Nordheim tunneling allows wave-like electron probability distributions to penetrate thin (~10 nm) silicon dioxide dielectric barriers.",
        "کمپیوٹر کی ایس ایس ڈی (SSD) اور فلیش ڈرائیوز بجلی کے ناقابل تسخیر انسولیٹر کے آر پار ڈیٹا کیسے محفوظ کرتی ہیں؟",
        ["الیکٹران کوانٹم ٹنلنگ (Quantum tunneling) کے ذریعے رکاوٹ کو توڑے بغیر بھوت کی طرح دیوار کے آر پار گزر جاتے ہیں", "زیادہ وولٹیج انسولیٹر میں سوراخ کر دیتی ہے", "گرمی سے انسولیٹر موصل بن جاتا ہے", "مقناطیسی فیلڈ الیکٹرانز کو کھینچتی ہے"],
        "الیکٹران کوانٹم ٹنلنگ (Quantum tunneling) کے ذریعے رکاوٹ کو توڑے بغیر بھوت کی طرح دیوار کے آر پار گزر جاتے ہیں",
        "کلاسیکی فزکس میں دیوار پھلانگنے کے لیے طاقت چاہیے، مگر کوانٹم فزکس میں الیکٹران کی لہر کا کچھ حصہ دیوار کے دوسری طرف نمودار ہو جاتا ہے، جس سے ڈیٹا چارج ہو جاتا ہے۔"
    ),
    (
        "Why do two uncharged, highly polished metallic mirror plates placed nanometers apart in a total vacuum attract each other with a measurable physical force (Casimir effect)?",
        ["Fewer virtual quantum vacuum fluctuations can fit between the narrow plates than in the surrounding space, creating an inward net radiation pressure", "Residual magnetic fields in polished metal", "Static electricity attracts mirror coatings", "Gravity is amplified between close mirrors"],
        "Fewer virtual quantum vacuum fluctuations can fit between the narrow plates than in the surrounding space, creating an inward net radiation pressure",
        "The Casimir effect proves vacuum is not empty; boundary conditions restrict zero-point electromagnetic modes between plates, generating inward net force F ~ 1/d^4.",
        "مکمل خلا (Vacuum) میں بغیر کسی برقی چارج کے دو بالکل ہموار دھاتی پلیٹیں ایک دوسرے کے انتہائی قریب رکھی جائیں تو وہ خود بخود آپس میں کیوں جڑ جاتی ہیں (Casimir effect)؟",
        ["پلیٹوں کے درمیان تنگ جگہ میں خلا کے کوانٹم بلبلے (Virtual particles) کم سما پاتے ہیں جبکہ باہر کا دباؤ انہیں اندر دھکیلتا ہے", "دھات کا بچا کچا مقناطیس کھینچتا ہے", "ساکن بجلی شیشے کو ملاتی ہے", "قریب آنے سے کشش ثقل لاکھوں گنا بڑھ جاتی ہے"],
        "پلیٹوں کے درمیان تنگ جگہ میں خلا کے کوانٹم بلبلے (Virtual particles) کم سما پاتے ہیں جبکہ باہر کا دباؤ انہیں اندر دھکیلتا ہے",
        "کاسمیر اثر ثابت کرتا ہے کہ خلا خالی نہیں ہے۔ وہاں ہر لمحے ورچوئل ذرات جنم لیتے ہیں اور مرتے ہیں۔ پلیٹوں کے باہر زیادہ ذرات ہونے سے اندر کی طرف دباؤ پڑتا ہے۔"
    ),
    (
        "Why did Stephen Hawking predict that black holes are not completely black, but slowly lose mass and eventually evaporate away over cosmic time (Hawking radiation)?",
        ["Virtual particle-antiparticle pairs near the event horizon are separated, with one falling in and the other escaping as real thermal radiation", "Black holes eject nuclear matter through jets", "Photons tunnel out of the singularity", "Solar wind blows black hole matter away"],
        "Virtual particle-antiparticle pairs near the event horizon are separated, with one falling in and the other escaping as real thermal radiation",
        "Quantum field theory in curved spacetime dictates that horizon separation of entangled vacuum pairs imparts negative energy into the hole, radiating positive energy outward.",
        "اسٹیفن ہاکنگ نے یہ انقلابی پیشین گوئی کیوں کی تھی کہ بلیک ہول مکمل سیاہ نہیں ہیں بلکہ آہستہ آہستہ تابکاری خارج کر کے وقت کے ساتھ غائب ہو جاتے ہیں (Hawking radiation)؟",
        ["بلیک ہول کے کنارے (Event horizon) پر بننے والے ورچوئل ذرات میں سے ایک اندر گر جاتا ہے اور دوسرا کائنات میں حرارتی تابکاری بن کر فرار ہو جاتا ہے", "بلیک ہول اپنے مادے کو فوارے کی طرح پھینکتا ہے", "روشنی مرکز سے سرنگ بنا کر نکلتی ہے", "شمسی ہوا بلیک ہول کا مادہ اڑا دیتی ہے"],
        "بلیک ہول کے کنارے (Event horizon) پر بننے والے ورچوئل ذرات میں سے ایک اندر گر جاتا ہے اور دوسرا کائنات میں حرارتی تابکاری بن کر فرار ہو جاتا ہے",
        "خلا میں ذرات کے جوڑے بنتے رہتے ہیں۔ بلیک ہول کے دہانے پر منفی توانائی کا ذرہ اندر گر کر بلیک ہول کا وزن گھٹاتا ہے جبکہ مثبت ذرہ باہر نکل کر روشنی بن جاتا ہے۔"
    ),
    (
        "What bizarre physical transformation would happen to a human astronaut falling feet-first toward a stellar-mass black hole (spaghettification)?",
        ["Extreme gravitational tidal forces would stretch the astronaut vertically into a long thin strand while compressing them horizontally", "They would freeze into a solid statue", "They would bounce off the event horizon", "They would instantly disintegrate into light"],
        "Extreme gravitational tidal forces would stretch the astronaut vertically into a long thin strand while compressing them horizontally",
        "Tidal gradient d F/d r ~ 1/r^3. Gravitational pull on the feet is astronomically higher than on the head, stretching the body along the radial axis.",
        "اگر کوئی خلا باز پیروں کے بل کسی چھوٹے بلیک ہول میں گرنے لگے تو کشش ثقل اس کے جسم کے ساتھ کیا خوفناک سلوک کرے گی (Spaghettification)؟",
        ["کشش ثقل کے شدید ٹائیڈل دباؤ کی وجہ سے انسان کا جسم عمودی طور پر نوڈل کی طرح لمبا کھنچ جائے گا اور پہلو سے باریک دب جائے گا", "وہ فورا جم کر مجسمہ بن جائے گا", "وہ دہانے سے ٹکرا کر واپس اچھل جائے گا", "وہ ایک سیکنڈ میں روشنی بن جائے گا"],
        "کشش ثقل کے شدید ٹائیڈل دباؤ کی وجہ سے انسان کا جسم عمودی طور پر نوڈل کی طرح لمبا کھنچ جائے گا اور پہلو سے باریک دب جائے گا",
        "بلیک ہول کے قریب چند فٹ کے فاصلے پر کشش میں لاکھوں گنا فرق آ جاتا ہے۔ پاؤں پر لگنے والا کھنچاؤ سر سے کہیں زیادہ ہونے کی وجہ سے جسم سپگیٹی کی طرح کھنچ کر تار بن جاتا ہے۔"
    ),
    (
        "Why does a massive galaxy cluster act as a giant cosmic magnifying glass, bending and magnifying the light of distant galaxies behind it (gravitational lensing)?",
        ["Mass curves the geometry of spacetime itself, forcing light photons to travel along curved geodesic trajectories", "Galaxies contain giant glass lenses", "Interstellar dust reflects light inward", "Dark matter emits focusing laser beams"],
        "Mass curves the geometry of spacetime itself, forcing light photons to travel along curved geodesic trajectories",
        "General Relativity states gravity is spacetime curvature (G_uv = 8*pi*T_uv). Light follows null geodesics bent around massive mass concentrations.",
        "دیوہیکل کہکشائیں اپنے پیچھے چھپی ہوئی دور دراز کہکشاؤں کی روشنی کو موڑ کر ایک دیوہیکل عدسے (Gravitational lens) کی طرح بڑا کر کے کیسے دکھاتی ہیں؟",
        ["کہکشاں کی زبردست کمیت اسپیس ٹائم (Spacetime) کے تانے بانے کو موڑ دیتی ہے جس سے سیدھی روشنی بھی کمان کی طرح مڑ کر فوکس ہو جاتی ہے", "کہکشاؤں میں شیشے کے عدسے تیرتے ہیں", "کہکشانی دھول روشنی کو اندر موڑتی ہے", "ڈارک میٹر لیزر بیم چھوڑتا ہے"],
        "کہکشاں کی زبردست کمیت اسپیس ٹائم (Spacetime) کے تانے بانے کو موڑ دیتی ہے جس سے سیدھی روشنی بھی کمان کی طرح مڑ کر فوکس ہو جاتی ہے",
        "آئن اسٹائن کے مطابق کشش کوئی جادوئی ڈوری نہیں بلکہ خلا کا جھکاؤ ہے۔ جب روشنی کسی بھاری کہکشاں کے پاس سے گزرتی ہے تو مڑے ہوئے خلا میں مڑ کر ایک عدسے کا کام کرتی ہے۔"
    ),
    (
        "Why is the night sky dark rather than blazing as bright as the surface of the Sun, even though there are trillions of stars in every direction (Olbers' Paradox)?",
        ["The universe has a finite age (13.8 billion years) and is expanding, redshifting light and limiting the observable horizon", "Interstellar dust blocks 100 percent of starlight", "Stars only shine during daylight hours", "Dark matter absorbs all distant light"],
        "The universe has a finite age (13.8 billion years) and is expanding, redshifting light and limiting the observable horizon",
        "If the universe were static, infinitely old, and infinite, every line of sight would terminate on a star. Finite age and cosmological redshift resolve the paradox.",
        "اگر کائنات میں ہر سمت کھربوں ستارے موجود ہیں تو رات کا آسمان سورج کی طرح دہکنے کی بجائے کالا سیاہ کیوں نظر آتا ہے (Olbers' Paradox)؟",
        ["کائنات کی عمر محدود ہے (13.8 ارب سال) اور وہ پھیل رہی ہے، جس سے دور کے ستاروں کی روشنی ابھی ہم تک نہیں پہنچی اور پھیل کر مدہم ہو چکی ہے", "خلا کی دھول ساری روشنی روک لیتی ہے", "ستارے صرف دن میں جلتے ہیں", "ڈارک میٹر ساری روشنی نگل لیتا ہے"],
        "کائنات کی عمر محدود ہے (13.8 ارب سال) اور وہ پھیل رہی ہے، جس سے دور کے ستاروں کی روشنی ابھی ہم تک نہیں پہنچی اور پھیل کر مدہم ہو چکی ہے",
        "اولبرز کے پیراڈاکس کا حل یہ ہے کہ کائنات ازلی نہیں ہے۔ بہت دور کے ستاروں کی روشنی کو پہنچنے میں ابھی اربوں سال درکار ہیں، اور کائنات کے پھیلاؤ نے پرانی روشنی کو انفراریڈ بنا دیا ہے۔"
    ),
    (
        "Physicist Enrico Fermi famously asked: 'If intelligent alien life is mathematically probable across billions of stars, where is everybody?' What is this dilemma called?",
        ["The Fermi Paradox", "The Drake Dilemma", "The Hubble Horizon", "The Anthropic Trap"],
        "The Fermi Paradox",
        "The Fermi Paradox highlights the apparent contradiction between high probabilistic estimates of extraterrestrial civilizations and the complete absence of empirical evidence.",
        "ماہر طبیعیات اینریکو فرمی نے پوچھا تھا: 'اگر اربوں ستاروں میں ذہین خلائی مخلوق کا ہونا ریاضیاتی طور پر یقینی ہے، تو پھر وہ سب کہاں ہیں اور کوئی رابطہ کیوں نہیں ہوا؟' اس معمہ کو کیا کہتے ہیں؟",
        ["فرمی کا معمہ (Fermi Paradox)", "ڈریک کا مخمصہ", "ہبل کا ہورائزن", "انسانی تعصب کا ٹریپ"],
        "فرمی کا معمہ (Fermi Paradox)",
        "فرمی پیراڈاکس اس تضاد کو کہتے ہیں کہ کائنات میں اربوں ایسے سیارے ہیں جہاں زندگی پنپ سکتی تھی، مگر ہمارے پاس اب تک کسی ایک بھی خلائی تہذیب کا کوئی ثبوت نہیں ملا۔"
    ),
    (
        "Why do distant galaxies appear to be moving away from Earth with redshifted light in all directions, without Earth being the center of the universe?",
        ["Space itself is expanding uniformly everywhere like raisins in an expanding loaf of rising bread", "Earth repels other galaxies gravitationally", "Our galaxy is moving at light speed", "Galaxies are falling into black holes"],
        "Space itself is expanding uniformly everywhere like raisins in an expanding loaf of rising bread",
        "Cosmological metric expansion stretches space itself between non-gravitationally bound objects; every observer sees all distant galaxies receding from their vantage point.",
        "دور کی تمام کہکشائیں زمین سے ہر سمت میں دور بھاگتی ہوئی کیوں دکھائی دیتی ہیں، حالانکہ زمین کائنات کا مرکز نہیں ہے؟",
        ["کائنات کی فضا خود ہر جگہ یکساں طور پر پھیل رہی ہے جیسے پھولتے ہوئے کیک میں کشمش کے دانے ایک دوسرے سے دور ہوتے ہیں", "زمین کہکشاؤں کو مقناطیس کی طرح دھکیلتی ہے", "ہماری کہکشاں روشنی کی رفتار سے بھاگ رہی ہے", "کہکشائیں بلیک ہول میں گر رہی ہیں"],
        "کائنات کی فضا خود ہر جگہ یکساں طور پر پھیل رہی ہے جیسے پھولتے ہوئے کیک میں کشمش کے دانے ایک دوسرے سے دور ہوتے ہیں",
        "کہکشائیں خلا میں نہیں دوڑ رہیں بلکہ خود خلا کا فاصلہ پھیل رہا ہے۔ کسی بھی کہکشاں پر کھڑے ہو کر دیکھا جائے تو ہر دوسری دور کی کہکشاں دور جاتی نظر آئے گی۔"
    ),
    (
        "Why do the stars in the outer arms of spiral galaxies rotate at virtually identical high velocities as stars near the galaxy core, violating Keplerian orbital mechanics?",
        ["Galaxies are enveloped in massive spherical halos of invisible Dark Matter providing extra gravitational binding", "Black holes at the center spin the arms mechanically", "Galactic friction pulls stars together", "Stars are tethered by magnetic ropes"],
        "Galaxies are enveloped in massive spherical halos of invisible Dark Matter providing extra gravitational binding",
        "Flat galaxy rotation curves (Vera Rubin discovery) show orbital speed does not fall off with radius (v != 1/sqrt(r)), demonstrating massive non-luminous dark matter halos.",
        "گھومتی ہوئی کہکشاؤں کے بیرونی کناروں کے ستارے مرکز کے ستاروں جتنی ہی تیز رفتاری سے کیوں گھومتے ہیں، جو کیپلر کے قوانین کے خلاف ہے؟",
        ["کہکشائیں ایک نادیدہ 'ڈارک میٹر' (Dark Matter) کے وزنی ہالے میں لپٹی ہوئی ہیں جو اضافی کشش ثقل فراہم کرتا ہے", "مرکز کا بلیک ہول ستاروں کو لاٹھی کی طرح گھماتا ہے", "کہکشانی رگڑ ستاروں کو کھینچتی ہے", "ستارے مقناطیسی رسیوں سے بندھے ہیں"],
        "کہکشائیں ایک نادیدہ 'ڈارک میٹر' (Dark Matter) کے وزنی ہالے میں لپٹی ہوئی ہیں جو اضافی کشش ثقل فراہم کرتا ہے",
        "اگر صرف نظر آنے والا مادہ ہوتا تو بیرونی ستاروں کو سست ہونا چاہیے تھا۔ ویرا روبن نے دریافت کیا کہ بیرونی ستارے اتنے تیز گھومتے ہیں کہ انہیں بکھرنے سے صرف ایک چھپا ہوا وزنی ڈارک میٹر ہی روکے ہوئے ہے۔"
    ),
    (
        "Why does the exact same face of the Moon always point toward Earth, leaving the far side permanently hidden from terrestrial observers?",
        ["Gravitational tidal friction dissipated rotational energy until the Moon's spin period synchronized with its orbital period (tidal locking)", "The far side is too heavy to turn", "Earth's magnetic pole pins the Moon", "The Moon does not rotate on its axis at all"],
        "Gravitational tidal friction dissipated rotational energy until the Moon's spin period synchronized with its orbital period (tidal locking)",
        "Earth's tidal bulges exerted gravitational torque on the Moon over billions of years, slowing its rotation until its orbital period equaled its axial spin (1:1 resonance).",
        "چاند کا ہمیشہ ایک ہی رخ زمین کی طرف کیوں رہتا ہے جبکہ اس کی پچھلی سائیڈ زمین سے کبھی دکھائی نہیں دیتی؟",
        ["زمین کی کشش ثقل کے ٹائیڈل رگڑ نے چاند کے گھومنے کی رفتار کو سست کر کے اس کے مدار کے برابر کر دیا ہے (Tidal locking)", "چاند کا پچھلا حصہ وزنی ہے جو مڑ نہیں سکتا", "زمین کا مقناطیس چاند کو پکڑ کر رکھتا ہے", "چاند اپنے محور پر بالکل نہیں گھومتا"],
        "زمین کی کشش ثقل کے ٹائیڈل رگڑ نے چاند کے گھومنے کی رفتار کو سست کر کے اس کے مدار کے برابر کر دیا ہے (Tidal locking)",
        "چاند اپنے محور پر اتنے ہی دنوں (27.3 دن) میں ایک چکر پورا کرتا ہے جتنے دنوں میں وہ زمین کے گرد گھومتا ہے۔ اس کامل ہم آہنگی کی وجہ سے زمین سے ہمیشہ ایک ہی رخ نظر آتا ہے۔"
    ),
    (
        "Why are space telescopes like the James Webb Space Telescope positioned at Lagrange Point L2 (1.5 million km from Earth) rather than in low Earth orbit?",
        ["Gravitational forces of Earth and Sun balance centripetal force, allowing the spacecraft to maintain a stable sun-shielded orbit in permanent cold darkness", "L2 has zero gravitational pull from any planet", "Radio signals travel instantly from L2", "L2 is protected by Earth's atmosphere"],
        "Gravitational forces of Earth and Sun balance centripetal force, allowing the spacecraft to maintain a stable sun-shielded orbit in permanent cold darkness",
        "At L2, solar and terrestrial gravity combine to match orbital angular velocity, keeping the telescope permanently in Earth's shadow to maintain deep cryogenic infrared cooling.",
        "جیمز ویب خلائی دوربین (JWST) کو زمین کے قریب رکھنے کی بجائے 15 لاکھ کلومیٹر دور لاگرانج پوائنٹ (L2) پر کیوں بھیجا گیا؟",
        ["وہاں سورج اور زمین کی مشترکہ کشش ثقل دوربین کو ایک ساکن اور شدید ٹھنڈے مقام پر رکھتی ہے جہاں سورج کی تپش سے بچاؤ ممکن ہے", "L2 پر کسی بھی سیارے کی کشش ثقل نہیں ہوتی", "L2 سے ریڈیو سگنل ایک سیکنڈ میں پہنچتے ہیں", "L2 زمین کی فضا کے اندر واقع ہے"],
        "وہاں سورج اور زمین کی مشترکہ کشش ثقل دوربین کو ایک ساکن اور شدید ٹھنڈے مقام پر رکھتی ہے جہاں سورج کی تپش سے بچاؤ ممکن ہے",
        "انفراریڈ دوربین کو کام کرنے کے لیے منفی 233 ڈگری ٹھنڈ چاہیے ہوتی ہے۔ L2 پوائنٹ پر زمین اور سورج ایک ہی طرف رہتے ہیں، جس سے ایک ہی شیلڈ سے دھوپ روک کر مستقل تاریکی مل جاتی ہے۔"
    ),
    (
        "Why does a comet's bright dust and ion tail always point directly away from the Sun, even when the comet is traveling away from the Sun back toward deep space?",
        ["Radiation pressure from sunlight and the continuous solar wind blow dust and ionized gas radially outward away from the solar core", "Gravity pulls the tail backward", "Comets leave rocket exhaust behind them", "Friction with space vacuum pushes the tail"],
        "Radiation pressure from sunlight and the continuous solar wind blow dust and ionized gas radially outward away from the solar core",
        "Solar photon momentum (radiation pressure) and high-speed solar wind protons push microscopic volatiles radially outward, regardless of comet velocity vector.",
        "دُم دار ستارے (Comet) کی چمکدار دم ہمیشہ سورج سے الٹی سمت میں باہر کی طرف کیوں ہوتی ہے، چاہے وہ سورج سے دور ہی کیوں نہ جا رہا ہو؟",
        ["سورج کی تیز شعاعوں کا دباؤ (Radiation pressure) اور شمسی ہوائیں گیس اور دھول کو زبردستی سورج سے دور دھکیلتی ہیں", "کشش ثقل دم کو پیچھے کھینچتی ہے", "دُم دار ستارے راکٹ کا دھواں چھوڑتے ہیں", "خلا کی رگڑ دم کو پیچھے کرتی ہے"],
        "سورج کی تیز شعاعوں کا دباؤ (Radiation pressure) اور شمسی ہوائیں گیس اور دھول کو زبردستی سورج سے دور دھکیلتی ہیں",
        "دُم دار ستارے کی دم گاڑی کے دھوئیں کی طرح پیچھے نہیں چھٹتی، بلکہ سورج سے نکلنے والی تابکاری کی آندھی اسے ہر وقت سورج کے مخالف رخ اڑائے رکھتی ہے۔"
    ),
    (
        "What prevents a super-dense white dwarf star from collapsing completely into a black hole under its own crushing gravitational weight?",
        ["Electron degeneracy pressure caused by the Pauli Exclusion Principle forbidding identical fermions from sharing quantum states", "Nuclear fusion explosions in the core", "Intense magnetic repulsion of iron atoms", "Solar wind blowing from surrounding space"],
        "Electron degeneracy pressure caused by the Pauli Exclusion Principle forbidding identical fermions from sharing quantum states",
        "Quantum mechanics dictates electrons cannot occupy identical phase space cells; compressing them generates immense non-thermal degeneracy pressure up to the 1.4 solar mass limit.",
        "سفید بونے ستارے (White Dwarf) کو اس کی اپنی دیوہیکل کشش ثقل کے نیچے دب کر بلیک ہول بننے سے کون سی طاقت روکے رکھتی ہے؟",
        ["الیکٹرانز کا انحطاطی دباؤ (Electron degeneracy pressure) جو پاؤلی کے اصول کے تحت الیکٹرانز کو ایک ہی کوانٹم حالت میں دبنے سے روکتا ہے", "مرکز میں ایٹمی فیوژن کے دھماکے", "لوہے کے ایٹموں کی مقناطیسی کشش", "خلا سے آنے والی شمسی ہوائیں"],
        "الیکٹرانز کا انحطاطی دباؤ (Electron degeneracy pressure) جو پاؤلی کے اصول کے تحت الیکٹرانز کو ایک ہی کوانٹم حالت میں دبنے سے روکتا ہے",
        "جب ستارے کا ایندھن ختم ہو جاتا ہے تو کوانٹم فزکس کا پاؤلی کا اصول کام آتا ہے۔ الیکٹرانز ایک دوسرے میں گھسنے سے انکار کر کے اتنی زبردست کوانٹم طاقت پیدا کرتے ہیں جو ستارے کو سہارا دیتی ہے۔"
    ),
    (
        "Why does an induction cooktop heat an iron skillet to frying temperatures in seconds, while the glass surface beneath remains cool enough to touch safely?",
        ["High-frequency alternating magnetic fields induce circulating eddy currents and magnetic hysteresis losses directly inside the ferrous pan", "The cooktop emits microwaves into iron", "The glass conducts heat away to ground", "Iron creates chemical fire reactions"],
        "High-frequency alternating magnetic fields induce circulating eddy currents and magnetic hysteresis losses directly inside the ferrous pan",
        "A copper coil generates high-frequency magnetic flux (24 kHz); electromagnetic induction produces intense Joule heating (I^2 * R) strictly inside ferromagnetic cookware.",
        "انڈکشن چولہا (Induction stove) لوہے کے فرائنگ پین کو سیکنڈوں میں دہکا دیتا ہے مگر چولہے کی شیشے کی سطح ہاتھ لگانے پر محفوظ اور ٹھنڈی کیوں رہتی ہے؟",
        ["چولہے کی مقناطیسی لہریں صرف لوہے کے برتن کے اندر بھنور نما برقی رو (Eddy currents) پیدا کر کے اسے خود بخود گرم کرتی ہیں", "چولہا لوہے میں مائیکرو ویو پھینکتا ہے", "شیشہ ساری حرارت زمین میں اتار دیتا ہے", "لوہا کیمیائی آگ بھڑکاتا ہے"],
        "چولہے کی مقناطیسی لہریں صرف لوہے کے برتن کے اندر بھنور نما برقی رو (Eddy currents) پیدا کر کے اسے خود بخود گرم کرتی ہیں",
        "چولہے کے اندر شعلہ یا ہیٹر نہیں ہوتا۔ تانبے کا کوائل تیز مقناطیسی لہریں چھوڑتا ہے جو صرف لوہے کے مالیکیولز کو ہلا کر برتن کو خود ہیٹر بنا دیتی ہیں، شیشے پر کوئی اثر نہیں ہوتا۔"
    ),
    (
        "Why can a bird fly safely past a glass skyscraper without issues, but frequently crashes violently into clean reflective exterior glass windows?",
        ["Reflective glass mirrors the sky and surrounding foliage, creating an illusory continuous flight corridor indistinguishable to avian eyes", "Birds are colorblind to glass reflections", "Glass emits acoustic frequencies that disorient birds", "Birds fly with closed eyes"],
        "Reflective glass mirrors the sky and surrounding foliage, creating an illusory continuous flight corridor indistinguishable to avian eyes",
        "Birds perceive mirrored outdoor vegetation and open sky reflections as real physical airspace, lacking cognitive cues to recognize transparent planar barriers.",
        "پرندے آسمان پر آزادانہ اڑتے ہیں مگر شیشے کے فلک بوس ٹاورز کی کھڑکیوں سے پوری رفتار سے ٹکرا کر ہلاک کیوں ہو جاتے ہیں؟",
        ["شیشہ آسمان اور سامنے کے درختوں کا ہو بہو عکس دکھاتا ہے جسے پرندہ کھلی فضا اور راستہ سمجھ کر اندر گھسنے کی کوشش کرتا ہے", "پرندوں کو شیشہ کالا نظر آتا ہے", "شیشہ آواز خارج کر کے پرندوں کو پاگل کرتا ہے", "پرندے آنکھیں بند کر کے اڑتے ہیں"],
        "شیشہ آسمان اور سامنے کے درختوں کا ہو بہو عکس دکھاتا ہے جسے پرندہ کھلی فضا اور راستہ سمجھ کر اندر گھسنے کی کوشش کرتا ہے",
        "پرندوں کا بصری نظام شیشے کی رکاوٹ کو نہیں سمجھ سکتا۔ شیشے میں چمکتا ہوا نیلا آسمان اور بادل انہیں کھلا راستہ لگتے ہیں جس کی وجہ سے وہ رک نہیں پاتے۔"
    ),
    (
        "Why does an entire society attempting to save more money during an economic recession paradoxically cause total national savings and income to collapse (the Paradox of Thrift)?",
        ["Increased saving reduces aggregate consumer demand, which slashes business revenues and lowers total national income and savings", "Banks confiscate surplus savings during recessions", "Paper currency dissolves in bank vaults", "Recessions convert savings into inflation"],
        "Increased saving reduces aggregate consumer demand, which slashes business revenues and lowers total national income and savings",
        "John Maynard Keynes proved that while saving is prudent for an individual, collective belt-tightening reduces aggregate consumption, driving down economic output and total realized savings.",
        "کفایت شعاری کا معمہ (The Paradox of Thrift): معاشی بحران کے دوران اگر تمام شہری ایک ساتھ زیادہ پیسے بچانا شروع کر دیں تو ملک کی مجموعی بچت اور معیشت الٹی برباد کیوں ہو جاتی ہے؟",
        ["بچت بڑھانے سے مارکیٹ میں خریداری کم ہو جاتی ہے جس سے کاروبار تباہ ہوتے ہیں اور لوگوں کی آمدنیاں گر کر مجموعی بچت کو گرا دیتی ہیں", "بینک بحران میں بچت ضبط کر لیتے ہیں", "والٹس میں نوٹ گل جاتے ہیں", "بحران بچت کو مہنگائی بنا دیتا ہے"],
        "بچت بڑھانے سے مارکیٹ میں خریداری کم ہو جاتی ہے جس سے کاروبار تباہ ہوتے ہیں اور لوگوں کی آمدنیاں گر کر مجموعی بچت کو گرا دیتی ہیں",
        "انفرادی طور پر بچت اچھی چیز ہے، مگر جب سب بچت کرنے لگیں تو کوئی دکان پر نہیں جاتا۔ فیکٹریاں بند ہوتی ہیں، ملازمین بے روزگار ہوتے ہیں اور بالآخر کسی کے پاس بچانے کے لیے پیسے ہی نہیں بچتے۔"
    ),
    (
        "Why can collective majority voting result in circular, non-transitive outcomes where Candidate A beats B, B beats C, yet C beats A (the Condorcet Paradox)?",
        ["Individual transitive preferences do not necessarily aggregate into a rational, transitive collective group preference under majority rule", "Voters secretly switch ballots", "Election machines round fractions", "Candidates bribe voters cyclically"],
        "Individual transitive preferences do not necessarily aggregate into a rational, transitive collective group preference under majority rule",
        "The Marquis de Condorcet proved in 1785 that even when every voter has consistent rational preferences, pairwise majority voting can cycle endlessly (rock-paper-scissors), lacking a stable winner.",
        "کونڈورسیٹ کا انتخابی معمہ (The Condorcet Paradox): اکثریتی ووٹنگ میں ایسا چکر کیوں بن سکتا ہے جہاں امیدوار A امیدوار B کو ہرائے، B امیدوار C کو ہرائے، مگر C امیدوار A کو ہرا دے؟",
        ["انفرادی رائے اگرچہ منطقی ہو مگر جب انہیں اکثریتی اصول پر جوڑا جائے تو اجتماعی فیصلہ غیر منطقی اور دائرے دار چکر میں پھنس سکتا ہے", "ووٹرز خفیہ طور پر پرچی بدلتے ہیں", "ووٹنگ مشینیں اعشاریہ کاٹتی ہیں", "امیدوار رشوت دیتے ہیں"],
        "انفرادی رائے اگرچہ منطقی ہو مگر جب انہیں اکثریتی اصول پر جوڑا جائے تو اجتماعی فیصلہ غیر منطقی اور دائرے دار چکر میں پھنس سکتا ہے",
        "اگر تین ووٹرز کے گروپس کی ترجیحات مختلف ہوں، تو دو دو کے مقابلے میں ہر امیدوار کسی نہ کسی سے جیتتا ہے اور کسی نہ کسی سے ہارتا ہے۔ اس چکر میں اکثریت کا کوئی ایک حتمی فاتح نہیں بن پاتا۔"
    ),
    (
        "What does the Gibbard-Satterthwaite Theorem prove about any deterministic voting system with three or more distinct candidates?",
        ["Every non-dictatorial voting rule is susceptible to strategic tactical voting, where voters gain an advantage by misrepresenting their true preferences", "All elections require two rounds", "Paper ballots prevent strategic voting", "Dictators always win fair elections"],
        "Every non-dictatorial voting rule is susceptible to strategic tactical voting, where voters gain an advantage by misrepresenting their true preferences",
        "The theorem proves that unless an election is a dictatorship, there is always at least one situation where a voter can achieve a preferred outcome by insincerely ranking a lesser-favored candidate higher.",
        "گبارڈ سیٹرتھویٹ تھیورم (Gibbard-Satterthwaite Theorem): تین یا اس سے زیادہ امیدواروں والے کسی بھی جمہوری ووٹنگ نظام کے بارے میں یہ قانون کیا سچ بتاتا ہے؟",
        ["آمریت کے سوا دنیا کا ہر انتخابی نظام حکمت عملی پر مبنی ووٹنگ کے خطرے سے دوچار ہے جہاں لوگ اپنے پسندیدہ امیدوار کو چھوڑ کر چالاکی سے ووٹ دیتے ہیں", "تمام انتخابات میں دو مرحلے درکار ہوتے ہیں", "کاغذی پرچی چالاکی کو روکتی ہے", "آمر ہمیشہ جیت جاتا ہے"],
        "آمریت کے سوا دنیا کا ہر انتخابی نظام حکمت عملی پر مبنی ووٹنگ کے خطرے سے دوچار ہے جہاں لوگ اپنے پسندیدہ امیدوار کو چھوڑ کر چالاکی سے ووٹ دیتے ہیں",
        "اگر کوئی نظام ایک آمر کے ہاتھ میں نہ ہو تو ووٹر ہمیشہ اپنے سچے دل کے پسندیدہ امیدوار کو ووٹ دینے کی بجائے اس امیدوار کو ووٹ دینے پر مجبور ہوتا ہے جو کم برا ہو تاکہ بدترین کو روکا جا سکے۔"
    ),
    (
        "In a mechanical spring network arranged in a diamond, why does physically CUTTING a taut central string connecting two springs cause a suspended heavy weight to RISE rather than fall (Braess's Spring Paradox)?",
        ["Cutting the central string shifts the springs from a soft series configuration into a much stiffer parallel configuration", "The string cuts air resistance", "Scissors impart upward kinetic energy", "The spring loses gravitational mass"],
        "Cutting the central string shifts the springs from a soft series configuration into a much stiffer parallel configuration",
        "This is the mechanical analogue of Braess's paradox. The string connects the network in series (stretching heavily). Severing the link forces both spring branches into parallel tension, doubling stiffness and lifting the load.",
        "اسپرنگ کا مکینیکل معمہ (Braess's Spring Paradox): تاروں اور اسپرنگ کے جال میں سے جب ایک تنے ہوئے دھاگے کو قینچی سے کاٹا جائے تو نیچے لٹکا ہوا وزنی باٹ گرنے کی بجائے اوپر کیوں اٹھ جاتا ہے؟",
        ["درمیانی دھاگہ کٹنے سے اسپرنگ کمزور سیریز نظام سے نکل کر ایک مضبوط متوازی (Parallel) تناؤ میں آ جاتے ہیں جس سے کھچاؤ دگنا ہو کر وزن کو اوپر کھینچ لیتا ہے", "دھاگہ ہوا کی رگڑ کاٹ دیتا ہے", "قینچی اوپر کی طاقت منتقل کرتی ہے", "اسپرنگ کا وزن کم ہو جاتا ہے"],
        "درمیانی دھاگہ کٹنے سے اسپرنگ کمزور سیریز نظام سے نکل کر ایک مضبوط متوازی (Parallel) تناؤ میں آ جاتے ہیں جس سے کھچاؤ دگنا ہو کر وزن کو اوپر کھینچ لیتا ہے",
        "دیکھنے والے کو لگتا ہے کہ دھاگہ کاٹنے پر وزن نیچے گرے گا۔ مگر دھاگہ اسپرنگز کو لمبا کھینچ رہا تھا، اس کے کٹتے ہی دونوں اسپرنگ مل کر متوازی کام کرنے لگتے ہیں جس سے وہ سمٹ کر باٹ کو اوپر اٹھا لیتے ہیں۔"
    ),
    (
        "Why do two competing ice cream vendors on a long 1-kilometer beach invariably end up setting up their carts right next to each other at the exact center (Hotelling's Law)?",
        ["Nash equilibrium of spatial competition: moving toward the center maximizes each vendor's market share against the competitor's territory", "The center of the beach has cold sand", "Local zoning laws require central permits", "Customers only swim at the midpoint"],
        "Nash equilibrium of spatial competition: moving toward the center maximizes each vendor's market share against the competitor's territory",
        "Harold Hotelling showed that firms minimize product or spatial differentiation. If Vendor A sets up at 25%, Vendor B sets up at 26% to capture 74% of the beach, pulling both to the central 50% Nash equilibrium.",
        "ہوٹلنگ کا قانون اور دکانداروں کا گٹھ جوڑ (Hotelling's Law): ایک میل لمبے ساحل پر دو حریف آئس کریم والے دور دور رہنے کی بجائے بالکل آمنے سامنے ساحل کے عین بیچ میں کیوں بیٹھ جاتے ہیں؟",
        ["مارکیٹ کی مسابقت کا نیش توازن: بیچ میں آ کر بیٹھنے سے ہر دکاندار زیادہ سے زیادہ گاہکوں کے علاقے پر قبضہ کر لیتا ہے تاکہ دوسرے کا شیئر کم ہو", "بیچ میں ریت ٹھنڈی ہوتی ہے", "قانون صرف بیچ میں بیٹھنے کی اجازت دیتا ہے", "گاہک صرف بیچ میں نہاتے ہیں"],
        "مارکیٹ کی مسابقت کا نیش توازن: بیچ میں آ کر بیٹھنے سے ہر دکاندار زیادہ سے زیادہ گاہکوں کے علاقے پر قبضہ کر لیتا ہے تاکہ دوسرے کا شیئر کم ہو",
        "گاہکوں کے لیے بہتر تھا کہ وہ ایک چوتھائی اور تین چوتھائی پر بیٹھتے تاکہ سب کو نزدیک پڑے۔ مگر ذاتی مقابلے کے چکر میں دونوں ایک دوسرے کا علاقہ گھیرتے گھیرتے عین مرکز میں چپک کر بیٹھ جاتے ہیں۔"
    )
]

print(f"Tricky P1 Chunk 1 loaded: {len(ITEMS)} items.")
