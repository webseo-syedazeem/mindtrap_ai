# -*- coding: utf-8 -*-
"""
Fresh Normal tier items (35 distinct items to complete exactly 400).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why do owls fly in virtually total acoustic silence without making any fluttering wing sound?",
        ["Serrated leading-edge feathers and velvety down break up air turbulence into microscopic micro-vortices", "Owls fly with zero air resistance", "Owls only glide downward", "Owl wings are made of hollow bones"],
        "Serrated leading-edge feathers and velvety down break up air turbulence into microscopic micro-vortices",
        "Serrated comb-like structures on the flight feathers break large acoustic vortices into tiny eddies, suppressing audible aerodynamic flap noise.",
        "الّو رات کے اندھیرے میں پر پھڑپھڑائے بغیر بالکل خاموشی سے پرواز کیسے کر لیتا ہے کہ شکار کو بھنک بھی نہیں پڑتی؟",
        ["اس کے پروں کے اگلے کناروں پر کنگھی نما دندانے ہوا کے گرداب کو باریک لہروں میں توڑ کر شور ختم کر دیتے ہیں", "الّو ہوا کی رکاوٹ کے بغیر اڑتا ہے", "الّو صرف نیچے کی طرف گلائیڈ کرتا ہے", "الّو کے پر کھوکھلے ہوتے ہیں"],
        "اس کے پروں کے اگلے کناروں پر کنگھی نما دندانے ہوا کے گرداب کو باریک لہروں میں توڑ کر شور ختم کر دیتے ہیں",
        "عام پرندوں کے پر ہوا کو کاٹتے ہوئے پھڑپھڑاہٹ پیدا کرتے ہیں، جبکہ الّو کے پروں کا مخملی اور دندانے دار حاشیہ ہوا کے دباؤ کو خاموش بکھیر دیتا ہے۔"
    ),
    (
        "Why does a quartz wristwatch keep exceptionally precise time over months on a tiny coin battery?",
        ["A tiny piezoelectric quartz tuning fork vibrates at exactly 32,768 Hz when voltage is applied, providing an ultrastable oscillator", "The battery contains atomic clock gears", "Quartz absorbs planetary rotation", "The watch hands use solar magnetism"],
        "A tiny piezoelectric quartz tuning fork vibrates at exactly 32,768 Hz when voltage is applied, providing an ultrastable oscillator",
        "Piezoelectric quartz oscillates at 2^15 = 32,768 Hz. A digital binary circuit divides this frequency 15 times to generate precisely one pulse per second.",
        "کوارٹز (Quartz) گھڑی ایک چھوٹے سے بٹن سیل پر مہینوں تک ایک سیکنڈ کا بھی فرق پڑے بغیر بالکل درست وقت کیسے دکھاتی ہے؟",
        ["بجلی ملنے پر کوارٹز کا باریک کرسٹل بالکل 32,768 بار فی سیکنڈ تھرتھراتا ہے جو گھڑی کو انتہائی مستحکم نبض دیتا ہے", "بیٹری میں ایٹمی گیئرز ہوتے ہیں", "کوارٹز زمین کی گردش محسوس کرتا ہے", "سوئیاں شمسی مقناطیس پر چلتی ہیں"],
        "بجلی ملنے پر کوارٹز کا باریک کرسٹل بالکل 32,768 بار فی سیکنڈ تھرتھراتا ہے جو گھڑی کو انتہائی مستحکم نبض دیتا ہے",
        "کوارٹز کرسٹل بجلی کے دباؤ سے سیکنڈ میں عین 32,768 بار وائبریٹ کرتا ہے۔ چپ اس فریکوئنسی کو 15 بار آدھا کر کے ہر سیکنڈ پر عین ایک سیکنڈ کا سگنل بناتی ہے۔"
    ),
    (
        "Why are thick bass piano strings wrapped with spiral copper wire rather than made of a single thick solid steel rod?",
        ["Wrapping adds linear mass density without increasing bending stiffness, maintaining harmonious musical pitch and tone", "Copper is cheaper than steel", "Solid steel strings cannot be tuned", "Copper conducts sound faster"],
        "Wrapping adds linear mass density without increasing bending stiffness, maintaining harmonious musical pitch and tone",
        "A solid steel wire of equal mass would be excessively stiff, causing severe inharmonicity (sharp overtones); winding copper provides mass while preserving flexibility.",
        "پیانو کی نچلی بھاری تاروں (Bass strings) پر تانبے کے باریک تار کو اسپرنگ کی طرح کیوں لپیٹا جاتا ہے بجائے اس کے کہ موٹا لوہا استعمال کیا جائے؟",
        ["تار لپیٹنے سے وزن بڑھ جاتا ہے مگر تار کی لچک برقرار رہتی ہے جس سے سر بالکل میٹھا اور درست نکلتا ہے", "تانبا لوہے سے سستا ہوتا ہے", "موٹا لوہا ٹیون نہیں ہو سکتا", "تانبا آواز تیز چلاتا ہے"],
        "تار لپیٹنے سے وزن بڑھ جاتا ہے مگر تار کی لچک برقرار رہتی ہے جس سے سر بالکل میٹھا اور درست نکلتا ہے",
        "اگر اتنا ہی وزنی موٹا سریا لگایا جائے تو وہ سخت ہو جائے گا جس سے آواز بے سری ہو جائے گی۔ باریک تانبے کا کوائل لچک برقرار رکھتے ہوئے مطلوبہ بھاری پن دیتا ہے۔"
    ),
    (
        "Why does a falling mercury barometer reading indicate that foul, stormy weather is approaching?",
        ["Low barometric pressure signals a rising convective column of warm, moist air where clouds and precipitation form", "Rain weighs down the air column", "Mercury evaporates during storms", "Atmospheric air turns into ozone"],
        "Low barometric pressure signals a rising convective column of warm, moist air where clouds and precipitation form",
        "A drop in surface pressure indicates a cyclone or low-pressure trough, which draws surrounding winds inward and drives upward convective storm clouds.",
        "بیرومیٹر (Barometer) میں پارے کی سطح کا اچانک گرنا طوفان اور بارش کے آنے کی نشانی کیوں مانا جاتا ہے؟",
        ["ہوا کا کم دباؤ اس بات کا ثبوت ہوتا ہے کہ گرم مرطوب ہوا اوپر اٹھ رہی ہے جو بادلوں اور آندھی کو جنم دیتی ہے", "بارش ہوا کو بھاری کر دیتی ہے", "طوفان میں پارہ اڑ جاتا ہے", "ہوا اوزون بن جاتی ہے"],
        "ہوا کا کم دباؤ اس بات کا ثبوت ہوتا ہے کہ گرم مرطوب ہوا اوپر اٹھ رہی ہے جو بادلوں اور آندھی کو جنم دیتی ہے",
        "جب فضا کا دباؤ گرتا ہے تو چاروں طرف کی ہوائیں اس نچلے دباؤ کے خلا کو بھرنے کے لیے تیزی سے دوڑتی ہیں اور اٹھتی ہوئی ہوا بادل اور بارش لاتی ہے۔"
    ),
    (
        "Why do natural winding rivers naturally develop looping bends (meanders) rather than flowing in a straight line over flat plains?",
        ["Water flows fastest around the outer river bend, eroding the outer bank while depositing sediment on the slow inner bend (helical flow)", "Tree roots divert river paths", "Earthquakes curve riverbeds", "Fish nests block straight currents"],
        "Water flows fastest around the outer river bend, eroding the outer bank while depositing sediment on the slow inner bend (helical flow)",
        "Secondary helical flow causes cross-channel transport: the outer bank experiences centrifugal erosion (cut bank), while the inner bank accumulates point-bar silt.",
        "میدانی علاقوں میں بہنے والے قدرتی دریا سیدھے بہنے کی بجائے سانپ کی طرح بل کھاتے ہوئے (Meanders) کیوں ہو جاتے ہیں؟",
        ["موڑ کے بیرونی کنارے پر پانی تیز بہہ کر مٹی کاٹتا ہے اور اندرونی کنارے پر مٹی جماتا ہے جس سے موڑ مزید گہرا ہوتا جاتا ہے", "درختوں کی جڑیں دریا کا رخ موڑتی ہیں", "زلزلے دریا کو ٹیڑھا کرتے ہیں", "مچھلیوں کے گھونسلے راستے روکتے ہیں"],
        "موڑ کے بیرونی کنارے پر پانی تیز بہہ کر مٹی کاٹتا ہے اور اندرونی کنارے پر مٹی جماتا ہے جس سے موڑ مزید گہرا ہوتا جاتا ہے",
        "ہلکا سا موڑ بنتے ہی مرکز گریز قوت بیرونی دیوار کو کاٹنا شروع کر دیتی ہے جبکہ اندرونی کنارے پر ریت جمع ہوتی رہتی ہے، جس سے دریا کا راستہ مسلسل بل کھاتا جاتا ہے۔"
    ),
    (
        "Why do deep-sea creatures living thousands of feet under extreme water pressure survive without being squashed flat?",
        ["Their internal fluid and cellular hydrostatic pressure matches external water pressure exactly, with no air-filled cavities to compress", "Their skeletons are made of pure titanium", "They have buoyant bladders made of steel", "Water pressure is zero at the bottom"],
        "Their internal fluid and cellular hydrostatic pressure matches external water pressure exactly, with no air-filled cavities to compress",
        "Because water and cell tissues are largely incompressible, equal internal and external hydrostatic pressure prevents tissue deformation.",
        "سمندر کی ہزاروں فٹ گہرائی میں جہاں پانی کا لاکھوں ٹن دباؤ ہوتا ہے، وہاں پائی جانے والی نازک مچھلیاں پچکنے سے کیسے محفوظ رہتی ہیں؟",
        ["ان کے خلیات کا اندرونی مائع بیرونی پانی کے دباؤ کے بالکل برابر ہوتا ہے اور ان میں کوئی ہوا کی خالی تھیلی نہیں ہوتی", "ان کی ہڈیاں ٹائٹینیم کی بنی ہوتی ہیں", "ان کے اندر لوہے کے غبارے ہوتے ہیں", "سمندر کی تہہ میں دباؤ ختم ہو جاتا ہے"],
        "ان کے خلیات کا اندرونی مائع بیرونی پانی کے دباؤ کے بالکل برابر ہوتا ہے اور ان میں کوئی ہوا کی خالی تھیلی نہیں ہوتی",
        "پانی مائع ہونے کی وجہ سے دبتا نہیں ہے۔ گہرے سمندر کے جانداروں کے جسم کے اندر کا مائع بیرونی دباؤ کے عین برابر ہوتا ہے، اس لیے وہ بغیر کسی تکلیف کے تیرتے ہیں۔"
    ),
    (
        "Why must oceanic great white sharks swim continuously forward without ever stopping, even while resting?",
        ["They rely on obligate ram ventilation to push oxygenated water across their gills, lacking muscular pumping mechanisms", "If they stop, they float to space", "Their blood freezes when motionless", "Sharks have no tail fins"],
        "They rely on obligate ram ventilation to push oxygenated water across their gills, lacking muscular pumping mechanisms",
        "Ram-ventilating elasmobranchs cannot pump water via buccal muscles; halting forward motion halts water flow across gill lamellae, causing suffocation.",
        "سمندری شارک مچھلی کو سوتے یا آرام کرتے وقت بھی مسلسل آگے کی طرف تیرتے کیوں رہنا پڑتا ہے؟",
        ["ان کے گلپھڑوں میں پانی پمپ کرنے والے پٹھے نہیں ہوتے، سانس لینے کے لیے تیرتے ہوئے پانی کو گلپھڑوں سے گزارنا لازمی ہوتا ہے (Ram ventilation)", "رکنے پر وہ ہوا میں اڑ جائیں گی", "ساکن رہنے سے ان کا خون جم جاتا ہے", "شارک کے پاس دم نہیں ہوتی"],
        "ان کے گلپھڑوں میں پانی پمپ کرنے والے پٹھے نہیں ہوتے، سانس لینے کے لیے تیرتے ہوئے پانی کو گلپھڑوں سے گزارنا لازمی ہوتا ہے (Ram ventilation)",
        "شارک مچھلی منہ سے پانی نہیں چوس سکتی۔ جب وہ آگے تیرتی ہے تو منہ سے داخل ہونے والا سمندری پانی خود بخود گلپھڑوں سے ٹکرا کر خون کو آکسیجن دیتا ہے۔"
    ),
    (
        "Why do bats navigating in total pitch darkness never collide with thin fishing wires strung across a room?",
        ["They emit high-frequency ultrasonic clicks (20-100 kHz) and process tiny Doppler echo delays into high-resolution 3D acoustic imagery", "Bats have night vision infrared eyes", "Wires reflect magnetic fields", "Bats feel air currents with their fur"],
        "They emit high-frequency ultrasonic clicks (20-100 kHz) and process tiny Doppler echo delays into high-resolution 3D acoustic imagery",
        "Laryngeal echolocation pulses have millimeter-scale acoustic wavelengths, allowing the bat's auditory cortex to reconstruct fine obstacles.",
        "چمگادڑ گھپ اندھیرے میں اڑتے ہوئے کمرے میں تنے ہوئے بال جتنے باریک تار سے بھی ٹکرائے بغیر کیسے بچ نکلتی ہے؟",
        ["وہ منہ سے الٹراسونک صوتی لہریں نکال کر ان کی بازگشت (Echo) سے ملی میٹر کے فاصلے تک کا تھری ڈی صوتی نقشہ بنا لیتی ہے", "چمگادڑ کی آنکھوں میں انفراریڈ نظر ہوتی ہے", "تار مقناطیسی لہریں خارج کرتا ہے", "چمگادڑ کھال کے بالوں سے ہوا ناپتی ہے"],
        "وہ منہ سے الٹراسونک صوتی لہریں نکال کر ان کی بازگشت (Echo) سے ملی میٹر کے فاصلے تک کا تھری ڈی صوتی نقشہ بنا لیتی ہے",
        "چمگادڑ انسان کے سننے سے کہیں اوپر کی آوازیں نکالتی ہے۔ تار سے ٹکرا کر لوٹنے والی لہر کے وقت اور سمت سے وہ تار کی صحیح موٹائی اور فاصلہ بھانپ لیتی ہے۔"
    ),
    (
        "Why does a carbon-14 dating test determine the age of ancient wooden artifacts accurately, but fails completely on a stone axe of the same age?",
        ["Carbon-14 is only absorbed by living organisms through atmospheric carbon exchange; rocks contain inorganic minerals without biological carbon cycles", "Stone destroys radioisotopes", "Wood absorbs uranium from soil", "Rocks have no atomic half-life"],
        "Carbon-14 is only absorbed by living organisms through atmospheric carbon exchange; rocks contain inorganic minerals without biological carbon cycles",
        "C-14 decays with a 5,730-year half-life; plants assimilate it during photosynthesis. Stone minerals formed millions of years prior via geological non-atmospheric processes.",
        "ریڈیو کاربن ڈیٹنگ (Carbon-14) لکڑی یا ہڈی کے قدیم برتن کی عمر تو بتا دیتی ہے مگر اسی زمانے کی بنی پتھر کی کلہاڑی کی عمر کیوں نہیں بتا سکتی؟",
        ["کاربن-14 صرف جاندار اجسام خوراک اور سانس کے ذریعے جذب کرتے ہیں، پتھروں میں نامیاتی کاربن کا تبادلہ نہیں ہوتا", "پتھر تابکاری کو ختم کر دیتا ہے", "لکڑی مٹی سے یورینیم چوستی ہے", "پتھروں کی کوئی ہاف لائف نہیں ہوتی"],
        "کاربن-14 صرف جاندار اجسام خوراک اور سانس کے ذریعے جذب کرتے ہیں، پتھروں میں نامیاتی کاربن کا تبادلہ نہیں ہوتا",
        "کاربن 14 فضا سے پودوں اور لکڑی میں شامل ہوتی ہے۔ مرنے کے بعد اس کی بتدریج کمی سے عمر کا اندازہ ہوتا ہے۔ پتھر چونکہ کبھی جاندار نہیں تھا اس لیے اس میں یہ کاربن نہیں ہوتی۔"
    ),
    (
        "In forensic ballistics, how do investigators prove that two fired bullets came from the exact same rifle barrel?",
        ["Microscopic striation toolmarks (lands and grooves) impressed onto the soft bullet jacket match with unique microscopic individual characteristics", "Bullets share identical serial numbers", "Both bullets weigh exactly zero grams", "Gunpowder chemical formula is unique per bullet"],
        "Microscopic striation toolmarks (lands and grooves) impressed onto the soft bullet jacket match with unique microscopic individual characteristics",
        "Rifling broaches leave microscopic toolmark imperfections in the barrel steel; these unique scratches engrave matching striations onto every bullet jacket.",
        "فرانزک تفتیش میں ماہرین کیسے ثابت کرتے ہیں کہ واردات میں ملنے والی دو گولیاں عین ایک ہی بندوق سے فائر کی گئی تھیں؟",
        ["بندوق کی نالی کے اندرونی گھماؤ دار کٹاؤ (Rifling grooves) گولی پر خوردبینی نشانات چھوڑتے ہیں جو ہر بندوق کے لیے منفرد ہوتے ہیں", "گولیوں پر ایک جیسا سیریل نمبر چھپا ہوتا ہے", "دونوں گولیوں کا وزن صفر ہوتا ہے", "ہر گولی کے بارود کا کیمیکل منفرد ہوتا ہے"],
        "بندوق کی نالی کے اندرونی گھماؤ دار کٹاؤ (Rifling grooves) گولی پر خوردبینی نشانات چھوڑتے ہیں جو ہر بندوق کے لیے منفرد ہوتے ہیں",
        "فائرنگ کے دوران گولی جب نالی سے رگڑ کھا کر نکلتی ہے تو نالی کی باریک دراڑیں گولی کے تانبے پر فنگر پرنٹ کی طرح منفرد لکیریں کھود دیتی ہیں جن کا موازنہ کیا جاتا ہے۔"
    ),
    (
        "Why does a bullet hole through a window pane produce concentric fracture rings around the hole on the exit side rather than the entrance side?",
        ["Impact shock waves bend the brittle glass outward in tension on the rear surface, creating wider cone spalling (Hertzian cone fracture)", "Glass dissolves from bullet heat", "Air pressure sucks glass inward", "Bullets rotate clockwise only"],
        "Impact shock waves bend the brittle glass outward in tension on the rear surface, creating wider cone spalling (Hertzian cone fracture)",
        "Glass fails under tension rather than compression. The impact flexes the rear face in tension, propagating a conical fracture radiating outward.",
        "کھڑکی کے شیشے میں گولی لگنے پر گولی نکلنے والی دوسری طرف سوراخ بڑا اور کون (Cone) کی طرح پھیلا ہوا کیوں بنتا ہے؟",
        ["شیشہ دباؤ کے مقابلے میں کھنچاؤ (Tension) سے ٹوٹتا ہے، اور پچھلی سطح پر دباؤ کی لہریں شیشے کو مخروطی انداز میں اڑا دیتی ہیں", "گولی کی گرمی شیشے کو پگھلا دیتی ہے", "ہوا کا دباؤ شیشے کو اندر کھینچتا ہے", "گولی صرف کلاک وائز گھومتی ہے"],
        "شیشہ دباؤ کے مقابلے میں کھنچاؤ (Tension) سے ٹوٹتا ہے، اور پچھلی سطح پر دباؤ کی لہریں شیشے کو مخروطی انداز میں اڑا دیتی ہیں",
        "گولی لگنے پر جھٹکا سامنے سے اندر جاتا ہے، پچھلی طرف شیشہ لچک کی انتہا پر باہر اچھلتا ہے جس سے سوراخ کا پچھلا کنارہ کون (Hertzian cone) کی طرح چوڑا اکھڑتا ہے۔"
    ),
    (
        "Why does a diesel engine operate with exceptional fuel efficiency without requiring any spark plugs in its combustion chambers?",
        ["High compression ratio (16:1 to 22:1) heats cylinder air past 550°C, causing injected fuel to auto-ignite spontaneously", "Diesel fuel contains radioactive particles", "The pistons create perpetual electrical sparks", "Diesel engines have no exhaust valves"],
        "High compression ratio (16:1 to 22:1) heats cylinder air past 550°C, causing injected fuel to auto-ignite spontaneously",
        "Adiabatic compression of air raises temperature above diesel's auto-ignition threshold; direct fuel injection initiates instant combustion without electrical ignition.",
        "ڈیزل انجن میں پیٹرول انجن کے برعکس کوئی سپارک پلگ نہیں ہوتا، پھر وہ اندر آگ کیسے بھڑکاتا ہے اور اتنی زیادہ مائلیج کیسے دیتا ہے؟",
        ["پسٹن ہوا کو اتنا شدید دباتا ہے (Compression) کہ ہوا 500 ڈگری تک دہک اٹھتی ہے، جس میں ڈیزل چھڑکتے ہی وہ خود بخود جل اٹھتا ہے", "ڈیزل میں تابکاری کے ذرات ہوتے ہیں", "پسٹن خود برقی چنگاریاں بناتے ہیں", "ڈیزل انجن میں کوئی والو نہیں ہوتا"],
        "پسٹن ہوا کو اتنا شدید دباتا ہے (Compression) کہ ہوا 500 ڈگری تک دہک اٹھتی ہے، جس میں ڈیزل چھڑکتے ہی وہ خود بخود جل اٹھتا ہے",
        "جب ہوا کو تیزی سے انتہائی باریک حجم میں دبایا جائے تو اس کا درجہ حرارت آگ جتنا دہک اٹھتا ہے۔ جونہی ڈیزل کا اسپرے ہوتا ہے، وہ گرم ہوا سے فوراً بھڑک اٹھتا ہے۔"
    ),
    (
        "Why does vinyl LP audio record playback produce occasional crackles and pops on dry winter days?",
        ["Static electricity accumulated on the non-conductive PVC surface discharges microscopic electric sparks to the grounded metal needle", "Dust dissolves into liquid vinyl", "The diamond stylus melts the groove", "The turntable motor skips magnets"],
        "Static electricity accumulated on the non-conductive PVC surface discharges microscopic electric sparks to the grounded metal needle",
        "Triboelectric charging builds static potential on vinyl; as the conductive magnetic cartridge stylus tracks grooves, micro-arcs create audible voltage spikes.",
        "پرانے ونائل ریکارڈز (Gramophone LP) چلاتے وقت خشک سردیوں میں چٹخنے اور کڑکنے کی باریک آوازیں (Crackles) کیوں آنے لگتی ہیں؟",
        ["پلاسٹک ریکارڈ پر جمع ہونے والا ساکن برقی چارج (Static charge) لوہے کی سوئی کے ساتھ باریک چنگاریاں چھوڑتا ہے جو آواز بن جاتی ہیں", "دھول پگھل کر گوند بن جاتی ہے", "سوئی ریکارڈ کی نالی کو کاٹ دیتی ہے", "موٹر کا مقناطیس اچھلتا ہے"],
        "پلاسٹک ریکارڈ پر جمع ہونے والا ساکن برقی چارج (Static charge) لوہے کی سوئی کے ساتھ باریک چنگاریاں چھوڑتا ہے جو آواز بن جاتی ہیں",
        "ریکارڈ کی سطح پر رگڑ سے ساکن بجلی بنتی ہے۔ جب گراموفون کی سوئی اس پر سے گزرتی ہے تو باریک برقی ڈسچارج سپیکر میں چٹخنے کی آواز کے طور پر گونجتا ہے۔"
    ),
    (
        "Why does looking at the bottom of a clear swimming pool make the water appear roughly 25 percent shallower than it actually is?",
        ["Refraction bends light rays diverging from the pool floor away from the normal as they enter the air, elevating the virtual image", "Water absorbs light wavelengths", "Pool tiles curve the eyes", "Surface waves create optical magnifying glass"],
        "Refraction bends light rays diverging from the pool floor away from the normal as they enter the air, elevating the virtual image",
        "Snell's Law (n1 * sin theta1 = n2 * sin theta2) causes light rays exiting denser water (n=1.33) into air (n=1.0) to bend away from normal, raising apparent depth: d' = d / n.",
        "سوئمنگ پول کا تلا باہر سے دیکھنے پر حقیقت کے مقابلے میں 25 فیصد کم گہرا (اوپر اٹھا ہوا) کیوں معلوم ہوتا ہے؟",
        ["روشنی کی کرنیں پانی سے ہوا میں داخل ہوتے وقت مڑ جاتی ہیں جس سے انسان کی آنکھ کو تلا اوپر اٹھا ہوا نظر آتا ہے (Refraction)", "پانی روشنی کو پی جاتا ہے", "ٹائلیں آنکھ کو موڑ دیتی ہیں", "لہریں عدسے کا کام کرتی ہیں"],
        "روشنی کی کرنیں پانی سے ہوا میں داخل ہوتے وقت مڑ جاتی ہیں جس سے انسان کی آنکھ کو تلا اوپر اٹھا ہوا نظر آتا ہے (Refraction)",
        "روشنی جب کثیف پانی سے ہلکی ہوا میں نکلتی ہے تو عمود سے دور ہٹتی ہے۔ دماغ سمجھتا ہے کہ روشنی سیدھی آ رہی ہے، اس لیے تلا اصلی گہرائی سے چوتھائی حصہ اوپر لگتا ہے۔"
    ),
    (
        "Why do tropical cyclones in the Northern Hemisphere spin counter-clockwise, while cyclones in the Southern Hemisphere spin clockwise?",
        ["The Coriolis effect deflects inward-rushing low-pressure winds to the right in the north, creating counter-clockwise rotation", "Ocean currents flow in opposite directions", "Earth's magnetic poles repel wind", "Sunlight heats the hemispheres backwards"],
        "The Coriolis effect deflects inward-rushing low-pressure winds to the right in the north, creating counter-clockwise rotation",
        "Earth's eastward rotation produces apparent Coriolis acceleration: rightward deflection in Northern Hemisphere, leftward in Southern Hemisphere.",
        "شمالی نصف کرہ میں سمندری طوفان (Cyclones) گھڑی کی سوئی کے مخالف (Counter-clockwise) کیوں گھومتے ہیں جبکہ جنوبی نصف کرہ میں کلاک وائز گھومتے ہیں؟",
        ["زمین کی محوری گردش سے پیدا ہونے والی کوریولس قوت (Coriolis effect) شمال میں ہواؤں کو دائیں جانب موڑ کر مخالف رخ گھماتی ہے", "سمندری لہریں الٹی چلتی ہیں", "زمین کے مقناطیسی قطبین ہوا کو موڑتے ہیں", "دھوپ دونوں حصوں پر الٹی پڑتی ہے"],
        "زمین کی محوری گردش سے پیدا ہونے والی کوریولس قوت (Coriolis effect) شمال میں ہواؤں کو دائیں جانب موڑ کر مخالف رخ گھماتی ہے",
        "زمین کی اپنے محور پر تیز گردش کی وجہ سے شمال میں کم دباؤ کے مرکز کی طرف دوڑنے والی ہوائیں دائیں مڑ جاتی ہیں جس سے طوفان کا دائرہ الٹی سمت میں گھومنے لگتا ہے۔"
    ),
    (
        "Why does a person feeling an intense sneeze look directly toward a bright sunny window to trigger the sneeze?",
        ["The photic sneeze reflex causes bright light stimulation of the optic nerve to cross-activate adjacent trigeminal nasal nerves", "Sunlight burns dust in the nose", "Warmth causes nasal blood vessels to rupture", "Sneezing is purely a psychological reaction to light"],
        "The photic sneeze reflex causes bright light stimulation of the optic nerve to cross-activate adjacent trigeminal nasal nerves",
        "Autosomal dominant compulsive helio-ophthalmic outburst (ACHOO) syndrome involves parasympathetic signal leakage from optic pathways into maxillary trigeminal branches.",
        "چھینک رک جانے پر جب انسان اچانک سورج کی تیز روشنی یا بلب کو دیکھتا ہے تو اسے فوراً چھینک کیوں آ جاتی ہے؟",
        ["بصری اعصاب کی تیز چمک ساتھ والی ناک کی حس (Trigeminal nerve) میں کراس سگنل بھیج کر چھینک کو متحرک کر دیتی ہے (Photic sneeze reflex)", "دھوپ ناک کی دھول جلا دیتی ہے", "گرمی سے ناک کی رگیں پھٹتی ہیں", "روشنی سے چھینک کا کوئی تعلق نہیں ہوتا"],
        "بصری اعصاب کی تیز چمک ساتھ والی ناک کی حس (Trigeminal nerve) میں کراس سگنل بھیج کر چھینک کو متحرک کر دیتی ہے (Photic sneeze reflex)",
        "آنکھ اور ناک کے اعصابی راستے دماغ کے قریب سے گزرتے ہیں۔ اچانک تیز روشنی کا تیز سگنل ناک کے اعصاب کو چھیڑ دیتا ہے جسے دماغ خارش سمجھ کر چھینک دلاتا ہے۔"
    ),
    (
        "Why does an ordinary refrigerator door seal tightly shut with a soft 'thump' and remain held closed without any mechanical latch or hook?",
        ["A flexible rubber gasket encloses flexible magnetic strips that attract the steel refrigerator cabinet frame continuously", "Suction vacuum holds the door permanently", "Static electricity glues the rubber", "Gravity tilts the cabinet forward"],
        "A flexible rubber gasket encloses flexible magnetic strips that attract the steel refrigerator cabinet frame continuously",
        "Extruded flexible barium ferrite magnetic strips embedded in the elastomeric door bellows maintain continuous airtight perimeter seal.",
        "فریج کا دروازہ بغیر کسی کنڈی، چٹخنی یا ہک کے بند ہوتے ہی نرمی سے خود بخود مضبوطی سے کیوں جڑ جاتا ہے؟",
        ["دروازے کی ربڑ کی گسکیٹ کے اندر لچکدار مقناطیسی پٹی بند ہوتی ہے جو لوہے کے فریم کو ہر وقت اپنی گرفت میں رکھتی ہے", "اندرونی ویکیوم دروازے کو چوس لیتا ہے", "ساکن بجلی ربڑ کو چپکا دیتی ہے", "کشش ثقل دروازے کو آگے جھکاتی ہے"],
        "دروازے کی ربڑ کی گسکیٹ کے اندر لچکدار مقناطیسی پٹی بند ہوتی ہے جو لوہے کے فریم کو ہر وقت اپنی گرفت میں رکھتی ہے",
        "ربڑ کی جھلی کے اندر مقناطیسی پاؤڈر بھرا ہوتا ہے۔ دروازہ قریب آتے ہی مقناطیس فریم کے ساتھ جڑ کر ہوا بند مہر لگا دیتا ہے تاکہ ٹھنڈک باہر نہ نکلے۔"
    ),
    (
        "Why does a forensic fingerprint examiner use ninhydrin spray on porous paper documents to reveal invisible latent fingerprints?",
        ["Ninhydrin chemically reacts with amino acids in human sweat to form a vivid purple-blue dye known as Ruhemann's purple", "Ninhydrin dyes cellulose wood fibers", "Ninhydrin melts ink on paper", "It burns carbon residue"],
        "Ninhydrin chemically reacts with amino acids in human sweat to form a vivid purple-blue dye known as Ruhemann's purple",
        "Amino acids from sebaceous fingerprint residue bind irreversibly to cellulose fibers; ninhydrin decarboxylation yields intensely colored Ruhemann's purple complex.",
        "فرانزک لیب میں کاغذ پر موجود غائب انگلیوں کے نشانات ڈھونڈنے کے لیے نن ہائیڈرین (Ninhydrin) کا اسپرے کیوں کیا جاتا ہے؟",
        ["نن ہائیڈرین پسینے میں موجود امینو ایسڈز کے ساتھ مل کر جامنی نیلے رنگ کا واضح کیمیائی مرکب بنا دیتا ہے (Ruhemann's purple)", "یہ کاغذ کے ریشوں کو کالا کر دیتا ہے", "یہ سیاہی کو پگھلا دیتا ہے", "یہ کاربن کو جلا کر راکھ کرتا ہے"],
        "نن ہائیڈرین پسینے میں موجود امینو ایسڈز کے ساتھ مل کر جامنی نیلے رنگ کا واضح کیمیائی مرکب بنا دیتا ہے (Ruhemann's purple)",
        "انگلیوں کا پسینہ کاغذ کے ریشوں میں جذب ہو جاتا ہے۔ نن ہائیڈرین پروٹین کے اجزا سے کیمیائی عمل کر کے جامنی رنگ ابھارتا ہے جس سے لکیریں صاف چمک اٹھتی ہیں۔"
    ),
    (
        "Why do birds sitting on high-voltage power lines safely fly away unharmed, but a large stork touching two parallel wires simultaneously is electrocuted instantly?",
        ["Touching two different cables creates a high voltage potential difference across the body, driving lethal current between phases", "Storks have metallic feathers", "High cables carry no electricity", "Two cables attract lightning"],
        "Touching two different cables creates a high voltage potential difference across the body, driving lethal current between phases",
        "Single-wire perch offers zero potential difference; bridging two phase lines (thousands of volts apart) creates a catastrophic closed short circuit through the bird.",
        "ایک تار پر بیٹھا پرندہ بالکل محفوظ رہتا ہے مگر بڑا سارس جب اپنے پر پھیلا کر ایک ساتھ دو الگ الگ تاروں کو چھوتا ہے تو فوری ہلاک کیوں ہو جاتا ہے؟",
        ["دو مختلف تاروں کو ایک ساتھ چھونے سے ان کے درمیانی ہزاروں وولٹ کا برقی فرق جسم کے آر پار جان لیوا کرنٹ دوڑا دیتا ہے", "سارس کے پر دھاتی ہوتے ہیں", "اوپری تار میں بجلی نہیں ہوتی", "دو تاریں آسمانی بجلی کھینچتی ہیں"],
        "دو مختلف تاروں کو ایک ساتھ چھونے سے ان کے درمیانی ہزاروں وولٹ کا برقی فرق جسم کے آر پار جان لیوا کرنٹ دوڑا دیتا ہے",
        "ایک تار پر دونوں پاؤں ہوں تو کوئی پوٹینشل فرق نہیں ہوتا۔ مگر جب پرندہ دو الگ فیز کی تاروں کو چھوتا ہے تو شارٹ سرکٹ بن کر لاکھوں واٹ بجلی اس کے جسم سے گزرتی ہے۔"
    ),
    (
        "Why does an ordinary automobile shock absorber contain pressurized hydraulic fluid forced through tiny internal orifice valves?",
        ["Fluid viscous damping converts spring oscillation kinetic energy into dissipated thermal heat, dampening bounce rapidly", "Hydraulic fluid cools the tires", "Fluid pushes the car body upward", "Hydraulic valves generate electricity"],
        "Fluid viscous damping converts spring oscillation kinetic energy into dissipated thermal heat, dampening bounce rapidly",
        "Without dampers, suspension springs oscillate indefinitely. Forcing incompressible oil through calibrated orifices dissipates kinetic energy into heat.",
        "گاڑی کے شاک ایبزاربر (Shock absorber) میں تیل اور باریک والو کیوں لگائے جاتے ہیں بجائے اس کے کہ صرف سادہ اسپرنگ لگایا جائے؟",
        ["تیل کا باریک سوراخوں سے گزرنا جھٹکوں کی توانائی کو رگڑ کی حرارت میں بدل کر اسپرنگ کے مسلسل اچھلنے کو فوراً روک دیتا ہے", "تیل ٹائروں کو ٹھنڈا رکھتا ہے", "تیل گاڑی کی باڈی کو مستقل اٹھاتا ہے", "والوز بجلی پیدا کرتے ہیں"],
        "تیل کا باریک سوراخوں سے گزرنا جھٹکوں کی توانائی کو رگڑ کی حرارت میں بدل کر اسپرنگ کے مسلسل اچھلنے کو فوراً روک دیتا ہے",
        "اگر صرف اسپرنگ ہو تو گاڑی کھڈے کے بعد منٹوں تک اچھلتی رہے گی۔ شاک ایبزاربر کا گاڑھا تیل سوراخوں سے گزر کر اس اچھال کو ایک سیکنڈ میں دبا دیتا ہے۔"
    ),
    (
        "Why does a piece of dry spaghetti snap into three or more pieces rather than breaking cleanly into two when bent from both ends?",
        ["The initial fracture releases an explosive flexural stress recoil wave that travels along the curved pasta, triggering secondary breaks", "Spaghetti has hollow internal bubbles", "Dry pasta contains air pockets", "Bending heats the center to melting point"],
        "The initial fracture releases an explosive flexural stress recoil wave that travels along the curved pasta, triggering secondary breaks",
        "Richard Feynman's puzzle: snap-back relaxation excites snap-back flexural waves, locally increasing curvature beyond the initial break threshold.",
        "خشک اسپگیٹی (سوکھے نوڈلز) کی تیلی کو دونوں سروں سے موڑنے پر وہ دو ٹکڑے ہونے کی بجائے ہمیشہ تین یا زیادہ ٹکڑوں میں کیوں چٹختی ہے؟",
        ["پہلے ٹوٹنے کا جھٹکا تیلی کے اندر لچکدار لہر دوڑاتا ہے جو مڑے ہوئے حصے کو مزید دہرا کر کے دوسرے مقام سے بھی توڑ دیتی ہے", "اسپگیٹی کے اندر بلبلے ہوتے ہیں", "خشک آٹے میں ہوا کے سوراخ ہوتے ہیں", "موڑنے سے درمیان کا حصہ پگھل جاتا ہے"],
        "پہلے ٹوٹنے کا جھٹکا تیلی کے اندر لچکدار لہر دوڑاتا ہے جو مڑے ہوئے حصے کو مزید دہرا کر کے دوسرے مقام سے بھی توڑ دیتی ہے",
        "نوبل انعام یافتہ رچرڈ فین مین کا یہ مشہور معمہ بتاتا ہے کہ پہلا ٹکڑا الگ ہوتے ہی تیلی سیدھی ہونے کے لیے جھٹکا کھاتی ہے، جس کا تناؤ اسے دوسری جگہ سے توڑ دیتا ہے۔"
    ),
    (
        "Why does a person feeling motion sickness on a ship feel so much better when stepping outside onto the open deck?",
        ["Fresh sensory cues: viewing the distant horizon realigns the inner ear's vestibular cues with the visual cortex, and cool air dampens nausea", "Deck wood absorbs motion sickness", "Open sea has zero gravity", "Engine noise is louder outside"],
        "Fresh sensory cues: viewing the distant horizon realigns the inner ear's vestibular cues with the visual cortex, and cool air dampens nausea",
        "Visual confirmation of true motion eliminates sensory conflict; concurrent facial airflow stimulates trigeminal cold receptors to suppress nausea.",
        "بحری جہاز پر بیمار محسوس کرنے والا مسافر جب کیبن سے نکل کر کھلے ڈیک پر آتا ہے تو اس کی طبیعت اچانک کیوں سنبھل جاتی ہے؟",
        ["دور افق کو دیکھنے سے آنکھوں اور کانوں کا تضاد ختم ہو جاتا ہے اور چہرے پر ٹھنڈی ہوا متلی کے سگنل کو دبا دیتی ہے", "ڈیک کی لکڑی بیماری چوس لیتی ہے", "کھلے سمندر میں کشش ثقل نہیں ہوتی", "باہر انجن کا شور زیادہ ہوتا ہے"],
        "دور افق کو دیکھنے سے آنکھوں اور کانوں کا تضاد ختم ہو جاتا ہے اور چہرے پر ٹھنڈی ہوا متلی کے سگنل کو دبا دیتی ہے",
        "افق کو دیکھ کر دماغ کو کشتی کے جھولنے کا منطقی ثبوت مل جاتا ہے جس سے الجھن دور ہوتی ہے اور ٹھنڈی ہوا اعصاب کو فوری پرسکون کر دیتی ہے۔"
    ),
    (
        "Why does water boil at a lower temperature than 100°C at the peak of Mount Everest (around 71°C)?",
        ["Atmospheric pressure on Everest is only one-third of sea-level pressure, allowing water molecules to overcome vapor pressure barriers at lower thermal energy", "Mountain ice cools the water", "Everest gravity is weaker", "Air contains zero oxygen at high altitude"],
        "Atmospheric pressure on Everest is only one-third of sea-level pressure, allowing water molecules to overcome vapor pressure barriers at lower thermal energy",
        "Boiling occurs when saturated vapor pressure equals ambient atmospheric pressure; reduced barometric pressure lowers the saturation temperature.",
        "ماؤنٹ ایورسٹ کی اونچی چوٹی پر پانی 100 ڈگری کی بجائے محض 71 ڈگری سینٹی گریڈ پر ہی کیوں ابلنے لگتا ہے؟",
        ["چوٹی پر ہوا کا دباؤ سمندر کے مقابلے میں ایک تہائی رہ جاتا ہے، اس لیے پانی کے بخارات کم گرمی میں ہی فضا کے دباؤ پر غالب آ جاتے ہیں", "پہاڑ کی برف پانی کو ٹھنڈا کرتی ہے", "چوٹی پر کشش ثقل کمزور ہے", "بلندی پر آکسیجن بالکل ختم ہو جاتی ہے"],
        "چوٹی پر ہوا کا دباؤ سمندر کے مقابلے میں ایک تہائی رہ جاتا ہے، اس لیے پانی کے بخارات کم گرمی میں ہی فضا کے دباؤ پر غالب آ جاتے ہیں",
        "ابلنے کا مطلب یہ ہے کہ پانی کے بخارات کا زور باہر کی ہوا کے دباؤ کے برابر ہو جائے۔ بلندی پر ہوا کا بوجھ کم ہونے کی وجہ سے پانی معمولی گرمی پر ابل پڑتا ہے۔"
    ),
    (
        "Why does an airplane fly upside down during aerobatic stunts without the engine immediately starving of aviation fuel?",
        ["Aerobatic aircraft use inverted fuel tanks with flexible weighted flop tubes that sink to wherever fuel gathers under negative-G forces", "Fuel defies gravity in airplanes", "Pilots pump fuel by foot pedals", "Aerobatic engines use solid fuel"],
        "Aerobatic aircraft use inverted fuel tanks with flexible weighted flop tubes that sink to wherever fuel gathers under negative-G forces",
        "A weighted hose (flop tube) inside the fuel cell drops to the top of the tank under negative Gs, keeping the fuel pickup submerged in inverted fuel.",
        "کرتب دکھانے والے ہوائی جہاز جب فضا میں الٹے اڑتے ہیں تو کشش ثقل کے الٹ ہونے کے باوجود ان کے انجن کو پیٹرول ملنا بند کیوں نہیں ہوتا؟",
        ["ان کے فیول ٹینک میں وزنی لچکدار نالی (Flop tube) لگی ہوتی ہے جو الٹے ہونے پر پیٹرول کے بہاؤ کے ساتھ خود بخود نیچے گر جاتی ہے", "جہاز کے اندر ایندھن کشش ثقل کو نہیں مانتا", "پائلٹ پاؤں کے پیڈل سے پیٹرول پمپ کرتا ہے", "یہ جہاز ٹھوس ایندھن پر چلتے ہیں"],
        "ان کے فیول ٹینک میں وزنی لچکدار نالی (Flop tube) لگی ہوتی ہے جو الٹے ہونے پر پیٹرول کے بہاؤ کے ساتھ خود بخود نیچے گر جاتی ہے",
        "عام ٹینک میں پیٹرول چھت پر چلا جائے تو نالی ہوا کھینچنے لگتی ہے۔ کرتب والے جہاز میں وزنی نلکی پیٹرول کے ساتھ ہی حرکت کرتی ہے اور ایندھن کا بہاؤ نہیں ٹوٹتا۔"
    ),
    (
        "Why does a piece of ice stick painfully to your tongue if you lick an ice cube straight out of a deep freezer?",
        ["Frigid sub-zero ice instantly freezes moisture on your tongue, cementing saliva ice into microscopic taste bud pores", "Ice contains microscopic barbs", "Freezer frost is made of superglue", "Taste buds emit electrical glue"],
        "Frigid sub-zero ice instantly freezes moisture on your tongue, cementing saliva ice into microscopic taste bud pores",
        "Thermal conduction to deep sub-zero ice rapidly cools surface saliva below 0°C, freezing it in intimate contact with the tongue's lingual papillae.",
        "ڈیپ فریزر سے تازہ نکالی گئی سخت ٹھنڈی برف کو زبان لگانے پر وہ زبان کے ساتھ اتنی سختی سے کیوں چپک جاتی ہے کہ چھڑانا دردناک ہو جاتا ہے؟",
        ["منفی 18 ڈگری ٹھنڈی برف زبان کے لعاب (تھوک) کو سیکنڈ کے دسویں حصے میں جما کر زبان کے مساموں کے ساتھ برف کا کنکریٹ جوڑ بنا دیتی ہے", "برف پر باریک کانٹے ہوتے ہیں", "فریزر کی برف میں گوند ہوتی ہے", "زبان برقی چارج خارج کرتی ہے"],
        "منفی 18 ڈگری ٹھنڈی برف زبان کے لعاب (تھوک) کو سیکنڈ کے دسویں حصے میں جما کر زبان کے مساموں کے ساتھ برف کا کنکریٹ جوڑ بنا دیتی ہے",
        "فریزر کی برف کا درجہ حرارت منفی 15 سے 20 ڈگری ہوتا ہے۔ چھوتے ہی وہ زبان کی نمی کی ساری گرمی چوس کر اسے فوراً جما دیتی ہے اور مضبوطی سے پکڑ لیتی ہے۔"
    ),
    (
        "Why does an ocean cargo container ship have bulbous bows (a protruding bulb under the waterline at the front of the hull)?",
        ["The bulb creates an advance wave that destructively interferes with the ship's natural bow wave, reducing total hydrodynamic drag by up to 15 percent", "To bump floating icebergs safely", "To house forward sonar cameras", "To store heavy anchor chains"],
        "The bulb creates an advance wave that destructively interferes with the ship's natural bow wave, reducing total hydrodynamic drag by up to 15 percent",
        "A properly shaped bulbous bow produces a trough that cancels the crest of the primary bow wave, minimizing wave-making resistance at design cruise speeds.",
        "بڑے بحری جہازوں کے اگلے سرے پر پانی کے اندر ایک ابھرا ہوا گول ناک نما بلب (Bulbous bow) کیوں بنایا جاتا ہے؟",
        ["یہ ابھار پانی میں ایک پیشگی لہر بنا کر جہاز کی اگلی لہر کو منسوخ کر دیتا ہے جس سے پانی کی رکاوٹ اور ایندھن کا خرچ 15 فیصد کم ہو جاتا ہے", "برفانی تودوں کو توڑنے کے لیے", "آگے کیمرے لگانے کے لیے", "لنگر کی زنجیر رکھنے کے لیے"],
        "یہ ابھار پانی میں ایک پیشگی لہر بنا کر جہاز کی اگلی لہر کو منسوخ کر دیتا ہے جس سے پانی کی رکاوٹ اور ایندھن کا خرچ 15 فیصد کم ہو جاتا ہے",
        "چلتا ہوا جہاز پانی پر اونچی لہر اٹھاتا ہے جو ایندھن کھاتی ہے۔ نیچے نکلا ہوا گول بلب اپنی الگ لہر بناتا ہے جو مرکزی لہر کو دبا کر پانی کو ہموار کر دیتی ہے۔"
    ),
    (
        "Why does an ordinary automobile engine air filter trap microscopic road dust without completely restricting engine breathing air intake?",
        ["Porous pleated cellulose microfibers capture particles through inertial impaction and diffusion while presenting an immense total surface area", "Air filters use electric magnets", "Dust dissolves into paper fibers", "Air filters use water spray"],
        "Porous pleated cellulose microfibers capture particles through inertial impaction and diffusion while presenting an immense total surface area",
        "Accordion pleating expands effective filtration area up to 50 times the duct size, drastically lowering face velocity and pressure drop.",
        "گاڑی کا ائیر فلٹر سڑک کی باریک مٹی کو اپنے اندر روک لیتا ہے مگر انجن کے سانس لینے کے لیے ہوا کا راستہ بند کیوں نہیں کرتا؟",
        ["جھریوں دار (Pleated) ڈیزائن کاغذ کے رقبے کو 50 گنا بڑا کر دیتا ہے جس سے ہوا کا بہاؤ رکے بغیر مٹی کے ذرات ریشوں میں پھنس جاتے ہیں", "فلٹر میں مقناطیس لگے ہوتے ہیں", "مٹی کاغذ میں گھل جاتی ہے", "فلٹر پر پانی کا چھڑکاؤ ہوتا ہے"],
        "جھریوں دار (Pleated) ڈیزائن کاغذ کے رقبے کو 50 گنا بڑا کر دیتا ہے جس سے ہوا کا بہاؤ رکے بغیر مٹی کے ذرات ریشوں میں پھنس جاتے ہیں",
        "فلٹر کا کاغذ پنکھے کی طرح طے شدہ تہوں میں مڑا ہوتا ہے۔ اتنا بڑا رقبہ ہوا کو بغیر دباؤ کے آسانی سے گزرنے دیتا ہے جبکہ ریشے گرد کو جکڑ لیتے ہیں۔"
    ),
    (
        "Why does a person feeling motion sickness suffer worse nausea when seated backwards facing away from the direction of travel on a train?",
        ["Sensory dissonance is heightened when visual motion signals traveling backward while somatic inertia feels forward motion acceleration", "Backwards seating lowers oxygen intake", "Train wheels vibrate backwards", "Backward seating reverses digestion"],
        "Sensory dissonance is heightened when visual motion signals traveling backward while somatic inertia feels forward motion acceleration",
        "The brain's predictive locomotor models anticipate motion along the line of sight; viewing receding terrain while accelerating conflicts with vestibulospinal reflexes.",
        "ٹرین میں الٹے رخ (سفر کی سمت کے مخالف پیٹھ کر کے) بیٹھنے والے مسافر کو چکر اور متلی کا امکان کہیں زیادہ کیوں ہوتا ہے؟",
        ["کیونکہ آنکھیں پیچھے بھاگتی ہوئی دنیا دیکھتی ہیں جبکہ جسم کا اندرونی توازن آگے کی سمت کا جھٹکا محسوس کرتا ہے، جس سے تضاد بڑھ جاتا ہے", "الٹے بیٹھنے سے آکسیجن کم ملتی ہے", "ٹرین کے پہیے الٹے لرزتے ہیں", "الٹے بیٹھنے سے ہاضمہ الٹ جاتا ہے"],
        "کیونکہ آنکھیں پیچھے بھاگتی ہوئی دنیا دیکھتی ہیں جبکہ جسم کا اندرونی توازن آگے کی سمت کا جھٹکا محسوس کرتا ہے، جس سے تضاد بڑھ جاتا ہے",
        "انسانی آنکھیں اور دماغ آگے بڑھنے کے لیے بنے ہیں۔ پیچھے کی طرف چیزوں کو چھوٹتے دیکھنا اور جھٹکا آگے لگنا دماغ کے توازن کے مرکز کو الجھا کر متلی پیدا کرتا ہے۔"
    ),
    (
        "Why does an ocean iceberg float with roughly 90 percent of its massive bulk submerged hidden beneath the waterline?",
        ["Pure glacial ice density (0.917 g/cm^3) is roughly nine-tenths the density of cold seawater (1.025 g/cm^3)", "Icebergs are magnetized to the ocean seabed", "Underwater currents pull icebergs down", "The top evaporates in cold air"],
        "Pure glacial ice density (0.917 g/cm^3) is roughly nine-tenths the density of cold seawater (1.025 g/cm^3)",
        "Archimedes' principle: submerged volume fraction equals the ratio of ice density to seawater density (0.917 / 1.025 = ~89.5%).",
        "سمندر میں تیرتے ہوئے برفانی تودے (Iceberg) کا 90 فیصد دیوہیکل حصہ پانی کے نیچے چھپا کیوں رہتا ہے اور صرف 10 فیصد حصہ اوپر نظر آتا ہے؟",
        ["برف کی کثافت (0.917) نمکین سمندری پانی کی کثافت (1.025) کے تقریباً نو بٹا دس (90%) کے برابر ہوتی ہے (Archimedes' principle)", "تودے پیندے کے مقناطیس سے جڑے ہوتے ہیں", "زیر آب لہریں تودے کو نیچے کھینچتی ہیں", "اوپری حصہ سردی میں اڑ جاتا ہے"],
        "برف کی کثافت (0.917) نمکین سمندری پانی کی کثافت (1.025) کے تقریباً نو بٹا دس (90%) کے برابر ہوتی ہے (Archimedes' principle)",
        "آرکیمیڈیز کا قانون بتاتا ہے کہ تیرتی چیز کا جتنا تناسب مائع سے ہلکا ہوگا اتنا ہی حصہ اوپر رہے گا۔ چونکہ برف پانی سے صرف 10 فیصد ہلکی ہے اس لیے 90 فیصد نیچے ڈوبی رہتی ہے۔"
    ),
    (
        "Why does an ordinary lead-acid car battery produce corrosive white crusty powder around its lead terminals over time?",
        ["Escaping sulfuric acid electrolyte fumes react with copper wire lugs and lead terminals to form lead sulfate and copper sulfate crystals", "Road salt accumulates on battery tops", "Lead oxidizes directly into white paint", "Acid turns into solid baking soda"],
        "Escaping sulfuric acid electrolyte fumes react with copper wire lugs and lead terminals to form lead sulfate and copper sulfate crystals",
        "Hydrogen gas venting carries trace sulfuric acid aerosols; reaction with lead battery posts and brass/copper terminals precipitates insoluble sulfate salts.",
        "گاڑی کی بیٹری کے ٹرمینلز کے ارد گرد وقت کے ساتھ سفید یا نیلگوں سفوف جیسا زنگ (Corrosion) کیوں جم جاتا ہے؟",
        ["بیٹری سے نکلنے والی گندھک کے تیزاب کی بھاپ تانبے اور لیڈ کے ٹرمینلز سے مل کر لیڈ سلفیٹ کی قلمیں جما دیتی ہے", "سڑک کا نمک بیٹری پر جم جاتا ہے", "لیڈ سفید پینٹ میں بدل جاتا ہے", "تیزاب خود بخود بیکنگ سوڈا بن جاتا ہے"],
        "بیٹری سے نکلنے والی گندھک کے تیزاب کی بھاپ تانبے اور لیڈ کے ٹرمینلز سے مل کر لیڈ سلفیٹ کی قلمیں جما دیتی ہے",
        "بیٹری کے چارج ہونے پر باریک سوراخوں سے ہائیڈروجن اور تیزابی بخارات اڑتے ہیں جو کنیکٹرز کے ساتھ کیمیائی تعامل کر کے سفید سفوف کی شکل میں جم جاتے ہیں۔"
    ),
    (
        "Why does a piece of dry chalk write smoothly on a rough stone blackboard, but slides uselessly without leaving a mark on smooth oily glass?",
        ["Chalk writing relies on abrasive mechanical shear against micro-rough asperities to pulverize calcium carbonate flakes", "Glass chemically repels chalk", "Chalk dissolves in glass oils", "Stone emits electromagnetic writing energy"],
        "Chalk writing relies on abrasive mechanical shear against micro-rough asperities to pulverize calcium carbonate flakes",
        "Abrasive wear requires surface roughness asperities with shear strength exceeding chalk cohesion; smooth glass lacks asperities to shear particles.",
        "چاک کھردرے بلیک بورڈ پر تو صاف اور واضح لکھتا ہے مگر چکنے شیشے پر بغیر کوئی نشان چھوڑے پھسل کیوں جاتا ہے؟",
        ["چاک سے لکھنے کے لیے کھردری سطح کی رگڑ درکار ہوتی ہے جو چاک کے ذرات کو رگڑ کر الگ کرتی ہے، جبکہ شیشہ چکنا ہوتا ہے", "شیشہ چاک کو کیمیائی طور پر دھکیلتا ہے", "چاک شیشے کے تیل میں گھل جاتا ہے", "پتھر لکھنے کی مقناطیسی توانائی دیتا ہے"],
        "چاک سے لکھنے کے لیے کھردری سطح کی رگڑ درکار ہوتی ہے جو چاک کے ذرات کو رگڑ کر الگ کرتی ہے، جبکہ شیشہ چکنا ہوتا ہے",
        "بلیک بورڈ پر مائکروسکوپک اتار چڑھاؤ ہوتے ہیں جو چاک کے کیلشیم کاربونیٹ کو رگڑ کر پاؤڈر بنا دیتے ہیں۔ شیشے پر یہ کھردرائی نہ ہونے سے چاک پھسل جاتا ہے۔"
    ),
    (
        "Why does a diver in deep ocean waters feel extremely hungry and crave carbohydrate-rich foods after completing an underwater dive?",
        ["The human body expends immense metabolic calories conducting thermoregulation against water, which conducts body heat 24 times faster than air", "Seawater drains stomach calories", "Breathing compressed oxygen burns sugars", "Undersea depth lowers body insulin"],
        "The human body expends immense metabolic calories conducting thermoregulation against water, which conducts body heat 24 times faster than air",
        "Water's tremendous heat capacity and high thermal conductivity rapidly drain core calories; the liver depletes glycogen stores to maintain core body temperature.",
        "سمندر میں غوطہ لگانے کے بعد غوطہ خور کو اچانک شدید بھوک کیوں لگتی ہے اور وہ میٹھا یا روٹی کھانے کی شدید طلب کیوں محسوس کرتا ہے؟",
        ["پانی انسان کی جسمانی حرارت ہوا سے 24 گنا زیادہ تیزی سے چوس لیتا ہے جس کی تلافی کے لیے جسم تیزی سے کیلوریز جلاتا ہے", "سمندری پانی معدے کی خوراک چوس لیتا ہے", "کمپریسڈ آکسیجن شکر جلا دیتی ہے", "سمندر کی گہرائی انسولین ختم کر دیتی ہے"],
        "پانی انسان کی جسمانی حرارت ہوا سے 24 گنا زیادہ تیزی سے چوس لیتا ہے جس کی تلافی کے لیے جسم تیزی سے کیلوریز جلاتا ہے",
        "پانی میں جسم کو 37 ڈگری پر گرم رکھنا سخت محنت مانگتا ہے۔ اندرونی ہیٹر چلانے کے لیے جگر کا سارا گلائیکوجن جل جاتا ہے جس سے شدید بھوک لگتی ہے۔"
    ),
    (
        "Why does an airplane cabin crew dim the interior lights during a night takeoff or landing?",
        ["To allow passengers' and crew's eyes to adapt to darkness (rhodopsin rod adaptation) in case of an emergency evacuation in the dark", "To conserve aircraft battery power", "To help passengers fall asleep", "To prevent ground radar detection"],
        "To allow passengers' and crew's eyes to adapt to darkness (rhodopsin rod adaptation) in case of an emergency evacuation in the dark",
        "Dark adaptation takes up to 20-30 minutes; dimming cabin lights ensures immediate night vision if lights fail during a sudden nighttime crash landing.",
        "رات کے وقت لینڈنگ یا ٹیک آف کے دوران ہوائی جہاز کے کیبن کی روشنیاں مدہم (Dim) کیوں کر دی جاتی ہیں؟",
        ["تاکہ ہنگامی لینڈنگ کی صورت میں مسافروں اور عملے کی آنکھیں باہر کے گھپ اندھیرے کی عادی رہیں اور وہ فوری بھاگ سکیں", "جہاز کی بیٹری کا کرنٹ بچانے کے لیے", "مسافروں کو نیند کی ترغیب دینے کے لیے", "زمین کے ریڈار سے چھپنے کے لیے"],
        "تاکہ ہنگامی لینڈنگ کی صورت میں مسافروں اور عملے کی آنکھیں باہر کے گھپ اندھیرے کی عادی رہیں اور وہ فوری بھاگ سکیں",
        "اگر روشن کیبن سے اچانک اندھیری زمین پر نکلنا پڑے تو آنکھیں منٹوں تک اندھی ہو جاتی ہیں۔ روشنیاں مدہم کر کے آنکھوں کے روڈاپسن خلیات پہلے سے تیار کیے جاتے ہیں۔"
    ),
    (
        "Why does an arch bridge keystone remain firmly in place without mortar or glue, even when heavy traffic rolls directly across it?",
        ["Tapered wedge geometry converts vertical downward weight into lateral compressive forces against neighboring voussoirs", "Magnetic forces in masonry", "Friction with the road asphalt", "The keystone is pinned with hidden steel bolts"],
        "Tapered wedge geometry converts vertical downward weight into lateral compressive forces against neighboring voussoirs",
        "The wedge-shaped trapezoid cannot drop through without pushing adjacent stones outward; the abutments hold the arch in rigid static equilibrium.",
        "محرابی پل کا درمیانی کلس پتھر (Keystone) بغیر کسی سیمنٹ یا گوند کے صدیوں تک بھاری ٹریفک کے باوجود نیچے کیوں نہیں گرتا؟",
        ["اس کی پچانی (Wedge) شکل اوپر کے وزن کو دائیں بائیں کے پتھروں پر زبردست دباؤ میں بدل دیتی ہے جو اسے پھنسائے رکھتی ہے", "پتھروں میں قدرتی مقناطیس ہوتا ہے", "سڑک کی تارکول کی رگڑ", "اندر چھپے لوہے کے نٹ بولٹ"],
        "اس کی پچانی (Wedge) شکل اوپر کے وزن کو دائیں بائیں کے پتھروں پر زبردست دباؤ میں بدل دیتی ہے جو اسے پھنسائے رکھتی ہے",
        "درمیانی پتھر اوپر سے چوڑا اور نیچے سے پتلا ہوتا ہے۔ جتنا وزن اوپر سے پڑے گا وہ اتنی ہی سختی سے دائیں بائیں کے پتھروں میں پھنس جائے گا، نیچے گر نہیں سکتا۔"
    ),
    (
        "Why does an iceberg in the Arctic ocean produce freshwater when melted, even though it was formed in salty ocean seawater?",
        ["Glacial ice forms from compacted atmospheric snowfall over land, not frozen ocean water", "Salt evaporates at sub-zero temperatures", "Polar bears filter the ice", "Salt sinks to the seabed before freezing"],
        "Glacial ice forms from compacted atmospheric snowfall over land, not frozen ocean water",
        "Icebergs calve from continental glaciers made of accumulated freshwater snow, containing virtually zero salt.",
        "بحر منجمد شمالی میں تیرتے ہوئے برفانی تودے پگھلنے پر نمکین سمندری پانی کی بجائے میٹھا پینے کا پانی کیوں بناتے ہیں؟",
        ["برفانی تودے خشکی پر گرنے والی میٹھی برف باری کے جمنے سے بنتے ہیں، سمندر کے پانی سے نہیں", "منفی درجہ حرارت پر نمک اڑ جاتا ہے", "قطبی ریچھ نمک کو صاف کر دیتے ہیں", "جمنے سے پہلے نمک نیچے بیٹھ جاتا ہے"],
        "برفانی تودے خشکی پر گرنے والی میٹھی برف باری کے جمنے سے بنتے ہیں، سمندر کے پانی سے نہیں",
        "برفانی تودے خشکی کے گلیشیئرز سے ٹوٹ کر گرتے ہیں جو آسمانی بارش اور برف باری سے بنتے ہیں، اس لیے ان میں نمک نہیں ہوتا۔"
    ),
    (
        "Why does a piece of dry spaghetti bend slightly without breaking when you bend it slowly, but snaps abruptly when bent past a critical threshold?",
        ["Tensile strain along the outer curved surface exceeds the critical brittle tensile strength of dry pasta", "Water molecules evaporate during bending", "The center becomes hotter than boiling point", "Spaghetti has steel fibers inside"],
        "Tensile strain along the outer curved surface exceeds the critical brittle tensile strength of dry pasta",
        "As curvature increases, outer surface tensile stress reaches the brittle fracture limit, triggering catastrophic crack propagation.",
        "خشک اسپگیٹی کو آہستہ آہستہ موڑنے پر وہ معمولی سی مڑ جاتی ہے مگر ایک حد سے آگے جاتے ہی اچانک چٹخ کیوں جاتی ہے؟",
        ["موڑنے پر باہر کی سطح کا کھنچاؤ سوکھے آٹے کی لچکدار حد سے بڑھ کر دراڑ پیدا کر دیتا ہے", "موڑنے سے پانی اڑ جاتا ہے", "درمیان کا حصہ ابلنے جتنا گرم ہوتا ہے", "اسپگیٹی کے اندر لوہے کی تاریں ہوتی ہیں"],
        "موڑنے پر باہر کی سطح کا کھنچاؤ سوکھے آٹے کی لچکدار حد سے بڑھ کر دراڑ پیدا کر دیتا ہے",
        "چونکہ خشک آٹا غیر لچکدار ہوتا ہے، اس لیے موڑنے پر بیرونی سطح پر کھنچاؤ کا دباؤ حد سے بڑھتے ہی سیکنڈ کے ہزارویں حصے میں چٹخ جاتا ہے۔"
    ),
    (
        "Why does a compass needle point toward the geographic North Pole rather than true South?",
        ["Earth's geomagnetic South pole is located near the geographic North pole, attracting the needle's magnetic north pole", "The needle is pushed by solar wind", "North Pole has lower gravity", "Polar ice attracts magnetized steel"],
        "Earth's geomagnetic South pole is located near the geographic North pole, attracting the needle's magnetic north pole",
        "Opposites attract in magnetism: the north-seeking pole of a magnet is drawn toward Earth's magnetic south pole located in the Arctic.",
        "قطب نما (Compass) کی مقناطیسی سوئی ہمیشہ جغرافیائی شمالی قطب کی طرف ہی کیوں رخ کرتی ہے؟",
        ["زمین کا مقناطیسی جنوبی قطب جغرافیائی شمالی قطب کے پاس واقع ہے جو سوئی کے شمالی سرے کو کھینچتا ہے", "شمسی ہوا سوئی کو دھکیلتی ہے", "شمالی قطب پر کشش ثقل کم ہے", "برف مقناطیسی لوہے کو بلاتی ہے"],
        "زمین کا مقناطیسی جنوبی قطب جغرافیائی شمالی قطب کے پاس واقع ہے جو سوئی کے شمالی سرے کو کھینچتا ہے",
        "مقناطیس کے متضاد سرے کشش کرتے ہیں۔ چونکہ زمین کا مقناطیسی قطب شمال میں 'جنوبی' نوعیت کا ہے، اس لیے وہ سوئی کے شمالی رخ کو کھینچ کر شمال دکھاتا ہے۔"
    ),
    (
        "Why do birds sitting on high cliffs face directly into the incoming wind when taking off into flight?",
        ["Facing headwinds immediately generates maximum relative airspeed over their wings, producing instant aerodynamic lift", "Facing downwind blows feathers away", "Birds cannot turn their heads", "Tailwinds pull birds downward"],
        "Facing headwinds immediately generates maximum relative airspeed over their wings, producing instant aerodynamic lift",
        "Lift is proportional to the square of relative airspeed (v^2). Running or leaping into a headwind provides free airspeed for effortless takeoff.",
        "اونچی چٹانوں پر بیٹھے پرندے اڑان بھرتے وقت ہمیشہ ہوا کے سامنے رخ کر کے چھلانگ کیوں لگاتے ہیں؟",
        ["ہوا کے رخ کے سامنے رخ کرنے سے پروں پر فوری طور پر ہوا کی تیز رفتاری سے اڑنے کی طاقت (Lift) مل جاتی ہے", "پیچھے سے ہوا پر اکھاڑ دیتی ہے", "پرندے سر نہیں موڑ سکتے", "پیچھے کی ہوا نیچے گراتی ہے"],
        "ہوا کے رخ کے سامنے رخ کرنے سے پروں پر فوری طور پر ہوا کی تیز رفتاری سے اڑنے کی طاقت (Lift) مل جاتی ہے",
        "ہوائی جہاز کی طرح پرندوں کے پروں کو لفٹ ہوا کی نسبتی رفتار سے ملتی ہے۔ سامنے سے آتی ہوا بغیر محنت کیے پرندے کو فوری فضا میں بلند کر دیتی ہے۔"
    )
]

print(f"Fresh Normal 35 loaded: {len(ITEMS)} items.")
