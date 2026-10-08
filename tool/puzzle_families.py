# -*- coding: utf-8 -*-
"""
Puzzle families for MindTrap AI question banks.

Each family produces genuinely different questions (different scenario, numbers,
objects and answers) in natural language - never a repeated question with a
"#12" / "(مرحلہ 12)" tag appended. Every family is written natively for English
and Urdu (Urdu is NOT a translation of the English text).

A family returns a list of dicts: {question, options, correctAnswer, explanation}.
"""
import random

DAYS = {
    'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'ur': ['پیر', 'منگل', 'بدھ', 'جمعرات', 'جمعہ', 'ہفتہ', 'اتوار'],
}
NAMES = {
    'en': ['Ali', 'Sara', 'Omar', 'Lina', 'Adam', 'Maya', 'Zain', 'Noor', 'Ravi', 'Emma', 'Leo', 'Hana', 'Sam', 'Aisha', 'Yusuf', 'Mia'],
    'ur': ['علی', 'سارہ', 'عمر', 'لینا', 'آدم', 'مایا', 'زین', 'نور', 'روی', 'ایما', 'لیو', 'ہانا', 'سام', 'عائشہ', 'یوسف', 'میا'],
}
ITEMS = {
    'en': ['apples', 'pencils', 'marbles', 'books', 'oranges', 'stickers', 'coins', 'balloons', 'cookies', 'flowers', 'toy cars', 'eggs'],
    'ur': ['سیب', 'پنسلیں', 'کنچے', 'کتابیں', 'مالٹے', 'اسٹیکر', 'سکے', 'غبارے', 'بسکٹ', 'پھول', 'کھلونا گاڑیاں', 'انڈے'],
}
U = {
    'en': {'km': '{} km', 'kmh': '{} km/h', 'hours': '{} hours', 'minutes': '{} minutes', 'seconds': '{} seconds',
           'years': '{} years', 'coins': '{} coins', 'pos': 'Position {}', 'day': 'Day {}', 'deg': '{}°',
           'legs': '{} legs', 'posts': '{} posts', 'socks': '{} socks', 'children': '{} children',
           'squares': '{} squares', 'handshakes': '{} handshakes', 'digits': '{} digits', 'days': '{} days', 'n': '{}'},
    'ur': {'km': '{} کلومیٹر', 'kmh': '{} کلومیٹر فی گھنٹہ', 'hours': '{} گھنٹے', 'minutes': '{} منٹ', 'seconds': '{} سیکنڈ',
           'years': '{} سال', 'coins': '{} سکے', 'pos': '{} نمبر', 'day': '{} واں دن', 'deg': '{}°',
           'legs': '{} ٹانگیں', 'posts': '{} کھمبے', 'socks': '{} جرابیں', 'children': '{} بچے',
           'squares': '{} مربعے', 'handshakes': '{} مصافحے', 'digits': '{} ہندسے', 'days': '{} دن', 'n': '{}'},
}


def num(v):
    v = float(v)
    return str(int(v)) if v.is_integer() else ('%g' % v)


def numeric(ans, traps, rng, unit, L):
    vals = [ans]
    for t in traps:
        if t is None:
            continue
        if t >= 0 and all(abs(t - x) > 1e-9 for x in vals):
            vals.append(t)
        if len(vals) == 4:
            break
    d = 1
    while len(vals) < 4:
        for c in (ans + d, ans - d):
            if c >= 0 and all(abs(c - x) > 1e-9 for x in vals) and len(vals) < 4:
                vals.append(c)
        d += 1
    rng.shuffle(vals)
    fmt = U[L][unit]
    return [fmt.format(num(v)) for v in vals], fmt.format(num(ans))


def mk(q, opts, ans, exp):
    return {'question': q, 'options': opts, 'correctAnswer': ans, 'explanation': exp}


def pick_days(correct_idx, traps_idx, rng, L):
    idx = [correct_idx % 7]
    for t in traps_idx:
        t %= 7
        if t not in idx:
            idx.append(t)
        if len(idx) == 4:
            break
    k = 1
    while len(idx) < 4:
        c = (correct_idx + k) % 7
        if c not in idx:
            idx.append(c)
        k += 1
    rng.shuffle(idx)
    return [DAYS[L][i] for i in idx], DAYS[L][correct_idx % 7]


# ─────────────────────────────── EASY FAMILIES ───────────────────────────────

def e_sub(L):
    rng = random.Random(101); out = []
    for i in range(45):
        n = NAMES[L][i % 16]; it = ITEMS[L][(i * 5) % 12]
        a = rng.randint(9, 40); b = rng.randint(2, a - 3); r = a - b
        opts, ans = numeric(r, [a + b, b, r + 2], rng, 'n', L)
        if L == 'en':
            q = f"{n} has {a} {it}. {n} gives {b} of them to a friend. How many {it} does {n} have left?"
            e = f"{a} − {b} = {r}."
        else:
            q = f"{n} کے پاس {a} {it} ہیں۔ {n} نے ان میں سے {b} اپنے دوست کو دے دیے۔ اب {n} کے پاس کتنے {it} بچے؟"
            e = f"{a} − {b} = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def e_add(L):
    rng = random.Random(102); out = []
    places_en = ['basket', 'box', 'jar', 'bag', 'drawer', 'bowl']
    places_ur = ['ٹوکری', 'ڈبے', 'مرتبان', 'تھیلے', 'دراز', 'پیالے']
    for i in range(40):
        it = ITEMS[L][(i * 7) % 12]; p = i % 6
        a = rng.randint(5, 45); b = rng.randint(3, 30); r = a + b
        opts, ans = numeric(r, [a - b if a > b else None, r + 10, r - 1], rng, 'n', L)
        if L == 'en':
            q = f"A {places_en[p]} has {a} {it}. Someone puts in {b} more. How many {it} are in the {places_en[p]} now?"
            e = f"{a} + {b} = {r}."
        else:
            q = f"ایک {places_ur[p]} میں {a} {it} ہیں۔ کسی نے اس میں {b} اور ڈال دیے۔ اب اس میں کل کتنے {it} ہیں؟"
            e = f"{a} + {b} = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def e_mul(L):
    rng = random.Random(103); out = []; seen = set()
    while len(out) < 40:
        a = rng.randint(2, 12); b = rng.randint(2, 12)
        if (a, b) in seen:
            continue
        seen.add((a, b)); it = ITEMS[L][len(out) % 12]; r = a * b
        opts, ans = numeric(r, [a + b, r + a, r - b], rng, 'n', L)
        if L == 'en':
            q = f"There are {a} boxes and each box holds {b} {it}. How many {it} are there altogether?"
            e = f"{a} × {b} = {r}."
        else:
            q = f"{a} ڈبے ہیں اور ہر ڈبے میں {b} {it} ہیں۔ کل کتنے {it} ہیں؟"
            e = f"{a} × {b} = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def e_seq(L):
    rng = random.Random(104); out = []; seen = set()
    while len(out) < 40:
        s = rng.randint(1, 30); d = rng.randint(2, 9)
        if (s, d) in seen:
            continue
        seen.add((s, d))
        terms = [s + d * k for k in range(4)]; r = s + d * 4
        opts, ans = numeric(r, [r + 1, r - 1, r + d], rng, 'n', L)
        t = (', ' if L == 'en' else '، ').join(map(str, terms))
        if L == 'en':
            q = f"Which number comes next: {t}, ...?"
            e = f"Each number is {d} more than the one before it."
        else:
            q = f"اگلا عدد کون سا ہوگا: {t}، ...؟"
            e = f"ہر عدد پچھلے عدد سے {d} زیادہ ہے۔"
        out.append(mk(q, opts, ans, e))
    return out


