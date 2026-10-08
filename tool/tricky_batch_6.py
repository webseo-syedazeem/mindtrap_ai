# -*- coding: utf-8 -*-
"""
Tricky Batch 6 (40 items: 311-350).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why is cosmological redshift caused by the expansion of the universe fundamentally different from the ordinary Doppler effect?",
        ["Cosmological redshift stretches the wavelength of light as the metric fabric of space itself expands during transit", "Distant galaxies move through space faster than light", "Cosmic dust scatters blue wavelengths into red", "Gravity slows down light to red frequencies"],
        "Cosmological redshift stretches the wavelength of light as the metric fabric of space itself expands during transit",
        "The Doppler effect is kinematic motion through static space. Cosmological redshift z = (a_obs / a_emit) - 1 occurs because spacetime metric expansion physically elongates traveling photon wavelengths.",
        "کائناتی ریڈ شفٹ بمقابلہ ڈوپلر اثر (Cosmological Redshift vs Doppler): کہکشاؤں سے آنے والی روشنی کے سرخ ہونے کا سبب روایتی ڈوپلر اثر سے بنیادی طور پر مختلف کیوں ہے؟",
        ["روشنی کے سفر کے دوران کائنات کے زمان و مکان کی چادر کے خود پھیلنے کی وجہ سے روشنی کی طول موج کھنچ کر لمبی ہو جاتی ہے", "کہکشائیں خلا میں روشنی سے تیز بھاگ رہی ہیں", "خلا کی دھول نیلے رنگ کو سرخ کر دیتی ہے", "کشش ثقل روشنی کی رفتار کم کر دیتی ہے"],
        "روشنی کے سفر کے دوران کائنات کے زمان و مکان کی چادر کے خود پھیلنے کی وجہ سے روشنی کی طول موج کھنچ کر لمبی ہو جاتی ہے",
        "ڈوپلر اثر خلا کے اندر کسی گاڑی کے بھاگنے سے ہوتا ہے، جبکہ کائناتی ریڈ شفٹ میں خود وہ خلا پھیل جاتی ہے جس میں روشنی سفر کر رہی ہوتی ہے، جس سے اربوں سالوں میں فوٹون کھنچ کر سرخ ہو جاتا ہے۔"
    ),
    (
        "Why do Fast Radio Bursts (FRBs) from distant galaxies arrive with high frequencies reaching radio dishes earlier than low frequencies (Plasma Dispersion)?",
        ["Interstellar and intergalactic ionized plasma slows down lower frequencies more than higher frequencies proportional to electron column density", "High-frequency radio waves are physically lighter", "Low-frequency waves bounce off dark matter", "Telescopes process bass notes slower"],
        "Interstellar and intergalactic ionized plasma slows down lower frequencies more than higher frequencies proportional to electron column density",
        "Dispersion delay Delta t = 4.15 ms * DM * (nu_low^-2 - nu_high^-2). Free electrons in intergalactic plasma introduce frequency-dependent phase velocities, allowing astronomers to measure intervening cosmic matter.",
        "فاسٹ ریڈیو برسٹس (Fast Radio Bursts & Plasma Dispersion): اربوں نوری سال دور سے آنے والے ریڈیو دھماکوں میں اونچی فریکوئنسی والی آوازیں نچلی فریکوئنسی سے چند ملی سیکنڈ پہلے کیوں پہنچتی ہیں؟",
        ["راستے میں موجود آئنائزڈ گیس کا پلازما نچلی فریکوئنسی والی لہروں کو اونچی لہروں کے مقابلے میں زیادہ سست کر دیتا ہے", "اونچی فریکوئنسی والی لہریں وزنی نہیں ہوتیں", "نچلی لہریں تاریک مادے سے ٹکرا جاتی ہیں", "ٹیلی سکوپ دھیمی آوازیں دیر سے سنتی ہے"],
        ["راستے میں موجود آئنائزڈ گیس کا پلازما نچلی فریکوئنسی والی لہروں کو اونچی لہروں کے مقابلے میں زیادہ سست کر دیتا ہے", "اونچی فریکوئنسی والی لہریں وزنی نہیں ہوتیں", "نچلی لہریں تاریک مادے سے ٹکرا جاتی ہیں", "ٹیلی سکوپ دھیمی آوازیں دیر سے سنتی ہے"][0],
        "خلا مکمل خالی نہیں بلکہ اس میں آزاد الیکٹرانز کا پلازما ہوتا ہے۔ یہ پلازما لمبی لہروں کو روکتا ہے جس سے اونچی لہریں پہلے اور نچلی لہریں بعد میں پہنچتی ہیں، اور سیٹی جیسی گرتی ہوئی گونج پیدا ہوتی ہے۔"
    ),
    (
        "To a distant outside observer, an astronaut falling into a supermassive black hole appears to freeze at the event horizon forever. What does the astronaut actually experience?",
        ["The astronaut falls smoothly through the event horizon in a finite amount of proper time without freezing at all", "The astronaut stops moving in mid-air", "The astronaut bounces off the event horizon like rubber", "The astronaut turns into pure dark energy instantly"],
        "The astronaut falls smoothly through the event horizon in a finite amount of proper time without freezing at all",
        "Coordinate time t diverges to infinity at r = 2M for distant observers due to gravitational redshift. In the astronaut's co-moving proper time tau, crossing the horizon is smooth and uneventful.",
        "بلیک ہول میں گرنے کا منظر (Black Hole Event Horizon Infall): باہر کھڑے شخص کو خلاباز بلیک ہول کے افق پر ہمیشہ کے لیے جمتا نظر آتا ہے، مگر خود خلاباز کو کیا محسوس ہوتا ہے؟",
        ["خلاباز بغیر کسی رکاوٹ کے اپنے ذاتی وقت کے چند سیکنڈز میں افق کو پار کر کے سیدھا اندر گر جاتا ہے", "خلاباز فضا میں ہمیشہ کے لیے رک جاتا ہے", "خلاباز ربڑ کی طرح ٹکرا کر اچھل جاتا ہے", "خلاباز فوری طور پر تاریک توانائی بن جاتا ہے"],
        ["خلاباز بغیر کسی رکاوٹ کے اپنے ذاتی وقت کے چند سیکنڈز میں افق کو پار کر کے سیدھا اندر گر جاتا ہے", "خلاباز فضا میں ہمیشہ کے لیے رک جاتا ہے", "خلاباز ربڑ کی طرح ٹکرا کر اچھل جاتا ہے", "خلاباز فوری طور پر تاریک توانائی بن جاتا ہے"][0],
        "باہر والے کے لیے روشنی کی لہریں کھنچ کر اتنی سست اور مدہم ہو جاتی ہیں کہ تصویر رکتی ہوئی لگتی ہے، مگر خلاباز کی گھڑی عام رفتار سے چلتی رہتی ہے اور وہ بغیر رکے افق کے اندر داخل ہو جاتا ہے۔"
    ),
    (
        "What bizarre hybrid stellar object was proposed by Kip Thorne and Anna Żytkow (a Thorne-Żytkow Object)?",
        ["A red supergiant star that has swallowed a dense neutron star, housing the neutron star as its active central stellar core", "A star made of pure frozen diamond", "A black hole orbiting inside a comet", "A star held together by electrostatic glass"],
        "A red supergiant star that has swallowed a dense neutron star, housing the neutron star as its active central stellar core",
        "A binary collision leads to a red giant absorbing its neutron star companion. The degenerate neutron core provides gravitational energy via rp-process nucleosynthesis, mimicking a supergiant with unique chemical anomalies.",
        "تھورن زیٹکو آبجیکٹ (Thorne-Żytkow Object): کیپ تھورن اور اینا زیٹکو کا تجویز کردہ یہ انوکھا ہائبرڈ ستارہ کیا ہوتا ہے؟",
        ["ایک دیوہیکل سرخ ستارہ جس کے پیٹ کے اندر ایک مردہ نیوٹران ستارہ اس کے مرکزی مرکزے (Core) کے طور پر زندہ ہو", "خالص ہیرے کا بنا ستارہ", "دم دار ستارے میں قید بلیک ہول", "شیشے کی برقی طاقت سے جڑا ستارہ"],
        ["ایک دیوہیکل سرخ ستارہ جس کے پیٹ کے اندر ایک مردہ نیوٹران ستارہ اس کے مرکزی مرکزے (Core) کے طور پر زندہ ہو", "خالص ہیرے کا بنا ستارہ", "دم دار ستارے میں قید بلیک ہول", "شیشے کی برقی طاقت سے جڑا ستارہ"][0],
        "یہ ایک ستارے کے اندر دوسرا ستارہ ہے۔ جب ایک دیوہیکل ستارہ اپنے قریب گھومتے نیوٹران ستارے کو نگل لے، تو نیوٹران ستارہ اس کے دل میں بیٹھ کر اس کے پورے نظام کو توانائی دینے لگتا ہے۔"
    ),
    (
        "In theoretical astrophysics, what is a 'Kugelblitz'?",
        ["A black hole formed entirely from an extreme concentration of focused electromagnetic radiation (light) rather than matter", "A lightning bolt frozen in liquid helium", "A plasma weapon used by naval ships", "An asteroid composed of uranium"],
        "A black hole formed entirely from an extreme concentration of focused electromagnetic radiation (light) rather than matter",
        "In General Relativity, energy curves spacetime via the stress-energy tensor T_munu. Focusing sufficient radiation into a tiny volume traps light within its own gravitational Schwarzschild radius, forming a Kugelblitz.",
        "کوگل بلٹز (Kugelblitz - Light Black Hole): نظریاتی فزکس میں 'کوگل بلٹز' سے کیا مراد ہے؟",
        ["ایک ایسا بلیک ہول جو کسی مادی چیز سے نہیں بلکہ روشنی اور تابکاری کے شدید ترین ارتکاز سے کشش ثقل کے سکڑنے پر بنتا ہے", "مائع ہیلیم میں جمی ہوئی آسمانی بجلی", "بحری جہازوں کا پلازما ہتھیار", "یورینیم سے بنا شہابیہ"],
        ["ایک ایسا بلیک ہول جو کسی مادی چیز سے نہیں بلکہ روشنی اور تابکاری کے شدید ترین ارتکاز سے کشش ثقل کے سکڑنے پر بنتا ہے", "مائع ہیلیم میں جمی ہوئی آسمانی بجلی", "بحری جہازوں کا پلازما ہتھیار", "یورینیم سے بنا شہابیہ"][0],
        "آئن سٹائن کے مطابق توانائی بھی زمان و مکان کو موڑتی ہے۔ اگر آپ اربوں لیزرز کو ایک نقطے پر اتنا شدید مرتکز کر دیں کہ ان کی اپنی کشش روشنی کو ہی قید کر لے، تو بغیر کسی مادے کے بلیک ہول بن جائے گا۔"
    ),
    (
        "Why did Albert Einstein strongly object to the concept of 'Relativistic Mass' (the idea that an object gets physically heavier as it speeds up)?",
        ["Mass is an invariant scalar quantity; velocity alters relativistic momentum and energy, not the intrinsic rest mass m_0", "Moving objects lose atoms to friction", "Speed creates anti-gravity", "Mass measurements melt scales"],
        "Mass is an invariant scalar quantity; velocity alters relativistic momentum and energy, not the intrinsic rest mass m_0",
        "Einstein wrote that introducing relativistic mass m = gamma * m_0 is confusing and non-covariant. Modern physics defines mass strictly as invariant rest mass m = sqrt(E^2 - p^2 c^2) / c^2.",
        "اضافیتی کمیت پر آئن سٹائن کا اعتراض (Einstein on Relativistic Mass): البرٹ آئن سٹائن نے اس عام تصور کو غلط کیوں قرار دیا کہ 'تیز بھاگنے سے چیز کا مادی وزن بڑھ جاتا ہے'؟",
        ["کمیت ایک مستقل حقیقت ہے؛ رفتار صرف مومنٹم اور توانائی کو بڑھاتی ہے، خود مادی کمیت (Rest mass) کو تبدیل نہیں کرتی", "حرکت سے ایٹم رگڑ کر جھڑ جاتے ہیں", "رفتار اینٹی گریویٹی پیدا کرتی ہے", "پیمانہ پگھل جاتا ہے"],
        ["کمیت ایک مستقل حقیقت ہے؛ رفتار صرف مومنٹم اور توانائی کو بڑھاتی ہے، خود مادی کمیت (Rest mass) کو تبدیل نہیں کرتی", "حرکت سے ایٹم رگڑ کر جھڑ جاتے ہیں", "رفتار اینٹی گریویٹی پیدا کرتی ہے", "پیمانہ پگھل جاتا ہے"][0],
        "آئن سٹائن نے خود خط لکھ کر سمجھایا کہ یہ کہنا غلط ہے کہ چیز بھاری ہو گئی۔ اصل بات یہ ہے کہ اس کی توانائی اور مومنٹم میں اضافہ ہوتا ہے جس سے اس کی رفتار مزید بڑھانا مشکل ہوتا چلا جاتا ہے۔"
    ),
    (
        "Why does a massive intervening galaxy create a perfect, glowing circular ring of light around itself known as an 'Einstein Ring'?",
        ["A background light source, the foreground lens galaxy, and Earth are aligned in an exact, symmetrical straight line", "The galaxy burns ring-shaped hydrogen gas", "Cosmic dust forms a circular mirror", "Galaxy rotation flings stars into a halo"],
        "A background light source, the foreground lens galaxy, and Earth are aligned in an exact, symmetrical straight line",
        "Gravitational lensing bends light around a mass. If the source, lens, and observer share a collinear optical axis, axial symmetry deflects the distorted background wavefront into an Einstein ring with angular radius theta_E.",
        "آئن سٹائن کا دائرہ (Einstein Ring in Gravitational Lensing): خلا میں ایک کہکشاں کے گرد روشنی کا بالکل گول دائرہ دار چھلا کیسے بن جاتا ہے؟",
        ["جب پیچھے کی کہکشاں، سامنے کی کہکشاں اور زمین بالکل ایک سیدھی لکیر میں آ جائیں تو سامنے والی کہکشاں کی کشش ثقل پیچھے کی روشنی کو گول دائرے میں موڑ دیتی ہے", "کہکشاں گول گیس جلاتی ہے", "دھول نے گول آئینہ بنایا ہے", "کہکشاں کے گھماؤ نے تارے پھینکے ہیں"],
        ["جب پیچھے کی کہکشاں، سامنے کی کہکشاں اور زمین بالکل ایک سیدھی لکیر میں آ جائیں تو سامنے والی کہکشاں کی کشش ثقل پیچھے کی روشنی کو گول دائرے میں موڑ دیتی ہے", "کہکشاں گول گیس جلاتی ہے", "دھول نے گول آئینہ بنایا ہے", "کہکشاں کے گھماؤ نے تارے پھینکے ہیں"][0],
        "سامنے والی کہکشاں کی کشش ثقل ایک بڑے عدسے کا کام کرتی ہے۔ جب توازن بالکل 100 فیصد سیدھا ہو تو پیچھے کی کہکشاں کی روشنی چاروں طرف سے برابر مڑ کر ایک سنہری چھلے کی شکل اختیار کر لیتی ہے۔"
    ),
    (
        "How can astronomers detect solitary 'rogue planets' wandering in pitch-black interstellar space with zero host star (Gravitational Microlensing)?",
        ["The wandering planet's gravity briefly focuses and magnifies light from a background star like a cosmic magnifying glass", "The rogue planet reflects deep starlight", "The planet emits radioactive radio pulses", "Telescopes track planetary exhaust trails"],
        "The wandering planet's gravity briefly focuses and magnifies light from a background star like a cosmic magnifying glass",
        "Gravitational microlensing occurs when an unlit compact object passes in front of a background star. Its gravitational field bends light rays, producing a transient symmetric spike in apparent stellar brightness.",
        "آوارہ سیاروں کی کھوج (Gravitational Microlensing): بغیر کسی سورج کے اندھیرے میں اکیلے گھومتے آوارہ سیاروں کو سائنسدان زمین سے کیسے پکڑتے ہیں؟",
        ["جب وہ سیارہ کسی دور کے ستارے کے آگے سے گزرتا ہے تو اس کی کشش ثقل ایک عدسے کی طرح اس ستارے کی چمک کو چند گھنٹوں کے لیے تیز کر دیتی ہے", "سیارہ دور کے ستاروں کی روشنی لوٹاتا ہے", "سیارے سے ریڈیو لہریں نکلتی ہیں", "سیارے کے دھوئیں کے نشانات دیکھ کر"],
        ["جب وہ سیارہ کسی دور کے ستارے کے آگے سے گزرتا ہے تو اس کی کشش ثقل ایک عدسے کی طرح اس ستارے کی چمک کو چند گھنٹوں کے لیے تیز کر دیتی ہے", "سیارہ دور کے ستاروں کی روشنی لوٹاتا ہے", "سیارے سے ریڈیو لہریں نکلتی ہیں", "سیارے کے دھوئیں کے نشانات دیکھ کر"][0],
        "سیارہ خود بالکل کالا اور اندھا ہوتا ہے۔ مگر جب وہ دور دراز کے ستارے کے عین سامنے سے گزرتا ہے تو اس کی کشش کی بدولت اس ستارے کی روشنی کا گراف اچانک اوپر جاتا ہے، جس سے سیارے کے سائز کا پتہ چل جاتا ہے۔"
    ),
    (
        "What defines the boundaries of a planet's 'Hill Sphere' in celestial mechanics?",
        ["The region of space surrounding a body where its own gravitational attraction dominates over the gravitational attraction of its host star", "The atmosphere's boundary with deep space", "The distance where planetary magnetic fields end", "The orbital path of the outermost artificial satellite"],
        "The region of space surrounding a body where its own gravitational attraction dominates over the gravitational attraction of its host star",
        "The Hill sphere radius r_H = a * (1 - e) * (m / 3M)^(1/3) defines the zone of gravitational dominance. Moons orbiting outside the Hill sphere are eventually stripped away by solar tidal perturbations.",
        "ہل اسفیئر (The Hill Sphere in Orbital Mechanics): کسی سیارے کے گرد خلا کا وہ دائرہ کیا کہلاتا ہے جس کے اندر ہی کوئی چاند اس کے گرد گھوم سکتا ہے؟",
        ["سیارے کے ارد گرد خلا کا وہ علاقہ جہاں سیارے کی اپنی کشش ثقل سورج کی کشش ثقل پر حاوی ہوتی ہے اور چاند کو اپنے مدار میں سنبھال سکتی ہے", "فضا کی آخری حد", "مقناطیسی فیلڈ کا کنارہ", "مصنوعی سیاروں کا آخری راستہ"],
        ["سیارے کے ارد گرد خلا کا وہ علاقہ جہاں سیارے کی اپنی کشش ثقل سورج کی کشش ثقل پر حاوی ہوتی ہے اور چاند کو اپنے مدار میں سنبھال سکتی ہے", "فضا کی آخری حد", "مقناطیسی فیلڈ کا کنارہ", "مصنوعی سیاروں کا آخری راستہ"][0],
        "اگر کوئی چاند اس دائرے سے باہر نکل جائے تو سورج کی کشش اسے سیارے سے چھین کر اپنے مدار میں کھینچ لے گی۔ زمین کا ہل اسفیئر تقریباً 15 لاکھ کلومیٹر تک پھیلا ہوا ہے۔"
    ),
    (
        "Why do Trojan Asteroids stay perpetually clustered 60 degrees ahead (L4) and 60 degrees behind (L5) Jupiter without falling into the planet or drifting away?",
        ["Coriolis forces in the rotating reference frame stabilize orbits around the equilateral Lagrange points against gravitational perturbations", "Jupiter pulls asteroids with magnetic cables", "Solar wind pins asteroids against space ice", "Electrostatic charge repels the asteroids"],
        "Coriolis forces in the rotating reference frame stabilize orbits around the equilateral Lagrange points against gravitational perturbations",
        "L4 and L5 are potential maxima in the effective potential energy surface. Coriolis acceleration balances gravitational and centrifugal drifts for mass ratios M1/M2 > 24.96, dynamically trapping Trojan swarms.",
        "ٹروجن شہابیے اور ایل 4، ایل 5 پوائنٹس (Trojan Asteroids Stability): مشتری سیارے سے 60 ڈگری آگے اور پیچھے شہابیوں کے غول ہمیشہ اپنے مدار میں محفوظ کیوں رہتے ہیں؟",
        ["گھومتے ہوئے نظام میں پیدا ہونے والی کوریولس قوت ان لگرینج پوائنٹس پر شہابیوں کے بہاؤ کو خود بخود متوازن اور مقفل کر دیتی ہے", "مشتری مقناطیسی تاروں سے کھینچتا ہے", "سورج کی ہوا انہیں برف سے چپکاتی ہے", "جامد چارج انہیں دور رکھتا ہے"],
        ["گھومتے ہوئے نظام میں پیدا ہونے والی کوریولس قوت ان لگرینج پوائنٹس پر شہابیوں کے بہاؤ کو خود بخود متوازن اور مقفل کر دیتی ہے", "مشتری مقناطیسی تاروں سے کھینچتا ہے", "سورج کی ہوا انہیں برف سے چپکاتی ہے", "جامد چارج انہیں دور رکھتا ہے"][0],
        "سورج اور مشتری کی باہمی کشش ان دو تکونی مقامات پر ایسا کنواں بناتی ہے جہاں اگر کوئی پتھر ہلنے کی کوشش کرے تو کوریولس اثر اسے واپس اسی محفوظ چکر میں دھکیل دیتا ہے۔"
    ),
    (
        "Why does sunlight subtly push and alter the orbital trajectories of small rotating asteroids over millions of years (the Yarkovsky Effect)?",
        ["The asteroid warms up on its afternoon side and re-radiates thermal infrared photons with a directional recoil thrust", "Sunlight knocks electrons off the asteroid", "Solar wind physically erodes the asteroid surface", "Solar flares melt the asteroid iron core"],
        "The asteroid warms up on its afternoon side and re-radiates thermal infrared photons with a directional recoil thrust",
        "Due to thermal inertia, an asteroid's hottest spot is not at local noon, but in the afternoon. Emitting anisotropic infrared thermal photons imparts a net reaction force, altering semi-major axis over millions of years.",
        "یارکووسکی اثر اور شہابیوں کا راستہ (The Yarkovsky Effect): سورج کی دھوپ لاکھوں سالوں میں گھومتے ہوئے شہابیوں کا مدار کیسے بدل دیتی ہے؟",
        ["شہابیے کا دوپہر والا رخ زیادہ گرم ہو کر انفراریڈ فوٹونز خارج کرتا ہے جس کا باریک الٹا دھکا شہابیے کے مدار کو آہستہ آہستہ موڑ دیتا ہے", "دھوپ الیکٹران اڑا دیتی ہے", "سورج کی ہوا شہابیے کو گھس دیتی ہے", "شعلے لوہے کو پگھلا دیتے ہیں"],
        ["شہابیے کا دوپہر والا رخ زیادہ گرم ہو کر انفراریڈ فوٹونز خارج کرتا ہے جس کا باریک الٹا دھکا شہابیے کے مدار کو آہستہ آہستہ موڑ دیتا ہے", "دھوپ الیکٹران اڑا دیتی ہے", "سورج کی ہوا شہابیے کو گھس دیتی ہے", "شعلے لوہے کو پگھلا دیتے ہیں"][0],
        "شہابیے پر دن کی گرمی تھوڑی دیر بعد شام کے رخ سے خارج ہوتی ہے۔ حرارت کا یہ اخراج فوٹونز کے باریک راکٹ کا کام کرتا ہے جو کروڑوں سالوں میں پتھر کو کھینچ کر زمین کی طرف بھی دھکیل سکتا ہے۔"
    ),
    (
        "Why does a rocket engine burn generate significantly more total kinetic energy when fired at periapsis (closest approach and highest orbital speed) than at apoapsis (the Oberth Effect)?",
        ["The kinetic energy gained scales with the vehicle's instantaneous velocity: Delta KE = m * v * Delta v + 0.5 * m * (Delta v)^2", "Periapsis has zero atmospheric air resistance", "Planetary gravity acts as rocket fuel", "Rocket nozzles expand at high speeds"],
        "The kinetic energy gained scales with the vehicle's instantaneous velocity: Delta KE = m * v * Delta v + 0.5 * m * (Delta v)^2",
        "Hermann Oberth discovered that because kinetic energy is proportional to v^2, applying Delta v at higher speed v converts chemical propellant potential into vehicle kinetic energy far more efficiently.",
        "اوبرتھ اثر اور راکٹ کی رفتار (The Oberth Effect): راکٹ کے انجن کو اس وقت چلانے سے سب سے زیادہ توانائی کیوں ملتی ہے جب وہ سیارے کے قریب ترین اور تیز ترین رفتار پر ہو؟",
        ["حاصل ہونے والی حرکی توانائی راکٹ کی اس وقت کی رفتار سے ضرب کھاتی ہے؛ جتنی زیادہ رفتار پر دھکا لگے گا اتنا ہی زیادہ کائنیٹک انرجی کا اضافہ ہوگا", "قریب ترین مقام پر ہوا کی رکاوٹ نہیں ہوتی", "کشش ثقل ایندھن کا کام کرتی ہے", "نوزل تیز رفتار پر پھیل جاتی ہے"],
        ["حاصل ہونے والی حرکی توانائی راکٹ کی اس وقت کی رفتار سے ضرب کھاتی ہے؛ جتنی زیادہ رفتار پر دھکا لگے گا اتنا ہی زیادہ کائنیٹک انرجی کا اضافہ ہوگا", "قریب ترین مقام پر ہوا کی رکاوٹ نہیں ہوتی", "کشش ثقل ایندھن کا کام کرتی ہے", "نوزل تیز رفتار پر پھیل جاتی ہے"][0],
        "راکٹ کی انرجی کا اضافہ رفتار کے اسکوائر (v^2) پر منحصر ہے۔ تیز ترین مقام پر ایندھن جلانے سے ایندھن کی اپنی کائنیٹک انرجی بھی راکٹ کو منتقل ہو جاتی ہے، جس سے کم ایندھن میں زیادہ رفتار ملتی ہے۔"
    ),
    (
        "Why did the mysterious decelerating trajectory drift of the Pioneer 10 and 11 spacecraft puzzle physicists for decades until solved in 2012 (the Pioneer Anomaly)?",
        ["Asymmetric thermal radiation: heat from onboard radioisotope thermoelectric generators bounced off the backside of the high-gain dish, producing a tiny recoil force", "Dark matter friction dragged the probes", "Newton's gravitational constant G changes in deep space", "Interstellar gas clogged probe thrusters"],
        "Asymmetric thermal radiation: heat from onboard radioisotope thermoelectric generators bounced off the backside of the high-gain dish, producing a tiny recoil force",
        "Slava Turyshev resolved the anomaly: anisotropic thermal emission from electrical boxes and RTGs reflected off the parabolic antenna, generating an unmodeled thermal photon recoil acceleration a_P = -(8.74 x 10^-10) m/s^2 toward the Sun.",
        "پائنیر خلائی جہازوں کا معمہ (The Pioneer Anomaly): نظام شمسی سے باہر جاتے ہوئے پائنیر جہازوں کی رفتار میں نامعلوم کمی کا معمہ 30 سال بعد کیسے حل ہوا؟",
        ["جہاز کی ایٹمی بیٹری کی گرمی کے فوٹونز اینٹینا کے پچھلے حصے سے ٹکرا کر سورج کے رخ پر باریک فوٹون راکٹ جیسا الٹا دھکا لگا رہے تھے", "ڈارک میٹر کی رگڑ جہاز کو روک رہی تھی", "خلا میں کشش ثقل کا قانون بدل گیا تھا", "گیس نے انجن کو جام کر دیا تھا"],
        ["جہاز کی ایٹمی بیٹری کی گرمی کے فوٹونز اینٹینا کے پچھلے حصے سے ٹکرا کر سورج کے رخ پر باریک فوٹون راکٹ جیسا الٹا دھکا لگا رہے تھے", "ڈارک میٹر کی رگڑ جہاز کو روک رہی تھی", "خلا میں کشش ثقل کا قانون بدل گیا تھا", "گیس نے انجن کو جام کر دیا تھا"][0],
        "سب سمجھے کہ کشش ثقل کے نئے قوانین دریافت ہو گئے ہیں۔ مگر کمپیوٹر ماڈل نے ثابت کیا کہ بیٹری سے اڑنے والی گرمی کی باریک لہریں جب اینٹینا کی پشت سے پلٹتی تھیں تو وہ جہاز کو معمولی سا پیچھے کھینچتی تھیں۔"
    ),
    (
        "How does a spacecraft gain immense speed from a Gravitational Slingshot (Gravity Assist) around a moving planet without violating conservation of energy?",
        ["The spacecraft steals a tiny fraction of the planet's vast orbital momentum around the Sun, boosting its own heliocentric speed", "The planet's magnetic field repels the spacecraft like a railgun", "Atmospheric friction catapults the spacecraft", "Solar flares ignite leftover rocket fuel"],
        "The spacecraft steals a tiny fraction of the planet's vast orbital momentum around the Sun, boosting its own heliocentric speed",
        "In the planet's rest frame, the encounter is elastic (entry speed = exit speed). In the Sun's frame, the spacecraft exits with v_final ~ v_initial + 2 * v_planet, draining an imperceptible amount of the planet's orbital kinetic energy.",
        "ثقلی غلیل یا گریویٹی اسسٹ (Gravitational Slingshot): مشتری کے پاس سے گزر کر خلائی جہاز اپنی رفتار میں ہزاروں میل فی گھنٹہ کا مفت اضافہ کیسے کر لیتا ہے؟",
        ["جہاز سورج کے گرد مشتری کے گھومنے کے بے پناہ کائناتی مومنٹم کا ایک معمولی سا حصہ چرا لیتا ہے جس سے اس کی اپنی رفتار بڑھ جاتی ہے", "مشتری کا مقناطیس جہاز کو بندوق کی طرح چلاتا ہے", "فضا کی رگڑ جہاز کو اچھالتی ہے", "شعلے ایندھن کو جلا دیتے ہیں"],
        ["جہاز سورج کے گرد مشتری کے گھومنے کے بے پناہ کائناتی مومنٹم کا ایک معمولی سا حصہ چرا لیتا ہے جس سے اس کی اپنی رفتار بڑھ جاتی ہے", "مشتری کا مقناطیس جہاز کو بندوق کی طرح چلاتا ہے", "فضا کی رگڑ جہاز کو اچھالتی ہے", "شعلے ایندھن کو جلا دیتے ہیں"][0],
        "مشتری کے لحاظ سے رفتار وہی رہتی ہے، مگر سورج کے فریم میں جہاز مشتری کی اپنی رفتار کو اپنے اندر سمیٹ کر آگے نکلتا ہے۔ اس سے مشتری کی رفتار کھربویں حصے کم ہوتی ہے اور جہاز طوفان بن جاتا ہے۔"
    ),
    (
        "Why did rocket scientist Konstantin Tsiolkovsky refer to his famous rocket equation Delta v = v_e * ln(m_0 / m_f) as the 'tyranny of the rocket equation'?",
        ["To add payload or speed, the required fuel mass increases exponentially, because the rocket must carry fuel to lift fuel", "Rocket engines overheat after 3 minutes", "Fuel tanks rust in vacuum", "Gravity increases with rocket mass"],
        "To add payload or speed, the required fuel mass increases exponentially, because the rocket must carry fuel to lift fuel",
        "Because mass ratio m_0 / m_f = exp(Delta v / v_e) is exponential, achieving orbital velocity (~8 km/s) with chemical rockets (v_e ~ 3-4 km/s) requires ~90% of the launch vehicle mass to be pure propellant.",
        "سیالکووسکی راکٹ مساوات اور ایندھن کا بوجھ (Tyranny of the Rocket Equation): راکٹ کے سائنسدان اس قانون کو خلائی سفر پر راکٹ کی سب سے بڑی غلامی کیوں کہتے ہیں؟",
        ["رفتار یا وزن بڑھانے کے لیے ایندھن کا وزن حسابی طور پر ضرب کھا کر ایکسپونینشل بڑھتا ہے، کیونکہ اضافی ایندھن کو اٹھانے کے لیے مزید ایندھن لادنا پڑتا ہے", "انجن تین منٹ بعد گرم ہو جاتے ہیں", "ٹینک خلا میں زنگ آلود ہوتے ہیں", "کشش ثقل وزن کے ساتھ بڑھتی ہے"],
        ["رفتار یا وزن بڑھانے کے لیے ایندھن کا وزن حسابی طور پر ضرب کھا کر ایکسپونینشل بڑھتا ہے، کیونکہ اضافی ایندھن کو اٹھانے کے لیے مزید ایندھن لادنا پڑتا ہے", "انجن تین منٹ بعد گرم ہو جاتے ہیں", "ٹینک خلا میں زنگ آلود ہوتے ہیں", "کشش ثقل وزن کے ساتھ بڑھتی ہے"][0],
        "اگر آپ کو تھوڑا سا سامان مدار میں بھیجنا ہو تو راکٹ کا 90 فیصد وزن خالص ایندھن ہونا لازمی ہے۔ زیادہ سامان کے لیے مزید ایندھن چاہیے، اور اس ایندھن کو اٹھانے کے لیے مزید ایندھن، جس سے راکٹ پہاڑ بن جاتا ہے۔"
    ),
    (
        "Why do Deep Space ion thrusters deliver only the gentle thrust equivalent to the weight of a sheet of paper, yet propel probes to distant planets faster than chemical rockets?",
        ["Ion thrusters achieve extraordinary specific impulse and exhaust velocities (30 to 50 km/s), operating continuously for years", "Chemical rockets are illegal in deep space", "Ion engines use solar panels to reflect sunlight", "Space vacuum dissolves xenon gas"],
        "Ion thrusters achieve extraordinary specific impulse and exhaust velocities (30 to 50 km/s), operating continuously for years",
        "While thrust F = m_dot * v_e is tiny due to low mass flow rate m_dot, exhaust velocity v_e is 10x higher than chemical combustion. Firing uninterrupted for 10,000 hours accumulates immense total Delta v.",
        "آئن انجن کی رفتار (Ion Propulsion Specific Impulse): ایک کاغذ کے برابر ہلکا سا دھکا لگانے والا آئن انجن کیمیائی راکٹوں کے مقابلے میں خلائی جہاز کو اتنی تیز رفتاری کیسے دے دیتا ہے؟",
        ["آئن انجن ایندھن کے ذرات کو 30 سے 50 کلومیٹر فی سیکنڈ کی بھیانک رفتار سے باہر پھینکتے ہیں اور برسوں تک مسلسل بغیر رکے چلتے رہتے ہیں", "کیمیائی راکٹ خلا میں ممنوع ہیں", "وہ شیشوں سے دھوپ پلٹاتے ہیں", "خلا گیس کو گھول دیتی ہے"],
        ["آئن انجن ایندھن کے ذرات کو 30 سے 50 کلومیٹر فی سیکنڈ کی بھیانک رفتار سے باہر پھینکتے ہیں اور برسوں تک مسلسل بغیر رکے چلتے رہتے ہیں", "کیمیائی راکٹ خلا میں ممنوع ہیں", "وہ شیشوں سے دھوپ پلٹاتے ہیں", "خلا گیس کو گھول دیتی ہے"][0],
        "عام راکٹ چند منٹوں میں سارا ایندھن پھونک کر بند ہو جاتا ہے۔ آئن انجن بجلی سے ایٹمز کو تیز رفتار بندوق کی طرح سالہا سال تک مسلسل پھینکتا رہتا ہے، جس سے جہاز کی رفتار ہر روز تیز تر ہوتی چلی جاتی ہے۔"
    ),
    (
        "How can a Solar Sail propel a spacecraft across interstellar space without carrying a single drop of fuel on board?",
        ["Reflecting photons transfer twice their momentum (p = 2E/c) to the reflective sail via electromagnetic radiation pressure", "Solar wind blows the sail like ocean wind on canvas", "The sail generates electrostatic lightning bolts", "Sunlight charges solar batteries to run fans"],
        "Reflecting photons transfer twice their momentum (p = 2E/c) to the reflective sail via electromagnetic radiation pressure",
        "Photons carry momentum p = E/c. A perfectly reflecting mirror rebounds photons, imparting momentum Delta p = 2 * E / c. Continuous radiation pressure (~9 micro-Newtons/m^2 near Earth) accelerates the spacecraft continuously.",
        "شمسی بادبان (Solar Sail Propulsion): بغیر کسی ایک قطرہ ایندھن کے شمسی بادبان سے لیس جہاز خلا کی گہرائیوں میں کیسے دوڑتا ہے؟",
        ["چمکدار بادبان سے ٹکرا کر پلٹنے والے روشنی کے فوٹونز آئینے کو اپنے مومنٹم کا دگنا دھکا (2E/c) منتقل کرتے ہیں", "سورج کی ہوا کپڑے کو اڑاتی ہے", "بادبان بجلی کی چنگاریاں چھوڑتا ہے", "دھوپ سے پنکھے چلتے ہیں"],
        ["چمکدار بادبان سے ٹکرا کر پلٹنے والے روشنی کے فوٹونز آئینے کو اپنے مومنٹم کا دگنا دھکا (2E/c) منتقل کرتے ہیں", "سورج کی ہوا کپڑے کو اڑاتی ہے", "بادبان بجلی کی چنگاریاں چھوڑتا ہے", "دھوپ سے پنکھے چلتے ہیں"][0],
        "روشنی بے وزن لگتی ہے مگر اس کے پاس مومنٹم ہوتا ہے۔ جب سورج کے اربوں کھربوں فوٹون چاندی جیسے پتلے بادبان سے ٹکرا کر پلٹتے ہیں تو وہ مستقل دھکا لگاتے ہیں جو جہاز کو تیز ترین رفتار تک پہنچا دیتا ہے۔"
    ),
    (
        "How did ground-based astronomical telescopes using Adaptive Optics achieve sharper image clarity than the Hubble Space Telescope?",
        ["A laser guide star measures atmospheric wavefront distortion, and a computer deforms a flexible mirror 1,000 times per second to cancel turbulence", "Ground telescopes use larger computer screens", "Engineers vacuum-seal the observatory dome", "Air turbulence freezes at midnight"],
        "A laser guide star measures atmospheric wavefront distortion, and a computer deforms a flexible mirror 1,000 times per second to cancel turbulence",
        "Atmospheric turbulence scrambles wavefronts (Fried parameter r_0). Adaptive optics measures distortion using a sodium laser guide star and uses piezoelectric actuators to warp a thin mirror, restoring the diffraction limit.",
        "ایڈاپٹیو آپٹکس اور دوربینیں (Adaptive Optics in Astronomy): زمین پر لگی دوربینیں فضا کے بگاڑ کو مٹا کر ہبل خلائی دوربین سے بھی زیادہ شفاف تصویر کیسے کھینچ لیتی ہیں؟",
        ["آسمان پر لیزر مار کر ہوا کی لرزش کو ناپا جاتا ہے اور کمپیوٹر لچکدار آئینے کو فی سیکنڈ ایک ہزار بار موڑ کر فضا کے بگاڑ کو بالکل زائل کر دیتا ہے", "زمین پر بڑی اسکرینیں ہوتی ہیں", "گنبد کو ویکیوم کیا جاتا ہے", "ہوا رات کو جم جاتی ہے"],
        ["آسمان پر لیزر مار کر ہوا کی لرزش کو ناپا جاتا ہے اور کمپیوٹر لچکدار آئینے کو فی سیکنڈ ایک ہزار بار موڑ کر فضا کے بگاڑ کو بالکل زائل کر دیتا ہے", "زمین پر بڑی اسکرینیں ہوتی ہیں", "گنبد کو ویکیوم کیا جاتا ہے", "ہوا رات کو جم جاتی ہے"][0],
        "تارے فضا کی گرم ٹھنڈی ہوا سے جھلملاتے اور دھندلے ہوتے ہیں۔ ایڈاپٹیو آپٹکس کا آئینہ اتنی تیز رفتاری سے اپنی شکل بدلتا ہے کہ وہ ہوا کی خرابی کا عین الٹ عکس بنا کر تصویر کو مکمل کرسٹل شفاف کر دیتا ہے۔"
    ),
    (
        "How did the Event Horizon Telescope capture the historic first direct image of the supermassive black hole in galaxy M87 in 2019?",
        ["By combining synchronized radio dishes across the entire globe using Very Long Baseline Interferometry to synthesize an Earth-sized virtual telescope", "By sending a robotic probe to the M87 event horizon", "By using a giant space laser reflector", "By measuring X-rays from astronaut visors"],
        "By combining synchronized radio dishes across the entire globe using Very Long Baseline Interferometry to synthesize an Earth-sized virtual telescope",
        "Angular resolution theta ~ lambda / D. By synchronizing radio observatories across Hawaii, Chile, Europe, and the South Pole via atomic clocks, the EHT synthesized an aperture D equal to Earth's diameter, resolving 20 microarcseconds.",
        "ایونٹ ہورائزن ٹیلی سکوپ اور بلیک ہول کی تصویر (Event Horizon Telescope): 2019 میں سائنسدانوں نے کہکشاں M87 کے بلیک ہول کے سائے کی پہلی تصویر کیسے کھینچی؟",
        ["پوری دنیا کے مختلف براعظموں میں لگی ریڈیو دوربینوں کو ایٹمی گھڑیوں سے جوڑ کر زمین کے سائز کی ایک واحد ورچوئل دوربین بنا کر", "بلیک ہول میں کیمرہ بھیج کر", "خلا میں بڑا لیزر آئینہ لگا کر", "خلابازوں کے ماسک سے ایکس رے ناپ کر"],
        ["پوری دنیا کے مختلف براعظموں میں لگی ریڈیو دوربینوں کو ایٹمی گھڑیوں سے جوڑ کر زمین کے سائز کی ایک واحد ورچوئل دوربین بنا کر", "بلیک ہول میں کیمرہ بھیج کر", "خلا میں بڑا لیزر آئینہ لگا کر", "خلابازوں کے ماسک سے ایکس رے ناپ کر"][0],
        "بلیک ہول کا سایہ اتنا چھوٹا تھا جیسے چاند پر رکھی سیب کی تصویر لینا۔ سائنسدانوں نے چلی، ہوائی اور قطب جنوبی کی دوربینوں کا ڈیٹا آپس میں ملا کر پوری زمین جتنا بڑا خیالی عدسہ بنا کر یہ تصویر مکمل کی۔"
    ),
    (
        "How did physicists discover a previously unknown 30-meter hidden void inside the Great Pyramid of Giza in 2017 without drilling a single stone (Muon Tomography)?",
        ["Cosmic ray muons pass through stone but get absorbed differently depending on density; detectors recorded excess muon flux through the empty void", "By sending ultrasound waves through pyramid tombs", "By measuring ground temperature infrared cameras", "By digging secret tunnels with robots"],
        "Cosmic ray muons pass through stone but get absorbed differently depending on density; detectors recorded excess muon flux through the empty void",
        "Muons created by cosmic rays penetrate hundreds of meters of rock. Nuclear emulsion plates and scintillator trackers measured directional muon attenuation: an empty void allows more muons to pass, revealing its 3D geometry.",
        "میوآن ٹوموگرافی اور اہرام مصر کا خفیہ کمرہ (Muon Tomography in Giza): 2017 میں سائنسدانوں نے اہرام مصر کا ایک بھی پتھر ہلائے بغیر اس کے اندر 30 میٹر لمبا خفیہ کمرہ کیسے ڈھونڈ نکالا؟",
        ["کائناتی شعاعوں سے پیدا ہونے والے میوآن ذرات پتھروں کے اندر سے گزرتے ہیں؛ کھوکھلی جگہ سے زیادہ ذرات گزرنے کو ڈیٹیکٹرز نے ریکارڈ کر کے کمرے کا نقشہ بنا لیا", "الٹرا ساؤنڈ لہریں پھینک کر", "انفراریڈ کیمروں سے گرمی ناپ کر", "روبوٹس سے خفیہ سرنگیں کھود کر"],
        ["کائناتی شعاعوں سے پیدا ہونے والے میوآن ذرات پتھروں کے اندر سے گزرتے ہیں؛ کھوکھلی جگہ سے زیادہ ذرات گزرنے کو ڈیٹیکٹرز نے ریکارڈ کر کے کمرے کا نقشہ بنا لیا", "الٹرا ساؤنڈ لہریں پھینک کر", "انفراریڈ کیمروں سے گرمی ناپ کر", "روبوٹس سے خفیہ سرنگیں کھود کر"][0],
        "میوآن ذرات قدرتی ایکسرے کی طرح کام کرتے ہیں۔ اگر سامنے ٹھوس پتھر ہو تو وہ رک جاتے ہیں، مگر جہاں اندر خالی کمرہ تھا وہاں سے زیادہ ذرات پار نکل گئے۔ سینسرز نے اس فرق سے کمرے کا تھری ڈی ماڈل بنا دیا۔"
    ),
    (
        "How does a medical PET Scan (Positron Emission Tomography) pinpoint cancerous tumors inside the human body with sub-millimeter precision?",
        ["Injected radioactive tracer emits positrons that annihilate with electrons, releasing twin 511 keV gamma rays at 180 degrees detected in coincidence", "X-ray lasers incinerate cancer cells directly", "Magnetic fields spin tumor iron atoms", "Ultrasound crystals detect tumor sounds"],
        "Injected radioactive tracer emits positrons that annihilate with electrons, releasing twin 511 keV gamma rays at 180 degrees detected in coincidence",
        "Fluorodeoxyglucose (FDG) concentrates in high-glucose tumors. Positron beta+ decay leads to e+ e- annihilation, shooting two collinear 511 keV gamma photons detected simultaneously by a circular ring, localizing the line of response.",
        "پی ای ٹی اسکین اور اینٹی میٹر کا علاج (PET Scan & Positron Annihilation): ہسپتالوں میں کینسر کی رسولی کو نینو میٹر کی درستگی کے ساتھ تلاش کرنے میں اینٹی میٹر کیسے مدد کرتا ہے؟",
        ["جسم میں لگائے گئے گلوکوز کے ذرے پوزیٹران (اینٹی میٹر) چھوڑتے ہیں جو الیکٹران سے ٹکرا کر 180 ڈگری پر دو گاما شعاعیں نکالتے ہیں جن کو کیمرہ فوراً پکڑ لیتا ہے", "لیزر شعاعیں رسولی کو جلا دیتی ہیں", "مقناطیس کینسر کا لوہا گھماتا ہے", "الٹرا ساؤنڈ رسولی کی آواز سنتا ہے"],
        ["جسم میں لگائے گئے گلوکوز کے ذرے پوزیٹران (اینٹی میٹر) چھوڑتے ہیں جو الیکٹران سے ٹکرا کر 180 ڈگری پر دو گاما شعاعیں نکالتے ہیں جن کو کیمرہ فوراً پکڑ لیتا ہے", "لیزر شعاعیں رسولی کو جلا دیتی ہیں", "مقناطیس کینسر کا لوہا گھماتا ہے", "الٹرا ساؤنڈ رسولی کی آواز سنتا ہے"][0],
        "کینسر تیزی سے گلوکوز کھاتا ہے۔ جب اس میں ملا پوزیٹران جسم کے الیکٹران سے ٹکراتا ہے تو وہ مکمل فنا ہو کر مخالف رخ پر دو گاما فوٹون بھیجتا ہے۔ دونوں شعاعوں کے ملنے کا مقام عین رسولی کی درست جگہ بتا دیتا ہے۔"
    ),
    (
        "Why does an MRI machine make deafening acoustic knocking and banging sounds during medical imaging of the brain?",
        ["Lorentz forces: heavy electric current pulses switching through gradient coils inside the 3-Tesla magnetic field cause the coils to physically flex and bang against their mounts", "The patient's skull bones echo radio signals", "Liquid helium boils into gas bubbles", "Radio antennas spark against shielding"],
        "Lorentz forces: heavy electric current pulses switching through gradient coils inside the 3-Tesla magnetic field cause the coils to physically flex and bang against their mounts",
        "Gradient coils rapidly toggle magnetic gradients for spatial encoding. Massive currents (hundreds of amps) in a strong 3T field generate intense oscillatory Lorentz forces (F = I * L x B), mechanically hammering coil mounts at acoustic frequencies.",
        "ایم آر آئی مشین کی خوفناک کھٹ کھٹ کی آواز (MRI Acoustic Noise Origin): دماغ کا ایم آر آئی کرواتے وقت مشین میں ہتھوڑے لگنے جیسی بھیانک آوازیں کیوں گونجتی ہیں؟",
        ["طاقتور مقناطیس کے اندر جب کوائلز میں کرنٹ کے تیز جھٹکے دیے جاتے ہیں تو لارینٹز فورس تانبے کے فریم کو زور زور سے اپنے اڈوں پر پٹختی ہے", "کھوپڑی کی ہڈیاں ریڈیو گونج پیدا کرتی ہیں", "ہیلیم گیس بلبلے بناتی ہے", "اینٹینا سے چنگاریاں نکلتی ہیں"],
        ["طاقتور مقناطیس کے اندر جب کوائلز میں کرنٹ کے تیز جھٹکے دیے جاتے ہیں تو لارینٹز فورس تانبے کے فریم کو زور زور سے اپنے اڈوں پر پٹختی ہے", "کھوپڑی کی ہڈیاں ریڈیو گونج پیدا کرتی ہیں", "ہیلیم گیس بلبلے بناتی ہے", "اینٹینا سے چنگاریاں نکلتی ہیں"][0],
        "یہ کوئی اسپیکر کی آواز نہیں ہوتی۔ 3 ٹیسلا کے دیوہیکل مقناطیس میں جب ہزاروں ایمپیئر کرنٹ آن آف ہوتا ہے تو فزکس کی مقناطیسی قوت تانبے کے پائپوں کو اتنی شدت سے جھنجھوڑتی ہے کہ وہ دھاتی ہتھوڑوں کی طرح بجتے ہیں۔"
    ),
    (
        "How can Transcranial Magnetic Stimulation (TMS) painlessly make a person's thumb twitch or temporarily disrupt speech without touching the brain?",
        ["Faraday electromagnetic induction: a pulsed magnetic field coil placed against the scalp induces localized electrical currents in underlying cortical neurons", "Static electricity jumps through hair follicles", "Magnetic fields pull blood iron into the thumb", "Sound waves resonate with nerve endings"],
        "Faraday electromagnetic induction: a pulsed magnetic field coil placed against the scalp induces localized electrical currents in underlying cortical neurons",
        "A figure-8 coil pulses a 2-Tesla field in ~100 microseconds. By Faraday's Law curl(E) = -dB/dt, the rapid magnetic flux change induces an electric field in cortical tissue, depolarizing neuronal axon membranes and triggering action potentials.",
        "ٹی ایم ایس اور دماغ پر مقناطیسی قابو (Transcranial Magnetic Stimulation): سر کو چھوئے بغیر مقناطیسی کوائل کے ذریعے انسان کے انگوٹھے کو خود بخود کیسے ہلایا جا سکتا ہے؟",
        ["فیراڈے کے انڈکشن کے قانون کے تحت مقناطیسی فیلڈ کے تیز جھٹکے کھوپڑی کے اندر دماغ کے مخصوص نیورونز میں برقی کرنٹ پیدا کر کے ان کو حرکت پر مجبور کر دیتے ہیں", "جامد بجلی بالوں سے اندر کودتی ہے", "مقناطیس خون کے لوہے کو کھینچتا ہے", "صوتی لہریں رگوں کو چھوتی ہیں"],
        ["فیراڈے کے انڈکشن کے قانون کے تحت مقناطیسی فیلڈ کے تیز جھٹکے کھوپڑی کے اندر دماغ کے مخصوص نیورونز میں برقی کرنٹ پیدا کر کے ان کو حرکت پر مجبور کر دیتے ہیں", "جامد بجلی بالوں سے اندر کودتی ہے", "مقناطیس خون کے لوہے کو کھینچتا ہے", "صوتی لہریں رگوں کو چھوتی ہیں"][0],
        "کھوپڑی ہڈی ہے جس سے بجلی نہیں گزر سکتی مگر مقناطیس بے روک ٹوک پار نکل جاتا ہے۔ مقناطیسی لہر اندر جا کر دماغ کے موٹر حصے میں فوری بجلی پیدا کرتی ہے جو تار کی طرح سگنل بھیج کر ہاتھ کو ہلا دیتی ہے۔"
    ),
    (
        "How does revolutionary Optogenetics allow neuroscientists to turn specific memories and behaviors on and off using pulses of blue laser light?",
        ["Light-sensitive microbial opsin ion channels (Channelrhodopsin-2) are genetically inserted into specific neurons, causing them to fire upon blue illumination", "Light burns away bad memories thermally", "Blue lasers heat neurons to trigger neurotransmitters", "Photons replace blood cells in cerebral veins"],
        "Light-sensitive microbial opsin ion channels (Channelrhodopsin-2) are genetically inserted into specific neurons, causing them to fire upon blue illumination",
        "Ed Boyden and Karl Deisseroth introduced ChR2 genes via viral vectors. Blue light (470 nm) gates the opsin ion channel, driving rapid inward Na+ flux that depolarizes the target neuron within milliseconds.",
        "آپٹوجینیٹکس اور روشنی سے یادوں کا کنٹرول (Optogenetics): سائنسدان نیلے رنگ کی لیزر کی چمک سے مخصوص یادوں اور رویوں کو کیسے آن اور آف کر لیتے ہیں؟",
        ["جینیاتی انجینیئرنگ کے ذریعے نیورونز میں روشنی کے حساس پروٹین (Channelrhodopsin) داخل کیے جاتے ہیں جو نیلی روشنی پڑتے ہی کرنٹ چھوڑ کر خلیے کو بیدار کر دیتے ہیں", "روشنی بری یادوں کو جلا دیتی ہے", "لیزر نیورونز کو گرم کر کے متحرک کرتی ہے", "فوٹونز خون کے خلیوں کی جگہ لے لیتے ہیں"],
        ["جینیاتی انجینیئرنگ کے ذریعے نیورونز میں روشنی کے حساس پروٹین (Channelrhodopsin) داخل کیے جاتے ہیں جو نیلی روشنی پڑتے ہی کرنٹ چھوڑ کر خلیے کو بیدار کر دیتے ہیں", "روشنی بری یادوں کو جلا دیتی ہے", "لیزر نیورونز کو گرم کر کے متحرک کرتی ہے", "فوٹونز خون کے خلیوں کی جگہ لے لیتے ہیں"][0],
        "یہ دماغ کا ریموٹ کنٹرول ہے۔ الجی کے پودوں سے لیے گئے پروٹین چوہے کے مخصوص دماغی خلیوں میں ڈالے جاتے ہیں۔ جب نیلے رنگ کی لائٹ جلائی جائے تو صرف وہی خلیے فوری جاگ اٹھتے ہیں اور بند کرنے پر سو جاتے ہیں۔"
    ),
    (
        "Why was the discovery that fatal neurological diseases like Mad Cow and Kuru are caused by Prions considered a shocking heresy in molecular biology?",
        ["Prions are infectious pathogen agents consisting entirely of misfolded proteins with zero DNA or RNA nucleic acid genetic material", "Prions are alien bacteria from meteorites", "The disease is caused by microscopic glass needles", "Mad Cow disease is caused by viral fungi"],
        "Prions are infectious pathogen agents consisting entirely of misfolded proteins with zero DNA or RNA nucleic acid genetic material",
        "Stanley Prusiner proved the protein-only hypothesis. Misfolded prion proteins (PrPSc) act as templates that induce normal cellular proteins (PrPC) to refold into the infectious amyloid beta-sheet conformation without any genetic code.",
        "پرایونز اور میڈ کاؤ کی پراسرار بیماری (Prions & Protein Infection): جب سٹینلی پروسینر نے ثابت کیا کہ پرایونز بیماری پھیلاتے ہیں تو دنیا کے تمام بیالوجسٹ حیران کیوں رہ گئے؟",
        ["یہ بیماری پھیلانے والے ایسے انفیکشن ایجنٹ ہیں جن کے پاس کوئی ڈی این اے یا آر این اے موجود نہیں ہوتا بلکہ وہ صرف ٹیڑھے مڑے ہوئے پروٹینز ہوتے ہیں", "وہ شہابیوں سے آنے والے بیکٹیریا ہیں", "یہ شیشے کی سوئیوں سے پھیلتی ہے", "یہ فنگس کا وائرس ہے"],
        ["یہ بیماری پھیلانے والے ایسے انفیکشن ایجنٹ ہیں جن کے پاس کوئی ڈی این اے یا آر این اے موجود نہیں ہوتا بلکہ وہ صرف ٹیڑھے مڑے ہوئے پروٹینز ہوتے ہیں", "وہ شہابیوں سے آنے والے بیکٹیریا ہیں", "یہ شیشے کی سوئیوں سے پھیلتی ہے", "یہ فنگس کا وائرس ہے"][0],
        "حیاتیات کا اٹل قانون تھا کہ بیماری پھیلانے کے لیے جینیاتی مادہ (DNA/RNA) لازمی ہے۔ مگر پرایون محض ایک بگڑا ہوا پروٹین ہے جو تندرست پروٹینز کو چھو کر اپنے جیسا بگڑا ہوا بنا دیتا ہے اور دماغ کو اسفنج کی طرح کھا جاتا ہے۔"
    ),
    (
        "How can microscopic Tardigrades (Water Bears) survive complete desiccation, outer space vacuum, and thousands of times more radiation than humans (Cryptobiosis)?",
        ["They replace bodily water with specialized intrinsically disordered protective glass proteins (TDPs), entering a vitrified suspended animation state", "They grow heavy titanium armor scales", "They split into duplicate spores", "They absorb cosmic radiation as food"],
        "They replace bodily water with specialized intrinsically disordered protective glass proteins (TDPs), entering a vitrified suspended animation state",
        "Tardigrades express tardigrade-disordered proteins (TDPs) and trehalose. Dehydration vitrifies their cellular interior into biological glass, immobilizing macromolecules and halting metabolic activity (tun state) indefinitely.",
        "ٹارڈیگریڈ کی لافانی بقا (Tardigrade Cryptobiosis): یہ خوردبینی جاندار پانی کے مکمل خاتمے، خلا کے ویکیوم اور تابکاری کے بھیانک طوفان میں بھی زندہ کیسے بچ جاتے ہیں؟",
        ["وہ اپنے جسم کے پانی کی جگہ شیشے جیسے خصوصی پروٹینز (TDPs) بنا لیتے ہیں جو ان کے خلیات اور ڈی این اے کو ایک غیر متحرک شیشے کے بت کی طرح محفوظ کر دیتے ہیں", "ان پر ٹائٹینیم کا خول اگ آتا ہے", "وہ دو ٹکڑوں میں بٹ جاتے ہیں", "وہ تابکاری کو خوراک بنا لیتے ہیں"],
        ["وہ اپنے جسم کے پانی کی جگہ شیشے جیسے خصوصی پروٹینز (TDPs) بنا لیتے ہیں جو ان کے خلیات اور ڈی این اے کو ایک غیر متحرک شیشے کے بت کی طرح محفوظ کر دیتے ہیں", "ان پر ٹائٹینیم کا خول اگ آتا ہے", "وہ دو ٹکڑوں میں بٹ جاتے ہیں", "وہ تابکاری کو خوراک بنا لیتے ہیں"][0],
        "جب پانی سوکھتا ہے تو وہ اپنے اندرونی خلیات کو شیشے کی طرح جما دیتے ہیں جہاں وقت رک جاتا ہے اور میٹابولزم صفر ہو جاتا ہے۔ دہائیوں بعد جب پانی کا ایک قطرہ ڈالا جائے تو وہ شیشہ پگھلتا ہے اور وہ دوبارہ چلنے لگتے ہیں۔"
    ),
    (
        "Why do giant tube worms living around deep-sea hydrothermal vents at 2,500 meters depth flourish in total pitch-black darkness without any sunlight?",
        ["Symbiotic chemotrophic bacteria oxidize toxic hydrogen sulfide from volcanic vents to synthesize organic nutrients (Chemosynthesis)", "Tube worms feed on falling dead whales exclusively", "Volcanic vents emit ultraviolet light for photosynthesis", "Worms absorb thermal magma energy through gills"],
        "Symbiotic chemotrophic bacteria oxidize toxic hydrogen sulfide from volcanic vents to synthesize organic nutrients (Chemosynthesis)",
        "Riftia pachyptila lack digestive systems. They host billions of endosymbiont bacteria in a trophosome organ that fix inorganic carbon via sulfide oxidation: H2S + 2O2 -> SO4^2- + 2H+ + energy, sustaining ecosystems independent of solar energy.",
        "گہرے سمندر کے چیری کیڑے اور کیموسنتھیسز (Hydrothermal Vent Chemosynthesis): سمندر کی تہہ میں جہاں سورج کی ایک کرن نہیں پہنچتی، وہاں زہریلی گیسوں کے دہانوں پر جاندار کیسے پھل پھول رہے ہیں؟",
        ["ان کے اندر موجود بیکٹیریا سورج کی روشنی کی بجائے آتش فشاں سے نکلنے والی زہریلی ہائیڈروجن سلفائیڈ کو کیمیائی طور پر جلا کر خوراک بناتے ہیں (Chemosynthesis)", "وہ صرف مردہ وہیل مچھلیاں کھاتے ہیں", "دہانوں سے الٹرا وائلٹ روشنی نکلتی ہے", "وہ میگما کی گرمی گلپھڑوں سے پیتے ہیں"],
        ["ان کے اندر موجود بیکٹیریا سورج کی روشنی کی بجائے آتش فشاں سے نکلنے والی زہریلی ہائیڈروجن سلفائیڈ کو کیمیائی طور پر جلا کر خوراک بناتے ہیں (Chemosynthesis)", "وہ صرف مردہ وہیل مچھلیاں کھاتے ہیں", "دہانوں سے الٹرا وائلٹ روشنی نکلتی ہے", "وہ میگما کی گرمی گلپھڑوں سے پیتے ہیں"][0],
        "پوری دنیا کا ماحولیاتی نظام سورج کی روشنی اور فوٹوسنتھیسز پر چلتا ہے، مگر گہرے سمندر کا یہ جہان اکیلا ایسا ہے جو سورج کے بغیر زمین کے اندرونی کیمیکلز سے توانائی بنا کر اپنی الگ دنیا بسائے ہوئے ہے۔"
    ),
    (
        "Why does a person who has their inner ear semicircular canals damaged experience severe, room-spinning vertigo whenever they tilt their head (BPPV)?",
        ["Dislodged calcium carbonate otoconia crystals migrate into the fluid semicircular canals, deflecting sensory hair cells improperly with gravity", "The eardrum develops microscopic holes", "Auditory nerves lose all electrical voltage", "Ear wax blocks blood flow to the brain"],
        "Dislodged calcium carbonate otoconia crystals migrate into the fluid semicircular canals, deflecting sensory hair cells improperly with gravity",
        "In Benign Paroxysmal Positional Vertigo, detached otoconia particles settle in the posterior semicircular canal. Tilting the head causes gravitational drag on endolymph fluid, cupular deflection, and false nystagmus sensation.",
        "چکر آنا اور کان کے پتھر (BPPV Vertigo): سر کو ہلانے پر پوری دنیا گول گھومتی ہوئی اور جھولتی ہوئی کیوں محسوس ہونے لگتی ہے؟",
        ["اندرونی کان کے باریک کیلشیم کرسٹل اپنی جگہ سے اکھڑ کر توازن کی مائع نالیوں میں گر جاتے ہیں اور کشش ثقل سے حسی بالوں کو غلط سگنل بھیجتے ہیں", "کان کے پردے میں سوراخ ہو جاتا ہے", "سننے کی رگیں وولٹیج کھو دیتی ہیں", "کان کا میل خون روک دیتا ہے"],
        ["اندرونی کان کے باریک کیلشیم کرسٹل اپنی جگہ سے اکھڑ کر توازن کی مائع نالیوں میں گر جاتے ہیں اور کشش ثقل سے حسی بالوں کو غلط سگنل بھیجتے ہیں", "کان کے پردے میں سوراخ ہو جاتا ہے", "سننے کی رگیں وولٹیج کھو دیتی ہیں", "کان کا میل خون روک دیتا ہے"][0],
        "کان کے اندر توازن ناپنے والے باریک ریت جیسے ذرات ہوتے ہیں۔ جب وہ اکھڑ کر مائع کی نالی میں گر جائیں، تو سر ہلانے پر وہ اسفنج کی طرح پانی میں ہلتے ہیں اور دماغ کو جھوٹا سگنل دیتے ہیں کہ انسان تیزی سے گھوم رہا ہے۔"
    ),
    (
        "Why does a passenger on a boat experience debilitating seasickness even when lying completely motionless in a comfortable cabin bed?",
        ["Sensory Conflict Theory: vestibular inner ear balance organs signal continuous rolling motion while eyes see a stationary, static cabin room", "Cabin air contains carbon monoxide", "Ocean waves emit infrasound frequencies", "Sea water evaporates stomach acid"],
        "Sensory Conflict Theory: vestibular inner ear balance organs signal continuous rolling motion while eyes see a stationary, static cabin room",
        "Motion sickness arises when vestibular semicircular canals detect acceleration, but visual cues from fixed cabin walls register zero movement. The brain interprets this multisensory mismatch as neurotoxin hallucination, triggering vomiting.",
        "سمندری بیماری یا متلی (Seasickness & Sensory Mismatch): بحری جہاز کے کیبن میں پرسکون لیٹے ہوئے انسان کو اچانک شدید چکر اور الٹیاں کیوں آنے لگتی ہیں؟",
        ["حسی تضاد: اندرونی کان کے توازن والے اعضاء لہروں کے جھولنے کا سگنل دیتے ہیں جبکہ آنکھیں کمرے کو بالکل ساکن دیکھتی ہیں، جس سے دماغ الجھ جاتا ہے", "کیبن کی ہوا میں زہریلی گیس ہوتی ہے", "سمندر کی لہریں انفرارائونڈ چھوڑتی ہیں", "سمندر کا پانی معدہ خراب کرتا ہے"],
        ["حسی تضاد: اندرونی کان کے توازن والے اعضاء لہروں کے جھولنے کا سگنل دیتے ہیں جبکہ آنکھیں کمرے کو بالکل ساکن دیکھتی ہیں، جس سے دماغ الجھ جاتا ہے", "کیبن کی ہوا میں زہریلی گیس ہوتی ہے", "سمندر کی لہریں انفرارائونڈ چھوڑتی ہیں", "سمندر کا پانی معدہ خراب کرتا ہے"][0],
        "جب کان کہیں کہ ہم ہل رہے ہیں اور آنکھیں کہیں کہ ہم ساکن ہیں، تو ارتقائی طور پر دماغ سمجھتا ہے کہ شاید ہم نے کوئی زہریلی بوٹی یا زہر کھا لیا ہے جو دماغ کو بہکا رہا ہے، اس لیے وہ دفاع کے طور پر قے کروا دیتا ہے۔"
    ),
    (
        "Why can drinking large volumes of pure distilled water after intense athletic exertion be fatal (Water Intoxication / Hyponatremia)?",
        ["Severe dilution of blood plasma sodium ions creates an osmotic gradient that drives water into brain cells, causing lethal cerebral edema", "Distilled water corrodes stomach linings", "Pure water freezes inside blood vessels", "Water neutralizes digestive enzymes permanently"],
        "Severe dilution of blood plasma sodium ions creates an osmotic gradient that drives water into brain cells, causing lethal cerebral edema",
        "Excessive hypotonic hydration drops serum sodium below 135 mEq/L. Osmotic pressure forces extracellular fluid into intracellular compartments, swelling neurons inside the rigid cranium and causing fatal herniation.",
        "پانی کا زہر اور ہائپونیٹریمیا (Water Intoxication / Hyponatremia): شدید گرمی اور محنت کے بعد بہت زیادہ خالص پانی پینا جان لیوا کیوں ثابت ہو سکتا ہے؟",
        ["خون میں نمکیات (سوڈیم) کا تناسب اچانک گر جاتا ہے جس سے آسموسس کے اصول کے تحت پانی دماغ کے خلیات کے اندر بھر کر دماغ کو جان لیوا سوجن میں مبتلا کر دیتا ہے", "خالص پانی معدے کی جھلی کاٹ دیتا ہے", "خالص پانی رگوں میں جم جاتا ہے", "پانی ہاضمے کے اینزائمز کو ختم کرتا ہے"],
        ["خون میں نمکیات (سوڈیم) کا تناسب اچانک گر جاتا ہے جس سے آسموسس کے اصول کے تحت پانی دماغ کے خلیات کے اندر بھر کر دماغ کو جان لیوا سوجن میں مبتلا کر دیتا ہے", "خالص پانی معدے کی جھلی کاٹ دیتا ہے", "خالص پانی رگوں میں جم جاتا ہے", "پانی ہاضمے کے اینزائمز کو ختم کرتا ہے"][0],
        "پسینے میں نمک نکل جاتا ہے۔ اگر صرف سادہ پانی پیا جائے تو خون کا نمک پتلا ہو جاتا ہے۔ توازن برابر کرنے کے لیے پانی دماغ کے خلیوں میں گھس کر انہیں غبارے کی طرح پھلا دیتا ہے جس سے کھوپڑی میں شدید دباؤ بن جاتا ہے۔"
    ),
    (
        "Why does stepping onto a stationary broken escalator give a person a momentary sensation of clumsy loss of balance, despite knowing it is not moving?",
        ["The cerebellum automatically triggers an unconscious anticipatory motor adjustment program based on learned visual cues", "Escalator steps are coated with magnetic grease", "Broken metal alters gravitational fields", "Static electricity numbs ankle reflexes"],
        "The cerebellum automatically triggers an unconscious anticipatory motor adjustment program based on learned visual cues",
        "The 'broken escalator phenomenon' shows motor automation: seeing escalator stairs triggers conditioned feed-forward postural compensation (swaying forward to counter expected acceleration), producing motor dissonance.",
        "بند برقی سیڑھی کا جھٹکا (Broken Escalator Phenomenon): بند پڑی برقی سیڑھی پر چڑھتے وقت انسان کو معلوم ہونے کے باوجود پاؤں لڑکھڑاتا ہوا اور عجیب کیوں محسوس ہوتا ہے؟",
        ["دماغ کا چھوٹا حصہ (Cerebellum) شکل دیکھتے ہی لاشعوری طور پر پٹھوں کو چلتی سیڑھی کے مطابق خودکار جھٹکے کے لیے پہلے سے تیار کر دیتا ہے", "سیڑھی پر مقناطیسی چکنائی لگی ہوتی ہے", "ٹوٹی ہوئی دھات کشش ثقل بدلتی ہے", "جامد بجلی پاؤں کو سن کر دیتی ہے"],
        ["دماغ کا چھوٹا حصہ (Cerebellum) شکل دیکھتے ہی لاشعوری طور پر پٹھوں کو چلتی سیڑھی کے مطابق خودکار جھٹکے کے لیے پہلے سے تیار کر دیتا ہے", "سیڑھی پر مقناطیسی چکنائی لگی ہوتی ہے", "ٹوٹی ہوئی دھات کشش ثقل بدلتی ہے", "جامد بجلی پاؤں کو سن کر دیتی ہے"][0],
        "دماغ عادات کا غلام ہے۔ سیڑھی دیکھتے ہی وہ جسم کو آگے جھکانے کا خودکار سگنل بھیجتا ہے جو وہ ہمیشہ چلتی سیڑھی پر چڑھتے ہوئے کرتا ہے۔ جب سیڑھی نہیں چلتی تو جسم کا یہ غیر ضروری جھکاؤ لڑکھڑاہٹ بن جاتا ہے۔"
    ),
    (
        "Why does smelling a particular childhood fragrance or food aroma instantly evoke vivid, emotionally overwhelming memories (the Proustian Effect)?",
        ["The olfactory bulb has direct, un-routed anatomical connections to the amygdala and hippocampus, bypassing the cognitive thalamus", "Fragrance particles dissolve in brain spinal fluid", "Nose hairs contain genetic memory chips", "Perfume chemicals act as neurotoxins"],
        "The olfactory bulb has direct, un-routed anatomical connections to the amygdala and hippocampus, bypassing the cognitive thalamus",
        "Unlike all other senses (vision, touch, hearing) which route through the thalamic relay center, olfactory signals project directly to the limbic system (amygdala for emotion, hippocampus for memory), evoking instant nostalgia.",
        "خوشبو اور پرانی یادیں (The Proustian Olfactory Effect): بچپن کی کسی خاص خوشبو کا سونگھنا پلک جھپکنے میں برسوں پرانی تفصیلی یادیں اور جذبات کیسے تازہ کر دیتا ہے؟",
        ["سونگھنے کی حس کا اعصابی راستہ دماغ کے مرکزی فلٹر کو بائی پاس کر کے سیدھا جذبات (Amygdala) اور یادداشت کے مرکز (Hippocampus) سے جڑا ہوتا ہے", "خوشبو کے ذرات دماغ کے پانی میں گھلتے ہیں", "ناک کے بالوں میں میموری چپس ہوتی ہیں", "عطر کے کیمیکلز نشہ پیدا کرتے ہیں"],
        ["سونگھنے کی حس کا اعصابی راستہ دماغ کے مرکزی فلٹر کو بائی پاس کر کے سیدھا جذبات (Amygdala) اور یادداشت کے مرکز (Hippocampus) سے جڑا ہوتا ہے", "خوشبو کے ذرات دماغ کے پانی میں گھلتے ہیں", "ناک کے بالوں میں میموری چپس ہوتی ہیں", "عطر کے کیمیکلز نشہ پیدا کرتے ہیں"][0],
        "دیکھنے اور سننے کے سگنل پہلے عقل کے فلٹر میں جاتے ہیں، مگر سونگھنے کا تار سیدھا دل اور پرانی یادوں کے خانے میں لگا ہوتا ہے۔ اسی لیے ایک ہلکی سی خوشبو انسان کو فوراً 20 سال پرانے لمحات میں پہنچا دیتی ہے۔"
    ),
    (
        "Why does a person who holds a cold beverage glass perceive a job candidate as colder, while holding a warm mug makes them perceive the candidate as warm and trustworthy?",
        ["Embodied Cognition: the insular cortex processes both physical temperature sensations and social emotional warmth using overlapping neural circuitry", "Warm drinks increase blood pressure", "Cold drinks chill the vocal cords", "Caffeine induces hypnotic compliance"],
        "Embodied Cognition: the insular cortex processes both physical temperature sensations and social emotional warmth using overlapping neural circuitry",
        "Lawrence Williams and John Bargh showed embodied priming: physical warmth stimulates the insula, priming psychological social warmth and generosity without conscious awareness.",
        "جسمانی حرارت اور سماجی تاثر (Embodied Cognition Warmth Priming): ہاتھ میں گرم چائے کا کپ پکڑے ہوئے انسان کو سامنے والا شخص زیادہ مخلص، پیارا اور ہمدرد کیوں لگتا ہے؟",
        ["دماغ کا انسولا (Insular Cortex) حصہ جسمانی درجہ حرارت اور سماجی و جذباتی اپنائیت دونوں کو ایک ہی مشترکہ اعصابی راستے پر ریکارڈ کرتا ہے", "گرم مشروب بلڈ پریشر بڑھاتا ہے", "ٹھنڈا مشروب آواز دبا دیتا ہے", "کیفین انسان کو بے بس کر دیتی ہے"],
        ["دماغ کا انسولا (Insular Cortex) حصہ جسمانی درجہ حرارت اور سماجی و جذباتی اپنائیت دونوں کو ایک ہی مشترکہ اعصابی راستے پر ریکارڈ کرتا ہے", "گرم مشروب بلڈ پریشر بڑھاتا ہے", "ٹھنڈا مشروب آواز دبا دیتا ہے", "کیفین انسان کو بے بس کر دیتی ہے"][0],
        "ہمارا دماغ تجریدی خیالات کو جسمانی احساسات کے ساتھ ملا کر سوچتا ہے۔ ہاتھ میں گرم کپ ہونے سے دماغ میں پیدا ہونے والی گرمجوشی کا سگنل سامنے والے انسان کی شخصیت کے جائزے پر بھی غیر شعوری طور پر چھا جاتا ہے۔"
    ),
    (
        "Why does an individual who undergoes complete sensory deprivation in a dark, silent, body-temperature salt water tank begin hallucinating vividly within 45 minutes?",
        ["Sensory deprivation forces the cerebral cortex to amplify internal spontaneous neural baseline noise to compensate for lack of external sensory input", "Salt water seeps through ear drums", "Darkness burns optical rods", "The brain runs out of oxygen in tanks"],
        "Sensory deprivation forces the cerebral cortex to amplify internal spontaneous neural baseline noise to compensate for lack of external sensory input",
        "The brain is a predictive engine. When external sensory afferents drop to zero, neural gain is dialed up. Spontaneous baseline cortical fluctuations are interpreted as real sensory percepts, producing hallucinations.",
        "حسی تنہائی اور فریب نظر (Sensory Deprivation Hallucinations): مکمل تاریک، بے آواز اور نیم گرم پانی کے بند ٹینک میں بند انسان کو بغیر کسی دوا کے رنگ برنگے مناظر اور آوازیں کیوں آنے لگتی ہیں؟",
        ["بیرونی سگنلز کے بند ہونے پر دماغ اپنے اندرونی خودکار اعصابی شور کو اتنا زیادہ اونچا کر دیتا ہے کہ انسان کے اپنے ہی خیالات حقیقی دنیا بن کر نظر آنے لگتے ہیں", "نمکین پانی کان کے پردے میں گھستا ہے", "اندھیرا آنکھوں کے پردے جلا دیتا ہے", "ٹینک میں آکسیجن ختم ہو جاتی ہے"],
        ["بیرونی سگنلز کے بند ہونے پر دماغ اپنے اندرونی خودکار اعصابی شور کو اتنا زیادہ اونچا کر دیتا ہے کہ انسان کے اپنے ہی خیالات حقیقی دنیا بن کر نظر آنے لگتے ہیں", "نمکین پانی کان کے پردے میں گھستا ہے", "اندھیرا آنکھوں کے پردے جلا دیتا ہے", "ٹینک میں آکسیجن ختم ہو جاتی ہے"][0],
        "دماغ خاموش نہیں بیٹھ سکتا۔ جب باہر سے آنکھ، کان اور جلد کا تمام ڈیٹا آنا بند ہو جائے تو وہ اپنے سگنلز کا والیوم فل کر دیتا ہے۔ اس سے دماغ کے اپنے اندرونی سپنے اور یادیں باہر کی حقیقت بن کر سامنے ناچنے لگتی ہیں۔"
    ),
    (
        "Why does repeatedly saying an ordinary familiar word (like 'door' or 'fork') out loud 40 times cause the word to suddenly sound like meaningless gibberish (Semantic Satiation)?",
        ["Prolonged repetitive stimulation causes reactive neural inhibition in specific cortical semantic representations, uncoupling sound from meaning", "The tongue muscles experience lactic acid fatigue", "Vocal cords alter their acoustic pitch", "Saliva washes away lexical taste memory"],
        "Prolonged repetitive stimulation causes reactive neural inhibition in specific cortical semantic representations, uncoupling sound from meaning",
        "Leon Jakobovits James proved semantic satiation: continuous repetition produces refractory fatigue in specific cortical neural assemblies, dissociating acoustic phonetic perception from lexical semantic access.",
        "سیمینٹک سیٹی ایشن یا لفظ کا اجنبی بننا (Semantic Satiation): کسی عام سے لفظ کو اگر لگاتار 40 بار تیزی سے دہرایا جائے تو وہ اچانک بے معنی، عجیب اور غیر مانوس کیوں لگنے لگتا ہے؟",
        ["دماغ کے مخصوص اعصابی مراکز مسلسل ایک ہی سگنل ملنے پر تھک کر عارضی طور پر سست ہو جاتے ہیں جس سے لفظ کی آواز کا اس کے مفہوم سے رابطہ کٹ جاتا ہے", "زبان کے پٹھے تھک جاتے ہیں", "آواز کا سُر بدل جاتا ہے", "تھوک یادداشت کے مالیکیولز بہا دیتا ہے"],
        ["دماغ کے مخصوص اعصابی مراکز مسلسل ایک ہی سگنل ملنے پر تھک کر عارضی طور پر سست ہو جاتے ہیں جس سے لفظ کی آواز کا اس کے مفہوم سے رابطہ کٹ جاتا ہے", "زبان کے پٹھے تھک جاتے ہیں", "آواز کا سُر بدل جاتا ہے", "تھوک یادداشت کے مالیکیولز بہا دیتا ہے"][0],
        "جب ایک ہی نیورون کو بار بار جگایا جائے تو وہ حفاظت کے لیے جواب دینا بند کر دیتا ہے۔ اب کانوں کو صرف ایک بے تکی آواز سنائی دے رہی ہوتی ہے جبکہ دماغ کا لغت والا شعبہ اس کا مطلب یاد کرنے سے عارضی طور پر انکاری ہو جاتا ہے۔"
    ),
    (
        "Why can people looking at a noisy television screen or cloud formation easily see clear human faces, but rarely see random mechanical objects like toasters (Pareidolia)?",
        ["Evolutionary survival hardwired the Fusiform Face Area to aggressively favor false positives in detecting faces over false negatives", "Clouds contain facial moisture proteins", "Television pixels are programmed with human faces", "The human retina is shaped like a face"],
        "Evolutionary survival hardwired the Fusiform Face Area to aggressively favor false positives in detecting faces over false negatives",
        "Face perception relies on dedicated neural architecture (FFA). Error management theory dictates that mistaking a cloud for an approaching predator/human has zero evolutionary cost, while missing a real face could be fatal.",
        "پریڈولیا اور چہروں کی پہچان (Pareidolia Face Bias): بادلوں، چاند یا گاڑی کی لائٹوں میں انسان کو ہر جگہ چہرے ہی کیوں بنے نظر آتے ہیں، کوئی اور چیز کیوں نہیں؟",
        ["دماغ کا چہرہ پہچاننے والا شعبہ (FFA) بقا کی خاطر اتنا زیادہ حساس بنایا گیا ہے کہ وہ غیر متعلقہ چیزوں میں بھی فوری چہرہ تلاش کر کے الرٹ کر دیتا ہے", "بادلوں میں انسانی پروٹین ہوتے ہیں", "ٹی وی کے پکسلز میں چہرے چھپے ہوتے ہیں", "آنکھ کا پردہ چہرے کی شکل کا ہوتا ہے"],
        ["دماغ کا چہرہ پہچاننے والا شعبہ (FFA) بقا کی خاطر اتنا زیادہ حساس بنایا گیا ہے کہ وہ غیر متعلقہ چیزوں میں بھی فوری چہرہ تلاش کر کے الرٹ کر دیتا ہے", "بادلوں میں انسانی پروٹین ہوتے ہیں", "ٹی وی کے پکسلز میں چہرے چھپے ہوتے ہیں", "آنکھ کا پردہ چہرے کی شکل کا ہوتا ہے"][0],
        "جنگل میں کسی دشمن یا شیر کا چہرہ نہ پہچاننا جان لیوا تھا، جبکہ پتھر میں جھوٹ موٹ کا چہرہ دیکھ لینے کا کوئی نقصان نہیں تھا۔ اسی لیے ہمارا دماغ ہر بے ترتیب نمونے میں چہرہ تلاش کرنے پر مجبور ہے۔"
    ),
    (
        "Why does reading a list of words like [bed, awake, tired, dream, snore, blanket] cause 80 percent of people to falsely remember the word 'sleep' being on the list (the DRM Illusion)?",
        ["Spreading activation in semantic memory networks automatically primes unmentioned critical lures that share dense associative nodes", "The list contains subliminal audio frequencies", "People confuse dreams with reality", "Short-term memory expires after 3 words"],
        "Spreading activation in semantic memory networks automatically primes unmentioned critical lures that share dense associative nodes",
        "The Deese-Roediger-McDermott paradigm shows that presenting related words activates the central thematic node ('sleep') in semantic associative networks, generating high-confidence false memories.",
        "ڈی آر ایم میموری وہم (The DRM False Memory Illusion): جب بستر، تھکاوٹ، خواب اور خراٹوں کے الفاظ سنوائے جائیں تو لوگ پختہ یقین کے ساتھ یہ جھوٹی گواہی کیوں دیتے ہیں کہ انہوں نے لفظ 'نیند' بھی سنا تھا؟",
        ["دماغ کا یادداشت کا جال آپس میں جڑے ہوئے تمام قریبی الفاظ کے متحرک ہونے پر مرکزی عنوان والے لفظ کو خود بخود یادداشت میں شامل کر لیتا ہے", "لسٹ میں خفیہ صوتی لہریں ہوتی ہیں", "لوگ نیند میں سن رہے ہوتے ہیں", "یادداشت تین الفاظ بعد مٹ جاتی ہے"],
        ["دماغ کا یادداشت کا جال آپس میں جڑے ہوئے تمام قریبی الفاظ کے متحرک ہونے پر مرکزی عنوان والے لفظ کو خود بخود یادداشت میں شامل کر لیتا ہے", "لسٹ میں خفیہ صوتی لہریں ہوتی ہیں", "لوگ نیند میں سن رہے ہوتے ہیں", "یادداشت تین الفاظ بعد مٹ جاتی ہے"][0],
        "دماغ ٹیپ ریکارڈر کی طرح لفظ لفظ ریکارڈ نہیں کرتا بلکہ مفہوم کا خلاصہ بناتا ہے۔ جب تمام الفاظ 'نیند' کے گرد گھوم رہے ہوں تو دماغ بغیر سنے ہی یقین کر لیتا ہے کہ نیند کا لفظ بھی ضرور بولا گیا تھا۔"
    ),
    (
        "Why does an eyewitness's memory of a car accident change drastically when an investigator asks 'How fast were the cars going when they smashed into each other?' vs 'contacted each other' (the Misinformation Effect)?",
        ["Post-event leading language alters and overwrites malleable reconstructive memory traces during the cognitive retrieval process", "Eyewitnesses deliberately perjure themselves for rewards", "The word 'smashed' creates acoustic shock waves in ears", "Car accidents erase anterior temporal lobes"],
        "Post-event leading language alters and overwrites malleable reconstructive memory traces during the cognitive retrieval process",
        "Elizabeth Loftus demonstrated that memory is reconstructive rather than reproductive. Introducing presuppositions ('smashed') retroactively integrates false details (like broken glass) into the subject's recalled memory.",
        "غلط معلومات کا اثر اور گواہی کی یادداشت (Loftus Misinformation Effect): 'گاڑیاں ٹکرائیں' کی بجائے صرف یہ پوچھنے سے کہ 'گاڑیاں جب آپس میں چکنا چور ہوئیں تو رفتار کیا تھی؟' گواہ جھوٹا شیشہ ٹوٹا ہوا کیوں یاد کرنے لگتے ہیں؟",
        ["سوال میں استعمال کیے گئے طاقتور الفاظ پرانی لچکدار یادداشت کو تبدیل کر کے اس میں وہ جھوٹے مناظر بھی فٹ کر دیتے ہیں جو حقیقت میں ہوئے ہی نہیں تھے", "گواہ انعام کے لالچ میں جھوٹ بولتے ہیں", "لفظ سے کان میں جھٹکا لگتا ہے", "حادثہ دماغی یادداشت مٹا دیتا ہے"],
        ["سوال میں استعمال کیے گئے طاقتور الفاظ پرانی لچکدار یادداشت کو تبدیل کر کے اس میں وہ جھوٹے مناظر بھی فٹ کر دیتے ہیں جو حقیقت میں ہوئے ہی نہیں تھے", "گواہ انعام کے لالچ میں جھوٹ بولتے ہیں", "لفظ سے کان میں جھٹکا لگتا ہے", "حادثہ دماغی یادداشت مٹا دیتا ہے"][0],
        "انسانی یادداشت ویڈیو فائل نہیں بلکہ گیلی مٹی کی طرح ہے۔ جب آپ یاد کو باہر نکالتے ہیں تو نیا پوچھا گیا سوال اس مٹی میں نئے ڈیزائن بنا دیتا ہے، اور انسان پورے یقین سے وہ بات یاد کرنے لگتا ہے جو کبھی ہوئی ہی نہیں تھی۔"
    ),
    (
        "Why did hundreds of ordinary European villagers in 1518 dance uncontrollably in the town square for weeks until suffering fatal exhaustion and heart attacks (the Dancing Plague)?",
        ["Mass Psychogenic Illness / Mass Motor Hysteria triggered by extreme famine, poverty, and shared superstitious psychological stress", "Villagers drank fermented dancing potion", "Toxic gas leaked from limestone caves", "A contagious dancing virus spread through water"],
        "Mass Psychogenic Illness / Mass Motor Hysteria triggered by extreme famine, poverty, and shared superstitious psychological stress",
        "Historian John Waller proved the 1518 Strasbourg dancing mania was a mass psychogenic dissociation. Under severe famine and religious terror of St. Vitus's curse, shared cultural beliefs induced trance states spread by behavioral contagion.",
        "ڈانسنگ پلیگ اور اجتماعی وہم (The Dancing Plague of 1518): سینکڑوں عام انسان ہفتوں تک سڑکوں پر بے قابو ہو کر کیوں ناچتے رہے یہاں تک کہ دل کے دورے اور تھکن سے مر گئے؟",
        ["اجتماعی نفسیاتی بیماری (Mass Motor Hysteria): شدید قحط، غربت اور توہم پرستی کے خوف نے لوگوں کے لاشعور میں ایسا سکتہ طاری کر دیا جو ایک دوسرے کو دیکھ کر وبا کی طرح پھیل گیا", "انہوں نے ناچنے والا شربت پیا تھا", "غاروں سے زہریلی گیس نکلی تھی", "پانی سے ناچنے کا وائرس پھیلا تھا"],
        ["اجتماعی نفسیاتی بیماری (Mass Motor Hysteria): شدید قحط، غربت اور توہم پرستی کے خوف نے لوگوں کے لاشعور میں ایسا سکتہ طاری کر دیا جو ایک دوسرے کو دیکھ کر وبا کی طرح پھیل گیا", "انہوں نے ناچنے والا شربت پیا تھا", "غاروں سے زہریلی گیس نکلی تھی", "پانی سے ناچنے کا وائرس پھیلا تھا"][0],
        "یہ کوئی جادو یا جسمانی وائرس نہیں تھا۔ انتہائی فاقہ کشی اور ذہنی دباؤ کے ماحول میں ایک عورت نے ناچنا شروع کیا۔ دوسرے لوگوں کے تناؤ زدہ ذہنوں نے اس جنون کو ایک مذہبی عذاب سمجھ کر لاشعوری طور پر اپنا لیا اور پورا شہر اس میں مبتلا ہو گیا۔"
    ),
    (
        "Why do individuals in complete solitary confinement for months develop severe paranoia, auditory hallucinations, and profound spatial disorientation?",
        ["The human brain requires continuous sensory and social feedback to calibrate its internal reality-testing and emotional baseline models", "Solitary confinement cells are painted with toxic chemicals", "Loneliness drains electrical cerebrospinal fluid", "Lack of conversation causes tongue atrophy"],
        "The human brain requires continuous sensory and social feedback to calibrate its internal reality-testing and emotional baseline models",
        "Neurological isolation deprives cortical networks of the sensory-rich reference frames required for neural predictive processing. Without ongoing external calibration, error-checking loops fail, causing paranoid psychosis.",
        "تنہائی کا عذاب اور پاگل پن (The Neurobiology of Solitary Confinement): مکمل تنہائی کے قید خانے میں مہینوں بند رہنے والا انسان خود بخود خوف، واہموں اور آوازوں کے پاگل پن میں کیوں مبتلا ہو جاتا ہے؟",
        ["انسانی دماغ کو حقیقت کا توازن اور اپنے باطنی خیالات کو پرکھنے کے لیے دوسرے انسانوں اور بیرونی ماحول کے مسلسل فیڈ بیک کی لازمی ضرورت ہوتی ہے", "کمروں پر زہریلا رنگ کیا ہوتا ہے", "تنہائی دماغ کا پانی خشک کر دیتی ہے", "بات نہ کرنے سے زبان سکڑ جاتی ہے"],
        ["انسانی دماغ کو حقیقت کا توازن اور اپنے باطنی خیالات کو پرکھنے کے لیے دوسرے انسانوں اور بیرونی ماحول کے مسلسل فیڈ بیک کی لازمی ضرورت ہوتی ہے", "کمروں پر زہریلا رنگ کیا ہوتا ہے", "تنہائی دماغ کا پانی خشک کر دیتی ہے", "بات نہ کرنے سے زبان سکڑ جاتی ہے"][0],
        "انسان کا دماغ تنہائی میں رہنے کے لیے نہیں بنا۔ جب اسے دنیا کا کوئی منظر، آواز یا گفتگو نہ ملے تو وہ اپنے ہی وسوسوں کو حقیقی دنیا ماننے لگتا ہے، جس سے حقیقت اور واہمے کی حدیں مکمل طور پر مٹ جاتی ہیں۔"
    ),
]
