# -*- coding: utf-8 -*-
"""
Tricky Batch 2 (55 items: 81-135).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why does Shor's Algorithm running on a theoretical quantum computer pose a critical threat to RSA public-key encryption?",
        ["It finds the prime factors of large integers in polynomial time using quantum Fourier transform", "It guesses passwords at light speed", "It overheats quantum processors", "It disables internet fiber cables"],
        "It finds the prime factors of large integers in polynomial time using quantum Fourier transform",
        "Classical prime factorization scales exponentially, but Shor's algorithm exploits quantum superposition and period finding to solve it in polynomial time O((log N)^3).",
        "شور کا کوانٹم الگورتھم (Shor's Algorithm) موجودہ دور کے محفوظ ترین RSA انکرپشن نظام کے لیے ایک بہت بڑا خطرہ کیوں مانا جاتا ہے؟",
        ["یہ کوانٹم فویئر ٹرانسفارم کے ذریعے بڑے ہندسوں کے پرائم فیکٹرز چند منٹوں میں معلوم کر لیتا ہے", "یہ روشنی کی رفتار سے پاس ورڈ کے تکے لگاتا ہے", "یہ کمپیوٹر کے پروسیسر کو جلا دیتا ہے", "یہ انٹرنیٹ کے فائبر تاروں کو بند کر دیتا ہے"],
        "یہ کوانٹم فویئر ٹرانسفارم کے ذریعے بڑے ہندسوں کے پرائم فیکٹرز چند منٹوں میں معلوم کر لیتا ہے",
        "روایتی کمپیوٹر پر 2048 بٹ کا خفیہ پرائم کوڈ توڑنے میں کھربوں سال لگتے ہیں، لیکن شور کا الگورتھم کوانٹم سپر پوزیشن استعمال کر کے اسے پولی نومیل وقت میں حل کر سکتا ہے۔"
    ),
    (
        "How does Grover's Quantum Algorithm accelerate searching through an unsorted database of N items?",
        ["It provides a quadratic speedup, finding the target in roughly square-root of N steps", "It checks all items in zero time", "It sorts the database using light", "It duplicates the hard drive"],
        "It provides a quadratic speedup, finding the target in roughly square-root of N steps",
        "While classical brute force requires O(N) queries on average, Grover's algorithm amplifies the quantum probability amplitude of the correct state in O(sqrt(N)) iterations.",
        "گروور کا کوانٹم الگورتھم (Grover's Algorithm) کسی بے ترتیب ڈیٹا بیس میں مطلوبہ ریکارڈ تلاش کرنے کی رفتار کیسے بڑھاتا ہے؟",
        ["یہ جڑ (Square Root of N) کے تناسب سے رفتار تیز کر کے مطلوبہ ڈیٹا ڈھونڈتا ہے", "یہ صفر سیکنڈ میں تمام آئٹمز چیک کر لیتا ہے", "یہ روشنی کی مدد سے فائلوں کو ترتیب دیتا ہے", "یہ ڈیٹا بیس کی دس کاپیاں بنا دیتا ہے"],
        "یہ جڑ (Square Root of N) کے تناسب سے رفتار تیز کر کے مطلوبہ ڈیٹا ڈھونڈتا ہے",
        "اگر ایک غیر منظم ڈیٹا میں 10 لاکھ آئٹمز ہوں تو روایتی کمپیوٹر کو اوسطاً 5 لاکھ کوششیں درکار ہوں گی، مگر گروور کا الگورتھم کوانٹم ایمپلیٹیوڈ کے ذریعے صرف 1000 مراحل میں اسے ڈھونڈ لیتا ہے۔"
    ),
    (
        "In probability theory, why do you need only 23 people in a room to have a greater than 50 percent chance that two people share the exact same birthday (the Birthday Paradox)?",
        ["You compare pairs of people (253 distinct pairings) rather than comparing individuals to a single date", "Leap years have 366 days", "Most people are born in summer", "People forget their actual birthdates"],
        "You compare pairs of people (253 distinct pairings) rather than comparing individuals to a single date",
        "With 23 individuals, the number of distinct pairing combinations is 23*22/2 = 253. The complementary probability of zero matches drops below 0.5.",
        "سالگرہ کا معمہ (Birthday Paradox): کسی کمرے میں محض 23 افراد موجود ہوں تو اس بات کا امکان 50 فیصد سے زیادہ کیوں ہوتا ہے کہ کوئی سے دو افراد کی سالگرہ ایک ہی دن ہو؟",
        ["کیونکہ ہم ایک فرد کا موازنہ نہیں کرتے بلکہ آپس کے تمام ممکنہ جوڑوں (253 جوڑے) کا موازنہ کرتے ہیں", "لیپ کے سال میں 366 دن ہوتے ہیں", "زیادہ تر لوگ گرمیوں میں پیدا ہوتے ہیں", "لوگ اپنی تاریخ پیدائش بھول جاتے ہیں"],
        "کیونکہ ہم ایک فرد کا موازنہ نہیں کرتے بلکہ آپس کے تمام ممکنہ جوڑوں (253 جوڑے) کا موازنہ کرتے ہیں",
        "لوگ سمجھتے ہیں کہ 365 دن ہیں تو 180 لوگ چاہیے ہوں گے، مگر 23 افراد کے درمیان باہمی 253 جوڑے بنتے ہیں، جس سے کسی دو کے ایک ہی تاریخ پر پیدا ہونے کا امکان 50.7 فیصد تک پہنچ جاتا ہے۔"
    ),
    (
        "What statistical illusion occurs in Simpson's Paradox, where a treatment appears superior across every individual sub-group yet inferior when data is aggregated?",
        ["A confounding variable skews the weighting and sample sizes of the underlying sub-groups", "Computers round decimals improperly", "The survey contains fraudulent data", "Standard deviation drops to zero"],
        "A confounding variable skews the weighting and sample sizes of the underlying sub-groups",
        "Simpson's paradox arises when an unobserved confounding factor influences both group assignment and outcome, reversing the marginal association direction.",
        "سمپسن کا معمہ (Simpson's Paradox): اعداد و شمار میں ایسا کیوں ہوتا ہے کہ ایک دوا ہر الگ گروپ میں فائدہ مند نظر آتی ہے لیکن تمام گروپس کو اکٹھا کرنے پر مجموعی طور پر نقصان دہ لگتی ہے؟",
        ["ایک چھپا ہوا متغیر (Confounding Variable) مختلف ذیلی گروہوں کے نمونوں کے حجم اور وزن کو بگاڑ دیتا ہے", "کمپیوٹر اعشاریہ درست نہیں گنتا", "سروے میں جعلی ڈیٹا شامل ہوتا ہے", "ڈیٹا کا انحراف صفر ہو جاتا ہے"],
        "ایک چھپا ہوا متغیر (Confounding Variable) مختلف ذیلی گروہوں کے نمونوں کے حجم اور وزن کو بگاڑ دیتا ہے",
        "جب ذیلی گروہوں میں مریضوں کی بیماری کی شدت مختلف ہو اور شدید بیماروں کو دوا زیادہ دی گئی ہو، تو مجموعی شماریات کا رجحان بالکل الٹ جاتا ہے، حالانکہ انفرادی سطح پر دوا بہتر کام کر رہی تھی۔"
    ),
    (
        "According to Benford's Law (First-Digit Law), why does the digit '1' appear as the leading first digit in natural datasets (like river lengths and accounting ledgers) over 30 percent of the time?",
        ["Natural phenomena span multiple orders of magnitude with logarithmic and scale-invariant distributions", "Number 1 is visually prominent", "Auditors favor odd digits", "Small numbers weigh less"],
        "Natural phenomena span multiple orders of magnitude with logarithmic and scale-invariant distributions",
        "Scale-invariant data obeys a logarithmic distribution P(d) = log10(1 + 1/d), meaning growing from 1 to 2 requires a 100% increase, while 8 to 9 requires only 12.5%.",
        "بینفورڈ کا قانون (Benford's Law): قدرتی ڈیٹا جیسے دریاؤں کی لمبائی یا اکاؤنٹنگ کے کھاتوں میں ہندسہ '1' تقریباً 30 فیصد سے زیادہ مرتبہ پہلے ہندسے کے طور پر کیوں آتا ہے؟",
        ["قدرتی پیمانے لوگارتھمک اور پیمانے سے آزاد (Scale-invariant) تقسیم پر چلتے ہیں", "ہندسہ 1 دیکھنے میں نمایاں ہوتا ہے", "آڈیٹرز طاق اعداد پسند کرتے ہیں", "چھوٹے اعداد وزنی نہیں ہوتے"],
        "قدرتی پیمانے لوگارتھمک اور پیمانے سے آزاد (Scale-invariant) تقسیم پر چلتے ہیں",
        "1 سے بڑھ کر 2 بننے کے لیے ڈیٹا کو 100 فیصد دوگنا ہونا پڑتا ہے جبکہ 8 سے 9 بننے کے لیے صرف 12.5 فیصد اضافہ چاہیے۔ اسی لیے پہلے ہندسے کے طور پر 1 سب سے زیادہ کثرت سے آتا ہے۔"
    ),
    (
        "Why is Gabriel's Horn (Torricelli's Trumpet)—formed by rotating y = 1/x for x >= 1 around the x-axis—called the 'Painter's Paradox'?",
        ["It has a strictly finite internal volume of pi cubic units, but an infinite external surface area", "It cannot be held by hands", "Paint evaporates instantly inside", "Its cross-section is square"],
        "It has a strictly finite internal volume of pi cubic units, but an infinite external surface area",
        "The improper integral for volume converges to pi, while the surface area integral diverges to infinity; theoretically you could fill it with pi paint, but cannot coat its outside.",
        "گیبریل کا بگل (Painter's Paradox): ریاضی کی اس شکل کو پینٹر کا پیراڈاکس کیوں کہا جاتا ہے جسے اندر سے بھرا جا سکتا ہے لیکن باہر سے رنگنا ناممکن ہے؟",
        ["کیونکہ اس کا اندرونی حجم محدود (صرف پائی یونٹس) ہے جبکہ اس کا بیرونی رقبہ لا محدود ہے", "اسے ہاتھوں سے پکڑنا ناممکن ہے", "اس کے اندر پینٹ فوری بخارات بن جاتا ہے", "اس کی چوڑائی چوکور ہوتی ہے"],
        "کیونکہ اس کا اندرونی حجم محدود (صرف پائی یونٹس) ہے جبکہ اس کا بیرونی رقبہ لا محدود ہے",
        "حساب کے مطابق اسے بھرنے کے لیے پائی مقدار میں پینٹ کافی ہے، لیکن اس کی بیرونی سطح لامحدود لمبی ہے جس کو رنگنے کے لیے لامحدود پینٹ درکار ہوگا۔"
    ),
    (
        "Why does the Banach-Tarski Paradox state that a solid mathematical sphere can be cut into 5 disjoint pieces and reassembled into two identical spheres identical in volume to the original?",
        ["The decomposition relies on non-measurable sets generated using the non-constructive Axiom of Choice", "Spheres are made of empty atomic space", "The pieces expand upon cutting", "Gravity duplicates matter"],
        "The decomposition relies on non-measurable sets generated using the non-constructive Axiom of Choice",
        "The pieces are infinitely jagged, non-measurable sets with undefined Lebesgue volume. Rotating these non-measurable sets in 3D yields two whole unit spheres.",
        "بناخ تارسکی کا معمہ (Banach-Tarski Paradox): یہ حیران کن تھیورم کیسے ممکن بتاتا ہے کہ ایک گیند کو 5 ٹکڑوں میں کاٹ کر جوڑنے سے اصل سائز کی دو مکمل گیندیں بن جائیں؟",
        ["یہ نان میژریبل (Non-measurable) سیٹس پر مبنی ہے جو انتخاب کے اصول (Axiom of Choice) سے بنتے ہیں جن کا کوئی پیمانہ نہیں ہوتا", "گیندیں ایٹموں کے خالی حصے سے بنی ہوتی ہیں", "ٹکڑے کٹنے کے بعد خود بخود پھیل جاتے ہیں", "کشش ثقل مادے کی کاپی بنا دیتی ہے"],
        "یہ نان میژریبل (Non-measurable) سیٹس پر مبنی ہے جو انتخاب کے اصول (Axiom of Choice) سے بنتے ہیں جن کا کوئی پیمانہ نہیں ہوتا",
        "یہ مادی گیند کے لیے نہیں بلکہ خالص ریاضیاتی سیٹس کے لیے ہے۔ وہ 5 ٹکڑے اتنے بے ترتیب اور لامحدود پیچیدہ ہوتے ہیں کہ ان کا کوئی ٹھوس حجم ناپنا ممکن نہیں ہوتا، اسی لیے ان کو گھما کر دو گیندیں بن جاتی ہیں۔"
    ),
    (
        "In the Coastline Paradox, why does the measured geographical perimeter of Great Britain grow drastically larger the smaller your measuring ruler becomes?",
        ["Coastlines exhibit fractal self-similarity, meaning smaller measuring sticks capture finer bays and crevices ad infinitum", "Tides expand the landmass hourly", "Smaller rulers stretch under moisture", "Cartographers distort border lines"],
        "Coastlines exhibit fractal self-similarity, meaning smaller measuring sticks capture finer bays and crevices ad infinitum",
        "Benoit Mandelbrot proved coastlines have fractal dimensions greater than 1. As the ruler length epsilon approaches zero, total perimeter diverges toward infinity.",
        "ساحلی پٹی کا معمہ (Coastline Paradox): کسی جزیرے جیسے برطانیہ کے ساحل کی لمبائی کا ناپ جتنا چھوٹے پیمانے یا فیتے سے لیا جائے، کل لمبائی اتنی ہی زیادہ اور لامحدود کیوں نکلتی ہے؟",
        ["ساحلی پٹی فریکٹل (Fractal) ساخت رکھتی ہے، چھوٹا پیمانہ ہر موڑ اور پتھر کے اندرونی گھماؤ کو بھی گن لیتا ہے", "سمندر کی لہریں زمین کو ہر گھنٹے بڑا کر دیتی ہیں", "چھوٹا فیتہ نمی سے لمبا ہو جاتا ہے", "نقشہ ساز سرحدوں کو جان بوجھ کر ٹیڑھا کرتے ہیں"],
        "ساحلی پٹی فریکٹل (Fractal) ساخت رکھتی ہے، چھوٹا پیمانہ ہر موڑ اور پتھر کے اندرونی گھماؤ کو بھی گن لیتا ہے",
        "اگر 100 کلومیٹر کے اسکیل سے ناپیں تو چھوٹی خلیجیں چھوٹ جاتی ہیں، 1 میٹر سے ناپیں تو ہر پتھر گنا جاتا ہے، اور خردبین سے ناپیں تو ذرات کا گھماؤ لمبائی کو لامتناہی بنا دیتا ہے۔"
    ),
    (
        "In Zeno's Paradox of Achilles and the Tortoise, why does the swift Achilles mathematically overtake the slow tortoise in the real physical world despite infinite subdivisions of distance?",
        ["An infinite geometric series of decreasing distances and times converges to a finite sum", "Achilles steps on the tortoise", "The tortoise gets tired and stops", "Space ceases to exist at small scales"],
        "An infinite geometric series of decreasing distances and times converges to a finite sum",
        "Achilles covers distances that form an infinite geometric progression. Because sum(1/2^n) converges to 1, both the total distance and total elapsed time remain strictly finite.",
        "زینو کا معمہ (Achilles and Tortoise Paradox): اگر کچھوا چند میٹر آگے ہو تو تیز رفتار ایتھلیٹ ریاضیاتی تقسیم کے باوجود حقیقی دنیا میں کچھوے سے آگے کیسے نکل جاتا ہے؟",
        ["فاصلوں اور سیکنڈز کی لامتناہی جیومیٹرک سیریز کا مجموعہ محدود وقت اور فاصلے پر آ کر ختم ہو جاتا ہے", "ایتھلیٹ کچھوے پر پاؤں رکھ دیتا ہے", "کچھوا تھک کر بیٹھ جاتا ہے", "چھوٹے فاصلوں پر جگہ غائب ہو جاتی ہے"],
        "فاصلوں اور سیکنڈز کی لامتناہی جیومیٹرک سیریز کا مجموعہ محدود وقت اور فاصلے پر آ کر ختم ہو جاتا ہے",
        "اگرچہ درمیان میں لامتناہی مراحل بنتے ہیں (1/2, 1/4, 1/8...) مگر ان سب کا مجموعہ صرف 1 سیکنڈ بنتا ہے، اس لیے محدود وقت میں ایتھلیٹ کچھوے کو باآسانی پیچھے چھوڑ دیتا ہے۔"
    ),
    (
        "In Zeno's Arrow Paradox, an arrow in flight is motionless at every instantaneous moment in time. Why does it still travel across space?",
        ["Instantaneous velocity is the derivative of position with respect to time; motion exists across open intervals, not isolated points", "Air currents carry the arrow", "The archer bends physical space", "Human eyes see illusory arrows"],
        "Instantaneous velocity is the derivative of position with respect to time; motion exists across open intervals, not isolated points",
        "Motion is a relation between different points at different instants. As calculus proves, velocity is the limit of Delta x / Delta t as Delta t approaches zero, not static zero.",
        "زینو کا تیر کا معمہ (Arrow Paradox): فضا میں اڑتا ہوا تیر اگر وقت کے ہر ایک ساکت لمحے میں بالکل ساکن ہوتا ہے تو وہ آگے کا فاصلہ کیسے طے کرتا ہے؟",
        ["حرکت وقت کے ایک الگ تھلگ نقطے میں نہیں بلکہ وقت کے مسلسل بہاؤ اور تبدیلی کی رفتار (Derivatives) میں ہوتی ہے", "ہوا کا دباؤ تیر کو کھینچتا ہے", "تیر انداز جگہ کو موڑ دیتا ہے", "آنکھیں تیر کو غلط دیکھتی ہیں"],
        "حرکت وقت کے ایک الگ تھلگ نقطے میں نہیں بلکہ وقت کے مسلسل بہاؤ اور تبدیلی کی رفتار (Derivatives) میں ہوتی ہے",
        "حرکت کسی ایک ساکت فریم کا نام نہیں بلکہ وقت کے گزرنے کے ساتھ پوزیشن کی تبدیلی کی شرح کا نام ہے۔ کیلکولس نے ثابت کیا کہ لامحدود چھوٹے لمحے میں بھی ولاسٹی موجود رہتی ہے۔"
    ),
    (
        "In Parrondo's Paradox, how can alternating unpredictably between two distinct gambling games—both of which are mathematically guaranteed losing games on their own—result in a consistently winning game?",
        ["Nonlinear feedback and capital-dependent state switching introduce a ratcheting bias toward net profit", "The casino makes counting errors", "Dice wear down over time", "The house lowers taxes"],
        "Nonlinear feedback and capital-dependent state switching introduce a ratcheting bias toward net profit",
        "Similar to the Brownian ratchet in physics, state-dependent branching in Game B alters the stationary probability distribution, turning two negative drifts into a positive drift.",
        "پارونڈو کا معمہ (Parrondo's Paradox): دو ایسے کھیل جو اکیلے کھیلے جائیں تو دونوں میں یقینی نقصان ہوتا ہے، ان کو باری باری ملا کر کھیلنے سے کھلاڑی ہمیشہ نفع میں کیسے چلا جاتا ہے؟",
        ["سرمائے پر منحصر شرطیں ایسی حالتیں پیدا کرتی ہیں جو ایک گیم کے نقصان کو دوسری گیم کے نفع میں بدل دیتی ہیں", "کیسینو سکے گننے میں غلطی کرتا ہے", "پانسے گھس جاتے ہیں", "کھیل کے ٹیکس کم ہو جاتے ہیں"],
        "سرمائے پر منحصر شرطیں ایسی حالتیں پیدا کرتی ہیں جو ایک گیم کے نقصان کو دوسری گیم کے نفع میں بدل دیتی ہیں",
        "یہ فزکس کے براؤنین ریچٹ اصول پر کام کرتا ہے۔ ایک گیم سرمائے کے طاق یا جفت ہونے پر رولز بدلتی ہے، جس سے دونوں نقصان دہ کھیلوں کا امتزاج ایک نفع بخش سلسلہ بن جاتا ہے۔"
    ),
    (
        "In the St. Petersburg Paradox, a fair coin is tossed until heads appears on flip n, paying 2^n dollars. Why are rational people unwilling to pay more than $20 to play, despite an infinite mathematical expected value?",
        ["Human utility of wealth exhibits diminishing marginal returns, and real-world banks have finite wealth", "People dislike coin games", "Heads never appears past 5 flips", "Tosses take infinite time"],
        "Human utility of wealth exhibits diminishing marginal returns, and real-world banks have finite wealth",
        "Daniel Bernoulli resolved this using logarithmic utility: the utility of gaining billions approaches an asymptote, and no physical entity has infinite capital to pay extreme payouts.",
        "سینٹ پیٹرزبرگ کا معمہ (St. Petersburg Paradox): ایک کھیل جس میں متوقع ریاضیاتی انعام لامحدود کھربوں ڈالر بنتا ہے، عقلمند انسان اس میں شرکت کے لیے صرف 20 یا 25 ڈالر سے زیادہ دینے کو تیار کیوں نہیں ہوتے؟",
        ["دولت کی افادیت میں بتدریج کمی (Diminishing Marginal Utility) واقع ہوتی ہے اور دنیا کے کسی بینک کے پاس لامحدود دولت نہیں ہوتی", "لوگ سکے کا کھیل ناپسند کرتے ہیں", "پانچویں باری کے بعد ہیڈز کبھی نہیں آتا", "سکہ اچھالنے میں صدیاں لگتی ہیں"],
        "دولت کی افادیت میں بتدریج کمی (Diminishing Marginal Utility) واقع ہوتی ہے اور دنیا کے کسی بینک کے پاس لامحدود دولت نہیں ہوتی",
        "ریاضی دان برنولی نے واضح کیا کہ انسان پیسوں کی افادیت کو ریاضیاتی اوسط کی بجائے اپنے ذہنی اطمینان کے حساب سے دیکھتا ہے، اور کڑوڑوں کا انعام جیتنے کا امکان صفر کے اتنا قریب ہوتا ہے کہ خطرہ مول نہیں لیا جاتا۔"
    ),
    (
        "In Newcomb's Problem, an infallible predictor leaves Box A ($1,000) and Box B ($1,000,000 if predicted you take B only; empty if predicted you take both). Why does decision theory split between taking one box vs both boxes?",
        ["Causal Decision Theory argues the money is already fixed inside, while Evidential Decision Theory argues your choice correlates with the prediction", "Box B has a transparent bottom", "The predictor cheats with mirrors", "Box A contains counterfeit bills"],
        "Causal Decision Theory argues the money is already fixed inside, while Evidential Decision Theory argues your choice correlates with the prediction",
        "Causal decision theorists two-box because the box contents were physically placed in the past and cannot be changed causally. Evidential theorists one-box to maximize expected value.",
        "نیوکومب کا مسئلہ (Newcomb's Paradox): ایک غیب دان نے پہلے ہی باکس میں پیسے رکھ دیے ہیں۔ اس میں ایک باکس لینا چاہیے یا دونوں؟ اس پر فیصلے کی تھیوری دو حصوں میں کیوں بٹ جاتی ہے؟",
        ["سببی تھیوری (Causal) کہتی ہے کہ رقم پہلے ہی رکھی جا چکی ہے جبکہ شواہدی تھیوری (Evidential) کہتی ہے کہ آپ کا فیصلہ پیش گوئی کے ساتھ جڑا ہے", "دوسرے باکس کا پیندا شفاف ہوتا ہے", "غیب دان شیشوں کے ذریعے دھوکہ دیتا ہے", "پہلے باکس میں جعلی نوٹ ہوتے ہیں"],
        "سببی تھیوری (Causal) کہتی ہے کہ رقم پہلے ہی رکھی جا چکی ہے جبکہ شواہدی تھیوری (Evidential) کہتی ہے کہ آپ کا فیصلہ پیش گوئی کے ساتھ جڑا ہے",
        "کازل تھیوری کے ماننے والے کہتے ہیں کہ ماضی بدلا نہیں جا سکتا اس لیے دونوں باکس اٹھا کر ہزار ڈالر مزید کماؤ، جبکہ ایویڈینشل والے کہتے ہیں کہ غیب دان 99 فیصد درست ہے اس لیے صرف دوسرا باکس چنو۔"
    ),
    (
        "In the Sleeping Beauty Problem, Beauty is put to sleep and awakened on Monday (and also Tuesday if a coin lands Tails, with her memory wiped). Upon awakening, what is her subjective credence that the coin landed Heads?",
        ["'Halfers' argue the prior probability remains 1/2, while 'Thirders' argue she is in 1 of 3 equally likely waking events (1/3)", "She calculates exactly 3/4", "Her credence drops to zero", "Coin tosses are prohibited"],
        "'Halfers' argue the prior probability remains 1/2, while 'Thirders' argue she is in 1 of 3 equally likely waking events (1/3)",
        "Thirders point out there are three indistinguishable awakening scenarios (Mon/Heads, Mon/Tails, Tue/Tails), making Heads 1/3. Halfers argue no new relevant evidence was acquired.",
        "سوتی ہوئی شہزادی کا معمہ (Sleeping Beauty Problem): جب شہزادی کو جگایا جاتا ہے اور اس کی یادداشت مٹا دی گئی ہو، تو اس کے نزدیک سکہ ہیڈز آنے کا امکان کیا ہونا چاہیے؟",
        ["ہافرز (Halfers) کہتے ہیں کہ کوئی نئی معلومات نہیں ملی اس لیے 1/2 ہے، جبکہ تھرڈرز (Thirders) کہتے ہیں کہ جاگنے کے تین ممکنہ واقعات میں سے ایک ہے اس لیے 1/3 ہے", "وہ حساب لگا کر 3/4 جواب دیتی ہے", "اس کا امکان صفر ہو جاتا ہے", "سکہ اچھالنا منع ہوتا ہے"],
        "ہافرز (Halfers) کہتے ہیں کہ کوئی نئی معلومات نہیں ملی اس لیے 1/2 ہے، جبکہ تھرڈرز (Thirders) کہتے ہیں کہ جاگنے کے تین ممکنہ واقعات میں سے ایک ہے اس لیے 1/3 ہے",
        "تھرڈرز کا ماننا ہے کہ اگر ٹیلز آئے تو وہ دو بار جاگتی ہے اور ہیڈز پر ایک بار، تو کل 3 جاگنے کی حالتوں میں سے صرف 1 میں ہیڈز ہوتا ہے، جبکہ ہافرز کہتے ہیں سکے کی اصل 50 فیصد اوسط نہیں بدلی۔"
    ),
    (
        "In the Two Envelopes Problem, Envelope A contains $X and Envelope B contains either $2X or $X/2. Why is the apparent expected gain from switching (1.25 * X) fallacious?",
        ["It falsely assumes a uniform prior probability distribution across an unbounded positive real number space", "The second envelope is always empty", "Money shrinks inside envelopes", "Envelopes cannot be opened"],
        "It falsely assumes a uniform prior probability distribution across an unbounded positive real number space",
        "A uniform probability distribution over all positive real numbers is mathematically improper. Any valid integrable prior probability distribution eliminates the expected gain from switching.",
        "دو لفافوں کا معمہ (Two Envelopes Problem): ایک لفافے میں دوسرے سے دگنی یا آدھی رقم ہے۔ ریاضیاتی طور پر لفافہ بدلنے پر 1.25 گنا متوقع فائدے کا حساب کیوں غلط اور دھوکہ ثابت ہوتا ہے؟",
        ["کیونکہ یہ مفروضہ غلط ہے کہ لامحدود رقم تک ہر عدد کے ہونے کا امکان بالکل یکساں (Uniform) ہو سکتا ہے", "دوسرا لفافہ ہمیشہ خالی ہوتا ہے", "لفافے کے اندر نوٹ سکڑ جاتے ہیں", "لفافے کھولنا ممنوع ہوتا ہے"],
        "کیونکہ یہ مفروضہ غلط ہے کہ لامحدود رقم تک ہر عدد کے ہونے کا امکان بالکل یکساں (Uniform) ہو سکتا ہے",
        "حقیقی دنیا میں رقم لامحدود نہیں ہو سکتی۔ ایک بار جب آپ ایک متوازن پراببلٹی ڈسٹری بیوشن لگاتے ہیں تو لفافہ بدلنے کا متوقع فائدہ خود بخود صفر ہو جاتا ہے۔"
    ),
    (
        "In Hempel's Raven Paradox, why does observing a green apple on your kitchen table logically constitute Bayesian evidence for the hypothesis that 'All ravens are black'?",
        ["'All ravens are black' is logically equivalent to its contrapositive: 'All non-black things are non-ravens'", "Apples and ravens share DNA", "Green apples turn black when ripe", "Kitchens attract ravens"],
        "'All ravens are black' is logically equivalent to its contrapositive: 'All non-black things are non-ravens'",
        "By contraposition, 'All ravens are black' (R -> B) equals (~B -> ~R). A non-black non-raven (green apple) confirms the contrapositive, though the Bayesian posterior shift is infinitesimally tiny.",
        "ہیمپیل کا کوؤں کا معمہ (Raven Paradox): کچن میں رکھے ہوئے ایک ہرے سیب کو دیکھنا منطقی طور پر اس بات کا ثبوت کیوں بنتا ہے کہ 'دنیا کے تمام کوے کالے ہیں'؟",
        ["کیونکہ منطق میں 'تمام کوے کالے ہیں' کا الٹ عکسی بیان (Contrapositive) یہ ہے کہ 'ہر وہ چیز جو کالی نہیں ہے وہ کوا بھی نہیں ہے'", "سیب اور کوے کا ڈی این اے ملتا ہے", "ہرے سیب پک کر کالے ہو جاتے ہیں", "کچن کوؤں کو پسند ہوتے ہیں"],
        "کیونکہ منطق میں 'تمام کوے کالے ہیں' کا الٹ عکسی بیان (Contrapositive) یہ ہے کہ 'ہر وہ چیز جو کالی نہیں ہے وہ کوا بھی نہیں ہے'",
        "ہرا سیب نہ کالا ہے اور نہ کوا ہے، اس لیے وہ الٹ بیان کی تصدیق کرتا ہے جو کہ اصل بیان کے بالکل برابر ہے۔ البتہ دنیا میں غیر کالی چیزیں اتنی زیادہ ہیں کہ اس سے ثبوت کا وزن نہ ہونے کے برابر بنتا ہے۔"
    ),
    (
        "In Nelson Goodman's 'Grue' Paradox, why does defining a predicate 'grue' (green before year 2050, blue afterwards) challenge the foundation of scientific induction?",
        ["All emeralds examined so far provide identical empirical support for being 'green' and for being 'grue'", "Emeralds change color in 2050", "Grue is an invalid English word", "Gemologists disagree on colors"],
        "All emeralds examined so far provide identical empirical support for being 'green' and for being 'grue'",
        "Goodman demonstrated that induction requires criteria for 'projectible' predicates. Past observational data cannot mathematically distinguish between timeless laws and time-conditioned predicates.",
        "گڈمین کا گرُو پیراڈاکس (Grue Paradox): یہ فلسفیانہ معمہ سائنسی مشاہدات اور استقرائی منطق پر کیا سوال اٹھاتا ہے؟",
        ["اب تک دیکھے گئے تمام زمرد بیک وقت 'سبز' ہونے کا بھی اتنا ہی ثبوت دیتے ہیں جتنا کہ 'گرُو' (جو کہ 2050 میں نیلا ہو جائے گا) ہونے کا", "زمرد 2050 میں خود بخود نیلے ہو جائیں گے", "گرُو ایک غیر قانونی لفظ ہے", "ماہرین رنگوں کی پہچان نہیں کر سکتے"],
        "اب تک دیکھے گئے تمام زمرد بیک وقت 'سبز' ہونے کا بھی اتنا ہی ثبوت دیتے ہیں جتنا کہ 'گرُو' (جو کہ 2050 میں نیلا ہو جائے گا) ہونے کا",
        "صرف ماضی کے مشاہدے سے ہم یہ ثابت نہیں کر سکتے کہ کل چیزوں کا رویہ بدل نہیں جائے گا۔ یہ معمہ ثابت کرتا ہے کہ سائنسی قوانین کی قبولیت میں سادہ مشاہدے کے علاوہ دیگر وجوہات درکار ہوتی ہیں۔"
    ),
    (
        "In the Unexpected Hanging Paradox, a judge sentences a prisoner to be hanged on a weekday at noon, but promises the day will be a total surprise. Why does backward induction fail to save the prisoner?",
        ["A surprise is an epistemological state; the prisoner's logical deduction that it cannot happen makes Friday (or any day) a genuine surprise", "The judge cancels the execution", "The jail has only 3 days", "Prisoners cannot think clearly"],
        "A surprise is an epistemological state; the prisoner's logical deduction that it cannot happen makes Friday (or any day) a genuine surprise",
        "The prisoner deduced it couldn't happen Friday, then Thursday, and so on, concluding it was impossible. When hanged on Wednesday, he was completely surprised, validating the judge's decree.",
        "غیر متوقع پھانسی کا معمہ (Unexpected Hanging Paradox): قیدی نے منطق لگا کر ثابت کیا کہ اسے کسی دن پھانسی نہیں دی جا سکتی، مگر بدھ کے دن جلاد آیا تو قیدی حیران کیوں رہ گیا؟",
        ["حیرت ایک علمی کیفیت ہے؛ قیدی کے یہ سوچ لینے کے بعد کہ پھانسی ممکن ہی نہیں، کسی بھی دن پھانسی کا ہونا اس کے لیے غیر متوقع اور حیران کن بن گیا", "جج نے سزا معاف کر دی تھی", "ہفتے میں صرف تین دن بچے تھے", "قیدی کی عقل کام نہیں کر رہی تھی"],
        "حیرت ایک علمی کیفیت ہے؛ قیدی کے یہ سوچ لینے کے بعد کہ پھانسی ممکن ہی نہیں، کسی بھی دن پھانسی کا ہونا اس کے لیے غیر متوقع اور حیران کن بن گیا",
        "قیدی نے الٹی گنتی سے آخری دن مسترد کیے اور مطمئن ہو گیا۔ جب بدھ کو جلاد آیا تو جج کی یہ بات بالکل سچی ثابت ہوئی کہ پھانسی کا دن قیدی کے لیے مکمل غیر متوقع تھا۔"
    ),
    (
        "In the Prisoner's Dilemma, why do two rational players end up defecting and receiving a worse outcome than if both had remained silent?",
        ["Defection is the strictly dominant strategy for each individual, resulting in a Pareto-suboptimal Nash equilibrium", "They hate each other personal feelings", "The police beat them into confessing", "Cooperation is illegal"],
        "Defection is the strictly dominant strategy for each individual, resulting in a Pareto-suboptimal Nash equilibrium",
        "Regardless of what the partner chooses, defecting yields a better payoff for each individual. Since both reason rationally, they reach mutual defection, which is worse for both.",
        "قیدیوں کا مخمصہ (Prisoner's Dilemma): دو عقل مند قیدی باہمی تعاون کرنے کی بجائے ایک دوسرے کے خلاف گواہی دے کر دونوں طویل قید کی سزا کیوں بھگتتے ہیں؟",
        ["دھوکہ دینا ہر انفرادی قیدی کے ذاتی فائدے کے لیے برتر حکمت عملی (Dominant Strategy) ہوتی ہے جس سے دونوں برے توازن پر پہنچتے ہیں", "ان دونوں میں پرانی دشمنی ہوتی ہے", "پولیس ان پر تشدد کرتی ہے", "خاموش رہنا قانوناً جرم ہے"],
        "دھوکہ دینا ہر انفرادی قیدی کے ذاتی فائدے کے لیے برتر حکمت عملی (Dominant Strategy) ہوتی ہے جس سے دونوں برے توازن پر پہنچتے ہیں",
        "اگر دوسرا قیدی چپ رہے تو دھوکہ دے کر بندہ چھوٹ سکتا ہے، اگر دوسرا دھوکہ دے تو چپ رہنے پر زیادہ سزا ہو گی۔ اس لیے ذاتی مفاد کی منطق دونوں کو اس توازن پر لا کھڑا کرتی ہے جو دونوں کے لیے برا ہے۔"
    ),
    (
        "In game theory's Stag Hunt, why might players choose to hunt a small Hare alone rather than cooperate to hunt a large Stag?",
        ["Hunting the Hare is risk-dominant and requires zero trust, whereas Stag hunting is payoff-dominant but vulnerable to defection", "Hares taste significantly better", "Stags are completely extinct", "Hares are slower than snails"],
        "Hunting the Hare is risk-dominant and requires zero trust, whereas Stag hunting is payoff-dominant but vulnerable to defection",
        "Cooperating on a stag offers the highest mutual reward, but if the partner abandons, the remaining hunter starves. Hunting hare provides guaranteed solitary survival without trust.",
        "ہرن کا شکار بمقابلہ خرگوش (Stag Hunt Game): شکاری مل کر بڑے ہرن کا شکار کرنے کی بجائے اکیلے اکیلے چھوٹے خرگوش کا شکار کیوں پسند کرتے ہیں؟",
        ["خرگوش کا شکار خطرے سے پاک (Risk-dominant) ہوتا ہے اور اس میں دوسرے کے بھروسے کی ضرورت نہیں ہوتی، جبکہ ہرن کے لیے باہمی اعتماد لازم ہے", "خرگوش کا گوشت زیادہ لذیذ ہوتا ہے", "ہرن ناپید ہو چکے ہیں", "خرگوش گھونگھے سے بھی سست ہوتا ہے"],
        "خرگوش کا شکار خطرے سے پاک (Risk-dominant) ہوتا ہے اور اس میں دوسرے کے بھروسے کی ضرورت نہیں ہوتی، جبکہ ہرن کے لیے باہمی اعتماد لازم ہے",
        "اگر ایک ساتھی بھاگ جائے تو ہرن کے اکیلے شکاری کو بھوکا مرنا پڑے گا۔ اس لیے عدم اعتماد کی فضا میں انسان زیادہ منافع چھوڑ کر کم نفع مگر یقینی تحفظ کو ترجیح دیتا ہے۔"
    ),
    (
        "Why does Garrett Hardin's 'Tragedy of the Commons' inevitably cause shared pasture lands or ocean fisheries to become overexploited and depleted?",
        ["Individual users receive 100 percent of the benefit from each extra resource extracted, but bear only a fraction of the shared depletion cost", "Grass stops growing when grazed", "Ocean water evaporates too fast", "Government mandates overuse"],
        "Individual users receive 100 percent of the benefit from each extra resource extracted, but bear only a fraction of the shared depletion cost",
        "Each rational herder gains +1 utility per cow added, while the negative pasture degradation is divided among all herdsmen, incentivizing infinite individual overconsumption.",
        "مشترکہ چراگاہ کا المیہ (Tragedy of the Commons): مشترکہ جھیل کی مچھلیاں یا مشترکہ چراگاہ کی گھاس ہمیشہ ضرورت سے زیادہ استعمال ہو کر ختم کیوں ہو جاتی ہے؟",
        ["ہر چرواہے کو اضافی جانور چرانے کا 100 فیصد ذاتی فائدہ ملتا ہے جبکہ چراگاہ کے نقصان کا بوجھ سب میں تقسیم ہوتا ہے", "چرنے کے بعد گھاس دوبارہ نہیں اگتی", "جھیل کا پانی اڑ جاتا ہے", "حکومت زیادہ جانور رکھنے پر مجبور کرتی ہے"],
        "ہر چرواہے کو اضافی جانور چرانے کا 100 فیصد ذاتی فائدہ ملتا ہے جبکہ چراگاہ کے نقصان کا بوجھ سب میں تقسیم ہوتا ہے",
        "ایک چرواہا جانور بڑھاتا ہے تو دودھ اور گوشت کا نفع صرف اس کا ہوتا ہے، مگر چراگاہ کی بربادی تمام چرواہوں کا مشترکہ نقصان ہوتی ہے۔ اس ذاتی فائدے کے چکر میں وسائل برباد ہو جاتے ہیں۔"
    ),
    (
        "In Martin Shubik's 'Dollar Auction' game, why do rational bidders regularly bid $2, $3, or even $5 to purchase a single crisp $1 bill?",
        ["The second-highest bidder must pay their bid without receiving anything, creating an escalation of commitment trap to minimize loss", "The dollar bill contains hidden gold", "Bidders think money is fake", "The auctioneer changes the rules"],
        "The second-highest bidder must pay their bid without receiving anything, creating an escalation of commitment trap to minimize loss",
        "If Bidder A bids $1.00 and Bidder B bids $0.95, Bidder B faces losing $0.95 or bidding $1.05 to lose only $0.05. Both enter a vicious bidding war to avoid total loss.",
        "ایک ڈالر کی نیلامی کا معمہ (Dollar Auction): ایک ڈالر کے نوٹ کی نیلامی میں ہوشیار لوگ ایک ڈالر خریدنے کے لیے دو، تین یا پانچ ڈالر کی بولی کیوں لگانے لگتے ہیں؟",
        ["کیونکہ دوسرے نمبر پر آنے والے کو بھی اپنی بولی کی رقم بھرنی پڑتی ہے مگر اسے ملتا کچھ نہیں، جس سے وہ نقصان کم کرنے کے چکر میں بولی بڑھاتا رہتا ہے", "نوٹ میں سونا چھپا ہوتا ہے", "لوگ سمجھتے ہیں نوٹ جعلی ہے", "نیلام کرنے والا اصول بدل دیتا ہے"],
        "کیونکہ دوسرے نمبر پر آنے والے کو بھی اپنی بولی کی رقم بھرنی پڑتی ہے مگر اسے ملتا کچھ نہیں، جس سے وہ نقصان کم کرنے کے چکر میں بولی بڑھاتا رہتا ہے",
        "اگر ایک نے 1 ڈالر لگائے اور دوسرے نے 95 سینٹ، تو دوسرا سوچتا ہے کہ 95 سینٹ ڈوبنے سے بہتر ہے کہ میں 1.05 ڈالر لگا دوں تاکہ صرف 5 سینٹ کا نقصان ہو۔ یوں دونوں برباد ہوتے رہتے ہیں۔"
    ),
    (
        "In the Centipede Game, backward induction predicts that rational players will terminate the game on the very first turn. Why?",
        ["Each player anticipates that the other player will defect on the final move, propagating defection backwards to Move 1", "The game board runs out of space", "Tokens dissolve after 1 turn", "Players run out of patience"],
        "Each player anticipates that the other player will defect on the final move, propagating defection backwards to Move 1",
        "Knowing the opponent will defect on step 100 to maximize profit, Player 1 defects on step 99, which makes the other defect on step 98, unwinding cooperation entirely to step 1.",
        "سینٹی پیڈ گیم (Centipede Game): گیم تھیوری میں عقل اور منطق کے اصول پر دونوں کھلاڑی پہلے ہی مرحلے پر گیم کیوں ختم کر دیتے ہیں؟",
        ["ہر کھلاڑی پہلے ہی حساب لگا لیتا ہے کہ دوسرا کھلاڑی آخری مرحلے پر دھوکہ دے گا، جس سے الٹی گنتی کی منطق پہلے مرحلے پر دھوکہ دینے پر مجبور کرتی ہے", "کھیل کے بورڈ پر جگہ ختم ہو جاتی ہے", "گیم کے سکے پگھل جاتے ہیں", "کھلاڑیوں کا صبر ختم ہو جاتا ہے"],
        "ہر کھلاڑی پہلے ہی حساب لگا لیتا ہے کہ دوسرا کھلاڑی آخری مرحلے پر دھوکہ دے گا، جس سے الٹی گنتی کی منطق پہلے مرحلے پر دھوکہ دینے پر مجبور کرتی ہے",
        "اگر آخری باری پر سامنے والا سارا مال سمیٹ لے گا، تو اس سے پہلے والا کھلاڑی اس سے ایک باری پہلے ہی ختم کر دے گا۔ یوں سوچتے سوچتے دونوں پہلے ہی قدم پر تعاون چھوڑ کر کھیل روک دیتے ہیں۔"
    ),
    (
        "What human cognitive bias is exposed by the Allais Paradox, where people prefer a guaranteed $1 million over an 89 percent gamble for more, violating expected utility theory?",
        ["Certainty effect: people disproportionately overweight certainty and exhibit non-linear probability weighting near 100 percent", "People do not know arithmetic", "Lottery tickets are illegal", "Inflation makes money worthless"],
        "Certainty effect: people disproportionately overweight certainty and exhibit non-linear probability weighting near 100 percent",
        "Maurice Allais showed human risk preferences violate the independence axiom. The psychological relief of 100% certainty is valued far higher than an incremental 1% risk of zero.",
        "ایلے کا معمہ (Allais Paradox): لوگ 89 فیصد زیادہ جیتنے کے امکان والے جوئے کے مقابلے میں یقینی 10 لاکھ ڈالر کو کیوں ترجیح دیتے ہیں، جو ریاضیاتی افادیت کے فارمولے کے خلاف ہے؟",
        ["یقینی ہونے کا اثر (Certainty Effect): انسانی دماغ 100 فیصد یقینی نتیجے کو معمولی غیر یقینی کے مقابلے میں غیر معمولی حد تک زیادہ ترجیح دیتا ہے", "لوگوں کو گنتی نہیں آتی", "لاٹری ٹکٹ غیر قانونی ہوتے ہیں", "مہنگائی پیسے کی قدر ختم کر دیتی ہے"],
        "یقینی ہونے کا اثر (Certainty Effect): انسانی دماغ 100 فیصد یقینی نتیجے کو معمولی غیر یقینی کے مقابلے میں غیر معمولی حد تک زیادہ ترجیح دیتا ہے",
        "اگرچہ ریاضی کے فارمولے کے مطابق رسک والے آپشن میں اوسط آمدن زیادہ بنتی ہے، مگر انسان کا دل 1 فیصد بھی خالی ہاتھ لوٹنے کے پچھتاوے کو برداشت نہیں کر سکتا۔"
    ),
    (
        "In the Ellsberg Paradox, why do people strongly prefer betting on an urn containing 50 red and 50 black balls over an urn with 100 balls of completely unknown color proportion?",
        ["Ambiguity aversion: humans fear unknown probability distributions far more than known equal risks", "Unknown balls are heavier", "The second urn has no balls", "Black balls absorb luck"],
        "Ambiguity aversion: humans fear unknown probability distributions far more than known equal risks",
        "Daniel Ellsberg proved people distinguish between risk (known odds) and knightian uncertainty / ambiguity (unknown odds), systematically rejecting ambiguous wagers.",
        "ایلزبرگ کا معمہ (Ellsberg Paradox): لوگ اس مٹکے پر شرط لگانا کیوں زیادہ پسند کرتے ہیں جس میں 50 لال اور 50 کالی گیندیں معلوم ہوں، بنسبت اس مٹکے کے جس میں گیندوں کا تناسب نامعلوم ہو؟",
        ["ابهام سے بیزاری (Ambiguity Aversion): انسان معلوم خطرے کو نامعلوم امکانات کے مقابلے میں زیادہ محفوظ اور قابل قبول سمجھتا ہے", "نامعلوم گیندیں وزنی ہوتی ہیں", "دوسرے مٹکے میں کوئی گیند نہیں ہوتی", "کالی گیندیں قسمت خراب کرتی ہیں"],
        "ابهام سے بیزاری (Ambiguity Aversion): انسان معلوم خطرے کو نامعلوم امکانات کے مقابلے میں زیادہ محفوظ اور قابل قبول سمجھتا ہے",
        "اگرچہ نامعلوم مٹکے میں بھی جیتنے کا اوسط امکان 50 فیصد ہی نکلتا ہے، مگر انسانی فطرت معلومات کی کمی اور ابہام سے اتنی خوفزدہ ہوتی ہے کہ وہ معلوم رسک کو ترجیح دیتی ہے۔"
    ),
    (
        "Why is believing a roulette wheel that landed on Red 10 times in a row is 'due' to hit Black called the Gambler's Fallacy?",
        ["Independent random events have no memory; the probability of landing on Red or Black remains exactly 50 percent on every individual spin", "Roulette wheels reset their magnets", "The dealer swaps the ball", "Croupiers must balance the colors"],
        "Independent random events have no memory; the probability of landing on Red or Black remains exactly 50 percent on every individual spin",
        "The coin or roulette wheel has no physical memory mechanism. Believing a long streak influences independent future trials conflates the law of large numbers with local balancing.",
        "جواری کا مغالطہ (Gambler's Fallacy): اگر رولیٹ کا پہیہ لگاتار 10 بار سرخ رنگ پر رکے تو یہ سوچنا کہ 'اب اگلی بار کالا رنگ آنا ہی آنا ہے' غلط کیوں ہے؟",
        ["آزادانہ واقعات کی کوئی یادداشت نہیں ہوتی؛ ہر گھماؤ پر لال یا کالے کا امکان بالکل وہی 50 فیصد رہتا ہے", "پہیے کا مقناطیس ری سیٹ ہو جاتا ہے", "ڈیلر گیند بدل دیتا ہے", "کیسینو پر لازم ہے کہ دونوں رنگ برابر لائے"],
        "آزادانہ واقعات کی کوئی یادداشت نہیں ہوتی؛ ہر گھماؤ پر لال یا کالے کا امکان بالکل وہی 50 فیصد رہتا ہے",
        "سکے یا پہیے کے پاس دماغ نہیں ہوتا کہ وہ یاد رکھے کہ پہلے کیا آیا تھا۔ لمبی قطار کے باوجود ہر نئی باری کا پچھلی باریوں سے کوئی تعلق نہیں ہوتا۔"
    ),
    (
        "Why does a medical test that is 99 percent accurate for a rare disease affecting 1 in 10,000 people only indicate a roughly 1 percent chance of actually having the disease upon a positive result?",
        ["Base rate neglect: the vast majority of positive tests in a healthy population are false positives", "The test uses expired reagents", "Doctors misinterpret blood samples", "The patient has high immunity"],
        "Base rate neglect: the vast majority of positive tests in a healthy population are false positives",
        "In 10,000 people, 1 is sick (true positive) while ~100 healthy people test false positive (1% of 9,999). Thus, P(Sick | Positive) = 1 / (1 + 100) ~ 1%.",
        "بیس ریٹ نظراندازی (Base Rate Neglect): ایک نادر بیماری جو 10,000 میں سے 1 بندے کو ہو، اس کا 99 فیصد درست ٹیسٹ پازیٹو آنے کے باوجود بیماری ہونے کا اصل امکان صرف 1 فیصد کیوں ہوتا ہے؟",
        ["کیونکہ صحت مند افراد کی اتنی بڑی تعداد (9,999) میں ٹیسٹ کی 1 فیصد غلطی درجنوں جھوٹے پازیٹو (False Positives) نتائج پیدا کر دیتی ہے", "ٹیسٹ کی دوائی ایکسپائر ہوتی ہے", "ڈاکٹر رپورٹ پڑھنا نہیں جانتے", "مریض کی قوت مدافعت بہت زیادہ ہے"],
        "کیونکہ صحت مند افراد کی اتنی بڑی تعداد (9,999) میں ٹیسٹ کی 1 فیصد غلطی درجنوں جھوٹے پازیٹو (False Positives) نتائج پیدا کر دیتی ہے",
        "10 ہزار لوگوں میں صرف 1 شخص بیمار ہے، جبکہ 9999 تندرست لوگوں کا 1 فیصد فالز پازیٹو مل کر 100 جھوٹے کیس بناتا ہے۔ اس لیے 101 پازیٹو نتائج میں سے صرف 1 بندہ واقعی بیمار ہوتا ہے۔"
    ),
    (
        "Why did mathematician Abraham Wald advise the US military to add heavy armor to the undamaged sections of returning combat bombers rather than where bullet holes were found?",
        ["Survivorship bias: planes hit in the engine and cockpit crashed and never returned; returning planes showed where hits were non-fatal", "Armor placed on wings made planes fly backwards", "Bullet holes made planes more aerodynamic", "Mechanics had limited rivets"],
        "Survivorship bias: planes hit in the engine and cockpit crashed and never returned; returning planes showed where hits were non-fatal",
        "Wald recognized the returning fleet was a biased sample of survivors. Areas with zero bullet holes on survivors (engine, cockpit) were precisely where hits were fatal.",
        "بقا کا تعصب (Survivorship Bias): دوسری جنگ عظیم میں ماہر ریاضی دان نے جنگ سے لوٹنے والے جہازوں کے ان حصوں پر لوہا لگانے کا مشورہ کیوں دیا جہاں گولیوں کا ایک بھی نشان نہیں تھا؟",
        ["کیونکہ جن جہازوں کے انجن اور کاک پٹ پر گولیاں لگی تھیں وہ تباہ ہو کر لوٹے ہی نہیں؛ لوٹنے والے جہاز وہ تھے جن کے غیر اہم حصوں پر گولیاں لگی تھیں", "پروں پر لوہا لگانے سے جہاز الٹا اڑتا تھا", "گولیوں کے سوراخ جہاز کو تیز چلاتے تھے", "مستریوں کے پاس کیلیں ختم ہو گئی تھیں"],
        "کیونکہ جن جہازوں کے انجن اور کاک پٹ پر گولیاں لگی تھیں وہ تباہ ہو کر لوٹے ہی نہیں؛ لوٹنے والے جہاز وہ تھے جن کے غیر اہم حصوں پر گولیاں لگی تھیں",
        "لوٹنے والے جہاز زندہ بچ جانے والے نمونے تھے۔ جن کے انجن پر گولی لگی وہ سمندر میں گر گئے۔ اس لیے جہاں لوٹنے والے جہازوں پر کوئی سوراخ نہیں تھا، اصل خطرہ وہی تھا اور وہیں بکتر بند لگانا ضروری تھا۔"
    ),
    (
        "In the Wason Selection Task, why do over 80 percent of people fail to test the rule 'If a card shows a vowel on one side, it must show an even number on the other' with cards showing [A, K, 4, 7]?",
        ["Confirmation bias: people flip card '4' to confirm the rule rather than flipping '7' to attempt to falsify it (modus tollens)", "People confuse letters and numbers", "Cards have blank backs", "Even numbers are lucky"],
        "Confirmation bias: people flip card '4' to confirm the rule rather than flipping '7' to attempt to falsify it (modus tollens)",
        "The rule is P -> Q. To test it, one must check P (card 'A') and not-Q (card '7'). Flipping '4' (Q) commits affirming the consequent and cannot falsify the rule.",
        "واسن کا سلیکشن ٹیسٹ (Wason Selection Task): 'اگر کارڈ پر حرف علت (Vowel) ہو تو دوسری طرف جفت عدد ہوگا' اصول کو پرکھنے کے لیے [A, K, 4, 7] کارڈز میں سے لوگ کارڈ 7 الٹنے میں کیوں ناکام ہوتے ہیں؟",
        ["تصدیقی تعصب (Confirmation Bias): لوگ اصول کو غلط ثابت کرنے کی بجائے کارڈ 4 الٹ کر اسے سچ ثابت کرنے کے چکر میں پڑ جاتے ہیں", "لوگ حروف اور نمبروں میں فرق نہیں کر پاتے", "کارڈ کے پیچھے کچھ نہیں لکھا ہوتا", "جفت اعداد خوش قسمت ہوتے ہیں"],
        "تصدیقی تعصب (Confirmation Bias): لوگ اصول کو غلط ثابت کرنے کی بجائے کارڈ 4 الٹ کر اسے سچ ثابت کرنے کے چکر میں پڑ جاتے ہیں",
        "منطق کا تقاضا ہے کہ آپ A کو الٹیں اور طاق عدد 7 کو الٹیں (کیونکہ اگر 7 کے پیچھے وول نکلا تو اصول جھوٹا ہو جائے گا)۔ مگر انسانی ذہن منفی ثبوت ڈھونڈنے کی بجائے تصدیق کی طرف بھاگتا ہے۔"
    ),
    (
        "In Prospect Theory, why do human beings experience roughly twice as much psychological pain from losing $100 as they do pleasure from gaining $100?",
        ["Loss aversion: human subjective value functions are steeper in the negative domain than in the positive domain", "Money burns the skin", "Losses are taxed higher", "Bankers charge fees on lost cash"],
        "Loss aversion: human subjective value functions are steeper in the negative domain than in the positive domain",
        "Kahneman and Tversky proved value is defined over gains and losses relative to a reference point. The loss aversion coefficient lambda is typically between 1.5 and 2.5.",
        "نقصان سے خوف کا نظریہ (Loss Aversion): انسان کو 100 ڈالر کے نقصان کا صدمہ اسی 100 ڈالر کے منافع کی خوشی کے مقابلے میں دگنا شدید کیوں محسوس ہوتا ہے؟",
        ["نقصان سے نفرت (Loss Aversion): انسانی نفسیات کا پیمانہ نفع کے مقابلے میں نقصان کی تکلیف کو دوگنا گہرا ریکارڈ کرتا ہے", "پیسہ جلد کو جلا دیتا ہے", "نقصان پر زیادہ ٹیکس لگتا ہے", "بینک کھوئے ہوئے پیسوں پر فیس لیتے ہیں"],
        "نقصان سے نفرت (Loss Aversion): انسانی نفسیات کا پیمانہ نفع کے مقابلے میں نقصان کی تکلیف کو دوگنا گہرا ریکارڈ کرتا ہے",
        "ارتقائی طور پر بقا کے لیے نقصان سے بچنا خوشی حاصل کرنے سے زیادہ اہم تھا۔ اسی لیے 100 روپے کھونا جتنا رنج دیتا ہے، 100 روپے ملنا اتنی خوشی نہیں دے پاتا۔"
    ),
    (
        "Why does the Dunning-Kruger Effect cause novices with minimal competence in a domain to severely overestimate their abilities?",
        ["The lack of metacognitive skill needed to perform well also prevents them from recognizing their own incompetence", "Novices read too many books", "Experts lie to novices", "Exams are designed too easy"],
        "The lack of metacognitive skill needed to perform well also prevents them from recognizing their own incompetence",
        "Dunning and Kruger found that poor performers suffer a double curse: their lack of expertise leads to mistakes, and their deficit in expertise blinds them to evaluating quality accurately.",
        "ڈننگ کروگر اثر (Dunning-Kruger Effect): کسی نئے میدان میں کم علم اور نابلد افراد اپنی صلاحیتوں کا غیر معمولی حد تک زیادہ اور جھوٹا اندازہ کیوں لگاتے ہیں؟",
        ["جس علم کی کمی ان سے غلطیاں کرواتی ہے، وہی کمی انہیں اپنی ہی نااہلی اور جہالت کو سمجھنے سے بھی محروم رکھتی ہے", "نوآموز افراد بہت زیادہ کتابیں پڑھتے ہیں", "ماہرین نئے لوگوں سے جھوٹ بولتے ہیں", "امتحانات بہت آسان بنائے جاتے ہیں"],
        "جس علم کی کمی ان سے غلطیاں کرواتی ہے، وہی کمی انہیں اپنی ہی نااہلی اور جہالت کو سمجھنے سے بھی محروم رکھتی ہے",
        "ایک اناڑی کو یہ معلوم ہی نہیں ہوتا کہ وہ کیا کچھ نہیں جانتا۔ جب تک انسان کسی علم کی گہرائی میں نہ اترے، وہ اپنے معمولی علم کو ہی کل کائنات سمجھ کر غرور کا شکار رہتا ہے۔"
    ),
    (
        "Why does stating an arbitrary initial number (like spinning a roulette wheel) heavily distort subsequent quantitative estimates by judges and negotiators (Anchoring Bias)?",
        ["The brain anchors to the initial value and makes insufficient adjustments along a subjective continuum", "High numbers induce sleepiness", "The anchor erases mathematical memory", "Judges dislike calculations"],
        "The brain anchors to the initial value and makes insufficient adjustments along a subjective continuum",
        "Tversky and Kahneman showed people adjust their estimate away from the anchor until reaching a boundary of plausibility, systematically terminating adjustment prematurely.",
        "اینکرنگ تعصب (Anchoring Bias): سودے بازی یا عدالتی فیصلوں میں پہلے سے بولا گیا کوئی بھی بے تکا عدد لوگوں کے حتمی تخمینے کو اپنی طرف کیوں کھینچ لیتا ہے؟",
        ["انسانی دماغ ابتدائی نمبر پر لنگر (Anchor) انداز ہو جاتا ہے اور اس سے آگے یا پیچھے ناکافی ایڈجسٹمنٹ کرتا ہے", "بڑے اعداد نیند کا باعث بنتے ہیں", "پہلا نمبر یادداشت مٹا دیتا ہے", "جج حساب کتاب سے بیزار ہوتے ہیں"],
        "انسانی دماغ ابتدائی نمبر پر لنگر (Anchor) انداز ہو جاتا ہے اور اس سے آگے یا پیچھے ناکافی ایڈجسٹمنٹ کرتا ہے",
        "اگر دکاندار پہلے 10 ہزار روپے مانگے، تو انسان 5 ہزار کو بہت بڑی رعایت سمجھ کر خوش ہو جاتا ہے، چاہے اصل چیز 1 ہزار کی ہو۔ پہلا عدد دماغ کے سوچنے کا دائرہ طے کر دیتا ہے۔"
    ),
    (
        "Why does learning that an individual is physically attractive or friendly bias people into assuming they are also intelligent, honest, and competent (the Halo Effect)?",
        ["A positive impression in one trait generates a global cognitive heuristic that colors all unrelated evaluations favorably", "Attractive people study harder", "Beauty reflects genetic integrity directly", "Honesty improves facial symmetry"],
        "A positive impression in one trait generates a global cognitive heuristic that colors all unrelated evaluations favorably",
        "Edward Thorndike identified the halo effect as the tendency for an overall impression of a person to influence how we feel and think about their character in unrelated domains.",
        "ہالو اثر (Halo Effect): کسی انسان کی ایک ظاہری خوبی (جیسے خوبصورتی یا خوش اخلاقی) دیکھ کر لوگ یہ کیوں مان لیتے ہیں کہ وہ ذہین اور ایماندار بھی ہوگا؟",
        ["ایک نمایاں مثبت خوبی پورے دماغ پر ایسا تاثر طاری کر دیتی ہے جو باقی تمام غیر متعلقہ اوصاف کو بھی خود بخود اچھا دکھاتا ہے", "خوبصورت لوگ زیادہ پڑھتے ہیں", "خوبصورتی شرافت کا لازمی ثبوت ہے", "سچ بولنے سے چہرہ خوبصورت ہوتا ہے"],
        "ایک نمایاں مثبت خوبی پورے دماغ پر ایسا تاثر طاری کر دیتی ہے جو باقی تمام غیر متعلقہ اوصاف کو بھی خود بخود اچھا دکھاتا ہے",
        "دماغ انسان کی مکمل شخصیت کا محنت سے جائزہ لینے کی بجائے ایک چمکتی ہوئی خوبی سے متاثر ہو کر اس کی عقل، دیانت اور قابلیت کے بارے میں بھی بلا ثبوت مثبت رائے قائم کر لیتا ہے۔"
    ),
    (
        "Why did dozens of bystanders fail to intervene or call emergency services during public medical crises (the Bystander Effect)?",
        ["Diffusion of responsibility: the presence of multiple onlookers dilutes each individual's perceived duty to act", "Bystanders are uniformly sadistic", "Emergency numbers are blocked in crowds", "Adrenaline paralyzes all muscles"],
        "Diffusion of responsibility: the presence of multiple onlookers dilutes each individual's perceived duty to act",
        "Darley and Latane proved bystander inaction stems from diffusion of responsibility and pluralistic ignorance: seeing others stay calm convinces observers the event is not urgent.",
        "تماشائیوں کا اثر (Bystander Effect): سر عام حادثے یا ایمرجنسی میں ہجوم جتنا بڑا ہو، زخمی کی مدد کے لیے کسی کے آگے بڑھنے کا امکان اتنا ہی کم کیوں ہو جاتا ہے؟",
        ["ذمہ داری کی تقسیم (Diffusion of Responsibility): ہر کوئی یہ سمجھتا ہے کہ کوئی دوسرا مدد کر لے گا، جس سے انفرادی احساس ذمہ داری ختم ہو جاتا ہے", "ہجوم میں سب ظالم ہوتے ہیں", "ہجوم میں ایمرجنسی فون نہیں ملتا", "خوف سے پٹھے جام ہو جاتے ہیں"],
        "ذمہ داری کی تقسیم (Diffusion of Responsibility): ہر کوئی یہ سمجھتا ہے کہ کوئی دوسرا مدد کر لے گا، جس سے انفرادی احساس ذمہ داری ختم ہو جاتا ہے",
        "اگر ایک بندہ اکیلا ہو تو وہ جانتا ہے کہ ساری ذمہ داری اس پر ہے اور وہ فوراً مدد کرتا ہے۔ لیکن 50 بندوں کے سامنے ہر کوئی دوسرے کا منہ دیکھتا ہے کہ شاید وہ قدم اٹھائے گا۔"
    ),
    (
        "In Solomon Asch's conformity experiments, why did 75 percent of participants conform to an obviously incorrect group answer about line lengths at least once?",
        ["Normative and informational social influence: the intense psychological urge to avoid social rejection or second-guess one's senses", "Participants developed sudden astigmatism", "Actors intimidated subjects physically", "The cards were out of focus"],
        "Normative and informational social influence: the intense psychological urge to avoid social rejection or second-guess one's senses",
        "Asch demonstrated the power of peer pressure. Subjects feared being perceived as strange, while others doubted their own perceptual judgment against a unanimous consensus.",
        "ایش کا موافقت کا تجربہ (Asch Conformity Experiment): جب تمام ایکٹرز نے جان بوجھ کر غلط لکیر کو بڑی کہا، تو 75 فیصد اصلی طلباء نے اپنی آنکھوں کو جھٹلا کر غلط جواب پر ہاں کیوں کہہ دی؟",
        ["معاشرتی ہم آہنگی اور رد ہونے کا خوف (Social Conformity): انسان گروپ سے الگ اور عجیب دکھنے سے بچنے کے لیے اپنی آنکھوں پر شک کرنے لگتا ہے", "تمام طلباء کی نظر اچانک کمزور ہو گئی تھی", "ایکٹرز طلباء کو دھمکی دے رہے تھے", "لکیریں دھندلی چھپی تھیں"],
        "معاشرتی ہم آہنگی اور رد ہونے کا خوف (Social Conformity): انسان گروپ سے الگ اور عجیب دکھنے سے بچنے کے لیے اپنی آنکھوں پر شک کرنے لگتا ہے",
        "انسان ایک سماجی جاندار ہے۔ جب اس کے آس پاس کے تمام لوگ متفقہ طور پر غلط بات کہہ رہے ہوں، تو تنہا کھڑے ہونے کا خوف انسان کو واضح سچائی سے بھی دستبردار کرا دیتا ہے۔"
    ),
    (
        "Why did 65 percent of ordinary participants in Stanley Milgram's experiment administer what they believed to be fatal 450-volt electric shocks to an innocent person?",
        ["Obedience to authority: shifting into an 'agentic state' where individuals surrender moral responsibility to perceived legitimate authority", "Subjects were sociopathic volunteers", "Shocks emitted laughing gas", "The lab paid massive bribes"],
        "Obedience to authority: shifting into an 'agentic state' where individuals surrender moral responsibility to perceived legitimate authority",
        "Milgram demonstrated that under the direction of an authoritative figure wearing a lab coat, moral agency dissolves as subjects view themselves as mere instruments of authority.",
        "ملگرام کا تجربہ (Milgram Obedience Experiment): عام شریف شہریوں نے ایک سائنسدان کے کہنے پر معصوم انسان کو 450 وولٹ کے جان لیوا کرنٹ کے جھٹکے دینے پر رضامندی کیوں ظاہر کی؟",
        ["حاکمیت کی اطاعت (Obedience to Authority): جب مستند اتھارٹی حکم دے تو انسان اپنی ذاتی اخلاقی ذمہ داری اتھارٹی کے کندھوں پر ڈال کر آلہ کار بن جاتا ہے", "شامل ہونے والے تمام لوگ ذہنی مریض تھے", "کرنٹ سے ہنسانے والی گیس نکلتی تھی", "لیب نے انہیں لاکھوں روپے رشوت دی تھی"],
        "حاکمیت کی اطاعت (Obedience to Authority): جب مستند اتھارٹی حکم دے تو انسان اپنی ذاتی اخلاقی ذمہ داری اتھارٹی کے کندھوں پر ڈال کر آلہ کار بن جاتا ہے",
        "سفید کوٹ پہنے محقق نے صرف اتنا کہا کہ 'تجربے کا تقاضا ہے کہ آپ جاری رکھیں'۔ انسان کے اندر طاقتور اتھارٹی کی اطاعت اتنی گہری ہے کہ وہ اپنے اندرونی ضمیر کو دبا دیتا ہے۔"
    ),
    (
        "In Leon Festinger's cognitive dissonance experiment, why did subjects paid only $1 to lie report actually enjoying a boring peg-turning task far more than subjects paid $20?",
        ["To resolve internal psychological conflict without financial justification, they changed their internal attitude to justify the lie", "One-dollar bills carried perfume", "Twenty dollars made subjects cynical", "The pegs became smoother"],
        "To resolve internal psychological conflict without financial justification, they changed their internal attitude to justify the lie",
        "A $20 reward provided sufficient external justification for lying. A $1 reward created dissonance between self-image and lying, compelling subjects to self-convince that the task was fun.",
        "ادراکی تضاد (Cognitive Dissonance): بورنگ کام کے بعد جھوٹ بولنے کے لیے جن طلباء کو صرف 1 ڈالر ملا انہوں نے دل سے کام کو دلچسپ کیوں مانا، بنسبت ان کے جنہیں 20 ڈالر ملے تھے؟",
        ["اپنے ضمیر کے تضاد کو مٹانے کے لیے، کیونکہ 1 ڈالر کا لالچ جھوٹ بولنے کی تسلی بخش وجہ نہیں تھا، اس لیے دماغ نے اپنے یقین کو ہی بدل ڈالا", "ایک ڈالر کے نوٹ پر خوشبو لگی تھی", "بیس ڈالر لے کر لوگ سست ہو گئے تھے", "لکڑی کے کھونٹے نرم ہو گئے تھے"],
        "اپنے ضمیر کے تضاد کو مٹانے کے لیے، کیونکہ 1 ڈالر کا لالچ جھوٹ بولنے کی تسلی بخش وجہ نہیں تھا، اس لیے دماغ نے اپنے یقین کو ہی بدل ڈالا",
        "20 ڈالر والے جانتے تھے کہ انہوں نے پیسوں کے لیے جھوٹ بولا، مگر 1 ڈالر والے اپنے آپ کو جھوٹا نہیں مان سکتے تھے، چنانچہ اندرونی تضاد دور کرنے کے لیے ان کے دماغ نے یقین کر لیا کہ کام واقعی اچھا تھا۔"
    ),
    (
        "Why do over 90 percent of licensed automobile drivers evaluate their driving skills as 'well above the median average' (the Lake Wobegon Effect)?",
        ["Illusory superiority: individuals define ambiguous evaluation criteria using their own unique personal strengths", "Speedometers read high", "Average drivers lose their licenses", "Highways are built downhill"],
        "Illusory superiority: individuals define ambiguous evaluation criteria using their own unique personal strengths",
        "People define competence egocentrically (a fast driver defines skill as reaction time; a slow driver defines it as caution), mathematically skewing subjective self-assessments upward.",
        "لیک ووبیگن اثر (Lake Wobegon Effect / Illusory Superiority): 90 فیصد سے زیادہ ڈرائیور خود کو اوسط سے زیادہ ماہر اور بہترین ڈرائیور کیوں سمجھتے ہیں؟",
        ["فوقیت کا وہم (Illusory Superiority): ہر انسان اچھے ڈرائیور کی تعریف اپنے ذاتی انداز اور خوبیوں کے مطابق گھڑ لیتا ہے", "گاڑیوں کے سپیڈومیٹر تیز چلتے ہیں", "عام ڈرائیوروں کے لائسنس ضبط ہو جاتے ہیں", "موٹر وے پر نیچے کی طرف ڈھلوان ہوتی ہے"],
        "فوقیت کا وہم (Illusory Superiority): ہر انسان اچھے ڈرائیور کی تعریف اپنے ذاتی انداز اور خوبیوں کے مطابق گھڑ لیتا ہے",
        "تیز گاڑی چلانے والا سمجھتا ہے کہ وہ حاضر دماغ ہے، اور دھیمی چلانے والا سمجھتا ہے کہ وہ محتاط ہے۔ ہر کوئی اچھائی کا معیار اپنے گرد بنا کر خود کو دوسروں سے بہتر سمجھنے لگتا ہے۔"
    ),
    (
        "Why do individuals consistently rate generic horoscope personality profiles as uniquely and astoundingly accurate to themselves (the Barnum / Forer Effect)?",
        ["People project specific personal meaning onto vague, universally applicable statements that carry high social desirability", "Astrologers observe planetary gravity", "Constellations emit radio signals", "Horoscopes are written individually"],
        "People project specific personal meaning onto vague, universally applicable statements that carry high social desirability",
        "Bertram Forer demonstrated subjects rated vague text ('you have a great need for other people to like you') as 4.3/5 in accuracy because people instinctively validate flattering generalities.",
        "بارنم اثر (Barnum / Forer Effect): لوگ اخبار میں لکھے زائچوں اور برجوں کے عام بیانات کو پڑھ کر یہ کیوں یقین کر لیتے ہیں کہ یہ خاص ان کی شخصیت کے لیے لکھا گیا ہے؟",
        ["انسان مبہم اور عام جملوں میں اپنے ذاتی واقعات اور پسندیدہ اوصاف خود بخود تلاش کر کے جوڑ لیتا ہے", "نجومی سیاروں کی کشش ناپتے ہیں", "ستارے ریڈیو سگنل بھیجتے ہیں", "ہر انسان کا زائچہ الگ چھپتا ہے"],
        "انسان مبہم اور عام جملوں میں اپنے ذاتی واقعات اور پسندیدہ اوصاف خود بخود تلاش کر کے جوڑ لیتا ہے",
        "جیسے 'آپ بظاہر مضبوط مگر اندر سے حساس ہیں'۔ یہ جملہ دنیا کے ہر انسان پر صادق آتا ہے۔ مگر پڑھنے والا سمجھتا ہے کہ نجومی نے اس کے دل کا راز جان لیا ہے۔"
    ),
    (
        "Why do corporate managers and governments continue pouring billions into doomed, failing projects rather than canceling them (the Sunk Cost Fallacy)?",
        ["Irrational honoring of past unrecoverable investments to avoid admitting failure and realizing a psychological loss", "Canceling requires purchasing extra cement", "Doomed projects always recover eventually", "Auditors forbid terminating contracts"],
        "Irrational honoring of past unrecoverable investments to avoid admitting failure and realizing a psychological loss",
        "Economic decision theory mandates forward-looking marginal cost-benefit analysis. Sunk costs are irrecoverable and should have zero weight on prospective future capital allocation.",
        "ڈوبے ہوئے سرمائے کا مغالطہ (Sunk Cost Fallacy): جب کوئی پروجیکٹ مسلسل ناکام ہو رہا ہو، تب بھی حکومتیں اور کمپنیاں اس میں مزید اربوں روپے کیوں جھونکتی چلی جاتی ہیں؟",
        ["ماضی میں لگائے گئے ناقابل واپسی پیسوں کو جائز ثابت کرنے اور نقصان کے اعتراف سے بچنے کی نفسیاتی ضد", "پروجیکٹ روکنے پر نیا سیمنٹ خریدنا پڑتا ہے", "ہر ڈوبتا پروجیکٹ آخر میں کامیاب ہوتا ہے", "آڈیٹرز کام روکنے سے منع کرتے ہیں"],
        "ماضی میں لگائے گئے ناقابل واپسی پیسوں کو جائز ثابت کرنے اور نقصان کے اعتراف سے بچنے کی نفسیاتی ضد",
        "عقلمندی یہ ہے کہ آئندہ کے فائدے کو دیکھا جائے۔ مگر انسان سوچتا ہے کہ 'ہم پہلے ہی 50 کروڑ لگا چکے ہیں، اب کیسے پیچھے ہٹیں'، اور مزید 50 کروڑ ڈبو دیتا ہے۔"
    ),
    (
        "In educational psychology, how does arbitrarily telling teachers that certain random students are 'intellectual bloomers' cause those students to experience dramatic real IQ gains (the Pygmalion Effect)?",
        ["Teacher expectations subtly alter educator body language, feedback frequency, warmth, and cognitive challenge", "Bloomers receive special secret textbooks", "Teachers falsify final exam scores", "IQ tests adapt to teacher names"],
        "Teacher expectations subtly alter educator body language, feedback frequency, warmth, and cognitive challenge",
        "Robert Rosenthal demonstrated a self-fulfilling prophecy: teachers granted higher expectations gave students more time to answer, clearer feedback, and greater encouragement.",
        "پگمیلیئن اثر (Pygmalion Effect): اگر اساتذہ کو جھوٹ موٹ بتا دیا جائے کہ فلاں چند عام بچے غیر معمولی ذہین ہیں، تو سال کے آخر میں ان بچوں کی اصل ذہانت اور نمبر واقعی کیوں بڑھ جاتے ہیں؟",
        ["استاد کے بلند ذہنی تاثرات ان بچوں کے ساتھ رویے، شفقت، توجہ اور حوصلہ افزائی کو غیر شعوری طور پر بہتر بنا دیتے ہیں", "ان بچوں کو خفیہ کتابیں دی جاتی ہیں", "اساتذہ نمبروں میں ہیرا پھیری کرتے ہیں", "ٹیسٹ استاد کے نام پر بدل جاتے ہیں"],
        "استاد کے بلند ذہنی تاثرات ان بچوں کے ساتھ رویے، شفقت، توجہ اور حوصلہ افزائی کو غیر شعوری طور پر بہتر بنا دیتے ہیں",
        "جب استاد کو یقین ہو کہ بچہ باصلاحیت ہے، تو وہ اسے سمجھانے کے لیے زیادہ وقت دیتا ہے اور غلطی پر ڈانٹنے کی بجائے حوصلہ دیتا ہے، جس سے بچہ سچ مچ ترقی کر جاتا ہے۔"
    ),
    (
        "Why did factory workers at Western Electric improve their manufacturing productivity every time lighting was changed—whether the lights were made brighter OR dimmer (the Hawthorne Effect)?",
        ["Subjects modified their behavior in response to the awareness of being observed and receiving organizational attention", "Dim light sharpens human eyesight", "Bulb heat energized factory tools", "Supervisors replaced workers secretly"],
        "Subjects modified their behavior in response to the awareness of being observed and receiving organizational attention",
        "The Hawthorne experiments showed that social and psychological conditions—specifically the novel attention of researchers—had a larger impact on output than physical workplace variables.",
        "ہوتھورن اثر (Hawthorne Effect): ایک فیکٹری میں لائٹیں تیز کی گئیں تو مزدوروں نے پیداوار بڑھا دی، اور جب لائٹیں مدہم کی گئیں تب بھی پیداوار بڑھ گئی۔ اس کی اصل وجہ کیا تھی؟",
        ["مزدور روشنی کی وجہ سے نہیں بلکہ اس احساس کی وجہ سے زیادہ محنت کر رہے تھے کہ انتظامیہ اور محققین ان پر خصوصی توجہ دے رہے ہیں", "مدہم روشنی میں آنکھیں تیز ہو جاتی ہیں", "بلب کی گرمی نے مشینوں کو طاقت دی", "نگرانوں نے پرانے مزدور بدل دیے تھے"],
        "مزدور روشنی کی وجہ سے نہیں بلکہ اس احساس کی وجہ سے زیادہ محنت کر رہے تھے کہ انتظامیہ اور محققین ان پر خصوصی توجہ دے رہے ہیں",
        "یہ ثابت ہوا کہ کام کے ماحول کی فزیکل تبدیلی اتنی اہم نہیں جتنی یہ نفسیاتی تسکین کہ لوگ آپ کے کام کو مانیٹر کر رہے ہیں اور آپ کی اہمیت تسلیم کر رہے ہیں۔"
    ),
    (
        "Why does administering a completely inert sugar pill in clinical trials relieve pain and trigger genuine biochemical endorphin release in patients (the Placebo Effect)?",
        ["Psychological expectation and conditioning stimulate descending analgesic pathways in the brain, releasing real endogenous opioids", "Sugar acts as a chemical narcotic", "Pain nerves dissolve in glucose", "Doctors practice hypnosis during pills"],
        "Psychological expectation and conditioning stimulate descending analgesic pathways in the brain, releasing real endogenous opioids",
        "Neuroimaging confirms placebo analgesia activates the prefrontal cortex and rostral anterior cingulate, driving real mu-opioid receptor binding in the spinal cord.",
        "پلاسیبو اثر (Placebo Effect): محض چینی کی بے اثر گولی کھا کر مریضوں کا شدید درد اور بیماری کی علامات سچ مچ ختم کیوں ہو جاتی ہیں؟",
        ["صحت یابی کی پختہ نفسیاتی امید دماغ کو اینڈورفنز اور قدرتی درد کش کیمیکلز خارج کرنے پر آمادہ کر دیتی ہے", "چینی ایک نشہ آور دوا کا کام کرتی ہے", "درد کی رگیں گلوکوز میں گھل جاتی ہیں", "ڈاکٹر گولی دیتے وقت ہپناٹائز کرتے ہیں"],
        "صحت یابی کی پختہ نفسیاتی امید دماغ کو اینڈورفنز اور قدرتی درد کش کیمیکلز خارج کرنے پر آمادہ کر دیتی ہے",
        "یہ کوئی محض وہم نہیں بلکہ دماغ کا ٹھوس حیاتیاتی ردعمل ہے۔ دوا ملنے کی امید پر دماغ خود اپنے اندر قدرتی افیون اور درد کش اجزاء بنا کر جسم کو بھیج دیتا ہے۔"
    ),
    (
        "In the Rubber Hand Illusion, why does synchronous brushing of a visible fake rubber hand and a hidden real hand cause subjects to feel physical sensations on the rubber hand?",
        ["Multisensory integration: the brain resolves visual-tactile synchrony by updating its internal cortical body schema to adopt the rubber limb", "The rubber conducts bioelectric nerves", "Static electricity jumps across air", "The real hand goes numb from cold"],
        "Multisensory integration: the brain resolves visual-tactile synchrony by updating its internal cortical body schema to adopt the rubber limb",
        "When visual tactile cues match synchronized somatic sensations, the brain's parietal cortex overrides proprioception, remapping body ownership onto the visible object.",
        "ربڑ کے ہاتھ کا وہم (Rubber Hand Illusion): جب سامنے رکھے نقلی ربڑ کے ہاتھ اور پردے کے پیچھے چھپے اصلی ہاتھ پر بیک وقت برش پھیرا جائے تو انسان کو نقلی ہاتھ اپنا ہاتھ کیوں لگنے لگتا ہے؟",
        ["دماغ بصری اور حسی سگنلز کے ایک ساتھ ملنے پر اپنے جسم کے اندرونی نقشے کو اپ ڈیٹ کر کے نقلی ہاتھ کو اپنا حصہ تسلیم کر لیتا ہے", "ربڑ کا ہاتھ برقی لہریں بھیجتا ہے", "جامد بجلی ہوا کے ذریعے منتقل ہوتی ہے", "اصلی ہاتھ ٹھنڈا ہو کر بے حس ہو جاتا ہے"],
        "دماغ بصری اور حسی سگنلز کے ایک ساتھ ملنے پر اپنے جسم کے اندرونی نقشے کو اپ ڈیٹ کر کے نقلی ہاتھ کو اپنا حصہ تسلیم کر لیتا ہے",
        "دماغ آنکھوں کی گواہی اور جلد کے احساس کو اکٹھا جوڑتا ہے۔ جب وہ ربڑ کے ہاتھ پر برش پھرتا دیکھتا ہے اور ویسا ہی چھونا محسوس کرتا ہے، تو وہ فوراً ربڑ کے ہاتھ پر ہاتھ کی حس منتقل کر دیتا ہے۔"
    ),
    (
        "Why does a patient with Capgras Delusion insist that their spouse or mother is an identical imposter or clone, despite recognizing their face perfectly?",
        ["The neurological pathway linking facial recognition to emotional autonomic arousal is damaged, creating visual familiarity without affective feeling", "The spouse underwent secret surgery", "The patient's optic nerve reversed", "Mirror neurons went blind"],
        "The neurological pathway linking facial recognition to emotional autonomic arousal is damaged, creating visual familiarity without affective feeling",
        "V.S. Ramachandran showed that while ventral facial recognition (fusiform gyrus) is intact, the connection to the amygdala is severed, causing an uncanny lack of emotional warmth.",
        "کیپگراس وہم (Capgras Delusion): ایک مریض اپنے جیون ساتھی یا ماں کا چہرہ بالکل پہچاننے کے باوجود یہ ضد کیوں کرتا ہے کہ یہ کوئی بہروپیا ہے جس نے اس کا روپ دھارا ہوا ہے؟",
        ["چہرہ پہچاننے والے حصے اور جذباتی احساس جگانے والے دماغی راستے کے درمیان رابطہ ٹوٹ جاتا ہے، جس سے چہرہ جانا پہچانا لگنے کے باوجود دلی اپنائیت کا سگنل غائب ہو جاتا ہے", "ساتھی نے چپکے سے چہرے کی سرجری کرائی ہوتی ہے", "مریض کی بصری رگ الٹی ہو جاتی ہے", "دماغ کے آئینے کے خلیات اندھے ہو جاتے ہیں"],
        "چہرہ پہچاننے والے حصے اور جذباتی احساس جگانے والے دماغی راستے کے درمیان رابطہ ٹوٹ جاتا ہے، جس سے چہرہ جانا پہچانا لگنے کے باوجود دلی اپنائیت کا سگنل غائب ہو جاتا ہے",
        "عام انسان ماں کو دیکھ کر جذباتی گرمجوشی محسوس کرتا ہے۔ مریض چہرہ تو ماں کا دیکھتا ہے مگر اندرونی گرمجوشی نہیں ملتی، اس لیے اس کا دماغ یہ الٹا نتیجہ نکالتا ہے کہ یہ میری ماں نہیں بلکہ ہم شکل بہروپیا ہے۔"
    ),
    (
        "Why does a person with Cotard's Syndrome firmly believe they are literally dead, putrefying, or completely devoid of internal organs?",
        ["Severe dual failure of sensory emotional processing combined with complete cognitive misattribution and profound depressive derealization", "The heart stops pumping blood", "Body temperature falls to 0 Celsius", "Blood cells become transparent"],
        "Severe dual failure of sensory emotional processing combined with complete cognitive misattribution and profound depressive derealization",
        "Cotard delusion represents the ultimate culmination of Capgras: all sensory experience is completely disconnected from affective significance, leading to the nihilistic delusion of nonexistence.",
        "کوٹارڈ سنڈروم (Cotard's Syndrome): اس نایاب مرض کا شکار انسان سچے دل سے یہ دعویٰ کیوں کرنے لگتا ہے کہ وہ مر چکا ہے، اس کی لاش سڑ رہی ہے یا اس کے اندر دل اور پھیپھڑے موجود ہی نہیں ہیں؟",
        ["دماغ کے تمام حسی راستوں سے جذباتی سگنلز کا مکمل کٹ جانا اور شدید ترین اداسی کا دماغی نظام کو وجود سے بیگانہ کر دینا", "مریض کا دل واقعی دھڑکنا بند کر دیتا ہے", "جسم کا درجہ حرارت صفر ہو جاتا ہے", "خون کے سرخ خلیات شفاف ہو جاتے ہیں"],
        "دماغ کے تمام حسی راستوں سے جذباتی سگنلز کا مکمل کٹ جانا اور شدید ترین اداسی کا دماغی نظام کو وجود سے بیگانہ کر دینا",
        "جب دنیا کا کوئی بھی احساس مریض کے دماغ میں زندگی اور جذبے کی لہر پیدا نہ کر سکے، تو دماغ اس مکمل ویرانی اور بے حسی کی واحد منطقی وضاحت یہ نکالتا ہے کہ میں دراصل مر چکا ہوں۔"
    ),
    (
        "How can a patient experiencing severe phantom limb pain in an amputated arm obtain rapid relief using V.S. Ramachandran's mirror box?",
        ["Visual feedback of the intact arm reflecting in the mirror tricks the motor cortex into relaxing clenched phantom muscles", "The mirror focuses infrared heat", "Glass absorbs nerve pain signals", "The reflection numbs the eyes"],
        "Visual feedback of the intact arm reflecting in the mirror tricks the motor cortex into relaxing clenched phantom muscles",
        "The brain's motor map continues sending spasm signals to the missing limb without receiving sensory feedback. Seeing the reflection 'unclench' visually resolves learned paralysis.",
        "فینٹم لمب اور آئینہ باکس (Mirror Box Therapy): کٹے ہوئے بازو کے شدید درد کو مریض آئینے کے ایک ڈبے میں تندرست بازو دیکھ کر فوری طور پر کیسے ختم کر لیتا ہے؟",
        ["آئینے میں تندرست بازو کا عکس دیکھ کر دماغ کو بصری دھوکہ ملتا ہے کہ کٹا ہوا بازو کھل گیا ہے، جس سے موٹر کارٹیکس کا کھچاؤ پرسکون ہو جاتا ہے", "آئینہ انفراریڈ گرمی پیدا کرتا ہے", "شیشہ درد کے اعصابی سگنل جذب کر لیتا ہے", "عکس دیکھنے سے آنکھیں سن ہو جاتی ہیں"],
        "آئینے میں تندرست بازو کا عکس دیکھ کر دماغ کو بصری دھوکہ ملتا ہے کہ کٹا ہوا بازو کھل گیا ہے، جس سے موٹر کارٹیکس کا کھچاؤ پرسکون ہو جاتا ہے",
        "دماغ کٹے ہوئے ہاتھ کو مٹھی بند کرنے کا سگنل بھیجتا رہتا ہے مگر بازو نہ ہونے سے واپسی کی تصدیق نہیں ملتی۔ آئینے میں ہاتھ کھلتا دیکھ کر دماغ کو تسلی ہو جاتی ہے اور درد کے سگنل بند ہو جاتے ہیں۔"
    ),
    (
        "Why do individuals with Synesthesia experience specific colors when hearing musical chords, or specific flavors when reading words?",
        ["Cross-activation and hyper-connectivity between adjacent specialized cortical sensory processing areas in the brain", "Ears contain hidden taste buds", "Eye retinas leak fluid into tongues", "Auditory bones rub against optic nerves"],
        "Cross-activation and hyper-connectivity between adjacent specialized cortical sensory processing areas in the brain",
        "Synesthesia arises from incomplete neural pruning during early development, preserving structural cross-talk between adjacent regions (e.g. V4 color area and grapheme area).",
        "سائینستھیزیا (Synesthesia): اس حالت کے حامل افراد موسیقی کا سُر سن کر مخصوص رنگ کیوں دیکھنے لگتے ہیں یا لفظ پڑھ کر ان کے منہ میں مخصوص ذائقہ کیوں آ جاتا ہے؟",
        ["دماغ کے مختلف حسی مراکز (جیسے سننے اور رنگ دیکھنے کے شعبے) کے درمیان اعصابی رابطوں کی آپس میں اضافی جڑت اور ملاپ", "کانوں کے اندر چکھنے کی حس ہوتی ہے", "آنکھ کا پانی زبان پر گرتا ہے", "کان کی ہڈیاں بصری رگوں سے رگڑ کھاتی ہیں"],
        "دماغ کے مختلف حسی مراکز (جیسے سننے اور رنگ دیکھنے کے شعبے) کے درمیان اعصابی رابطوں کی آپس میں اضافی جڑت اور ملاپ",
        "بچپن میں دماغ کی وائرنگ بنتے وقت ان کے مختلف حسی راستے الگ ہونے کی بجائے آپس میں جڑے رہ گئے۔ چنانچہ جب آواز کا مرکز جاگتا ہے تو رنگوں کا مرکز بھی ساتھ ہی روشن ہو جاتا ہے۔"
    ),
    (
        "Why can patients with Cortical Blindness (Blindsight) accurately point to moving lights across a room while swearing they see absolute pitch-black darkness?",
        ["Subcortical visual pathways (superior colliculus) process spatial location independently of conscious primary visual cortex (V1)", "Light travels through forehead skin", "Patients hear the photons hum", "Memory recreates the lights"],
        "Subcortical visual pathways (superior colliculus) process spatial location independently of conscious primary visual cortex (V1)",
        "Lesions to V1 extinguish conscious visual awareness, but ancient retinotectal pathways bypass V1 directly to the midbrain, enabling unconscious motor navigation.",
        "بلائنڈ سائٹ (Blindsight): پردہ بصارت (V1) تباہ ہونے کے باعث مکمل نابینا مریض کمرے میں چلتی ہوئی روشنی کی طرف بالکل درست انگلی کیسے اٹھا لیتے ہیں حالانکہ وہ قسم کھاتے ہیں کہ انہیں کچھ نظر نہیں آ رہا؟",
        ["دماغ کا قدیم نچلا بصری راستہ (Superior Colliculus) شعوری آگاہی کے بغیر بھی جگہ اور حرکت کو خود بخود بھانپ لیتا ہے", "روشنی پیشانی کی جلد سے اندر داخل ہوتی ہے", "مریض روشنی کے ذرات کی گونج سنتے ہیں", "یادداشت روشنیوں کو دوبارہ بنا دیتی ہے"],
        "دماغ کا قدیم نچلا بصری راستہ (Superior Colliculus) شعوری آگاہی کے بغیر بھی جگہ اور حرکت کو خود بخود بھانپ لیتا ہے",
        "شعوری دیکھنے کے لیے کارٹیکس درکار ہے، مگر جگہ اور حرکت کا قدیم ترین خودکار نظام دماغ کے نچلے تنے سے جڑا ہوتا ہے جو شعور کو خبر کیے بغیر ہاتھ کو صحیح سمت موڑ دیتا ہے۔"
    ),
    (
        "Why does a patient with Alien Hand Syndrome find their left hand buttoning up a shirt while their right hand is unbuttoning it against their conscious will?",
        ["Damage to the corpus callosum or medial frontal cortex isolates motor intentions between hemispheres, producing autonomous goal-directed limb behavior", "Nerves in the arm grow independent brains", "Blood clots stimulate muscular twitching", "Reflex arcs bypass spinal cords"],
        "Damage to the corpus callosum or medial frontal cortex isolates motor intentions between hemispheres, producing autonomous goal-directed limb behavior",
        "Disconnection between frontal supplementary motor areas and contralateral inhibition lets one hemisphere execute learned motor routines without the conscious awareness of the other.",
        "خلائی ہاتھ کا سنڈروم (Alien Hand Syndrome): مریض کا ایک ہاتھ قمیض کے بٹن بند کر رہا ہوتا ہے جبکہ دوسرا ہاتھ اس کی مرضی کے خلاف خود بخود بٹن کھولنا کیوں شروع کر دیتا ہے؟",
        ["دماغ کے دونوں حصوں کو جوڑنے والے رابطے (Corpus Callosum) کے کٹ جانے سے ایک نصف حصہ دوسرے کی مرضی کے بغیر ہاتھ سے خود مختار کام کروانے لگتا ہے", "بازو کی رگوں میں الگ دماغ اگ آتا ہے", "خون کے لوتھڑے پٹھوں کو کھینچتے ہیں", "ریڑھ کی ہڈی کا نظام کٹ جاتا ہے"],
        "دماغ کے دونوں حصوں کو جوڑنے والے رابطے (Corpus Callosum) کے کٹ جانے سے ایک نصف حصہ دوسرے کی مرضی کے بغیر ہاتھ سے خود مختار کام کروانے لگتا ہے",
        "دماغ کا دایاں اور بایاں نصف مختلف بازوؤں کو چلاتے ہیں۔ جب دونوں کا درمیانی رابطہ کٹ جائے تو دایاں دماغ آزادانہ فیصلے کر کے بائیں ہاتھ سے کام کروانے لگتا ہے اور انسان کو لگتا ہے کہ ہاتھ بے قابو ہو گیا ہے۔"
    ),
    (
        "In split-brain research, when an image of a snow shovel is flashed exclusively to the mute right hemisphere and a chicken claw to the left hemisphere, why does the patient's left hand pick the shovel while their mouth claims they picked it 'to clean chicken coops'?",
        ["The left hemisphere is a compulsive interpreter: it invents plausible post-hoc narratives to rationalize actions executed outside its awareness", "The right hemisphere controls vocal cords", "The optic nerve crosses backward", "Chickens prefer shovels"],
        "The left hemisphere is a compulsive interpreter: it invents plausible post-hoc narratives to rationalize actions executed outside its awareness",
        "Michael Gazzaniga discovered the 'left hemisphere interpreter', a module that weaves coherent retrospective justifications for behaviors generated by subcortical or disconnected modules.",
        "منقسم دماغ کے تجربات (Split-Brain Interpreter): جب بائیں ہاتھ نے بیلچے کا انتخاب کیا تو بولنے والے دماغ نے یہ جھوٹا بہانہ کیوں گھڑ لیا کہ 'میں نے مرغیوں کا ڈربا صاف کرنے کے لیے بیلچہ چنا'؟",
        ["دماغ کا بایاں بولنے والا حصہ ایک لازمی مفسر (Interpreter) ہے، وہ لاعلمی میں کیے گئے کاموں کی بھی فوری من گھڑت مگر معقول تاویل تیار کر لیتا ہے", "دایاں دماغ بولنے والی رگوں کو چلاتا ہے", "بصری رگ الٹی جڑ جاتی ہے", "مرغیاں بیلچے پسند کرتی ہیں"],
        "دماغ کا بایاں بولنے والا حصہ ایک لازمی مفسر (Interpreter) ہے، وہ لاعلمی میں کیے گئے کاموں کی بھی فوری من گھڑت مگر معقول تاویل تیار کر لیتا ہے",
        "بولنے والے بائیں دماغ کو معلوم ہی نہیں تھا کہ دائیں دماغ کو برف کا منظر دکھایا گیا تھا۔ مگر جب اس نے ہاتھ کو بیلچہ اٹھاتے دیکھا تو شرمندگی سے بچنے کے لیے فوراً جھوٹی منطق گھڑ لی۔"
    ),
    (
        "Why can amnesia patient Clive Wearing sit at a piano and play complex Bach fugues with virtuosic mastery, yet forget a conversation that happened 10 seconds ago?",
        ["Damage to the hippocampus destroys declarative episodic memory, while procedural motor memory in the basal ganglia and cerebellum remains entirely intact", "Muscle fibers store sheet music notes", "Pianos emit tactile radio waves", "Auditory nerves bypass the brain"],
        "Damage to the hippocampus destroys declarative episodic memory, while procedural motor memory in the basal ganglia and cerebellum remains entirely intact",
        "Episodic memory (recalling events and facts) depends on medial temporal lobe structures, whereas procedural motor memory (skills like piano playing) is localized in the cerebellum and striatum.",
        "کلائیو ویئرنگ کا معمہ (Clive Wearing Amnesia): شدید بھولنے کی بیماری کا شکار مریض جو پچھلے 10 سیکنڈز کی بات بھول جاتا ہے، وہ پیانو پر پیانو ماسٹرز کی مشکل ترین دھنیں روانی سے کیسے بجا لیتا ہے؟",
        ["ہپوکیمپس تباہ ہونے سے واقعات کی یادداشت ختم ہو جاتی ہے مگر مہارتوں اور ہنر کی یادداشت (Procedural Memory) دماغ کے دوسرے محفوظ حصوں میں قائم رہتی ہے", "ہاتھ کے پٹھے موسیقی کے نوٹ یاد رکھتے ہیں", "پیانو سے لہریں نکلتی ہیں", "کان کی رگیں دماغ کو بائی پاس کرتی ہیں"],
        "ہپوکیمپس تباہ ہونے سے واقعات کی یادداشت ختم ہو جاتی ہے مگر مہارتوں اور ہنر کی یادداشت (Procedural Memory) دماغ کے دوسرے محفوظ حصوں میں قائم رہتی ہے",
        "واقعات کو یاد رکھنا اور ہنر کا سیکھنا دماغ کے دو بالکل الگ الگ شعبے ہیں۔ پچھلی بات بھول جانے کے باوجود پیانو بجانے کا اعصابی نظام دماغ کے پچھلے حصے میں محفوظ رہتا ہے۔"
    ),
    (
        "When an iron tamping rod blasted entirely through railroad worker Phineas Gage's skull in 1848, he walked and talked immediately, yet his friends declared 'Gage was no longer Gage'. Why?",
        ["Destruction of the ventromedial prefrontal cortex shattered his emotional regulation, moral reasoning, and executive social personality", "The iron rod left toxic rust", "His vocal cords became coarse", "His blood pressure dropped"],
        "Destruction of the ventromedial prefrontal cortex shattered his emotional regulation, moral reasoning, and executive social personality",
        "Gage provided the first definitive evidence that the prefrontal cortex mediates executive social planning, impulse inhibition, and civilized moral judgment.",
        "فنیس گیج کا تاریخی واقعہ (Phineas Gage): جب لوہے کا موٹا سریہ ریلوے ملازم کے دماغ کے آر پار نکل گیا تو وہ زندہ بچ گیا اور بولنے لگا، مگر اس کے دوستوں نے کیوں کہا کہ 'گیج اب گیج نہیں رہا'؟",
        ["دماغ کے سامنے والے حصے (Prefrontal Cortex) کے تباہ ہونے سے اس کے اخلاق، جذباتی ضبط، تمیز اور سماجی شخصیت کا مکمل نظام درہم برہم ہو گیا تھا", "لوہے کے سریے نے زنگ چھوڑ دیا تھا", "اس کی آواز موٹی ہو گئی تھی", "اس کا بلڈ پریشر گر گیا تھا"],
        "دماغ کے سامنے والے حصے (Prefrontal Cortex) کے تباہ ہونے سے اس کے اخلاق، جذباتی ضبط، تمیز اور سماجی شخصیت کا مکمل نظام درہم برہم ہو گیا تھا",
        "اس تاریخی واقعے سے سائنس کو پہلی بار معلوم ہوا کہ انسان کی شرافت، صبر، اخلاقیات اور تمیز دماغ کے سامنے والے حصے میں بستی ہے۔ سریہ لگنے کے بعد وہ بدتمیز، جھگڑالو اور غیر ذمہ دار بن گیا۔"
    ),
    (
        "Why does a person who has their corpus callosum surgically severed (split-brain) fail to verbally name an object placed in their left hand while blindfolded?",
        ["Sensory input from the left hand travels to the right hemisphere, which has no direct access to the speech center in the left hemisphere", "The left hand loses all tactile feeling", "The right ear becomes deaf", "Blindfolds paralyze speech"],
        "Sensory input from the left hand travels to the right hemisphere, which has no direct access to the speech center in the left hemisphere",
        "Touch on the left hand routes to the right somatosensory cortex. Since speech centers (Broca/Wernicke) reside exclusively in the left hemisphere, the mute right hemisphere cannot verbalize the object.",
        "منقسم دماغ (Split-Brain Sensory Block): جب آنکھوں پر پٹی باندھ کر مریض کے بائیں ہاتھ میں چابی رکھی جائے تو وہ زبان سے اس کا نام بول کر کیوں نہیں بتا سکتا؟",
        ["بائیں ہاتھ کا حسی سگنل دائیں دماغ میں جاتا ہے، جس کا بولنے کے مرکز (جو کہ بائیں دماغ میں ہے) سے رابطہ کٹ چکا ہوتا ہے", "بایاں ہاتھ چھونے کی حس کھو بیٹھتا ہے", "دایاں کان بہرہ ہو جاتا ہے", "آنکھوں پر پٹی باندھنے سے آواز بند ہو جاتی ہے"],
        "بائیں ہاتھ کا حسی سگنل دائیں دماغ میں جاتا ہے، جس کا بولنے کے مرکز (جو کہ بائیں دماغ میں ہے) سے رابطہ کٹ چکا ہوتا ہے",
        "وہ مریض چابی کے استعمال کا اشارہ ہاتھ سے کر کے دکھا سکتا ہے، مگر چونکہ بولنے کا مرکز بائیں دماغ میں ہے اور دونوں دماغوں کا پل کٹا ہوا ہے، اس لیے وہ زبان سے نام ادا نہیں کر سکتا۔"
    ),
    (
        "Why did healthy psychological students assigned as guards in the Stanford Prison Experiment rapidly degenerate into cruel and abusive behavior (the Lucifer Effect)?",
        ["Deindividuation and situational role conformity: extreme systemic expectations and symbols of institutional power overwhelm individual moral compasses", "Guards suffered from food poisoning", "The basement had toxic gas", "Prisoners provoked guards physically"],
        "Deindividuation and situational role conformity: extreme systemic expectations and symbols of institutional power overwhelm individual moral compasses",
        "Philip Zimbardo showed that situations and assigned institutional roles exert overwhelming pressure, stripping personal accountability through uniforms, sunglasses, and absolute unchecked authority.",
        "اسٹینفورڈ کا قید خانے کا تجربہ (Stanford Prison Experiment / Lucifer Effect): عام شریف اور پرامن طلباء جب جیل کے چوکیدار بنے تو وہ محض چند دنوں میں ظالم اور اذیت پسند کیوں بن گئے؟",
        ["انفرادی شناخت کا خاتمہ اور حاکمانہ کردار کی اندھی پیروی (Deindividuation): طاقتور وردی اور غیر محدود اختیارات انسان کے ذاتی ضمیر اور اخلاق کو دبا دیتے ہیں", "گارڈز کے کھانے میں زہر مل گیا تھا", "تہہ خانے میں زہریلی گیس تھی", "قیدیوں نے گارڈز پر حملہ کیا تھا"],
        "انفرادی شناخت کا خاتمہ اور حاکمانہ کردار کی اندھی پیروی (Deindividuation): طاقتور وردی اور غیر محدود اختیارات انسان کے ذاتی ضمیر اور اخلاق کو دبا دیتے ہیں",
        "جب انسان کو مکمل بے لگام طاقت اور گمنامی (کالے چشمے اور وردی) دی جائے اور ادارہ جبر کی اجازت دے، تو شریف ترین انسان بھی خود کو دیے گئے ظالمانہ کردار میں پوری طرح ڈھل جاتا ہے۔"
    ),
]
