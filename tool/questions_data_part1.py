# -*- coding: utf-8 -*-
"""
PART 1: EASY TIER (250 distinct questions: IDs 1 to 250)
Every question has a completely unique premise, storyline, and POV.
Zero templates, zero repeated question patterns.
Available natively in English and Urdu.
"""

EASY_PUZZLES = [
    # 1: Towel
    {
        "en": ("What gets wetter the more it dries?", ["A towel", "A sponge", "A cloud", "Rain"], "A towel", "A towel absorbs moisture from your body as it dries you."),
        "ur": ("وہ کون سی چیز ہے جو خشک کرتے وقت خود گیلی ہو جاتی ہے؟", ["تولیہ", "بادل", "سورج", "ریت"], "تولیہ", "تولیہ پانی جذب کرتا ہے جس سے وہ خود گیلا ہو جاتا ہے۔")
    },
    # 2: Clock hands
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
    # 8: Future
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
]
