# -*- coding: utf-8 -*-
"""
Normal tier remaining items (Part 2: 52 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why does a person swinging on a playground swing gain higher amplitude by pumping their legs at the highest point of each arc?",
        ["Parametric excitation changes the swing's moment of inertia and center of mass at resonant frequency", "Kicking air pushes the swing forward", "Leg muscles generate wind thrust", "Air resistance drops at the peak"],
        "Parametric excitation changes the swing's moment of inertia and center of mass at resonant frequency",
        "Raising the center of mass near peak elevation injects mechanical work into the harmonic oscillator, increasing total energy.",
        "جھولے پر بیٹھا بچہ جھولے کے سب سے اونچے موڑ پر ٹانگیں سمیٹنے اور پھیلانے سے جھولے کو مزید اونچا کیسے کر لیتا ہے؟",
        ["وہ جھولے کے توازن کے مرکز کو بدل کر ارتعاش میں توانائی شامل کرتا ہے (Parametric resonance)", "ٹانگ مار کر ہوا کو پیچھے دھکیلتا ہے", "پٹھوں سے ہوا کا طوفان بنتا ہے", "بلندی پر ہوا کی رکاوٹ کم ہوتی ہے"],
        "وہ جھولے کے توازن کے مرکز کو بدل کر ارتعاش میں توانائی شامل کرتا ہے (Parametric resonance)",
        "اوپر پہنچ کر کشش ثقل کے مرکز کو اوپر اٹھانے سے پٹھوں کی توانائی جھولے کی میکانکی توانائی میں تبدیل ہو کر جھولا اونچا کرتی ہے۔"
    ),
    (
        "Why do tall factory smokestacks occasionally snap and break into two pieces in mid-air before hitting the ground when demolished?",
        ["Bending stresses produced by rotational shear exceed the brittle chimney's tensile strength", "Wind pulls the top off", "Air pressure collapses the hollow brick", "Explosives ignite inside mid-shaft"],
        "Bending stresses produced by rotational shear exceed the brittle chimney's tensile strength",
        "As the base fails, the tall column rotates like a falling lever; angular acceleration produces flexural shear that snaps the stack.",
        "فیکٹری کی اونچی چمنی جب زمین پر گرائی جاتی ہے تو وہ زمین سے ٹکرانے سے پہلے ہی فضا میں دو ٹکڑے کیوں ہو جاتی ہے؟",
        ["گرتے ہوئے گردش کی وجہ سے پیدا ہونے والا اندرونی تناؤ چمنی کو بیچ میں سے موڑ کر توڑ دیتا ہے", "ہوا اوپری حصے کو اڑا لے جاتی ہے", "ہوا کا دباؤ اندرونی خلا کو توڑتا ہے", "بارود درمیان میں پھٹ جاتا ہے"],
        "گرتے ہوئے گردش کی وجہ سے پیدا ہونے والا اندرونی تناؤ چمنی کو بیچ میں سے موڑ کر توڑ دیتا ہے",
        "نیچے سے جھکتے وقت چمنی کے اوپری حصے کی تیز گردش اس پر شدید لچکدار دباؤ ڈالتی ہے جسے اینٹیں برداشت نہیں کر پاتیں۔"
    ),
    (
        "Why does water flowing smoothly out of a kitchen faucet narrow into a thinner stream as it falls downward?",
        ["Gravitational acceleration increases water velocity, requiring a smaller cross-sectional area to conserve volumetric flow rate (A1*v1 = A2*v2)", "Air pressure squeezes the stream together", "Surface tension pulls water inward", "Evaporation shrinks the volume"],
        "Gravitational acceleration increases water velocity, requiring a smaller cross-sectional area to conserve volumetric flow rate (A1*v1 = A2*v2)",
        "The continuity equation for incompressible fluids dictates that as speed increases due to gravity, the cross-sectional area must decrease.",
        "نلکے سے گرتا ہوا پانی جیسے جیسے نیچے جاتا ہے اس کی دھار پتلی کیوں ہوتی جاتی ہے؟",
        ["کشش ثقل سے پانی کی رفتار بڑھتی ہے، اس لیے بہاؤ برابر رکھنے کے لیے دھار کا رقبہ کم ہو جاتا ہے (A1*v1 = A2*v2)", "ہوا کا دباؤ پانی کو دباتا ہے", "سطحی تناؤ اندر کھینچتا ہے", "بخارات بننے سے پانی کم ہوتا ہے"],
        "کشش ثقل سے پانی کی رفتار بڑھتی ہے، اس لیے بہاؤ برابر رکھنے کے لیے دھار کا رقبہ کم ہو جاتا ہے (A1*v1 = A2*v2)",
        "جیسے جیسے پانی گرتا ہے، اس کی گرنے کی رفتار تیز ہوتی جاتی ہے۔ بہاؤ کی مقدار یکساں رکھنے کے لیے دھار کا قطر سکڑ جاتا ہے۔"
    ),
    (
        "Why does a standard boomerang return to the thrower's hands when hurled forward with a spin?",
        ["Gyroscopic precession tilts the curved airfoil blades, causing aerodynamic lift to steer the flight path into a closed horizontal circle", "Wind currents carry it back", "Centrifugal force reverses flight direction", "A boomerang is weighted magnetically"],
        "Gyroscopic precession tilts the curved airfoil blades, causing aerodynamic lift to steer the flight path into a closed horizontal circle",
        "The advancing wing experiences higher relative airspeed and lift than the retreating wing; gyroscopic precession translates this torque into a turn.",
        "بومرانگ (Boomerang) گھما کر پھینکنے پر گول چکر کاٹ کر واپس پھینکنے والے کے پاس کیسے آ جاتا ہے؟",
        ["گھومتے ہوئے پروں کی غیر مساوی لفٹ گائروسکوپک پری سیشن کے ذریعے اس کے راستے کو دائرے میں موڑ دیتی ہے", "ہوا کے جھونکے اسے واپس لاتے ہیں", "مرکز گریز قوت رخ الٹ دیتی ہے", "اس میں مقناطیسی وزن ہوتا ہے"],
        "گھومتے ہوئے پروں کی غیر مساوی لفٹ گائروسکوپک پری سیشن کے ذریعے اس کے راستے کو دائرے میں موڑ دیتی ہے",
        "اوپر کا پر ہوا میں زیادہ تیزی سے آگے بڑھتا ہے جس سے زیادہ لفٹ ملتی ہے۔ اس ناہموار قوت اور گھومنے کے امتزاج سے راستہ دائرہ بن جاتا ہے۔"
    ),
    (
        "Why does a person looking at a straw submerged in a glass of water perceive the straw as bent or broken at the water's surface?",
        ["Light waves change speed and refract at the boundary between two optical media of different refractive indices", "Water magnifies the lower half only", "The glass curves the physical object", "Surface tension distorts the plastic"],
        "Light waves change speed and refract at the boundary between two optical media of different refractive indices",
        "Light travels at roughly 225,000 km/s in water versus 300,000 km/s in air; this velocity differential bends light rays at the interface.",
        "پانی کے گلاس میں ڈالا ہوا اسٹرا (تنکا) پانی کی سطح پر ٹوٹا ہوا یا مڑا ہوا کیوں دکھائی دیتا ہے؟",
        ["روشنی کی کرنیں پانی اور ہوا کے مختلف انعطافی انڈیکس کی وجہ سے سطح پر مڑ جاتی ہیں (Refraction)", "پانی نچلے حصے کو بڑا کر دیتا ہے", "گلاس خود لکڑی کو موڑ دیتا ہے", "سطحی تناؤ پلاسٹک کو ٹیڑھا کرتا ہے"],
        "روشنی کی کرنیں پانی اور ہوا کے مختلف انعطافی انڈیکس کی وجہ سے سطح پر مڑ جاتی ہیں (Refraction)",
        "پانی میں روشنی کی رفتار سست ہوتی ہے بنسبت ہوا کے، اس لیے جب روشنی پانی سے باہر نکلتی ہے تو وہ زاویہ بدل لیتی ہے۔"
    ),
    (
        "Why do dry leaves rustle loudly when crushed underfoot, whereas fresh green leaves crumple silently?",
        ["Dry cell walls are brittle and fracture catastrophically, while turgid cells deform plastically and dissipate energy silently", "Dry leaves contain trapped air chambers", "Green leaves absorb sound waves via chlorophyll", "Dry leaves are lighter in weight"],
        "Dry cell walls are brittle and fracture catastrophically, while turgid cells deform plastically and dissipate energy silently",
        "Moisture loss stiffens cellulose; applied force causes rapid mechanical crack propagation, releasing sudden acoustic energy bursts.",
        "سوکھے پتے پیروں تلے کچلے جانے پر چرچراہٹ کی تیز آواز کیوں پیدا کرتے ہیں جبکہ تازہ ہرے پتے خاموشی سے مڑ جاتے ہیں؟",
        ["سوکھے خلیات کی دیواریں سخت اور خستہ ہو جاتی ہیں جو ٹوٹتے وقت اچانک آواز پیدا کرتی ہیں", "سوکھے پتوں میں ہوا بند ہوتی ہے", "کلوروفیل آواز کو جذب کر لیتا ہے", "سوکھے پتے وزنی نہیں ہوتے"],
        "سوکھے خلیات کی دیواریں سخت اور خستہ ہو جاتی ہیں جو ٹوٹتے وقت اچانک آواز پیدا کرتی ہیں",
        "تازہ پتوں میں پانی خلیات کو لچکدار رکھتا ہے، جبکہ سوکھنے سے سیلولوز شیشے کی طرح کڑک ہو کر فوراً چٹخ جاتا ہے۔"
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
        "Why does the handle of an all-metal cooking spoon submerged in hot boiling soup become painfully hot to the touch?",
        ["Metals possess high thermal conductivity via free valence electrons transferring kinetic energy rapidly along the lattice", "Hot soup splashes up the handle", "Steam clings to metal surfaces", "Boiling broth creates chemical reactions"],
        "Metals possess high thermal conductivity via free valence electrons transferring kinetic energy rapidly along the lattice",
        "Delocalized conduction electrons in metallic bonds carry thermal vibrational energy along the spoon far faster than insulators.",
        "ابلتے ہوئے سالن میں رکھے لوہے کے چمچے کا دستہ بھی پکڑنے پر ہاتھ جلا دینے کی حد تک گرم کیوں ہو جاتا ہے؟",
        ["دھاتوں کے آزاد الیکٹرانز حرارتی توانائی کو تیزی سے دستے کے آخری سرے تک منتقل کر دیتے ہیں (Conduction)", "گرم سالن دستے پر اچھلتا ہے", "بھاپ دھات کو چپک جاتی ہے", "سالن میں کیمیائی حرارت ہوتی ہے"],
        "دھاتوں کے آزاد الیکٹرانز حرارتی توانائی کو تیزی سے دستے کے آخری سرے تک منتقل کر دیتے ہیں (Conduction)",
        "دھات میں الیکٹرانز آزاد گھومتے ہیں، وہ گرم سرے سے حرارت لے کر ٹھنڈے سرے کی طرف سیکنڈوں میں دوڑتے ہیں۔"
    ),
    (
        "Why does a submerged piece of cork immediately shoot straight upward when released at the bottom of a deep swimming pool?",
        ["Cork density is much lower than water, creating a net upward buoyant force exceeding the downward gravitational force", "Water at the bottom is under suction", "Compressed air pockets in cork expand", "Pool floor repels plant material"],
        "Cork density is much lower than water, creating a net upward buoyant force exceeding the downward gravitational force",
        "Buoyant force equals the weight of displaced water. Because displaced water weighs far more than the cork, upward acceleration occurs.",
        "پانی کی گہرائی میں ڈبویا ہوا کارک (Cork) چھوڑتے ہی تیر کی طرح سیدھا اوپر کیوں بھاگتا ہے؟",
        ["کارک کی کثافت پانی سے بہت کم ہوتی ہے جس سے اچھال کی قوت کشش ثقل سے کہیں زیادہ ہو جاتی ہے", "تہہ کا پانی اوپر کی طرف کھینچتا ہے", "کارک کے اندر کی ہوا پھیلتی ہے", "تالاب کا فرش لکڑی کو دھکیلتا ہے"],
        "کارک کی کثافت پانی سے بہت کم ہوتی ہے جس سے اچھال کی قوت کشش ثقل سے کہیں زیادہ ہو جاتی ہے",
        "کارک جتنا پانی ہٹاتا ہے اس پانی کا وزن کارک کے اپنے وزن سے کئی گنا زیادہ ہوتا ہے، جو زبردست اچھال دیتا ہے۔"
    ),
    (
        "Why do desert camels have broad, wide, flat foot pads instead of sharp narrow hooves like mountain goats?",
        ["A large contact surface area distributes body weight, drastically reducing ground pressure and preventing sinking into soft sand", "Flat feet absorb desert heat faster", "To scoop sand while walking", "Camels walk on water during flash floods"],
        "A large contact surface area distributes body weight, drastically reducing ground pressure and preventing sinking into soft sand",
        "Pressure equals Force divided by Area (P = F/A). Wide foot pads reduce pressure per square inch, keeping the heavy animal atop shifting dunes.",
        "ریگستانی اونٹ کے پاؤں پہاڑی بکریوں کے کھروں کے برعکس چوڑے، ہموار اور گدی دار کیوں ہوتے ہیں؟",
        ["چوڑا رقبہ جسم کے وزن کو پھیلا کر ریت پر دباؤ کم کرتا ہے جس سے پاؤں ریت میں نہیں دھنستے", "ہموار پاؤں گرمی جذب کرتے ہیں", "چلتے ہوئے ریت اڑانے کے لیے", "اونٹ سیلاب میں تیرنے کے لیے استعمال کرتے ہیں"],
        "چوڑا رقبہ جسم کے وزن کو پھیلا کر ریت پر دباؤ کم کرتا ہے جس سے پاؤں ریت میں نہیں دھنستے",
        "دباؤ رقبے کے الٹ ہوتا ہے۔ چوڑے گدی دار تلوے اونٹ کا بھاری وزن ریت پر دباؤ ڈالے بغیر آسانی سے پھسلا کر لے جاتے ہیں۔"
    ),
    (
        "Why does ice always float on top of liquid water, whereas almost all other solid substances sink in their own liquid phase?",
        ["Liquid water reaches maximum density at 4°C, and water molecules expand into an open hexagonal crystalline cage upon freezing", "Ice traps atmospheric oxygen inside", "Freezing boils water molecules", "Liquid water repels solids chemically"],
        "Liquid water reaches maximum density at 4°C, and water molecules expand into an open hexagonal crystalline cage upon freezing",
        "Hydrogen bonding forces ice into a rigid geometric lattice that occupies more volume than disordered liquid water, reducing solid density.",
        "برف پانی کی سطح پر کیوں تیرتی ہے جبکہ کائنات کی تقریباً تمام ٹھوس چیزیں اپنے ہی مائع میں ڈوب جاتی ہیں؟",
        ["پانی 4 ڈگری پر سب سے وزنی ہوتا ہے اور جم کر برف بنتے وقت اس کا حجم بڑھ کر کثافت کم ہو جاتی ہے", "برف ہوا کی آکسیجن قید کر لیتی ہے", "جمنے سے پانی ابلتا ہے", "پانی ٹھوس چیزوں کو دھکیلتا ہے"],
        "پانی 4 ڈگری پر سب سے وزنی ہوتا ہے اور جم کر برف بنتے وقت اس کا حجم بڑھ کر کثافت کم ہو جاتی ہے",
        "ہائیڈروجن بانڈنگ کی وجہ سے برف کے مالیکیولز ایک کھوکھلا چھ کونوں والا جال بناتے ہیں جو مائع پانی سے تقریباً 9 فیصد ہلکا ہوتا ہے۔"
    ),
    (
        "Why does an archer aim slightly above a distant bullseye target to hit the center accurately?",
        ["Earth's downward gravitational acceleration causes the arrow to travel along a curved parabolic trajectory", "Wind naturally pushes arrows upward", "The target moves down slightly", "Optical refraction elevates target sight"],
        "Earth's downward gravitational acceleration causes the arrow to travel along a curved parabolic trajectory",
        "Projectile motion dictates that gravity continuously pulls the projectile downward at 9.8 m/s^2 throughout its flight duration.",
        "تیر انداز دور کے نشانے پر سیدھا نشانہ باندھنے کی بجائے تھوڑا سا اوپر نشانہ کیوں لیتا ہے؟",
        ["زمین کی کشش ثقل تیر کو پرواز کے دوران نیچے کھینچتی ہے جس سے اس کا راستہ کمان نما منحنی ہو جاتا ہے", "ہوا تیر کو اوپر اٹھاتی ہے", "نشانہ خود بخود نیچے ہوتا ہے", "روشنی کا دھوکہ نشانے کو اونچا دکھاتا ہے"],
        "زمین کی کشش ثقل تیر کو پرواز کے دوران نیچے کھینچتی ہے جس سے اس کا راستہ کمان نما منحنی ہو جاتا ہے",
        "تیر جیسے ہی کمان سے نکلتا ہے کشش ثقل اسے نیچے گرانا شروع کر دیتی ہے۔ فاصلہ جتنا زیادہ ہوگا تیر اتنا ہی نیچے جا کر لگے گا۔"
    ),
    (
        "Why does an ordinary automobile tire appear round and full, yet flattens slightly at the exact point touching the pavement?",
        ["Normal contact force from the road creates an upward compressive reaction that counters the vehicle's axle load", "Tire pressure drops to zero at the bottom", "Friction heats and softens bottom rubber only", "Road surface absorbs air molecules"],
        "Normal contact force from the road creates an upward compressive reaction that counters the vehicle's axle load",
        "The tire carcass must deform until the contact patch area multiplied by internal tire pressure equals the downward wheel load.",
        "گاڑی کا ٹائر گول ہونے کے باوجود سڑک سے ٹکرانے والے نچلے مقام پر ہلکا سا چپٹا کیوں نظر آتا ہے؟",
        ["سڑک کا ردعمل کا دباؤ اندرونی ہوا کے پریشر کے ساتھ مل کر گاڑی کا وزن سنبھالنے کے لیے ٹائر کو دباتا ہے", "نیچے ہوا کا دباؤ ختم ہو جاتا ہے", "رگڑ صرف نچلے حصے کو پگھلاتی ہے", "سڑک ہوا چوس لیتی ہے"],
        "سڑک کا ردعمل کا دباؤ اندرونی ہوا کے پریشر کے ساتھ مل کر گاڑی کا وزن سنبھالنے کے لیے ٹائر کو دباتا ہے",
        "جب تک ٹائر کے چھونے والے رقبے اور اندر کی ہوا کا دباؤ مل کر گاڑی کے وزن کے برابر نہ ہو جائے، ٹائر تھوڑا سا دب کر بیٹھتا ہے۔"
    ),
    (
        "Why does a drop of dishwashing liquid instantly cause pepper flakes floating on water to scatter to the edges of the bowl?",
        ["Surfactant molecules dramatically reduce surface tension at the center, and higher peripheral surface tension pulls the film outward", "Pepper hates chemical odors", "Soap creates heat that pushes pepper", "Soap magnetizes pepper flakes"],
        "Surfactant molecules dramatically reduce surface tension at the center, and higher peripheral surface tension pulls the film outward",
        "This is the Marangoni effect: a gradient in surface tension causes fluid and floating debris to flow away from the low-tension region.",
        "پانی کی سطح پر تیرتی کالی مرچ کے سفوف پر برتن دھونے والے صابن کا قطرہ ڈالتے ہی مرچ کناروں کی طرف کیوں بھاگتی ہے؟",
        ["صابن مرکز میں سطحی تناؤ توڑ دیتا ہے جبکہ کناروں کا زیادہ تناؤ پانی کی باریک جھلی کو باہر کھینچتا ہے (Marangoni effect)", "کالی مرچ خوشبو سے دور بھاگتی ہے", "صابن گرمی پیدا کرتا ہے", "صابن مرچ کو مقناطیسی دھکا دیتا ہے"],
        "صابن مرکز میں سطحی تناؤ توڑ دیتا ہے جبکہ کناروں کا زیادہ تناؤ پانی کی باریک جھلی کو باہر کھینچتا ہے (Marangoni effect)",
        "صابن پانی کے مالیکیولز کی گرفت توڑ دیتا ہے، جبکہ پیالے کے کناروں کا مضبوط پانی فوراً پھیل کر مرچ کو اپنے ساتھ کناروں پر کھینچ لیتا ہے۔"
    ),
    (
        "Why does an ice skater spin much faster when she pulls her outstretched arms tightly in toward her chest?",
        ["Conservation of angular momentum dictates that reducing the moment of inertia increases rotational angular velocity (L = I * omega)", "Air friction decreases against her arms", "Centrifugal force pushes her around", "Her muscles generate spinning torque"],
        "Conservation of angular momentum dictates that reducing the moment of inertia increases rotational angular velocity (L = I * omega)",
        "With zero external torque, angular momentum remains constant. Bringing mass closer to the rotational axis reduces moment of inertia.",
        "برف پر رقص کرنے والی اسکیٹر جب اپنے پھیلے ہوئے بازو سمیٹ کر سینے سے لگاتی ہے تو اس کے گھومنے کی رفتار اچانک تیز کیوں ہو جاتی ہے؟",
        ["زاویائی مومینٹم کی بقا (L = I * omega) کے تحت ماس کو مرکز کے قریب لانے سے گھومنے کی رفتار بڑھ جاتی ہے", "ہوا کی رگڑ کم ہو جاتی ہے", "مرکز گریز قوت اسے گھماتی ہے", "پٹھے نئی طاقت پیدا کرتے ہیں"],
        "زاویائی مومینٹم کی بقا (L = I * omega) کے تحت ماس کو مرکز کے قریب لانے سے گھومنے کی رفتار بڑھ جاتی ہے",
        "جب گھومتی ہوئی چیز کا وزن مرکز کے قریب آ جاتا ہے تو اس کی گردش کا جمود کم ہو جاتا ہے اور رفتار خود بخود کئی گنا تیز ہو جاتی ہے۔"
    ),
    (
        "Why does a standard domestic refrigerator maintain a colder temperature in its bottom freezer compartment than its top shelves?",
        ["Cold air is denser than warm air and naturally sinks to the lowest level by gravitational convection", "The refrigerator light warms the top shelf", "Freezer compressors only cool downward", "Top shelves contain thinner plastic"],
        "Cold air is denser than warm air and naturally sinks to the lowest level by gravitational convection",
        "Molecules in colder air have lower thermal agitation and pack closer together; high density forces colder air downward.",
        "فریج کے اندرونی خانے میں نچلے حصے کا درجہ حرارت اوپری خانوں کے مقابلے میں زیادہ ٹھنڈا کیوں رہتا ہے؟",
        ["ٹھنڈی ہوا گرم ہوا سے زیادہ کثیف (بھاری) ہوتی ہے اور کشش ثقل کے تحت خود بخود نیچے بیٹھتی ہے", "بلب اوپری خانے کو گرم رکھتا ہے", "کمپریسر صرف نیچے ٹھنڈک بھیجتا ہے", "اوپر کا پلاسٹک پتلا ہوتا ہے"],
        "ٹھنڈی ہوا گرم ہوا سے زیادہ کثیف (بھاری) ہوتی ہے اور کشش ثقل کے تحت خود بخود نیچے بیٹھتی ہے",
        "حرارت کی کنویکشن کے اصول کے مطابق ٹھنڈی ہوا بھاری ہو کر نیچے کی طرف گرتی ہے اور گرم ہوا اوپر اٹھتی ہے۔"
    ),
    (
        "Why does a pendulum inside an airtight bell jar continue swinging back and forth for days, whereas one in an open room stops in hours?",
        ["Evacuating atmospheric air eliminates aerodynamic drag that dissipates kinetic energy into heat", "Vacuum creates antigravity energy", "Glass bell jar magnifies momentum", "Air pressure locks pendulum joints"],
        "Evacuating atmospheric air eliminates aerodynamic drag that dissipates kinetic energy into heat",
        "Air resistance provides the dominant viscous damping force. In high vacuum, only minuscule mechanical pivot friction remains.",
        "ہوا بند شیشے کے جار (Vacuum) میں جھولنے والا پینڈولم کھلے کمرے کے مقابلے میں کئی دن تک کیوں جھولتا رہتا ہے؟",
        ["ہوا کو نکال دینے سے وہ رگڑ (Aerodynamic drag) ختم ہو جاتی ہے جو توانائی کو ضائع کر کے پینڈولم کو روکتی ہے", "خلا میں کشش ثقل الٹ جاتی ہے", "شیشہ مومینٹم کو بڑھاتا ہے", "ہوا پینڈولم کے جوڑوں کو جکڑتی ہے"],
        "ہوا بند شیشے کے جار (Vacuum) میں جھولنے والا پینڈولم کھلے کمرے کے مقابلے میں کئی دن تک کیوں جھولتا رہتا ہے؟",
        "کھلی فضا میں ہوا کے مالیکیولز مسلسل پینڈولم سے ٹکرا کر اس کی رفتار کم کرتے ہیں۔ خلا میں صرف سہارے کی معمولی رگڑ باقی بچتی ہے۔"
    ),
    (
        "Why does sound travel roughly four times faster through solid steel rails than through open atmospheric air?",
        ["Steel has a vastly higher elastic modulus (bulk stiffness) that restores displaced atoms rapidly despite higher density", "Steel conducts electrical acoustic waves", "Air molecules are too heavy to vibrate", "Sound in steel travels as light waves"],
        "Steel has a vastly higher elastic modulus (bulk stiffness) that restores displaced atoms rapidly despite higher density",
        "Acoustic velocity depends on the ratio of elastic stiffness to density: c = sqrt(E / rho). Steel's immense stiffness dominates.",
        "ٹرین کی آواز کھلی ہوا کے مقابلے میں لوہے کی پٹڑی میں چار گنا زیادہ تیز رفتار سے کیوں سفر کرتی ہے؟",
        ["لوہے کے ایٹمی بندھنوں کی لچکدار سختی (Elastic stiffness) ہوا کے مقابلے میں لاکھوں گنا زیادہ ہوتی ہے", "لوہا برقی لہریں چلاتا ہے", "ہوا کے ذرات تھرتھرا نہیں سکتے", "لوہے میں آواز روشنی بن جاتی ہے"],
        "لوہے کے ایٹمی بندھنوں کی لچکدار سختی (Elastic stiffness) ہوا کے مقابلے میں لاکھوں گنا زیادہ ہوتی ہے",
        "آواز مادے کے ارتعاش سے چلتی ہے۔ لوہے کے ایٹم ایک دوسرے سے سختی سے جڑے ہوتے ہیں اس لیے دھچکا فوراً آگے پہنچتا ہے۔"
    ),
    (
        "Why does a scuba diver underwater appear roughly 33 percent larger and closer when viewed through a flat glass face mask?",
        ["Refraction of light at the flat water-glass-air interface bends rays, creating an enlarged virtual image", "Water acts as a magnifying lens", "The mask glass is curved like spectacles", "Air inside the mask magnifies objects"],
        "Refraction of light at the flat water-glass-air interface bends rays, creating an enlarged virtual image",
        "Snell's Law bending at the air-water optical boundary reduces the divergence angle of light rays reaching the eyes, making objects seem closer.",
        "پانی کے اندر فلیٹ شیشے کا ماسک پہن کر دیکھنے پر مچھلیاں اور چیزیں تقریباً ایک تہائی بڑی اور قریب کیوں نظر آتی ہیں؟",
        ["پانی، شیشے اور ماسک کی اندرونی ہوا کے درمیان روشنی کے انعطاف سے بڑا مجازی عکس بنتا ہے", "پانی خود عدسہ بن جاتا ہے", "ماسک کا شیشہ محدب ہوتا ہے", "اندر کی ہوا چیزوں کو پھیلاتی ہے"],
        "پانی، شیشے اور ماسک کی اندرونی ہوا کے درمیان روشنی کے انعطاف سے بڑا مجازی عکس بنتا ہے",
        "روشنی جب پانی سے ماسک کی ہوا میں داخل ہوتی ہے تو باہر کی طرف مڑتی ہے، جس سے انسانی دماغ کو چیزیں 25 سے 33 فیصد بڑی لگتی ہیں۔"
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
        "Why does an electric toaster heating wire glow bright red-orange while the power cord plugged into the wall outlet stays cool?",
        ["Nichrome wire has vastly higher electrical resistance than copper, dissipating substantial Joule heat (P = I^2 * R)", "Power cords contain refrigerant fluid", "Wall outlets filter heat out", "Copper wires repel electrical energy"],
        "Nichrome wire has vastly higher electrical resistance than copper, dissipating substantial Joule heat (P = I^2 * R)",
        "Current I is identical throughout the series circuit. Copper's low resistance yields negligible heat, while nichrome's high resistance glows.",
        "ٹووسٹر کی جالی کی باریک تاریں سرخ دہک اٹھتی ہیں جبکہ دیوار کے ساکٹ میں لگی مین کیبل بالکل ٹھنڈی کیوں رہتی ہے؟",
        ["نائی کروم تار کی برقی مزاحمت (Resistance) تانبے سے کہیں زیادہ ہوتی ہے جو جول حرارت بناتی ہے (P = I^2 * R)", "مین کیبل میں ٹھنڈا مائع ہوتا ہے", "ساکٹ گرمی کو روک لیتا ہے", "تانبا بجلی کو آگے دھکیلتا ہے"],
        "نائی کروم تار کی برقی مزاحمت (Resistance) تانبے سے کہیں زیادہ ہوتی ہے جو جول حرارت بناتی ہے (P = I^2 * R)",
        "دونوں تاروں میں کرنٹ برابر گزرتا ہے، مگر نائی کروم کی زیادہ رکاوٹ الیکٹرانز کی توانائی کو حرارت اور روشنی میں بدل کر دہکا دیتی ہے۔"
    ),
    (
        "Why do passengers standing on a moving bus stumble forward when the bus driver suddenly slams on the brakes?",
        ["Newton's First Law of Inertia causes the passenger's upper body to maintain its forward velocity", "The floor pulls feet backward by suction", "Air inside the bus rushes forward", "Gravity shifts toward the windshield"],
        "Newton's First Law of Inertia causes the passenger's upper body to maintain its forward velocity",
        "An object in motion remains in uniform rectilinear motion unless acted upon by an external net force; braking acts on feet first.",
        "چلتی ہوئی بس کے اچانک زوردار بریک لگانے پر کھڑے ہوئے مسافر آگے کی طرف کیوں گرتے ہیں؟",
        ["نیوٹن کے پہلے قانون (انرشیا) کے تحت مسافر کا جسم اپنی آگے بڑھنے کی رفتار کو برقرار رکھنا چاہتا ہے", "فرش پاؤں کو پیچھے کھینچتا ہے", "اندر کی ہوا آگے دھکیلتی ہے", "کشش ثقل آگے جھک جاتی ہے"],
        "نیوٹن کے پہلے قانون (انرشیا) کے تحت مسافر کا جسم اپنی آگے بڑھنے کی رفتار کو برقرار رکھنا چاہتا ہے",
        "پاؤں فرش کی رگڑ سے رک جاتے ہیں مگر اوپری جسم پر فوری قوت نہ لگنے سے وہ پرانی رفتار پر آگے ہی بڑھتا رہتا ہے۔"
    ),
    (
        "Why does the human heart beat faster during intense physical exercise?",
        ["To increase cardiac output and deliver oxygen and glucose to contracting skeletal muscle tissues", "To cool down arterial blood", "To prevent blood from clotting", "Muscles squeeze the heart mechanically"],
        "To increase cardiac output and deliver oxygen and glucose to contracting skeletal muscle tissues",
        "Sympathetic nervous stimulation elevates stroke rate and volume to meet elevated metabolic aerobic respiration demands.",
        "تیز دوڑنے یا سخت ورزش کے دوران انسان کے دل کی دھڑکن تیز کیوں ہو جاتی ہے؟",
        ["ورزش کرتے پٹھوں کو آکسیجن اور گلوکوز کی فوری ترسیل کے لیے خون کا بہاؤ بڑھانا ضروری ہوتا ہے", "خون کو ٹھنڈا کرنے کے لیے", "خون کو جمنے سے روکنے کے لیے", "پٹھے دل کو دباتے ہیں"],
        "ورزش کرتے پٹھوں کو آکسیجن اور گلوکوز کی فوری ترسیل کے لیے خون کا بہاؤ بڑھانا ضروری ہوتا ہے",
        "پٹھوں کو توانائی بنانے کے لیے زیادہ آکسیجن چاہیے ہوتی ہے، دل پمپنگ کی رفتار بڑھا کر یہ ضرورت پوری کرتا ہے۔"
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
        "چمچ کے اندرونی گہرے رخ (Concave) میں دیکھنے پر انسان کا اپنا چہرہ الٹا کیوں دکھائی دیتا ہے؟",
        "مقعر آئینہ روشنی کی شعاعوں کو اندر کی طرف موڑتا ہے جو آنکھوں تک پہنچنے سے پہلے الٹ جاتی ہیں، جس سے الٹا عکس بنتا ہے۔"
    ),
    (
        "Why does warm bread freshly taken out of the oven smell so intensely fragrant across the whole kitchen?",
        ["High thermal energy accelerates the volatility and kinetic diffusion of aromatic ester compounds through the air", "Yeast multiplies in mid-air", "Oven heat burns the bread crust", "Flour dust creates vapor trails"],
        "High thermal energy accelerates the volatility and kinetic diffusion of aromatic ester compounds through the air",
        "Elevated temperature raises vapor pressure, propelling aromatic Maillard reaction volatile molecules rapidly into the surrounding atmosphere.",
        "تندور یا اوون سے تازی نکلی ہوئی گرم روٹی کی خوشبو پورے کمرے میں فوراً کیوں پھیل جاتی ہے؟",
        ["حرارت خوشبودار مالیکیولز کو بخارات بنا کر ہوا میں ان کے پھیلاؤ (Diffusion) کی رفتار تیز کر دیتی ہے", "خمیر فضا میں اڑتا ہے", "گرمی سے روٹی جلتی ہے", "آٹے کا غبار فضا میں پھیلتا ہے"],
        "حرارت خوشبودار مالیکیولز کو بخارات بنا کر ہوا میں ان کے پھیلاؤ (Diffusion) کی رفتار تیز کر دیتی ہے",
        "گرم چیزوں کے مالیکیولز کی حرکی توانائی زیادہ ہوتی ہے جس سے وہ گیس بن کر کمرے کی ہوا میں تیزی سے پھیل جاتے ہیں۔"
    ),
    (
        "Why does an ocean lighthouse beam rotate continuously across the dark coastline rather than shine as a steady stationary light?",
        ["Sweeping a concentrated collimated light beam allows mariners at sea to perceive a bright flash and gauge bearing and identity", "Stationary bulbs burn out quickly", "Lighthouses use windmill power", "Fog extinguishes stationary lights"],
        "Sweeping a concentrated collimated light beam allows mariners at sea to perceive a bright flash and gauge bearing and identity",
        "Fresnel lenses concentrate light into narrow intense rays; revolving them produces unique flash characteristics identifying coastal hazards.",
        "سمندر کے کنارے لائٹ ہاؤس کی روشنی ساکن رہنے کی بجائے مسلسل گھومتی کیوں رہتی ہے؟",
        ["روشنی کی تیز شعاع گھوم کر سمندر میں دور موجود جہازوں کو چمک اور پہچان فراہم کرتی ہے", "ساکن بلب جلد فیوز ہو جاتے ہیں", "لائٹ ہاؤس ہوا کے رخ پر چلتا ہے", "دھند ساکن روشنی کو بجھا دیتی ہے"],
        "روشنی کی تیز شعاع گھوم کر سمندر میں دور موجود جہازوں کو چمک اور پہچان فراہم کرتی ہے",
        "طاقتور لینز روشنی کو ایک بیم میں مرکوز کرتے ہیں، گھومنے سے ہر لائٹ ہاؤس کا ایک مخصوص چمکنے کا وقفہ بنتا ہے جس سے ملاح راستہ پہچانتے ہیں۔"
    ),
    (
        "Why does an acoustic echo occur only when you shout in a large hall or near a distant cliff, but never in a small furnished bedroom?",
        ["Reflected sound waves in small rooms return in under 0.1 seconds, merging into the original sound before the brain can separate them", "Furniture destroys acoustic sound waves", "Small rooms have lower air pressure", "Human ears mute echoes automatically"],
        "Reflected sound waves in small rooms return in under 0.1 seconds, merging into the original sound before the brain can separate them",
        "The human auditory persistence threshold is roughly 100 ms. If reflected sound returns sooner, it is perceived as reverberation, not a distinct echo.",
        "بڑے ہال یا پہاڑ کے سامنے آواز کی بازگشت (Echo) سنائی دیتی ہے مگر چھوٹے سجے ہوئے کمرے میں گونج کیوں نہیں بنتی؟",
        ["چھوٹے کمرے میں ٹکرا کر لوٹنے والی آواز 0.1 سیکنڈ سے پہلے آ جاتی ہے جسے دماغ الگ آواز نہیں مان سکتا", "فرنیچر آواز کو ختم کر دیتا ہے", "چھوٹے کمرے میں ہوا کم ہوتی ہے", "کان خود بخود گونج بند کر دیتے ہیں"],
        "چھوٹے کمرے میں ٹکرا کر لوٹنے والی آواز 0.1 سیکنڈ سے پہلے آ جاتی ہے جسے دماغ الگ آواز نہیں مان سکتا",
        "دماغ دو آوازوں میں فرق تب کرتا ہے جب ان میں کم از کم 0.1 سیکنڈ کا وقفہ ہو (کم از کم 17 میٹر فاصلہ)۔ فرنیچر بھی آواز جذب کر لیتا ہے۔"
    ),
    (
        "Why does a freshly cracked chicken egg remain separate with a rounded yolk resting on top of clear albumen?",
        ["The vitelline membrane encloses the dense hydrophobic lipid yolk, segregating it from the water-rich albumen", "Yolk has higher air pressure inside", "The egg white contains solid shell dust", "Centrifugal force centers the yolk"],
        "The vitelline membrane encloses the dense hydrophobic lipid yolk, segregating it from the water-rich albumen",
        "A delicate protein-based vitelline envelope encapsulates the yolk, preventing mixing with the surrounding aqueous protein solution.",
        "انڈے کو توڑنے پر اس کی زردی سفیدی کے اوپر گول اور الگ تھلگ کیوں برقرار رہتی ہے؟",
        ["ایک باریک جھلی (Vitelline membrane) چربی دار زردی کو بند رکھ کر سفیدی میں گھلنے سے روکتی ہے", "زردی کے اندر ہوا کا دباؤ ہوتا ہے", "سفیدی میں چھلکے کا پاؤڈر ہوتا ہے", "مرکز گریز قوت زردی کو گول رکھتی ہے"],
        "ایک باریک جھلی (Vitelline membrane) چربی دار زردی کو بند رکھ کر سفیدی میں گھلنے سے روکتی ہے",
        "زردی کے گرد ایک قدرتی لچکدار جھلی ہوتی ہے جو اسے اپنی گولائی قائم رکھنے دیتی ہے جب تک کہ اسے جان بوجھ کر توڑا نہ جائے۔"
    ),
    (
        "Why does a diver tuck their knees tightly against their chest when performing multi-rotation somersaults from a high platform?",
        ["Minimizing the radius of gyration reduces moment of inertia, dramatically accelerating spin rate (Conservation of Angular Momentum)", "To resist wind pressure against the face", "To stay warm during high drops", "To soften the water impact"],
        "Minimizing the radius of gyration reduces moment of inertia, dramatically accelerating spin rate (Conservation of Angular Momentum)",
        "Because angular momentum is conserved once in free flight, reducing rotational inertia increases angular velocity.",
        "اونچائی سے غوطہ لگانے والا کھلاڑی ہوا میں تیزی سے کلا بازیاں کھاتے وقت اپنے گھٹنے سینے سے کیوں جکڑ لیتا ہے؟",
        ["گھٹنے سمیٹنے سے جسم کا جمود کم ہو جاتا ہے اور ہوا میں گھومنے کی رفتار خود بخود تیز ہو جاتی ہے", "ہوا کے تھپیڑوں سے چہرے کو بچانے کے لیے", "جسم کو ٹھنڈک سے بچانے کے لیے", "پانی میں نرم لینڈنگ کے لیے"],
        "گھٹنے سمیٹنے سے جسم کا جمود کم ہو جاتا ہے اور ہوا میں گھومنے کی رفتار خود بخود تیز ہو جاتی ہے",
        "زاویائی مومینٹم کی بقا کے اصول کے تحت جسم جتنا گول اور چھوٹا ہوگا، وہ ہوا میں اتنے ہی زیادہ چکر کاٹ سکے گا۔"
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
        "Why does a drop of water on a hot cooking pan sizzle and skate across the metal without boiling away immediately if the pan is extremely hot?",
        ["A thin insulating vapor layer forms underneath the droplet, insulating it from direct thermal conduction (Leidenfrost effect)", "Water turns into solid dry ice", "Metal expands and repels water magnetically", "Extreme heat freezes the water surface"],
        "A thin insulating vapor layer forms underneath the droplet, insulating it from direct thermal conduction (Leidenfrost effect)",
        "Above the Leidenfrost point, bottom water flash-vaporizes into steam with poor thermal conductivity, suspending the droplet.",
        "بہت زیادہ دہکتے ہوئے فرائنگ پین پر پانی کا قطرہ فوراً ابلنے کی بجائے پین پر گیند کی طرح ناچتا ہوا کیوں تیرتا ہے؟",
        ["قطرے کے نیچے بھاپ کی ایک باریک تہہ بن جاتی ہے جو حرارت کو روک کر قطرے کو معلق کر دیتی ہے (Leidenfrost effect)", "پانی خشک برف بن جاتا ہے", "گرم لوہا مقناطیسی دھکا دیتا ہے", "شدید گرمی سے پانی کی سطح جم جاتی ہے"],
        "قطرے کے نیچے بھاپ کی ایک باریک تہہ بن جاتی ہے جو حرارت کو روک کر قطرے کو معلق کر دیتی ہے (Leidenfrost effect)",
        "لائیڈن فروسٹ اثر کے تحت قطرے کا نچلا حصہ فوری بھاپ بن کر ایک کشن کا کام کرتا ہے جس سے باقی قطرہ دیر تک نہیں ابلتا۔"
    ),
    (
        "Why does an ordinary lead-acid car battery require distilled water rather than mineral tap water when being topped off?",
        ["Dissolved mineral ions in tap water cause internal galvanic short-circuits and rapid plate degradation", "Tap water is too cold for car engines", "Distilled water contains pure hydrogen fuel", "Lead reacts explosively with chlorine only"],
        "Dissolved mineral ions in tap water cause internal galvanic short-circuits and rapid plate degradation",
        "Metallic ions (iron, calcium, magnesium) poison the lead plates, promoting self-discharge and battery sulfation.",
        "گاڑی کی تیزابی بیٹری میں عام نلکے کا پانی ڈالنے کی بجائے مقطر پانی (Distilled water) کیوں ڈالا جاتا ہے؟",
        ["نلکے کے پانی کے نمکیات بیٹری کی تختیوں پر جم کر اندرونی شارٹ سرکٹ اور خرابی پیدا کرتے ہیں", "نلکے کا پانی گاڑی کے لیے بہت ٹھنڈا ہوتا ہے", "مقطر پانی میں ہائیڈروجن ایندھن ہوتا ہے", "لیڈ کلورین سے دھماکہ کرتا ہے"],
        "نلکے کے پانی کے نمکیات بیٹری کی تختیوں پر جم کر اندرونی شارٹ سرکٹ اور خرابی پیدا کرتے ہیں",
        "عام پانی میں موجود معدنیات بجلی کے چارج کو ضائع کر دیتی ہیں اور لیڈ کی پلیٹوں کو وقت سے پہلے ناکارہ بنا دیتی ہیں۔"
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
        "Why does a metallic sound ring out with a clear chime when struck, while a wooden block emits only a dull thud?",
        ["Metals have crystalline lattice elasticity with minimal internal friction, vibrating continuously with low mechanical damping", "Wood is denser than metal", "Metal is hollow on the molecular level", "Wood destroys sound frequencies"],
        "Metals have crystalline lattice elasticity with minimal internal friction, vibrating continuously with low mechanical damping",
        "Rigid metallic bonding allows acoustic vibrations to oscillate with low energy dissipation, unlike fibrous wood polymers that absorb mechanical vibrations.",
        "دھات کی گھنٹی پر چوٹ مارنے سے مدھر جھنکار گونجتی ہے جبکہ لکڑی پر چوٹ مارنے سے صرف بھدی آواز کیوں نکلتی ہے؟",
        ["دھات کا ایٹمی جال لچکدار ہوتا ہے جو ارتعاش کو جذب کرنے کی بجائے دیر تک تھرتھراتا رہتا ہے", "لکڑی دھات سے زیادہ کثیف ہوتی ہے", "دھات اندر سے کھوکھلی ہوتی ہے", "لکڑی تمام آوازوں کو ختم کر دیتی ہے"],
        "دھات کا ایٹمی جال لچکدار ہوتا ہے جو ارتعاش کو جذب کرنے کی بجائے دیر تک تھرتھراتا رہتا ہے",
        "لکڑی کے ریشے جھٹکے کی توانائی کو فوراً دبا کر ضائع کر دیتے ہیں، جبکہ دھات کے ایٹم لچکدار چشمے کی طرح مسلسل لہریں پیدا کرتے ہیں۔"
    ),
    (
        "Why does an ocean cargo vessel maintain its upright stability even when buffeted by gigantic side waves?",
        ["Its center of buoyancy shifts outward as the ship rolls, generating a righting moment that restores the vessel upright", "It uses giant submarine magnets", "Water pushes the ship down equally", "Ballast water freezes during storms"],
        "Its center of buoyancy shifts outward as the ship rolls, generating a righting moment that restores the vessel upright",
        "When the hull heels over, the submerged volume shape displaces toward the lower side, shifting the metacenter above the center of gravity.",
        "بڑا بحری جہاز سمندر کی اونچی لہروں کے تھپیڑے کھانے کے باوجود الٹنے کی بجائے واپس سیدھا کیسے ہو جاتا ہے؟",
        ["جہاز کے جھکتے ہی اچھال کا مرکز (Buoyancy) باہر سرک کر الٹنے کے مخالف قوت پیدا کرتا ہے (Righting moment)", "پیندے میں طاقتور مقناطیس ہوتے ہیں", "پانی ہر طرف سے برابر دباتا ہے", "جہاز کا پانی جم جاتا ہے"],
        "جہاز کے جھکتے ہی اچھال کا مرکز (Buoyancy) باہر سرک کر الٹنے کے مخالف قوت پیدا کرتا ہے (Righting moment)",
        "جب جہاز ٹیڑھا ہوتا ہے تو ڈوبنے والے حصے پر پانی کا اچھال بڑھ جاتا ہے جو اسے خود بخود دھکیل کر دوبارہ سیدھا کر دیتا ہے۔"
    ),
    (
        "Why does a person feeling car sickness recover more easily when sitting in the front passenger seat than the rear seat?",
        ["The front windshield offers an unobstructed view of the horizon, aligning visual input with inner-ear balance signals", "The front seat has lower cabin air pressure", "Rear seats have no seatbelts", "Engines pull front seats forward"],
        "The front windshield offers an unobstructed view of the horizon, aligning visual input with inner-ear balance signals",
        "Viewing road motion reduces sensory mismatch between the vestibular apparatus (detecting turns) and the visual cortex.",
        "گاڑی میں سفر کے دوران چکر محسوس کرنے والا مسافر پچھلی سیٹ کے مقابلے میں اگلی سیٹ پر بیٹھ کر بہتر کیوں محسوس کرتا ہے؟",
        ["سامنے کے شیشے سے سڑک اور افق صاف نظر آتا ہے جو کان اور آنکھوں کے توازن کے سگنلز کو ہم آہنگ کر دیتا ہے", "سامنے ہوا کا دباؤ کم ہوتا ہے", "پچھلی سیٹوں پر جھٹکے نہیں لگتے", "انجن اگلی سیٹ کو کھینچتا ہے"],
        "سامنے کے شیشے سے سڑک اور افق صاف نظر آتا ہے جو کان اور آنکھوں کے توازن کے سگنلز کو ہم آہنگ کر دیتا ہے",
        "جب انسان سامنے دیکھتا ہے تو دماغ گاڑی کے موڑ اور حرکت کو پہلے سے دیکھ کر قبول کر لیتا ہے، جس سے متلی پیدا نہیں ہوتی۔"
    ),
    (
        "Why does an ordinary candle flame naturally point straight upward toward the ceiling in Earth's gravity?",
        ["Hot combustion gases expand, become less dense than surrounding cool air, and are buoyed straight upward by convection", "The wick pulls the flame upward", "Carbon atoms repel gravitational pull", "Ceilings attract heat magnetically"],
        "Hot combustion gases expand, become less dense than surrounding cool air, and are buoyed straight upward by convection",
        "Convective buoyancy drives hot light gas upward, drawing cooler dense air inward at the base to feed oxygen into the teardrop-shaped flame.",
        "موم بتی کا شعلہ زمین کی کشش ثقل میں ہمیشہ سیدھا اوپر چھت کی طرف ہی کیوں اٹھتا ہے؟",
        ["جلنے والی گرم گیسیں ہلکی ہو کر پھیلتی ہیں اور ٹھنڈی بھاری ہوا کے دباؤ سے سیدھی اوپر اٹھتی ہیں (Buoyancy)", "بتی شعلے کو اوپر کھینچتی ہے", "کاربن کشش ثقل کے الٹ بھاگتا ہے", "چھت گرمی کو کھینچتی ہے"],
        "جلنے والی گرم گیسیں ہلکی ہو کر پھیلتی ہیں اور ٹھنڈی بھاری ہوا کے دباؤ سے سیدھی اوپر اٹھتی ہیں (Buoyancy)",
        "گرمی سے ہوا پھیل کر ہلکی ہو جاتی ہے اور چاروں طرف کی ٹھنڈی ہوا اسے اوپر اچھال دیتی ہے، خلا میں شعلہ گیند کی طرح گول بنتا ہے۔"
    ),
    (
        "Why does an inflated soccer ball bounce higher on a warm summer afternoon than on a freezing winter morning?",
        ["Warm air inside increases molecular kinetic pressure, making the ball firmer with greater coefficient of restitution", "Summer turf is softer than winter snow", "Winter gravity pulls sports equipment harder", "Ball leather absorbs cold air molecules"],
        "Warm air inside increases molecular kinetic pressure, making the ball firmer with greater coefficient of restitution",
        "Higher temperature increases internal gauge pressure according to Gay-Lussac's Law; higher pressure reduces deformation energy losses.",
        "فٹ بال سردیوں کی صبح کے مقابلے میں گرمیوں کی دوپہر کو فرش پر زیادہ اونچا اچھال کیوں لیتی ہے؟",
        ["گرمی سے گیند کے اندر ہوا کے مالیکیولز کا اندرونی دباؤ بڑھ جاتا ہے جو اسے زیادہ لچکدار اور اچھلنے والا بناتا ہے", "گرمیوں میں زمین نرم ہوتی ہے", "سردیوں میں کشش ثقل بڑھ جاتی ہے", "چمڑا سردی میں ہوا پی جاتا ہے"],
        "گرمی سے گیند کے اندر ہوا کے مالیکیولز کا اندرونی دباؤ بڑھ جاتا ہے جو اسے زیادہ لچکدار اور اچھلنے والا بناتا ہے",
        "درجہ حرارت بڑھنے سے اندرونی گیس کا پریشر بڑھ جاتا ہے، جس سے گیند زمین سے ٹکرا کر اپنی شکل فوراً بحال کرتی ہے اور اونچا اچھلتی ہے۔"
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
        "Why does a metal spoon feel freezing cold when removed from ice cream, while a wooden spoon at the exact same temperature feels comfortable?",
        ["Metals have high thermal conductivity, conducting heat away from your fingertips hundreds of times faster than wood", "The metal spoon is physically colder in degrees", "Wood produces internal heat through friction", "Metal absorbs human skin oils"],
        "Metals have high thermal conductivity, conducting heat away from your fingertips hundreds of times faster than wood",
        "Human temperature receptors sense the rate of heat flux leaving the skin (d Q/d t), not absolute temperature.",
        "آئس کریم سے نکالا گیا لوہے کا چمچ ہاتھ کو برف کی طرح ٹھنڈا لگتا ہے جبکہ لکڑی کا چمچ اسی درجہ حرارت پر ٹھنڈا کیوں نہیں لگتا؟",
        ["دھات کی تھرمل کنڈکٹیویٹی انگلیوں سے حرارت کو لکڑی کے مقابلے میں سینکڑوں گنا زیادہ تیزی سے چوس لیتی ہے", "لوہے کا چمچ درحقیقت زیادہ ٹھنڈا ہوتا ہے", "لکڑی اندرونی حرارت بناتی ہے", "دھات جلد کا تیل پی لیتی ہے"],
        "دھات کی تھرمل کنڈکٹیویٹی انگلیوں سے حرارت کو لکڑی کے مقابلے میں سینکڑوں گنا زیادہ تیزی سے چوس لیتی ہے",
        "ہماری جلد درجہ حرارت نہیں ناپتی بلکہ یہ دیکھتی ہے کہ حرارت کتنی تیزی سے جسم سے نکل رہی ہے۔ لوہا حرارت تیزی سے کھینچتا ہے اس لیے شدید ٹھنڈا لگتا ہے۔"
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
        "دھند اور کہرے میں مدہم منظر انسانی دماغ کو یہ دھوکہ دیتا ہے کہ عمارت بہت دور ہے، اس لیے دماغ اس کا سائز بڑا تصور کرتا ہے",
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
    )
]

print(f"Normal Remaining Part 2 loaded: {len(ITEMS)} items.")