def e_units(L):
    rng = random.Random(105); out = []
    for w in range(2, 21):
        r = 7 * w
        opts, ans = numeric(r, [r + 7, r - 7, 5 * w], rng, 'days', L)
        q = f"How many days are there in {w} weeks?" if L == 'en' else f"{w} ہفتوں میں کتنے دن ہوتے ہیں؟"
        e = f"One week has 7 days, so {w} × 7 = {r}." if L == 'en' else f"ایک ہفتے میں 7 دن ہوتے ہیں، اس لیے {w} × 7 = {r}۔"
        out.append(mk(q, opts, ans, e))
    for d in range(2, 16):
        r = 24 * d
        opts, ans = numeric(r, [12 * d, r + 24, r - 12], rng, 'hours', L)
        q = f"How many hours are there in {d} full days?" if L == 'en' else f"{d} پورے دنوں میں کتنے گھنٹے ہوتے ہیں؟"
        e = f"A day has 24 hours, so {d} × 24 = {r}." if L == 'en' else f"ایک دن میں 24 گھنٹے ہوتے ہیں، اس لیے {d} × 24 = {r}۔"
        out.append(mk(q, opts, ans, e))
    for h in range(2, 13):
        r = 60 * h
        opts, ans = numeric(r, [100 * h, r + 60, r - 30], rng, 'minutes', L)
        q = f"How many minutes are there in {h} hours?" if L == 'en' else f"{h} گھنٹوں میں کتنے منٹ ہوتے ہیں؟"
        e = f"An hour has 60 minutes, so {h} × 60 = {r}." if L == 'en' else f"ایک گھنٹے میں 60 منٹ ہوتے ہیں، اس لیے {h} × 60 = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def e_change(L):
    rng = random.Random(106); out = []; seen = set()
    things_en = ['notebook', 'toy car', 'sandwich', 'bottle of juice', 'kite', 'ice cream', 'pencil box', 'puzzle book']
    things_ur = ['کاپی', 'کھلونا گاڑی', 'سینڈوچ', 'جوس کی بوتل', 'پتنگ', 'آئس کریم', 'پنسل باکس', 'پہیلیوں کی کتاب']
    i = 0
    while len(out) < 32:
        k = i % 8
        p = rng.randint(12, 95)
        if (k, p) in seen:
            p = rng.randint(12, 95)
            if (k, p) in seen:
                continue
        seen.add((k, p))
        pay = 100 if p < 100 else 200; r = pay - p
        opts, ans = numeric(r, [r + 10, r - 10 if r > 10 else None, p], rng, 'coins', L)
        article = 'An' if things_en[k].startswith(('a', 'e', 'i', 'o', 'u')) else 'A'
        if L == 'en':
            q = f"{article} {things_en[k]} costs {p} coins. You pay with {pay} coins. How much change should you get back?"
            e = f"{pay} − {p} = {r} coins."
        else:
            q = f"ایک {things_ur[k]} کی قیمت {p} سکے ہے۔ آپ {pay} سکے دیتے ہیں۔ آپ کو کتنے سکے واپس ملیں گے؟"
            e = f"{pay} − {p} = {r} سکے۔"
        out.append(mk(q, opts, ans, e))
        i += 1
    return out



ODD_GROUPS = [
    (['Apple', 'Banana', 'Mango'], 'Carrot', 'fruits', ['سیب', 'کیلا', 'آم'], 'گاجر', 'پھل'),
    (['Potato', 'Onion', 'Spinach'], 'Grapes', 'vegetables', ['آلو', 'پیاز', 'پالک'], 'انگور', 'سبزیاں'),
    (['Red', 'Blue', 'Green'], 'Circle', 'colors', ['سرخ', 'نیلا', 'سبز'], 'دائرہ', 'رنگ'),
    (['Square', 'Triangle', 'Circle'], 'Purple', 'shapes', ['مربع', 'مثلث', 'دائرہ'], 'جامنی', 'شکلیں'),
    (['Mars', 'Venus', 'Jupiter'], 'Moon', 'planets', ['مریخ', 'زہرہ', 'مشتری'], 'چاند', 'سیارے'),
    (['Sparrow', 'Eagle', 'Parrot'], 'Bat', 'birds', ['چڑیا', 'عقاب', 'طوطا'], 'چمگادڑ', 'پرندے'),
    (['Salmon', 'Tuna', 'Trout'], 'Dolphin', 'fish', ['سالمن', 'ٹونا', 'ٹراؤٹ'], 'ڈولفن', 'مچھلیاں'),
    (['Ant', 'Bee', 'Butterfly'], 'Spider', 'insects', ['چیونٹی', 'شہد کی مکھی', 'تتلی'], 'مکڑی', 'کیڑے (حشرات)'),
    (['January', 'March', 'July'], 'Sunday', 'months', ['جنوری', 'مارچ', 'جولائی'], 'اتوار', 'مہینے'),
    (['Monday', 'Friday', 'Tuesday'], 'April', 'days of the week', ['پیر', 'جمعہ', 'منگل'], 'اپریل', 'ہفتے کے دن'),
    (['Airplane', 'Helicopter', 'Glider'], 'Submarine', 'flying machines', ['ہوائی جہاز', 'ہیلی کاپٹر', 'گلائیڈر'], 'آبدوز', 'اڑنے والی مشینیں'),
    (['Guitar', 'Violin', 'Flute'], 'Hammer', 'musical instruments', ['گٹار', 'وائلن', 'بانسری'], 'ہتھوڑا', 'موسیقی کے ساز'),
    (['Hammer', 'Saw', 'Screwdriver'], 'Piano', 'tools', ['ہتھوڑا', 'آری', 'پیچ کس'], 'پیانو', 'اوزار'),
    (['Iron', 'Copper', 'Gold'], 'Wood', 'metals', ['لوہا', 'تانبا', 'سونا'], 'لکڑی', 'دھاتیں'),
    (['Hand', 'Knee', 'Elbow'], 'Glove', 'body parts', ['ہاتھ', 'گھٹنا', 'کہنی'], 'دستانہ', 'جسم کے اعضاء'),
    (['Chair', 'Table', 'Sofa'], 'Spoon', 'furniture', ['کرسی', 'میز', 'صوفہ'], 'چمچ', 'فرنیچر'),
    (['Spoon', 'Fork', 'Plate'], 'Pillow', 'kitchen items', ['چمچ', 'کانٹا', 'پلیٹ'], 'تکیہ', 'باورچی خانے کی چیزیں'),
    (['Milk', 'Juice', 'Tea'], 'Bread', 'drinks', ['دودھ', 'جوس', 'چائے'], 'روٹی', 'مشروبات'),
    (['Football', 'Cricket', 'Tennis'], 'Painting', 'sports', ['فٹ بال', 'کرکٹ', 'ٹینس'], 'مصوری', 'کھیل'),
    (['4', '8', '12'], '9', 'even numbers', ['4', '8', '12'], '9', 'جفت اعداد'),
    (['3', '7', '11'], '10', 'odd numbers', ['3', '7', '11'], '10', 'طاق اعداد'),
    (['15', '25', '40'], '32', 'multiples of 5', ['15', '25', '40'], '32', '5 کے پہاڑے کے اعداد'),
    (['Winter', 'Summer', 'Spring'], 'Morning', 'seasons', ['سردی', 'گرمی', 'بہار'], 'صبح', 'موسم'),
    (['Asia', 'Africa', 'Europe'], 'Pacific', 'continents', ['ایشیا', 'افریقہ', 'یورپ'], 'بحر الکاہل', 'براعظم'),
    (['Whale', 'Cow', 'Lion'], 'Shark', 'mammals', ['وہیل', 'گائے', 'شیر'], 'شارک', 'ممالیہ جانور'),
    (['Snake', 'Lizard', 'Crocodile'], 'Frog', 'reptiles', ['سانپ', 'چھپکلی', 'مگرمچھ'], 'مینڈک', 'رینگنے والے جانور'),
    (['Doctor', 'Teacher', 'Pilot'], 'Hospital', 'jobs', ['ڈاکٹر', 'استاد', 'پائلٹ'], 'ہسپتال', 'پیشے'),
    (['Rose', 'Tulip', 'Lily'], 'Oak', 'flowers', ['گلاب', 'ٹیولپ', 'سوسن'], 'بلوط', 'پھول'),
    (['Shirt', 'Trousers', 'Jacket'], 'Bucket', 'clothes', ['قمیض', 'پتلون', 'جیکٹ'], 'بالٹی', 'کپڑے'),
    (['Bus', 'Car', 'Truck'], 'Boat', 'road vehicles', ['بس', 'کار', 'ٹرک'], 'کشتی', 'سڑک پر چلنے والی گاڑیاں'),
]


