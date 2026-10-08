# -*- coding: utf-8 -*-
import json

EASY_ITEMS = [
    # --- Household & Classic Objects (1..100) ---
    {
        "en": ("What gets wetter the more it dries?", ["A towel", "A sponge", "A cloud", "Rain"], "A towel", "A towel absorbs moisture from your body as it dries you."),
        "ur": ("وہ کون سی چیز ہے جو خشک کرتے وقت خود گیلی ہو جاتی ہے؟", ["تولیہ", "بادل", "سورج", "ریت"], "تولیہ", "تولیہ پانی جذب کرتا ہے جس سے وہ خود گیلا ہو جاتا ہے۔")
    },
    {
        "en": ("What has hands but cannot clap?", ["A clock", "A glove", "A tree", "A robot"], "A clock", "A clock has hour and minute hands but cannot clap."),
        "ur": ("وہ کیا ہے جس کے ہاتھ ہیں مگر وہ تالی نہیں بجا سکتی؟", ["گھڑی", "درخت", "کرسی", "دستانہ"], "گھڑی", "گھڑی کی سوئیاں اس کے ہاتھ کہلاتی ہیں مگر وہ تالی نہیں بجا سکتیں۔")
    },
    {
        "en": ("What has to be broken before you can use it?", ["An egg", "A bottle", "A lock", "A stick"], "An egg", "You must crack an eggshell before cooking or consuming it."),
        "ur": ("وہ کون سی چیز ہے جسے استعمال کرنے سے پہلے توڑنا پڑتا ہے؟", ["انڈا", "تالہ", "شیشہ", "بادام"], "انڈا", "انڈے کو پکانے یا کھانے کے لیے پہلے توڑنا پڑتا ہے۔")
    },
    {
        "en": ("I am tall when young, and short when old. What am I?", ["A candle", "A tree", "A giraffe", "A building"], "A candle", "A candle melts down shorter as it burns over time."),
        "ur": ("وہ کیا ہے جو نیا ہو تو لمبا اور پرانا ہو تو چھوٹا ہو جاتا ہے؟", ["موم بتی", "درخت", "پنسل", "رسی"], "موم بتی", "موم بتی جلنے کے ساتھ ساتھ پگھل کر چھوٹی ہوتی جاتی ہے۔")
    },
    {
        "en": ("Which month of the year has 28 days?", ["All 12 months", "Only February", "Only January", "None of them"], "All 12 months", "Every calendar month has at least 28 days."),
        "ur": ("سال کے کتنے مہینوں میں 28 دن ہوتے ہیں؟", ["تمام 12 مہینوں میں", "صرف فروری میں", "چار مہینوں میں", "کسی میں نہیں"], "تمام 12 مہینوں میں", "ہر مہینے میں کم از کم 28 دن تو لازمی ہوتے ہیں۔")
    },
    {
        "en": ("What is full of holes but still holds water?", ["A sponge", "A bucket", "A net", "A colander"], "A sponge", "A sponge is filled with porous holes and absorbs water."),
        "ur": ("وہ کون سی چیز ہے جو سوراخوں سے بھری ہے مگر پھر بھی پانی روک لیتی ہے؟", ["اسفنج", "چھلنی", "بالٹی", "جالی"], "اسفنج", "اسفنج میں بے شمار سوراخ ہوتے ہیں لیکن وہ پانی جذب کر لیتا ہے۔")
    },
    {
        "en": ("What question can you never answer 'yes' to honestly?", ["Are you asleep?", "Are you awake?", "Are you hungry?", "Are you ready?"], "Are you asleep?", "If you are truly asleep, you cannot consciously answer the question."),
        "ur": ("وہ کون سا سوال ہے جس کا جواب آپ سچائی سے کبھی 'ہاں' میں نہیں دے سکتے؟", ["کیا آپ سو رہے ہیں؟", "کیا آپ جاگ رہے ہیں؟", "کیا آپ بھوکے ہیں؟", "کیا آپ تیار ہیں؟"], "کیا آپ سو رہے ہیں؟", "اگر انسان واقعی سو رہا ہو تو وہ ہوش و حواس میں جواب نہیں دے سکتا۔")
    },
    {
        "en": ("What is always in front of you but cannot be seen?", ["The future", "Air", "Your nose", "Darkness"], "The future", "The future is always ahead in time, yet invisible until it arrives."),
        "ur": ("وہ کیا ہے جو ہمیشہ آپ کے سامنے ہوتا ہے مگر دیکھا نہیں جا سکتا؟", ["مستقبل", "ہوا", "اندھیرا", "روشنی"], "مستقبل", "مستقبل ہمیشہ آنے والے وقت میں آگے ہوتا ہے مگر اسے دیکھا نہیں جا سکتا۔")
    },
    {
        "en": ("There is a one-story pink house with pink furniture. What color are the stairs?", ["No stairs", "Pink", "White", "Brown"], "No stairs", "A one-story house has no second floor, so it has no stairs."),
        "ur": ("ایک منزلہ گلابی گھر میں ہر چیز گلابی ہے۔ بتائیں سیڑھیاں کس رنگ کی ہیں؟", ["کوئی سیڑھی نہیں", "گلابی", "سفید", "بھوری"], "کوئی سیڑھی نہیں", "ایک منزلہ مکان میں دوسری منزل ہی نہیں ہوتی تو سیڑھیاں کہاں سے آئیں گی۔")
    },
    {
        "en": ("What can you break without ever picking it up or touching it?", ["A promise", "A window", "A twig", "A plate"], "A promise", "A promise is broken by failing to keep your word."),
        "ur": ("وہ کیا ہے جسے آپ چھوئے یا اٹھائے بغیر بھی توڑ سکتے ہیں؟", ["وعدہ", "شیشہ", "لکڑی", "تار"], "وعدہ", "وعدہ پورا نہ کرنے سے ٹوٹ جاتا ہے، اسے چھونے کی ضرورت نہیں۔")
    },
    {
        "en": ("What goes up but never comes down?", ["Your age", "A kite", "A balloon", "Smoke"], "Your age", "Your age only increases with each passing year."),
        "ur": ("وہ کون سی چیز ہے جو اوپر تو جاتی ہے مگر کبھی نیچے نہیں آتی؟", ["عمر", "پتنگ", "دھواں", "غبارہ"], "عمر", "انسان کی عمر وقت کے ساتھ صرف بڑھتی ہے، کم نہیں ہوتی۔")
    },
    {
        "en": ("A man walked in heavy rain with no umbrella or hat, yet did not get a single hair wet. Why?", ["He was bald", "He ran fast", "He wore a hood", "It was mist"], "He was bald", "He had no hair on his head to get wet."),
        "ur": ("ایک آدمی بارش میں بنا چھتری اور بنا ٹوپی کے گیا مگر اس کا ایک بال بھی نہیں بھیگا، کیوں؟", ["کیونکہ وہ گنجا تھا", "وہ تیز دوڑ رہا تھا", "اس نے پناہ لی", "بارش ہلکی تھی"], "کیونکہ وہ گنجا تھا", "اس کے سر پر بال ہی نہیں تھے جو بھیگتے۔")
    },
    {
        "en": ("What has a neck but no head?", ["A bottle", "A guitar", "A shirt", "A snake"], "A bottle", "A bottle has a narrow neck leading to its opening, but no head."),
        "ur": ("وہ کیا ہے جس کے پاس گردن ہے لیکن سر نہیں؟", ["بوتل", "قمیض", "گٹار", "چمچ"], "بوتل", "بوتل کا اوپری حصہ گردن کہلاتا ہے مگر اس کا سر نہیں ہوتا۔")
    },
    {
        "en": ("What has a thumb and four fingers, but is not alive?", ["A glove", "A robot", "A mannequin", "A skeleton"], "A glove", "A glove has five finger slots but is an inanimate clothing item."),
        "ur": ("وہ کون سی چیز ہے جس کے چار انگلیاں اور ایک انگوٹھا ہے مگر وہ جاندار نہیں؟", ["دستانہ", "روبوٹ", "پتلا", "ڈھانچہ"], "دستانہ", "دستانے میں انگلیوں کی جگہ بنی ہوتی ہے مگر وہ بے جان ہوتا ہے۔")
    },
    {
        "en": ("What has many teeth, but cannot bite?", ["A comb", "A saw", "A zipper", "A gear"], "A comb", "A comb has teeth designed for styling hair, not chewing."),
        "ur": ("وہ کون سی چیز ہے جس کے دانت ہیں مگر وہ چبا نہیں سکتی؟", ["کنگھی", "آری", "زپ", "پہیہ"], "کنگھی", "کنگھی کے دانت بال سنوارنے کے لیے ہوتے ہیں، کھانے کے لیے نہیں۔")
    },
    {
        "en": ("What has a head and a tail, but no body?", ["A coin", "A snake", "A pin", "A kite"], "A coin", "A coin has heads and tails sides but no anatomical body."),
        "ur": ("وہ کیا ہے جس کا سر اور دم تو ہے مگر دھڑ (جسم) نہیں؟", ["سکہ", "سانپ", "پن", "پتنگ"], "سکہ", "سکّے کے دونوں رخوں کو ہیڈ اور ٹیل کہا جاتا ہے۔")
    },
    {
        "en": ("Where does today come before yesterday?", ["In a dictionary", "On a calendar", "In a dream", "In history"], "In a dictionary", "Alphabetically, 'Today' comes before 'Yesterday' in a dictionary."),
        "ur": ("وہ کون سی جگہ ہے جہاں 'آج' ہمیشہ 'کل' سے پہلے آتا ہے؟", ["لغت (ڈکشنری) میں", "کیلنڈر پر", "خواب میں", "تاریخ میں"], "لغت (ڈکشنری) میں", "حروف تہجی کی ترتیب میں 'آ' کا لفظ 'ک' سے پہلے آتا ہے۔")
    },
    {
        "en": ("What has words, but never speaks?", ["A book", "A radio", "A painting", "A phone"], "A book", "A book contains written words, but cannot speak aloud on its own."),
        "ur": ("وہ کیا ہے جس کے اندر بے شمار الفاظ ہیں مگر وہ کبھی بولتی نہیں؟", ["کتاب", "ریڈیو", "تصویر", "دیوار"], "کتاب", "کتاب میں تحریری الفاظ ہوتے ہیں مگر اس کی اپنی آواز نہیں ہوتی۔")
    },
    {
        "en": ("What has one eye, but cannot see anything?", ["A sewing needle", "A storm", "A potato", "A camera"], "A sewing needle", "The small loop at the end of a sewing needle is called an eye."),
        "ur": ("وہ کون سی چیز ہے جس کی ایک آنکھ ہے مگر وہ دیکھ نہیں سکتی؟", ["سوئی", "آلو", "طوفان", "بٹن"], "سوئی", "سوئی کے ناکے (سوراخ) کو اس کی آنکھ کہا جاتا ہے۔")
    },
    {
        "en": ("What can travel around the entire world while staying in a single corner?", ["A postage stamp", "A compass", "A passport", "A suitcase"], "A postage stamp", "A postage stamp stays in the top corner of the envelope during international transit."),
        "ur": ("وہ کون سی چیز ہے جو ایک کونے میں رہتے ہوئے پوری دنیا کا سفر کر لیتی ہے؟", ["ڈاک ٹکٹ", "قطب نما", "پاسپورٹ", "نقشہ"], "ڈاک ٹکٹ", "ڈاک ٹکٹ لفافے کے کونے پر لگ کر دنیا بھر میں سفر کرتا ہے۔")
    },
    {
        "en": ("What has four legs, but cannot walk?", ["A table", "A horse", "A baby", "A lizard"], "A table", "A table has four supporting legs but cannot walk."),
        "ur": ("وہ کون سی چیز ہے جس کی چار ٹانگیں ہیں مگر وہ چل نہیں سکتی؟", ["میز", "کرسی", "پلنگ", "درخت"], "میز", "میز کے چار پائے ہوتے ہیں جن پر وہ ساکن کھڑی رہتی ہے۔")
    },
    {
        "en": ("What has a bed but never sleeps, and a mouth but never talks?", ["A river", "A mountain", "An ocean", "A canyon"], "A river", "A river has a riverbed and river mouth, but is water."),
        "ur": ("وہ کیا ہے جس کا منہ ہے مگر بولتی نہیں، بستر ہے مگر سوتی نہیں؟", ["دریا", "سمندر", "پہاڑ", "کنواں"], "دریا", "دریا کا دہانہ (ماؤتھ) اور پیٹ (بیڈ) ہوتا ہے لیکن وہ پانی کی روانی ہے۔")
    },
    {
        "en": ("What follows you in the sunlight but disappears in the dark?", ["Your shadow", "Your echo", "Your reflection", "Your footprints"], "Your shadow", "A shadow requires light to be cast against a surface."),
        "ur": ("وہ کون سی چیز ہے جو روشنی میں آپ کے ساتھ رہتی ہے مگر اندھیرے میں غائب ہو جاتی ہے؟", ["سایہ", "آئینہ", "تصویر", "عینک"], "سایہ", "سایہ بننے کے لیے روشنی کا ہونا بنیادی شرط ہے۔")
    },
    {
        "en": ("Feed me and I live, but give me water and I die. What am I?", ["Fire", "A sponge", "A desert plant", "An engine"], "Fire", "Fire consumes fuel and oxygen, but water extinguishes it."),
        "ur": ("وہ کیا ہے جسے خوراک دو تو زندہ رہتی ہے مگر پانی پلاتے ہی مر جاتی ہے؟", ["آگ", "پیاس", "اسفنج", "ریت"], "آگ", "آگ لکڑی اور ہوا سے بھڑکتی ہے لیکن پانی سے بجھ جاتی ہے۔")
    },
    {
        "en": ("What runs all the way around a backyard without ever moving?", ["A fence", "A pathway", "A stream", "A dog"], "A fence", "A fence borders the perimeter of a yard while standing completely still."),
        "ur": ("وہ کیا ہے جو پورے باغ کے گرد گھومتی ہے مگر کبھی اپنی جگہ سے نہیں ہلتی؟", ["باڑ (دیوار)", "راستہ", "نہر", "گھاس"], "باڑ (دیوار)", "باڑ باغ کی سرحد پر قائم رہتی ہے بغیر حرکت کیے۔")
    },
    {
        "en": ("What gets sharper the more you use it?", ["Your mind", "A kitchen knife", "A pencil", "A saw"], "Your mind", "Practicing mental puzzles keeps your brain sharp, whereas blades dull with use."),
        "ur": ("وہ کون سی چیز ہے جسے جتنا زیادہ استعمال کرو وہ اتنی ہی تیز ہوتی ہے؟", ["انسانی دماغ", "چھری", "پنسل", "آری"], "انسانی دماغ", "دماغی مشقوں اور علم سے ذہانت مزید نکھرتی ہے۔")
    },
    {
        "en": ("What belongs to you, but other people use it far more than you do?", ["Your name", "Your phone", "Your shoes", "Your money"], "Your name", "Other people address you by your name constantly."),
        "ur": ("وہ کیا ہے جو آپ کی اپنی ملکیت ہے مگر دوسرے لوگ اسے آپ سے زیادہ استعمال کرتے ہیں؟", ["آپ کا نام", "آپ کا فون", "آپ کے جوتے", "آپ کا قلم"], "آپ کا نام", "لوگ آپ کو مخاطب کرنے کے لیے آپ کا نام پکارتے ہیں۔")
    },
    {
        "en": ("What has many keys, but cannot unlock a single door?", ["A piano", "A keychain", "A computer", "A puzzle"], "A piano", "A musical piano has black and white keys that produce musical notes."),
        "ur": ("وہ کون سی چیز ہے جس کے پاس بے شمار چابیاں ہیں مگر وہ کوئی تالہ نہیں کھول سکتی؟", ["پیانو", "کی بورڈ", "الماری", "خزانہ"], "پیانو", "پیانو کی چابیاں (کیز) موسیقی کی دھنیں پیدا کرنے کے لیے ہوتی ہیں۔")
    },
    {
        "en": ("What has cities with no houses, forests with no trees, and rivers with no water?", ["A map", "A painting", "A globe", "A book"], "A map", "A geographical map displays representations of landscapes and boundaries."),
        "ur": ("وہ کون سی جگہ ہے جہاں شہر ہیں مگر مکان نہیں، جنگل ہیں مگر درخت نہیں، دریا ہیں مگر پانی نہیں؟", ["نقشہ", "تصویر", "خواب", "کہانی"], "نقشہ", "نقشہ جغرافیائی خاکہ ہوتا ہے جس پر نشانات بنے ہوتے ہیں۔")
    },
    {
        "en": ("What has a bottom at the top?", ["Your legs", "A cup", "A river", "A mountain"], "Your legs", "Your legs have their bottom (buttocks) at the top end of the limbs."),
        "ur": ("وہ کون سا جسمانی عضو ہے جس کا نچلا حصہ اوپر ہوتا ہے؟", ["ٹانگیں", "ہاتھ", "سر", "گردن"], "ٹانگیں", "ٹانگوں کا اوپری حصہ نیچے کا اختتام کہلاتا ہے۔")
    },
    {
        "en": ("What can fill an entire room without taking up any physical space?", ["Light", "Air", "Water", "Smoke"], "Light", "Light illuminates all corners of a room without occupying volume."),
        "ur": ("وہ کون سی چیز ہے جو پورے کمرے کو بھر دیتی ہے مگر کوئی جگہ نہیں گھیرتی؟", ["روشنی", "ہوا", "دھواں", "خوشبو"], "روشنی", "روشنی ہر کونے میں پھیل جاتی ہے بغیر کوئی ٹھوس جگہ لیے۔")
    },
    {
        "en": ("What has a face and two hands, but no arms or legs?", ["A clock", "A coin", "A mirror", "A mask"], "A clock", "An analog clock dial has a face and hour/minute hands."),
        "ur": ("وہ کیا ہے جس کا چہرہ اور دو ہاتھ ہیں لیکن بازو اور ٹانگیں نہیں؟", ["گھڑی", "آئینہ", "تصویر", "پتلا"], "گھڑی", "گھڑی کا ڈائل اس کا چہرہ اور سوئیاں اس کے ہاتھ کہلاتی ہیں۔")
    },
    {
        "en": ("What can you catch, but never throw?", ["A cold", "A ball", "A fish", "A bus"], "A cold", "You can catch a cold illness, but you cannot physically throw it."),
        "ur": ("وہ کیا ہے جسے آپ پکڑ تو سکتے ہیں مگر واپس پھینک نہیں سکتے؟", ["نزلہ / زکام", "گیند", "مچھلی", "بس"], "نزلہ / زکام", "بیماری یا زکام انسان کو لگ جاتا ہے مگر اسے ہاتھ سے پھینکا نہیں جا سکتا۔")
    },
    {
        "en": ("What begins with T, ends with T, and has T inside it?", ["A teapot", "A tent", "A target", "A toast"], "A teapot", "A teapot starts with 'T', ends with 'T', and holds tea inside."),
        "ur": ("وہ کون سی چیز ہے جس کے نام کا پہلا اور آخری حرف 'ت' ہو اور اس کے اندر چائے ہو؟", ["ترموس / ٹی پاٹ", "تیار چائے", "پیالی", "کیٹلی"], "ترموس / ٹی پاٹ", "ٹی پاٹ کے اندر گرم چائے بھری ہوتی ہے۔")
    },
    {
        "en": ("What has an eye, but cannot see, and moves faster when threaded?", ["A sewing needle", "A storm", "A potato", "A camera"], "A sewing needle", "A needle carries thread through fabric to sew."),
        "ur": ("وہ کیا ہے جس کی آنکھ میں دھاگہ ڈالو تو وہ کپڑے سینے دوڑتی ہے؟", ["سوئی", "مشین", "دھاگہ", "کینچی"], "سوئی", "سوئی کے ناکے میں دھاگہ پرو کر سلائی کی جاتی ہے۔")
    },
    {
        "en": ("What kind of band never plays music?", ["A rubber band", "A marching band", "A rock band", "A jazz band"], "A rubber band", "A rubber band is an elastic loop used to hold objects together."),
        "ur": ("وہ کون سا بینڈ ہے جو کبھی کوئی گانا یا موسیقی نہیں بجاتا؟", ["ربڑ بینڈ", "فوجی بینڈ", "میوزک بینڈ", "گلوکار"], "ربڑ بینڈ", "ربڑ بینڈ چیزوں کو باندھنے والی لچکدار ڈوری ہوتی ہے۔")
    },
    {
        "en": ("What building has the most stories in the entire world?", ["A public library", "A skyscraper", "A hospital", "A university"], "A public library", "A library contains thousands of published storybooks."),
        "ur": ("وہ کون سی عمارت ہے جس کے اندر دنیا کی سب سے زیادہ کہانیاں (منزلیں) ہوتی ہیں؟", ["لائبریری (کتب خانہ)", "بلند و بالا عمارت", "ہسپتال", "اسکول"], "لائبریری (کتب خانہ)", "کتب خانے میں ہزاروں کہانیوں کی کتابیں موجود ہوتی ہیں۔")
    },
    {
        "en": ("What is so fragile that saying its name breaks it?", ["Silence", "Glass", "A bubble", "A secret"], "Silence", "Speaking any word instantly breaks the silence."),
        "ur": ("وہ کون سی چیز ہے جو اتنی نازک ہے کہ اس کا نام لیتے ہی وہ ٹوٹ جاتی ہے؟", ["خاموشی", "شیشہ", "بلبلہ", "راز"], "خاموشی", "زبان سے ایک لفظ بولتے ہی خاموشی ختم ہو جاتی ہے۔")
    },
    {
        "en": ("What has a ring, but no finger?", ["A telephone", "A bell", "A circus", "A planet"], "A telephone", "A telephone rings when an incoming call arrives."),
        "ur": ("وہ کیا ہے جس کی گھنٹی بجتی ہے مگر وہ کوئی انگوٹھی نہیں پہنتا؟", ["ٹیلی فون", "دروازہ", "سائیکل", "گھڑی"], "ٹیلی فون", "فون کال آنے پر فون کی گھنٹی بجتی ہے۔")
    },
    {
        "en": ("If you have me, you want to share me; if you share me, you haven't got me. What am I?", ["A secret", "Money", "Knowledge", "Love"], "A secret", "Once a secret is shared, it is no longer a secret kept to yourself."),
        "ur": ("وہ کیا ہے جو آپ کے پاس ہو تو آپ دوسروں کو بتانا چاہتے ہیں، مگر بتاتے ہی وہ آپ کے پاس نہیں رہتا؟", ["راز", "دولت", "علم", "خوشی"], "راز", "راز کسی کو بتا دیا جائے تو وہ پوشیدہ راز نہیں رہتا۔")
    },
    {
        "en": ("What goes through cities and over hills, but never moves?", ["A road", "A river", "The wind", "A train"], "A road", "Paved roads stretch across geographic landscapes without changing location."),
        "ur": ("وہ کیا ہے جو شہروں، پہاڑوں اور میدانوں سے گزرتی ہے مگر کبھی حرکت نہیں کرتی؟", ["سڑک", "ندی", "ہوا", "ریل"], "سڑک", "سڑک دور دور تک پھیلی رہتی ہے مگر خود ساکن ہوتی ہے۔")
    },
    {
        "en": ("What can be cracked, made, told, and played?", ["A joke", "A nut", "A puzzle", "A record"], "A joke", "You crack a joke, make a joke, tell a joke, and play a practical joke."),
        "ur": ("وہ کیا ہے جسے بنایا بھی جاتا ہے، سنایا بھی جاتا ہے اور سن کر ہنسی بھی آتی ہے؟", ["لطیفہ", "کہانی", "پہیلی", "گانا"], "لطیفہ", "لطیفہ ہنسی مذاق کے لیے کہا اور سنایا جاتا ہے۔")
    },
    {
        "en": ("What has a head, a foot, and four legs, but no body?", ["A bed", "A table", "A chair", "A dog"], "A bed", "A bed has a headboard, a footboard, and four support legs."),
        "ur": ("وہ کیا ہے جس کا سرہانہ اور پائینتی ہے اور چار پائے ہیں مگر کوئی دھڑ نہیں؟", ["پلنگ (چارپائی)", "کرسی", "میز", "صوفہ"], "پلنگ (چارپائی)", "چارپائی کا سرہانہ اور پائے ہوتے ہیں جن پر بستر بچھتا ہے۔")
    },
    {
        "en": ("What tastes better than it smells?", ["A tongue", "A flower", "An apple", "A cake"], "A tongue", "Your tongue does the tasting, while its physical odor is unremarkable."),
        "ur": ("وہ کون سا عضو ہے جو خود سونگھ نہیں سکتا مگر ہر چیز کا ذائقہ چکھتا ہے؟", ["زبان", "ناک", "کان", "آنکھ"], "زبان", "زبان سے انسان ہر کھانے کا کھٹا میٹھا ذائقہ پہچانتا ہے۔")
    },
    {
        "en": ("What can you hold without ever using your hands or arms?", ["Your breath", "A cup", "A rope", "A coin"], "Your breath", "You hold your breath using your diaphragm and respiratory lungs."),
        "ur": ("وہ کیا ہے جسے آپ ہاتھ لگائے بغیر بھی روکے رکھ سکتے ہیں؟", ["سانس", "پانی", "روشنی", "ہوا"], "سانس", "انسان اپنے پھیپھڑوں سے سانس روک سکتا ہے۔")
    },
    {
        "en": ("What has bark, but no bite?", ["A tree", "A dog", "A seal", "A canoe"], "A tree", "Trees are covered with outer wood bark, not animal jaws."),
        "ur": ("وہ کیا ہے جس کی چھال تو ہے مگر وہ کبھی کسی کو کاٹ نہیں سکتا؟", ["درخت", "کتا", "شیر", "سانپ"], "درخت", "درخت کا بیرونی تنا چھال کہلاتا ہے۔")
    },
    {
        "en": ("What loses its head in the morning, but gets it back at night?", ["A pillow", "A hat", "A blanket", "A moon"], "A pillow", "You place your head on a pillow at night and lift it off in the morning."),
        "ur": ("وہ کون سی چیز ہے جس پر رات کو سر رکھا جاتا ہے اور صبح سر ہٹا لیا جاتا ہے؟", ["تکیہ", "ٹوپی", "چادر", "چارپائی"], "تکیہ", "انسان رات کو سوتے ہوئے تکیے پر سر رکھتا ہے۔")
    },
    {
        "en": ("What gets bigger the more you take away from it?", ["A hole", "A pile", "A shadow", "A bank balance"], "A hole", "Removing more dirt or material enlarges the hole's dimensions."),
        "ur": ("وہ کیا ہے جس میں سے جتنا زیادہ مادہ نکالو وہ اتنا ہی بڑا ہوتا جاتا ہے؟", ["گڑھا", "ڈھیر", "درخت", "پہاڑ"], "گڑھا", "زمین میں سے مٹی کھود کر نکالنے سے گڑھا وسیع ہو جاتا ہے۔")
    },
    {
        "en": ("What has a spine, but no bones?", ["A book", "A snake", "A jellyfish", "A leaf"], "A book", "The bound edge of a printed book is called its spine."),
        "ur": ("وہ کون سی چیز ہے جس کی پشت (سپائن) تو ہے مگر کوئی ہڈی نہیں؟", ["کتاب", "سانپ", "پتا", "کیڑا"], "کتاب", "کتاب کی جلد کے درمیانی جوڑ کو پشت یا سپائن کہتے ہیں۔")
    },
    {
        "en": ("What runs but never walks, murmurs but never talks?", ["A stream", "A clock", "An engine", "A child"], "A stream", "A water stream runs downhill and produces bubbling murmuring sounds."),
        "ur": ("وہ کیا ہے جو مسلسل بہتی ہے مگر چلتی نہیں، اور گنگناتی ہے مگر بولتی نہیں؟", ["ندی (آبشار)", "ہوا", "گاڑی", "گھڑی"], "ندی (آبشار)", "ندی کا پانی پتھروں پر بہتے ہوئے ترنم کی آواز پیدا کرتا ہے۔")
    },
]

print(f"make_catalog_easy loaded base {len(EASY_ITEMS)} items.")
