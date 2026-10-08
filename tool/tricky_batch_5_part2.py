# -*- coding: utf-8 -*-
"""
Tricky Batch 5 Part 2 (37 items).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why does Fitch's Paradox of Knowability logically prove that if all truths were potentially knowable, then every single truth must already be known right now?",
        ["Assuming an unknown truth exists (p and not-Kp) leads to a logical contradiction when the knowability operator is applied", "Human knowledge is stored in quantum computers", "Books contain all universal facts", "The brain cannot process false statements"],
        "Assuming an unknown truth exists (p and not-Kp) leads to a logical contradiction when the knowability operator is applied",
        "Frederic Fitch proved that if 'for all p: p -> Poss(Kp)', then inserting the unknown truth 'p and not-Kp' yields the impossible conclusion that one could know both p and that one does not know p.",
        "فچ کا علم کا معمہ (Fitch's Paradox of Knowability): منطق کا یہ قانون کیسے ثابت کرتا ہے کہ اگر کائنات کا ہر سچ جانا جا سکتا ہے، تو اس کا لازمی مطلب یہ ہے کہ کائنات کا ہر سچ پہلے سے ہی معلوم ہے؟",
        ["یہ ماننا کہ 'ایک سچائی موجود ہے جو نامعلوم ہے' جاننے کے اصول کے تحت ایک براہ راست منطقی تضاد بن جاتا ہے", "انسان کا علم کوانٹم کمپیوٹر میں محفوظ ہے", "کتابوں میں تمام حقائق لکھے ہیں", "دماغ جھوٹے بیانات نہیں سمجھ سکتا"],
        "یہ ماننا کہ 'ایک سچائی موجود ہے جو نامعلوم ہے' جاننے کے اصول کے تحت ایک براہ راست منطقی تضاد بن جاتا ہے",
        "اگر ہم کہیں کہ یہ جاننا ممکن ہے کہ 'ایک بات سچ ہے مگر کوئی نہیں جانتا'، تو جیسے ہی آپ اسے جانیں گے وہ بات خود بخود جھوٹی ہو جائے گی کہ کوئی نہیں جانتا۔ اس منطقی جال سے یہ معمہ جنم لیتا ہے۔"
    ),
    (
        "Why does Curry's Paradox allow a person to logically prove any arbitrary absurdity (such as 'The Moon is made of green cheese') using self-reference without any negation?",
        ["A self-referential conditional statement ('If this sentence is true, then X is true') validates itself through natural deduction", "Sentences about cheese bypass grammar rules", "The moon reflects yellow light", "Falsehoods convert into truths in winter"],
        "A self-referential conditional statement ('If this sentence is true, then X is true') validates itself through natural deduction",
        "Haskell Curry showed that defining sentence C = 'C -> B' allows deriving B via conditional proof and modus ponens without ever using logical negation (~), revealing paradoxes in naive logic.",
        "کری کا پیراڈاکس (Curry's Paradox): منطق کا یہ اصول بغیر کسی نفی کے کسی بھی بے تکی بات (جیسے 'چاند مکھن کا بنا ہے') کو مکمل سچ کیسے ثابت کر دیتا ہے؟",
        ["ایک ایسا خود حوالہ جملہ بنا کر جس کی شرط کے پورا ہونے کا دعویٰ خود بخود مطلوبہ نتیجے کو سچ تسلیم کرنے پر مجبور کر دیتا ہے", "مکھن کے جملے قواعد سے آزاد ہوتے ہیں", "چاند پیلی روشنی لوٹاتا ہے", "جھوٹ سردیوں میں سچ بن جاتا ہے"],
        "ایک ایسا خود حوالہ جملہ بنا کر جس کی شرط کے پورا ہونے کا دعویٰ خود بخود مطلوبہ نتیجے کو سچ تسلیم کرنے پر مجبور کر دیتا ہے",
        "اگر جملہ ہو: 'اگر یہ جملہ سچ ہے، تو چاند مکھن کا ہے'۔ اگر آپ جملے کو سچ مانیں تو شرط پوری ہو گئی اور چاند مکھن کا بن گیا، اور اگر جھوٹ مانیں تب بھی منطقی شرط پوری ہو جاتی ہے۔ یہ رسمی منطق کا ایک خطرناک نقائص ہے۔"
    ),
    (
        "Why did philosopher G.E. Moore describe sentences like 'It is raining outside, but I do not believe it' as a profound paradox (Moore's Paradox)?",
        ["The sentence is non-contradictory as an objective factual statement, yet asserting it openly produces an immediate pragmatic performative contradiction", "Rain drops extinguish human beliefs", "Beliefs require sunny weather", "Speech sounds cannot describe weather"],
        "The sentence is non-contradictory as an objective factual statement, yet asserting it openly produces an immediate pragmatic performative contradiction",
        "Moore showed that while 'P and not-Believes(P)' can be true of someone in third person, uttering it in first person violates the pragmatic implicature of assertion, which inherently claims belief in P.",
        "مور کا معمہ (Moore's Paradox): 'باہر بارش ہو رہی ہے، مگر مجھے اس کا یقین نہیں ہے' جملہ منطقی طور پر ممکن ہونے کے باوجود بولنے میں مضحکہ خیز اور ناممکن کیوں لگتا ہے؟",
        ["یہ بیان ایک معروضی حقیقت کے طور پر سچا ہو سکتا ہے مگر اپنی ہی زبان سے بولتے وقت یہ ایک زبردست عملی اور بیانیاتی تضاد پیدا کر دیتا ہے", "بارش کے قطرے یقین کو مٹا دیتے ہیں", "یقین کے لیے دھوپ ضروری ہے", "آوازیں موسم بیان نہیں کر سکتیں"],
        "یہ بیان ایک معروضی حقیقت کے طور پر سچا ہو سکتا ہے مگر اپنی ہی زبان سے بولتے وقت یہ ایک زبردست عملی اور بیانیاتی تضاد پیدا کر دیتا ہے",
        "کوئی دوسرا شخص آپ کے بارے میں کہہ سکتا ہے کہ باہر بارش ہے مگر اسے معلوم نہیں، مگر آپ خود یہ جملہ نہیں بول سکتے کیونکہ کسی بات کا دعویٰ کرنا خود بخود اس پر یقین رکھنے کا اعلان ہوتا ہے۔"
    ),
    (
        "What fundamental limitation on formal languages was established by Alfred Tarski's Undefinability Theorem in 1936?",
        ["Arithmetical truth cannot be defined within the language of formal arithmetic itself without encountering Liar Paradox contradictions", "Languages run out of alphabet symbols", "Grammar books cannot exceed 100 pages", "Computers cannot spell numbers"],
        "Arithmetical truth cannot be defined within the language of formal arithmetic itself without encountering Liar Paradox contradictions",
        "Tarski proved that any formal system expressive enough to define its own truth predicate True(x) allows constructing a diagonal Liar sentence: 'This sentence is not true', creating an immediate contradiction.",
        "تارسکی کا ناقابل تعریف ہونے کا تھیورم (Tarski's Undefinability Theorem): 1936 میں الفریڈ تارسکی نے زبان اور ریاضیاتی سچائی کی حدود کے بارے میں کیا ثابت کیا؟",
        ["ریاضی کی کوئی بھی زبان اپنے ہی اندر 'سچائی' (Truth) کا حتمی پیمانہ خود بیان نہیں کر سکتی ورنہ وہ 'جھوٹے کے معمے' میں پھنس جائے گی", "زبان کے حروف تہجی ختم ہو جاتے ہیں", "گرائمر سو صفحات سے زیادہ نہیں ہو سکتی", "کمپیوٹر ہندسوں کے ہجے نہیں کر سکتے"],
        "ریاضی کی کوئی بھی زبان اپنے ہی اندر 'سچائی' (Truth) کا حتمی پیمانہ خود بیان نہیں کر سکتی ورنہ وہ 'جھوٹے کے معمے' میں پھنس جائے گی",
        "اگر ریاضی کے اندر ہی 'یہ جملہ سچ ہے' کا الگورتھم ڈال دیا جائے تو 'یہ جملہ جھوٹا ہے' کی شکل میں پورا نظام بیٹھ جائے گا۔ اس لیے سچ کو پرکھنے کے لیے ہمیشہ ایک اس سے بڑی میٹا زبان درکار ہوتی ہے۔"
    ),
    (
        "According to Rice's Theorem in computer science, what semantic property of computer programs can be algorithmically decided?",
        ["None: any non-trivial semantic property regarding what a program actually computes is undecidable", "Whether a program has more than 5 lines", "Whether a program uses the letter 'x'", "Whether source code takes up disk space"],
        "None: any non-trivial semantic property regarding what a program actually computes is undecidable",
        "Henry Gordon Rice proved that for any non-trivial semantic property of partial recursive functions, there is no general algorithm to determine whether an arbitrary program exhibits that property, extending Turing's halting theorem.",
        "رائس کا تھیورم (Rice's Theorem): کمپیوٹر سائنس کا یہ قانون پروگرام کے کام کرنے کی صلاحیت کے بارے میں کیا فیصلہ سناتا ہے؟",
        ["کوئی بھی نہیں: کمپیوٹر پروگرام دراصل کیا نتیجہ اور مطلب نکالے گا، اس کی کسی بھی بامعنی صفت کا پہلے سے خودکار فیصلہ کرنا قطعی ناممکن ہے", "کیا پروگرام پانچ لائنوں سے بڑا ہے", "کیا پروگرام میں حرف x استعمال ہوا ہے", "کیا کوڈ ڈسک پر جگہ گھیرتا ہے"],
        "کوئی بھی نہیں: کمپیوٹر پروگرام دراصل کیا نتیجہ اور مطلب نکالے گا، اس کی کسی بھی بامعنی صفت کا پہلے سے خودکار فیصلہ کرنا قطعی ناممکن ہے",
        "کوڈ کے حروف گننا آسان ہے مگر یہ جاننا کہ کیا یہ پروگرام ہمیشہ پرائم نمبر دے گا یا کبھی وائرس بنے گا، اس کا کوئی عالمگیر الگورتھم نہیں بن سکتا کیونکہ یہ ٹیورنگ کے ہالٹنگ مسئلے کی شاخ ہے۔"
    ),
    (
        "Why is Emil Post's Correspondence Problem (matching top and bottom word strings on domino tiles) proved to be undecidable?",
        ["Finding an arbitrary finite sequence of dominoes that matches the top and bottom words can simulate the execution trace of an arbitrary Turing machine", "Dominoes dissolve in computer memory", "Word tiles have different colors", "Alphabets lack sufficient vowels"],
        "Finding an arbitrary finite sequence of dominoes that matches the top and bottom words can simulate the execution trace of an arbitrary Turing machine",
        "PCP asks whether a sequence of pairs (u_i, v_i) exists such that u_i1...u_ik = v_i1...v_ik. Post reduced the halting problem to PCP: matching domino strings simulates a Turing tape configuration step-by-step.",
        "پوسٹ کا خط و کتابت کا معمہ (Post Correspondence Problem): ڈومینو کارڈز کے اوپر اور نیچے کے حروف کو جوڑ کر ایک جیسا لفظ بنانے کا مسئلہ کمپیوٹر کے لیے حل کرنا ناممکن کیوں ہے؟",
        ["کارڈز کے جوڑوں کو ملا کر ایک جیسا لفظ بنانے کا کھیل دراصل کسی بھی ٹیورنگ مشین کے مکمل حسابی سفر کو نقل کرنے کے برابر بن جاتا ہے", "کارڈز میموری میں گھل جاتے ہیں", "کارڈز کے رنگ مختلف ہوتے ہیں", "حروف میں علت کی کمی ہوتی ہے"],
        "کارڈز کے جوڑوں کو ملا کر ایک جیسا لفظ بنانے کا کھیل دراصل کسی بھی ٹیورنگ مشین کے مکمل حسابی سفر کو نقل کرنے کے برابر بن جاتا ہے",
        "دیکھنے میں یہ بچوں کی پزل گیم لگتی ہے، مگر ریاضی دانوں نے ثابت کیا کہ اگر آپ اس پزل کو حل کرنے کا کوئی مستقل کمپیوٹر پروگرام بنا لیں تو اس سے کائنات کے تمام حل نہ ہونے والے کمپیوٹر مسائل حل ہو جائیں گے۔"
    ),
    (
        "Why did mathematician Paul Erdős say 'Mathematics may not be ready for such problems' when discussing the Collatz Conjecture (the 3n + 1 problem)?",
        ["Despite testing past quintillions of integers with all reaching 1, no one can prove that every number avoids entering an infinite diverging loop or distinct cycle", "Numbers stop dividing after one trillion", "Collatz sequences generate negative zeros", "Computers overflow on odd numbers"],
        "Despite testing past quintillions of integers with all reaching 1, no one can prove that every number avoids entering an infinite diverging loop or distinct cycle",
        "The simple rule (if even divide by 2, if odd multiply by 3 and add 1) exhibits pseudo-random chaotic trajectories. Current analytic number theory lacks tools to bound the ergodic properties of these trajectories.",
        "کولاتز کا معمہ (Collatz Conjecture / 3n + 1): ریاضی کے اس آسان ترین فارمولے کے بارے میں عظیم ریاضی دان ایرڈش نے کیوں کہا تھا کہ 'ریاضی ابھی ایسے مسائل کے لیے تیار نہیں ہے'؟",
        ["کھربوں اعداد پر چیک کرنے کے بعد سب کا جواب آخر میں 1 آنے کے باوجود، کوئی یہ ثابت نہیں کر سکا کہ کیا دنیا کا ہر عدد ہمیشہ 1 پر ہی ختم ہوگا یا کوئی لامتناہی لوپ میں بھاگ جائے گا", "اعداد تقسیم ہونا بند ہو جاتے ہیں", "یہ منفی صفر بناتا ہے", "کمپیوٹر طاق اعداد پر رک جاتا ہے"],
        "کھربوں اعداد پر چیک کرنے کے بعد سب کا جواب آخر میں 1 آنے کے باوجود، کوئی یہ ثابت نہیں کر سکا کہ کیا دنیا کا ہر عدد ہمیشہ 1 پر ہی ختم ہوگا یا کوئی لامتناہی لوپ میں بھاگ جائے گا",
        "قاعدہ محض اتنا ہے: اگر جفت ہو تو آدھا کرو، طاق ہو تو تین سے ضرب دے کر ایک جمع کرو۔ بچہ بھی یہ کر سکتا ہے مگر دنیا بھر کے ریاضی دان مل کر بھی اس کے مکمل اصول کو ثابت نہیں کر سکے۔"
    ),
    (
        "What extraordinary universal physical discovery was made by Mitchell Feigenbaum in 1978 regarding the transition from order into chaos (Feigenbaum Constant delta = 4.6692016...)?",
        ["The geometric rate at which period-doubling bifurcations cascade into chaos is strictly identical across all nonlinear dynamical systems in nature", "All chaotic systems explode after 4.6 seconds", "Turbulent fluids freeze at 4.6 Celsius", "Planetary orbits repeat every 4.6 years"],
        "The geometric rate at which period-doubling bifurcations cascade into chaos is strictly identical across all nonlinear dynamical systems in nature",
        "Feigenbaum proved that the ratio of successive period-doubling intervals (d_n - d_n-1) / (d_n+1 - d_n) approaches delta = 4.6692016... for any one-dimensional map with a quadratic maximum, demonstrating profound universality.",
        "فیگن بام کا مستقل عدد (Feigenbaum Constant): 1978 میں مچل فیگن بام نے نظم و ضبط سے بے ترتیبی اور انتشار (Chaos) میں داخل ہونے کے بارے میں کیا عالمی سچائی دریافت کی؟",
        ["قدرت کے تمام غیر لکیری نظاموں میں لہروں کے دگنا ہونے اور بے قابو انتشار میں داخل ہونے کی حسابی رفتار کا تناسب (4.669...) ہمیشہ بالکل ایک جیسا رہتا ہے", "تمام نظام ساڑھے چار سیکنڈ بعد پھٹ جاتے ہیں", "انتشار ساڑھے چار ڈگری پر جم جاتا ہے", "مدار ہر ساڑھے چار سال بعد دہراتے ہیں"],
        "قدرت کے تمام غیر لکیری نظاموں میں لہروں کے دگنا ہونے اور بے قابو انتشار میں داخل ہونے کی حسابی رفتار کا تناسب (4.669...) ہمیشہ بالکل ایک جیسا رہتا ہے",
        "چاہے وہ دل کی دھڑکن کا بے قابو ہونا ہو، نلکے کے قطروں کا گرنا ہو یا موسم کی خرابی، سب کے انتشار کی دہلیز کا تناسب ٹھیک 4.6692016 نکلتا ہے۔ یہ پائی (Pi) کی طرح فطرت کا ایک اٹل مستقل ہے۔"
    ),
    (
        "Why is the boundary of the Mandelbrot Set—generated by iterating the simple quadratic equation z = z^2 + c—known as the most complex object in mathematics?",
        ["It exhibits infinitely intricate, non-repeating self-similar fractal patterns with a boundary Hausdorff dimension of exactly 2", "It contains pictures of living humans", "It requires infinite RAM to calculate 1 pixel", "The shape changes when printed on paper"],
        "It exhibits infinitely intricate, non-repeating self-similar fractal patterns with a boundary Hausdorff dimension of exactly 2",
        "Iterating z_(n+1) = z_n^2 + c for complex numbers c tests whether the sequence remains bounded. Shishikura proved its boundary has Hausdorff dimension 2, containing endless miniature copies of itself and infinite geometric variety.",
        "مینڈل بروٹ سیٹ کی حدود (The Mandelbrot Set): محض z = z^2 + c مساوات سے بننے والی اس شکل کو ریاضی کی سب سے پیچیدہ ترین کائنات کیوں مانا جاتا ہے؟",
        ["اس کے کناروں کو جتنا بھی زوم کیا جائے، اس کے اندر لامتناہی نئی، غیر تکراری اور کبھی ختم نہ ہونے والی خوبصورت ساختیں ابھرتی رہتی ہیں", "اس میں انسانوں کی تصویریں ہوتی ہیں", "ایک نقطہ نکالنے میں لامحدود میموری لگتی ہے", "کاغذ پر چھاپنے سے شکل بدل جاتی ہے"],
        "اس کے کناروں کو جتنا بھی زوم کیا جائے، اس کے اندر لامتناہی نئی، غیر تکراری اور کبھی ختم نہ ہونے والی خوبصورت ساختیں ابھرتی رہتی ہیں",
        "اگر آپ اسے ایک کھرب گنا بھی زوم کر لیں تو بھی یہ کبھی ختم نہیں ہوگا اور ہر نئے موڑ پر حیرت انگیز نئی جیومیٹری سامنے لاتا رہے گا۔ یہ سادگی سے لامتناہی پیچیدگی جنم لینے کا سب سے بڑا مظہر ہے۔"
    ),
    (
        "Why does the Lorenz Strange Attractor in chaos theory trace out a butterfly-shaped loop that never intersects or repeats its own path?",
        ["The trajectory is confined within a bounded 3D phase space but has a fractional fractal dimension of 2.06, creating infinite length without self-intersection", "Computer graphics run out of ink", "Air friction pushes the lines apart", "The equations contain random noise terms"],
        "The trajectory is confined within a bounded 3D phase space but has a fractional fractal dimension of 2.06, creating infinite length without self-intersection",
        "A deterministic autonomous system cannot intersect its own path in phase space (uniqueness theorem). Because it is bounded yet aperiodic, the attractor folds continuously in a fractional dimension (~2.06).",
        "لورینز اسٹرینج اٹریکٹر (The Lorenz Attractor): تتلی کے پروں جیسی گھومتی ہوئی یہ شکل کبھی بھی اپنے ہی پچھلے راستے کو کیوں نہیں کاٹتی اور نہ کبھی دہراتی ہے؟",
        ["یہ لکیر ایک محدود دائرے میں قید ہونے کے باوجود 2.06 کی فریکٹل جہت رکھتی ہے جس کی بدولت وہ اپنے آپ کو چھوئے بغیر لامتناہی لمبائی تک گھومتی رہتی ہے", "کمپیوٹر کی سیاہی ختم ہو جاتی ہے", "ہوا کی رگڑ لکیروں کو دور رکھتی ہے", "مساوات میں بے بنیاد شور شامل ہوتا ہے"],
        "یہ لکیر ایک محدود دائرے میں قید ہونے کے باوجود 2.06 کی فریکٹل جہت رکھتی ہے جس کی بدولت وہ اپنے آپ کو چھوئے بغیر لامتناہی لمبائی تک گھومتی رہتی ہے",
        "چونکہ مساواتیں قطعی ہیں اس لیے لکیر خود کو کاٹ نہیں سکتی، مگر انتشار کی وجہ سے وہ راستہ دہرا بھی نہیں سکتی۔ نتیجہ یہ کہ وہ دو پروں کے درمیان لامتناہی طور پر نئے نئے چکر کاٹتی رہتی ہے۔"
    ),
    (
        "In statistical thermodynamics, how did J. Willard Gibbs resolve the 'Gibbs Paradox' where mixing two identical containers of identical ideal gas falsely predicted an increase in entropy?",
        ["Identical gas particles are fundamentally indistinguishable, requiring dividing phase space volume by N! in statistical mechanics", "Gas molecules destroy each other upon mixing", "Ideal gases possess zero mass", "Entropy does not apply to air"],
        "Identical gas particles are fundamentally indistinguishable, requiring dividing phase space volume by N! in statistical mechanics",
        "Classically treating particles as distinguishable yields Delta S = 2Nk ln 2 when opening the divider between identical gases. Gibbs introduced the 1/N! correction factor, anticipating quantum indistinguishability.",
        "گبز کا معمہ (Gibbs Paradox): ایک ہی گیس کے دو پیالوں کو آپس میں ملانے پر پرانے حسابی فارمولے کے تحت بے ترتیبی (اینٹروپی) میں غیر حقیقی اضافہ کیوں ظاہر ہو رہا تھا؟",
        ["کیونکہ ایک ہی قسم کی گیس کے تمام ایٹم ایک دوسرے کے بالکل ہو بہو اور ناقابل تمیز ہوتے ہیں جس کی وجہ سے حساب کو N! سے تقسیم کرنا لازمی ہوتا ہے", "ملنے پر گیس کے مالیکیول فنا ہو جاتے ہیں", "آئیڈیل گیس کا کوئی وزن نہیں ہوتا", "اینٹروپی ہوا پر لاگو نہیں ہوتی"],
        "کیونکہ ایک ہی قسم کی گیس کے تمام ایٹم ایک دوسرے کے بالکل ہو بہو اور ناقابل تمیز ہوتے ہیں جس کی وجہ سے حساب کو N! سے تقسیم کرنا لازمی ہوتا ہے",
        "اگر دو الگ گیسیں ملیں تو اینٹروپی بڑھتی ہے کیونکہ نئی ملاوٹ ہوئی۔ مگر ایک ہی گیس کے ملنے پر کچھ نیا نہیں بدلا۔ کوانٹم فزکس نے ثابت کیا کہ ایک ہی گیس کے ایٹموں پر کوئی نام یا لیبل نہیں ہوتا۔"
    ),
    (
        "Why did Josef Loschmidt argue that the Second Law of Thermodynamics contradicts classical mechanics (Loschmidt's Paradox / Reversibility Paradox)?",
        ["Newton's laws of motion are completely time-symmetric and reversible, so every micro-trajectory increasing entropy has an equally valid time-reversed trajectory decreasing entropy", "Friction only works backwards", "Gravity repels particles in mirrors", "Thermodynamics was invented by economists"],
        "Newton's laws of motion are completely time-symmetric and reversible, so every micro-trajectory increasing entropy has an equally valid time-reversed trajectory decreasing entropy",
        "If you reverse all molecular velocities (v -> -v), Newton's equations evolve backwards, meaning gas should spontaneously un-mix. Boltzmann responded that while reversible states exist, their phase space volume is astronomically tiny.",
        "لاسچمڈ کا الٹاؤ کا معمہ (Loschmidt's Reversibility Paradox): نیوٹن کے قوانین اگر وقت میں آگے اور پیچھے دونوں طرف یکساں کام کرتے ہیں تو دنیا میں اینٹروپی صرف ایک ہی رخ پر کیوں بڑھتی ہے؟",
        ["نیوٹن کے قوانین مکمل الٹنے کے قابل ہیں، لہٰذا اگر تمام ایٹموں کی رفتار الٹی کر دی جائے تو بکھری ہوئی گیس کو سکیڑنے والے راستے بھی اتنے ہی جائز ہونے چاہئیں", "رگڑ صرف الٹے رخ کام کرتی ہے", "کشش ثقل آئینے میں چیزیں اچھالتی ہے", "تھرمو ڈائنامکس ماہرین معاشیات نے بنائی تھی"],
        "نیوٹن کے قوانین مکمل الٹنے کے قابل ہیں، لہٰذا اگر تمام ایٹموں کی رفتار الٹی کر دی جائے تو بکھری ہوئی گیس کو سکیڑنے والے راستے بھی اتنے ہی جائز ہونے چاہئیں",
        "اگر آپ زمین پر گری پلیٹ کے ہر ایٹم کی ولاسٹی الٹی کر دیں تو پلیٹ اچھل کر دوبارہ جڑ جانی چاہیے۔ بولٹزمین نے جواب دیا کہ الٹا ہونا ناممکن نہیں مگر اس کا امکان اتنا کم ہے کہ کائنات میں کبھی نہیں ہوگا۔"
    ),
    (
        "Why is David Albert's 'Past Hypothesis' necessary to explain why we remember the past but cannot remember the future?",
        ["The universe began in a state of extraordinarily low gravitational and thermodynamic entropy at the Big Bang, defining the thermodynamic arrow of time", "Human memory only works in forward gear", "Future light has not reached our eyes", "The past is physically heavier than the future"],
        "The universe began in a state of extraordinarily low gravitational and thermodynamic entropy at the Big Bang, defining the thermodynamic arrow of time",
        "Microphysics is time-symmetric. The reason entropy increases toward the future is solely that the initial boundary condition of the cosmos (the Big Bang) was characterized by extraordinarily low entropy.",
        "ماضی کا مفروضہ (The Past Hypothesis): ہمیں ماضی یاد رہتا ہے مگر مستقبل یاد کیوں نہیں رہتا؟ فزکس اس کا کیا بنیادی سبب بتاتی ہے؟",
        ["بگ بینگ کے آغاز پر کائنات کی کشش ثقل اور اینٹروپی غیر معمولی طور پر انتہائی کم حالت میں تھی جس نے وقت کے بہاؤ کا ایک مستقل رخ طے کر دیا", "انسانی یادداشت صرف فارورڈ گیئر میں چلتی ہے", "مستقبل کی روشنی آنکھوں تک نہیں پہنچی", "ماضی جسمانی طور پر مستقبل سے وزنی ہوتا ہے"],
        "بگ بینگ کے آغاز پر کائنات کی کشش ثقل اور اینٹروپی غیر معمولی طور پر انتہائی کم حالت میں تھی جس نے وقت کے بہاؤ کا ایک مستقل رخ طے کر دیا",
        "فزکس کے بنیادی قوانین میں آگے اور پیچھے کا کوئی فرق نہیں۔ وقت کا تیر صرف اس لیے آگے بہتا ہے کیونکہ کائنات کی شروعات انتہائی منظم حالت سے ہوئی تھی جو اب بے ترتیبی کی طرف پھیل رہی ہے۔"
    ),
    (
        "According to Peter Ward and Donald Brownlee's 'Rare Earth Hypothesis', why might complex multicellular animal life be extraordinarily rare in the Milky Way galaxy?",
        ["While simple microbial life may be common, complex life requires a delicate chain of astrophysical and geological coincidences (plate tectonics, large Moon, Jupiter shield)", "Our galaxy is too hot for DNA", "Alien civilizations colonized all planets", "Stars emit toxic antimatter"],
        "While simple microbial life may be common, complex life requires a delicate chain of astrophysical and geological coincidences (plate tectonics, large Moon, Jupiter shield)",
        "The hypothesis argues that intelligent life requires a narrow Galactic Habitable Zone, a stabilizing Moon for axial tilt, plate tectonics for carbon cycling, and a gas giant like Jupiter to deflect comet impacts.",
        "نایاب زمین کا نظریہ (Rare Earth Hypothesis): سائنسدانوں کے ایک گروہ کے مطابق کہکشاں میں بیکٹیریا تو عام ہو سکتے ہیں مگر انسان اور جانوروں جیسی پیچیدہ زندگی انتہائی نایاب کیوں ہو سکتی ہے؟",
        ["پیچیدہ زندگی کی بقا کے لیے غیر معمولی کائناتی اتفاقات کا ایک طویل سلسلہ درکار ہے (جیسے بڑا چاند، زمین کے اندرونی پلیٹوں کی حرکت اور مشتری کا حفاظتی ڈھال بننا)", "کہکشاں ڈی این اے کے لیے بہت گرم ہے", "خلائی مخلوق تمام سیاروں پر قابض ہے", "ستارے اینٹی میٹر خارج کرتے ہیں"],
        "پیچیدہ زندگی کی بقا کے لیے غیر معمولی کائناتی اتفاقات کا ایک طویل سلسلہ درکار ہے (جیسے بڑا چاند، زمین کے اندرونی پلیٹوں کی حرکت اور مشتری کا حفاظتی ڈھال بننا)",
        "بیکٹیریا تو سخت ماحول میں جی لیتے ہیں، مگر جانور بننے کے لیے اربوں سال کا مسلسل پرامن ماحول، مستحکم موسم، اور تابکاری سے بچاؤ درکار ہوتا ہے جو کائنات میں شاذ و نادر ہی میسر آتا ہے۔"
    ),
    (
        "In proposed solutions to the Fermi Paradox, what is John Ball's 'Zoo Hypothesis'?",
        ["Advanced extraterrestrial civilizations deliberately avoid contacting Earth to allow human civilization to evolve naturally without contamination", "Aliens keep humans in physical cages on the Moon", "Earth is an exhibit in an intergalactic circus", "Aliens communicate only with zoo animals"],
        "Advanced extraterrestrial civilizations deliberately avoid contacting Earth to allow human civilization to evolve naturally without contamination",
        "Similar to the 'Prime Directive' in Star Trek, the Zoo Hypothesis posits that extraterrestrial civilizations are aware of Earth but intentionally avoid contact, treating us like a protected biological wilderness reserve.",
        "چڑیا گھر کا نظریہ (The Zoo Hypothesis): فرمی پیراڈاکس کا یہ مشہور مفروضہ خلائی مخلوق کی پراسرار خاموشی کی کیا وجہ بتاتا ہے؟",
        ["ترقی یافتہ کہکشانی تہذیبیں جان بوجھ کر زمین سے رابطہ نہیں کر رہیں تاکہ انسانی معاشرہ قدرتی طور پر اور بغیر کسی مداخلت کے پروان چڑھ سکے", "وہ انسانوں کو چاند کے پنجروں میں رکھتے ہیں", "زمین خلائی سرکس کی نمائش گاہ ہے", "وہ صرف جانوروں سے بات کرتے ہیں"],
        "ترقی یافتہ کہکشانی تہذیبیں جان بوجھ کر زمین سے رابطہ نہیں کر رہیں تاکہ انسانی معاشرہ قدرتی طور پر اور بغیر کسی مداخلت کے پروان چڑھ سکے",
        "جیسے انسان جنگلی حیات کے تحفظ کے لیے نیشنل پارک بناتا ہے اور جانوروں کی زندگی میں دخل نہیں دیتا، ہو سکتا ہے کہ سپر انٹیلی جنٹ تہذیبیں زمین کو دور سے ایک ریسرچ پارک کی طرح دیکھ رہی ہوں۔"
    ),
    (
        "What is the 'Planetarium Hypothesis' proposed by science fiction author Stephen Baxter regarding our view of the night sky?",
        ["The universe appears empty because an advanced civilization is projecting a giant virtual simulation to make our cosmos look barren and uninhabited", "Planetariums project fake stars on Earth domes", "The Moon is made of hollow fiberglass", "Telescopes contain pre-recorded video tapes"],
        "The universe appears empty because an advanced civilization is projecting a giant virtual simulation to make our cosmos look barren and uninhabited",
        "Baxter suggested that the apparent silence of the cosmos is an illusion: an Type III civilization has constructed a simulation cloak (a virtual planetarium) around our solar system to isolate our perception.",
        "سیارہ گاہ کا نظریہ (The Planetarium Hypothesis): سٹیفن بیکسٹر کا یہ عجیب و غریب سائنسی مفروضہ آسمان کے خالی نظر آنے کی کیا تشریح کرتا ہے؟",
        ["ہمارے نظام شمسی کے گرد ایک جدید ترین کہکشانی تہذیب نے ورچوئل پروجیکشن کا ایسا پردہ ڈال رکھا ہے جو ہمیں کائنات کو مکمل سنسان اور ویران دکھا رہا ہے", "زمین کے گنبد پر نقلی ستارے دکھائے جاتے ہیں", "چاند فائبر گلاس کا بنا ہے", "دوربینوں میں پرانی ویڈیو کیسٹیں ہوتی ہیں"],
        "ہمارے نظام شمسی کے گرد ایک جدید ترین کہکشانی تہذیب نے ورچوئل پروجیکشن کا ایسا پردہ ڈال رکھا ہے جو ہمیں کائنات کو مکمل سنسان اور ویران دکھا رہا ہے",
        "ہو سکتا ہے کہ حقیقت میں پوری کہکشاں آباد ہو، مگر ہمارے سینسرز اور ریڈیو ٹیلی سکوپس کو جو خلا نظر آ رہی ہے وہ ایک دانستہ تیار کردہ ہولوگرافک اسکرین ہو تاکہ انسان خود کو تنہا سمجھے۔"
    ),
    (
        "On the Nikolai Kardashev scale of cosmic civilizations, what distinguishes a Type II civilization from a Type I civilization?",
        ["A Type II civilization harnesses the entire energy output of its host star (10^26 Watts), while Type I harnesses only its home planet's energy", "Type II civilizations live underground", "Type II civilizations have two suns", "Type II civilizations use coal instead of oil"],
        "A Type II civilization harnesses the entire energy output of its host star (10^26 Watts), while Type I harnesses only its home planet's energy",
        "Kardashev classified civilizations by power consumption: Type I uses all planetary energy (~10^16 W), Type II captures its star's total luminosity (~10^26 W via Dyson spheres), and Type III captures an entire galaxy (~10^37 W).",
        "کارداشیف اسکیل (The Kardashev Scale of Civilizations): کارداشیف کے پیمانے پر ٹائپ 2 کی کائناتی تہذیب ٹائپ 1 سے کس طرح برتر ہوتی ہے؟",
        ["ٹائپ 2 تہذیب اپنے پورے سورج کی تمام تر توانائی (10 کی پاور 26 واٹ) پر مکمل تصرف حاصل کر چکی ہوتی ہے جبکہ ٹائپ 1 صرف اپنے سیارے کی توانائی استعمال کرتی ہے", "ٹائپ 2 تہذیب زمین کے اندر رہتی ہے", "ٹائپ 2 کے پاس دو سورج ہوتے ہیں", "وہ کوئلے کا استعمال کرتے ہیں"],
        "ٹائپ 2 تہذیب اپنے پورے سورج کی تمام تر توانائی (10 کی پاور 26 واٹ) پر مکمل تصرف حاصل کر چکی ہوتی ہے جبکہ ٹائپ 1 صرف اپنے سیارے کی توانائی استعمال کرتی ہے",
        "انسان ابھی ٹائپ 1 پر بھی نہیں پہنچا (ہم 0.73 پر ہیں)۔ ٹائپ 2 تہذیب اپنے ستارے کے گرد ڈائیسن اسفیئر بنا کر ستارے کی ایک ایک کرن کو اپنی مشینوں اور کمپیوٹرز کو چلانے کے لیے نچوڑ لیتی ہے۔"
    ),
    (
        "Why did physicist Gerard O'Neill propose pairing two massive counter-rotating cylindrical habitats together in his space colony design (O'Neill Cylinders)?",
        ["Counter-rotation cancels net angular momentum, preventing the space habitat from precessing wildly and allowing it to remain permanently aimed at the Sun", "One cylinder holds water while the other holds air", "The cylinders bump together to generate heat", "Counter-rotation doubles the speed of light"],
        "Counter-rotation cancels net angular momentum, preventing the space habitat from precessing wildly and allowing it to remain permanently aimed at the Sun",
        "A single spinning cylinder acts as a giant gyroscope; orbital motion would cause gyroscopic precession, losing solar alignment. Counter-rotating identical cylinders yields zero net angular momentum vector.",
        "او نیل سلنڈرز اور مصنوعی کشش ثقل (O'Neill Cylinders): خلا میں انسانی بستیوں کے لیے دو دیوہیکل سلنڈروں کو ہمیشہ ایک دوسرے کے الٹے رخ پر گھمانے کا مشورہ کیوں دیا جاتا ہے؟",
        ["الٹے رخ پر گھومنے سے ان کا کونیائی مومنٹم صفر ہو جاتا ہے، جس سے بستی فضا میں جھولنے سے محفوظ رہ کر مستقل طور پر سورج کے رخ پر جمی رہتی ہے", "ایک سلنڈر میں پانی اور دوسرے میں ہوا رکھی جاتی ہے", "وہ ٹکرا کر حرارت پیدا کرتے ہیں", "الٹا گھومنے سے روشنی کی رفتار بڑھتی ہے"],
        "الٹے رخ پر گھومنے سے ان کا کونیائی مومنٹم صفر ہو جاتا ہے، جس سے بستی فضا میں جھولنے سے محفوظ رہ کر مستقل طور پر سورج کے رخ پر جمی رہتی ہے",
        "اگر صرف ایک سلنڈر گھومے گا تو وہ جائرواسکوپ بن کر مدار میں بری طرح مڑنے لگے گا اور دھوپ کی کھڑکیاں سورج سے ہٹ جائیں گی۔ دوسرا الٹا سلنڈر اس موڑ کو بالکل متوازن کر دیتا ہے۔"
    ),
    (
        "Why is Larry Niven's famous science-fiction megastructure 'Ringworld' dynamically unstable around its central star?",
        ["The ring experiences zero net restoring gravitational force from the central star; any slight drift causes it to collide with the star unless actively stabilized", "The ring spins too fast and flings its air away", "Solar flares melt the ring floor", "Planetary gravity collapses the walls"],
        "The ring experiences zero net restoring gravitational force from the central star; any slight drift causes it to collide with the star unless actively stabilized",
        "James Clerk Maxwell proved that a rigid concentric ring around a mass is in neutral/unstable equilibrium. If offset by distance delta, gravitational forces on the closer side are stronger, pulling the ring catastrophically into the star.",
        "رنگ ورلڈ کا عدم استحکام (Ringworld Dynamic Instability): ستارے کے گرد بنائی گئی کھربوں کلومیٹر لمبی ٹھوس انگوٹھی والی بستی بغیر راکٹ انجنوں کے اپنے ستارے سے کیوں ٹکرا جائے گی؟",
        ["ستارے کے مرکز سے کھچاؤ کا کوئی خودکار بحالی توازن نہیں ہوتا؛ ذرا سا ہٹنے پر قریب والا رخ ستارے کی طرف کھنچتا چلا جائے گا جب تک کہ انگوٹھی ستارے میں نہ گر جائے", "انگوٹھی تیز گھوم کر ہوا پھینک دیتی ہے", "شعلے فرش پگھلا دیتے ہیں", "دیواریں گر جاتی ہیں"],
        "ستارے کے مرکز سے کھچاؤ کا کوئی خودکار بحالی توازن نہیں ہوتا؛ ذرا سا ہٹنے پر قریب والا رخ ستارے کی طرف کھنچتا چلا جائے گا جب تک کہ انگوٹھی ستارے میں نہ گر جائے",
        "فزکس دان جیمز کلرک میکس ویل نے زحل کے چھلوں پر ثابت کیا تھا کہ ٹھوس انگوٹھی کبھی مستحکم نہیں رہ سکتی۔ ذرا سا جھٹکا لگنے پر کشش کا توازن بگڑ جاتا ہے اور انگوٹھی ستارے پر گر کر تباہ ہو جائے گی۔"
    ),
    (
        "How can a megastructure called a Shkadov Thruster slowly move an entire star system across interstellar space over millions of years?",
        ["A giant curved static mirror hovers above the star, reflecting half its radiation pressure to produce asymmetric net thrust", "By attaching rocket boosters to the star's equator", "By detonating antimatter bombs inside the core", "By towing the star with magnetic cables"],
        "A giant curved static mirror hovers above the star, reflecting half its radiation pressure to produce asymmetric net thrust",
        "Leonid Shkadov designed a class-A stellar engine: a colossal statite mirror balances radiation pressure against gravitational attraction. Reflected starlight creates net photon thrust, steering the Sun at ~100 km/s over 10^8 years.",
        "شکادوف تھرسٹر اور ستارے کا سفر (Shkadov Thruster Stellar Engine): ایک دیوہیکل آئینے کی مدد سے پورے سورج اور اس کے تمام سیاروں کو کہکشاں میں دوسری جگہ کیسے منتقل کیا جا سکتا ہے؟",
        ["ستارے کے ایک رخ پر دیوہیکل خمیدہ آئینہ فضا میں معلق کر کے، جس سے ستارے کی ادھی روشنی پلٹ کر اسے ایک بہت بڑے فوٹون راکٹ کی طرح دھکیلنے لگتی ہے", "ستارے کے گرد راکٹ باندھ کر", "مرکز میں ایٹم بم پھوڑ کر", "مقناطیسی تاروں سے کھینچ کر"],
        "ستارے کے ایک رخ پر دیوہیکل خمیدہ آئینہ فضا میں معلق کر کے، جس سے ستارے کی ادھی روشنی پلٹ کر اسے ایک بہت بڑے فوٹون راکٹ کی طرح دھکیلنے لگتی ہے",
        "روشنی کا دباؤ بھی وزن رکھتا ہے۔ جب سورج کی ایک طرف کی روشنی آئینے سے ٹکرا کر پلٹتی ہے تو سورج پر ایک دھیما مگر مسلسل دھکا لگتا ہے جو لاکھوں سالوں میں پورے نظام شمسی کو کہکشاں میں ہانک کر لے جاتا ہے۔"
    ),
    (
        "Why does Nick Bostrom's Simulation Argument conclude that you are almost certainly living in an ancestor computer simulation?",
        ["If advanced civilizations run vast numbers of ancestor simulations, simulated conscious minds will vastly outnumber biological original minds", "Human brains run on 5-volt electrical signals", "Computer monitors refresh at 60 Hertz", "Memory loss proves hard drive glitches"],
        "If advanced civilizations run vast numbers of ancestor simulations, simulated conscious minds will vastly outnumber biological original minds",
        "Bostrom presented a trilemma: either (1) civilizations go extinct before posthumanity, (2) posthuman civilizations lose interest in simulations, or (3) we almost certainly live in a simulation because simulated beings outnumber real ones billions to one.",
        "سمولیشن کا فکری استدلال (Bostrom's Simulation Argument): نک بوسٹروم کا فلسفہ یہ کیوں کہتا ہے کہ ہمارے ایک کمپیوٹر سمولیشن میں جینے کا امکان 99 فیصد سے زیادہ ہے؟",
        ["اگر ترقی یافتہ انسانیت کمپیوٹرز پر اربوں نقلی تاریخیں چلاتی ہے، تو نقلی انسانوں کی تعداد اصل مادی انسانوں کے مقابلے میں اربوں گنا زیادہ ہو جائے گی", "انسانی دماغ 5 وولٹ پر چلتا ہے", "اسکرین 60 ہرٹز پر چلتی ہے", "بھولنا ہارڈ ڈرائیو کی خرابی ہے"],
        "اگر ترقی یافتہ انسانیت کمپیوٹرز پر اربوں نقلی تاریخیں چلاتی ہے، تو نقلی انسانوں کی تعداد اصل مادی انسانوں کے مقابلے میں اربوں گنا زیادہ ہو جائے گی",
        "اگر کمپیوٹر پر ذہین مخلوق کو سمیولیٹ کرنا ممکن ہو تو اربوں ورچوئل جہان بنائے جائیں گے اور اصلی جہان صرف 1 ہوگا۔ چنانچہ کسی بھی ہوش مند وجود کے ورچوئل دنیا میں پیدا ہونے کا امکان کھرب گنا زیادہ بنتا ہے۔"
    ),
    (
        "In the Quantum Suicide / Quantum Immortality thought experiment, why does an experimenter subjected to an automated quantum weapon believe they are immortal?",
        ["According to Many-Worlds, the experimenter's conscious perspective can only survive in parallel quantum branches where the weapon continuously fails to fire", "The weapon shoots quantum blanks", "Quantum decoherence absorbs bullets", "The human skull deflects gamma rays"],
        "According to Many-Worlds, the experimenter's conscious perspective can only survive in parallel quantum branches where the weapon continuously fails to fire",
        "Max Tegmark formulated the thought experiment: in Everett's interpretation, the universe branches on each trigger pull. Dead observers experience nothing; subjective consciousness only tracks branches with 100% survival history.",
        "کوانٹم خودکشی اور لافانیت (Quantum Immortality Thought Experiment): ایورٹ کی متوازی دنیاؤں کی تھیوری کے تحت خود پر کوانٹم بندوق چلانے والے کو کیوں لگے گا کہ وہ کبھی نہیں مر سکتا؟",
        ["کیونکہ اس کا ذاتی شعور صرف اور صرف انہی شاخوں اور جہانوں میں زندہ رہ کر سوچ سکتا ہے جہاں بندوق کا کوانٹم ٹریگر کسی خرابی کے باعث نہیں چلا", "بندوق خالی گولیاں چلاتی ہے", "کوانٹم فزکس گولی نگل جاتی ہے", "کھوپڑی شعاعیں موڑ دیتی ہے"],
        "کیونکہ اس کا ذاتی شعور صرف اور صرف انہی شاخوں اور جہانوں میں زندہ رہ کر سوچ سکتا ہے جہاں بندوق کا کوانٹم ٹریگر کسی خرابی کے باعث نہیں چلا",
        "باہر کھڑے شخص کے لیے وہ 50 فیصد باریوں میں مر جائے گا۔ مگر اس کے اپنے شعور کے لیے مردہ حالت کا کوئی تجربہ نہیں ہوتا، اس لیے وہ خود کو ہمیشہ اسی متوازی کائنات میں پائے گا جہاں بندوق مس فائر ہو گئی۔"
    ),
    (
        "In time travel physics, how does the Novikov Self-Consistency Principle resolve the Grandfather Paradox without spawning parallel timelines?",
        ["Only self-consistent histories with zero logical contradictions can physically occur on closed timelike curves (probability of contradiction is strictly zero)", "Time machines run out of chroniton fuel", "Grandfathers become bulletproof in the past", "Time travelers lose their memories"],
        "Only self-consistent histories with zero logical contradictions can physically occur on closed timelike curves (probability of contradiction is strictly zero)",
        "Igor Novikov proposed that local physical laws apply globally on closed timelike curves. Any action by a time traveler must already be an integrated, non-contradictory part of past history.",
        "نوویکوف کا اصول خود مطابقت (Novikov Self-Consistency Principle): ماضی کے سفر میں دادا کو مارنے کے معمے کو یہ قانون متوازی دنیاؤں کے بغیر کیسے حل کرتا ہے؟",
        ["وقت کے بند دائرے میں صرف وہی واقعات طبعی طور پر رونما ہو سکتے ہیں جن میں کوئی منطقی تضاد نہ ہو؛ تضاد پیدا کرنے والے کسی بھی واقعے کا امکان قطعی صفر ہوتا ہے", "ٹائم مشین کا ایندھن ختم ہو جاتا ہے", "دادا ماضی میں گولی سے محفوظ ہو جاتے ہیں", "مسافر یادداشت کھو بیٹھتا ہے"],
        "وقت کے بند دائرے میں صرف وہی واقعات طبعی طور پر رونما ہو سکتے ہیں جن میں کوئی منطقی تضاد نہ ہو؛ تضاد پیدا کرنے والے کسی بھی واقعے کا امکان قطعی صفر ہوتا ہے",
        "آپ ماضی میں جا سکتے ہیں مگر دادا کو مارنے کی ہر کوشش ناکام ہوگی (بندوق جام ہوگی، پاؤں پھسلے گا یا آپ غلط بندے کو ماریں گے) کیونکہ تاریخ پہلے ہی آپ کے اس سفر کو اپنے اندر ریکارڈ کر چکی ہے۔"
    ),
    (
        "What is the Bootstrap Paradox (Ontological Paradox) in general relativistic time travel?",
        ["An object, document, or piece of information exists in a closed causal time loop without ever having been created or originated by anyone", "A person pulls themselves up by shoelaces", "Time machines create heavy gravitational boots", "Information decays at absolute zero"],
        "An object, document, or piece of information exists in a closed causal time loop without ever having been created or originated by anyone",
        "If a traveler copies Beethoven's symphonies, travels to 1790, and gives them to a young Beethoven to publish, the music exists in a closed causal loop with no original author, violating classical causality.",
        "بوٹ اسٹریپ پیراڈاکس (The Bootstrap Paradox): وقت کے چکر میں معلومات یا کسی چیز کے وجود میں آنے کا یہ عجیب معمہ کیا ہے؟",
        ["کوئی کتاب، معلومات یا چیز وقت کے ایک بند چکر میں گھومتی رہتی ہے مگر کائنات میں اسے حقیقت میں کبھی کسی نے تخلیق ہی نہیں کیا ہوتا", "انسان جوتوں کے تسموں سے خود کو اٹھاتا ہے", "ٹائم مشین وزنی جوتے بناتی ہے", "معلومات سردی میں فنا ہو جاتی ہے"],
        "کوئی کتاب، معلومات یا چیز وقت کے ایک بند چکر میں گھومتی رہتی ہے مگر کائنات میں اسے حقیقت میں کبھی کسی نے تخلیق ہی نہیں کیا ہوتا",
        "جیسے ایک شخص شیکسپیئر کا ڈرامہ لے کر ماضی میں جا کر شیکسپیئر کو دے دے، اور شیکسپیئر اسے اپنے نام سے چھاپ دے۔ اب سوال یہ ہے کہ وہ ڈرامہ اصل میں لکھا کس نے تھا؟ اس کا کوئی خالق وجود ہی نہیں رکھتا۔"
    ),
    (
        "What bizarre solution to Einstein's Field Equations did logician Kurt Gödel discover in 1949 that shocked Einstein on his 70th birthday?",
        ["A rotating universe where matter curves spacetime into closed timelike curves, mathematically permitting time travel into any moment of the past", "A universe where time runs completely backwards", "A cosmos composed entirely of dark antimatter", "A universe where speed of light is zero"],
        "A rotating universe where matter curves spacetime into closed timelike curves, mathematically permitting time travel into any moment of the past",
        "Gödel's metric is an exact cosmological solution with non-zero cosmological constant and homogeneous rotating matter. It contains closed timelike curves through every point, demonstrating time is not linear.",
        "گوئڈل کا گھومتی کائنات کا ماڈل (The Gödel Metric): 1949 میں ریاضی دان کرٹ گوئڈل نے آئن سٹائن کی مساوات کا کون سا ایسا حل نکال کر آئن سٹائن کو ہلا دیا تھا؟",
        ["ایک مسلسل گھومتی ہوئی کائنات کا ماڈل جس کے اندر زمان و مکان اس طرح مڑ جاتے ہیں کہ خلا میں آگے سفر کر کے ماضی کے کسی بھی لمحے میں واپس پہنچا جا سکتا ہے", "ایک ایسی کائنات جہاں وقت الٹا بہتا ہے", "خالص اینٹی میٹر سے بنی کائنات", "جہاں روشنی کی رفتار صفر ہو"],
        "ایک مسلسل گھومتی ہوئی کائنات کا ماڈل جس کے اندر زمان و مکان اس طرح مڑ جاتے ہیں کہ خلا میں آگے سفر کر کے ماضی کے کسی بھی لمحے میں واپس پہنچا جا سکتا ہے",
        "آئن سٹائن کا خیال تھا کہ ان کی تھیوری میں وقت کا سفر ناممکن ہوگا۔ مگر گوئڈل نے ثابت کیا کہ اگر کائنات اپنے محور پر گھوم رہی ہو تو زمان و مکان کا تانا بانا بند دائرے بنا دیتا ہے جس سے ماضی کا سفر ریاضیاتی طور پر ممکن ہو جاتا ہے۔"
    ),
    (
        "Why is an infinitely long, rapidly rotating cylinder of ultra-dense neutron matter capable of enabling backwards time travel in General Relativity (a Tipler Cylinder)?",
        ["Extreme frame-dragging twists spacetime so severely that light cones tilt beyond the horizontal, converting spatial paths into closed timelike curves", "The cylinder radiates tachyons", "Centrifugal force destroys the speed of light", "The cylinder melts atomic nuclei into pure chronitons"],
        "Extreme frame-dragging twists spacetime so severely that light cones tilt beyond the horizontal, converting spatial paths into closed timelike curves",
        "Frank Tipler showed that near an infinite cylinder rotating at half light speed, dragging of inertial frames tilts light cones into the toroidal direction, allowing a sub-light rocket orbiting the cylinder to return before it left.",
        "ٹپلر سلنڈر (The Tipler Cylinder Time Machine): اضافیت کے مطابق انتہائی وزنی اور تیزی سے گھومتا ہوا لمبا سلنڈر ماضی کے سفر کا راستہ کیسے کھول دیتا ہے؟",
        ["اس کا بھیانک فریم ڈریگنگ خلا کو اتنا شدید موڑ دیتا ہے کہ روشنی کے کونز الٹ جاتے ہیں اور عام راستے وقت کے بند دائروں میں بدل جاتے ہیں", "سلنڈر ٹیکیونز خارج کرتا ہے", "مرکز گریز قوت روشنی کی رفتار مٹا دیتی ہے", "سلنڈر ایٹموں کو ٹائم پارٹیکلز بنا دیتا ہے"],
        "اس کا بھیانک فریم ڈریگنگ خلا کو اتنا شدید موڑ دیتا ہے کہ روشنی کے کونز الٹ جاتے ہیں اور عام راستے وقت کے بند دائروں میں بدل جاتے ہیں",
        "جب سلنڈر روشنی کی آدھی رفتار سے گھومتا ہے تو اس کے گرد خلا شہد کے بھنور کی طرح لپٹ جاتی ہے۔ جہاز اس کے گرد چکر کاٹ کر روشنی سے کم رفتار میں رہ کر بھی اپنے روانہ ہونے سے پہلے کے وقت میں لوٹ سکتا ہے۔"
    ),
    (
        "Why does keeping the throat of a traversable wormhole (an Einstein-Rosen bridge) physically open require exotic matter with negative mass or negative energy density?",
        ["Normal gravity pulls the throat shut at light speed, so negative energy is required to exert gravitational repulsion and hold it open", "Positive matter dissolves inside wormholes", "Electrons neutralize wormhole portals", "Wormholes require sub-zero ice"],
        "Normal gravity pulls the throat shut at light speed, so negative energy is required to exert gravitational repulsion and hold it open",
        "Morris and Thorne demonstrated that traversable wormholes violate the Null Energy Condition (NEC: T_munu k^mu k^nu >= 0). Only negative energy densities (like Casimir vacuum states) produce the repulsive defocusing needed to prevent collapse.",
        "وارم ہول اور منفی توانائی (Wormholes & Exotic Negative Energy): خلا کے دو دور دراز مقامات کو جوڑنے والی سرنگ (Wormhole) کو کھلا رکھنے کے لیے منفی مادے کی ضرورت کیوں ہوتی ہے؟",
        ["عام کشش ثقل سرنگ کے گلے کو فوری بھینچ کر بند کر دیتی ہے، اس لیے سرنگ کو کھلا رکھنے کے لیے منفی توانائی کی دھکیلنے والی کشش درکار ہوتی ہے", "عام مادہ سرنگ کے اندر پگھل جاتا ہے", "الیکٹران دروازے کو نیوٹرل کر دیتے ہیں", "سرنگوں کو منفی درجہ حرارت کی برف چاہیے"],
        "عام کشش ثقل سرنگ کے گلے کو فوری بھینچ کر بند کر دیتی ہے، اس لیے سرنگ کو کھلا رکھنے کے لیے منفی توانائی کی دھکیلنے والی کشش درکار ہوتی ہے",
        "کشش ثقل کی فطرت چیزوں کو سکیڑنا ہے۔ جیسے ہی وارم ہول بنتا ہے، کشش ثقل پلک جھپکنے میں اس کے درمیان کے راستے کو دبا کر توڑ دیتی ہے۔ صرف کشش ثقل کو پیچھے دھکیلنے والی منفی انرجی ہی اس کے منہ کو کھلا رکھ سکتی ہے۔"
    ),
    (
        "What theoretical cosmic entity is mathematically predicted by General Relativity as the exact time-reversed mirror image of a Black Hole (a White Hole)?",
        ["An event horizon from which matter and light can only erupt outward, but into which nothing can ever enter from the outside", "A star made of pure frozen white ice", "A hole that absorbs all visible radiation", "A supernova that implodes into a neutron star"],
        "An event horizon from which matter and light can only erupt outward, but into which nothing can ever enter from the outside",
        "White holes are maximal analytic extensions of the Schwarzschild metric. While black holes are regions where nothing can escape, white holes possess past event horizons from which matter continuously emerges and external entry is impossible.",
        "وائٹ ہول کا تصور (White Holes in General Relativity): جنرل ریلیٹیویٹی کے حسابی فارمولوں کے مطابق وائٹ ہول، بلیک ہول کا بالکل الٹ عکس کیسے ہوتا ہے؟",
        ["ایک ایسا کائناتی افق جس کے اندر سے مادہ اور روشنی صرف باہر کی طرف ابل سکتے ہیں، مگر باہر سے کوئی بھی چیز کبھی اس کے اندر داخل نہیں ہو سکتی", "خالص سفید برف کا ستارہ", "ایک سوراخ جو تمام روشنی پی جائے", "سپر نووا جو سکڑ کر نیوٹران ستارہ بن جائے"],
        "ایک ایسا کائناتی افق جس کے اندر سے مادہ اور روشنی صرف باہر کی طرف ابل سکتے ہیں، مگر باہر سے کوئی بھی چیز کبھی اس کے اندر داخل نہیں ہو سکتی",
        "بلیک ہول میں چیزیں صرف اندر گر سکتی ہیں اور باہر کچھ نہیں آ سکتا۔ وقت کو الٹا چلائیں تو وائٹ ہول بنتا ہے جہاں سے مادہ چشمے کی طرح پھوٹتا ہے مگر اس کی باؤنڈری کے اندر جانا طبعی طور پر ناممکن ہوتا ہے۔"
    ),
    (
        "What violent topological transformation of spacetime was predicted by John Archibald Wheeler to occur at the subatomic Planck scale (Quantum Foam)?",
        ["Spacetime ceases to be smooth and continuous, boiling into a turbulent froth of quantum foam with micro-wormholes and topological bubbles", "Empty space freezes into solid crystal glass", "Vacuum converts into liquid petroleum", "Photons split into solid iron balls"],
        "Spacetime ceases to be smooth and continuous, boiling into a turbulent froth of quantum foam with micro-wormholes and topological bubbles",
        "At scales near the Planck length (1.6 x 10^-35 m) and Planck time (5.4 x 10^-44 s), Heisenberg uncertainty creates energy fluctuations Delta E ~ hbar / Delta t that distort geometry into chaotic quantum foam.",
        "کوانٹم جھاگ اور زمان و مکان کا ابال (Wheeler's Quantum Foam): پلانک اسکیل (10 کی پاور -35 میٹر) پر پہنچ کر خلا کی خالی جگہ کیسی شکل اختیار کر لیتی ہے؟",
        ["زمان و مکان کی ہموار چادر ختم ہو جاتی ہے اور خلا ابلتے ہوئے جھاگ کی طرح نادیدہ سوراخوں، بلبلوں اور کوانٹم سرنگوں کے طوفان میں بدل جاتی ہے", "خلا جم کر شیشے کا کرسٹل بن جاتی ہے", "خالی جگہ مائع پیٹرول بن جاتی ہے", "روشنی لوہے کی گیندیں بن جاتی ہے"],
        "زمان و مکان کی ہموار چادر ختم ہو جاتی ہے اور خلا ابلتے ہوئے جھاگ کی طرح نادیدہ سوراخوں، بلبلوں اور کوانٹم سرنگوں کے طوفان میں بدل جاتی ہے",
        "دور سے دیکھنے پر سمندر پرسکون لگتا ہے مگر پاس جائیں تو جھاگ اور لہریں ٹکرا رہی ہوتی ہیں۔ بالکل اسی طرح کوانٹم فزکس اور اضافیت کے ملاپ پر خلا کا تانا بانا ابلتے ہوئے کھولتے پانی کے بلبلوں کی طرح بن جاتا ہے۔"
    ),
    (
        "Why is the Planck Length (1.616 x 10^-35 meters) considered the absolute shortest meaningful distance in fundamental physics?",
        ["Probing distances smaller than the Planck length requires so much localized energy that it collapses the region into a micro black hole", "Microscopes cannot focus small light rays", "Rulers break under small atomic forces", "Atoms evaporate at smaller scales"],
        "Probing distances smaller than the Planck length requires so much localized energy that it collapses the region into a micro black hole",
        "To resolve length Delta x, photons require momentum p ~ hbar / Delta x. Squeezing this energy into Delta x creates a Schwarzschild radius r_s = 2GE/c^4 >= Delta x, forming a black hole that swallows the measurement.",
        "پلانک لمبائی کی آخری حد (The Planck Length Limit): فزکس میں پلانک لمبائی (10 کی پاور -35 میٹر) کو کائنات کا سب سے چھوٹا ممکنہ فاصلہ کیوں مانا جاتا ہے جس سے چھوٹا کچھ نہیں ہو سکتا؟",
        ["اس سے چھوٹے فاصلے کو دیکھنے کے لیے اتنی شدید توانائی چاہیے کہ وہ خود اس جگہ کو سکیڑ کر ایک خوردبینی بلیک ہول میں بدل دے گی", "خوردبینیں چھوٹی شعاعوں پر فوکس نہیں کر سکتیں", "چھوٹے فاصلوں پر پیمانے ٹوٹ جاتے ہیں", "اس سے نیچے ایٹم بھاپ بن جاتے ہیں"],
        "اس سے چھوٹے فاصلے کو دیکھنے کے لیے اتنی شدید توانائی چاہیے کہ وہ خود اس جگہ کو سکیڑ کر ایک خوردبینی بلیک ہول میں بدل دے گی",
        "چھوٹی چیز دیکھنے کے لیے زیادہ انرجی کی شعاع مارنی پڑتی ہے۔ اگر آپ پلانک فاصلے سے چھوٹی چیز دیکھنا چاہیں گے تو فوٹون کی انرجی اتنی زیادہ ہوگی کہ وہ اس جگہ پر خود ایک بلیک ہول بنا کر مشاہدے کو ہڑپ کر لے گا۔"
    ),
    (
        "Why does an acoustic shock wave from a supersonic jet's sonic boom spread through the atmosphere as a 3D cone rather than a spherical wave (the Mach Cone)?",
        ["Constructive interference of spherical sound waves emitted at successive points along the flight path forms a conical tangent envelope", "Jet engines burn fuel in triangular patterns", "Air pressure forms triangle crystals", "The jet's nose pushes air magnetically"],
        "Constructive interference of spherical sound waves emitted at successive points along the flight path forms a conical tangent envelope",
        "When aircraft speed v exceeds sound speed c, emitted spherical wavefronts lag behind. The envelope of these spherical waves forms a cone with half-angle sin(mu) = c/v = 1/M, where pressure discontinuities pile up.",
        "ماخ کون اور آواز سے تیز جھٹکا (Mach Cone & Sonic Boom): آواز کی رفتار سے تیز اڑنے والے جیٹ طیارے کی شاک ویو فضا میں گولائی کی بجائے ایک تکونی مخروط (Cone) کی شکل میں کیوں پھیلتی ہے؟",
        ["طیارے کے ہر لمحے چھوڑی جانے والی صوتی لہریں طیارے کے پیچھے ایک دوسرے پر چڑھ کر تکونی چھتری نما دباؤ کی لہر بنا دیتی ہیں", "انجن تکونی شکل میں ایندھن جلاتے ہیں", "ہوا کا دباؤ تکونی قلمیں بناتا ہے", "جہاز ہوا کو مقناطیسی طور پر دھکیلتا ہے"],
        "طیارے کے ہر لمحے چھوڑی جانے والی صوتی لہریں طیارے کے پیچھے ایک دوسرے پر چڑھ کر تکونی چھتری نما دباؤ کی لہر بنا دیتی ہیں",
        "چونکہ جہاز اپنی ہی آواز کی لہروں سے آگے نکل جاتا ہے، اس لیے وہ تمام لہریں جہاز کے تعاقب میں جمع ہو کر ایک دباؤ دار کون بنا دیتی ہیں۔ جب اس کون کا نچلا سرا زمین کو چھوتا ہے تو زوردار دھماکہ سنائی دیتا ہے۔"
    ),
    (
        "Why does a high-speed projectile traveling faster than the speed of light in water emit an eerie blue optical glow (Cherenkov Radiation)?",
        ["The charged particle outpaces the local phase velocity of light in the dielectric medium, creating an optical shock wave analogous to a sonic boom", "Water splits into blue hydrogen isotopes", "Friction with water boils surrounding atoms", "The projectile reflects deep ocean light"],
        "The charged particle outpaces the local phase velocity of light in the dielectric medium, creating an optical shock wave analogous to a sonic boom",
        "While c in vacuum is invariant, light in water travels at c/n ~ 0.75c. Charged particles exceeding c/n polarize water molecules, creating constructive coherent electromagnetic shock waves peaked at blue and UV wavelengths.",
        "چرینکوف تابکاری اور نیلی روشنی (Cherenkov Radiation): ایٹمی ری ایکٹر کے تالاب میں پانی کے اندر ذرات کے دوڑنے پر پرسرار نیلی چمک کیوں نکلتی ہے؟",
        ["جب چارج شدہ ذرہ پانی کے اندر روشنی کی رفتار (c/n) سے بھی تیز دوڑتا ہے تو وہ صوتی دھماکے (Sonic boom) کی طرح روشنی کا ایک دھماکہ خیز شاک ویو مخروط بناتا ہے", "پانی نیلی ہائیڈروجن میں بدل جاتا ہے", "پانی کی رگڑ ایٹموں کو ابالتی ہے", "پانی گہرائی کی روشنی پلٹاتا ہے"],
        "جب چارج شدہ ذرہ پانی کے اندر روشنی کی رفتار (c/n) سے بھی تیز دوڑتا ہے تو وہ صوتی دھماکے (Sonic boom) کی طرح روشنی کا ایک دھماکہ خیز شاک ویو مخروط بناتا ہے",
        "خلا میں روشنی سے تیز کچھ نہیں چل سکتا، مگر پانی میں روشنی کی رفتار 25 فیصد کم ہو جاتی ہے۔ جب تابکار ذرہ پانی میں روشنی سے تیز نکلتا ہے تو وہ روشنی کا آپٹیکل دھماکہ پیدا کرتا ہے جو خوبصورت نیلے رنگ کا چمکتا ہے۔"
    ),
    (
        "Why does high-energy X-ray or gamma radiation passing through dense matter undergo Bremsstrahlung ('Braking Radiation')?",
        ["Fast-moving charged electrons are decelerated by the electric Coulomb field of heavy atomic nuclei, emitting excess kinetic energy as photons", "Electrons collide head-on with neutrons", "Nuclei absorb electrons into nuclear orbits", "Radiation friction creates heat sparks"],
        "Fast-moving charged electrons are decelerated by the electric Coulomb field of heavy atomic nuclei, emitting excess kinetic energy as photons",
        "Larmor's formula dictates that any accelerated or decelerated electric charge radiates power P = (q^2 * a^2) / (6*pi*epsilon_0*c^3). Electrons deflected by nuclear Coulomb fields radiate continuous X-ray Bremsstrahlung.",
        "برمس اسٹراہلونگ یا بریکنگ تابکاری (Bremsstrahlung Radiation): تیز رفتار الیکٹران جب بھاری ایٹموں کے پاس سے گزرتے ہیں تو اچانک طاقتور ایکس رے شعاعیں کیوں خارج کرتے ہیں؟",
        ["ایٹم کے مرکزے کے شدید برقی کھچاؤ کی وجہ سے الیکٹران کی رفتار اچانک دھیمی پڑ جاتی ہے اور اس کی کھوئی ہوئی توانائی ایکس رے فوٹون بن کر نکلتی ہے", "الیکٹران نیوٹران سے ٹکرا جاتے ہیں", "مرکزہ الیکٹران کو نگل لیتا ہے", "تابکاری کی رگڑ چنگاریاں چھوڑتی ہے"],
        "ایٹم کے مرکزے کے شدید برقی کھچاؤ کی وجہ سے الیکٹران کی رفتار اچانک دھیمی پڑ جاتی ہے اور اس کی کھوئی ہوئی توانائی ایکس رے فوٹون بن کر نکلتی ہے",
        "جرمن زبان میں اس کا مطلب 'بریک کی تابکاری' ہے۔ جب الیکٹران گاڑی کی طرح مرکزے کے موڑ پر بریک لگاتا ہے تو اس بریک لگنے کے جھٹکے سے کلاسک فزکس کے قانون کے تحت روشنی اور ایکس رے کی تابکاری خارج ہوتی ہے۔"
    ),
    (
        "Why can a high-energy gamma-ray photon completely vanish and materialize into an electron and a positron pair near an atomic nucleus (Pair Production)?",
        ["Einstein's mass-energy equivalence (E = mc^2) allows photon energy exceeding 1.022 MeV to convert into particle rest mass in a Coulomb field", "Photons split in half mechanically", "Atomic nuclei act as particle factories", "Gamma rays contain trapped electrons"],
        "Einstein's mass-energy equivalence (E = mc^2) allows photon energy exceeding 1.022 MeV to convert into particle rest mass in a Coulomb field",
        "Dirac equation dictates that a photon with energy E >= 2 * m_e * c^2 (1.022 MeV) can transform into an electron and positron. A spectator nucleus absorbs recoil momentum to satisfy conservation laws.",
        "جوڑے کی پیدائش (Pair Production): خالص روشنی کا ایک گاما فوٹون جب ایٹم کے قریب سے گزرتا ہے تو وہ اچانک غائب ہو کر ایک الیکٹران اور ایک پوزیٹران میں کیسے بدل جاتا ہے؟",
        ["آئن سٹائن کی مساوات (E = mc^2) کے تحت جب فوٹون کی توانائی 1.022 میگا الیکٹران وولٹ سے زیادہ ہو تو وہ خالص روشنی سے ٹھوس مادے میں تبدیل ہو جاتی ہے", "فوٹون مکینیکل طور پر دو ٹکڑے ہو جاتا ہے", "مرکزہ ایک فیکٹری کی طرح کام کرتا ہے", "گاما لہروں میں الیکٹران قید ہوتے ہیں"],
        "آئن سٹائن کی مساوات (E = mc^2) کے تحت جب فوٹون کی توانائی 1.022 میگا الیکٹران وولٹ سے زیادہ ہو تو وہ خالص روشنی سے ٹھوس مادے میں تبدیل ہو جاتی ہے",
        "یہ توانائی کے مادے میں تبدیل ہونے کا براہ راست ثبوت ہے۔ روشنی کا ذرہ فنا ہو جاتا ہے اور اس کی انرجی سے ایک عام الیکٹران اور ایک اینٹی میٹر کا پوزیٹران مادی صورت میں وجود پا لیتے ہیں۔"
    ),
    (
        "What dramatic astronomical phenomenon occurs when an electron and a positron meet each other in deep interstellar space (Pair Annihilation)?",
        ["Both particles completely annihilate each other, converting 100 percent of their rest masses into two back-to-back 511 keV gamma-ray photons", "They fuse into a neutral atom of helium", "They collapse into a microscopic black hole", "They form a stable superconducting molecule"],
        "Both particles completely annihilate each other, converting 100 percent of their rest masses into two back-to-back 511 keV gamma-ray photons",
        "Because lepton number and charge balance (+e and -e), total particle mass converts to electromagnetic radiation via E = mc^2. Conservation of momentum mandates two collinear 511 keV photons flying in opposite directions.",
        "جوڑے کی فنا (Pair Annihilation): خلا میں جب ایک الیکٹران اور اینٹی میٹر کا پوزیٹران آپس میں ٹکراتے ہیں تو ان کے ساتھ کیا قیامت پیش آتی ہے؟",
        ["دونوں ذرات ایک دوسرے کو 100 فیصد مکمل فنا کر کے اپنی تمام تر کمیت کو مخالف سمت میں اڑنے والی دو گاما شعاعوں میں تبدیل کر دیتے ہیں", "وہ مل کر ہیلیم کا ایٹم بن جاتے ہیں", "وہ ایک چھوٹا بلیک ہول بنا لیتے ہیں", "وہ ایک مالیکیول بنا کر جڑ جاتے ہیں"],
        "دونوں ذرات ایک دوسرے کو 100 فیصد مکمل فنا کر کے اپنی تمام تر کمیت کو مخالف سمت میں اڑنے والی دو گاما شعاعوں میں تبدیل کر دیتے ہیں",
        "مادے کا ایک ذرہ بھی پیچھے نہیں بچتا۔ سو فیصد مادہ خالص توانائی بن جاتا ہے اور دونوں سمتوں میں 511 کلو الیکٹران وولٹ کے دو فوٹون کائنات میں بکھر جاتے ہیں۔ یہ کائنات کا سب سے طاقتور انرجی ری ایکشن ہے۔"
    ),
    (
        "Why does an atomic clock aboard a fast supersonic aircraft flying east around the world lose time, while an identical clock flying west gains time (the Hafele-Keating Experiment)?",
        ["Kinematic velocity adds to Earth's eastward rotational velocity for the eastbound flight and subtracts for westbound, modulating relativistic time dilation", "Eastbound flights fly into the Sun's magnetic field", "Westbound flights travel downhill geographically", "Jet fuel emits radioactive particles"],
        "Kinematic velocity adds to Earth's eastward rotational velocity for the eastbound flight and subtracts for westbound, modulating relativistic time dilation",
        "In 1971, Hafele and Keating flew cesium clocks on airliners. Relative to a non-rotating Earth-centered inertial frame, eastbound speed is v_rot + v_plane (greater time dilation, clock runs slower), while westbound is v_rot - v_plane (clock runs faster).",
        "ہیفیل کیٹنگ کا ہوائی جہاز کا تجربہ (Hafele-Keating Experiment): دنیا کا چکر لگانے والے جہاز پر مشرق کی طرف اڑنے والی ایٹمی گھڑی سست اور مغرب کی طرف اڑنے والی گھڑی تیز کیوں ہو جاتی ہے؟",
        ["مشرق کی طرف جہاز کی رفتار زمین کے گھماؤ کی رفتار میں جمع ہو کر اس کا وقت مزید سست کر دیتی ہے، جبکہ مغرب کی طرف رفتار کم ہونے سے گھڑی تیز چلتی ہے", "مشرق کی پروازیں مقناطیسی فیلڈ میں جاتی ہیں", "مغرب کی پروازیں جغرافیائی ڈھلوان پر ہوتی ہیں", "ایندھن تابکاری چھوڑتا ہے"],
        "مشرق کی طرف جہاز کی رفتار زمین کے گھماؤ کی رفتار میں جمع ہو کر اس کا وقت مزید سست کر دیتی ہے، جبکہ مغرب کی طرف رفتار کم ہونے سے گھڑی تیز چلتی ہے",
        "خلا کے ساکن فریم سے دیکھنے پر زمین خود مشرق کی طرف گھوم رہی ہے۔ مشرق جانے والا جہاز زمین سے بھی زیادہ تیز دوڑ رہا ہوتا ہے اس لیے اضافیت کے تحت اس کا وقت سست پڑ جاتا ہے، جس کی گھڑیوں نے تصدیق کی۔"
    ),
    (
        "Why does a person looking at an illuminated fiber optic decorative lamp see brilliant points of colored light only at the very tips of the clear plastic strands?",
        ["Total internal reflection confines all light along the smooth transparent core, escaping only where the fibers terminate at raw cut ends", "The tips contain miniature LED light bulbs", "Light travels faster at the ends of plastic", "Plastic absorbs light along the sides"],
        "Total internal reflection confines all light along the smooth transparent core, escaping only where the fibers terminate at raw cut ends",
        "Light entered at the base undergoes continuous total internal reflection along the cylindrical dielectric waveguide. Photons cannot escape until the boundary condition changes at the cleaved terminal facet.",
        "فائبر آپٹک کا لیمپ (Total Internal Reflection in Fiber Tips): فائبر آپٹک لیمپ کے شفاف پلاسٹک کے تاروں میں سائیڈوں سے کوئی روشنی نہیں نکلتی مگر ان کے آخری سرے ستاروں کی طرح کیوں چمکتے ہیں؟",
        ["ٹوٹل انٹرنل ریفلیکشن روشنی کو تار کے اندر قید رکھتی ہے اور روشنی صرف اسی مقام سے باہر نکل سکتی ہے جہاں تار کٹا ہوا اور ختم ہوتا ہے", "تاروں کے سروں پر چھوٹے بلب لگے ہوتے ہیں", "روشنی تار کے سرے پر تیز ہو جاتی ہے", "پلاسٹک سائیڈوں سے روشنی پی جاتا ہے"],
        "ٹوٹل انٹرنل ریفلیکشن روشنی کو تار کے اندر قید رکھتی ہے اور روشنی صرف اسی مقام سے باہر نکل سکتی ہے جہاں تار کٹا ہوا اور ختم ہوتا ہے",
        "پلاسٹک کے تار کی اندرونی دیواریں شیشے کی طرح روشنی کو سو فیصد اندر ہی اچھالتی رہتی ہیں۔ جب تک روشنی تار کے کٹے ہوئے کونے تک نہ پہنچے، وہ باہر ہوا میں فرار نہیں ہو سکتی، اس لیے صرف سرے جگمگاتے ہیں۔"
    ),
]