def e_odd(L):
    rng = random.Random(107); out = []
    for g in ODD_GROUPS:
        same, odd, cat = (g[0], g[1], g[2]) if L == 'en' else (g[3], g[4], g[5])
        opts = list(same) + [odd]; rng.shuffle(opts)
        if L == 'en':
            q = f"Which one does not belong: {', '.join(opts)}?"
            e = f"All the others are {cat}, but {odd} is not."
        else:
            q = f"ان میں سے کون سا باقیوں سے مختلف ہے: {'، '.join(opts)}؟"
            e = f"باقی سب {cat} ہیں، مگر {odd} نہیں۔"
        out.append(mk(q, opts, odd, e))
    return out


def e_half(L):
    rng = random.Random(108); out = []
    for x in range(22, 222, 8):
        r = x // 2
        opts, ans = numeric(r, [x * 2, r + 2, r - 2], rng, 'n', L)
        q = f"What is half of {x}?" if L == 'en' else f"{x} کا آدھا کتنا ہوتا ہے؟"
        e = f"{x} ÷ 2 = {r}." if L == 'en' else f"{x} ÷ 2 = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


# ────────────────────────────── NORMAL FAMILIES ──────────────────────────────

def n_dayoff(L):
    rng = random.Random(201); out = []; seen = set()
    while len(out) < 50:
        d = rng.randint(0, 6); k = rng.randint(3, 60)
        if (d, k) in seen or k % 7 == 0:
            continue
        seen.add((d, k)); c = d + k
        opts, ans = pick_days(c, [c - 1, c + 1, d + (k % 10)], rng, L)
        if L == 'en':
            q = f"If today is {DAYS[L][d]}, what day of the week will it be in {k} days?"
            e = f"{k} days = {k // 7} full weeks and {k % 7} extra days, so it will be {ans}."
        else:
            q = f"اگر آج {DAYS[L][d]} ہے تو {k} دن بعد کون سا دن ہوگا؟"
            e = f"{k} دن = {k // 7} پورے ہفتے اور {k % 7} اضافی دن، اس لیے اس دن {ans} ہوگا۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_seq(L):
    rng = random.Random(202); out = []; seen = set()
    sep = ', ' if L == 'en' else '، '
    # geometric
    for s in range(1, 7):
        for r in range(2, 5):
            terms = [s * r ** k for k in range(4)]; nxt = s * r ** 4
            opts, ans = numeric(nxt, [terms[-1] + (terms[-1] - terms[-2]), nxt + r, nxt - s], rng, 'n', L)
            q = (f"What is the next number in this pattern: {sep.join(map(str, terms))}, ...?" if L == 'en'
                 else f"اس ترتیب میں اگلا عدد کیا ہے: {sep.join(map(str, terms))}، ...؟")
            e = f"Each number is multiplied by {r}." if L == 'en' else f"ہر عدد کو {r} سے ضرب دی گئی ہے۔"
            out.append(mk(q, opts, ans, e))
    # squares
    for k in range(1, 16):
        terms = [(k + i) ** 2 for i in range(4)]; nxt = (k + 4) ** 2
        opts, ans = numeric(nxt, [terms[-1] + (terms[-1] - terms[-2]), nxt + 1, nxt - 2], rng, 'n', L)
        q = (f"Continue the pattern: {sep.join(map(str, terms))}, ...?" if L == 'en'
             else f"اس سلسلے کو آگے بڑھائیں: {sep.join(map(str, terms))}، ...؟")
        e = (f"These are square numbers: {k + 4} × {k + 4} = {nxt}." if L == 'en'
             else f"یہ مربع اعداد ہیں: {k + 4} × {k + 4} = {nxt}۔")
        out.append(mk(q, opts, ans, e))
    # growing gaps
    while len(out) < 70:
        a = rng.randint(1, 20); d = rng.randint(1, 5)
        if (a, d) in seen:
            continue
        seen.add((a, d))
        terms = [a]
        for i in range(4):
            terms.append(terms[-1] + d + i)
        nxt = terms[-1] + d + 4
        opts, ans = numeric(nxt, [terms[-1] + d + 3, nxt + 1, nxt + 2], rng, 'n', L)
        q = (f"Find the next number: {sep.join(map(str, terms))}, ...?" if L == 'en'
             else f"اگلا عدد معلوم کریں: {sep.join(map(str, terms))}، ...؟")
        e = (f"The gap grows by 1 each time ({d}, {d + 1}, {d + 2}, {d + 3}, then {d + 4})." if L == 'en'
             else f"ہر بار فرق 1 بڑھ جاتا ہے ({d}، {d + 1}، {d + 2}، {d + 3}، پھر {d + 4})۔")
        out.append(mk(q, opts, ans, e))
    return out


