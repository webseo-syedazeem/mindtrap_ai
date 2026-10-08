# -*- coding: utf-8 -*-
"""
Tricky Part 1 Chunk 2 (60 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why does an acoustic sound illusion called the 'Shepard Tone' sound like a musical scale that is continuously ascending in pitch forever without ever getting higher?",
        ["A continuous loop of overlapping octave tones where high frequencies fade out while low frequencies fade in seamlessly", "Human ears run out of bass frequencies", "The speaker plays supersonic frequencies", "The acoustic scale uses zero decibels"],
        "A continuous loop of overlapping octave tones where high frequencies fade out while low frequencies fade in seamlessly",
        "A Shepard scale consists of sinusoids separated by octaves shaped by a fixed bell-shaped spectral envelope, creating an acoustic auditory barberpole illusion.",
        "شیپرڈ ٹون (Shepard Tone) نامی صوتی دھوکہ سننے والے کو مسلسل اونچی اور باریک ہوتی ہوئی آواز کیوں لگتا ہے جو کبھی ختم نہیں ہوتی؟",
        ["آکٹوز پر مبنی لہروں کا ایسا سرکلر لوپ جس میں اونچے سر مدہم ہو کر غائب ہوتے ہیں جبکہ نچلے سر بیک وقت ابھرتے رہتے ہیں", "انسانی کان باریک آوازیں سننا بند کر دیتے ہیں", "سپیکر سے غیر معمولی لہریں نکلتی ہیں", "اس کی آواز صفر ڈیسیبل پر ہوتی ہے"],
        "آکٹوز پر مبنی لہروں کا ایسا سرکلر لوپ جس میں اونچے سر مدہم ہو کر غائب ہوتے ہیں جبکہ نچلے سر بیک وقت ابھرتے رہتے ہیں",
        "یہ ایک آڈیو نائی کی گھومتی پٹی کی طرح ہے۔ جب ایک اونچا سر غائب ہو رہا ہوتا ہے تو نچلا سر اتنا ہی ابھر کر اوپر آ جاتا ہے، جس سے دماغ کو لگتا ہے کہ آواز لامتناہی طور پر اوپر ہی جا رہی ہے۔"
    ),
    (
        "Why does a person standing in an Ames Room appear as a giant in one corner and shrink to a miniature dwarf in the opposite corner?",
        ["The room is built as an asymmetrical trapezoid with a sloping floor and ceiling, while viewing through a peephole forces false rectangular perspective", "The room uses magnifying mirrors", "The corner contains dense air", "Gravity compresses people in the corner"],
        "The room is built as an asymmetrical trapezoid with a sloping floor and ceiling, while viewing through a peephole forces false rectangular perspective",
        "The Ames room is distorted in depth and height; monocular peephole viewing removes binocular parallax, forcing the brain's rectangular room prior to distort perceived actor size.",
        "ایمز روم (Ames Room) کے ایک کونے میں کھڑا انسان دیوہیکل اور دوسرے کونے میں کھڑا انسان بونا کیوں دکھائی دیتا ہے؟",
        ["کمرے کی دیواریں، فرش اور چھت ترچھی اور غیر متناسب بنائی جاتی ہیں جبکہ سوراخ سے دیکھنے پر دماغ اسے عام چوکور کمرہ سمجھتا ہے", "کمرے میں بڑے عدسے لگے ہوتے ہیں", "کونے کی ہوا وزنی ہوتی ہے", "کشش ثقل انسان کو دبا دیتی ہے"],
        "کمرے کی دیواریں، فرش اور چھت ترچھی اور غیر متناسب بنائی جاتی ہیں جبکہ سوراخ سے دیکھنے پر دماغ اسے عام چوکور کمرہ سمجھتا ہے",
        "ایک سوراخ سے دیکھنے پر آنکھ کو ترچھے زاویے سیدھے لگتے ہیں۔ اصل میں بونا نظر آنے والا انسان دیو سے دگنا فاصلے پر پیچھے کھڑا ہوتا ہے، جس سے دماغ کے سائز کا اندازہ دھوکہ کھا جاتا ہے۔"
    ),
    (
        "In Edward Adelson's Checker Shadow Illusion, why do squares A and B have identical photometric luminance, yet human observers perceive square A as dark grey and square B as nearly white?",
        ["The brain automatically corrects for cast shadows and local checkerboard contrast, discounting illumination to preserve perceived object reflectance", "The camera was calibrated incorrectly", "Square B emits internal light", "The eye's cornea darkens square A"],
        "The brain automatically corrects for cast shadows and local checkerboard contrast, discounting illumination to preserve perceived object reflectance",
        "Lightness constancy mechanisms subtract the perceived green cylinder shadow and compare square B against its darker neighbors, forcing high perceived reflectance.",
        "ایڈلسن کے چیکر شیڈو وہم (Checker Shadow Illusion) میں چوکور خانہ A اور B دونوں بالکل ایک جیسا گرے رنگ رکھنے کے باوجود B سفید اور A کالا کیوں لگتا ہے؟",
        ["انسانی دماغ سائے کے اثر اور ارد گرد کے رنگوں کے تضاد کو خود بخود منہا کر کے اصلی رنگ کا غلط اندازہ لگاتا ہے", "کیمرے کی لائٹ خراب تھی", "خانہ B سے روشنی نکلتی ہے", "آنکھ کی پتلی خانے A کو کالا کرتی ہے"],
        "انسانی دماغ سائے کے اثر اور ارد گرد کے رنگوں کے تضاد کو خود بخود منہا کر کے اصلی رنگ کا غلط اندازہ لگاتا ہے",
        "انسانی بصارت روشنی کی اصل مقدار نہیں ناپتی بلکہ سائے کو ذہن میں رکھ کر چیز کے اصلی رنگ کو سمجھنے کی کوشش کرتی ہے۔ سلنڈر کا سایہ دماغ کو یقین دلاتا ہے کہ B سفید خانہ ہے۔"
    ),
    (
        "In the McGurk Effect, watching a video of someone whose lips mouth 'ga-ga' while the audio track plays 'ba-ba' causes human listeners to hear an entirely new syllable: 'da-da'. Why?",
        ["The brain fuses conflicting auditory and visual speech streams into a single best-fit multisensory phonological percept", "Human ears malfunction under video light", "The mouth movements mute sound", "The audio frequency inverts"],
        "The brain fuses conflicting auditory and visual speech streams into a single best-fit multisensory phonological percept",
        "Speech perception is multimodal; the superior temporal sulcus integrates visual lip kinematics with acoustic cues, synthesizing an intermediate phonetic compromise ('da').",
        "میک گرک اثر (McGurk Effect) میں جب ویڈیو میں ہونٹ 'گا-گا' بولتے نظر آئیں اور سپیکر سے 'با-با' کی آواز آئے، تو انسان کو ایک نیا لفظ 'ڈا-ڈا' کیوں سنائی دیتا ہے؟",
        ["انسانی دماغ متضاد بصری اور صوتی سگنلز کو ملا کر ایک درمیانی متفقہ نیا لفظ بنا دیتا ہے", "ویڈیو دیکھ کر کان خراب ہو جاتے ہیں", "ہونٹوں کی حرکت آواز کو دبا دیتی ہے", "آواز کی فریکوئنسی الٹ جاتی ہے"],
        "انسانی دماغ متضاد بصری اور صوتی سگنلز کو ملا کر ایک درمیانی متفقہ نیا لفظ بنا دیتا ہے",
        "بولنے کی سمجھ صرف کانوں سے نہیں بلکہ آنکھوں سے بھی ہوتی ہے۔ جب کان کچھ اور اور آنکھیں کچھ اور دیکھیں تو دماغ الجھ کر دونوں کا درمیانی حل نکال لیتا ہے۔"
    ),
    (
        "In the Hermann Grid Illusion, why do faint dark grey ghost spots appear at the white line intersections, but vanish completely when you look directly at them?",
        ["Lateral inhibition of ganglion cells in the peripheral retina creates localized contrast reduction at four-way intersections", "The brain lacks peripheral memory", "White lines reflect blue light", "Foveal vision is colorblind"],
        "Lateral inhibition of ganglion cells in the peripheral retina creates localized contrast reduction at four-way intersections",
        "Peripheral receptive fields have concentric on-center/off-surround structures. Intersections have more white surround lighting, generating more inhibition and darker perceived spots.",
        "ہرمن گرڈ وہم (Hermann Grid) میں کالے چوکوروں کے درمیان سفید لکیروں کے چوراہوں پر ہلکے سرمئی نقطے کیوں چمکتے ہیں جو سیدھا دیکھنے پر غائب ہو جاتے ہیں؟",
        ["آنکھ کے پردے کے خلیات کا باہمی سگنل دبانے کا عمل (Lateral inhibition) کناروں پر روشنی کے زیادہ ہونے کی وجہ سے چوراہوں کو مدہم کر دیتا ہے", "دماغ کے پاس میموری ختم ہو جاتی ہے", "سفید لکیریں نیلی روشنی پلٹاتی ہیں", "سامنے کی نظر اندھی ہوتی ہے"],
        "آنکھ کے پردے کے خلیات کا باہمی سگنل دبانے کا عمل (Lateral inhibition) کناروں پر روشنی کے زیادہ ہونے کی وجہ سے چوراہوں کو مدہم کر دیتا ہے",
        "آنکھ کے سائیڈ کے خلیات کے ارد گرد جب زیادہ سفید روشنی پڑتی ہے تو وہ دماغ کو کم روشنی کا سگنل بھیجتے ہیں۔ جب سیدھا دیکھا جائے تو مرکزی باریک نظر اس وہم کو ختم کر دیتی ہے۔"
    ),
    (
        "Why does staring fixedly at a small red dot surrounded by a blurry blue circle cause the blue circle to vanish completely after 20 seconds (Troxler's Fading)?",
        ["Invariable, unmoving stimuli on peripheral retinal receptive fields undergo neural adaptation, fading into background perceptual fill-in", "The blue pigment dissolves in retinal fluid", "The eye stops receiving photons", "Red light paralyzes optic rods"],
        "Invariable, unmoving stimuli on peripheral retinal receptive fields undergo neural adaptation, fading into background perceptual fill-in",
        "Photoreceptors adapt to unvarying local stimuli; micro-saccades normally refresh boundaries, but soft gradients lack edges, causing complete neural habituation.",
        "ٹروکسلر کے اثر (Troxler's Fading) میں جب انسان کسی باریک نقطے کو ٹکٹکی باندھ کر دیکھتا رہے تو ارد گرد کا دھندلا نیلا دائرہ چند سیکنڈ بعد بالکل غائب کیوں ہو جاتا ہے؟",
        ["آنکھ کے ساکن خلیات غیر متحرک منظر کے عادی ہو کر سگنل بھیجنا بند کر دیتے ہیں اور دماغ اس جگہ کو پس منظر سے بھر دیتا ہے", "آنکھ کے اندر نیلا رنگ گھل جاتا ہے", "آنکھ میں روشنی جانا رک جاتی ہے", "سرخ رنگ اعصاب کو سن کر دیتا ہے"],
        "آنکھ کے ساکن خلیات غیر متحرک منظر کے عادی ہو کر سگنل بھیجنا بند کر دیتے ہیں اور دماغ اس جگہ کو پس منظر سے بھر دیتا ہے",
        "ہماری آنکھیں صرف تبدیلی کو دیکھتی ہیں۔ جب آنکھ بالکل ساکن رہے اور منظر میں کوئی حرکت نہ ہو تو بصری خلیات تھک کر خاموش ہو جاتے ہیں اور چیز نگاہوں سے اوجھل ہو جاتی ہے۔"
    ),
    (
        "Why does looking quickly at an analog clock's sweeping second hand give you the distinct impression that the second hand stayed frozen for much longer than one second (Chronostasis)?",
        ["Saccadic masking suppresses visual input during eye movement, and the brain back-dates the post-saccadic image to fill the temporal gap", "Clocks pause when observed", "The optic nerve stops light transmission", "The retina expands during eye shifts"],
        "Saccadic masking suppresses visual input during eye movement, and the brain back-dates the post-saccadic image to fill the temporal gap",
        "During rapid eye movements (saccades), the brain suppresses blurred vision; it retroactively projects the first clear target image backward in subjective time.",
        "دیوار گھڑی کی طرف اچانک نگاہ ڈالنے پر ایسا کیوں لگتا ہے کہ سیکنڈ والی سوئی ایک سیکنڈ سے کہیں زیادہ دیر تک ایک ہی جگہ پر جمی (Frozen) رہی (Chronostasis)؟",
        ["آنکھ گھومنے کے دوران دماغ دھندلا پن روکنے کے لیے بصارت وقتی طور پر منسوخ کر دیتا ہے اور نئے منظر کو وقت میں پیچھے کھینچ کر خلا بھرتا ہے", "دیکھنے پر گھڑی کی سوئی سست ہو جاتی ہے", "بصری عصب روشنی روک لیتا ہے", "آنکھ کا پردہ حرکت میں پھیل جاتا ہے"],
        "آنکھ گھومنے کے دوران دماغ دھندلا پن روکنے کے لیے بصارت وقتی طور پر منسوخ کر دیتا ہے اور نئے منظر کو وقت میں پیچھے کھینچ کر خلا بھرتا ہے",
        "آنکھ کو ایک جگہ سے دوسری جگہ مڑنے میں چند ملی سیکنڈ لگتے ہیں۔ موشن بلر سے بچنے کے لیے دماغ اس وقفے کو چھپا دیتا ہے اور نئی تصویر کو پچھلے وقت پر چسپاں کر کے لمبا کر دیتا ہے۔"
    ),
    (
        "Why does a droplet of molten glass dropped into cold water (a Prince Rupert's Drop) survive heavy hammer blows on its bulb, but explodes into powder when its hair-thin tail is clipped?",
        ["Extremely high compressive surface stresses encase an intensely tensioned core; breaking the tail releases a crack wave propagating at 1.5 km/s", "The bulb is made of solid titanium", "The tail contains poisonous explosive acid", "Cold water fills the inside of the glass"],
        "Extremely high compressive surface stresses encase an intensely tensioned core; breaking the tail releases a crack wave propagating at 1.5 km/s",
        "Rapid exterior quenching locks outer glass in gigapascal compression while the molten interior shrinks in extreme tensile stress; tail rupture unleashes explosive crack release.",
        "پرنس روپرٹ کا قطرہ (Prince Rupert's Drop) ہتھوڑے کی چوٹوں کو برداشت کر لیتا ہے مگر اس کی بال جیسی باریک دم کو ہلکا سا توڑتے ہی پورا قطرہ دھماکے سے باریک دھول کیوں بن جاتا ہے؟",
        ["باہر کی سطح شدید بیرونی دباؤ میں اور اندرونی حصہ زبردست کھنچاؤ میں قید ہوتا ہے، دم ٹوٹتے ہی شاک ویو پورے قطرے کو ریزہ ریزہ کر دیتی ہے", "اس کا سر ٹھوس ٹائٹینیم کا ہوتا ہے", "دم کے اندر بارود بھرا ہوتا ہے", "ٹھنڈا پانی شیشے کے اندر قید ہوتا ہے"],
        "باہر کی سطح شدید بیرونی دباؤ میں اور اندرونی حصہ زبردست کھنچاؤ میں قید ہوتا ہے، دم ٹوٹتے ہی شاک ویو پورے قطرے کو ریزہ ریزہ کر دیتی ہے",
        "پانی میں گرنے پر شیشے کی بیرونی سطح فوری جم جاتی ہے جبکہ اندر کا مائع سکڑتے ہوئے زبردست تناؤ پیدا کرتا ہے۔ دم ٹوٹتے ہی یہ قید توانائی آواز سے تیز رفتار شاک ویو بن کر پھٹ جاتی ہے۔"
    ),
    (
        "Why does a bent wire made of Nitinol (nickel-titanium alloy) spring back into its exact original complicated geometric shape when dipped into hot water?",
        ["A reversible thermoelastic martensite-to-austenite crystalline phase transition restores original atomic lattice arrangement", "The metal melts and resolidifies", "Hot water magnetizes the nickel", "Water surface tension straightens the wire"],
        "A reversible thermoelastic martensite-to-austenite crystalline phase transition restores original atomic lattice arrangement",
        "Nitinol undergoes a solid-state diffusionless twin boundary rearrangement: low-temperature twinned martensite shifts to high-symmetry parent austenite above transition temperature.",
        "نائٹینول (Nitinol) دھات سے بنی مڑی تڑی تار کو گرم پانی میں ڈالتے ہی وہ پلک جھپکتے ہی اپنی اصلی پیچیدہ شکل میں واپس کیسے آ جاتی ہے (Shape memory)؟",
        ["حرارت دھات کے اندرونی ایٹمی ڈھانچے کو مارٹن سائٹ سے آسٹینائٹ فیز میں بدل کر اس کی اصل بناوٹ بحال کر دیتی ہے", "دھات پگھل کر دوبارہ جم جاتی ہے", "گرم پانی نکل کو مقناطیس بنا دیتا ہے", "پانی کا سطحی تناؤ تار کو سیدھا کرتا ہے"],
        "حرارت دھات کے اندرونی ایٹمی ڈھانچے کو مارٹن سائٹ سے آسٹینائٹ فیز میں بدل کر اس کی اصل بناوٹ بحال کر دیتی ہے",
        "یہ ایک شیپ میموری الائے ہے۔ ٹھنڈی حالت میں اس کے ایٹمی جوڑ بغیر ٹوٹے مڑ جاتے ہیں، مگر گرم ہوتے ہی ایٹم اپنی پرانی اصل پوزیشن پر چھلانگ لگا کر شکل واپس لے لیتے ہیں۔"
    ),
    (
        "How can a gecko lizard run upside down across a polished, non-porous glass ceiling without using any wet glue, suction cups, or claws?",
        ["Millions of microscopic keratin spatulae on its toe pads generate cumulative intermolecular van der Waals forces with the glass", "Its toes create electrostatic high voltage", "Microscopic barbs dig into glass atoms", "Sweat glands secrete natural adhesive resin"],
        "Millions of microscopic keratin spatulae on its toe pads generate cumulative intermolecular van der Waals forces with the glass",
        "Setae branch into hundreds of nanometer-scale spatulae; intimate conformal contact brings billions of molecules within nanometers of glass, producing huge dry adhesion.",
        "چھپکلی شیشے کی ہموار اور چکنی چھت پر کسی گوند، سکشن کپ یا پنجوں کے بغیر الٹی کیسے دوڑ لیتی ہے؟",
        ["اس کے پنجوں کے بالوں کے باریک ریشے (Spatulae) شیشے کے ایٹموں کے ساتھ ونڈر والز قوتیں (van der Waals forces) بنا کر چپک جاتے ہیں", "اس کے پاؤں سے ہائی وولٹیج کرنٹ نکلتا ہے", "وہ شیشے کے ایٹموں میں کانٹے گاڑتی ہے", "وہ پیروں سے گوند خارج کرتی ہے"],
        "اس کے پنجوں کے بالوں کے باریک ریشے (Spatulae) شیشے کے ایٹموں کے ساتھ ونڈر والز قوتیں (van der Waals forces) بنا کر چپک جاتے ہیں",
        "چھپکلی کے پیروں پر لاکھوں نینو بال ہوتے ہیں جو اتنے باریک ہیں کہ شیشے کے مالیکیولز کے اتنے قریب پہنچ جاتے ہیں جہاں کائنات کی قدرتی ایٹمی کشش (van der Waals) خود بخود کام کرتی ہے۔"
    ),
    (
        "Why does water roll off a lotus flower leaf in perfect spherical beads, carrying away dirt and remaining completely spotless (the Lotus Effect)?",
        ["Microscopic epidermal papillae covered in hydrophobic epicuticular wax crystals minimize contact area, creating a contact angle over 150°", "Lotus leaves emit heat that boils water", "The leaf is coated in petroleum oil", "Water molecules dissolve leaf minerals"],
        "Microscopic epidermal papillae covered in hydrophobic epicuticular wax crystals minimize contact area, creating a contact angle over 150°",
        "Superhydrophobic Cassie-Baxter state: water droplets sit atop microscopic air pockets trapped between wax papillae, rolling off effortlessly and gathering particulates.",
        "کنول کے پھول کے پتے پر پانی گرتے ہی موتی کی طرح گول کیوں بن جاتا ہے اور ذرا سا ہلانے پر کیچڑ کو اپنے ساتھ بہا کر پتے کو بالکل خشک کیوں چھوڑ دیتا ہے؟",
        ["پتے کی سطح پر موم کے باریک ابھار ہوا کو قید رکھتے ہیں جس سے پانی کے قطرے کا پتے سے رابطہ کم سے کم رہتا ہے (Superhydrophobicity)", "پتا گرمی خارج کر کے پانی ابالتا ہے", "پتے پر تیل کی تہہ لگی ہوتی ہے", "پانی پتے کے معدنیات کو گھولتا ہے"],
        "پتے کی سطح پر موم کے باریک ابھار ہوا کو قید رکھتے ہیں جس سے پانی کے قطرے کا پتے سے رابطہ کم سے کم رہتا ہے (Superhydrophobicity)",
        "کنول کے پتے پر مائکروسکوپک ستون ہوتے ہیں جن پر موم کے دانے ہوتے ہیں۔ پانی ان ستونوں کے درمیان پھنسی ہوا کے اوپر بیٹھتا ہے جس سے وہ پھیل نہیں سکتا اور رول ہو کر گر جاتا ہے۔"
    ),
    (
        "Why is Aerogel (frozen smoke)—consisting of over 99 percent empty air—capable of shielding human skin from the direct flame of a blowtorch without getting hot?",
        ["Its highly tortuous silica nanopore network suppresses thermal conduction, while pore diameters (20 nm) are smaller than air's mean free path (Knudsen effect)", "Aerogel is made of solid ice", "The blowtorch reflects off aerogel", "Air inside aerogel turns into liquid helium"],
        "Its highly tortuous silica nanopore network suppresses thermal conduction, while pore diameters (20 nm) are smaller than air's mean free path (Knudsen effect)",
        "The Knudsen effect: gas molecules in 20-nm pores collide with pore walls rather than each other, completely choking conductive and convective gas heat transfer.",
        "ایروجل (Aerogel) جو کہ 99 فیصد خالی ہوا پر مشتمل ہوتا ہے، اس کے اوپر رکھی انگلی کو نیچے دہکتے ہوئے شعلے کی آگ سے بھی گرمی کیوں نہیں پہنچتی؟",
        ["اس کے نینو سوراخ اتنے باریک ہوتے ہیں کہ ہوا کے مالیکیولز ایک دوسرے سے ٹکرائے بغیر حرارت آگے منتقل نہیں کر سکتے (Knudsen effect)", "ایروجل ٹھوس برف سے بنتا ہے", "شعلہ ایروجل سے ٹکرا کر واپس پلٹ جاتا ہے", "اندر کی ہوا مائع ہیلیئم بن جاتی ہے"],
        "اس کے نینو سوراخ اتنے باریک ہوتے ہیں کہ ہوا کے مالیکیولز ایک دوسرے سے ٹکرائے بغیر حرارت آگے منتقل نہیں کر سکتے (Knudsen effect)",
        "ایروجل کے اندر باریک خلا ہوا کے مالیکیولز کے حرکت کے راستے سے بھی چھوٹا ہوتا ہے۔ ہوا کے ایٹم آپس میں ٹکرا نہیں پاتے جس سے گرمی کا سفر مکمل طور پر رک جاتا ہے۔"
    ),
    (
        "Why does adding a new high-speed highway to an already congested city road network frequently make average commuter travel times longer for everyone (Braess's Paradox)?",
        ["Selfish routing choices toward the new road reach a non-optimal Nash equilibrium that clogs surrounding choke points", "The new road lowers speed limits", "More cars are manufactured immediately", "GPS satellites malfunction"],
        "Selfish routing choices toward the new road reach a non-optimal Nash equilibrium that clogs surrounding choke points",
        "When each driver independently chooses their shortest route without coordination, the resulting Nash equilibrium yields a higher total network latency than before.",
        "شہر کی ٹریفک کی بھیڑ کم کرنے کے لیے جب ایک نئی چوڑی سڑک کھولی جاتی ہے تو اکثر تمام شہریوں کا سفر پہلے سے بھی زیادہ سست اور لمبا کیوں ہو جاتا ہے (Braess's Paradox)؟",
        ["ہر ڈرائیور اپنے ذاتی فائدے کے لیے نئی سڑک کا رخ کرتا ہے جس سے ایک نیا بدترین توازن (Nash equilibrium) بن کر سنگم جام ہو جاتے ہیں", "نئی سڑک پر رفتار کی حد کم کر دی جاتی ہے", "فوری طور پر لاکھوں نئی گاڑیاں بن جاتی ہیں", "جی پی ایس سگنل خراب ہو جاتے ہیں"],
        "ہر ڈرائیور اپنے ذاتی فائدے کے لیے نئی سڑک کا رخ کرتا ہے جس سے ایک نیا بدترین توازن (Nash equilibrium) بن کر سنگم جام ہو جاتے ہیں",
        "بریس کا پیراڈاکس بتاتا ہے کہ بغیر کوآرڈینیشن کے ہر گاڑی شارٹ کٹ سمجھ کر ایک ہی راستے پر ٹوٹ پڑتی ہے جس سے مرکزی راستے چوک ہو جاتے ہیں اور مجموعی وقت بڑھ جاتا ہے۔"
    ),
    (
        "Why does improving energy efficiency (such as building more fuel-efficient car engines) historically lead to higher overall national consumption of oil rather than less (Jevons Paradox)?",
        ["Increased efficiency lowers the effective cost of the service, driving exponential increases in demand and overall usage", "Fuel-efficient engines burn oil dirtier", "Car owners forget to turn off engines", "Oil companies dilute gasoline"],
        "Increased efficiency lowers the effective cost of the service, driving exponential increases in demand and overall usage",
        "W.S. Jevons noted that steam engine efficiency lowered coal costs, spurring widespread industrial adoption and multiplying aggregate coal burn.",
        "جیونز کا معمہ (Jevons Paradox) بتاتا ہے کہ ایندھن بچانے والی کفایت شعار گاڑیاں بنانے سے ملک میں پیٹرول کی مجموعی کھپت کم ہونے کی بجائے بڑھ کیوں جاتی ہے؟",
        ["کفایت شعاری سے سفر کا خرچ سستا ہو جاتا ہے جس سے لوگ گاڑیوں کا استعمال اور سفر بے تحاشا بڑھا دیتے ہیں", "کفایت شعار انجن پیٹرول گندا جلاتے ہیں", "ڈرائیور انجن بند کرنا بھول جاتے ہیں", "تیل کی کمپنیاں پیٹرول پتلا کر دیتی ہیں"],
        "کفایت شعاری سے سفر کا خرچ سستا ہو جاتا ہے جس سے لوگ گاڑیوں کا استعمال اور سفر بے تحاشا بڑھا دیتے ہیں",
        "جب کسی چیز کو کفایت شعار بنایا جائے تو اس کی فی یونٹ لاگت گر جاتی ہے جس سے معاشرے میں اس کی مانگ اور کھپت اتنی زیادہ پھیل جاتی ہے کہ کل خرچ پہلے سے بڑھ جاتا ہے۔"
    ),
    (
        "Why did a colonial government offering a cash bounty for every dead cobra brought in by citizens ultimately result in a massive explosion in the wild cobra population (the Cobra Effect)?",
        ["Enterprising citizens began breeding cobras in captivity to harvest bounties; when the program ended, they released them into the wild", "Cobras reproduced to seek revenge", "The bounty attracted snakes from other continents", "Snakes became immune to traps"],
        "Enterprising citizens began breeding cobras in captivity to harvest bounties; when the program ended, they released them into the wild",
        "Perverse incentives create perverse outcomes: bounty economics incentivized snake farming. Abolishing the bounty destroyed the market, prompting mass releases.",
        "کوبرائے اثر (Cobra Effect): حکومت نے زہریلے سانپ مار کر لانے والوں کو نقد انعام دینے کا اعلان کیا، مگر اس کے نتیجے میں شہر میں سانپ کم ہونے کی بجائے بے تحاشا بڑھ کیوں گئے؟",
        ["لالچی لوگوں نے انعام جیتنے کے لیے گھروں میں سانپ پالنے شروع کر دیے، اور انعام بند ہونے پر سب سانپ گلیوں میں چھوڑ دیے", "سانپوں نے بدلہ لینے کے لیے زیادہ انڈے دیے", "انعام نے دوسرے ملکوں سے سانپ بلا لیے", "سانپ زہر سے محفوظ ہو گئے"],
        "لالچی لوگوں نے انعام جیتنے کے لیے گھروں میں سانپ پالنے شروع کر دیے، اور انعام بند ہونے پر سب سانپ گلیوں میں چھوڑ دیے",
        "یہ غلط معاشی ترغیبات کا شاہکار ہے۔ لوگوں نے سانپ مارنے کی بجائے سانپوں کی باقاعدہ فارمنگ شروع کر دی۔ حکومت نے سکیم بند کی تو کسانوں نے فالتو سانپ جنگل میں آزاد کر دیے۔"
    ),
    (
        "Why did an attempt by a celebrity to legally censor and delete an aerial photograph of her coastal mansion result in millions of people downloading and viewing the photo worldwide (the Streisand Effect)?",
        ["Attempting to suppress public information draws intense media curiosity, amplifying viral attention exponentially", "The lawsuit contained the full photo inside court files", "Internet cables inverted data", "The photographer bought all newspapers"],
        "Attempting to suppress public information draws intense media curiosity, amplifying viral attention exponentially",
        "The Streisand effect demonstrates psychological reactance: aggressive censorship attempts transform an obscure record into a global cause celebre.",
        "اسٹرائی سینڈ اثر (Streisand Effect): ایک مشہور اداکارہ نے ساحل پر اپنے عالیشان بنگلے کی فضائی تصویر انٹرنیٹ سے ہٹانے کے لیے مقدمہ کیا، مگر نتیجہ یہ نکلا کہ کروڑوں لوگوں نے وہ تصویر دیکھ لی، کیوں؟",
        ["کسی معلومات کو زبردستی چھپانے کی کوشش عوام اور میڈیا میں شدید تجسس پیدا کر کے اسے وائرل کر دیتی ہے", "مقدمے کی فائل میں تصویر لگی ہوئی تھی", "انٹرنیٹ کے تاروں نے ڈیٹا الٹ دیا", "فوٹوگرافر نے سارے اخبار خرید لیے"],
        "کسی معلومات کو زبردستی چھپانے کی کوشش عوام اور میڈیا میں شدید تجسس پیدا کر کے اسے وائرل کر دیتی ہے",
        "پہلے اس تصویر کو محض چھ لوگوں نے دیکھا تھا، مگر قانونی نوٹس کی خبر آتے ہی دنیا بھر کے لاکھوں صارفین تجسس کے مارے تصویر ڈھونڈنے لگے جس سے وہ انٹرنیٹ کا ٹرینڈ بن گئی۔"
    ),
    (
        "If every wooden plank of the Ship of Theseus is replaced one by one over decades until zero original components remain, is it still the same ship?",
        ["A fundamental metaphysical paradox of identity over time with no single objective empirical answer", "Yes, legally identical", "No, it is a completely new entity", "Only if the captain remains unchanged"],
        "A fundamental metaphysical paradox of identity over time with no single objective empirical answer",
        "The Ship of Theseus addresses mereological essentialism versus spatiotemporal continuity. If parts are gathered to build a second ship, identity becomes contested.",
        "تھیسیئس کی کشتی (Ship of Theseus) کے پرانے تختے ایک ایک کر کے کئی سالوں میں نئے تختوں سے بدل دیے گئے یہاں تک کہ ایک بھی پرانی لکڑی نہ بچی۔ کیا یہ اب بھی وہی پرانی کشتی ہے؟",
        ["یہ فلسفے اور وجودیات (Metaphysics) کا ایک کلاسیکی معمہ ہے جس کا کوئی حتمی سائنسی جواب نہیں ہے", "ہاں، قانونی طور پر وہی ہے", "نہیں، یہ بالکل نئی کشتی ہے", "صرف اگر کپتان پرانا ہو"],
        "یہ فلسفے اور وجودیات (Metaphysics) کا ایک کلاسیکی معمہ ہے جس کا کوئی حتمی سائنسی جواب نہیں ہے",
        "اگر پرانے تمام تختوں کو جمع کر کے دوسری کشتی کھڑی کر دی جائے تو اصلی کشتی کون سی مانی جائے گی؟ یہ سوال وقت کے ساتھ شے کی شناخت اور بقا پر بحث چھیڑتا ہے۔"
    ),
    (
        "If a time traveler travels back into the past and accidentally prevents their biological grandfather from ever meeting their grandmother, how could the traveler have existed to travel back in time?",
        ["A self-contradictory causal loop known as the Grandfather Paradox", "The time traveler turns into a ghost", "The universe rewrites genetic DNA", "The grandmother adopts another person"],
        "A self-contradictory causal loop known as the Grandfather Paradox",
        "Closed timelike curves (CTCs) challenge causal consistency. Novikov's self-consistency principle posits that past probability self-adjusts to prevent contradictions.",
        "دادا کا معمہ (Grandfather Paradox): اگر کوئی شخص وقت میں پیچھے جا کر اپنے دادا اور دادی کی شادی روک دے، تو وہ خود کیسے پیدا ہوا کہ وقت میں پیچھے جا سکے؟",
        ["یہ وقت کے سفر کا ایک لاینحل منطقی تضاد ہے جسے دادا کا پیراڈاکس کہتے ہیں", "وقت کا مسافر بھوت بن جاتا ہے", "کائنات ڈی این اے بدل دیتی ہے", "دادی کسی اور کو گود لے لیتی ہے"],
        "یہ وقت کے سفر کا ایک لاینحل منطقی تضاد ہے جسے دادا کا پیراڈاکس کہتے ہیں",
        "اگر دادا کی شادی نہ ہوئی تو پوتا پیدا نہیں ہو سکتا، اور اگر پوتا پیدا نہ ہوا تو ماضی میں جا کر شادی کون روکے گا؟ یہ تضاد ثابت کرتا ہے کہ ماضی میں جانا منطقی اصولوں سے ٹکراتا ہے۔"
    ),
    (
        "Why is the One-Time Pad (Vernam cipher) mathematically proven to be 100 percent unbreakable even to an adversary with infinite computing power?",
        ["When using a truly random key as long as the plaintext used only once, ciphertext reveals zero Shannon information (perfect secrecy)", "The key is written in quantum ink", "The code destroys computers", "It uses prime numbers larger than the universe"],
        "When using a truly random key as long as the plaintext used only once, ciphertext reveals zero Shannon information (perfect secrecy)",
        "Claude Shannon proved information-theoretic secrecy: H(M | C) = H(M). Because any plaintext of equal length is equally likely, brute-force cracking yields all possible texts.",
        "ون ٹائم پیڈ (One-Time Pad) نامی خفیہ کوڈ کو ریاضیاتی طور پر دنیا کے کسی بھی سپر کمپیوٹر کے لیے توڑنا 100 فیصد ناممکن کیوں مانا جاتا ہے؟",
        ["اگر خفیہ چابی مکمل بے ترتیب ہو، پیغام جتنی لمبی ہو اور صرف ایک بار استعمال ہو تو خفیہ متن ریاضیاتی طور پر صفر معلومات ظاہر کرتا ہے (Perfect Secrecy)", "اس کی چابی کوانٹم سیاہی سے لکھی ہوتی ہے", "یہ کوڈ کمپیوٹر کو جلا دیتا ہے", "اس میں کائنات سے بڑے ہندسے ہوتے ہیں"],
        "اگر خفیہ چابی مکمل بے ترتیب ہو، پیغام جتنی لمبی ہو اور صرف ایک بار استعمال ہو تو خفیہ متن ریاضیاتی طور پر صفر معلومات ظاہر کرتا ہے (Perfect Secrecy)",
        "کلود شینن نے ثابت کیا کہ اس کوڈ کو لاکھوں سال بھی چلایا جائے تو ہر ممکنہ کتاب یا جملہ اس کے جواب میں نکل سکتا ہے۔ ریاضیاتی طور پر یہ جاننا ناممکن ہے کہ اصلی پیغام کون سا تھا۔"
    ),
    (
        "Why can modern public-key cryptography (like RSA-2048) be decoded in seconds with the private key, but takes billions of years to break without it?",
        ["Multiplying two large prime numbers is computationally trivial, but finding those prime factors from their product is an intractable trapdoor problem", "Private keys contain secret quantum codes", "RSA keys destroy unauthorized computers", "Public keys hide the length of the number"],
        "Multiplying two large prime numbers is computationally trivial, but finding those prime factors from their product is an intractable trapdoor problem",
        "RSA relies on the asymmetric computational complexity of integer factorization: O(1) multiplication versus sub-exponential general number field sieve factorization.",
        "آر ایس اے انکرپشن (RSA Cryptography) خفیہ چابی کے ساتھ سیکنڈوں میں کھل جاتی ہے مگر بغیر چابی کے اسے حل کرنے میں اربوں سال کیوں لگتے ہیں؟",
        ["دو بڑے پرائم نمبرز کو ضرب دینا انتہائی آسان ہے مگر ان کے حاصل ضرب سے اصل پرائم نمبرز واپس تلاش کرنا ناممکن حد تک مشکل ہے (Trapdoor function)", "خفیہ چابی میں کوانٹم کوڈ ہوتا ہے", "یہ چابی ہیکر کا کمپیوٹر توڑ دیتی ہے", "عوامی چابی ہندسے کو چھپا لیتی ہے"],
        "دو بڑے پرائم نمبرز کو ضرب دینا انتہائی آسان ہے مگر ان کے حاصل ضرب سے اصل پرائم نمبرز واپس تلاش کرنا ناممکن حد تک مشکل ہے (Trapdoor function)",
        "600 ہندسوں کے دو پرائم نمبرز کو سیکنڈ میں ضرب دی جا سکتی ہے، مگر اسی نمبر کے ٹکڑے (Factors) الگ کرنے کے لیے دنیا کے تمام کمپیوٹرز مل کر بھی کائنات کی عمر جتنا وقت لیں گے۔"
    )
]

print(f"Tricky P1 Chunk 2 loaded: {len(ITEMS)} items.")
