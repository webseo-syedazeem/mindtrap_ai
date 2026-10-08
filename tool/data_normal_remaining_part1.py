# -*- coding: utf-8 -*-
"""
Normal tier remaining items (Part 1: 52 distinct items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
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
        "Why does a concrete arch bridge get stronger as more weight is placed directly on top of its center keystone?",
        ["The downward weight forces the arch stones into tighter compression", "Concrete expands under pressure", "The foundations move closer together", "Friction turns into adhesive glue"],
        "The downward weight forces the arch stones into tighter compression",
        "Arches channel vertical loads into compressive lateral forces, pressing stone blocks tightly together.",
        "محرابی پل کے درمیانی پتھر (Keystone) پر جب زیادہ وزن پڑتا ہے تو وہ زیادہ مضبوط کیوں ہو جاتا ہے؟",
        ["اوپر کا وزن محراب کے پتھروں کو مزید دبا کر جوڑ دیتا ہے", "دباؤ سے کنکریٹ پھیلتا ہے", "پل کی بنیادیں قریب آ جاتی ہیں", "رگڑ گوند کا کام کرتی ہے"],
        "اوپر کا وزن محراب کے پتھروں کو مزید دبا کر جوڑ دیتا ہے",
        "محراب عمودی وزن کو بغلی دباؤ میں بدل دیتی ہے جس سے تمام پتھر آپس میں مزید سختی سے جڑ جاتے ہیں۔"
    ),
    (
        "In economics, why does Gresham's Law state that 'bad money drives out good money'?",
        ["People spend artificially overvalued currency and hoard intrinsically valuable money", "Counterfeit currency destroys banks", "Paper money degrades faster than silver", "Low denomination coins are lost easily"],
        "People spend artificially overvalued currency and hoard intrinsically valuable money",
        "When two currencies have equal legal tender status, people hoard coins with actual precious metal content.",
        "معاشیات میں گریشم کا قانون (Gresham's Law) کیوں کہتا ہے کہ 'برا پیسہ اچھے پیسے کو مارکیٹ سے نکال دیتا ہے'؟",
        ["لوگ کم قیمت کی کرنسی خرچ کرتے ہیں اور خالص قیمتی سکے چھپا لیتے ہیں", "جعلی کرنسی بینکوں کو تباہ کر دیتی ہے", "کاغذی نوٹ چاندی سے جلد گل جاتے ہیں", "چھوٹے سکے آسانی سے گم ہو جاتے ہیں"],
        "لوگ کم قیمت کی کرنسی خرچ کرتے ہیں اور خالص قیمتی سکے چھپا لیتے ہیں",
        "جب دو قسم کے پیسے کی قانونی قیمت ایک ہو تو لوگ اصلی سونے یا چاندی کے سکے جمع کر لیتے ہیں اور ہلکے سکے مارکیٹ میں چلاتے ہیں۔"
    ),
    (
        "In game theory, what is the core dilemma in the classic Prisoner's Dilemma?",
        ["Rational self-interest leads both players to defect, producing a worse outcome than mutual cooperation", "Neither player knows the law", "One player is always innocent", "The prosecutor flips a coin"],
        "Rational self-interest leads both players to defect, producing a worse outcome than mutual cooperation",
        "Individually dominant strategies cause both participants to betray each other, even though cooperation yields higher total reward.",
        "گیم تھیوری میں 'قیدیوں کے مخمصے' (Prisoner's Dilemma) کی اصل منطقی الجھن کیا ہے؟",
        ["دونوں کا ذاتی مفاد انہیں اعتراف پر اکساتا ہے جس سے مشترکہ انجام بدترین ہو جاتا ہے", "کوئی بھی قانون سے واقف نہیں ہوتا", "ایک قیدی ہمیشہ بے قصور ہوتا ہے", "جج سکے سے فیصلہ کرتا ہے"],
        "دونوں کا ذاتی مفاد انہیں اعتراف پر اکساتا ہے جس سے مشترکہ انجام بدترین ہو جاتا ہے",
        "اگرچہ دونوں کا خاموش رہنا بہترین نتیجہ دیتا، مگر انفرادی خوف اور لالچ دونوں کو دغا بازی پر مجبور کر دیتا ہے۔"
    ),
    (
        "Why do commercial airplanes fly in curved paths on a flat paper map rather than a straight line?",
        ["A great circle route is the shortest distance on a spherical globe", "To avoid military radar zones", "Wind currents only blow in circles", "Magnetic compasses curve during flight"],
        "A great circle route is the shortest distance on a spherical globe",
        "On a sphere, the shortest path between two distant points is an arc of a great circle, which projects as a curve on flat maps.",
        "ہوائی جہاز فلیٹ نقشے پر سیدھی لکیر کی بجائے گول کمان (Curve) بنا کر کیوں پرواز کرتے ہیں؟",
        ["کروی زمین پر گریٹ سرکل (Great Circle) کا راستہ دراصل سب سے چھوٹا فاصلہ ہوتا ہے", "فوجی ریڈار سے بچنے کے لیے", "ہوائیں ہمیشہ دائرے میں چلتی ہیں", "قطب نما پرواز کے دوران مڑ جاتا ہے"],
        "کروی زمین پر گریٹ سرکل (Great Circle) کا راستہ دراصل سب سے چھوٹا فاصلہ ہوتا ہے",
        "گول زمین پر دو دور دراز مقامات کے درمیان کم ترین فاصلہ سیدھی لکیر نہیں بلکہ دائرے کی کمان ہوتی ہے۔"
    ),
    (
        "Why is the sky dark in space even when the Sun is blazing brightly right next to the spacecraft?",
        ["There are no atmospheric air molecules to scatter sunlight into empty space", "The spacecraft absorbs all light", "Space is cold so light cannot shine", "The Sun's light only travels toward planets"],
        "There are no atmospheric air molecules to scatter sunlight into empty space",
        "Rayleigh scattering by atmospheric gases lights up our daylight sky; in vacuum, unscattered light leaves the background black.",
        "خلا میں سورج کی تیز روشنی کے باوجود پس منظر بالکل سیاہ کیوں دکھائی دیتا ہے؟",
        ["کیونکہ خلا میں ہوا کے مالیکیولز نہیں ہیں جو روشنی کو بکھیر سکیں", "خلائی جہاز ساری روشنی جذب کر لیتا ہے", "خلا ٹھنڈی ہے اس لیے روشنی نہیں چمکتی", "سورج کی روشنی صرف سیاروں کی طرف جاتی ہے"],
        "کیونکہ خلا میں ہوا کے مالیکیولز نہیں ہیں جو روشنی کو بکھیر سکیں",
        "زمین پر ہوا کے ذرات نیلی روشنی کو چاروں طرف بکھیرتے ہیں، جبکہ خلا کے خلاء میں روشنی بکھرتی نہیں اس لیے آسمان کالا رہتا ہے۔"
    ),
    (
        "Why does a person feel heavier at the bottom dip of a roller coaster loop?",
        ["Inertia pushes downward, adding centripetal acceleration to gravitational pull", "Earth's gravity increases closer to the ground", "The track magnetizes the passenger cart", "Air pressure compresses the chest"],
        "Inertia pushes downward, adding centripetal acceleration to gravitational pull",
        "Upward normal force must counter both gravity and provide centripetal acceleration, causing high G-forces against the seat.",
        "رولر کوسٹر کے سب سے نچلے موڑ پر پہنچ کر سوار کو اپنا جسم غیر معمولی وزنی کیوں محسوس ہوتا ہے؟",
        ["انرشیا نیچے دھکیلتا ہے جس سے مرکز مائل ایکسلریشن اور کشش ثقل مل جاتے ہیں", "زمین کے قریب کشش ثقل بڑھ جاتی ہے", "پٹڑی رولر کوسٹر کو مقناطیس کی طرح کھینچتی ہے", "ہوا کا دباؤ سینے کو دباتا ہے"],
        "انرشیا نیچے دھکیلتا ہے جس سے مرکز مائل ایکسلریشن اور کشش ثقل مل جاتے ہیں",
        "سیٹ کو اوپر کی طرف دباؤ ڈال کر جسم کو موڑنا پڑتا ہے، جس سے انسانی جسم پر عام وزن سے دوگنا دباؤ پڑتا ہے۔"
    ),
    (
        "Why does a chef recommend salting water when boiling dry pasta?",
        ["To season the pasta evenly from within as the starch absorbs water", "To make water boil at twice the speed", "To kill bacteria in tap water", "To prevent the metal pot from rusting"],
        "To season the pasta evenly from within as the starch absorbs water",
        "Salt minimally alters boiling point, but dissolves into the wheat matrix as starch granules swell, enhancing internal flavor.",
        "باورچی پاستا ابالتے وقت پانی میں نمک ڈالنے کی تاکید کیوں کرتے ہیں؟",
        ["تاکہ پاستا اندر تک یکساں طور پر ذائقہ دار ہو سکے جب وہ پانی جذب کرے", "تاکہ پانی دگنی رفتار سے ابلنے لگے", "پانی کے جراثیم مارنے کے لیے", "برتن کو زنگ سے بچانے کے لیے"],
        "تاکہ پاستا اندر تک یکساں طور پر ذائقہ دار ہو سکے جب وہ پانی جذب کرے",
        "نمک ابلنے کے درجہ حرارت میں معمولی فرق لاتا ہے، اصل مقصد پاستا کے اندر نمک کا یکساں جذب ہونا ہے۔"
    ),
    (
        "Why do automobile side mirrors display the warning: 'Objects in mirror are closer than they appear'?",
        ["Convex curved glass widens the field of view while shrinking virtual image size", "Concave mirrors reverse left and right", "Flat glass distorts perspective", "The glass is tinted for UV protection"],
        "Convex curved glass widens the field of view while shrinking virtual image size",
        "Convex mirrors diverge reflected rays, showing a broader rear panorama but making distant cars look smaller and farther away.",
        "گاڑی کے دائیں آئینے پر یہ کیوں لکھا ہوتا ہے کہ 'چیزیں جتنی دور دکھائی دیتی ہیں اس سے زیادہ قریب ہیں'؟",
        ["محدب (Convex) آئینہ وسیع منظر دکھاتا ہے جس سے چیزیں چھوٹی اور دور لگتی ہیں", "مقعر آئینہ دائیں بائیں کو الٹ دیتا ہے", "ہموار شیشہ فاصلہ بگاڑ دیتا ہے", "شیشے پر دھوپ سے بچاؤ کی تہہ ہوتی ہے"],
        "محدب (Convex) آئینہ وسیع منظر دکھاتا ہے جس سے چیزیں چھوٹی اور دور لگتی ہیں",
        "محدب آئینہ ڈرائیور کو اندھے موڑ دیکھنے کے لیے چوڑا زاویہ دیتا ہے، مگر اس سے عکس کا سائز چھوٹا ہو جاتا ہے۔"
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
        "Why does an ordinary metal key get warm after being vigorously jiggled inside a stuck mechanical lock?",
        ["Mechanical friction between the key ridges and internal lock pins converts kinetic energy to heat", "Electromagnetic currents in brass", "Static charge build-up", "Chemical oxidation of the lock"],
        "Mechanical friction between the key ridges and internal lock pins converts kinetic energy to heat",
        "Rubbing brass surfaces against steel spring-loaded pins generates frictional heating along microscopic contact points.",
        "پھنسے ہوئے تالے میں چابی کو تیزی سے آگے پیچھے ہلانے سے چابی گرم کیوں ہو جاتی ہے؟",
        ["چابی اور تالے کے اندرونی پنوں کے درمیان رگڑ حرکی توانائی کو حرارت میں بدل دیتی ہے", "پیتل میں برقی رو پیدا ہوتی ہے", "ساکن برقی چارج بنتا ہے", "تالے میں کیمیائی ردعمل ہوتا ہے"],
        "چابی اور تالے کے اندرونی پنوں کے درمیان رگڑ حرکی توانائی کو حرارت میں بدل دیتی ہے",
        "دھاتی سطحوں کی باہمی رگڑ سے حرارت جنم لیتی ہے جس سے چابی کا سرا گرم ہو جاتا ہے۔"
    ),
    (
        "Why does an old grandfather clock with a metal pendulum swing slightly slower in the peak of summer than in winter?",
        ["Thermal expansion lengthens the pendulum rod, increasing its period of oscillation", "Summer air humidity is heavier", "Gravity weakens during summer months", "The gear lubricant evaporates completely"],
        "Thermal expansion lengthens the pendulum rod, increasing its period of oscillation",
        "Period T = 2*pi*sqrt(L/g). Warmer temperatures lengthen rod L, increasing swing duration and slowing the clock down.",
        "پرانی گھڑی کا دھاتی پینڈولم سردیوں کے مقابلے میں سخت گرمیوں میں سست کیوں جھولتا ہے؟",
        ["گرمی کی شدت سے دھاتی راڈ پھیل کر لمبی ہو جاتی ہے جس سے جھولنے کا وقت بڑھ جاتا ہے", "گرمیوں میں ہوا کی نمی بھاری ہوتی ہے", "گرمیوں میں کشش ثقل کمزور ہو جاتی ہے", "گیئرز کا تیل اڑ جاتا ہے"],
        "گرمی کی شدت سے دھاتی راڈ پھیل کر لمبی ہو جاتی ہے جس سے جھولنے کا وقت بڑھ جاتا ہے",
        "پینڈولم جتنا لمبا ہوگا اس کے ایک چکر کا دورانیہ اتنا ہی طویل ہوگا، جس سے گھڑی روزانہ کچھ سیکنڈ پیچھے رہ جاتی ہے۔"
    ),
    (
        "Why do water pipes freeze and burst primarily when the ambient temperature drops significantly below 0 degrees Celsius?",
        ["Water uniquely expands by about 9 percent upon crystallizing into hexagonal ice", "Ice contracts and pulls pipes inward", "Freezing water creates explosive hydrogen gas", "Copper metal shrinks and shatters on its own"],
        "Water uniquely expands by about 9 percent upon crystallizing into hexagonal ice",
        "Hydrogen bonds form an open crystalline lattice in solid ice, increasing volume and generating immense hydraulic pressure in sealed pipes.",
        "شدید سردی میں پانی کے پائپ برف جمنے سے پھٹ کیوں جاتے ہیں؟",
        ["پانی جم کر برف بنتے وقت تقریباً 9 فیصد پھیلتا ہے جس سے پائپ پر اندرونی دباؤ بڑھ جاتا ہے", "برف سکڑ کر پائپ کو اندر کھینچتی ہے", "برف جمنے سے ہائیڈروجن گیس خارج ہوتی ہے", "تانبا خود بخود ٹوٹ جاتا ہے"],
        "پانی جم کر برف بنتے وقت تقریباً 9 فیصد پھیلتا ہے جس سے پائپ پر اندرونی دباؤ بڑھ جاتا ہے",
        "زیادہ تر مائع جم کر سکڑتے ہیں مگر پانی منفرد ہے کہ برف بنتے ہی حجم بڑھاتا ہے، جو بند پائپ کو پھاڑ دیتا ہے۔"
    ),
    (
        "Why does lightning appear instantaneously across the horizon while thunder takes several seconds to arrive?",
        ["Light travels at roughly 300,000 km/s while sound in air travels at only 343 m/s", "Thunder is created several miles higher in the sky", "Sound waves bounce off clouds first", "Human ears react slower than human eyes"],
        "Light travels at roughly 300,000 km/s while sound in air travels at only 343 m/s",
        "The million-fold velocity disparity between electromagnetic radiation and atmospheric acoustic pressure waves creates the noticeable delay.",
        "بجلی کی چمک فوراً نظر آ جاتی ہے جبکہ بادل کی گرج کئی سیکنڈ بعد کیوں سنائی دیتی ہے؟",
        ["روشنی کی رفتار 3 لاکھ کلومیٹر فی سیکنڈ ہے جبکہ ہوا میں آواز کی رفتار محض 343 میٹر فی سیکنڈ ہے", "گرج آسمان میں بہت زیادہ بلندی پر بنتی ہے", "آواز بادلوں سے ٹکرا کر مڑتی ہے", "انسانی کان آنکھوں سے سست کام کرتے ہیں"],
        "روشنی کی رفتار 3 لاکھ کلومیٹر فی سیکنڈ ہے جبکہ ہوا میں آواز کی رفتار محض 343 میٹر فی سیکنڈ ہے",
        "روشنی تقریباً پلک جھپکتے ہی پہنچ جاتی ہے، جبکہ آواز کو ہر ایک کلومیٹر کا فاصلہ طے کرنے میں تقریباً تین سیکنڈ لگتے ہیں۔"
    ),
    (
        "Why does an ocean cargo ship float lower in freshwater river docks than in open saltwater seas?",
        ["Freshwater has lower density, requiring the hull to displace a greater volume to equal ship mass", "River currents pull hulls downward", "Saltwater creates magnetic levitation", "Rivers have shallower seabeds"],
        "Freshwater has lower density, requiring the hull to displace a greater volume to equal ship mass",
        "Archimedes' principle states buoyant force equals weight of displaced fluid. Lower density fluid requires greater displaced volume.",
        "ایک بڑا بحری جہاز نمکین سمندر کے مقابلے میں میٹھے دریا میں زیادہ گہرا کیوں ڈوبتا ہے؟",
        ["میٹھے پانی کی کثافت (Density) کم ہوتی ہے، اس لیے جہاز کو تیرنے کے لیے زیادہ حجم گھیرنا پڑتا ہے", "دریا کی لہریں نیچے کھینچتی ہیں", "نمکین پانی میں مقناطیسی کشش ہوتی ہے", "دریا کی تہہ پتھریلی ہوتی ہے"],
        "میٹھے پانی کی کثافت (Density) کم ہوتی ہے، اس لیے جہاز کو تیرنے کے لیے زیادہ حجم گھیرنا پڑتا ہے",
        "نمکین پانی بھاری ہوتا ہے جو زیادہ اچھال کی قوت دیتا ہے، جبکہ دریا کا ہلکا پانی جہاز کو نیچے بیٹھنے دیتا ہے۔"
    ),
    (
        "Why does wet sand feel firm under your feet, while dry loose sand gives way and sinks beneath your weight?",
        ["Surface tension of thin water films creates capillary bridging between sand grains", "Water dissolves sand into solid rock", "Wet sand is colder and frozen solid", "Tidal friction glues quartz particles"],
        "Surface tension of thin water films creates capillary bridging between sand grains",
        "Capillary forces pull adjacent grains together, providing shear strength that supports foot pressure until saturated.",
        "گیلی ریت پر چلنا آسان اور مضبوط کیوں لگتا ہے جبکہ خشک ریت میں پاؤں اندر دھنس جاتے ہیں؟",
        ["پانی کے قطروں کا سطحی تناؤ ریت کے باریک ذرات کو آپس میں جوڑ کر مضبوط باندھ دیتا ہے", "پانی ریت کو پگھلا کر پتھر بنا دیتا ہے", "گیلی ریت ٹھنڈی ہو کر جم جاتی ہے", "سمندر کی لہریں گوند پیدا کرتی ہیں"],
        "پانی کے قطروں کا سطحی تناؤ ریت کے باریک ذرات کو آپس میں جوڑ کر مضبوط باندھ دیتا ہے",
        "پانی کی باریک تہیں ریت کے ذرات کے درمیان کیپلری فورس پیدا کرتی ہیں جو وزن سنبھالنے کی صلاحیت دیتی ہیں۔"
    ),
    (
        "Why does a person leaning forward on their toes to look over a cliff naturally feel their calf muscles tighten?",
        ["Calf muscles contract to create plantarflexion torque and counter the forward tipping center of mass", "Blood rushes to the legs due to fear", "Knee cartilage locks in place", "To absorb wind gusts against the chest"],
        "Calf muscles contract to create plantarflexion torque and counter the forward tipping center of mass",
        "When center of mass shifts anterior to the ankle pivot point, gastrocnemius muscles exert backward corrective tension.",
        "جب انسان چٹان کے کنارے آگے جھک کر نیچے دیکھتا ہے تو پنڈلی کے پٹھے خود بخود کیوں کھنچ جاتے ہیں؟",
        ["پنڈلی کے پٹھے جسم کے توازن کے مرکز کو آگے گرنے سے روکنے کے لیے کھنچاؤ پیدا کرتے ہیں", "خوف سے خون ٹانگوں میں جمع ہو جاتا ہے", "گھٹنے کی ہڈی جم جاتی ہے", "ہوا کے جھونکے کو سنبھالنے کے لیے"],
        "پنڈلی کے پٹھے جسم کے توازن کے مرکز کو آگے گرنے سے روکنے کے لیے کھنچاؤ پیدا کرتے ہیں",
        "جسم کا کشش ثقل کا مرکز جیسے ہی ٹخنوں سے آگے بڑھتا ہے، پنڈلی کے پٹھے پیچھے کھینچ کر گرنے سے بچاتے ہیں۔"
    ),
    (
        "Why is an ordinary steel needle able to float horizontally on the surface of calm water if placed with extreme gentleness?",
        ["Water surface tension forms an elastic skin-like interface that supports the needle's weight", "Needles contain microscopic trapped air pockets", "Surface oil creates magnetic repulsion", "Calm water has zero gravitational pull"],
        "Water surface tension forms an elastic skin-like interface that supports the needle's weight",
        "Cohesive hydrogen bonds at the liquid-gas boundary create surface tension that resists indentation if not punctured.",
        "ایک لوہے کی باریک سوئی احتیاط سے رکھنے پر پرسکون پانی کی سطح پر کیسے تیر سکتی ہے؟",
        ["پانی کا سطحی تناؤ ایک لچکدار جھلی کی طرح کام کر کے سوئی کا وزن سنبھال لیتا ہے", "سوئی کے اندر ہوا کے باریک سوراخ ہوتے ہیں", "تیل کی وجہ سے مقناطیسی اچھال پیدا ہوتا ہے", "پرسکون پانی میں کشش ثقل صفر ہو جاتی ہے"],
        "پانی کا سطحی تناؤ ایک لچکدار جھلی کی طرح کام کر کے سوئی کا وزن سنبھال لیتا ہے",
        "پانی کے مالیکیولز کی باہمی کشش سطح پر ایک باریک جھلی بناتی ہے جو سوئی کو نیچے ڈوبنے سے روکے رکھتی ہے۔"
    ),
    (
        "Why do racing bicycles use very high tire air pressures (80-120 psi) compared to automobile tires (32-35 psi)?",
        ["High pressure minimizes tire casing deformation, drastically reducing rolling resistance on smooth tarmac", "To make tires explode proof", "Bicycles are heavier per square inch of rubber", "Air expands more in bicycle tubes"],
        "High pressure minimizes tire casing deformation, drastically reducing rolling resistance on smooth tarmac",
        "Stiff tires deform less upon road contact, reducing energy lost to internal tire rubber hysteresis and friction.",
        "ریسنگ سائیکل کے ٹائروں میں گاڑی کے ٹائروں (32 psi) کے مقابلے میں بہت زیادہ ہوا کا دباؤ (100 psi) کیوں رکھا جاتا ہے؟",
        ["زیادہ دباؤ ٹائر کے دبنے کو روکتا ہے جس سے سڑک پر رولنگ رگڑ (Rolling resistance) کم ہو جاتی ہے", "ٹائر پھٹنے سے بچانے کے لیے", "سائیکل فی مربع انچ گاڑی سے بھاری ہوتی ہے", "سائیکل کی ٹیوب میں ہوا زیادہ پھیلتی ہے"],
        "زیادہ دباؤ ٹائر کے دبنے کو روکتا ہے جس سے سڑک پر رولنگ رگڑ (Rolling resistance) کم ہو جاتی ہے",
        "سخت ٹائر سڑک پر دب کر توانائی ضائع نہیں کرتا، جس سے سائیکل سوار کم محنت میں تیز رفتار حاصل کرتا ہے۔"
    ),
    (
        "Why does a campfire smoke seem to continuously drift directly into the eyes of whichever person sits closest to the fire?",
        ["The person's body blocks ambient breeze, creating a low-pressure eddy zone that draws hot smoke toward them", "Smoke is chemically attracted to human carbon dioxide", "Eyes emit heat that pulls particles", "The fire tilts toward human movement"],
        "The person's body blocks ambient breeze, creating a low-pressure eddy zone that draws hot smoke toward them",
        "An obstacle creates a downwind aerodynamic wake with localized low pressure, naturally drawing convection currents and smoke.",
        "آگ کے قریب بیٹھے شخص کو ایسا کیوں لگتا ہے کہ دھواں بار بار اسی کے چہرے کی طرف آ رہا ہے؟",
        ["اس کے جسم کی اوٹ سے ہوا رک جاتی ہے اور نچلے دباؤ کا خلا بنتا ہے جو دھوئیں کو کھینچتا ہے", "دھواں انسان کی سانس کی طرف کھنچتا ہے", "آنکھیں حرارت خارج کر کے دھوئیں کو بلاتی ہیں", "آگ انسانی حرکت کی طرف جھکتی ہے"],
        "اس کے جسم کی اوٹ سے ہوا رک جاتی ہے اور نچلے دباؤ کا خلا بنتا ہے جو دھوئیں کو کھینچتا ہے",
        "انسان کی پیٹھ کے پیچھے سے آنے والی ہوا رک کر سامنے کم دباؤ کا گرداب بناتی ہے جو دھوئیں کو اپنی سمت کھینچ لیتا ہے۔"
    ),
    (
        "Why do honeycombs built by honeybees naturally consist of perfect hexagonal cells rather than circular or square cells?",
        ["Hexagons tile a flat plane with zero gaps while using the absolute minimum perimeter of wax to enclose volume", "Bees have hexagonal compound eyes", "Round cells collapse under gravity", "Squares cannot hold liquid honey"],
        "Hexagons tile a flat plane with zero gaps while using the absolute minimum perimeter of wax to enclose volume",
        "The honeycomb conjecture proves hexagonal geometry provides the most boundary-efficient tessellation possible.",
        "شہد کی مکھیاں اپنے چھتے کے خانے گول یا چوکور کی بجائے چھ کونوں والے (Hexagonal) کیوں بناتی ہیں؟",
        ["مسدس (چھ کونوں والی شکل) بغیر کسی خالی جگہ کے جڑتی ہے اور موم کا کم سے کم خرچ کرتی ہے", "مکھیوں کی آنکھیں مسدس ہوتی ہیں", "گول خانے گر جاتے ہیں", "چوکور خانوں میں شہد نہیں ٹھہرتا"],
        "مسدس (چھ کونوں والی شکل) بغیر کسی خالی جگہ کے جڑتی ہے اور موم کا کم سے کم خرچ کرتی ہے",
        "ہندسہ بتاتا ہے کہ چھ کونوں والی شکل کم ترین موم خرچ کر کے زیادہ سے زیادہ شہد ذخیرہ کرنے کا بہترین ڈیزائن ہے۔"
    ),
    (
        "Why does tapping a glass soda bottle on its side with a spoon produce a higher musical pitch as you drink the liquid?",
        ["Less liquid mass means less inertia for the vibrating liquid-glass column, raising natural resonant frequency", "The glass gets physically thinner", "Air makes sounds lower in pitch", "Sugar dampens high acoustic harmonics"],
        "Less liquid mass means less inertia for the vibrating liquid-glass column, raising natural resonant frequency",
        "When struck, the coupled water-glass system vibrates; reducing water mass decreases effective vibrating mass, increasing frequency.",
        "کانچ کی بوتل کو چمچ سے بجانے پر جوں جوں پانی کم ہوتا ہے، آواز کی پچ (Pitch) اونچی اور باریک کیوں ہوتی جاتی ہے؟",
        ["پانی کا وزن کم ہونے سے بوتل کے ارتعاش کی فریکوئنسی بڑھ جاتی ہے", "شیشہ پتلا ہو جاتا ہے", "ہوا آواز کو گہرا بناتی ہے", "بوتل اندر سے گرم ہو جاتی ہے"],
        "پانی کا وزن کم ہونے سے بوتل کے ارتعاش کی فریکوئنسی بڑھ جاتی ہے",
        "جب بوتل کو چوٹ لگائی جاتی ہے تو پانی کی کم کمیت آسانی سے تیزی سے تھرتھراتی ہے جس سے تیز سر نکلتا ہے۔"
    ),
    (
        "Why does a heavy spinning top remain upright on its pointed tip without toppling over sideways?",
        ["Angular momentum creates gyroscopic stability that resists torques attempting to alter its axis of rotation", "Centrifugal force pushes it into the table", "Air cushions the perimeter", "The sharp tip pierces the surface"],
        "Angular momentum creates gyroscopic stability that resists torques attempting to alter its axis of rotation",
        "Conservation of angular momentum dictates that applying external gravitational torque causes gyroscopic precession rather than falling.",
        "گھومتا ہوا لٹو اپنی باریک نوک پر گرے بغیر سیدھا کھڑا کیسے رہتا ہے؟",
        ["زاویائی مومینٹم (Angular momentum) لٹو کو اس کے گھومنے کے محور پر گرنے سے روکتا ہے", "مرکز گریز قوت اسے میز پر چپکاتی ہے", "ہوا لٹو کو چاروں طرف سے سنبھالتی ہے", "نوک سطح کے اندر دھنس جاتی ہے"],
        "زاویائی مومینٹم (Angular momentum) لٹو کو اس کے گھومنے کے محور پر گرنے سے روکتا ہے",
        "تیز گھومنے سے پیدا ہونے والی گائروسکوپک قوت کشش ثقل کے موڑنے والے دباؤ کو سائیڈ میں پری سیشن میں بدل دیتی ہے۔"
    ),
    (
        "Why do commercial airplanes have small upturned vertical fins (winglets) at the outer tips of their wings?",
        ["To disrupt high-pressure wingtip vortices, reducing induced drag and conserving jet fuel", "To improve radio antenna reception", "For visual identification by air traffic controllers", "To prevent birds from landing during flight"],
        "To disrupt high-pressure wingtip vortices, reducing induced drag and conserving jet fuel",
        "Winglets block high-pressure air under the wing from curling around the tip to the low-pressure upper wing, diminishing turbulent drag.",
        "مسافر طیاروں کے پروں کے بیرونی سروں پر اوپر اٹھے ہوئے چھوٹے پر (Winglets) کیوں لگائے جاتے ہیں؟",
        ["پروں کے کناروں پر بننے والے ہوا کے گرداب کو روک کر ایندھن کی بچت کرنے کے لیے", "ریڈیو سگنل تیز کرنے کے لیے", "کنٹرول ٹاور کی شناخت کے لیے", "پرندوں کو بیٹھنے سے روکنے کے لیے"],
        "پروں کے کناروں پر بننے والے ہوا کے گرداب کو روک کر ایندھن کی بچت کرنے کے لیے",
        "پر کے نیچے کی تیز ہوا اوپر کی طرف چکر کاٹتی ہے، ونگلیٹس اس گرداب کو ختم کر کے ہوا کی رکاوٹ کم کرتے ہیں۔"
    ),
    (
        "Why does an apple slice turn brown a few minutes after being peeled and exposed to room air?",
        ["Polyphenol oxidase enzymes catalyze the oxidation of phenols into dark melanin pigments upon contact with oxygen", "Bacteria consume the fruit sugars", "Iron in the knife rusts the flesh", "Moisture evaporation concentrates natural dyes"],
        "Polyphenol oxidase enzymes catalyze the oxidation of phenols into dark melanin pigments upon contact with oxygen",
        "Enzymatic browning occurs when cellular trauma introduces atmospheric oxygen to polyphenol oxidase and phenolic compounds.",
        "سیب کو کاٹ کر کھلی ہوا میں رکھنے پر اس کی سطح کچھ دیر بعد بھوری کیوں پڑ جاتی ہے؟",
        ["سیب کے اینزائمز ہوا کی آکسیجن کے ساتھ مل کر فینولز کی آکسیڈیشن کرتے ہیں", "بیکٹیریا فوری طور پر شکر کھا جاتے ہیں", "چھری کا لوہا سیب پر زنگ لگاتا ہے", "نمی اڑنے سے رنگ گہرا ہو جاتا ہے"],
        "سیب کے اینزائمز ہوا کی آکسیجن کے ساتھ مل کر فینولز کی آکسیڈیشن کرتے ہیں",
        "جب سیب کا چھلکا اترتا ہے تو خلیات ٹوٹتے ہیں اور آکسیجن انزائمز کے ساتھ مل کر بھورا رنگ میلینن بناتی ہے۔"
    ),
    (
        "Why does pure olive oil turn cloudy and semi-solid when stored inside a standard household refrigerator?",
        ["Monounsaturated fatty acids with higher melting points crystallize at refrigerator temperatures (around 4°C)", "Water in the oil freezes into frost", "The cold air oxidizes the triglycerides", "Proteins coagulate due to bacterial action"],
        "Monounsaturated fatty acids with higher melting points crystallize at refrigerator temperatures (around 4°C)",
        "Oleic acid and triacylglycerols have freezing points between 0°C and 5°C, causing them to solidify without spoiling the oil.",
        "زیتون کا خالص تیل فریج میں رکھنے پر دھندلا اور نیم جما ہوا کیوں ہو جاتا ہے؟",
        ["زیتون کے تیل کے فیٹی ایسڈز 4 ڈگری سینٹی گریڈ پر قلمی شکل (Crystallize) اختیار کر لیتے ہیں", "تیل میں موجود پانی برف بن جاتا ہے", "ٹھنڈی ہوا چربی کو خراب کر دیتی ہے", "بیکٹیریا تیل کو دہی بنا دیتے ہیں"],
        "زیتون کے تیل کے فیٹی ایسڈز 4 ڈگری سینٹی گریڈ پر قلمی شکل (Crystallize) اختیار کر لیتے ہیں",
        "زیتون کے مونو ان سیچوریٹڈ فیٹس کم درجہ حرارت پر جمنے لگتے ہیں، کمرے کے درجہ حرارت پر واپس مائع بن جاتے ہیں۔"
    ),
    (
        "Why do modern passenger cars feature front crumple zones designed to crush easily during a severe crash?",
        ["Extending crash impact duration reduces peak deceleration force transferred to passengers (F = dp/dt)", "To make vehicles cheaper to manufacture", "To prevent engine parts from flying away", "To absorb gasoline spills safely"],
        "Extending crash impact duration reduces peak deceleration force transferred to passengers (F = dp/dt)",
        "By deforming progressively, crumple zones absorb kinetic energy over a longer time span, mitigating fatal deceleration spikes.",
        "جدید گاڑیوں کے اگلے حصے حادثے کے وقت دبنے (Crumple zone) کے لیے جان بوجھ کر لچکدار کیوں بنائے جاتے ہیں؟",
        ["ٹکراؤ کے وقت کا دورانیہ بڑھا کر مسافروں پر لگنے والے مہلک جھٹکے کو کم کرنے کے لیے", "گاڑی بنانے کا خرچ کم کرنے کے لیے", "انجن کے پرزے بکھرنے سے روکنے کے لیے", "پیٹرول لیک ہونے سے بچانے کے لیے"],
        "ٹکراؤ کے وقت کا دورانیہ بڑھا کر مسافروں پر لگنے والے مہلک جھٹکے کو کم کرنے کے لیے",
        "اگر گاڑی فوری رک جائے تو مسافروں پر شدید دھچکا لگتا ہے، جبکہ باڈی دب کر جھٹکے کے وقت کو بڑھاتی ہے جس سے جان بچتی ہے۔"
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
        "Why do soap bubbles always form perfect spheres in mid-air regardless of the shape of the plastic wand used to blow them?",
        ["A sphere has the minimum surface area for any given enclosed volume, minimizing surface tension energy", "Air pressure is spherical in atmosphere", "Wand vibrations round the edges", "Gravity molds bubbles from underneath"],
        "A sphere has the minimum surface area for any given enclosed volume, minimizing surface tension energy",
        "Surface tension continuously pulls the soap film inward until it achieves the lowest possible potential energy state: a sphere.",
        "صابن کا بلبلہ ہوا میں اڑتے ہی ہمیشہ گول دائرہ کیوں بن جاتا ہے چاہے پھونکنے والا فریم چوکور یا تکون ہی کیوں نہ ہو؟",
        ["کروی شکل (Sphere) کم سے کم سطحی رقبہ رکھتی ہے جو سطحی تناؤ کی توانائی کو کم ترین سطح پر لاتی ہے", "فضا میں ہوا گول دباؤ ڈالتی ہے", "ہوا کے جھونکے کونوں کو گول کرتے ہیں", "کشش ثقل نیچے سے دائرہ بناتی ہے"],
        "کروی شکل (Sphere) کم سے کم سطحی رقبہ رکھتی ہے جو سطحی تناؤ کی توانائی کو کم ترین سطح پر لاتی ہے",
        "مائع کی سطح کا تناؤ ہمیشہ اندر کی طرف کھینچتا ہے، اور کائنات میں کسی دیے گئے حجم کے لیے سب سے کم رقبہ گیند کا ہوتا ہے۔"
    ),
    (
        "Why does a magnifying glass burn dry leaves under bright sunlight, but a flat glass window pane never does?",
        ["A convex lens refracts parallel sun rays to converge at a single intense focal point, concentrating thermal flux", "Flat glass reflects 100 percent of heat", "A magnifying glass has special magnifying chemicals", "Flat glass filters out infrared rays"],
        "A convex lens refracts parallel sun rays to converge at a single intense focal point, concentrating thermal flux",
        "Refraction through curved geometry focuses wide electromagnetic solar energy onto a pinpoint area, reaching ignition temperature.",
        "دھوپ میں محدب عدسہ (Magnifying glass) سوکھے پتوں کو جلا دیتا ہے مگر کھڑکی کا سیدھا شیشہ کبھی نہیں جلاتا، کیوں؟",
        ["محدب عدسہ متوازی کرنوں کو موڑ کر ایک باریک نقطے (Focus) پر مرتکز کرتا ہے جس سے شدید حرارت بنتی ہے", "کھڑکی کا شیشہ ساری گرمی واپس پلٹاتا ہے", "عدسے پر آگ لگانے والے کیمیکل لگے ہوتے ہیں", "کھڑکی کا شیشہ روشنی کو روک لیتا ہے"],
        "محدب عدسہ متوازی کرنوں کو موڑ کر ایک باریک نقطے (Focus) پر مرتکز کرتا ہے جس سے شدید حرارت بنتی ہے",
        "سیدھا شیشہ روشنی کو بغیر موڑے سیدھا گزرنے دیتا ہے، جبکہ عدسہ پھیلی ہوئی تمام حرارت کو ایک سوئی جتنے نقطے پر جمع کر دیتا ہے۔"
    ),
    (
        "Why do divers ascending too rapidly from deep underwater suffer from the painful condition known as 'the bends'?",
        ["Rapid depressurization causes dissolved nitrogen gas to form expanding bubbles in bloodstream and tissues", "Lungs fill with seawater vapor", "Oxygen burns nerve endings", "Blood pressure drops to absolute zero"],
        "Rapid depressurization causes dissolved nitrogen gas to form expanding bubbles in bloodstream and tissues",
        "Henry's law dictates gas solubility drops with decreasing hydrostatic pressure; dissolved nitrogen effervesces dangerously.",
        "سمندر کی گہرائی سے غوطہ خور کے اچانک تیزی سے اوپر آنے پر اسے 'بینڈز' (The Bends) کا شدید درد کیوں ہوتا ہے؟",
        ["پانی کا دباؤ اچانک کم ہونے سے خون میں گھلی ہوئی نائٹروجن گیس بلبلے بن کر رگوں میں پھنس جاتی ہے", "پھیپھڑوں میں سمندری پانی بھر جاتا ہے", "آکسیجن اعصاب کو جلا دیتی ہے", "خون کا دباؤ اچانک ختم ہو جاتا ہے"],
        "پانی کا دباؤ اچانک کم ہونے سے خون میں گھلی ہوئی نائٹروجن گیس بلبلے بن کر رگوں میں پھنس جاتی ہے",
        "ہنری کے قانون کے مطابق گہرائی میں زیادہ دباؤ سے نائٹروجن خون میں گھل جاتی ہے، اچانک اوپر آنے سے وہ سوڈا بوتل کی طرح ابل پڑتی ہے۔"
    ),
    (
        "Why does a mirror reverse left and right from our perspective, but never reverses up and down?",
        ["A mirror actually reverses front-to-back (depth axis), which our brain perceives as a left-right swap", "Gravity aligns photons vertically", "Human eyes are spaced horizontally", "Mirror glass has horizontal polarity"],
        "A mirror actually reverses front-to-back (depth axis), which our brain perceives as a left-right swap",
        "Reflections invert the z-axis (perpendicular to mirror plane). We mentally imagine rotating 180 degrees to face ourselves, producing apparent lateral inversion.",
        "آئینہ ہمارے دیکھنے کے زاویے سے دائیں اور بائیں کو الٹ دیتا ہے مگر اوپر اور نیچے کو کبھی الٹ کیوں نہیں کرتا؟",
        ["آئینہ دراصل آگے اور پیچھے (Depth axis) کو الٹتا ہے، جسے انسانی دماغ دائیں بائیں کا الٹ سمجھتا ہے", "کشش ثقل روشنی کو عمودی رکھتی ہے", "انسانی آنکھیں افقی لکیر میں ہوتی ہیں", "آئینے کی بناوٹ افقی ہوتی ہے"],
        "آئینہ دراصل آگے اور پیچھے (Depth axis) کو الٹتا ہے، جسے انسانی دماغ دائیں بائیں کا الٹ سمجھتا ہے",
        "آئینہ آپ کے سامنے کے رخ کو اندر موڑتا ہے۔ اگر آپ اپنے پاؤں کو آئینے کے سامنے رکھیں تو وہ وہیں نظر آئیں گے، خرابی ہمارے دماغ کے تصور میں ہے۔"
    ),
    (
        "Why does a sharp kitchen knife cut raw vegetables far more effortlessly than a dull blunt knife?",
        ["A minuscule edge surface area concentrates applied downward force into vastly higher cutting pressure (P = F/A)", "Sharp steel has higher density", "Blunt blades generate friction heat", "Vegetables chemically attract sharp edges"],
        "A minuscule edge surface area concentrates applied downward force into vastly higher cutting pressure (P = F/A)",
        "Pressure is inversely proportional to area. A microscopic razor edge creates thousands of pounds of pressure per square inch.",
        "ایک تیز چھری سبزی کو کند چھری کے مقابلے میں اتنی آسانی اور صفائی سے کیوں کاٹ دیتی ہے؟",
        ["دھار کا باریک کنارہ دباؤ کے رقبے کو کم کر کے فورس کو ہزاروں گنا زیادہ پریشر میں بدل دیتا ہے (P = F/A)", "تیز لوہے کی کثافت زیادہ ہوتی ہے", "کند چھری رگڑ سے گرم ہو جاتی ہے", "سبزیاں تیز دھار کو اپنی طرف کھینچتی ہیں"],
        "دھار کا باریک کنارہ دباؤ کے رقبے کو کم کر کے فورس کو ہزاروں گنا زیادہ پریشر میں بدل دیتا ہے (P = F/A)",
        "دباؤ رقبے کے الٹ ہوتا ہے۔ جب چھری کی دھار بال جیسی باریک ہوتی ہے تو ہلکے ہاتھ کا دباؤ بھی سبزی کے ریشوں کو فوراً کاٹ دیتا ہے۔"
    ),
    (
        "Why do tall commercial skyscrapers sway back and forth in high-altitude gale winds without cracking their foundations?",
        ["They are engineered with structural flexibility and tuned mass dampers to dissipate oscillation kinetic energy", "Skyscrapers are anchored to bedrock with elastic rubber bands", "Winds at high altitude have zero air density", "Windows open to allow wind to pass freely"],
        "They are engineered with structural flexibility and tuned mass dampers to dissipate oscillation kinetic energy",
        "Rigid brittle structures fracture; flexible steel frames sway harmonically, while suspended counterweights cancel out resonance.",
        "اونچے فلک بوس ٹاور تیز آندھی میں دائیں بائیں جھولنے کے باوجود اپنی بنیادوں سے اکھڑتے کیوں نہیں؟",
        ["وہ لچکدار فریم اور اندرونی وزنی ڈیمپرز (Tuned mass dampers) کے ساتھ بنائے جاتے ہیں جو جھٹکوں کو جذب کر لیتے ہیں", "وہ ربڑ کی رسیوں سے بندھے ہوتے ہیں", "بلندی پر ہوا کا دباؤ نہیں ہوتا", "کھڑکیاں کھل کر ہوا کو گزار دیتی ہیں"],
        "وہ لچکدار فریم اور اندرونی وزنی ڈیمپرز (Tuned mass dampers) کے ساتھ بنائے جاتے ہیں جو جھٹکوں کو جذب کر لیتے ہیں",
        "اگر عمارت بالکل سخت ہو تو وہ ٹوٹ جائے گی۔ انجینئر عمارت کو درخت کی طرح لچکدار بناتے ہیں اور اندر بھاری گولہ مخالف سمت میں جھولتا ہے۔"
    ),
    (
        "Why does sprinkling dry sodium chloride salt onto icy sidewalks cause the solid ice to melt at sub-zero temperatures?",
        ["Dissolved salt ions lower the freezing point of water below zero degrees Celsius (freezing point depression)", "Salt chemically burns the ice with exothermic acid", "Salt absorbs sunlight and heats up to 50 degrees", "Salt crystals grind ice mechanically"],
        "Dissolved salt ions lower the freezing point of water below zero degrees Celsius (freezing point depression)",
        "Solute ions disrupt the thermodynamic equilibrium of ice crystal formation, forcing water to stay liquid down to roughly -21°C.",
        "برف سے جمی سڑک پر نمک چھڑکنے سے نقطہ انجماد سے نیچے ٹھنڈ کے باوجود برف کیوں پگھل جاتی ہے؟",
        ["نمک پانی کے نقطہ انجماد کو صفر سے نیچے گرا دیتا ہے جس سے برف مائع بن جاتی ہے (Freezing point depression)", "نمک تیزاب بن کر برف کو جلا دیتا ہے", "نمک سورج کی دھوپ سے 50 ڈگری گرم ہو جاتا ہے", "نمک کے دانے رگڑ کر برف توڑتے ہیں"],
        "نمک پانی کے نقطہ انجماد کو صفر سے نیچے گرا دیتا ہے جس سے برف مائع بن جاتی ہے (Freezing point depression)",
        "نمک کے ذرات پانی کے مالیکیولز کو آپس میں جڑ کر برف کی قلمیں بنانے سے روکتے ہیں، جس سے پانی منفی درجہ حرارت پر بھی بہتا رہتا ہے۔"
    ),
    (
        "Why does a person feeling motion sickness on a ship feel much better when looking at the distant fixed ocean horizon?",
        ["It resolves the sensory conflict between the inner ear's vestibular balance canals and visual input", "The horizon is cooler in temperature", "Focusing eyes lowers heartbeat to zero", "Horizon clouds produce calming acoustic frequencies"],
        "It resolves the sensory conflict between the inner ear's vestibular balance canals and visual input",
        "Motion sickness occurs when inner ear fluid signals rolling motion while cabin walls appear stationary; the horizon confirms actual movement.",
        "بحری جہاز پر متلی اور چکر محسوس کرنے والا شخص جب دور افق (Horizon) کو دیکھتا ہے تو اس کی طبیعت کیوں سنبھل جاتی ہے؟",
        ["یہ اندرونی کان کے توازن کے سگنل اور آنکھوں کے دیکھنے کے درمیان تضاد کو ختم کر دیتا ہے", "افق کا درجہ حرارت ٹھنڈا ہوتا ہے", "دور دیکھنے سے دل کی دھڑکن رک جاتی ہے", "افق کے بادل سکون دیتے ہیں"],
        "یہ اندرونی کان کے توازن کے سگنل اور آنکھوں کے دیکھنے کے درمیان تضاد کو ختم کر دیتا ہے",
        "متلی اس وقت ہوتی ہے جب کان حرکت محسوس کریں مگر کیبن کی دیواریں ساکن لگیں۔ دور افق کو دیکھ کر دماغ حقیقت تسلیم کر لیتا ہے۔"
    ),
    (
        "Why does striking an ordinary safety match against a box ignite fire, whereas striking it against a smooth tile fails?",
        ["The box strike strip contains red phosphorus that converts to white phosphorus by friction heat, igniting potassium chlorate", "The tile is too cold for matches", "Match heads contain invisible gunpowder", "Smooth tiles absorb all friction electricity"],
        "The box strike strip contains red phosphorus that converts to white phosphorus by friction heat, igniting potassium chlorate",
        "Friction converts red phosphorus on the strip into volatile white phosphorus, which ignites and triggers the match head's oxidizer.",
        "ماچس کی تیلی کو ڈبیا کی پٹی پر رگڑنے سے آگ بھڑک اٹھتی ہے مگر چکنی ٹائل پر رگڑنے سے کیوں نہیں جلتی؟",
        ["ڈبیا کی پٹی پر سرخ فاسفورس ہوتا ہے جو رگڑ کی حرارت سے ماچس کے کیمیکل کو آگ لگاتا ہے", "ٹائل بہت ٹھنڈی ہوتی ہے", "تیلی میں بارود بھرا ہوتا ہے", "چکنی ٹائل رگڑ کا چارج چوس لیتی ہے"],
        "ڈبیا کی پٹی پر سرخ فاسفورس ہوتا ہے جو رگڑ کی حرارت سے ماچس کے کیمیکل کو آگ لگاتا ہے",
        "سیفٹی ماچس کے مصالحے میں صرف ایندھن ہوتا ہے، جلانے والا فاسفورس ڈبیا کی سائیڈ پر ہوتا ہے۔ دونوں ملنے پر ہی آگ لگتی ہے۔"
    ),
    (
        "Why do birds sitting on high-voltage electrical power transmission lines never get electrocuted?",
        ["Both of the bird's feet are on the same cable at identical electrical potential, creating zero voltage difference", "Bird claws are made of pure electrical insulating rubber", "Power line exterior rubber absorbs all current", "High voltage currents only travel inside the metal core"],
        "Both of the bird's feet are on the same cable at identical electrical potential, creating zero voltage difference",
        "Current flows only across a potential difference (voltage drop). With both feet at equal potential, zero current traverses the bird.",
        "ہائی وولٹیج بجلی کی ننگی تاروں پر بیٹھے پرندوں کو کرنٹ کیوں نہیں لگتا؟",
        ["پرندے کے دونوں پنجے ایک ہی تار پر ایک جیسے وولٹیج پر ہوتے ہیں، جس سے کوئی برقی فرق نہیں بنتا", "پرندوں کے پنجے ربڑ کے بنے ہوتے ہیں", "تار پر موٹی انسولیشن چڑھی ہوتی ہے", "کرنٹ صرف تار کے مرکز میں رہتا ہے"],
        "پرندے کے دونوں پنجے ایک ہی تار پر ایک جیسے وولٹیج پر ہوتے ہیں، جس سے کوئی برقی فرق نہیں بنتا",
        "کرنٹ گزرنے کے لیے دو مختلف وولٹیج یا زمین سے رابطہ ضروری ہوتا ہے۔ پرندے کے جسم کے آر پار کوئی پوٹینشل فرق نہیں ہوتا۔"
    ),
    (
        "Why does a thermos vacuum flask keep hot soup steaming hot for many hours without any internal electric heating?",
        ["The double-walled vacuum barrier eliminates thermal conduction and convection, while silvered walls reflect radiant heat", "It contains pressurized boiling gas", "The outer shell produces insulation energy", "Soup emits perpetual heat when sealed"],
        "The double-walled vacuum barrier eliminates thermal conduction and convection, while silvered walls reflect radiant heat",
        "Without matter between walls, conduction and convection cannot occur; mirror coatings bounce electromagnetic infrared rays back inside.",
        "تھرمس (Thermos) میں رکھی گرم چائے بغیر کسی ہیٹر کے کئی گھنٹے تک گرم کیسے رہتی ہے؟",
        ["ڈبل دیواروں کے درمیان خلا کنڈکشن اور کنویکشن کو روکتا ہے، اور چمکدار سطح شعاعی حرارت کو واپس اچھالتی ہے", "اس میں ابلتی ہوئی گیس بھری ہوتی ہے", "باہر کا خول گرمی بناتا رہتا ہے", "بند چائے خود بخود گرمی پیدا کرتی ہے"],
        "ڈبل دیواروں کے درمیان خلا کنڈکشن اور کنویکشن کو روکتا ہے، اور چمکدار سطح شعاعی حرارت کو واپس اچھالتی ہے",
        "حرارت گزرنے کے لیے ہوا یا مادہ چاہیے، تھرمس کی دوہری دیوار میں ویکیوم ہوتا ہے اور چاندی جیسی پالش گرمی کی لہروں کو اندر ہی رکھتی ہے۔"
    ),
    (
        "Why do bubbles form on the bottom of a pot of water long before the water reaches its boiling point of 100 degrees Celsius?",
        ["Dissolved atmospheric gases (nitrogen and oxygen) precipitate out of solution as water temperature rises", "Water molecules split into hydrogen gas", "The metal bottom is melting into vapor", "Air leaks through the stainless steel"],
        "Dissolved atmospheric gases (nitrogen and oxygen) precipitate out of solution as water temperature rises",
        "Gas solubility decreases sharply with heating, causing previously dissolved air to nucleate as visible bubbles at 50-70°C.",
        "پانی ابلنے (100 ڈگری) سے کافی پہلے برتن کے پیندے پر چھوٹے بلبلے کیوں بننے لگتے ہیں؟",
        ["پانی میں گھلی ہوئی ہوائیں (آکسیجن اور نائٹروجن) گرمی پا کر باہر نکلتی ہیں", "پانی ہائیڈروجن گیس میں تبدیل ہو رہا ہوتا ہے", "برتن کا پیندا پگھل رہا ہوتا ہے", "سٹیل کے نیچے سے ہوا اندر آتی ہے"],
        "پانی میں گھلی ہوئی ہوائیں (آکسیجن اور نائٹروجن) گرمی پا کر باہر نکلتی ہیں",
        "ٹھنڈے پانی میں ہوا کے مالیکیولز گھلے ہوتے ہیں۔ گرم ہونے پر پانی گیس کو روک نہیں پاتا اور وہ بلبلے بن کر پیندے سے اوپر اٹھتی ہے۔"
    ),
    (
        "Why does a helium balloon deflate slowly over several days inside a closed room even when securely tied with a tight knot?",
        ["Helium atoms are so minuscule that they effuse through microscopic sub-nanometer pores in the rubber latex membrane", "Helium turns into liquid inside", "Rubber chemically dissolves the helium", "Static electricity destroys helium atoms"],
        "Helium atoms are so minuscule that they effuse through microscopic sub-nanometer pores in the rubber latex membrane",
        "Helium's atomic radius is tiny (~31 pm); concentration gradient drives helium effusion directly through polymer chains.",
        "ہیلیئم کا غبارہ مضبوطی سے بندھا ہونے کے باوجود چند دنوں میں خود بخود پچک کیوں جاتا ہے؟",
        ["ہیلیئم کے ایٹم اتنے چھوٹے ہوتے ہیں کہ وہ ربڑ کے باریک مساموں سے باہر نکل جاتے ہیں", "ہیلیئم اندر مائع بن جاتی ہے", "ربڑ گیس کو پی جاتا ہے", "ساکن بجلی گیس کو ختم کر دیتی ہے"],
        "ہیلیئم کے ایٹم اتنے چھوٹے ہوتے ہیں کہ وہ ربڑ کے باریک مساموں سے باہر نکل جاتے ہیں",
        "ہیلیئم کا ایٹم کائنات کے سب سے چھوٹے ذرات میں سے ایک ہے۔ ربڑ کے مالیکیولز کے درمیان باریک خالی جگہوں سے وہ آہستہ آہستہ رس جاتا ہے۔"
    ),
    (
        "Why does a person feeling cold begin to shiver uncontrollably?",
        ["Involuntary rapid skeletal muscle contractions generate metabolic heat to restore homeostatic body temperature", "Nerves freeze and vibrate", "Blood vessels rupture in the skin", "The heart slows down during shivering"],
        "Involuntary rapid skeletal muscle contractions generate metabolic heat to restore homeostatic body temperature",
        "The hypothalamus triggers oscillating somatic motor neuron signals; muscular inefficiency converts ATP into thermal energy.",
        "سردی لگنے پر انسان کا جسم خود بخود کانپنے (Shivering) کیوں لگتا ہے؟",
        ["پٹھوں کا تیزی سے سکڑنا اور پھیلنا حرارت پیدا کر کے جسم کا اندرونی درجہ حرارت بحال کرتا ہے", "اعصاب جم کر لرزتے ہیں", "جلد کی رگیں پھٹ جاتی ہیں", "کانپنے سے دل کی دھڑکن رک جاتی ہے"],
        "پٹھوں کا تیزی سے سکڑنا اور پھیلنا حرارت پیدا کر کے جسم کا اندرونی درجہ حرارت بحال کرتا ہے",
        "دماغ کا ہائپوتھیلمس سردی محسوس کرتے ہی پٹھوں کو مسلسل حرکت کا حکم دیتا ہے تاکہ جسم کے اندر فوری طور پر گرمی پیدا ہو سکے۔"
    ),
    (
        "Why does an ordinary iron nail rust quickly when exposed to humid outdoor air, but stays pristine inside completely dry air?",
        ["Corrosion requires both oxygen and liquid water to form an electrochemical cell that oxidizes metallic iron", "Dry air contains zero oxygen molecules", "Humid air is acidic from clouds", "Sunlight only shines through humid air"],
        "Corrosion requires both oxygen and liquid water to form an electrochemical cell that oxidizes metallic iron",
        "Water acts as an electrolyte allowing electron flow between anodic iron oxidation and cathodic oxygen reduction.",
        "لوہے کی کیل نمی والی کھلی ہوا میں جلد زنگ آلود ہو جاتی ہے جبکہ بالکل خشک ہوا میں سالہا سال محفوظ کیوں رہتی ہے؟",
        ["زنگ لگنے کے کیمیائی عمل کے لیے آکسیجن اور پانی (نمی) دونوں کا ایک ساتھ ہونا لازمی ہے", "خشک ہوا میں آکسیجن نہیں ہوتی", "نمی والی ہوا بادلوں سے تیزابی ہوتی ہے", "دھوپ صرف نمی میں چمکتی ہے"],
        "زنگ لگنے کے کیمیائی عمل کے لیے آکسیجن اور پانی (نمی) دونوں کا ایک ساتھ ہونا لازمی ہے",
        "پانی الیکٹرولائٹ کا کام کرتا ہے جس کے بغیر لوہا آکسیجن سے مل کر آئرن آکسائیڈ نہیں بنا سکتا۔ اکیلی خشک آکسیجن زنگ نہیں لگا سکتی۔"
    ),
    (
        "Why does the human eye pupil constrict to a tiny pinhole when stepping outside into blazing direct sunlight?",
        ["The iris sphincter muscle contracts to limit retinal light exposure and prevent photoreceptor saturation", "The cornea shrinks from heat", "Tear fluid covers the pupil opening", "UV radiation solidifies the lens"],
        "The iris sphincter muscle contracts to limit retinal light exposure and prevent photoreceptor saturation",
        "The pupillary light reflex adjusts aperture to protect delicate rods and cones while maximizing visual acuity.",
        "تیز دھوپ میں نکلتے ہی انسانی آنکھ کی پتلی (Pupil) سکڑ کر چھوٹی کیوں ہو جاتی ہے؟",
        ["آنکھ کے پردے (Retina) کو تیز روشنی سے محفوظ رکھنے کے لیے پتلی سکڑ کر روشنی کی مقدار کم کرتی ہے", "گرمی سے پتلی پگھل جاتی ہے", "آنسو پتلی کو ڈھانپ لیتے ہیں", "شعاعیں لینز کو جما دیتی ہیں"],
        "آنکھ کے پردے (Retina) کو تیز روشنی سے محفوظ رکھنے کے لیے پتلی سکڑ کر روشنی کی مقدار کم کرتی ہے",
        "یہ ایک خودکار حفاظتی نظام ہے جو کیمرے کے اپرچر کی طرح کام کرتا ہے تاکہ روشنی کے نازک خلیات جلنے سے بچ سکیں۔"
    ),
    (
        "Why do wet clothes dry outdoors on a clothesline even on a cool, cloudy day well below water's boiling point?",
        ["Water molecules with high kinetic energy overcome intermolecular hydrogen bonds and evaporate into unsaturated air", "Cloud shadows pull moisture upward", "Wind friction creates boiling temperatures", "Gravity pulls water down into vapor"],
        "Water molecules with high kinetic energy overcome intermolecular hydrogen bonds and evaporate into unsaturated air",
        "Evaporation is a surface phenomenon occurring at all temperatures as long as the relative humidity of surrounding air is below 100%.",
        "ٹھنڈے اور ابر آلود دن میں بھی تنی ہوئی رسی پر گیلے کپڑے ابلے بغیر کیسے سوکھ جاتے ہیں؟",
        ["پانی کے تیز رفتار مالیکیولز سطح سے بخارات بن کر خشک ہوا میں اڑ جاتے ہیں (Evaporation)", "بادلوں کا سایہ نمی کو اوپر کھینچتا ہے", "ہوا کی رگڑ سے پانی ابلتا ہے", "کشش ثقل پانی کو گیس بناتی ہے"],
        "پانی کے تیز رفتار مالیکیولز سطح سے بخارات بن کر خشک ہوا میں اڑ جاتے ہیں (Evaporation)",
        "بخارات بننے کے لیے ابلنا ضروری نہیں ہے۔ ہوا میں نمی کم ہو تو پانی کی سطح سے مالیکیولز ہر درجہ حرارت پر ہوا میں اڑتے رہتے ہیں۔"
    ),
    (
        "Why does an ocean tidal wave arrive at coastlines twice every 24 hours and 50 minutes rather than once?",
        ["The Moon's gravitational pull creates two oceanic bulges: one facing the Moon, and one on the opposite side due to inertia", "The Sun pulls ocean waters sideways", "Earth's core wobbles twice per day", "Ocean seafloor expands and contracts"],
        "The Moon's gravitational pull creates two oceanic bulges: one facing the Moon, and one on the opposite side due to inertia",
        "Differential gravitational pull stretches Earth into a football shape, creating antipodal tidal crests that Earth rotates through.",
        "سمندر میں مدوجزر (Tides) کا اونچا پانی 24 گھنٹوں میں ایک بار آنے کی بجائے دو بار ساحل پر کیوں آتا ہے؟",
        ["چاند کی کشش ایک لہر چاند کے سامنے اور دوسری انرشیا کی وجہ سے بالکل مخالف سمت میں پیدا کرتی ہے", "سورج پانی کو پہلو میں کھینچتا ہے", "زمین کا مرکز دن میں دو بار ہلتا ہے", "سمندر کی تہہ پھیلتی اور سکڑتی ہے"],
        "چاند کی کشش ایک لہر چاند کے سامنے اور دوسری انرشیا کی وجہ سے بالکل مخالف سمت میں پیدا کرتی ہے",
        "چاند زمین کے قریبی پانی کو کھینچتا ہے اور زمین کو دور والے پانی سے دور کھینچتا ہے، جس سے زمین کے دونوں طرف پانی کے دو ابھار بنتے ہیں۔"
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
        "Why does an open soda bottle go flat much faster when left warm on a kitchen counter compared to cold inside a refrigerator?",
        ["Carbon dioxide gas solubility in liquids decreases dramatically as liquid temperature increases", "Warm air sucks gas bubbles out", "Sugar breaks down into gas in heat", "Plastic caps leak more when warm"],
        "Carbon dioxide gas solubility in liquids decreases dramatically as liquid temperature increases",
        "Henry's law demonstrates that higher kinetic energy enables dissolved CO2 gas molecules to overcome attraction and escape the solution.",
        "گرم کمرے میں رکھی بوتل سے گیس فریج میں رکھی ٹھنڈی بوتل کے مقابلے میں اتنی جلدی کیوں اڑ جاتی ہے؟",
        ["مائع کا درجہ حرارت بڑھنے سے کاربن ڈائی آکسائیڈ گیس کی حل پذیری (Solubility) تیزی سے کم ہو جاتی ہے", "گرم ہوا گیس کو چوس لیتی ہے", "گرمی میں چینی گیس بن جاتی ہے", "گرم بوتل کا ڈھکن ڈھیلا ہو جاتا ہے"],
        "مائع کا درجہ حرارت بڑھنے سے کاربن ڈائی آکسائیڈ گیس کی حل پذیری (Solubility) تیزی سے کم ہو جاتی ہے",
        "گیسیں ٹھنڈے پانی میں زیادہ مضبوطی سے گھلتی ہیں۔ درجہ حرارت بڑھتے ہی گیس کے مالیکیولز تیزی سے مائع سے فرار ہو جاتے ہیں۔"
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
        "Why does salt dissolve completely in water, while sand remains completely insoluble at the bottom?",
        ["Water is polar and easily hydrates the charged sodium and chloride ions, but cannot break the strong covalent network of quartz", "Sand is heavier than salt", "Salt is made of sugar molecules", "Water contains microscopic acids"],
        "Water is polar and easily hydrates the charged sodium and chloride ions, but cannot break the strong covalent network of quartz",
        "Water's dipole moment provides sufficient electrostatic solvation energy to overcome ionic lattice bonds, but cannot dissociate silicon dioxide.",
        "نمک پانی میں گھل کر غائب ہو جاتا ہے جبکہ ریت پیندے پر ویسی ہی کیوں پڑی رہتی ہے؟",
        ["پانی نمک کے چارج شدہ آئنز کو الگ کر لیتا ہے مگر ریت کے کوویلنٹ جال (سلیکون ڈائی آکسائیڈ) کو توڑ نہیں پاتا", "ریت نمک سے بھاری ہوتی ہے", "نمک چینی سے بنا ہوتا ہے", "پانی میں تیزاب ہوتا ہے"],
        "پانی نمک کے چارج شدہ آئنز کو الگ کر لیتا ہے مگر ریت کے کوویلنٹ جال (سلیکون ڈائی آکسائیڈ) کو توڑ نہیں پاتا",
        "پانی کے پولر مالیکیولز نمک کے آئنز کو گھیر کر آسانی سے تحلیل کر لیتے ہیں، جبکہ ریت کے مضبوط کیمیائی بندھنوں پر ان کا کوئی اثر نہیں ہوتا۔"
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
    )
]

print(f"Normal Remaining Part 1 loaded: {len(ITEMS)} items.")