def n_fib(L):
    rng = random.Random(203); out = []; seen = set()
    sep = ', ' if L == 'en' else '، '
    while len(out) < 30:
        a = rng.randint(1, 9); b = rng.randint(a, 15)
        if (a, b) in seen:
            continue
        seen.add((a, b))
        t = [a, b]
        for _ in range(3):
            t.append(t[-1] + t[-2])
        nxt = t[-1] + t[-2]
        opts, ans = numeric(nxt, [t[-1] * 2, nxt + 1, t[-1] + (t[-1] - t[-2])], rng, 'n', L)
        q = (f"What comes next in this sequence: {sep.join(map(str, t))}, ...?" if L == 'en'
             else f"اس ترتیب میں آگے کیا آئے گا: {sep.join(map(str, t))}، ...؟")
        e = (f"Each number is the sum of the two before it: {t[-2]} + {t[-1]} = {nxt}." if L == 'en'
             else f"ہر عدد پچھلے دو اعداد کا مجموعہ ہے: {t[-2]} + {t[-1]} = {nxt}۔")
        out.append(mk(q, opts, ans, e))
    return out


def n_legs(L):
    rng = random.Random(204); out = []; seen = set()
    while len(out) < 35:
        c = rng.randint(2, 20); g = rng.randint(1, 12)
        if (c, g) in seen:
            continue
        seen.add((c, g)); r = 2 * c + 4 * g
        opts, ans = numeric(r, [(c + g) * 4, (c + g) * 2, r + 2], rng, 'legs', L)
        if L == 'en':
            q = f"A farmer has {c} chickens and {g} cows. How many legs do all the animals have together?"
            e = f"Chickens: {c} × 2 = {2 * c}. Cows: {g} × 4 = {4 * g}. Total = {r}."
        else:
            q = f"ایک کسان کے پاس {c} مرغیاں اور {g} گائیں ہیں۔ تمام جانوروں کی کل کتنی ٹانگیں ہیں؟"
            e = f"مرغیاں: {c} × 2 = {2 * c}۔ گائیں: {g} × 4 = {4 * g}۔ کل = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_speed(L):
    rng = random.Random(205); out = []; seen = set()
    veh_en = ['bus', 'train', 'car', 'truck', 'cyclist']
    veh_ur = ['بس', 'ٹرین', 'کار', 'ٹرک', 'سائیکل سوار']
    while len(out) < 35:
        v = rng.randrange(15, 95, 5); t = rng.randint(2, 7)
        if (v, t) in seen:
            continue
        seen.add((v, t)); r = v * t; k = len(out) % 5
        opts, ans = numeric(r, [v + t, r + v, r - v], rng, 'km', L)
        if L == 'en':
            q = f"A {veh_en[k]} moves at a steady {v} km/h. How far does it travel in {t} hours?"
            e = f"Distance = speed × time = {v} × {t} = {r} km."
        else:
            q = f"ایک {veh_ur[k]} {v} کلومیٹر فی گھنٹہ کی یکساں رفتار سے چلتی ہے۔ {t} گھنٹوں میں کتنا فاصلہ طے ہوگا؟"
            e = f"فاصلہ = رفتار × وقت = {v} × {t} = {r} کلومیٹر۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_arrive(L):
    rng = random.Random(206); out = []; seen = set()
    while len(out) < 30:
        h = rng.randint(5, 21); d = rng.randint(2, 9)
        if (h, d) in seen:
            continue
        seen.add((h, d)); a = (h + d) % 24
        vals = [a, (a + 1) % 24, (a - 1) % 24, (h + d + 2) % 24]
        vals = list(dict.fromkeys(vals))
        rng.shuffle(vals)
        opts = [f"{v:02d}:00" for v in vals]; ans = f"{a:02d}:00"
        if L == 'en':
            q = f"A train leaves at {h:02d}:00 and the journey takes {d} hours. At what time does it arrive?"
            e = f"{h:02d}:00 + {d} hours = {ans}."
        else:
            q = f"ایک ٹرین {h:02d}:00 بجے روانہ ہوتی ہے اور سفر {d} گھنٹے کا ہے۔ وہ کس وقت پہنچے گی؟"
            e = f"{h:02d}:00 + {d} گھنٹے = {ans}۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_age(L):
    rng = random.Random(207); out = []
    for i in range(35):
        n = NAMES[L][i % 16]; a = rng.randint(5, 30); d = rng.randint(2, 9); k = rng.randint(2, 15)
        r = a + d + k
        opts, ans = numeric(r, [a + k, a + d, r - d + 1 if d > 1 else r + 3], rng, 'years', L)
        if L == 'en':
            q = f"{n} is {a} years old and {n}'s sister is {d} years older. How old will the sister be in {k} years?"
            e = f"The sister is {a + d} now, so in {k} years she will be {r}."
        else:
            q = f"{n} کی عمر {a} سال ہے اور اس کی بہن اس سے {d} سال بڑی ہے۔ {k} سال بعد بہن کی عمر کتنی ہوگی؟"
            e = f"بہن کی موجودہ عمر {a + d} سال ہے، اس لیے {k} سال بعد وہ {r} سال کی ہوگی۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_percent(L):
    rng = random.Random(208); out = []; seen = set()
    ps = [5, 10, 20, 25, 30, 40, 50, 75]
    while len(out) < 35:
        p = rng.choice(ps); x = rng.randrange(40, 880, 20)
        if (p, x) in seen or (x * p) % 100:
            continue
        seen.add((p, x)); r = x * p // 100
        opts, ans = numeric(r, [r * 2, x - r, r + 5], rng, 'n', L)
        q = f"What is {p}% of {x}?" if L == 'en' else f"{x} کا {p}% کتنا ہوتا ہے؟"
        e = f"{x} × {p} ÷ 100 = {r}." if L == 'en' else f"{x} × {p} ÷ 100 = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_handshake(L):
    rng = random.Random(209); out = []
    for n in range(4, 22):
        r = n * (n - 1) // 2
        opts, ans = numeric(r, [n * (n - 1), n * n // 2, r + n], rng, 'handshakes', L)
        if L == 'en':
            q = f"At a meeting of {n} people, everyone shakes hands with everyone else exactly once. How many handshakes happen?"
            e = f"Each pair shakes once: {n} × {n - 1} ÷ 2 = {r}."
        else:
            q = f"ایک ملاقات میں {n} لوگ ہیں اور ہر شخص باقی ہر شخص سے صرف ایک بار ہاتھ ملاتا ہے۔ کل کتنے مصافحے ہوں گے؟"
            e = f"ہر جوڑا ایک بار ہاتھ ملاتا ہے: {n} × {n - 1} ÷ 2 = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_meet(L):
    rng = random.Random(210); out = []; seen = set()
    while len(out) < 30:
        t = rng.randint(2, 6); v1 = rng.randrange(20, 90, 10); v2 = rng.randrange(20, 90, 10)
        if (t, v1, v2) in seen:
            continue
        seen.add((t, v1, v2)); d = t * (v1 + v2)
        opts, ans = numeric(t, [t + 1, t * 2, t - 1 if t > 1 else None], rng, 'hours', L)
        if L == 'en':
            q = f"Two cars start {d} km apart and drive toward each other at {v1} km/h and {v2} km/h. After how many hours do they meet?"
            e = f"They close the gap at {v1} + {v2} = {v1 + v2} km/h, so {d} ÷ {v1 + v2} = {t} hours."
        else:
            q = f"دو کاریں ایک دوسرے سے {d} کلومیٹر دور ہیں اور {v1} اور {v2} کلومیٹر فی گھنٹہ کی رفتار سے ایک دوسرے کی طرف آتی ہیں۔ کتنے گھنٹوں بعد وہ ملیں گی؟"
            e = f"دونوں مل کر {v1 + v2} کلومیٹر فی گھنٹہ سے فاصلہ کم کرتی ہیں، اس لیے {d} ÷ {v1 + v2} = {t} گھنٹے۔"
        out.append(mk(q, opts, ans, e))
    return out


WEIGHT_PAIRS = [
    ('feathers', 'iron', 'پروں', 'لوہے'), ('cotton', 'stones', 'روئی', 'پتھروں'), ('sand', 'gold', 'ریت', 'سونے'),
    ('popcorn', 'bricks', 'پاپ کارن', 'اینٹوں'), ('paper', 'steel', 'کاغذ', 'فولاد'), ('leaves', 'rocks', 'پتوں', 'چٹانوں'),
    ('wool', 'copper', 'اون', 'تانبے'), ('sugar', 'salt', 'چینی', 'نمک'), ('rice', 'nails', 'چاول', 'کیلوں'),
    ('ice', 'water', 'برف', 'پانی'), ('tomatoes', 'potatoes', 'ٹماٹروں', 'آلوؤں'), ('bread', 'marble', 'روٹی', 'سنگ مرمر'),
    ('flour', 'lead', 'آٹے', 'سیسے'), ('grapes', 'coins', 'انگوروں', 'سکوں'), ('sponges', 'bananas', 'اسفنج', 'کیلوں کے گچھوں'),
]


def n_weight(L):
    rng = random.Random(211); out = []
    for i, (a, b, ua, ub) in enumerate(WEIGHT_PAIRS):
        x = [1, 2, 5, 10, 20, 50, 100, 3, 7, 25, 15, 40, 4, 8, 12][i]
        if L == 'en':
            opts = [f"{x} kg of {a}", f"{x} kg of {b}", "Both weigh the same", "It depends on the size"]
            ans = "Both weigh the same"
            q = f"Which is heavier: {x} kg of {a} or {x} kg of {b}?"
            e = f"Both are exactly {x} kg - a kilogram is a kilogram, whatever it is made of."
        else:
            opts = [f"{x} کلو {ua}", f"{x} کلو {ub}", "دونوں کا وزن برابر ہے", "یہ حجم پر منحصر ہے"]
            ans = "دونوں کا وزن برابر ہے"
            q = f"کون زیادہ بھاری ہے: {x} کلو {ua} یا {x} کلو {ub}؟"
            e = f"دونوں کا وزن بالکل {x} کلو ہے، چیز چاہے کوئی بھی ہو۔"
        rng.shuffle(opts)
        out.append(mk(q, opts, ans, e))
    return out


def n_sum(L):
    rng = random.Random(212); out = []
    for n in list(range(10, 101, 3))[:30]:
        r = n * (n + 1) // 2
        opts, ans = numeric(r, [n * n // 2, r + n, r - n], rng, 'n', L)
        q = (f"What is the sum of all whole numbers from 1 to {n}?" if L == 'en'
             else f"1 سے {n} تک تمام اعداد کا مجموعہ کتنا ہے؟")
        e = (f"Use n × (n + 1) ÷ 2: {n} × {n + 1} ÷ 2 = {r}." if L == 'en'
             else f"فارمولا n × (n + 1) ÷ 2: {n} × {n + 1} ÷ 2 = {r}۔")
        out.append(mk(q, opts, ans, e))
    return out


def n_calendar(L):
    rng = random.Random(213); out = []; seen = set()
    while len(out) < 30:
        d = rng.randint(0, 6); k = rng.randint(9, 31)
        if (d, k) in seen or (k - 1) % 7 == 0:
            continue
        seen.add((d, k)); c = d + (k - 1)
        opts, ans = pick_days(c, [c + 1, c - 1, d + k], rng, L)
        if L == 'en':
            q = f"If the 1st of a month falls on a {DAYS[L][d]}, which day of the week is day {k} of that month?"
            e = f"Day {k} is {k - 1} days after the 1st; {k - 1} = {(k - 1) // 7} weeks + {(k - 1) % 7} days, so it is {ans}."
        else:
            q = f"اگر کسی مہینے کی پہلی تاریخ کو {DAYS[L][d]} ہو تو اسی مہینے کی {k} تاریخ کو کون سا دن ہوگا؟"
            e = f"{k} تاریخ پہلی تاریخ کے {k - 1} دن بعد ہے؛ {k - 1} = {(k - 1) // 7} ہفتے + {(k - 1) % 7} دن، اس لیے {ans}۔"
        out.append(mk(q, opts, ans, e))
    return out


def n_even(L):
    rng = random.Random(214); out = []
    for n in range(15, 100, 4):
        r = n // 2
        opts, ans = numeric(r, [r + 1, n - r + 1 if n % 2 else r - 1, r + 2], rng, 'n', L)
        q = f"How many even numbers are there from 1 to {n}?" if L == 'en' else f"1 سے {n} تک کتنے جفت اعداد ہیں؟"
        e = (f"Every second number is even, so there are {r}." if L == 'en'
             else f"ہر دوسرا عدد جفت ہوتا ہے، اس لیے کل {r} ہیں۔")
        out.append(mk(q, opts, ans, e))
    return out


# ────────────────────────────── TRICKY FAMILIES ──────────────────────────────

def t_fence(L):
    rng = random.Random(301); out = []; seen = set()
    while len(out) < 30:
        g = rng.choice([2, 3, 4, 5, 6, 10]); k = rng.randint(4, 20); Ln = g * k
        if (g, k) in seen:
            continue
        seen.add((g, k)); r = k + 1
        opts, ans = numeric(r, [k, k + 2, k - 1], rng, 'posts', L)
        if L == 'en':
            q = f"A straight fence is {Ln} meters long with a post every {g} meters, including one at each end. How many posts are there?"
            e = f"{Ln} ÷ {g} = {k} gaps, and a fence always has one more post than gaps: {r}."
        else:
            q = f"ایک سیدھی باڑ {Ln} میٹر لمبی ہے اور ہر {g} میٹر پر ایک کھمبا لگا ہے، دونوں سروں سمیت۔ کل کتنے کھمبے ہیں؟"
            e = f"{Ln} ÷ {g} = {k} وقفے، اور کھمبے ہمیشہ وقفوں سے ایک زیادہ ہوتے ہیں: {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_cut(L):
    rng = random.Random(302); out = []; seen = set()
    while len(out) < 30:
        t = rng.randint(2, 12); k = rng.randint(3, 10)
        if (t, k) in seen:
            continue
        seen.add((t, k)); r = t * (k - 1)
        opts, ans = numeric(r, [t * k, t * k // 2, r + t], rng, 'minutes', L)
        if L == 'en':
            q = f"It takes {t} minutes to cut a log into 2 pieces. How many minutes does it take to cut an identical log into {k} pieces?"
            e = f"2 pieces need 1 cut. {k} pieces need {k - 1} cuts: {k - 1} × {t} = {r} minutes."
        else:
            q = f"ایک لکڑی کے 2 ٹکڑے کرنے میں {t} منٹ لگتے ہیں۔ بالکل ویسی ہی لکڑی کے {k} ٹکڑے کرنے میں کتنے منٹ لگیں گے؟"
            e = f"2 ٹکڑوں کے لیے 1 کٹ لگتا ہے۔ {k} ٹکڑوں کے لیے {k - 1} کٹ: {k - 1} × {t} = {r} منٹ۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_stairs(L):
    rng = random.Random(303); out = []; seen = set()
    while len(out) < 25:
        t = rng.randrange(12, 66, 6); k = rng.randint(4, 12)
        if (t, k) in seen:
            continue
        seen.add((t, k)); r = t // 2 * (k - 1)
        opts, ans = numeric(r, [t * k // 3, t * k // 2, r + t // 2], rng, 'seconds', L)
        if L == 'en':
            q = f"Walking up from floor 1 to floor 3 takes {t} seconds. At the same pace, how long does it take to walk from floor 1 to floor {k}?"
            e = f"Floor 1 to 3 is only 2 flights, so each flight takes {t // 2} s. Floor 1 to {k} is {k - 1} flights: {r} s."
        else:
            q = f"پہلی منزل سے تیسری منزل تک سیڑھیاں چڑھنے میں {t} سیکنڈ لگتے ہیں۔ اسی رفتار سے پہلی منزل سے {k} ویں منزل تک کتنا وقت لگے گا؟"
            e = f"پہلی سے تیسری منزل تک صرف 2 زینے ہیں، یعنی ہر زینہ {t // 2} سیکنڈ۔ پہلی سے {k} ویں منزل تک {k - 1} زینے: {r} سیکنڈ۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_socks(L):
    rng = random.Random(304); out = []
    for k in range(2, 12):
        r = k + 1
        opts, ans = numeric(r, [2, 2 * k, k], rng, 'socks', L)
        if L == 'en':
            q = f"A drawer holds socks in {k} different colors, all mixed up. In total darkness, how many socks must you take to be sure of a matching pair?"
            e = f"With {k} socks you might get one of each color; the next one ({r}) must match one of them."
        else:
            q = f"ایک دراز میں {k} مختلف رنگوں کی جرابیں ملی جلی پڑی ہیں۔ مکمل اندھیرے میں یقینی جوڑا بنانے کے لیے کم از کم کتنی جرابیں نکالنی ہوں گی؟"
            e = f"{k} جرابوں میں ہر رنگ کی ایک ایک آ سکتی ہے؛ اگلی ({r}) لازماً کسی سے میچ کرے گی۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_grid(L):
    rng = random.Random(305); out = []
    for n in range(2, 11):
        r = sum(i * i for i in range(1, n + 1))
        opts, ans = numeric(r, [n * n, n * n + 1, r - n], rng, 'squares', L)
        if L == 'en':
            q = f"How many squares of all sizes can you find on a {n} × {n} grid?"
            e = f"Count every size: 1² + 2² + ... + {n}² = {r}."
        else:
            q = f"{n} × {n} کے خانوں والے جال میں ہر سائز کے کل کتنے مربعے ہیں؟"
            e = f"ہر سائز گنیں: 1² + 2² + ... + {n}² = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


BB_PAIRS = [('notebook', 'pen', 'کاپی', 'قلم'), ('bat', 'ball', 'بلا', 'گیند'), ('cup', 'saucer', 'کپ', 'طشتری'),
            ('shirt', 'cap', 'قمیض', 'ٹوپی'), ('school bag', 'ruler', 'بستہ', 'فٹا'), ('book', 'bookmark', 'کتاب', 'بک مارک'),
            ('kite', 'string', 'پتنگ', 'ڈور'), ('lamp', 'bulb', 'لیمپ', 'بلب')]


def t_batball(L):
    rng = random.Random(306); out = []; seen = set()
    while len(out) < 32:
        b = rng.randint(5, 60); D = rng.randrange(20, 210, 10); p = BB_PAIRS[len(out) % len(BB_PAIRS)]
        if (b, D) in seen:
            continue
        seen.add((b, D)); T = 2 * b + D
        opts, ans = numeric(b, [T - D, b + 5, (T - D) // 2 + D], rng, 'coins', L)
        if L == 'en':
            A, B = p[0], p[1]
            q = f"A {A} and a {B} cost {T} coins together. The {A} costs {D} coins more than the {B}. How much does the {B} cost?"
            e = f"If the {B} is {b}, the {A} is {b + D}; together {b} + {b + D} = {T}. The quick answer {T - D} is the trap."
        else:
            A, B = p[2], p[3]
            q = f"ایک {A} اور ایک {B} کی کل قیمت {T} سکے ہے۔ {A} کی قیمت {B} سے {D} سکے زیادہ ہے۔ {B} کی قیمت کتنی ہے؟"
            e = f"اگر {B} {b} سکے کا ہو تو {A} {b + D} کا ہوگا؛ دونوں مل کر {T}۔ فوری جواب {T - D} ایک جال ہے۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_machines(L):
    rng = random.Random(307); out = []; seen = set()
    while len(out) < 30:
        m = rng.randint(3, 12); k = rng.choice([20, 30, 40, 50, 60, 80, 100, 120, 150, 200])
        if (m, k) in seen:
            continue
        seen.add((m, k))
        opts, ans = numeric(m, [k, m * 2, k // m if k // m != m else None], rng, 'minutes', L)
        if L == 'en':
            q = f"If {m} machines make {m} toys in {m} minutes, how many minutes would {k} machines need to make {k} toys?"
            e = f"Each machine makes one toy in {m} minutes, so {k} machines make {k} toys in the same {m} minutes."
        else:
            q = f"اگر {m} مشینیں {m} منٹ میں {m} کھلونے بناتی ہیں تو {k} مشینوں کو {k} کھلونے بنانے میں کتنے منٹ لگیں گے؟"
            e = f"ہر مشین {m} منٹ میں ایک کھلونا بناتی ہے، اس لیے {k} مشینیں بھی {m} منٹ میں ہی {k} کھلونے بنا لیں گی۔"
        out.append(mk(q, opts, ans, e))
    return out


LILY = [('water lilies', 'pond', 'کنول کے پتے', 'تالاب'), ('green algae', 'lake', 'سبز کائی', 'جھیل'),
        ('mold', 'slice of bread', 'پھپھوندی', 'ڈبل روٹی کے ٹکڑے'), ('moss', 'large rock', 'کائی', 'بڑی چٹان'),
        ('ivy', 'wall', 'بیل', 'دیوار'), ('frost', 'window', 'کہر', 'کھڑکی')]


def t_lily(L):
    rng = random.Random(308); out = []
    days = list(range(12, 61)); rng.shuffle(days)
    for i, d in enumerate(days[:36]):
        th = LILY[i % len(LILY)]
        opts, ans = numeric(d - 1, [d // 2, d - 2, d // 2 + 1], rng, 'day', L)
        if L == 'en':
            q = f"A patch of {th[0]} doubles in size every day. It fully covers the {th[1]} on day {d}. On which day was the {th[1]} half covered?"
            e = f"Because it doubles daily, one day before full coverage it was half: day {d - 1}."
        else:
            q = f"{th[2]} ہر روز دگنی ہو جاتی ہے۔ {d} ویں دن پورا {th[3]} ڈھک جاتا ہے۔ کس دن آدھا {th[3]} ڈھکا ہوا تھا؟"
            e = f"چونکہ ہر روز دگنا ہوتا ہے، اس لیے مکمل ہونے سے ایک دن پہلے آدھا تھا: {d - 1} واں دن۔"
        out.append(mk(q, opts, ans, e))
    return out


AVG = [(30, 60), (40, 60), (20, 30), (60, 90), (12, 24), (10, 40), (30, 70), (40, 120), (45, 90), (24, 40),
       (15, 30), (36, 45), (60, 120), (30, 45), (20, 80), (50, 75)]


def t_avgspeed(L):
    rng = random.Random(309); out = []
    for v1, v2 in AVG:
        r = 2 * v1 * v2 / (v1 + v2)
        opts, ans = numeric(r, [(v1 + v2) / 2, r + 5, v1 + v2], rng, 'kmh', L)
        if L == 'en':
            q = f"You drive to a town at {v1} km/h and come back the same way at {v2} km/h. What is your average speed for the whole trip?"
            e = f"You spend longer at the slower speed, so it is not {num((v1 + v2) / 2)}. Average = 2 × {v1} × {v2} ÷ ({v1} + {v2}) = {num(r)} km/h."
        else:
            q = f"آپ ایک شہر تک {v1} کلومیٹر فی گھنٹہ سے جاتے ہیں اور اسی راستے سے {v2} کلومیٹر فی گھنٹہ سے واپس آتے ہیں۔ پورے سفر کی اوسط رفتار کیا ہے؟"
            e = f"سست رفتار پر زیادہ وقت لگتا ہے، اس لیے جواب {num((v1 + v2) / 2)} نہیں۔ اوسط = 2 × {v1} × {v2} ÷ ({v1} + {v2}) = {num(r)}۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_updown(L):
    rng = random.Random(310); out = []
    things_en = ['jacket', 'bicycle', 'phone', 'watch', 'lamp', 'backpack']
    things_ur = ['جیکٹ', 'سائیکل', 'فون', 'گھڑی', 'لیمپ', 'بستے']
    i = 0
    for x in [100, 200, 400, 500, 800, 1000]:
        for p in [10, 20, 25, 50]:
            r = x * (100 + p) * (100 - p) / 10000
            opts, ans = numeric(r, [x, x + x * p / 100 * 0.5, r - x * p / 100], rng, 'coins', L)
            if L == 'en':
                q = f"A {things_en[i % 6]} costs {x} coins. Its price rises by {p}%, then the new price falls by {p}%. What is the final price?"
                e = f"Up: {num(x * (100 + p) / 100)}. Down {p}% of that: {num(r)}. It does not return to {x}."
            else:
                q = f"ایک {things_ur[i % 6]} کی قیمت {x} سکے ہے۔ قیمت {p}% بڑھتی ہے، پھر نئی قیمت {p}% کم ہو جاتی ہے۔ آخری قیمت کیا ہے؟"
                e = f"بڑھنے کے بعد: {num(x * (100 + p) / 100)}۔ اس کا {p}% کم: {num(r)}۔ قیمت واپس {x} نہیں ہوتی۔"
            out.append(mk(q, opts, ans, e)); i += 1
    return out


def t_clock(L):
    rng = random.Random(311); out = []; combos = []
    for h in range(1, 12):
        for m in (10, 20, 30, 40, 50):
            combos.append((h, m))
    rng.shuffle(combos)
    for h, m in combos[:40]:
        a = abs(30 * h - 5.5 * m); a = min(a, 360 - a)
        wrong = abs(30 * h - 6 * m); wrong = min(wrong, 360 - wrong)
        opts, ans = numeric(a, [wrong, a + 15, abs(a - 30)], rng, 'deg', L)
        if L == 'en':
            q = f"What is the smaller angle between the hour hand and the minute hand at {h}:{m:02d}?"
            e = f"The hour hand also moves: 30 × {h} + 0.5 × {m} vs 6 × {m}. The difference is {num(a)}°."
        else:
            q = f"{h}:{m:02d} بجے گھڑی کی گھنٹے والی اور منٹ والی سوئی کے درمیان چھوٹا زاویہ کتنا ہوتا ہے؟"
            e = f"گھنٹے والی سوئی بھی آگے بڑھتی ہے: 30 × {h} + 0.5 × {m} بمقابلہ 6 × {m}۔ فرق {num(a)}° ہے۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_race(L):
    rng = random.Random(312); out = []
    for p in range(2, 12):
        opts, ans = numeric(p, [p - 1, p + 1, 1 if p > 2 else None], rng, 'pos', L)
        if L == 'en':
            q = f"In a race, you overtake the runner who is in position {p}. What position are you in now?"
            e = f"You take that runner's place, so you are now in position {p}, not {p - 1}."
        else:
            q = f"ایک دوڑ میں آپ {p} نمبر پر دوڑنے والے کو پیچھے چھوڑ دیتے ہیں۔ اب آپ کس نمبر پر ہیں؟"
            e = f"آپ نے اسی کی جگہ لی ہے، اس لیے اب آپ {p} نمبر پر ہیں، {p - 1} پر نہیں۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_dayrel(L):
    rng = random.Random(313); out = []
    D = DAYS[L]
    for d in range(7):
        opts, ans = pick_days(d - 3, [d - 1, d - 2, d + 1], rng, L)
        q = (f"If the day after tomorrow is {D[d]}, what day was yesterday?" if L == 'en'
             else f"اگر پرسوں {D[d]} ہے تو کل گزرا ہوا دن کون سا تھا؟")
        e = (f"Day after tomorrow = today + 2, yesterday = today − 1: a 3-day gap back from {D[d]} gives {ans}." if L == 'en'
             else f"پرسوں = آج + 2، گزرا کل = آج − 1؛ {D[d]} سے 3 دن پیچھے: {ans}۔")
        out.append(mk(q, opts, ans, e))
    for d in range(7):
        opts, ans = pick_days(d + 3, [d + 2, d + 1, d + 4], rng, L)
        q = (f"If yesterday was {D[d]}, what day will it be the day after tomorrow?" if L == 'en'
             else f"اگر گزرا ہوا کل {D[d]} تھا تو پرسوں کون سا دن ہوگا؟")
        e = (f"From yesterday to the day after tomorrow is 3 days: {ans}." if L == 'en'
             else f"گزرے کل سے پرسوں تک 3 دن کا فرق ہے: {ans}۔")
        out.append(mk(q, opts, ans, e))
    combos = [(d, k) for d in range(7) for k in range(2, 7)]; rng.shuffle(combos)
    for d, k in combos[:16]:
        opts, ans = pick_days(d + k + 1, [d + k, d + k + 2, d + 1], rng, L)
        q = (f"If {k} days ago it was {D[d]}, what day will it be tomorrow?" if L == 'en'
             else f"اگر {k} دن پہلے {D[d]} تھا تو آنے والا کل کون سا دن ہوگا؟")
        e = (f"{D[d]} + {k} days is today, and one more day is tomorrow: {ans}." if L == 'en'
             else f"{D[d]} + {k} دن = آج، اور ایک دن مزید = کل: {ans}۔")
        out.append(mk(q, opts, ans, e))
    return out


WORK = [(3, 6), (4, 12), (6, 12), (10, 15), (12, 24), (20, 30), (12, 36), (5, 20), (8, 24), (6, 6), (10, 10),
        (15, 30), (18, 36), (9, 18), (4, 4), (14, 14), (12, 12), (30, 60)]


def t_workers(L):
    rng = random.Random(314); out = []
    jobs_en = ['paint a fence', 'clean a hall', 'fill a tank', 'pack the boxes', 'plant a garden', 'build a wall']
    jobs_ur = ['ایک باڑ پینٹ', 'ایک ہال صاف', 'ایک ٹینکی بھر', 'سارے ڈبے پیک', 'ایک باغ میں پودے لگا', 'ایک دیوار تعمیر']
    for i, (a, b) in enumerate(WORK):
        r = a * b / (a + b)
        opts, ans = numeric(r, [(a + b) / 2, a + b, min(a, b) - 1 if min(a, b) > 2 else None], rng, 'hours', L)
        if L == 'en':
            q = f"One worker can {jobs_en[i % 6]} in {a} hours and another can do it in {b} hours. Working together, how many hours will it take?"
            e = f"Rates add up: 1/{a} + 1/{b} per hour, so together it takes {a} × {b} ÷ ({a} + {b}) = {num(r)} hours."
        else:
            q = f"ایک مزدور {a} گھنٹوں میں اور دوسرا {b} گھنٹوں میں {jobs_ur[i % 6]} کر سکتا ہے۔ دونوں مل کر کتنے گھنٹوں میں یہ کام کریں گے؟"
            e = f"رفتاریں جمع ہوتی ہیں: {a} × {b} ÷ ({a} + {b}) = {num(r)} گھنٹے۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_pills(L):
    rng = random.Random(315); out = []; seen = set()
    while len(out) < 25:
        n = rng.randint(3, 9); m = rng.choice([10, 15, 20, 30, 45, 60])
        if (n, m) in seen:
            continue
        seen.add((n, m)); r = (n - 1) * m
        opts, ans = numeric(r, [n * m, r - m, r + m], rng, 'minutes', L)
        if L == 'en':
            q = f"A doctor gives you {n} pills and tells you to take one every {m} minutes, starting right now. How many minutes until you take the last one?"
            e = f"The first pill is at minute 0, so only {n - 1} waits remain: {n - 1} × {m} = {r} minutes."
        else:
            q = f"ڈاکٹر آپ کو {n} گولیاں دیتا ہے اور کہتا ہے کہ ابھی سے ہر {m} منٹ بعد ایک گولی کھائیں۔ آخری گولی کتنے منٹ بعد کھائی جائے گی؟"
            e = f"پہلی گولی فوراً کھائی جاتی ہے، اس لیے صرف {n - 1} وقفے: {n - 1} × {m} = {r} منٹ۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_sisters(L):
    rng = random.Random(316); out = []
    for k in range(2, 12):
        r = k + 1
        opts, ans = numeric(r, [2 * k, k, 2 * k + 1], rng, 'children', L)
        if L == 'en':
            q = f"In a family, each of the {k} sisters has exactly one brother. How many children are there in the family?"
            e = f"All {k} sisters share the same single brother: {k} + 1 = {r}."
        else:
            q = f"ایک خاندان میں {k} بہنیں ہیں اور ہر بہن کا صرف ایک بھائی ہے۔ خاندان میں کل کتنے بچے ہیں؟"
            e = f"تمام {k} بہنوں کا ایک ہی بھائی ہے: {k} + 1 = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


def t_pages(L):
    rng = random.Random(317); out = []
    ns = sorted(rng.sample(range(45, 400), 28))
    for n in ns:
        r = min(n, 9) + 2 * max(0, min(n, 99) - 9) + 3 * max(0, n - 99)
        opts, ans = numeric(r, [n, 2 * n, r + 9], rng, 'digits', L)
        if L == 'en':
            q = f"How many digits do you need to print page numbers 1 to {n} in a book?"
            e = f"Pages 1-9 use 1 digit, 10-99 use 2, 100+ use 3. Total = {r}."
        else:
            q = f"ایک کتاب کے صفحات پر 1 سے {n} تک نمبر لکھنے کے لیے کل کتنے ہندسے درکار ہوں گے؟"
            e = f"صفحات 1-9 پر 1 ہندسہ، 10-99 پر 2، اور 100 سے آگے 3۔ کل = {r}۔"
        out.append(mk(q, opts, ans, e))
    return out


EASY = [e_sub, e_add, e_mul, e_seq, e_units, e_change, e_odd, e_half]
NORMAL = [n_dayoff, n_seq, n_fib, n_legs, n_speed, n_arrive, n_age, n_percent, n_handshake, n_meet, n_weight, n_sum, n_calendar, n_even]
TRICKY = [t_fence, t_cut, t_stairs, t_socks, t_grid, t_batball, t_machines, t_lily, t_avgspeed, t_updown, t_clock,
          t_race, t_dayrel, t_workers, t_pills, t_sisters, t_pages]
