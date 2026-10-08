# -*- coding: utf-8 -*-
"""
Catalog Easy - Part 1 (Items 1 to 125)
Classic riddles, household objects, nature, animals, and common-sense logic.
Zero template loops, zero repeated POVs.
"""

ITEMS = [
    # 1: Towel
    {
        "en": ("What gets wetter the more it dries?", ["A towel", "A sponge", "A cloud", "Rain"], "A towel", "A towel absorbs moisture from your body as it dries you."),
        "ur": ("وہ کون سی چیز ہے جو خشک کرتے وقت خود گیلی ہو جاتی ہے؟", ["تولیہ", "بادل", "سورج", "ریت"], "تولیہ", "تولیہ پانی جذب کرتا ہے جس سے وہ خود گیلا ہو جاتا ہے۔")
    },
    # 2: Clock
    {
        "en": ("What has hands but cannot clap?", ["A clock", "A glove", "A tree", "A robot"], "A clock", "A clock has hour and minute hands but cannot clap."),
        "ur": ("وہ کیا ہے جس کے ہاتھ ہیں مگر وہ تالی نہیں بجا سکتی؟", ["گھڑی", "درخت", "کرسی", "دستانہ"], "گھڑی", "گھڑی کی سوئیاں اس کے ہاتھ کہلاتی ہیں مگر وہ تالی نہیں بجا سکتیں۔")
    },
    # 3: Egg
    {
        "en": ("What has to be broken before you can use it?", ["An egg", "A bottle", "A lock", "A stick"], "An egg", "You must crack an eggshell before cooking or consuming it."),
        "ur": ("وہ کون سی چیز ہے جسے استعمال کرنے سے پہلے توڑنا پڑتا ہے؟", ["انڈا", "تالہ", "شیشہ", "بادام"], "انڈا", "انڈے کو پکانے یا کھانے کے لیے پہلے توڑنا پڑتا ہے۔")
    },
    # 4: Candle
    {
        "en": ("I am tall when young, and short when old. What am I?", ["A candle", "A tree", "A giraffe", "A building"], "A candle", "A candle melts down shorter as it burns over time."),
        "ur": ("وہ کیا ہے جو نیا ہو تو لمبا اور پرانا ہو تو چھوٹا ہو جاتا ہے؟", ["موم بتی", "درخت", "پنسل", "رسی"], "موم بتی", "موم بتی جلنے کے ساتھ ساتھ پگھل کر چھوٹی ہوتی جاتی ہے۔")
    },
    # 5: Calendar months
    {
        "en": ("Which month of the year has 28 days?", ["All 12 months", "Only February", "Only January", "None of them"], "All 12 months", "Every calendar month has at least 28 days."),
        "ur": ("سال کے کتنے مہینوں میں 28 دن ہوتے ہیں؟", ["تمام 12 مہینوں میں", "صرف فروری میں", "چار مہینوں میں", "کسی میں نہیں"], "تمام 12 مہینوں میں", "ہر مہینے میں کم از کم 28 دن تو لازمی ہوتے ہیں۔")
    },
    # 6: Sponge
    {
        "en": ("What is full of holes but still holds water?", ["A sponge", "A bucket", "A net", "A colander"], "A sponge", "A sponge is filled with porous holes and absorbs water."),
        "ur": ("وہ کون سی چیز ہے جو سوراخوں سے بھری ہے مگر پھر بھی پانی روک لیتی ہے؟", ["اسفنج", "چھلنی", "بالٹی", "جالی"], "اسفنج", "اسفنج میں بے شمار سوراخ ہوتے ہیں لیکن وہ پانی جذب کر لیتا ہے۔")
    },
    # 7: Are you asleep
    {
        "en": ("What question can you never answer 'yes' to honestly?", ["Are you asleep?", "Are you awake?", "Are you hungry?", "Are you ready?"], "Are you asleep?", "If you are truly asleep, you cannot consciously answer the question."),
        "ur": ("وہ کون سا سوال ہے جس کا جواب آپ سچائی سے کبھی 'ہاں' میں نہیں دے سکتے؟", ["کیا آپ سو رہے ہیں؟", "کیا آپ جاگ رہے ہیں؟", "کیا آپ بھوکے ہیں؟", "کیا آپ تیار ہیں؟"], "کیا آپ سو رہے ہیں؟", "اگر انسان واقعی سو رہا ہو تو وہ ہوش و حواس میں جواب نہیں دے سکتا۔")
    },
    # 8: The future
    {
        "en": ("What is always in front of you but cannot be seen?", ["The future", "Air", "Your nose", "Darkness"], "The future", "The future is always ahead in time, yet invisible until it arrives."),
        "ur": ("وہ کیا ہے جو ہمیشہ آپ کے سامنے ہوتا ہے مگر دیکھا نہیں جا سکتا؟", ["مستقبل", "ہوا", "اندھیرا", "روشنی"], "مستقبل", "مستقبل ہمیشہ آنے والے وقت میں آگے ہوتا ہے مگر اسے دیکھا نہیں جا سکتا۔")
    },
    # 9: One-story house
    {
        "en": ("There is a one-story pink house with pink furniture. What color are the stairs?", ["No stairs", "Pink", "White", "Brown"], "No stairs", "A one-story house has no second floor, so it has no stairs."),
        "ur": ("ایک منزلہ گلابی گھر میں ہر چیز گلابی ہے۔ بتائیں سیڑھیاں کس رنگ کی ہیں؟", ["کوئی سیڑھی نہیں", "گلابی", "سفید", "بھوری"], "کوئی سیڑھی نہیں", "ایک منزلہ مکان میں دوسری منزل ہی نہیں ہوتی تو سیڑھیاں کہاں سے آئیں گی۔")
    },
    # 10: Promise
    {
        "en": ("What can you break without ever picking it up or touching it?", ["A promise", "A window", "A twig", "A plate"], "A promise", "A promise is broken by failing to keep your word."),
        "ur": ("وہ کیا ہے جسے آپ چھوئے یا اٹھائے بغیر بھی توڑ سکتے ہیں؟", ["وعدہ", "شیشہ", "لکڑی", "تار"], "وعدہ", "وعدہ پورا نہ کرنے سے ٹوٹ جاتا ہے، اسے چھونے کی ضرورت نہیں۔")
    },
    # 11: Age
    {
        "en": ("What goes up but never comes down?", ["Your age", "A kite", "A balloon", "Smoke"], "Your age", "Your age only increases with each passing year."),
        "ur": ("وہ کون سی چیز ہے جو اوپر تو جاتی ہے مگر کبھی نیچے نہیں آتی؟", ["عمر", "پتنگ", "دھواں", "غبارہ"], "عمر", "انسان کی عمر وقت کے ساتھ صرف بڑھتی ہے، کم نہیں ہوتی۔")
    },
    # 12: Bald man
    {
        "en": ("A man walked in heavy rain with no umbrella or hat, yet did not get a single hair wet. Why?", ["He was bald", "He ran fast", "He wore a hood", "It was mist"], "He was bald", "He had no hair on his head to get wet."),
        "ur": ("ایک آدمی بارش میں بنا چھتری اور بنا ٹوپی کے گیا مگر اس کا ایک بال بھی نہیں بھیگا، کیوں؟", ["کیونکہ وہ گنجا تھا", "وہ تیز دوڑ رہا تھا", "اس نے پناہ لی", "بارش ہلکی تھی"], "کیونکہ وہ گنجا تھا", "اس کے سر پر بال ہی نہیں تھے جو بھیگتے۔")
    },
    # 13: Bottle
    {
        "en": ("What has a neck but no head?", ["A bottle", "A guitar", "A shirt", "A snake"], "A bottle", "A bottle has a narrow neck leading to its opening, but no head."),
        "ur": ("وہ کیا ہے جس کے پاس گردن ہے لیکن سر نہیں؟", ["بوتل", "قمیض", "گٹار", "چمچ"], "بوتل", "بوتل کا اوپری حصہ گردن کہلاتا ہے مگر اس کا سر نہیں ہوتا۔")
    },
    # 14: Glove
    {
        "en": ("What has a thumb and four fingers, but is not alive?", ["A glove", "A robot", "A mannequin", "A skeleton"], "A glove", "A glove has five finger slots but is an inanimate clothing item."),
        "ur": ("وہ کون سی چیز ہے جس کے چار انگلیاں اور ایک انگوٹھا ہے مگر وہ جاندار نہیں؟", ["دستانہ", "روبوٹ", "پتلا", "ڈھانچہ"], "دستانہ", "دستانے میں انگلیوں کی جگہ بنی ہوتی ہے مگر وہ بے جان ہوتا ہے۔")
    },
    # 15: Comb
    {
        "en": ("What has many teeth, but cannot bite?", ["A comb", "A saw", "A zipper", "A gear"], "A comb", "A hair comb has teeth designed for styling, not biting."),
        "ur": ("وہ کون سی چیز ہے جس کے دانت ہیں مگر وہ چبا یا کاٹ نہیں سکتی؟", ["کنگھی", "آری", "زپ", "کانٹا"], "کنگھی", "کنگھی کے دانت بال سنوارنے کے لیے ہوتے ہیں۔")
    },
    # 16: Coin
    {
        "en": ("What has a head and a tail, but no body?", ["A coin", "A snake", "A pin", "A kite"], "A coin", "A coin has heads and tails sides but no biological body."),
        "ur": ("وہ کیا ہے جس کا سر اور دم (ہیڈ اور ٹیل) تو ہے مگر کوئی دھڑ نہیں؟", ["سکہ", "سانپ", "سوئی", "تیر"], "سکہ", "سکے کے دو رخوں کو ہیڈ اور ٹیل کہا جاتا ہے مگر اس کا دھڑ نہیں ہوتا۔")
    },
    # 17: Mirror
    {
        "en": ("What reflects everything before it, yet has no memory or eyes?", ["A mirror", "A camera", "A pond", "A shadow"], "A mirror", "A mirror creates optical reflections without conscious sight."),
        "ur": ("وہ کون سی بے جان چیز ہے جو ہر سامنے آنے والی صورت ہو بہو دکھاتی ہے؟", ["آئینہ", "تصویر", "کتاب", "پردہ"], "آئینہ", "آئینہ روشنی کے انعکاس سے ہر چیز کا عکس صاف دکھاتا ہے۔")
    },
    # 18: Needle
    {
        "en": ("What has one eye, but cannot see anything?", ["A sewing needle", "A storm", "A potato", "A camera"], "A sewing needle", "The eye of a needle is the opening for threading."),
        "ur": ("وہ کیا ہے جس کی ایک آنکھ ہے مگر وہ دیکھ بالکل نہیں سکتی؟", ["سوئی", "طوفان", "آلو", "بٹن"], "سوئی", "سوئی کے سوراخ کو آنکھ (Eye) کہا جاتا ہے جس میں دھاگہ ڈالا جاتا ہے۔")
    },
    # 19: Postage stamp
    {
        "en": ("What travels around the entire world while remaining in one corner?", ["A postage stamp", "A compass", "A passport", "A suitcase"], "A postage stamp", "A stamp stays on the envelope's corner while traveling worldwide."),
        "ur": ("وہ کیا ہے جو ایک کونے میں چپکی رہتی ہے مگر پوری دنیا کا سفر کر لیتی ہے؟", ["ڈاک ٹکٹ", "پاسپورٹ", "قطب نما", "چٹھی"], "ڈاک ٹکٹ", "ڈاک ٹکٹ لفافے کے کونے پر چسپاں رہ کر دنیا بھر میں پہنچتی ہے۔")
    },
    # 20: Table
    {
        "en": ("What has four legs, but cannot walk a single step?", ["A table", "A horse", "A baby", "A chair"], "A table", "Tables have four wooden or metal legs for support, but cannot walk."),
        "ur": ("وہ کیا ہے جس کے چار پاؤں ہیں مگر وہ ایک قدم بھی چل نہیں سکتی؟", ["میز", "کرسی", "پلنگ", "جانور"], "میز", "میز کے چار پائے ہوتے ہیں جن پر وہ کھڑی رہتی ہے مگر چل نہیں سکتی۔")
    },
    # 21: River
    {
        "en": ("What has a bed but never sleeps, and runs without having legs?", ["A river", "A clock", "A car", "A breeze"], "A river", "A river has a riverbed and river mouth, and flows continuously."),
        "ur": ("وہ کیا ہے جس کا بستر ہے مگر سوتی نہیں، اور منہ ہے مگر بولتی نہیں؟", ["دریا (ندی)", "ہوا", "پہاڑ", "بادل"], "دریا (ندی)", "دریا کا پیندہ (Riverbed) کہلاتا ہے اور وہ مسلسل بہتا رہتا ہے۔")
    },
    # 22: Shadow
    {
        "en": ("What follows you in bright sunlight but disappears in total darkness?", ["Your shadow", "Your echo", "Your footprints", "Your coat"], "Your shadow", "A shadow requires light to be cast upon a surface."),
        "ur": ("وہ کیا ہے جو روشنی میں آپ کا ساتھ دیتی ہے مگر اندھیرا ہوتے ہی غائب ہو جاتی ہے؟", ["سایہ", "تصویر", "عینک", "آواز"], "سایہ", "سایہ بننے کے لیے روشنی کا وجود ضروری ہوتا ہے۔")
    },
    # 23: Fire
    {
        "en": ("Feed me and I live, but give me water and I die. What am I?", ["Fire", "A sponge", "A desert plant", "An engine"], "Fire", "Combustion consumes fuel and oxygen, but water extinguishes the flame."),
        "ur": ("وہ کیا ہے جسے لکڑی کھلاؤ تو جیتی ہے، مگر پانی پلاؤ تو مر جاتی ہے؟", ["آگ", "پودا", "ہوا", "مٹی"], "آگ", "آگ ایندھن پا کر بھڑکتی ہے لیکن پانی ڈالنے سے فورا بجھ جاتی ہے۔")
    },
    # 24: Fence
    {
        "en": ("What runs all the way around a backyard without ever moving?", ["A fence", "A dog", "A lawnmower", "A stream"], "A fence", "A perimeter fence encloses a yard while standing stationary."),
        "ur": ("وہ کیا ہے جو پورے باغ یا گھر کے گرد گھومتی ہے مگر خود اپنی جگہ سے نہیں ہلتی؟", ["باڑ (چاردیواری)", "سڑک", "ندی", "ہوا"], "باڑ (چاردیواری)", "چاردیواری پورے احاطے کا گھیراؤ کرتی ہے مگر ساکن رہتی ہے۔")
    },
    # 25: Piano
    {
        "en": ("What has black and white keys that cannot open any door locks?", ["A piano", "A keyboard", "A map", "A safe"], "A piano", "A piano has musical keys designed to produce acoustic notes."),
        "ur": ("وہ کیا ہے جس کے پاس درجنوں چابیاں ہیں مگر وہ کوئی تالا نہیں کھول سکتیں؟", ["پیانو", "کی بورڈ", "الماری", "نقشہ"], "پیانو", "پیانو کی کلیدیں (Keys) سریلی دھنیں پیدا کرنے کے لیے ہوتی ہیں۔")
    },
    # 26: Right elbow
    {
        "en": ("What can you hold comfortably in your left hand, but never in your right hand?", ["Your right elbow", "A coin", "A pencil", "A coffee cup"], "Your right elbow", "Your right hand cannot reach around to grasp its own right elbow."),
        "ur": ("وہ کون سا عضو ہے جسے آپ بائیں ہاتھ سے تو پکڑ سکتے ہیں مگر دائیں ہاتھ سے کبھی نہیں؟", ["دایاں کہنی", "بایاں ہاتھ", "ناک", "کان"], "دایاں کہنی", "دایاں ہاتھ اپنے ہی کہنی کو ہاتھ کے اندر پکڑ نہیں سکتا۔")
    },
    # 27: Mushroom
    {
        "en": ("What kind of room has no doors, walls, or windows to enter?", ["A mushroom", "A darkroom", "A attic", "A basement"], "A mushroom", "A mushroom is an umbrella-shaped fungus, not an architectural room."),
        "ur": ("وہ کون سا روم (کمرہ) ہے جس کے نہ دروازے ہوتے ہیں اور نہ کھڑکیاں؟", ["مشروم (کھمبی)", "ڈارک روم", "کلاس روم", "اسٹور روم"], "مشروم (کھمبی)", "کھمبی کو انگریزی میں مشروم کہتے ہیں جو کہ ایک نباتات ہے۔")
    },
    # 28: Flight of stairs
    {
        "en": ("What goes up and down continuously without moving an inch?", ["A flight of stairs", "An elevator", "A swing", "A ladder"], "A flight of stairs", "Stairs lead up and down between building levels while remaining stationary."),
        "ur": ("وہ کیا ہے جو اوپر بھی جاتی ہے اور نیچے بھی، مگر خود کبھی حرکت نہیں کرتی؟", ["سیڑھیاں", "لفٹ", "جھولا", "رسی"], "سیڑھیاں", "سیڑھیاں منزلوں کو جوڑتی ہیں مگر خود اپنی جگہ قائم رہتی ہیں۔")
    },
    # 29: Cloud
    {
        "en": ("What flies high without wings and cries without having eyes?", ["A cloud", "The wind", "Smoke", "An airplane"], "A cloud", "Clouds drift across the atmosphere and produce rainfall."),
        "ur": ("وہ کیا ہے جو بنا پروں کے اڑتا ہے اور بنا آنکھوں کے روتا ہے؟", ["بادل", "ہوا", "دھواں", "پتنگ"], "بادل", "بادل فضا میں تیرتے ہیں اور بارش برسا کر روتے ہوئے محسوس ہوتے ہیں۔")
    },
    # 30: Bar of soap
    {
        "en": ("What gets visibly smaller every time it takes a warm bath?", ["A bar of soap", "A sponge", "A towel", "An ice cube"], "A bar of soap", "Soap dissolves into lather as it is used to wash."),
        "ur": ("وہ کون سی چیز ہے جو جتنا زیادہ نہائے، اتنی ہی گھل کر چھوٹی ہوتی جاتی ہے؟", ["صابن", "اسفنج", "تولیہ", "برف"], "صابن", "صابن کو جتنا زیادہ استعمال کیا جائے وہ پگھل کر گھٹتا جاتا ہے۔")
    },
    # 31: Light
    {
        "en": ("What can fill an entire room completely without taking up any space?", ["Light", "Air", "Sound", "Furniture"], "Light", "Photons illuminate every corner of an interior without displacing volume."),
        "ur": ("وہ کیا ہے جو پورے کمرے کو بھر دیتی ہے مگر ذرا سی بھی جگہ نہیں گھیرتی؟", ["روشنی", "ہوا", "خوشبو", "آواز"], "روشنی", "بلب یا چراغ کی روشنی پورے کمرے کو روشن کرتی ہے بغیر جگہ گھیرے ہوئے۔")
    },
    # 32: Financial bank
    {
        "en": ("What has branches across towns, but no trunk, leaves, or fruit?", ["A bank", "A river", "A tree", "A railway"], "A bank", "Financial institutions have branch offices rather than plant foliage."),
        "ur": ("وہ کیا ہے جس کی شاخیں تو دور دور تک پھیلی ہیں مگر ان پر پتے یا پھل نہیں لگتے؟", ["بینک", "درخت", "ریل کی پٹری", "پہاڑ"], "بینک", "بینکوں کی برانچز کو اردو میں شاخیں کہا جاتا ہے جہاں مالیاتی کام ہوتا ہے۔")
    },
    # 33: Rubber band
    {
        "en": ("What kind of band stretches elastic tension but never plays musical songs?", ["A rubber band", "A rock band", "A jazz band", "A brass band"], "A rubber band", "An elastic rubber band secures loose items rather than playing melodies."),
        "ur": ("وہ کون سا بینڈ ہے جو کھنچتا تو خوب ہے مگر کبھی ساز یا موسیقی نہیں بجاتا؟", ["ربر بینڈ", "میوزیکل بینڈ", "آرمی بینڈ", "واچ بینڈ"], "ربر بینڈ", "ربر بینڈ چیزوں کو باندھنے کے لیے لچکدار ربڑ کی پٹی ہوتی ہے۔")
    },
    # 34: Library
    {
        "en": ("What building contains the highest number of stories in any city?", ["A public library", "A skyscraper", "A hospital", "A university"], "A public library", "Libraries house thousands of written fiction and historical storybooks."),
        "ur": ("شہر کی وہ کون سی عمارت ہے جس کے اندر سب سے زیادہ کہانیاں (منزلیں) پائی جاتی ہیں؟", ["لائبریری (کتب خانہ)", "بلند ٹاور", "ہسپتال", "شاپنگ مال"], "لائبریری (کتب خانہ)", "کتب خانے میں دنیا بھر کی ہزاروں داستانوں اور کہانیوں کی کتابیں ہوتی ہیں۔")
    },
    # 35: Letter M
    {
        "en": ("What comes once in a minute, twice in a moment, but never in a thousand years?", ["The letter M", "A leap second", "A solar flare", "A breath"], "The letter M", "The letter 'M' appears once in 'Minute', twice in 'Moment', and zero in 'Thousand years'."),
        "ur": ("لفظ 'موم بتی' کے شروع اور درمیان میں کیا آتا ہے مگر آخر میں نہیں؟", ["حرف میم", "روشنی", "دھواں", "آگ"], "حرف میم", "لفظ 'موم بتی' میں حرف 'م' دو بار آتا ہے۔")
    },
    # 36: Your name
    {
        "en": ("What belongs exclusively to you, yet other people use it far more often?", ["Your name", "Your phone", "Your car", "Your coat"], "Your name", "Your personal name is used by everyone whenever they speak to you."),
        "ur": ("وہ کون سی چیز ہے جو ہے تو آپ کی ذاتی، مگر دوسرے لوگ اسے آپ سے زیادہ پکارتے ہیں؟", ["آپ کا نام", "آپ کا موبائل", "آپ کے جوتے", "آپ کی گاڑی"], "آپ کا نام", "آپ کا نام دوسرے لوگ آپ کو مخاطب کرنے کے لیے بار بار استعمال کرتے ہیں۔")
    },
    # 37: The word Short
    {
        "en": ("Which English word becomes shorter when you append two letters to it?", ["Short", "Small", "Tiny", "Brief"], "Short", "Adding 'er' to 'Short' forms the comparative word 'Shorter'."),
        "ur": ("وہ کون سا لفظ ہے جس کے آگے مزید حروف لگائیں تو وہ 'مختصر' کا معنی دینے لگتا ہے؟", ["شارٹ (Short)", "بڑا", "لمبا", "گہرا"], "شارٹ (Short)", "انگریزی لفظ Short کے آگے er لگانے سے Shorter بن جاتا ہے۔")
    },
    # 38: A cold
    {
        "en": ("What can you easily catch on a winter day, but can never throw away with your hands?", ["A cold", "A snowball", "A baseball", "A frisbee"], "A cold", "You catch a respiratory cold virus, but cannot physically throw it."),
        "ur": ("وہ کیا ہے جو سردی کے موسم میں انسان کو آسانی سے لگ جاتی ہے مگر نظر نہیں آتی؟", ["ٹھنڈ (نزلہ)", "پتنگ", "برف", "دھند"], "ٹھنڈ (نزلہ)", "نزلہ و زکام انسان کو لگ جاتا ہے مگر اسے ہاتھوں سے پکڑا نہیں جا سکتا۔")
    },
    # 39: Artichoke
    {
        "en": ("What culinary vegetable has a heart that never beats?", ["An artichoke", "A cabbage", "A cucumber", "A radish"], "An artichoke", "The tender edible center core of an artichoke is called its heart."),
        "ur": ("وہ کون سی سبزی ہے جس کا دل تو ہوتا ہے مگر وہ دھڑکتا نہیں؟", ["آرٹیکوک (ہاتھی چک)", "گوبھی", "بینگن", "ٹماٹر"], "آرٹیکوک (ہاتھی چک)", "ہاتھی چک کا اندرونی نرم گودا دل کہلاتا ہے۔")
    },
    # 40: Silence
    {
        "en": ("What is so fragile that the mere whisper of its name breaks it instantly?", ["Silence", "A bubble", "Fine crystal", "A secret"], "Silence", "Uttering any vocalization disrupts quiet silence."),
        "ur": ("وہ کون سی شے ہے جو اتنی نازک ہے کہ اس کا نام پکارتے ہی وہ ٹوٹ جاتی ہے؟", ["خاموشی", "شیشہ", "بلبلہ", "شاخ"], "خاموشی", "زبان سے کوئی بھی لفظ ادا کرتے ہی خاموشی ختم ہو جاتی ہے۔")
    },
    # 41: Highway road
    {
        "en": ("What stretches across cities and climbs steep hills without taking a single step?", ["A paved highway", "A locomotive", "A cable car", "The wind"], "A paved highway", "Road networks span geographic distances while permanently anchored."),
        "ur": ("وہ کیا ہے جو میدانوں، پہاڑوں اور بستیوں سے گزرتی ہے مگر خود ساکن رہتی ہے؟", ["سڑک", "ریل گاڑی", "دریا", "طوفان"], "سڑک", "سڑکیں شہروں کو آپس میں جوڑتی ہیں مگر خود ایک انچ نہیں ہلتیں۔")
    },
    # 42: Eye of hurricane
    {
        "en": ("What meteorological storm has a calm eye in its center, but cannot see?", ["A hurricane", "A blizzard", "A thunderstorm", "A sandstorm"], "A hurricane", "The low-pressure vortex center of a tropical cyclone is called its eye."),
        "ur": ("وہ کون سا شدید سمندری طوفان ہے جس کے عین وسط میں پرسکون 'آنکھ' ہوتی ہے؟", ["سمندری طوفان (ہریکین)", "برفانی طوفان", "جھکڑ", "زلزلہ"], "سمندری طوفان (ہریکین)", "طوفان کے درمیانی دائرے کو سائنسی زبان میں طوفان کی آنکھ کہتے ہیں۔")
    },
    # 43: Wet paint
    {
        "en": ("What kind of protective coat is applied wet so it dries properly?", ["A coat of paint", "A raincoat", "A fur coat", "A trenchcoat"], "A coat of paint", "Liquid paint is brushed on wet to form a smooth protective film."),
        "ur": ("وہ کون سا کوٹ ہے جو گیلا کر کے ہی دیوار یا لکڑی پر چڑھایا جاتا ہے؟", ["رنگ کا کوٹ (پینٹ)", "اوور کوٹ", "واٹر پروف کوٹ", "چمڑے کا کوٹ"], "رنگ کا کوٹ (پینٹ)", "دیواروں پر رنگ روغن کی تہہ کو پینٹ کا کوٹ کہا جاتا ہے۔")
    },
    # 44: Grand piano
    {
        "en": ("What musical instrument contains eighty-eight keys, yet cannot unlock any door?", ["A piano", "An accordion", "A harp", "A harpsichord"], "A piano", "A modern acoustic piano has 52 white and 36 black keys."),
        "ur": ("وہ کون سا ساز ہے جس کے اندر 88 کلیدیں ہیں مگر وہ کسی صندوق کو نہیں کھول سکتیں؟", ["پیانو", "بانسری", "ستار", "طبلہ"], "پیانو", "پیانو کے کی بورڈ پر کل 88 سیاہ و سفید کلیدیں ہوتی ہیں۔")
    },
    # 45: Tree bark
    {
        "en": ("What natural object has tough outer bark, but has no teeth to bite?", ["A tree", "A seal", "A dog", "A beaver"], "A tree", "The fibrous protective outer layer of a tree trunk is called bark."),
        "ur": ("وہ کیا ہے جس کے تنے پر موٹی چھال تو ہوتی ہے مگر وہ کسی کو کاٹ نہیں سکتا؟", ["درخت", "کتا", "شیر", "مگرمچھ"], "درخت", "درخت کا بیرونی حفاظتی خول چھال کہلاتا ہے۔")
    },
    # 46: Hummingbird
    {
        "en": ("Which tiny bird can hover in mid-air and fly completely backwards?", ["A hummingbird", "A sparrow", "A swallow", "A kingfisher"], "A hummingbird", "Hummingbirds possess specialized ball joints enabling omnidirectional flight."),
        "ur": ("وہ کون سا ننھا پرندہ ہے جو فضا میں ایک جگہ ساکن رہ سکتا ہے اور الٹا بھی اڑ سکتا ہے؟", ["شکر خورہ (ہمِنگ برڈ)", "چڑیا", "کبوتر", "باز"], "شکر خورہ (ہمِنگ برڈ)", "ہمِنگ برڈ کے پروں کی منفرد ساخت اسے الٹا اڑنے کی صلاحیت بخشتی ہے۔")
    },
    # 47: Bat
    {
        "en": ("Which nocturnal mammal flies through dark skies using ultrasonic echolocation?", ["A bat", "A flying squirrel", "An owl", "A moth"], "A bat", "Bats are the sole mammals capable of true powered aerodynamic flight."),
        "ur": ("وہ کون سا پرندہ نما ممالیہ جانور ہے جو رات کے اندھیرے میں الٹرا سونک آوازوں سے راستہ تلاش کرتا ہے؟", ["چمگادڑ", "الو", "فاختہ", "چیل"], "چمگادڑ", "چمگادڑ اڑنے والا ممالیہ جانور ہے جو ایکو لوکیشن سے اڑتا ہے۔")
    },
    # 48: Octopus
    {
        "en": ("Which marine animal possesses three distinct hearts and blue blood?", ["An octopus", "A dolphin", "A seal", "A sea turtle"], "An octopus", "An octopus utilizes copper-rich hemocyanin to carry oxygen through blue blood."),
        "ur": ("وہ کون سا سمندری جاندار ہے جس کے تین دل اور نیلا خون ہوتا ہے؟", ["آکٹوپس", "ڈولفن", "وہیل", "کچھوا"], "آکٹوپس", "آکٹوپس کے جسم میں خون کی گردش کے لیے تین دل قدرت نے بنائے ہیں۔")
    },
    # 49: Desert snail
    {
        "en": ("Which creature can seal its shell and sleep for up to three years during drought?", ["A desert snail", "A brown bear", "A tortoise", "A bullfrog"], "A desert snail", "Snails can estivate for extended years until rainfall returns."),
        "ur": ("وہ کون سا جاندار ہے جو قحط سالی کے دوران اپنے خول میں مسلسل تین سال تک سو سکتا ہے؟", ["صحرائی گھونگھا (سنیل)", "ریچھ", "کچھوا", "مینڈک"], "صحرائی گھونگھا (سنیل)", "گھونگھا شدید خشکی میں اپنے خول کو بند کر کے طویل نیند سو جاتا ہے۔")
    },
    # 50: Mantis shrimp
    {
        "en": ("Which sea creature has sixteen photoreceptor color cones detecting polarized light?", ["A mantis shrimp", "A goldfish", "A crab", "A lobster"], "A mantis shrimp", "Mantis shrimp have the most complex compound optical systems known in biology."),
        "ur": ("وہ کون سا سمندری کیکڑا نما جاندار ہے جس کی آنکھیں 16 رنگین کونز کے ساتھ الٹرا وائلٹ دیکھ سکتی ہیں؟", ["مینٹس شرمپ", "گولڈ فش", "اسٹار فش", "جھینگا"], "مینٹس شرمپ", "مینٹس شرمپ کی آنکھیں حیاتیات کے پیچیدہ ترین بصری نظام کی حامل ہیں۔")
    },
    # 51: Bullfrog
    {
        "en": ("Which amphibian exhibits identical brain responsiveness whether awake or resting?", ["A bullfrog", "A toad", "A newt", "A salamander"], "A bullfrog", "Bullfrogs do not experience typical slow-wave neurological sleep cycles."),
        "ur": ("وہ کون سا ایمفیبیئن جاندار ہے جس کا دماغ آرام کی حالت میں بھی مکمل بیدار رہتا ہے؟", ["بل فراگ (مینڈک)", "نیوٹ", "چھپکلی", "گرگٹ"], "بل فراگ (مینڈک)", "بل فراگ کی چوکسی سوتے اور جاگتے وقت ایک جیسی رہتی ہے۔")
    },
    # 52: Kiwi
    {
        "en": ("Which flightless bird lays an egg that accounts for twenty percent of its body weight?", ["A kiwi", "An ostrich", "A penguin", "An emu"], "A kiwi", "New Zealand's kiwi produces an egg proportionally larger than almost any bird."),
        "ur": ("وہ کون سا پرندہ ہے جس کا انڈا اس کے اپنے جسمانی وزن کے 20 فیصد کے برابر ہوتا ہے؟", ["کیوی پرندہ", "شتر مرغ", "پینگوئن", "فاختہ"], "کیوی پرندہ", "نیوزی لینڈ کا کیوی اپنے جسم کے تناسب سے دنیا کا سب سے بڑا انڈا دیتا ہے۔")
    },
    # 53: Cockroach
    {
        "en": ("Which resilient insect can survive for weeks without its head because it breathes through spiracles?", ["A cockroach", "An ant", "A beetle", "A termite"], "A cockroach", "Cockroaches have open circulatory systems and breathe through abdominal pores."),
        "ur": ("وہ کون سا حشرات الارض ہے جو سر کٹنے کے بعد بھی ہفتوں تک زندہ رہ سکتا ہے کیونکہ وہ پیٹ سے سانس لیتا ہے؟", ["کاکروچ (لال بیگ)", "چیونٹی", "ٹڈی", "بھنورا"], "کاکروچ (لال بیگ)", "لال بیگ اپنے جسم کے مساموں سے سانس لیتا ہے اس لیے سر کے بغیر بھی زندہ رہتا ہے۔")
    },
    # 54: Wombat
    {
        "en": ("Which Australian marsupial produces cube-shaped droppings to mark territory?", ["A wombat", "A koala", "A kangaroo", "A platypus"], "A wombat", "Wombat intestines have varying tissue stiffness, producing distinct cubic scat."),
        "ur": ("وہ کون سا آسٹریلوی جانور ہے جس کا فضلا چوکور (مربع نما) ہوتا ہے تاکہ وہ لڑھک نہ سکے؟", ["وومبیٹ", "کوالا", "کنگرو", "ڈِنگو"], "وومبیٹ", "وومبیٹ کی آنتوں کی مخصوص ساخت کی وجہ سے اس کا فضلا مربع کیوب جیسا بنتا ہے۔")
    },
    # 55: Shark immunity
    {
        "en": ("Which apex marine predator possesses cartilage tissues showing extraordinary resistance to illnesses?", ["A shark", "A killer whale", "A barracuda", "A moray eel"], "A shark", "Sharks have unique immune compounds and highly stable genome repair genes."),
        "ur": ("وہ کون سا شکاری سمندری جاندار ہے جس کا مدافعتی نظام بیماریوں کے خلاف بے پناہ مزاحمت رکھتا ہے؟", ["شارک مچھلی", "وہیل", "سیل", "ٹونا"], "شارک مچھلی", "شارک کے جسم میں ہڈیوں کی جگہ لچکدار کارٹلیج اور طاقتور اینٹی باڈیز ہوتی ہیں۔")
    },
    # 56: Ostrich eyes
    {
        "en": ("Which large bird has eyeballs that are physically larger in volume than its brain?", ["An ostrich", "An eagle", "An owl", "A vulture"], "An ostrich", "An ostrich has two-inch eyes that each weigh more than its forty-gram brain."),
        "ur": ("وہ کون سا بڑا پرندہ ہے جس کی آنکھیں اس کے اپنے دماغ سے بھی زیادہ بڑی اور وزنی ہوتی ہیں؟", ["شتر مرغ", "عقاب", "الو", "باز"], "شتر مرغ", "شتر مرغ کی دونوں آنکھیں اس کے پورے دماغ کے حجم سے بڑی ہوتی ہیں۔")
    },
    # 57: Duck-billed platypus
    {
        "en": ("Which semi-aquatic Australian mammal lays leathery eggs instead of giving live birth?", ["A platypus", "An echidna", "A beaver", "An otter"], "A platypus", "Monotremes like the platypus are primitive mammals that produce eggs."),
        "ur": ("وہ کون سا بطخ جیسی چونچ والا ممالیہ جاندار ہے جو بچے جننے کے بجائے انڈے دیتا ہے؟", ["پلیٹی پس", "اوٹر", "سیل", "کنگرو"], "پلیٹی پس", "پلیٹی پس ان معدودے چند ممالیہ میں سے ہے جو انڈے دیتے ہیں۔")
    },
    # 58: Koala fingerprints
    {
        "en": ("Which tree-climbing mammal has epidermal fingerprint ridges that closely match human prints?", ["A koala", "A chimpanzee", "A lemur", "A sloth"], "A koala", "Koala friction ridges cannot be easily distinguished from humans under a microscope."),
        "ur": ("وہ کون سا جانور ہے جس کی انگلیوں کے نشانات (فنگر پرنٹس) انسانی نشانات سے ہو بہو ملتے ہیں؟", ["کوالا", "بندر", "ریچھ", "بلی"], "کوالا", "کوالا کے ہاتھ کی انگلیوں کے خطوط مائیکرو اسکوپ میں انسان جیسے دکھتے ہیں۔")
    },
    # 59: Jellyfish
    {
        "en": ("Which gelatinous sea creature thrives with ninety-five percent water and no centralized brain?", ["A jellyfish", "A sea anemone", "A sea urchin", "A coral"], "A jellyfish", "Jellyfish coordinate muscle contractions via a radial nerve ring rather than a brain."),
        "ur": ("وہ کون سا سمندری جاندار ہے جس کے جسم میں ہڈی، دل اور مرکزی دماغ نہیں ہوتا اور وہ 95 فیصد پانی ہے؟", ["جیلی فش", "اسٹار فش", "کیکڑا", "جھینگا"], "جیلی فش", "جیلی فش بغیر دماغ کے صرف اعصابی جال کے ذریعے پانی میں تیرتی ہے۔")
    },
    # 60: Giraffe
    {
        "en": ("Which tall savanna mammal has the highest resting blood pressure to pump blood to its elevated head?", ["A giraffe", "An elephant", "A camel", "A rhinoceros"], "A giraffe", "A giraffe requires roughly double human systolic pressure to supply blood six feet up."),
        "ur": ("زمین کا وہ کون سا بلند قامت جانور ہے جس کا بلڈ پریشر سب سے زیادہ ہوتا ہے تاکہ خون سر تک پہنچے؟", ["زرافہ", "ہاتھی", "اونٹ", "گینڈا"], "زرافہ", "زرافے کا دل 6 فٹ اوپر سر تک خون پمپ کرنے کے لیے بے پناہ دباؤ بناتا ہے۔")
    },
    # 61: Frog skin
    {
        "en": ("Which common amphibian drinks water directly by absorbing it through an abdominal skin patch?", ["A frog", "A lizard", "A gecko", "A salamander"], "A frog", "Frogs rarely swallow drinking water; they absorb hydration cutaneously."),
        "ur": ("وہ کون سا مینڈک ہے جو منہ سے پانی پینے کے بجائے اپنی پیٹ کی جلد سے نمی جذب کرتا ہے؟", ["مینڈک", "سانپ", "چھپکلی", "گرگٹ"], "مینڈک", "مینڈک کی پتلی جلد پانی کو سیدھا اپنے اندر جذب کرنے کی صلاحیت رکھتی ہے۔")
    },
    # 62: Lyrebird
    {
        "en": ("Which Australian forest songbird is famous for flawlessly imitating chainsaws, car alarms, and camera shutters?", ["A lyrebird", "A parrot", "A cockatoo", "A raven"], "A lyrebird", "The superb lyrebird possesses the most acoustically complex avian syrinx in nature."),
        "ur": ("وہ کون سا جنگلی پرندہ ہے جو آری چلنے، کیمرے کے کلک اور گاڑی کے الارم کی ہو بہو نقالی کرتا ہے؟", ["لائر برڈ (Lyrebird)", "طوطا", "مینا", "کوئل"], "لائر برڈ (Lyrebird)", "لائر برڈ جنگل میں سنی گئی کسی بھی مشینی آواز کی حیران کن نقل کر سکتا ہے۔")
    },
    # 63: Chiton
    {
        "en": ("Which marine mollusk grazes on intertidal rocks with teeth tipped in magnetic iron ore?", ["A chiton", "A limpet", "A barnacle", "A sea slug"], "A chiton", "Chiton radula teeth synthesize biomineralized magnetite crystals to scrape hard granite."),
        "ur": ("وہ کون سا سمندری سیپ دار کیڑا ہے جس کے دانت لوہے کے قدرتی معدن (میگنیٹائٹ) سے بنے ہوتے ہیں؟", ["چائیٹن (Chiton)", "گھونگھا", "کیکڑا", "سیپی"], "چائیٹن (Chiton)", "چائیٹن پتھروں سے کائی کھرچنے کے لیے فولادی مضبوطی کے دانت استعمال کرتا ہے۔")
    },
    # 64: Sea otters
    {
        "en": ("Which playful marine mammal rafts in kelp beds and holds paws while sleeping to prevent drifting away?", ["A sea otter", "A seal", "A sea lion", "A manatee"], "A sea otter", "Sea otters interlock paws while napping on their backs in ocean swells."),
        "ur": ("وہ کون سا سمندری جانور ہے جو پانی میں سوتے ہوئے ایک دوسرے کا ہاتھ تھام لیتا ہے تاکہ بہہ نہ جائے؟", ["سمندری اود بلاؤ (سی اوٹر)", "سیل", "والرس", "ڈولفن"], "سمندری اود بلاؤ (سی اوٹر)", "سی اوٹر سوتے ہوئے اپنے ساتھیوں کے پنجے پکڑ کر پانی پر تیرتے رہتے ہیں۔")
    },
    # 65: Honeybee eyes
    {
        "en": ("Which industrious pollinating insect possesses five eyes: two large compound eyes and three dorsal ocelli?", ["A honeybee", "A dragonfly", "A housefly", "A butterfly"], "A honeybee", "Bees use their two compound eyes for image analysis and three top ocelli for celestial solar heading."),
        "ur": ("شہد کی مکھی کے سر پر کل کتنی آنکھیں ہوتی ہیں جو اسے سورج کی سمت تلاش کرنے میں مدد دیتی ہیں؟", ["پانچ آنکھیں", "دو آنکھیں", "چار آنکھیں", "چھ آنکھیں"], "پانچ آنکھیں", "شہد کی مکھی کی دو بڑی مرکب آنکھیں اور تین چھوٹی سادہ آنکھیں ہوتی ہیں۔")
    },
    # 66: Metal vs wooden spoon
    {
        "en": ("Why does an ice-cold metal spoon feel much colder to touch than a dry wooden spoon at the exact same temperature?", ["Metal conducts body heat away rapidly", "Wood produces internal heat", "Metal creates frost", "Wood absorbs coldness"], "Metal conducts body heat away rapidly", "Metals possess high thermal conductivity, transferring kinetic heat away from nerve endings rapidly."),
        "ur": ("ایک ہی کمرے کے درجہ حرارت پر رکھی لوہے کی چمچ لکڑی کی چمچ سے زیادہ ٹھنڈی کیوں محسوس ہوتی ہے؟", ["لوہا جسم سے حرارت تیزی سے جذب کرتا ہے", "لکڑی میں خود حرارت ہوتی ہے", "لوہا ٹھنڈک پیدا کرتا ہے", "لکڑی میں رگڑ ہوتی ہے"], "لوہا جسم سے حرارت تیزی سے جذب کرتا ہے", "دھاتوں میں حرارتی ایصال (کنڈکشن) بہت تیز ہوتی ہے جس سے انگلی کی حرارت فوراً کھنچ جاتی ہے۔")
    },
    # 67: White color reflection
    {
        "en": ("Which surface coloration reflects the highest percentage of incident ambient sunlight back into space?", ["White", "Yellow", "Sky blue", "Silver"], "White", "Pure white surfaces reflect nearly all visible wavelengths, giving them high albedo."),
        "ur": ("کون سا رنگ سورج کی روشنی کی تمام لہروں کو سب سے زیادہ واپس منعکس (Reflect) کرتا ہے؟", ["سفید", "پیلا", "نیلا", "سبز"], "سفید", "سفید رنگ تمام رنگوں کی روشنی کو منعکس کر کے کم سے کم گرمی جذب کرتا ہے۔")
    },
    # 68: Photosynthesis gas
    {
        "en": ("Which atmospheric gas do terrestrial green plants consume during daytime photosynthesis to synthesize sugars?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Methane"], "Carbon dioxide", "Chloroplasts capture photons to combine carbon dioxide and water into glucose."),
        "ur": ("دن کے وقت پودے ضیائی تالیف (فوٹو سنتھیسز) کے دوران ہوا سے کون سی گیس جذب کرتے ہیں؟", ["کاربن ڈائی آکسائیڈ", "آکسیجن", "نائٹروجن", "ہائیڈروجن"], "کاربن ڈائی آکسائیڈ", "پودے کاربن ڈائی آکسائیڈ لے کر خوراک بناتے ہیں اور آکسیجن خارج کرتے ہیں۔")
    },
    # 69: Anvil vs tennis ball in air
    {
        "en": ("When dropped simultaneously from a tall balcony in atmospheric air, why does a dense iron anvil reach the turf before a tennis ball?", ["Air resistance has less retarding effect on the heavy anvil", "Gravity pulls heavier objects with higher acceleration", "The tennis ball becomes lighter", "The anvil generates wind"], "Air resistance has less retarding effect on the heavy anvil", "Both experience identical gravitational acceleration, but aerodynamic drag slows low-density tennis balls far more."),
        "ur": ("کھلی ہوا میں ایک بھاری لوہے کا باٹ اور گیند ایک ساتھ گرائیں تو باٹ پہلے کیوں گرتا ہے؟", ["ہوا کی مزاحمت ہلکی گیند کو زیادہ روکتی ہے", "کشش ثقل بھاری چیز پر تیز ہوتی ہے", "گیند ہوا میں اڑنے لگتی ہے", "لوہا زمین کو کھینچتا ہے"], "ہوا کی مزاحمت ہلکی گیند کو زیادہ روکتی ہے", "خلا میں دونوں برابر گرتے ہیں لیکن ہوا کی رگڑ ہلکی چیز کی رفتار کو کم کر دیتی ہے۔")
    },
    # 70: Ice expansion
    {
        "en": ("What unique property causes solid water ice cubes to float atop liquid water in a drinking cup?", ["Water expands upon freezing, reducing its solid density", "Ice absorbs air bubbles", "Liquid water is boiling", "Ice has negative weight"], "Water expands upon freezing, reducing its solid density", "Liquid water reaches peak density at 4°C; crystal lattice formation widens molecular bonds into an open structure."),
        "ur": ("برف پانی کے گلاس میں ڈوبنے کے بجائے اوپر کیوں تیرتی رہتی ہے؟", ["پانی جمنے پر پھیلتا ہے اور اس کی کثافت کم ہو جاتی ہے", "برف میں ہوا بھر جاتی ہے", "برف کا وزن ختم ہو جاتا ہے", "پانی برف کو اوپر پھینکتا ہے"], "پانی جمنے پر پھیلتا ہے اور اس کی کثافت کم ہو جاتی ہے", "پانی جم کر برف بنتے ہوئے پھیلتا ہے جس سے اس کا وزن مائع پانی سے ہلکا ہو جاتا ہے۔")
    },
    # 71: Human brain energy
    {
        "en": ("Which vital cranial organ accounts for roughly two percent of adult body weight but burns twenty percent of resting glucose?", ["The brain", "The heart", "The liver", "The pancreas"], "The brain", "Human brain synaptic ion pumping requires immense continuous metabolic glucose consumption."),
        "ur": ("انسانی جسم کا وہ کون سا عضو ہے جو وزن میں صرف 2 فیصد ہے مگر 20 فیصد توانائی استعمال کرتا ہے؟", ["دماغ", "دل", "جگر", "پھیپھڑے"], "دماغ", "انسانی دماغ اربوں نیورونز کے سگنلز چلانے کے لیے جسم کی بیس فیصد توانائی خرچ کرتا ہے۔")
    },
    # 72: Blood platelets
    {
        "en": ("Which specialized cellular component of circulating human blood aggregates to form clotting plugs over vascular punctures?", ["Platelets", "Red blood cells", "White blood cells", "Plasma globulins"], "Platelets", "Thrombocytes trigger fibrin mesh cascades that seal capillary bleeds quickly."),
        "ur": ("خون کا وہ کون سا اہم جزو ہے جو زخم لگنے پر خون کو جما کر بہنے سے روکتا ہے؟", ["پلیٹ لیٹس (خلیات خون)", "سرخ خلیات", "سفید خلیات", "پلازما"], "پلیٹ لیٹس (خلیات خون)", "پلیٹ لیٹس زخم کی جگہ پر اکٹھے ہو کر جال بنا دیتے ہیں جس سے خون رک جاتا ہے۔")
    },
    # 73: Sunlight in space
    {
        "en": ("What apparent visual color does our Sun exhibit when photographed directly by astronauts in outer orbit without atmospheric haze?", ["Pure white", "Golden yellow", "Pale orange", "Bright cyan"], "Pure white", "The solar photosphere emits a continuous blackbody spectrum spanning all visible wavelengths equally."),
        "ur": ("زمین کی فضا سے باہر خلا میں دیکھنے پر سورج کا اصل رنگ کیسا دکھائی دیتا ہے؟", ["بالکل سفید", "چمکدار پیلا", "سرخ", "سنہری"], "بالکل سفید", "فضا کی غیر موجودگی میں سورج کی تمام رنگین لہریں مل کر خالص سفید نظر آتی ہیں۔")
    },
    # 74: Lemon juice pH
    {
        "en": ("Which acidic citrus beverage contains natural citric acid resulting in a measured pH value near 2.0?", ["Lemon juice", "Tomato paste", "Black coffee", "Cow milk"], "Lemon juice", "High citric acid hydrogen ion concentration gives fresh lemon juice a strong acidic rating."),
        "ur": ("کچن میں استعمال ہونے والا لیموں کا رس اپنی تیزابیت (pH) کے لحاظ سے کیسا ہوتا ہے؟", ["شدید تیزابی (pH تقریباً 2)", "نیوٹرل (pH 7)", "الکلائن (اساسی)", "ہلکا نمکین"], "شدید تیزابی (pH تقریباً 2)", "سٹرک ایسڈ کی وافر مقدار کی وجہ سے لیموں کا رس سخت تیزابی ہوتا ہے۔")
    },
    # 75: Mohs hardness 10
    {
        "en": ("Which crystalline allotrope of carbon achieves the highest ten rating on Friedrich Mohs mineral hardness scale?", ["Diamond", "Corundum", "Topaz", "Quartz"], "Diamond", "Dense sp3 tetrahedral covalent carbon lattice bonds make natural diamond impervious to scratching by other stones."),
        "ur": ("موہس کے معدنی سختی کے پیمانے پر 10 کی سب سے بلند ترین سختی کس پتھر کو حاصل ہے؟", ["ہیرا", "یاقوت", "زمرد", "عقیق"], "ہیرا", "ہیرے کے کاربن ایٹمز کی انتہائی مضبوط بانڈنگ کی وجہ سے وہ دنیا کا سخت ترین قدرتی مادہ ہے۔")
    },
    # 76: Summer power lines sag
    {
        "en": ("Why do high-voltage electrical grid aluminum transmission cables sag noticeably lower in July than in January?", ["Thermal expansion of the conductor metals", "Heavier wind pressure in summer", "Increased electrical resistance", "Accumulated dust layers"], "Thermal expansion of the conductor metals", "Heat causes metallic atoms to vibrate with higher amplitude, linearly elongating the cable span."),
        "ur": ("سخت گرمیوں میں بجلی کے کھمبوں پر بندھی موٹی تاریں نیچے کی طرف کیوں لٹک جاتی ہیں؟", ["گرمی سے دھاتوں کا پھیلاؤ (تھرمل ایکسپینشن)", "بجلی کا بہاؤ زیادہ ہونا", "پرندوں کا وزن", "ہوا کا دباؤ"], "گرمی سے دھاتوں کا پھیلاؤ (تھرمل ایکسپینشن)", "گرمی کی شدت سے تاروں کی دھات پھیل کر لمبی ہو جاتی ہے جس سے وہ لٹک جاتی ہیں۔")
    },
    # 77: Liquid mercury
    {
        "en": ("Which heavy chemical metal with elemental symbol Hg exists as a dense silvery liquid at standard room conditions?", ["Mercury", "Gallium", "Bromine", "Cesium"], "Mercury", "Relativistic 6s electron orbital contraction weakens interatomic metallic bonding in room temperature mercury."),
        "ur": ("وہ کون سی واحد دھات ہے جو کمرے کے عام درجہ حرارت پر ٹھوس ہونے کے بجائے مائع حالت میں رہتی ہے؟", ["پارہ (مرکری)", "سیسہ", "تانبا", "جست"], "پارہ (مرکری)", "پارے کے ایٹمی مداروں کی خاص ساخت کی وجہ سے وہ عام درجہ حرارت پر مائع رہتا ہے۔")
    },
    # 78: Heart chambers
    {
        "en": ("How many interior pumping chambers comprise the muscular organ of a normal human cardiovascular heart?", ["Four chambers", "Two chambers", "Three chambers", "Six chambers"], "Four chambers", "The mammal heart contains right atrium, right ventricle, left atrium, and left ventricle chambers."),
        "ur": ("ایک عام صحت مند انسانی دل کے اندر خون کی گردش کے لیے کل کتنے خانے (چیمبرز) ہوتے ہیں؟", ["چار خانے", "دو خانے", "تین خانے", "پانچ خانے"], "چار خانے", "انسانی دل دائیں اور بائیں دو ایٹریم اور دو وینٹریکل پر مشتمل چار خانوں والا عضو ہے۔")
    },
    # 79: Enamel hardness
    {
        "en": ("What hydroxyapatite biological substance covering the crowns of your teeth is the hardest mineral in human anatomy?", ["Tooth enamel", "Femur cortical bone", "Fingernail keratin", "Cartilage"], "Tooth enamel", "Crystalline calcium phosphate prism rods make outer dental enamel harder than skeletal bones."),
        "ur": ("انسانی جسم کی ساخت میں ہڈیوں سے بھی زیادہ سخت اور مضبوط مادہ کون سا ہے؟", ["دانتوں کا اینیمل (بیرونی خول)", "ران کی ہڈی", "ناخن کی کیراٹن", "کھوپڑی کی ہڈی"], "دانتوں کا اینیمل (بیرونی خول)", "دانتوں کی حفاظتی چمکدار تہہ (اینیمل) انسانی جسم کا سخت ترین معدنی مادہ ہے۔")
    },
    # 80: Camel hump
    {
        "en": ("What concentrated nutritional tissue is stored within a dromedary camel's prominent dorsal hump?", ["Dense fat tissue", "Water reserves", "Digestive bile", "Muscle fiber"], "Dense fat tissue", "Camels store up to 80 pounds of adipose lipid fat to metabolize calories and water when desert forage is dry."),
        "ur": ("صحرائی اونٹ کے کوہان میں قدرت نے اصل میں کیا چیز ذخیرہ کر رکھی ہوتی ہے؟", ["چکنائی (فیٹ)", "پانی کا ذخیرہ", "خون", "ہوا"], "چکنائی (فیٹ)", "کوہان میں اونٹ چکنائی جمع رکھتا ہے جو بھوک اور پیاس میں پگھل کر توانائی دیتی ہے۔")
    },
    # 81: Kangaroo forward hops
    {
        "en": ("Which anatomical leg tendon configuration prevents an Australian red kangaroo from walking backwards?", ["Large muscular hind legs and tail balance", "Short front paws", "Heavy bone structure", "Wide pouch angle"], "Large muscular hind legs and tail balance", "Kangaroos possess long elastic Achilles tendons and a tripod tail tailored exclusively for forward pentapedal hops."),
        "ur": ("کنگرو اپنی ٹانگوں اور دم کی مخصوص ساخت کی وجہ سے کون سی حرکت بالکل نہیں کر سکتا؟", ["پیچھے کی طرف چلنا", "اونچی چھلانگ لگانا", "تیز دوڑنا", "پانی میں تیرنا"], "پیچھے کی طرف چلنا", "کنگرو کی لمبی پچھلی ٹانگیں اور بھاری دم اسے پیچھے ہٹنے کی اجازت نہیں دیتیں۔")
    },
    # 82: Polar bear skin
    {
        "en": ("What pigment color lies directly beneath the dense translucent hollow fur coats of Arctic polar bears?", ["Jet black skin", "Pure white skin", "Pale pink skin", "Silver gray skin"], "Jet black skin", "Black dermal skin maximizes absorption of solar heat conducted through clear hollow light-trapping guard hairs."),
        "ur": ("برفانی قطبی ریچھ کی سفید کھال کے نیچے اس کی اصل جلد (چمڑی) کس رنگ کی ہوتی ہے؟", ["سیاہ (کالی)", "سفید", "گلابی", "نیلی"], "سیاہ (کالی)", "ریچھ کے بال شفاف ہوتے ہیں اور اس کی کالی جلد سورج کی تپش کو مکمل جذب کرتی ہے۔")
    },
    # 83: Beaver dam teeth
    {
        "en": ("Why are a forest beaver's continuously growing chisel incisor teeth coated in a bright orange enamel?", ["Iron compounds reinforce tooth strength", "Carrot pigment stains", "Bacterial plaque biofilm", "Pine sap resin"], "Iron compounds reinforce tooth strength", "Incorporating iron ions into dental enamel prevents brittle chipping when felling hardwoods."),
        "ur": ("درخت کاٹنے والے بیور (اود بلاؤ) کے آگے کے تیز دانت نارنجی رنگ کے کیوں ہوتے ہیں؟", ["دانتوں میں آئرن (لوہے) کے مرکبات ہوتے ہیں", "درخت کا رس لگنے سے", "گاجر کھانے سے", "بیماری کی وجہ سے"], "دانتوں میں آئرن (لوہے) کے مرکبات ہوتے ہیں", "لوہے کے قدرتی اجزا بیور کے دانتوں کو لکڑی کاٹنے کے لیے کلہاڑی کی طرح مضبوط بناتے ہیں۔")
    },
    # 84: Chameleon camouflage
    {
        "en": ("How does an arboreal chameleon rapidly alter its vibrant skin color patterns?", ["Nanocrystals in dermal iridophores shift lattice spacing", "Liquid blood flows to skin", "Pigment dyes sweat outward", "Hairs reflect daylight"], "Nanocrystals in dermal iridophores shift lattice spacing", "Guanine photonic nanocrystals tune constructive interference wavelengths of reflected environmental light."),
        "ur": ("گرگٹ اپنی جلد کا رنگ ماحول کے مطابق اتنی تیزی سے کیسے بدل لیتا ہے؟", ["جلد کے اندر مائیکرو کرسٹلز کا زاویہ بدلنے سے", "خون کا رنگ بدلنے سے", "رنگین پسینہ خارج کرنے سے", "جلد کے بال گرنے سے"], "جلد کے اندر مائیکرو کرسٹلز کا زاویہ بدلنے سے", "گرگٹ کے خلیوں میں نینو کرسٹلز روشنی کی شعاعوں کو موڑ کر مختلف رنگ پیدا کرتے ہیں۔")
    },
    # 85: Owl silent flight
    {
        "en": ("What unique feather adaptation allows predatory barn owls to glide over prey in near-total acoustic silence?", ["Serrated leading feather fringes that break up turbulent air", "Thick feather oil", "Heavy downy wings", "Narrow wing cords"], "Serrated leading feather fringes that break up turbulent air", "Comb-like serrations on primary wing feathers dissipate micro-turbulent air vortexes, silencing wing flap noise."),
        "ur": ("الو شکار کرتے وقت رات کو ہوا میں اڑتے ہوئے بالکل خاموش پرواز کیسے کرتا ہے؟", ["پروں کے کناروں پر لگی باریک جھالر سے ہوا کی آواز دب جاتی ہے", "وہ پر نہیں ہلاتا", "اس کے پر گیلے ہوتے ہیں", "پروں پر تیل لگا ہوتا ہے"], "پروں کے کناروں پر لگی باریک جھالر سے ہوا کی آواز دب جاتی ہے", "الو کے پروں پر باریک دندانے ہوا کے دباؤ کو توڑ کر پھڑپھڑاہٹ کی آواز ختم کر دیتے ہیں۔")
    },
    # 86: Cheetah speed endurance
    {
        "en": ("Why can an African cheetah sustain its blisteringly fast sprint of 60 mph for only twenty to thirty seconds?", ["Rapid core muscle thermal overheating", "Lack of lung capacity", "Low heart rate", "Weak tendon springs"], "Rapid core muscle thermal overheating", "Massive anaerobic metabolic expenditure raises body temperature above 105°F, necessitating an abrupt cool-down stop."),
        "ur": ("چیتا 100 کلومیٹر فی گھنٹہ کی رفتار سے دوڑنے کے بعد صرف 20-30 سیکنڈ میں کیوں رک جاتا ہے؟", ["جسمانی درجہ حرارت تیزی سے حد سے زیادہ بڑھ جاتا ہے", "پھیپھڑے بند ہو جاتے ہیں", "ٹانگوں کی ہڈی ٹوٹ جاتی ہے", "دل کی دھڑکن رک جاتی ہے"], "جسمانی درجہ حرارت تیزی سے حد سے زیادہ بڑھ جاتا ہے", "تیز ترین دوڑ سے چیتے کے اندر شدید حرارت پیدا ہو جاتی ہے جسے ٹھنڈا کرنا لازمی ہوتا ہے۔")
    },
    # 87: Elephant infrasound
    {
        "en": ("How do African bush elephant herds communicate across miles of arid savanna without trumpeting audibly?", ["Deep ground-borne infrasound rumblings", "High-frequency whistles", "Radio wave emission", "Pheromone air plumes"], "Deep ground-borne infrasound rumblings", "Elephants broadcast seismic sound waves below 20 Hz through padded feet across subterranean bedrock."),
        "ur": ("ہاتھی میلوں دور موجود اپنے ساتھی ہاتھیوں سے بغیر چنگھاڑے کیسے رابطہ کرتے ہیں؟", ["زمین میں جذب ہونے والی انفرا ساؤنڈ لہروں سے", "ہوا میں سیٹیاں بجا کر", "کانوں کو مسلسل ہلا کر", "خوشبو کے ذریعے"], "زمین میں جذب ہونے والی انفرا ساؤنڈ لہروں سے", "ہاتھی کے پاؤں زمین میں دھیمی فریکوئنسی کی لہریں پیدا کرتے ہیں جو دوسرے ہاتھی محسوس کر لیتے ہیں۔")
    },
    # 88: Bat upside-down roost
    {
        "en": ("Why do sleeping microbats hang upside-down from cave ceilings rather than perching right-side up?", ["Their light bones and weak legs cannot launch into flight from flat ground", "They sleep deeper that way", "To keep wings warm", "To hide their faces"], "Their light bones and weak legs cannot launch into flight from flat ground", "Hanging upside-down provides instant zero-energy drop-into-flight launch capability."),
        "ur": ("چمگادڑیں غاروں کی چھت سے الٹا لٹک کر کیوں سوتی ہیں؟", ["ان کی کمزور ٹانگیں زمین سے اڑان نہیں بھر سکتیں، گر کر اڑنا آسان ہوتا ہے", "انہیں سیدھا بیٹھنا پسند نہیں", "پروں کو ہوا لگانے کے لیے", "روشنی سے بچنے کے لیے"], "ان کی کمزور ٹانگیں زمین سے اڑان نہیں بھر سکتیں، گر کر اڑنا آسان ہوتا ہے", "چمگادڑ زمین سے چھلانگ نہیں لگا سکتی، چھت سے لٹک کر سیدھا نیچے گرتے ہی پر کھول لیتی ہے۔")
    },
    # 89: Honey longevity
    {
        "en": ("Why does raw natural honey found sealed in ancient Egyptian tombs remain completely edible without spoiling?", ["Extremely low moisture content and natural acidity", "High alcohol content", "Dense mineral salts", "Synthetic royal enzymes"], "Extremely low moisture content and natural acidity", "Honey's hygroscopic dry osmotic pressure and low pH suppress bacterial cell mitosis permanently."),
        "ur": ("ہزاروں سال پرانے مصری اہراموں سے ملنے والا شہد آج تک خراب کیوں نہیں ہوا؟", ["نمی کا نہ ہونا اور قدرتی تیزابیت جراثیم پیدا نہیں ہونے دیتی", "اس میں نمک ملا ہوتا ہے", "شہد کبھی پرانا نہیں ہوتا", "اس میں الکحل بن جاتی ہے"], "نمی کا نہ ہونا اور قدرتی تیزابیت جراثیم پیدا نہیں ہونے دیتی", "شہد میں پانی نہ ہونے کے برابر ہوتا ہے جس کی وجہ سے بیکٹیریا اس میں زندہ نہیں رہ سکتے۔")
    },
    # 90: Hummingbird metabolism
    {
        "en": ("What physiological state of torpor do ruby-throated hummingbirds enter at night to conserve critical metabolic energy?", ["Nocturnal torpor lowering body temperature by 30 degrees", "Deep hibernating coma", "Standard REM sleep", "Feather shedding state"], "Nocturnal torpor lowering body temperature by 30 degrees", "To survive cold darkness without continuous nectar sips, hummingbirds drop body temperature into temporary torpor."),
        "ur": ("رات کے وقت ہمِنگ برڈ پرندہ سردی اور بھوک سے بچنے کے لیے اپنے جسم کے ساتھ کیا کرتا ہے؟", ["ٹورپور (نیم بے ہوشی کی حالت) میں جا کر میٹابولزم سست کر دیتا ہے", "درخت کے تنے میں چھپ جاتا ہے", "مسلسل پر ہلاتا رہتا ہے", "گرم پانی تلاش کرتا ہے"], "ٹورپور (نیم بے ہوشی کی حالت) میں جا کر میٹابولزم سست کر دیتا ہے", "ہمِنگ برڈ رات کو درجہ حرارت اور دل کی دھڑکن گرا کر توانائی بچاتا ہے۔")
    },
    # 91: Electric eel shock
    {
        "en": ("What biological electrocyte cells in an Amazonian electric eel generate high-voltage discharges exceeding 600 volts?", ["Electrocytes arranged in series columns", "Modified venom glands", "Battery-like stomach acids", "Magnetic skin scales"], "Electrocytes arranged in series columns", "Thousands of electrocyte disk cells stack in biological series circuits to compound electric potential."),
        "ur": ("ایمیزون کے دریا کی الیکٹرک ایل مچھلی 600 وولٹ کا زوردار کرنٹ کیسے پیدا کرتی ہے؟", ["جسم میں موجود الیکٹرو سائٹس کے قدرتی خلیوں کے سلسلے سے", "زہریلے ڈنک سے", "پانی کے نمک کو چھو کر", "دانتوں کی رگڑ سے"], "جسم میں موجود الیکٹرو سائٹس کے قدرتی خلیوں کے سلسلے سے", "مچھلی کے پٹھوں میں ہزاروں خلیات بیٹری کی پلیٹوں کی طرح جڑ کر ہائی وولٹیج بناتے ہیں۔")
    },
    # 92: Firefly bioluminescence
    {
        "en": ("Which biochemical enzyme reaction produces 98% efficient cold luminescence in summer fireflies?", ["Luciferase catalyzing luciferin with ATP and oxygen", "Phosphorus glow stick friction", "Static electricity sparks", "Digestive methane burning"], "Luciferase catalyzing luciferin with ATP and oxygen", "Luciferase enzyme reaction yields visible photons with nearly zero thermal energy loss as heat."),
        "ur": ("گرمیوں کی راتوں میں چمکنے والا جگنو بغیر گرم ہوئے ٹھنڈی روشنی کیسے پیدا کرتا ہے؟", ["لوسیفرین مادے اور لوسیفریز انزائم کے کیمیائی ملاپ سے", "فاسفورس کے رگڑ سے", "پیٹ میں گیس جلنے سے", "جامد بجلی کے اخراج سے"], "لوسیفرین مادے اور لوسیفریز انزائم کے کیمیائی ملاپ سے", "جگنو کا کیمیائی عمل سو فیصد روشنی پیدا کرتا ہے جس میں حرارت کا ضیاع نہیں ہوتا۔")
    },
    # 93: Flamingo pink color
    {
        "en": ("What dietary nutrient causes grey wild flamingo chicks to develop bright pink and crimson plumage?", ["Carotenoid pigments found in brine shrimp and algae", "Iron minerals in lake mud", "Volcanic sulfur vents", "Berry juices"], "Carotenoid pigments found in brine shrimp and algae", "Flamingo liver enzymes metabolize dietary carotenoids into canthaxanthin pigments deposited in wing feathers."),
        "ur": ("پیدائش کے وقت سفید اور سرمئی فلیمنگو (راج ہنس) پرندے بڑے ہو کر گلابی کیوں ہو جاتے ہیں؟", ["خوراک میں کیروٹینائیڈ سے بھرپور جھینگے اور کائی کھانے سے", "پانی کے نمکیات سے", "دھوپ کی تپش سے", "قدرتی رنگ بدلنے سے"], "خوراک میں کیروٹینائیڈ سے بھرپور جھینگے اور کائی کھانے سے", "فلیمنگو جو خاص آبی خوراک کھاتا ہے اس کے گلابی کیمیائی اجزا پروں میں جمع ہو جاتے ہیں۔")
    },
    # 94: Spider silk tensile strength
    {
        "en": ("Why is natural golden orb-weaver spider dragline silk proportionally stronger by weight than high-grade steel cable?", ["Interwoven beta-sheet protein nanocrystals inside flexible peptide chains", "Liquid diamond fibers", "High carbon steel plating", "Adhesive mineral glue"], "Interwoven beta-sheet protein nanocrystals inside flexible peptide chains", "Spidroin protein molecules align rigid crystalline regions within elastic amorphous matrixes."),
        "ur": ("مکڑی کا جالا باریک ہونے کے باوجود وزن کے تناسب سے اسٹیل کے تار سے بھی زیادہ مضبوط کیوں ہوتا ہے؟", ["پروٹین کے نینو کرسٹلز کی لچکدار اور مضبوط چینز کی وجہ سے", "اس میں لوہے کے ذرات ہوتے ہیں", "چپکنے والے گوند کی وجہ سے", "ہوا کی نمی جمنے سے"], "پروٹین کے نینو کرسٹلز کی لچکدار اور مضبوط چینز کی وجہ سے", "مکڑی کے ریشم میں موجود پروٹین کی سالماتی ساخت کھنچاؤ برداشت کرنے میں بے مثال ہے۔")
    },
    # 95: Ant proportional strength
    {
        "en": ("Why can a tiny worker ant lift objects fifty times its own body mass while an elephant cannot?", ["Square-cube scaling law gives small muscles higher relative strength", "Ants have hydraulic fluid joints", "Ant muscles are made of titanium", "Ants use acoustic levitation"], "Square-cube scaling law gives small muscles higher relative strength", "Cross-sectional muscle area scales with the square of size, while overall body weight scales with the cube."),
        "ur": ("ایک چھوٹی چیونٹی اپنے وزن سے 50 گنا زیادہ بوجھ کیوں اٹھا لیتی ہے جبکہ ہاتھی ایسا نہیں کر سکتا؟", ["چھوٹے جسم کے مسلز کا رقبہ وزن کے مقابلے میں زیادہ طاقت دیتا ہے", "چیونٹی کی ہڈیاں لوہے کی ہوتی ہیں", "چیونٹی کے پاؤں چپکتے ہیں", "چیونٹی کے جسم میں ہوا ہوتی ہے"], "چھوٹے جسم کے مسلز کا رقبہ وزن کے مقابلے میں زیادہ طاقت دیتا ہے", "طبیعیات کے اسکوائر کیوب قانون کے مطابق ننھے جانداروں کی پٹھوں کی طاقت وزن کے مقابلے میں زیادہ ہوتی ہے۔")
    },
    # 96: Water strider surface tension
    {
        "en": ("How does a pond water strider bug glide across standing water puddles without sinking beneath the surface?", ["Hydrophobic leg microhairs and water surface tension", "Broad webbed feet", "Low body density like oil", "Tiny air bubbles under wings"], "Hydrophobic leg microhairs and water surface tension", "Thousands of nanogrooved setae trap air cushions, utilizing water hydrogen-bond surface tension as an elastic sheet."),
        "ur": ("پانی کا کیڑا (واٹر اسٹرائیڈر) ندی یا جوہڑ کے پانی پر بغیر ڈوبے تیزی سے کیسے چلتا ہے؟", ["ٹانگوں کے باریک واٹر پروف بال اور پانی کی سرفیس ٹینشن کی وجہ سے", "اس کے پاؤں میں چپو ہوتے ہیں", "وہ پانی سے ہلکا ہوتا ہے", "وہ مسلسل اڑتا رہتا ہے"], "ٹانگوں کے باریک واٹر پروف بال اور پانی کی سرفیس ٹینشن کی وجہ سے", "پانی کی سطح پر مالیکیولز کا تناؤ ایک لچکدار جھلی کا کام کرتا ہے جس پر کیڑا آسانی سے دوڑتا ہے۔")
    },
    # 97: Snail slime lubrication
    {
        "en": ("Why can a terrestrial garden snail crawl safely over the razor-sharp edge of a surgical blade without suffering cuts?", ["Thick protective layer of moisturizing mucus slime", "Hard metal skin on foot", "Rapid tissue regeneration", "The blade bends outward"], "Thick protective layer of moisturizing mucus slime", "Pedal mucus acts as a non-Newtonian gel cushion, distributing pressure and lubricating contact surfaces."),
        "ur": ("باغ کا گھونگھا (سنیل) تیز دھار بلیڈ پر سے گزر جائے تو بھی اس کا پیٹ کیوں نہیں کٹتا؟", ["اس کے پیر سے نکلنے والا گاڑھا لیس دار لعاب ایک محفوظ تہہ بنا دیتا ہے", "اس کی کھال چمڑے کی ہوتی ہے", "بلیڈ نرم ہو جاتا ہے", "وہ ہوا میں اٹھ کر چلتا ہے"], "اس کے پیر سے نکلنے والا گاڑھا لیس دار لعاب ایک محفوظ تہہ بنا دیتا ہے", "گھونگھے کا چپچپا لعاب دباؤ کو تقسیم کر کے بلیڈ کی دھار سے گوشت کو بچاتا ہے۔")
    },
    # 98: Gecko feet van der Waals
    {
        "en": ("How does a nocturnal gecko lizard scale smooth vertical glass panes and hang upside-down from ceilings?", ["Millions of spatulae setae producing intermolecular van der Waals forces", "Suction cup pads on toes", "Sticky resin secretion", "Static electrostatic charge"], "Millions of spatulae setae producing intermolecular van der Waals forces", "Microscopic toe hairs achieve atomic proximity with surfaces, engaging electrostatic van der Waals attractions."),
        "ur": ("چھپکلی شیشے کی بالکل ہموار کھڑکی پر بغیر گرے اور بغیر کسی گوند کے کیسے چڑھ جاتی ہے؟", ["انگلیوں کے باریک ریشوں میں ونڈر والز مالیکیولر فورسز کے باعث", "پاؤں میں سکشن کپ ہونے سے", "چپکنے والا پسینہ نکلنے سے", "ناخنوں کے پھنسنے سے"], "انگلیوں کے باریک ریشوں میں ونڈر والز مالیکیولر فورسز کے باعث", "چھپکلی کی انگلیوں پر لاکھوں ننھے بال ایٹمی سطح پر شیشے کے ساتھ کشش پیدا کرتے ہیں۔")
    },
    # 99: Axolotl regeneration
    {
        "en": ("Which unique Mexican salamander can regrow lost limbs, spinal cords, and portions of its brain without scarring?", ["The axolotl", "The newt", "The gecko", "The iguana"], "The axolotl", "Axolotls retain embryonic blastema progenitor cells throughout adult life, enabling perfect tissue regeneration."),
        "ur": ("میکسیکو کا وہ کون سا نایاب آبی جانور ہے جس کا کٹا ہوا ہاتھ، ریڑھ کی ہڈی یا دل کا حصہ دوبارہ اگ آتا ہے؟", ["ایکسولوٹل (Axolotl)", "نیوٹ", "مینڈک", "کچھوا"], "ایکسولوٹل (Axolotl)", "ایکسولوٹل میں خلیات کی پیدائش کا حیرت انگیز قدرتی نظام ہے جو کسی بھی عضو کو دوبارہ اگا دیتا ہے۔")
    },
    # 100: Monarch butterfly navigation
    {
        "en": ("How do migrating monarch butterflies navigate 3,000 miles to the exact winter fir forests in Mexico?", ["A time-compensated solar compass coupled with a circadian clock", "Visual highway landmarks", "Star constellation maps", "Following prevailing jet winds"], "A time-compensated solar compass coupled with a circadian clock", "Monarch antennae integrate sun azimuth angles with circadian molecular clocks to maintain steady southerly headings."),
        "ur": ("مونارک تتلیاں ہزاروں میل دور میکسیکو کے ایک مخصوص جنگل میں بغیر کسی نقشے کے کیسے پہنچتی ہیں؟", ["سورج کی پوزیشن اور اپنے اندرونی جسمانی گھڑیال (سرکیڈین کلاک) کی مدد سے", "دریاؤں کا پیچھا کر کے", "ہوا کے رخ پر اڑ کر", "ستاروں کو دیکھ کر"], "سورج کی پوزیشن اور اپنے اندرونی جسمانی گھڑیال (سرکیڈین کلاک) کی مدد سے", "تتلیاں سورج کے زاویے اور اپنے اینٹینا میں موجود سائنسی گھڑی سے سمندری راستہ طے کرتی ہیں۔")
    },
    # 101: Electric train smoke
    {
        "en": ("An electric high-speed train travels north at 100 mph while a gale wind blows from the west. In which direction does the train smoke drift?", ["Electric trains produce no smoke", "Toward the east", "Toward the south", "Toward the southwest"], "Electric trains produce no smoke", "Electric trains run on overhead catenary wires and emit zero engine smoke."),
        "ur": ("ایک تیز رفتار الیکٹرک ٹرین 100 کلومیٹر فی گھنٹہ کی رفتار سے شمال کی طرف جا رہی ہے، اس کا دھواں کس طرف جائے گا؟", ["الیکٹرک ٹرین کا کوئی دھواں نہیں ہوتا", "جنوب کی طرف", "مشرق کی طرف", "مغرب کی طرف"], "الیکٹرک ٹرین کا کوئی دھواں نہیں ہوتا", "بجلی سے چلنے والی ٹرین انجن میں کوئی دھواں پیدا ہی نہیں کرتی۔")
    },
    # 102: Two fathers and two sons
    {
        "en": ("Two fathers and two sons go fishing together. Each catches one whole fish, yet they bring home exactly three fish. How?", ["The fishing group consists of grandfather, father, and son", "One fish jumped away", "They shared a fishing rod", "They miscounted"], "The fishing group consists of grandfather, father, and son", "There are three individuals: the father is both a son to the grandfather and a father to the son."),
        "ur": ("دو باپ اور دو بیٹے مچھلیاں پکڑنے گئے۔ سب نے ایک ایک مچھلی پکڑی مگر کل مچھلیاں صرف 3 تھیں، کیسے؟", ["وہ تین لوگ تھے: دادا، باپ اور بیٹا", "ایک مچھلی گر گئی تھی", "ایک نے مچھلی نہیں پکڑی", "گنتی میں غلطی تھی"], "وہ تین لوگ تھے: دادا، باپ اور بیٹا", "باپ اپنے والد کا بیٹا ہے اور اپنے بچے کا باپ، اس طرح کل تین افراد بنتے ہیں۔")
    },
    # 103: Rooster on the roof
    {
        "en": ("A rooster sits on the peaked ridge of a barn roof. If it lays an egg, which side will the egg roll down?", ["Roosters do not lay eggs", "The eastern side", "The western side", "It balances on top"], "Roosters do not lay eggs", "Hens lay eggs, whereas male roosters do not produce eggs."),
        "ur": ("ایک مرغا چھت کی اونچی منڈیر پر بیٹھا ہے۔ اگر وہ انڈا دے تو انڈا دائیں گرے گا یا بائیں؟", ["مرغا انڈا نہیں دیتا (مرغی دیتی ہے)", "دائیں طرف", "بائیں طرف", "منڈیر پر رکا رہے گا"], "مرغا انڈا نہیں دیتا (مرغی دیتی ہے)", "انڈے صرف مرغیاں دیتی ہیں، نر مرغا انڈے نہیں دیتا۔")
    },
    # 104: 30-foot ladder fall
    {
        "en": ("A painter fell off a 30-foot extension ladder onto solid concrete pavement, yet did not suffer a single bruise. Why?", ["He was standing on the bottom rung", "He had a parachute", "The concrete was padded", "He wore a steel suit"], "He was standing on the bottom rung", "Falling off the bottom rung of a ladder is a drop of only a few inches."),
        "ur": ("ایک پینٹر 30 فٹ اونچی سیڑھی پر سے سیمنٹ کے فرش پر گرا مگر اسے ایک خراش بھی نہیں آئی، کیوں؟", ["کیونکہ وہ سیڑھی کے پہلے پائیدان پر کھڑا تھا", "اس نے حفاظتی جال باندھا تھا", "فرش پر گدا تھا", "وہ ہوا میں لٹک گیا"], "کیونکہ وہ سیڑھی کے پہلے پائیدان پر کھڑا تھا", "وہ سیڑھی کے سب سے نیچے والے ڈنڈے پر تھا جس کی زمین سے دوری صرف چند انچ تھی۔")
    },
    # 105: Living person burial
    {
        "en": ("Why is it legally prohibited in every country to bury a living person?", ["Living people are not buried", "State zoning codes", "Sanitary permits", "Cemetery land values"], "Living people are not buried", "Burial rituals are strictly reserved for deceased individuals; living people are alive."),
        "ur": ("لاہور میں رہنے والے ایک زندہ سلامت شخص کو کراچی کے قبرستان میں کیوں دفن نہیں کیا جا سکتا؟", ["کیونکہ وہ زندہ ہے اور زندہ انسانوں کو دفن نہیں کیا جاتا", "قانونی ممانعت ہے", "شہر کا فاصلہ ہے", "قبروں کی کمی ہے"], "کیونکہ وہ زندہ ہے اور زندہ انسانوں کو دفن نہیں کیا جاتا", "زندہ انسانوں کو دفنانا ممکن نہیں، صرف انتقال کر جانے والوں کی تدفین کی جاتی ہے۔")
    },
    # 106: Baker's dozen
    {
        "en": ("If you buy a traditional baker's dozen of fresh morning donuts, exactly how many donuts do you receive?", ["Thirteen donuts", "Twelve donuts", "Eleven donuts", "Fourteen donuts"], "Thirteen donuts", "Historically, bakers added a 13th item to avoid penal fines for underweight goods."),
        "ur": ("روایتی بیکرز درجن (Baker's Dozen) میں کل کتنی چیزیں ملتی ہیں؟", ["13 چیزیں", "12 چیزیں", "10 چیزیں", "14 چیزیں"], "13 چیزیں", "پرانے وقتوں میں نانبائی وزن میں کمی کے جرمانے سے بچنے کے لیے 12 کی جگہ 13 چیزیں دیتے تھے۔")
    },
    # 107: Drop egg on concrete
    {
        "en": ("How can you drop a fragile raw chicken egg onto a solid concrete floor from five feet up without cracking it?", ["Concrete floors do not crack from a dropped egg", "Drop it onto a sponge", "Boil the egg first", "Freeze the floor"], "Concrete floors do not crack from a dropped egg", "The concrete floor itself is immensely strong and will easily survive without cracking."),
        "ur": ("آپ انڈے کو ٹھوس کنکریٹ کے فرش پر کیسے گرائیں گے کہ فرش نہ ٹوٹے؟", ["انڈے کے گرنے سے فرش کبھی نہیں ٹوٹ سکتا", "انڈے کو آہستہ چھوڑیں", "فرش پر چادر بچھا کر", "انڈے کو ابال کر"], "انڈے کے گرنے سے فرش کبھی نہیں ٹوٹ سکتا", "سوال فرش کے ٹوٹنے کا ہے، انڈے سے ٹھوس کنکریٹ کا فرش کبھی نہیں ٹوٹتا۔")
    },
    # 108: Three under one umbrella
    {
        "en": ("Three adult friends walk down a city street in torrential rain under a small single umbrella, yet none gets wet. How?", ["It was not raining at the time", "They wore rain slickers", "They ran inside a taxi", "They walked very fast"], "It was not raining at the time", "The umbrella was carried, but there was no rain falling from the sky."),
        "ur": ("تین دوست بارش والی چھتری لے کر سڑک پر نکلے اور کسی کا ایک قطرہ بھی نہیں لگا، کیسے؟", ["کیونکہ بارش ہو ہی نہیں رہی تھی", "وہ چھتری میں چھپے ہوئے تھے", "وہ کار میں بیٹھ گئے", "ہوا تیز تھی"], "کیونکہ بارش ہو ہی نہیں رہی تھی", "وہ صرف چھتری ساتھ لے کر جا رہے تھے مگر اس وقت بارش نہیں ہو رہی تھی۔")
    },
    # 109: One-way street walking
    {
        "en": ("A pedestrian driver walks the wrong direction down a one-way avenue, right past police officers, but receives no ticket. Why?", ["He was walking on foot", "He was off duty", "The street was deserted", "It was midnight"], "He was walking on foot", "Traffic one-way lane rules apply strictly to motor vehicles, not walking pedestrians."),
        "ur": ("ایک شخص ون وے روڈ پر الٹی سمت جا رہا تھا، ٹریفک پولیس نے دیکھا مگر چالان نہیں کیا، کیوں؟", ["کیونکہ وہ پیدل چل رہا تھا", "وہ پولیس کا دوست تھا", "روڈ خالی تھا", "رات کا وقت تھا"], "کیونکہ وہ پیدل چل رہا تھا", "ون وے ٹریفک کے قوانین گاڑیوں کے لیے ہوتے ہیں، پیدل چلنے والوں کا چالان نہیں ہوتا۔")
    },
    # 110: Surgeon riddle
    {
        "en": ("A boy and his father are in a crash. At the clinic, the attending surgeon looks at the boy and gasps: 'I cannot operate, this boy is my son!' Who is the surgeon?", ["The boy's mother", "His grandfather", "His uncle", "A step-parent"], "The boy's mother", "The surgeon is the boy's biological mother."),
        "ur": ("ایک باپ اور بیٹا حادثے میں زخمی ہوئے۔ اسپتال میں چیف سرجن نے لڑکے کو دیکھ کر کہا: 'یہ میرا بیٹا ہے!' سرجن کا لڑکے سے کیا رشتہ تھا؟", ["وہ اس کی والدہ (ماں) تھی", "اس کا دادا تھا", "اس کا چچا تھا", "اس کا بڑا بھائی تھا"], "وہ اس کی والدہ (ماں) تھی", "سرجن ایک خاتون اور اس بچے کی سگی والدہ تھی۔")
    },
    # 111: Vacuum chamber bowling ball
    {
        "en": ("Inside a sealed vacuum cylinder evacuated of all air, an iron bowling ball and a goose feather are dropped together. Which strikes the base plate first?", ["Both strike simultaneously", "The iron bowling ball", "The goose feather", "Neither falls"], "Both strike simultaneously", "Without aerodynamic air resistance, gravitational acceleration g accelerates all masses identically."),
        "ur": ("ہوا سے مکمل خالی خلاء (ویکیوم) کے اندر لوہے کا بھاری گولہ اور پرندہ کا پر گرائیں تو پہلے کون گرے گا؟", ["دونوں بالکل ایک ساتھ گریں گے", "لوہے کا گولہ", "پرندے کا پر", "کوئی بھی نہیں گرے گا"], "دونوں بالکل ایک ساتھ گریں گے", "ہوا کی غیر موجودگی میں کشش ثقل تمام چیزوں کو ایک جیسی رفتار سے نیچے کھینچتی ہے۔")
    },
    # 112: Anchor dropped from boat
    {
        "en": ("A sailor tosses a heavy steel anchor overboard from a small rowboat into a calm pond. Does the anchor float or sink?", ["It sinks to the bottom", "It floats on water", "It hovers mid-depth", "It dissolves"], "It sinks to the bottom", "Dense steel possesses a specific gravity roughly eight times that of fresh water, sinking instantly."),
        "ur": ("کشتی میں بیٹھے ملاح نے وزنی لوہے کا لنگر پانی میں پھینک دیا، لنگر پر کیا بیتی؟", ["وہ فورا تہہ میں ڈوب گیا", "وہ پانی پر تیرنے لگا", "وہ غائب ہو گیا", "پانی ابلنے لگا"], "وہ فورا تہہ میں ڈوب گیا", "لوہے کی کثافت پانی سے بہت زیادہ ہوتی ہے اس لیے لنگر فورا گہرائی میں ڈوب جاتا ہے۔")
    },
    # 113: Ship ladder tide
    {
        "en": ("A ship moored in harbor has a rope ladder hanging over the hull. Rungs are one foot apart, and water touches the 3rd rung. If high tide raises the water level by four feet, which rung is touching the water now?", ["Still the 3rd rung", "The 7th rung", "The 1st rung", "The 5th rung"], "Still the 3rd rung", "The floating ship and its attached rope ladder rise upward together with the ocean tide."),
        "ur": ("سمندر میں تیرتے جہاز کے ساتھ لٹکی رسی کی سیڑھی کا تیسرا ڈنڈا پانی چھو رہا ہے۔ اگر جوار بھاٹا سے پانی 4 فٹ بلند ہو جائے تو اب کون سا ڈنڈا پانی چھوئے گا؟", ["اب بھی تیسرا ڈنڈا ہی چھوئے گا", "ساتواں ڈنڈا", "پہلا ڈنڈا", "پانچواں ڈنڈا"], "اب بھی تیسرا ڈنڈا ہی چھوئے گا", "پانی چڑھنے سے تیرتا ہوا بحری جہاز اور اس کی سیڑھی دونوں پانی کے ساتھ ہی اوپر اٹھ جائیں گے۔")
    },
    # 114: Black night walker
    {
        "en": ("A pedestrian dressed entirely in black walks along a dark road with broken streetlamps and no moonlight. A car speeding with headlights off stops right in time. How did the driver see him?", ["It was broad daylight", "The driver wore night goggles", "A lightning strike lit the road", "The pedestrian wore reflector shoes"], "It was broad daylight", "The riddle mentions no moon and broken streetlamps, but it was daytime when sunlight illuminates everything."),
        "ur": ("ایک آدمی کالے کپڑے اور کالی ٹوپی پہنے سڑک پر جا رہا تھا، اسٹریٹ لائٹ بند تھیں، گاڑی کی ہیڈ لائٹس بھی بند تھیں مگر ڈرائیور نے اسے دور سے دیکھ کر بریک لگا دی، کیسے؟", ["کیونکہ دن کا وقت تھا اور دھوپ نکلی تھی", "ڈرائیور کے پاس نائٹ ویژن چشمہ تھا", "بجلی چمکی تھی", "آدمی نے چیخ ماری"], "کیونکہ دن کا وقت تھا اور دھوپ نکلی تھی", "سوال میں اندھیری رات کا ذکر نہیں تھا، وہ دن کے اجالے میں سڑک پر جا رہا تھا۔")
    },
    # 115: Low bridge truck
    {
        "en": ("A cargo truck is wedged two inches beneath a concrete highway overpass. A passing schoolgirl suggests an effortless fix to drive through without damage. What was it?", ["Deflate the truck tires slightly", "Chop the bridge with an axe", "Tow the truck with a crane", "Melt the pavement"], "Deflate the truck tires slightly", "Releasing air pressure from heavy pneumatic tires lowers vehicle height by a few inches safely."),
        "ur": ("ایک کنٹینر والا بڑا ٹرک ایک پل کے نیچے پھنس گیا کیونکہ پل دو انچ نیچا تھا۔ ایک بچے نے بغیر پل توڑے ٹرک نکالنے کا کیا آسان حل بتایا؟", ["ٹرک کے ٹائروں کی تھوڑی ہوا نکال دیں", "پل کو ہتھوڑے سے توڑیں", "ٹرک کو کرین سے کھینچیں", "سڑک کھود دیں"], "ٹرک کے ٹائروں کی تھوڑی ہوا نکال دیں", "ٹائروں کی ہوا کم کرنے سے ٹرک کی اونچائی چند انچ کم ہو جاتی ہے اور وہ باآسانی نکل جاتا ہے۔")
    },
    # 116: Border plane crash
    {
        "en": ("An international passenger plane crashes exactly on the national border line between Canada and the USA. Where are the survivors buried?", ["Survivors are alive and not buried", "In Canada", "In the USA", "In neutral territory"], "Survivors are alive and not buried", "Survivors are living human beings who survived the crash, so they are hospitalized rather than buried."),
        "ur": ("ایک ہوائی جہاز دو ملکوں کی سرحد کی عین لائن پر گر کر تباہ ہو گیا۔ بتائیں زندہ بچ جانے والوں کو کہاں دفن کیا جائے گا؟", ["زندہ بچ جانے والوں کو دفن نہیں کیا جاتا", "پہلے ملک میں", "دوسرے ملک میں", "سرحد پر"], "زندہ بچ جانے والوں کو دفن نہیں کیا جاتا", "جو لوگ حادثے میں زندہ بچ گئے ہوں انہیں اسپتال لے جایا جاتا ہے، دفن نہیں کیا جاتا۔")
    },
    # 117: Subtract 5 from 25
    {
        "en": ("How many times can you subtract the number five from twenty-five?", ["Only once", "Five times", "Zero times", "Infinitely many times"], "Only once", "Once you subtract 5 from 25 the first time, the remaining balance is 20, not 25."),
        "ur": ("آپ عدد 25 میں سے عدد 5 کو کتنی بار تفریق (منفی) کر سکتے ہیں؟", ["صرف ایک بار", "پانچ بار", "دس بار", "کبھی نہیں"], "صرف ایک بار", "پہلی بار 5 گھٹانے کے بعد باقی 20 رہ جائے گا، لہٰذا 25 میں سے صرف ایک ہی بار نکالا جا سکتا ہے۔")
    },
    # 118: Right turn car wheel
    {
        "en": ("When a passenger car makes a sharp ninety-degree right turn around a street corner, which of its tires does not spin?", ["The spare tire in the trunk", "The front right tire", "The rear right tire", "The rear left tire"], "The spare tire in the trunk", "The spare wheel stored in the luggage compartment remains stationary while road tires rotate."),
        "ur": ("جب ایک کار تیز رفتاری سے دائیں طرف موڑ کاٹتی ہے تو کار کا کون سا پہیہ بالکل نہیں گھومتا؟", ["ڈگی میں رکھا اضافی پہیہ (اسٹپنی)", "آگے کا دایاں پہیہ", "پیچھے کا دایاں پہیہ", "بایاں پہیہ"], "ڈگی میں رکھا اضافی پہیہ (اسٹپنی)", "ڈگی میں رکھی ہوئی اسٹپنی گاڑی کے ساتھ سفر کرتی ہے مگر خود گھومتی نہیں ہے۔")
    },
    # 119: Baseball runner home
    {
        "en": ("A masked player runs away from home, turns left three times, and returns home safely, only to confront two masked men. What is the setting?", ["A baseball game", "A bank robbery", "A Halloween costume party", "A theatrical drama"], "A baseball game", "In baseball, the batter runs around 1st, 2nd, and 3rd bases to return to home plate facing the catcher and umpire."),
        "ur": ("ایک نقاب پوش شخص گھر سے بھاگتا ہے، تین بار بائیں مڑتا ہے اور واپس گھر پہنچتا ہے تو سامنے دو نقاب پوش کھڑے پاتا ہے، یہ کیا منظر ہے؟", ["بیس بال کا کھیل", "بینک ڈکیتی", "ڈرامے کا اسٹیج", "خواب"], "بیس بال کا کھیل", "بیس بال میں ہوم بیس سے دوڑ کر کھلاڑی واپس ہوم پلیٹ پر آتا ہے جہاں کیچر اور امپائر کھڑے ہوتے ہیں۔")
    },
    # 120: Two coins making thirty cents
    {
        "en": ("You have two United States coins that total thirty cents, and one of them is not a nickel. What are the two coins?", ["A quarter and a nickel", "Two dimes", "Three nickels", "A half-dollar and a dime"], "A quarter and a nickel", "One coin is a quarter (which is not a nickel), while the second coin is a nickel (25 + 5 = 30)."),
        "ur": ("آپ کے پاس دو سکے ہیں جن کا مجموعہ 30 روپے بنتا ہے، ان میں سے ایک سکہ 5 کا نہیں ہے۔ وہ دو سکے کون سے ہیں؟", ["ایک 25 کا اور دوسرا 5 کا", "دونوں 15 کے", "تین 10 کے", "ایک 20 کا اور ایک 10 کا"], "ایک 25 کا اور دوسرا 5 کا", "ایک سکہ 25 کا ہے (جو 5 کا نہیں ہے) اور دوسرا سکہ 5 کا ہے، کل ملا کر 30 بنتے ہیں۔")
    },
    # 121: Apples in basket
    {
        "en": ("There are five fresh red apples sitting in a fruit basket. If you take away three apples, how many apples do you have?", ["Three apples", "Two apples", "Five apples", "Zero apples"], "Three apples", "You physically took three apples, so you now possess those three apples in your hands."),
        "ur": ("ٹوکری میں پانچ تازہ سیب رکھے ہیں۔ اگر آپ ان میں سے تین سیب اٹھا لیتے ہیں تو آپ کے پاس کتنے سیب ہیں؟", ["تین سیب", "دو سیب", "پانچ سیب", "ایک بھی نہیں"], "تین سیب", "آپ نے خود تین سیب اٹھائے ہیں تو آپ کے اپنے ہاتھ میں وہی تین سیب ہوں گے۔")
    },
    # 122: Farmer river boat
    {
        "en": ("A farmer must transport a fox, a goose, and a bag of grain across a river in a boat holding only himself and one item. If left alone, fox eats goose, goose eats grain. What does he row across first?", ["The goose", "The fox", "The grain", "The fox and grain together"], "The goose", "Taking the goose first leaves the fox and grain safely alone on the initial shore."),
        "ur": ("ایک کسان کو کشتی میں لومڑی، بطخ اور دانہ دریا پار لے جانا ہے مگر کشتی میں صرف وہ اور ایک چیز آ سکتی ہے۔ وہ سب سے پہلے کسے لے جائے گا؟", ["بطخ کو", "لومڑی کو", "دانے کی بوری کو", "کسی کو نہیں"], "بطخ کو", "بطخ کو پہلے لے جانے سے کنارے پر لومڑی اور دانہ محفوظ رہتے ہیں کیونکہ لومڑی دانہ نہیں کھاتی۔")
    },
    # 123: Bird on high-voltage wire
    {
        "en": ("Why does a pigeon perching with both claws on an uninsulated 50,000-volt high-voltage overhead power line not get electrocuted?", ["Both feet are at the same electrical potential, so no current flows across its body", "Bird claws are made of rubber", "Air insulates the line", "The voltage is zero"], "Both feet are at the same electrical potential, so no current flows across its body", "Current requires a voltage potential difference to flow; perching on one wire creates virtually zero delta V across the claws."),
        "ur": ("بجلی کے ننگے ہائی وولٹیج تار پر دونوں پنجے جما کر بیٹھا پرندہ کرنٹ لگنے سے کیوں نہیں مرتا؟", ["دونوں پنجوں میں وولٹیج کا فرق نہیں ہوتا اس لیے جسم سے کرنٹ نہیں گزرتا", "پرندے کی ٹانگیں ربر کی ہوتی ہیں", "تار میں کرنٹ نہیں ہوتا", "پرندے کے پر محفوظ رکھتے ہیں"], "دونوں پنجوں میں وولٹیج کا فرق نہیں ہوتا اس لیے جسم سے کرنٹ نہیں گزرتا", "کرنٹ بہنے کے لیے دو مختلف وولٹیج یا زمین کی ضرورت ہوتی ہے، ایک ہی تار پر کوئی برقی دباؤ پیدا نہیں ہوتا۔")
    },
    # 124: Polar bear meets penguin
    {
        "en": ("Why do wild Arctic polar bears never hunt or consume wild Antarctic penguins for food in nature?", ["They inhabit opposite poles of the planet", "Penguins swim faster than bears", "Penguin meat is poisonous", "Polar bears hibernate during penguin season"], "They inhabit opposite poles of the planet", "Polar bears live exclusively in the North Pole Arctic, whereas penguins dwell in the Southern Hemisphere Antarctica."),
        "ur": ("قطبی ریچھ کبھی بھی پینگوئن پرندے کا شکار کیوں نہیں کر پاتا؟", ["کیونکہ ریچھ قطب شمالی پر اور پینگوئن قطب جنوبی پر رہتے ہیں", "پینگوئن ریچھ سے تیز بھاگتا ہے", "پینگوئن کا گوشت زہریلا ہوتا ہے", "ریچھ برف میں سوتا رہتا ہے"], "کیونکہ ریچھ قطب شمالی پر اور پینگوئن قطب جنوبی پر رہتے ہیں", "دونوں زمین کے دو بالکل مخالف سروں پر بستے ہیں اور قدرت میں کبھی آمنے سامنے نہیں آتے۔")
    },
    # 125: Iceberg underwater mass
    {
        "en": ("Why does approximately ninety percent of a floating glacial iceberg's total physical volume remain hidden beneath seawater?", ["Seawater density is only about nine percent greater than glacial ice density", "Icebergs are hollow", "The ocean pushes down on ice", "Salt dissolves underwater ice"], "Seawater density is only about nine percent greater than glacial ice density", "Archimedes' principle dictates that floating ice displaces seawater equal to its weight, leaving ~90% submerged."),
        "ur": ("سمندر میں تیرتے برفانی تودے (آئس برگ) کا 90 فیصد حصہ پانی کے نیچے کیوں چھپا رہتا ہے؟", ["برف کی کثافت سمندری پانی کے مقابلے میں صرف 9 فیصد کم ہوتی ہے", "برف اندر سے کھوکھلی ہوتی ہے", "پانی برف کو دباتا ہے", "نمک برف کو کھینچتا ہے"], "برف کی کثافت سمندری پانی کے مقابلے میں صرف 9 فیصد کم ہوتی ہے", "آرکیمیڈیز کے اصول کے تحت برف اپنے وزن کے برابر پانی ہٹاتی ہے جس سے اس کا بیشتر حصہ نیچے رہتا ہے۔")
    }
]

print(f"Catalog Easy Part 1 loaded {len(ITEMS)} items.")
