# -*- coding: utf-8 -*-
"""
Normal Supplementary Catalog Part 1 (112 distinct items)
Topics: Real-world engineering, applied physics, detective logic, and forensic science.
Each item is an 8-tuple: (q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    # 1: Seatbelt inertia lock
    (
        "Why does an automobile seatbelt webbing strap pull freely during normal movement, but instantly lock solid when the driver jerks it forward violently?",
        ["A spring-weighted pendulum or centrifugal clutch locks the ratchet spool under sudden acceleration", "Air pressure locks it", "Electromagnets turn on", "The belt shrinks"],
        "A spring-weighted pendulum or centrifugal clutch locks the ratchet spool under sudden acceleration",
        "Rapid deceleration swings an internal inertia pendulum, engaging a hardened pawl into the locking gear teeth.",
        "گاڑی کی سیٹ بیلٹ آہستہ کھینچنے پر آسانی سے کھلتی ہے مگر اچانک جھٹکا لگنے پر فوری جام کیوں ہو جاتی ہے؟",
        ["اندر موجود جائروسکوپک پنڈولم اچانک جھٹکے پر فورا گیئر کے دانتوں میں پھنس کر بیلٹ روک دیتا ہے", "ہوا کا دباؤ روکتا ہے", "مقناطیس آن ہو جاتا ہے", "بیلٹ چھوٹی ہو جاتی ہے"],
        "اندر موجود جائروسکوپک پنڈولم اچانک جھٹکے پر فورا گیئر کے دانتوں میں پھنس کر بیلٹ روک دیتا ہے",
        "حادثے کے جھٹکے سے اندر کا وزنی پنڈولم حرکت کر کے لاکنگ سسٹم کو متحرک کر دیتا ہے تاکہ مسافر آگے نہ گرے۔"
    ),
    # 2: Wind turbine aerodynamic lift
    (
        "How do the giant slender blades of an offshore wind turbine rotate to generate megawatts of clean electricity?",
        ["Aerodynamic airfoil camber creates aerodynamic lift perpendicular to relative wind, driving the low-speed shaft", "Wind pushes blades by pure flat friction", "The ocean waves turn it", "Electric motors spin it"],
        "Aerodynamic airfoil camber creates aerodynamic lift perpendicular to relative wind, driving the low-speed shaft",
        "Airfoil blades generate aerodynamic lift forces that exert rotational torque on the central hub rather than relying on simple drag.",
        "سمندر کنارے لگی ہوا سے چلنے والی ونڈ ٹربائن کے بڑے پر بجلی بنانے کے لیے کیسے گھومتے ہیں؟",
        ["ہوائی جہاز کے پروں جیسی ایروڈائنامک ساخت ہوا کے دباؤ سے لفٹ فورس پیدا کر کے شافٹ کو گھماتی ہے", "ہوا کی سیدھی رگڑ سے", "سمندر کی لہروں کے جھٹکے سے", "اندر کی موٹر گھماتی ہے"],
        "ہوائی جہاز کے پروں جیسی ایروڈائنامک ساخت ہوا کے دباؤ سے لفٹ فورس پیدا کر کے شافٹ کو گھماتی ہے",
        "ونڈ ٹربائن کے پر ہوائی جہاز کے پروں کی طرح ہوا کو کاٹتے ہیں جس سے پیدا ہونے والی لفٹ انہیں تیزی سے گھماتی ہے۔"
    ),
    # 3: Solar photovoltaic cell band gap
    (
        "How do silicon rooftop solar photovoltaic panels generate direct current (DC) electricity from ambient sunlight?",
        ["Incident photons knock valence electrons across the silicon band gap into the conduction band, creating electric current", "Sunlight heats water inside", "Solar wind strikes panels", "Glass melts into power"],
        "Incident photons knock valence electrons across the silicon band gap into the conduction band, creating electric current",
        "Photons with energy greater than silicon's 1.1 eV band gap excite electron-hole pairs separated by the internal p-n junction.",
        "چھت پر لگی سلیکان کی سولر پلیٹیں سورج کی دھوپ سے بجلی کیسے پیدا کرتی ہیں؟",
        ["روشنی کے فوٹونز سلیکان کے ایٹمز سے ٹکرا کر الیکٹرانز کو متحرک کرتے ہیں جس سے کرنٹ بہنے لگتا ہے", "سورج کی گرمی اندر کا پانی ابالتی ہے", "ہوا سے پلیٹیں ہلتی ہیں", "شیشہ پگھل کر بجلی بنتا ہے"],
        "روشنی کے فوٹونز سلیکان کے ایٹمز سے ٹکرا کر الیکٹرانز کو متحرک کرتے ہیں جس سے کرنٹ بہنے لگتا ہے",
        "سولر سیلز پر پڑنے والی روشنی کے پارٹیکلز (فوٹونز) سلیکان کے الیکٹرانز کو آزاد کر کے برقی رو پیدا کرتے ہیں۔"
    ),
    # 4: Electrical transformer mutual inductance
    (
        "How does an electrical grid substation transformer step 11,000 volts down to household 220 volts without moving parts?",
        ["Alternating current in the primary coil induces a fluctuating magnetic flux in the iron core, inducing voltage in the secondary coil", "Friction cools the wire", "The core absorbs extra volts", "Capacitors leak power"],
        "Alternating current in the primary coil induces a fluctuating magnetic flux in the iron core, inducing voltage in the secondary coil",
        "Faraday's law of induction dictates that voltage ratio equals the winding turns ratio (V1/V2 = N1/N2).",
        "محلے کا بجلی کا ٹرانسفارمر 11 ہزار وولٹ کی خطرناک بجلی کو بغیر کسی حرکت کے 220 وولٹ میں کیسے بدلتا ہے؟",
        ["پہلی کوائل کی الٹرنیٹنگ بجلی لوہے کے کور میں مقناطیسی لہریں بنا کر دوسری کوائل میں کم وولٹیج پیدا کرتی ہے", "تار کی رگڑ سے وولٹ کم ہوتے ہیں", "لوہا اضافی بجلی پی جاتا ہے", "کنڈینسز بجلی ضائع کرتے ہیں"],
        "پہلی کوائل کی الٹرنیٹنگ بجلی لوہے کے کور میں مقناطیسی لہریں بنا کر دوسری کوائل میں کم وولٹیج پیدا کرتی ہے",
        "ٹرانسفارمر میں دو کوائلز کے چکروں کا تناسب مقناطیسی فیلڈ کے ذریعے وولٹیج کو کم یا زیادہ کر دیتا ہے۔"
    ),
    # 5: High voltage power transmission lines
    (
        "Why do nationwide electrical power utilities transmit electricity across mountains at 500,000 volts instead of standard 220 volts?",
        ["Higher voltage proportionally reduces transmission current, minimizing I^2*R resistive thermal energy waste in cables", "High voltage travels faster than light", "500 kV makes cables lighter", "High voltage repels birds"],
        "Higher voltage proportionally reduces transmission current, minimizing I^2*R resistive thermal energy waste in cables",
        "Power loss in lines equals current squared times resistance (P_loss = I^2 * R); stepping voltage up reduces current by the same factor.",
        "دور دراز علاقوں تک بجلی پہنچانے کے لیے گرڈ کی بڑی تاروں میں 5 لاکھ وولٹ کا ہائی وولٹیج کیوں رکھا جاتا ہے؟",
        ["زیادہ وولٹیج کرنٹ (ایمپیئر) کو کم کر دیتا ہے جس سے تاروں میں گرمی کی صورت میں بجلی کا ضیاع کم سے کم ہوتا ہے", "ہائی وولٹیج روشنی سے تیز چلتا ہے", "اس سے تاروں کا وزن کم ہو جاتا ہے", "پرندوں کو دور رکھنے کے لیے"],
        "زیادہ وولٹیج کرنٹ (ایمپیئر) کو کم کر دیتا ہے جس سے تاروں میں گرمی کی صورت میں بجلی کا ضیاع کم سے کم ہوتا ہے",
        "وولٹیج بڑھانے سے کرنٹ کم ہو جاتا ہے، جس کی وجہ سے سینکڑوں میل لمبے تاروں میں حرارت کا ضیاع نہ ہونے کے برابر رہتا ہے۔"
    ),
    # 6: GFCI electrical safety outlet
    (
        "Why does a bathroom GFCI electrical safety outlet trip and shut off in milliseconds if a plugged-in hairdryer falls into a sink filled with water?",
        ["It detects any micro-imbalance between outgoing hot wire current and returning neutral wire current leaking to ground", "Water overloads the circuit breaker", "The outlet gets too hot", "The hair dryer blows a fuse"],
        "It detects any micro-imbalance between outgoing hot wire current and returning neutral wire current leaking to ground",
        "A differential current transformer senses leakages as low as 4-6 milliamps escaping to earth ground, opening contacts in 25 milliseconds.",
        "باتھ روم کا جدید حفاظتی سوئچ (GFCI) پانی میں ہیئر ڈرائر گرتے ہی سیکنڈ کے ہزارویں حصے میں کرنٹ کیوں کاٹ دیتا ہے؟",
        ["وہ جانے والے اور واپس آنے والے کرنٹ میں ذرا سا فرق آتے ہی پہچان لیتا ہے کہ کرنٹ پانی میں لیک ہو رہا ہے", "پانی سے تار جل جاتا ہے", "سوئچ گرم ہو جاتا ہے", "ڈرائر کا پنکھا رک جاتا ہے"],
        "وہ جانے والے اور واپس آنے والے کرنٹ میں ذرا سا فرق آتے ہی پہچان لیتا ہے کہ کرنٹ پانی میں لیک ہو رہا ہے",
        "سوئچ اندرونی طور پر کرنٹ کا توازن ناپتا رہتا ہے، ذرا سا کرنٹ باہر نکلتے ہی وہ بجلی بند کر کے جان بچاتا ہے۔"
    ),
    # 7: Incandescent tungsten bulb argon gas
    (
        "Why are traditional glass incandescent lightbulbs filled with inert argon gas rather than plain room air?",
        ["Oxygen in air would instantly oxidize and incinerate the white-hot 2,500°C tungsten filament in seconds", "Argon glows yellow", "Room air is too heavy", "Argon cools the glass"],
        "Oxygen in air would instantly oxidize and incinerate the white-hot 2,500°C tungsten filament in seconds",
        "Tungsten reacts vigorously with atmospheric oxygen at operating temperatures; inert argon prevents oxidation and retards tungsten evaporation.",
        "روایتی پیلے بلب کے اندر عام ہوا کے بجائے نائٹروجن یا آرگن جیسی غیر عامل گیس کیوں بھری جاتی ہے؟",
        ["ہوا کی آکسیجن 2500 ڈگری پر دہکتے ہوئے ٹنگسٹن کے باریک تار کو ایک سیکنڈ میں جلا کر راکھ کر دیتی", "آرگن گیس پیلی چمکتی ہے", "عام ہوا وزنی ہوتی ہے", "شیشے کو ٹھنڈا رکھنے کے لیے"],
        "ہوا کی آکسیجن 2500 ڈگری پر دہکتے ہوئے ٹنگسٹن کے باریک تار کو ایک سیکنڈ میں جلا کر راکھ کر دیتی",
        "آکسیجن کی موجودگی میں سرخ تار فوراً جل کر کٹ جاتا ہے، غیر عامل گیس تار کو جلنے سے محفوظ رکھتی ہے۔"
    ),
    # 8: LED solid state lighting efficiency
    (
        "Why do modern semiconductor LED lightbulbs consume 85% less electrical power than older incandescent filament bulbs for the same brightness?",
        ["Electrons recombine with holes directly emitting visible photons without heating a metal filament to incandescence", "LED bulbs use cold mirrors", "LEDs absorb room heat", "They reflect moonlight"],
        "Electrons recombine with holes directly emitting visible photons without heating a metal filament to incandescence",
        "Electroluminescence converts electrical energy directly into light at the band gap, avoiding incandescent thermal blackbody energy losses.",
        "جدید ایل ای ڈی (LED) بلب اتنی ہی روشنی دینے کے لیے پرانے بلبوں سے 85 فیصد کم بجلی کیوں کھاتے ہیں؟",
        ["سیمی کنڈکٹر چِپ میں الیکٹرانز بغیر تار کو گرم کیے براہ راست روشنی کے فوٹونز خارج کرتے ہیں", "ایل ای ڈی بلب میں آئینے لگے ہوتے ہیں", "وہ کمرے کی گرمی جذب کرتے ہیں", "وہ چاندنی کو لوٹاتے ہیں"],
        "سیمی کنڈکٹر چِپ میں الیکٹرانز بغیر تار کو گرم کیے براہ راست روشنی کے فوٹونز خارج کرتے ہیں",
        "پرانے بلب 90 فیصد بجلی گرمی میں ضائع کرتے تھے جبکہ ایل ای ڈی بجلی کو سیدھا روشنی میں تبدیل کرتی ہے۔"
    ),
    # 9: Air conditioner dehumidification
    (
        "Why does an indoor split-unit air conditioner constantly drip water through a drain hose to the outside on hot summer days?",
        ["Warm humid room air passes over freezing evaporator coils, causing water vapor to condense out of the air", "The refrigerant melts into water", "The outdoor compressor leaks rain", "The AC creates water chemically"],
        "Warm humid room air passes over freezing evaporator coils, causing water vapor to condense out of the air",
        "Cooling air below its local dew point temperature forces saturated water vapor to condense out as liquid droplets on coil fins.",
        "گرمیوں میں کمرے کا ایئر کنڈیشنر (AC) مسلسل باہر پائپ سے پانی کیوں ٹپکاتا رہتا ہے؟",
        ["کمرے کی گرم مرطوب ہوا ٹھنڈی کوائلز سے ٹکرا کر اپنی نمی پانی کے قطروں کی صورت میں گراتی ہے", "فریج کی گیس پانی بن جاتی ہے", "کمپریسر میں بارش کا پانی ہوتا ہے", "اے سی کیمیائی پانی بناتا ہے"],
        "کمرے کی گرم مرطوب ہوا ٹھنڈی کوائلز سے ٹکرا کر اپنی نمی پانی کے قطروں کی صورت میں گراتی ہے",
        "ٹھنڈی دھات سے ٹکراتے ہی ہوا میں موجود آبی بخارات کثیف ہو کر مائع بن جاتے ہیں جس سے کمرے کا حبس ختم ہوتا ہے۔"
    ),
    # 10: Heat pump coefficient of performance COP
    (
        "How can an efficient residential heat pump deliver three times more heat energy into a winter home than the electrical energy it consumes?",
        ["It moves existing thermal heat from outdoor ambient air inside rather than generating heat from scratch through resistance", "It uses miniature nuclear fusion", "It burns indoor dust", "It multiplies electricity"],
        "It moves existing thermal heat from outdoor ambient air inside rather than generating heat from scratch through resistance",
        "Thermodynamic refrigeration cycles transfer heat from cold exterior sinks to warm interior sinks with coefficients of performance exceeding 3.0.",
        "جدید ہیٹ پمپ سردیوں میں جتنی بجلی خرچ کرتا ہے اس سے تین گنا زیادہ گرمی کمرے میں کیسے فراہم کرتا ہے؟",
        ["وہ خود گرمی جلانے کے بجائے باہر کی کھلی ہوا سے حرارت کھینچ کر کمپریسر کے ذریعے اندر منتقل کرتا ہے", "وہ ایٹمی فیوژن استعمال کرتا ہے", "وہ کمرے کی مٹی جلاتا ہے", "وہ بجلی کو ضرب دیتا ہے"],
        "وہ خود گرمی جلانے کے بجائے باہر کی کھلی ہوا سے حرارت کھینچ کر کمپریسر کے ذریعے اندر منتقل کرتا ہے",
        "ہیٹ پمپ حرارت پیدا نہیں کرتا بلکہ فریج کے الٹے اصول پر باہر کی تپش کو اندر پمپ کرتا ہے جس سے زبردست بچت ہوتی ہے۔"
    ),
    # 11: Evaporative swamp cooler dry climates
    (
        "Why do evaporative swamp coolers provide crisp cool air in dry desert climates like Arizona, but fail completely in humid coastal Miami?",
        ["Evaporative cooling requires a large humidity deficit in ambient air to evaporate water and absorb latent heat", "Desert air contains cold minerals", "Miami water is too salty", "Swamp coolers need mountain winds"],
        "Evaporative cooling requires a large humidity deficit in ambient air to evaporate water and absorb latent heat",
        "When ambient relative humidity approaches 100%, wet-bulb temperature equals dry-bulb temperature, halting evaporative enthalpy transfer.",
        "خشک گرم علاقوں میں چلنے والا دیسی واٹر کولر تو خوب ٹھنڈک دیتا ہے مگر ساحلی مرطوب شہروں میں حبس کیوں بڑھا دیتا ہے؟",
        ["پانی تب ہی بخارات بن کر ٹھنڈک پیدا کرتا ہے جب ہوا میں نمی کم ہو، ساحلی ہوا پہلے ہی نمی سے بھری ہوتی ہے", "صحرائی ہوا ٹھنڈی ہوتی ہے", "ساحلی پانی نمکین ہوتا ہے", "کولر کو پہاڑی ہوا چاہیے ہوتی ہے"],
        "پانی تب ہی بخارات بن کر ٹھنڈک پیدا کرتا ہے جب ہوا میں نمی کم ہو، ساحلی ہوا پہلے ہی نمی سے بھری ہوتی ہے",
        "پانی اڑنے سے حرارت جذب ہوتی ہے، ساحلی علاقوں میں ہوا میں پہلے ہی نمی زیادہ ہونے سے پانی اڑتا نہیں بلکہ حبس ہوتا ہے۔"
    ),
    # 12: Mercury barometer Torricellian vacuum
    (
        "Why does a classical glass tube barometer filled with liquid mercury stand at precisely 760 millimeters (29.92 inches) at sea level?",
        ["Atmospheric weight pressing on the open mercury reservoir balances the weight of the mercury column in the sealed vacuum tube", "Mercury boils at 760 mm", "Glass absorbs mercury above that height", "Gravity turns off above 760 mm"],
        "Atmospheric weight pressing on the open mercury reservoir balances the weight of the mercury column in the sealed vacuum tube",
        "Hydrostatic equilibrium equates atmospheric pressure (101.3 kPa) with the weight of a column of mercury (rho * g * h) at 760 mm.",
        "شیشے کی ٹیوب میں بھرا پارہ سمندر کی سطح پر بالکل 760 ملی میٹر کی اونچائی پر آ کر کیوں رک جاتا ہے؟",
        ["باہر کی کھلی ہوا کا دباؤ نچلے پیالے پر دباؤ ڈال کر ٹیوب کے اندر پارے کے کالم کے وزن کو متوازن کر دیتا ہے", "پارہ 760 پر ابلتا ہے", "شیشہ اوپر پارے کو روک لیتا ہے", "اوپر کشش ثقل ختم ہو جاتی ہے"],
        "باہر کی کھلی ہوا کا دباؤ نچلے پیالے پر دباؤ ڈال کر ٹیوب کے اندر پارے کے کالم کے وزن کو متوازن کر دیتا ہے",
        "زمین کی پوری فضا کا دباؤ پارے کو نالی میں اوپر دھکیلتا ہے، 760 ملی میٹر پر پارے کا وزن اور ہوا کا دباؤ برابر ہو جاتے ہیں۔"
    ),
    # 13: Pitot tube dynamic airspeed
    (
        "How does a slender heated pitot tube protruding from the nose cone of an airliner calculate flight airspeed in knots?",
        ["Measuring dynamic ram air pressure compared against static atmospheric ambient pressure ports", "Counting passing air molecules", "Listening to engine roar", "Measuring wind friction on metal"],
        "Measuring dynamic ram air pressure compared against static atmospheric ambient pressure ports",
        "Bernoulli's equation states total pressure equals static pressure plus dynamic pressure (P_total = P_static + 0.5 * rho * V^2).",
        "ہوائی جہاز کی ناک پر لگی باریک نوکدار نالی (پیٹوٹ ٹیوب) پرواز کے دوران جہاز کی درست رفتار کیسے ناپتی ہے؟",
        ["سامنے سے ٹکرانے والی ہوا کے متحرک دباؤ کا سائیڈ کے ساکن دباؤ سے موازنہ کر کے", "ہوا کے مالیکیولز کو گن کر", "انجن کا شور سن کر", "دھات کی رگڑ ناپ کر"],
        "سامنے سے ٹکرانے والی ہوا کے متحرک دباؤ کا سائیڈ کے ساکن دباؤ سے موازنہ کر کے",
        "تیز رفتار سے سامنے آنے والی ہوا کا دباؤ رفتار کے ساتھ بڑھتا ہے، یہ نالی دباؤ کے فرق سے رفتار ناپتی ہے۔"
    ),
    # 14: Aneroid altimeter pressure drop
    (
        "How does a mechanical aneroid altimeter in an airplane cockpit determine altitude above sea level without radio towers?",
        ["A sealed evacuated metal bellows capsule expands as atmospheric air pressure drops with rising altitude", "A laser bounces off ground", "Gravity sensors weigh the plane", "The clock tracks climb time"],
        "A sealed evacuated metal bellows capsule expands as atmospheric air pressure drops with rising altitude",
        "Standard atmospheric barometric pressure decreases exponentially with geometric altitude (~1 inch Hg per 1,000 feet).",
        "ہوائی جہاز کا مکینیکل الٹی میٹر بنا ریڈار کے کیسے بتا دیتا ہے کہ جہاز زمین سے کتنے ہزار فٹ بلندی پر اڑ رہا ہے؟",
        ["اندر موجود ہوا سے خالی دھاتی کیپسول بلندی پر ہوا کا دباؤ کم ہوتے ہی پھیلنے لگتا ہے", "لیزر زمین سے ٹکرا کر آتی ہے", "کشش ثقل کا کانٹا ناپتا ہے", "گھڑی سے وقت دیکھا جاتا ہے"],
        "اندر موجود ہوا سے خالی دھاتی کیپسول بلندی پر ہوا کا دباؤ کم ہوتے ہی پھیلنے لگتا ہے",
        "جوں جوں بلندی بڑھتی ہے ہوا کا بیرونی دباؤ گھٹتا ہے، جس سے اندر کا لچکدار کیپسول پھیل کر ڈائل پر اونچائی دکھاتا ہے۔"
    ),
    # 15: Gyrocompass true north vs magnetic north
    (
        "Why do commercial marine navigation ships rely on spinning gyrocompasses rather than traditional magnetic compasses?",
        ["A motorized spinning gyroscope aligns with Earth's geographic rotational axis (true north), unaffected by hull magnetic fields", "Gyrocompasses work without power", "Magnetic compasses freeze in salt water", "Gyrocompasses float on water"],
        "A motorized spinning gyroscope aligns with Earth's geographic rotational axis (true north), unaffected by hull magnetic fields",
        "Precession caused by Earth's daily axial rotation forces a pendular gyroscope spin axis to stabilize along true geographic meridian lines.",
        "بڑے بحری جہاز قطب نما (کمپاس) کی مقناطیسی سوئی کے بجائے جائرواسکاپک کمپاس پر بھروسا کیوں کرتے ہیں؟",
        ["گھومتا ہوا جائرواسکوپ زمین کے اصل گھومنے کے جغرافیائی قطب شمالی کا پتہ دیتا ہے اور جہاز کے لوہے سے متاثر نہیں ہوتا", "جائرواسکوپ بغیر بجلی کے چلتا ہے", "مقناطیسی سوئی سمندر میں جم جاتی ہے", "وہ پانی پر تیرتا ہے"],
        "گھومتا ہوا جائرواسکوپ زمین کے اصل گھومنے کے جغرافیائی قطب شمالی کا پتہ دیتا ہے اور جہاز کے لوہے سے متاثر نہیں ہوتا",
        "مقناطیسی سوئی جہاز کے لوہے سے غلط رخ بتا سکتی ہے جبکہ گھومتا جائرواسکوپ زمین کے اصل گھماؤ کی سمت سیدھا رہتا ہے۔"
    ),
    # 16: Marine sonar bathymetry
    (
        "How do hydrographic survey research vessels accurately map ocean floor trenches four miles beneath the water surface?",
        ["Transmitting acoustic sonar acoustic sound pings and measuring two-way round-trip echo reflection return time", "Lowering weighted ropes", "Diving with cameras", "Reading GPS ocean waves"],
        "Transmitting acoustic sonar acoustic sound pings and measuring two-way round-trip echo reflection return time",
        "Sound propagates through seawater at ~1,500 m/s; timing acoustic reflection echoes yields depth profiles (Depth = 0.5 * v * t).",
        "سمندری تحقیقاتی جہاز پانی کے نیچے میلوں گہری کھائیوں اور پہاڑوں کا نقشہ کیسے بناتے ہیں؟",
        ["پانی کے نیچے سونار (Sonar) کی آواز کی لہریں بھیج کر اور ان کی بازگشت لوٹنے کا وقت ناپ کر", "رسی سے باٹ لٹکا کر", "غوطہ خوروں کے کیمروں سے", "جی پی ایس لہریں پڑھ کر"],
        "پانی کے نیچے سونار (Sonar) کی آواز کی لہریں بھیج کر اور ان کی بازگشت لوٹنے کا وقت ناپ کر",
        "پانی میں آواز 1500 میٹر فی سیکنڈ سے چلتی ہے، تہہ سے ٹکرا کر لوٹنے والی آواز کے وقت سے گہرائی ناپی جاتی ہے۔"
    ),
    # 17: Radar Doppler storm velocity
    (
        "How can modern Doppler weather radar detect rotating tornado funnel clouds hidden inside heavy rainfall clouds miles away?",
        ["Reflected microwave pulses shift frequency higher or lower depending on whether raindrops are moving toward or away from radar", "Radar senses cloud heat", "Radar measures rain color", "Cameras zoom through rain"],
        "Reflected microwave pulses shift frequency higher or lower depending on whether raindrops are moving toward or away from radar",
        "The Doppler effect compresses frequency (blue shift) for precipitation moving inbound and dilates frequency (red shift) outbound, revealing vortex rotation.",
        "ڈوپلر موسمی ریڈار بارش کے گھنے بادلوں کے اندر چھپے طوفانی بگولے (ٹورنیڈو) کے چکر کا پتہ دور سے کیسے لگا لیتا ہے؟",
        ["بارش کے قطروں سے ٹکرا کر لوٹنے والی لہروں کی فریکوئنسی آگے یا پیچھے حرکت کرنے سے بدل جاتی ہے (ڈوپلر اثر)", "ریڈار بادل کی گرمی ناپتا ہے", "ریڈار بارش کا رنگ دیکھتا ہے", "کیمرہ بادل چیر کر دیکھتا ہے"],
        "بارش کے قطروں سے ٹکرا کر لوٹنے والی لہروں کی فریکوئنسی آگے یا پیچھے حرکت کرنے سے بدل جاتی ہے (ڈوپلر اثر)",
        "ایک طرف آنے والے اور دوسری طرف جانے والے قطروں کی ریڈار لہروں میں فریکوئنسی کا فرق گھومتے بگولے کو فوراً ظاہر کر دیتا ہے۔"
    ),
    # 18: Lidar 3D point cloud
    (
        "How do autonomous self-driving cars perceive pedestrians and obstacles in three dimensions at night without ambient light?",
        ["Pulsing hundreds of thousands of invisible eye-safe infrared laser beams per second to map photon time-of-flight distances", "Using bright searchlights", "Ultrasonic chirps only", "Reading road maps"],
        "Pulsing hundreds of thousands of invisible eye-safe infrared laser beams per second to map photon time-of-flight distances",
        "Time-of-flight LiDAR calculates distance d = c * t / 2 for millions of data points, synthesizing an instant 3D point cloud.",
        "خودکار بغیر ڈرائیور کی کار رات کے گھپ اندھیرے میں پیدل چلنے والوں اور رکاوٹوں کا تھری ڈی ماڈل کیسے بنا لیتی ہے؟",
        ["سیکنڈ میں لاکھوں غیر مرئی لیزر شعاعیں پھینک کر اور ان کے لوٹنے کا وقت ناپ کر فاصلے کا نقشہ بناتی ہے (LiDAR)", "تیز ہیڈ لائٹس جلا کر", "صرف الٹرا ساؤنڈ سیٹیوں سے", "سڑک کے نقشے پڑھ کر"],
        "سیکنڈ میں لاکھوں غیر مرئی لیزر شعاعیں پھینک کر اور ان کے لوٹنے کا وقت ناپ کر فاصلے کا نقشہ بناتی ہے (LiDAR)",
        "لائیڈار لیزر بیمز کے ٹکرا کر واپس آنے کی رفتار سے گاڑی کے ارد گرد ہر چیز کی ساخت اور دوری کا مکمل 3D ماڈل بن جاتا ہے۔"
    ),
    # 19: Quartz watch 32768 Hz piezoelectric
    (
        "Why is a tiny fork-shaped synthetic quartz crystal inside an electronic wristwatch tuned to oscillate at precisely 32,768 Hz?",
        ["32,768 is exactly 2^15, allowing simple binary digital divide-by-two flip-flop circuits to output exactly one pulse per second", "It is the speed of sound in quartz", "Human ears can hear that frequency", "To save battery heat"],
        "32,768 is exactly 2^15, allowing simple binary digital divide-by-two flip-flop circuits to output exactly one pulse per second",
        "Dividing 32,768 by two fifteen sequential times in binary logic yields exactly 1.000 Hz, stepping the second hand precisely.",
        "کوآرٹز گھڑی کے اندر باریک کرسٹل کو سیکنڈ میں ٹھیک 32,768 بار لرزنے کے لیے ہی کیوں بنایا جاتا ہے؟",
        ["کیونکہ 32768 اصل میں 2 کی طاقت 15 ہے، جسے بائنری سرکٹ 15 بار آدھا کر کے بالکل ایک سیکنڈ کا درست سگنل بنا لیتا ہے", "یہ کوآرٹز میں آواز کی رفتار ہے", "انسان اس فریکوئنسی کو سن سکتا ہے", "بیٹری بچانے کے لیے"],
        "کیونکہ 32768 اصل میں 2 کی طاقت 15 ہے، جسے بائنری سرکٹ 15 بار آدھا کر کے بالکل ایک سیکنڈ کا درست سگنل بنا لیتا ہے",
        "ڈیجیٹل کمپیوٹر کے بائنری سرکٹ میں 32768 کو بار بار دو پر تقسیم کرنے سے آخر میں ٹھیک 1 سیکنڈ کی نبض حاصل ہوتی ہے۔"
    ),
    # 20: Polarized sunglasses horizontal glare
    (
        "Why do polarized sunglasses eliminate blinding white glare from wet asphalt roadways and lake surfaces far better than standard tinted glass?",
        ["Light reflected off horizontal dielectric surfaces is horizontally polarized; vertical polarization filters block horizontal waves", "Polarized lenses contain lead", "They reflect all visible light", "They darken pupil size"],
        "Light reflected off horizontal dielectric surfaces is horizontally polarized; vertical polarization filters block horizontal waves",
        "Brewster's angle reflection preferentially polarizes electric field vectors parallel to the surface plane (horizontal); vertical polymer alignments block it.",
        "پولرائزڈ دھوپ کے چشمے سڑک اور جھیل کے پانی سے آنکھوں کو چندھیانے والی چمک کو اتنی صفائی سے کیسے ختم کر دیتے ہیں؟",
        ["ہموار سطح سے لوٹنے والی روشنی افقی لہروں میں بدل جاتی ہے، چشمے کا عمودی فلٹر ان افقی لہروں کو مکمل روک دیتا ہے", "چشمے میں سیسہ ملا ہوتا ہے", "وہ تمام روشنی منعکس کرتے ہیں", "وہ آنکھ کی پتلی سکیڑتے ہیں"],
        "ہموار سطح سے لوٹنے والی روشنی افقی لہروں میں بدل جاتی ہے، چشمے کا عمودی فلٹر ان افقی لہروں کو مکمل روک دیتا ہے",
        "پانی اور سڑک سے ٹکرا کر روشنی کی لہریں ایک رخ میں سیدھی ہو جاتی ہیں، چشمے کی جالی ان لہروں کو بلاک کر دیتی ہے۔"
    ),
    # 21: Camera aperture f-stop depth of field
    (
        "Why does stopping down a camera lens aperture from f/1.8 to f/16 make both a nearby flower and distant mountains sharply in focus?",
        ["A smaller physical aperture narrows the cone of light rays, shrinking the circle of confusion and expanding depth of field", "It increases camera shutter speed", "It brightens the image sensor", "It magnifies distant objects"],
        "A smaller physical aperture narrows the cone of light rays, shrinking the circle of confusion and expanding depth of field",
        "Narrower ray cones entering the lens diverge more gradually before and behind the focal plane, expanding the acceptable depth of field.",
        "کیمرے کے لینز کا اپرچر f/1.8 سے کم کر کے f/16 کرنے پر قریب کا پھول اور دور کا پہاڑ دونوں ایک ساتھ فوکس میں کیوں آ جاتے ہیں؟",
        ["اپرچر کا سوراخ چھوٹا ہونے سے روشنی کی مخروطی لہریں باریک ہو جاتی ہیں جس سے فوکس کا گھیراؤ (Depth of Field) وسیع ہو جاتا ہے", "شٹر اسپیڈ تیز ہو جاتی ہے", "سینسر پر روشنی بڑھ جاتی ہے", "دور کی چیز بڑی ہو جاتی ہے"],
        "اپرچر کا سوراخ چھوٹا ہونے سے روشنی کی مخروطی لہریں باریک ہو جاتی ہیں جس سے فوکس کا گھیراؤ (Depth of Field) وسیع ہو جاتا ہے",
        "چھوٹے سوراخ سے گزرنے والی روشنی کی شعاعیں سیدھی گزرتی ہیں جس سے سامنے اور پس منظر دونوں پر نفاست آ جاتی ہے۔"
    ),
    # 22: Binocular Porro prisms erect image
    (
        "Why do standard marine binoculars incorporate a pair of glass Porro prisms between objective lenses and eyepieces?",
        ["Objective lenses project an upside-down, inverted mirror image; internal prisms fold and flip the image right-side up", "Prisms make binoculars waterproof", "Prisms zoom the image by 100x", "Prisms filter out night darkness"],
        "Objective lenses project an upside-down, inverted mirror image; internal prisms fold and flip the image right-side up",
        "Convex objective lenses invert images in both horizontal and vertical axes; two orthogonal total-internal-reflection Porro prisms invert them erect.",
        "دوربین کے اندر شیشے کے دائیں بائیں پرزم کیوں لگائے جاتے ہیں؟",
        ["سامنے کا لینز تصویر کو الٹا دکھاتا ہے، اندرونی پرزم روشنی کو منعکس کر کے تصویر کو دوبارہ سیدھا اور درست رخ کر دیتے ہیں", "دوربین کو واٹر پروف رکھنے کے لیے", "تصویر کو سو گنا بڑا کرنے کے لیے", "رات کا اندھیرا دور کرنے کے لیے"],
        "سامنے کا لینز تصویر کو الٹا دکھاتا ہے، اندرونی پرزم روشنی کو منعکس کر کے تصویر کو دوبارہ سیدھا اور درست رخ کر دیتے ہیں",
        "محدب عدسہ تصویر کو الٹا کر دیتا ہے، پرزم کی بدولت تصویر کے الٹے پن کو پلٹ کر سیدھا کیا جاتا ہے تاکہ دیکھنے والے کو درست نظر آئے۔"
    ),
    # 23: Periscope two 45 degree mirrors
    (
        "How can a submarine crew observe cargo ships on the ocean surface while submerged thirty feet below the waves?",
        ["Two flat mirrors aligned parallel at 45-degree angles bounce surface light down a vertical tube into the viewer's eye", "A glass tube reaches up", "Magnets guide photons", "Laser beams penetrate water"],
        "Two flat mirrors aligned parallel at 45-degree angles bounce surface light down a vertical tube into the viewer's eye",
        "The top mirror reflects horizontal surface light 90 degrees downward through the tube; the bottom mirror reflects it 90 degrees horizontally to the eye.",
        "سمندر کی گہرائی میں ڈوبی آبدوز کی پیری اسکوپ اوپر تیرتے جہازوں کو کیسے دیکھتی ہے؟",
        ["دو آئینے 45 درجے کے زاویے پر آمنے سامنے لگے ہوتے ہیں جو اوپر کی روشنی کو 90 ڈگری نیچے آنکھ تک موڑ دیتے ہیں", "شیشے کا پائپ اوپر جاتا ہے", "مقناطیس روشنی لاتے ہیں", "لیزر پانی چیرتی ہے"],
        "دو آئینے 45 درجے کے زاویے پر آمنے سامنے لگے ہوتے ہیں جو اوپر کی روشنی کو 90 ڈگری نیچے آنکھ تک موڑ دیتے ہیں",
        "اوپر کا آئینہ روشنی کو سیدھا نیچے بھیجتا ہے اور نیچے کا آئینہ اسے ملاح کی آنکھ کے سامنے موڑ کر منظر واضح کر دیتا ہے۔"
    ),
    # 24: Kaleidoscope hexagonal symmetry
    (
        "What optical arrangement inside a toy kaleidoscope transforms loose colored glass beads into endless repeating symmetric mandalas?",
        ["Three long flat mirrors joined in an equilateral triangle reflect beads across multiple 60-degree symmetry planes", "A digital kaleidoscope projector", "Magnifying glass lenses", "Prisms splitting white light"],
        "Three long flat mirrors joined in an equilateral triangle reflect beads across multiple 60-degree symmetry planes",
        "Mirrors joined at 60-degree angles create infinite virtual reflections that tile the circular field of view into hexagonal floral symmetries.",
        "کیلیڈواسکوپ کھلونے کے اندر رنگین موتیوں کے دانے گھمانے پر اتنے خوبصورت اور متناسب ڈیزائن کیسے بنتے ہیں؟",
        ["تین آئینے مثلث کی شکل میں جڑے ہوتے ہیں جو 60 ڈگری پر عکس کو بار بار دہرا کر چھ کونوں والے شاہکار بناتے ہیں", "اندر چھوٹا پروجیکٹر لگا ہوتا ہے", "عدسے روشنی موڑتے ہیں", "پرزم رنگ الگ کرتے ہیں"],
        "تین آئینے مثلث کی شکل میں جڑے ہوتے ہیں جو 60 ڈگری پر عکس کو بار بار دہرا کر چھ کونوں والے شاہکار بناتے ہیں",
        "تینوں آئینے ایک دوسرے کے اندر عکس کا لامتناہی سلسلہ بنا دیتے ہیں، جس سے معمولی کنکریاں بھی ہندسی ڈیزائن بن جاتی ہیں۔"
    ),
    # 25: Convex security mirror wide angle
    (
        "Why do parking garages and convenience stores mount curved convex mirrors at blind corners rather than flat mirrors?",
        ["Convex mirrors diverge light rays, compressing a wide-angle field of view into an upright virtual image", "Convex mirrors magnify small details", "Convex mirrors illuminate dark corners", "They are unbreakable"],
        "Convex mirrors diverge light rays, compressing a wide-angle field of view into an upright virtual image",
        "Reflecting off a convex spherical surface diverges incident rays, forming a diminished, upright virtual image covering a panoramic wide angle.",
        "دکانوں اور پارکنگ کے اندھے موڑ پر عام شیشے کے بجائے باہر کو ابھرا ہوا محدب (Convex) آئینہ کیوں لگایا جاتا ہے؟",
        ["باہر کو ابھرا ہوا آئینہ دور دور کے وسیع رقبے کو سمیٹ کر چھوٹے فریم میں پورا پینورامک منظر دکھا دیتا ہے", "وہ چیزوں کو بڑا کر کے دکھاتا ہے", "وہ اندھیرے میں روشنی دیتا ہے", "وہ کبھی نہیں ٹوٹتا"],
        "باہر کو ابھرا ہوا آئینہ دور دور کے وسیع رقبے کو سمیٹ کر چھوٹے فریم میں پورا پینورامک منظر دکھا دیتا ہے",
        "محدب آئینے کا پھیلاؤ زیادہ ہوتا ہے جس سے ڈرائیور یا دکاندار ایک ہی نظر میں پورے ہال اور موڑ کو دیکھ سکتا ہے۔"
    ),
    # 26: Stained glass colloidal gold nanoparticles
    (
        "Why have medieval cathedral stained-glass windows retained their vibrant ruby-red coloration for over eight hundred years without fading?",
        ["Colloidal gold and metal nanoparticles suspended inside molten silica glass exhibit localized surface plasmon resonance", "They are painted with oil varnishes", "Red sunlight permanently stains glass", "Stained glass produces its own light"],
        "Colloidal gold and metal nanoparticles suspended inside molten silica glass exhibit localized surface plasmon resonance",
        "Nanoscale gold clusters embedded in the amorphous glass matrix scatter and absorb specific wavelengths through plasmon resonance, immune to UV fading.",
        "قدیم گرجا گھروں کے سرخ شیشے (سٹینڈ گلاس) آٹھ سو سال گزرنے کے بعد بھی بالکل نئے جیسے چمکدار سرخ کیوں رہتے ہیں؟",
        ["پگھلے شیشے کے اندر سونے اور دھاتوں کے نینو ذرات شامل کیے گئے تھے جو الٹرا وائلٹ دھوپ سے کبھی مدہم نہیں ہوتے", "ان پر آئل پینٹ کیا گیا تھا", "دھوپ نے شیشہ رنگ دیا تھا", "شیشہ خود روشنی خارج کرتا ہے"],
        "پگھلے شیشے کے اندر سونے اور دھاتوں کے نینو ذرات شامل کیے گئے تھے جو الٹرا وائلٹ دھوپ سے کبھی مدہم نہیں ہوتے",
        "عام رنگ دھوپ سے اڑ جاتے ہیں مگر شیشے کے اندر گھلا ہوا نینو سونا روشنی کے خاص طول موج کو تاحیات چمکدار رکھتا ہے۔"
    ),
    # 27: Two way mirror interrogation room contrast
    (
        "How can police detectives stand in a dark observation booth and watch suspects through an ordinary two-way mirror without being seen?",
        ["A semi-reflective thin aluminum coating reflects 50% and transmits 50%; bright interrogation lighting drowns out the dark booth", "Detectives wear invisible suits", "The glass is an electronic monitor", "Light travels in only one direction"],
        "A semi-reflective thin aluminum coating reflects 50% and transmits 50%; bright interrogation lighting drowns out the dark booth",
        "Photons transmit equally in both directions; the intense luminance ratio (100:1) masks the faint light emerging from the pitch-dark viewing booth.",
        "پولیس کے تفتیشی کمرے کی دیوار کا شیشہ ملزم کو تو آئینہ لگتا ہے مگر پیچھے کھڑے افسران کو شفاف کھڑکی کیوں لگتا ہے؟",
        ["شیشہ آدھی روشنی لوٹاتا ہے، ملزم کا کمرہ تیز روشن اور افسران کا کمرہ گھپ اندھیرا ہونے سے اندر کا عکس چھپ جاتا ہے", "افسران جادو کا لباس پہنتے ہیں", "شیشہ کمپیوٹر کی اسکرین ہوتا ہے", "روشنی صرف ایک طرف چلتی ہے"],
        "شیشہ آدھی روشنی لوٹاتا ہے، ملزم کا کمرہ تیز روشن اور افسران کا کمرہ گھپ اندھیرا ہونے سے اندر کا عکس چھپ جاتا ہے",
        "روشنی کا فرق کھیل بناتا ہے: تیز روشنی والے کو اپنا ہی عکس نظر آتا ہے، جبکہ اندھیرے میں کھڑا شخص صاف پار دیکھ لیتا ہے۔"
    ),
    # 28: Laser beam collimation coherence
    (
        "Why can a handheld green laser pointer project a tight pinpoint dot onto a skyscraper a mile away without scattering like a flashlight?",
        ["Laser light is monochromatic and coherent, traveling in spatial phase as parallel collimated electromagnetic waves", "Lasers are hotter than flashlights", "Flashlights use dead batteries", "Laser beams are magnetic"],
        "Laser light is monochromatic and coherent, traveling in spatial phase as parallel collimated electromagnetic waves",
        "Stimulated emission in an optical resonator cavity forces all emitted photons into identical phase, frequency, and directional vectors.",
        "عام ٹارچ کی روشنی تو چند قدم پر پھیل جاتی ہے مگر لیزر پوائنٹر کی باریک کرن میل دور عمارت پر بھی ایک باریک نقطہ کیسے رہتی ہے؟",
        ["لیزر کی روشنی ایک ہی ویو لینتھ کی باہم جڑی ہوئی (کوہیرنٹ) متوازی لہروں پر مشتمل ہوتی ہے جو پھیلتی نہیں ہیں", "لیزر ٹارچ سے زیادہ گرم ہوتی ہے", "ٹارچ کا سیل کمزور ہوتا ہے", "لیزر شعاع مقناطیسی ہوتی ہے"],
        "لیزر کی روشنی ایک ہی ویو لینتھ کی باہم جڑی ہوئی (کوہیرنٹ) متوازی لہروں پر مشتمل ہوتی ہے جو پھیلتی نہیں ہیں",
        "لیزر کے تمام فوٹونز ایک ہی قطار اور ایک ہی رخ میں یکسو ہو کر سفر کرتے ہیں جس سے ان کا پھیلاؤ نہ ہونے کے برابر ہوتا ہے۔"
    ),
    # 29: Propeller cavitation damage
    (
        "Why do high-speed marine ship propellers develop pitted mechanical erosion craters on their bronze blade surfaces over time?",
        ["Extreme hydrodynamic low pressure vaporizes water into bubbles that violently collapse, releasing destructive microjets", "Salt dissolves bronze chemically", "Sharks bite the propeller blades", "Propellers strike floating driftwood"],
        "Extreme hydrodynamic low pressure vaporizes water into bubbles that violently collapse, releasing destructive microjets",
        "Cavitation bubbles form when local static fluid pressure drops below vapor pressure; their subsequent collapse generates localized shock pressures exceeding 1 GPa.",
        "تیز رفتار بحری جہاز کے کانسی کے پنکھے (پروپیلر) کے پروں پر وقت کے ساتھ ساتھ چھوٹے چھوٹے گڑھے اور نشانات کیوں پڑ جاتے ہیں؟",
        ["پانی کے شدید کم دباؤ سے بننے والے ویکیوم بلبلے پھٹ کر فولاد توڑنے والے مائیکرو جیٹس پیدا کرتے ہیں (کیویٹیشن)", "نمک کانسی کو پگھلا دیتا ہے", "شارک مچھلیاں دانت مارتی ہیں", "لکڑیاں ٹکراتی ہیں"],
        "پانی کے شدید کم دباؤ سے بننے والے ویکیوم بلبلے پھٹ کر فولاد توڑنے والے مائیکرو جیٹس پیدا کرتے ہیں (کیویٹیشن)",
        "تیز گھومنے سے بننے والے بخاراتی بلبلے جب واپس پھٹتے ہیں تو ان کا دھماکہ دھات کی سطح سے باریک ذرات اکھاڑ پھینکتا ہے۔"
    ),
    # 30: Mount Everest discovery
    (
        "Before Mount Everest was officially surveyed and measured by the Great Trigonometrical Survey in 1856, what was the highest mountain on Earth?",
        ["Mount Everest (it was still physically the highest mountain, even before human discovery)", "Mount Kilimanjaro", "K2", "Mount Blanc"],
        "Mount Everest (it was still physically the highest mountain, even before human discovery)",
        "Geological physical elevation exists independently of human cartographic recognition or measurement.",
        "1856ء میں سائنسدانوں کے ماؤنٹ ایورسٹ کو دریافت کرنے اور ناپنے سے پہلے، دنیا کا سب سے اونچا پہاڑ کون سا تھا؟",
        ["ماؤنٹ ایورسٹ ہی تھا (کیونکہ وہ انسان کے جاننے سے پہلے بھی دنیا کا بلند ترین پہاڑ موجود تھا)", "کے ٹو", "کوہ ہمالیہ کا کینچنجنگا", "کلیمنجارو"],
        "ماؤنٹ ایورسٹ ہی تھا (کیونکہ وہ انسان کے جاننے سے پہلے بھی دنیا کا بلند ترین پہاڑ موجود تھا)",
        "انسان نے اس کی بلندی بعد میں ناپی مگر کائنات کی حقیقت کے اعتبار سے وہ پہلے بھی دنیا کی بلند ترین چوٹی تھا۔"
    )
]

print(f"Normal Part 1 loaded {len(ITEMS)} items.")
