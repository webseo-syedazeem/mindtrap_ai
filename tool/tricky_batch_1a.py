# -*- coding: utf-8 -*-
"""
Tricky batch 1A (60 distinct items).
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
    )
]

print(f"Tricky Batch 1A loaded: {len(ITEMS)} items.")
