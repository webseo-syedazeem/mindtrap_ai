# -*- coding: utf-8 -*-
"""
Tricky Batch 3 (55 items: 136-190).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why did Albert Einstein refer to Quantum Entanglement as 'spooky action at a distance' in the EPR Paradox?",
        ["Measuring one entangled particle instantly determines the quantum state of its entangled twin across the universe without physical signals", "Entangled particles generate ghost shadows", "Quantum particles move through wormholes", "The particles emit audible whispers"],
        "Measuring one entangled particle instantly determines the quantum state of its entangled twin across the universe without physical signals",
        "Einstein, Podolsky, and Rosen argued local realism must hold; however, entangled spin states demonstrate instantaneous quantum non-local correlations.",
        "ای پی آر پیراڈاکس (EPR Paradox) میں البرٹ آئن سٹائن نے کوانٹم اینٹینگلمنٹ کو 'دور سے ہونے والا پراسرار عمل' (Spooky action at a distance) کیوں کہا تھا؟",
        ["ایک کوانٹم ذرے کی پیمائش کائنات کے دوسرے سرے پر موجود جڑواں ذرے کی حالت کا فوری اور بغیر کسی سگنل کے تعین کر دیتی ہے", "اینٹینگلڈ ذرات پراسرار سائے بناتے ہیں", "ذرات خلا کے خفیہ سوراخوں سے گزرتے ہیں", "ذرات آپس میں سرگوشیاں کرتے ہیں"],
        ["ایک کوانٹم ذرے کی پیمائش کائنات کے دوسرے سرے پر موجود جڑواں ذرے کی حالت کا فوری اور بغیر کسی سگنل کے تعین کر دیتی ہے", "اینٹینگلڈ ذرات پراسرار سائے بناتے ہیں", "ذرات خلا کے خفیہ سوراخوں سے گزرتے ہیں", "ذرات آپس میں سرگوشیاں کرتے ہیں"][0],
        "آئن سٹائن کا ماننا تھا کہ روشنی کی رفتار سے تیز کوئی چیز نہیں ہو سکتی، مگر کوانٹم فزکس نے ثابت کیا کہ دو باہم جڑے ذرات کے درمیان باہمی رابطہ پلک جھپکنے سے بھی پہلے اور بغیر کسی سگنل کے سفر کے ہو جاتا ہے۔"
    ),
    (
        "What did John Bell's mathematical theorem and Alain Aspect's experiments prove about the nature of our physical reality?",
        ["The universe cannot be simultaneously local and realistic; local hidden variables do not govern quantum mechanics", "Photons are made of liquid", "Speed of light is infinite in air", "Gravity does not exist at micro scales"],
        "The universe cannot be simultaneously local and realistic; local hidden variables do not govern quantum mechanics",
        "Bell's inequality sets an upper statistical bound for any local hidden variable theory. Experimental violations confirmed that nature exhibits genuine non-local quantum correlations.",
        "بیل کا تھیورم (Bell's Theorem) اور ایلن ایسپیکٹ کے تجربات نے ہماری مادی کائنات کے بارے میں کیا حتمی ثبوت فراہم کیا؟",
        ["کائنات بیک وقت مقامی (Local) اور حقیقی (Realistic) نہیں ہو سکتی؛ کوانٹم دنیا میں کوئی خفیہ چھپے ہوئے متغیرات (Hidden Variables) کام نہیں کر رہے", "روشنی کے ذرات مائع سے بنے ہیں", "ہوا میں روشنی کی رفتار لامحدود ہوتی ہے", "ایٹمی سطح پر کشش ثقل کام نہیں کرتی"],
        ["کائنات بیک وقت مقامی (Local) اور حقیقی (Realistic) نہیں ہو سکتی؛ کوانٹم دنیا میں کوئی خفیہ چھپے ہوئے متغیرات (Hidden Variables) کام نہیں کر رہے", "روشنی کے ذرات مائع سے بنے ہیں", "ہوا میں روشنی کی رفتار لامحدود ہوتی ہے", "ایٹمی سطح پر کشش ثقل کام نہیں کرتی"][0],
        "بیل نے ثابت کیا کہ اگر کائنات مقامی حقائق کے تحت چلتی ہے تو پیمائش کے نتائج ایک خاص حد سے تجاوز نہیں کر سکتے۔ لیب کے تجربات نے اس حد کو توڑ کر ثابت کیا کہ کوانٹم حقیقت مقامی نہیں ہے۔"
    ),
    (
        "What is the Quantum Zeno Effect, and how does it prevent an unstable radioactive particle from decaying?",
        ["Continuously measuring and observing the quantum system resets its wavefunction, effectively freezing it in its initial state", "Continuous light cools the nucleus to absolute zero", "Measurement fields repel radiation", "Detectors absorb nuclear decay energy"],
        "Continuously measuring and observing the quantum system resets its wavefunction, effectively freezing it in its initial state",
        "Because short-time transition probabilities scale quadratically with time (Delta t)^2, frequent projective measurements project the system back into its un-decayed eigenstate.",
        "کوانٹم زینو اثر (Quantum Zeno Effect): ایک تابکار ایٹم کو بار بار اور مسلسل مانیٹر اور چیک کرنے سے اس کا فنا اور ٹوٹنا رک کیوں جاتا ہے؟",
        ["مسلسل اور بار بار پیمائش کرنے سے ایٹم کا کوانٹم ویو فنکشن بار بار ابتدائی حالت پر ری سیٹ ہو کر ساکت رہ جاتا ہے", "مسلسل روشنی ایٹم کو مکمل ٹھنڈا کر دیتی ہے", "پیمائش کرنے والے آلے تابکاری کو پیچھے دھکیلتے ہیں", "کیمرے ایٹم کی انرجی کو چوس لیتے ہیں"],
        ["مسلسل اور بار بار پیمائش کرنے سے ایٹم کا کوانٹم ویو فنکشن بار بار ابتدائی حالت پر ری سیٹ ہو کر ساکت رہ جاتا ہے", "مسلسل روشنی ایٹم کو مکمل ٹھنڈا کر دیتی ہے", "پیمائش کرنے والے آلے تابکاری کو پیچھے دھکیلتے ہیں", "کیمرے ایٹم کی انرجی کو چوس لیتے ہیں"][0],
        "کوانٹم دنیا میں 'دیکھنے' کا عمل ویو فنکشن کو گرا دیتا ہے۔ اگر وقت کے انتہائی چھوٹے وقفوں میں بار بار ایٹم کی پوزیشن ناپی جائے تو وہ اپنی ابتدائی غیر تابکار حالت پر ہی قید ہو کر رہ جاتا ہے۔"
    ),
    (
        "In John Archibald Wheeler's Delayed-Choice Experiment, how does choosing how to measure a photon in the present appear to affect its past history billions of years ago?",
        ["The photon does not acquire a definite past history (wave or particle path) until the final macroscopic measurement configuration is chosen", "The photon travels backwards through time physically", "Future detectors emit tachyon waves", "Lenses store photons in crystal cavities"],
        "The photon does not acquire a definite past history (wave or particle path) until the final macroscopic measurement configuration is chosen",
        "Wheeler showed that photons from distant quasars bent by gravitational lensing remain in a superposition of paths until the astronomer chooses whether to insert a beam splitter today.",
        "وہیلر کا تاخیری انتخاب کا تجربہ (Delayed-Choice Experiment): اربوں سال پرانے فوٹون کے ماضی کے سفر کی تاریخ آج کے دن لیب میں ناپنے کے طریقے سے کیسے طے ہوتی ہے؟",
        ["فوٹون کا ماضی کا راستہ (موج یا ذرہ) تب تک غیر متعین رہتا ہے جب تک کہ آج اس کے حتمی معائنے کا طریقہ کار منتخب نہ کیا جائے", "فوٹون وقت میں سچ مچ پیچھے سفر کرتا ہے", "مستقبل کے کیمرے ٹیکیون لہریں چھوڑتے ہیں", "عدسے فوٹون کو شیشے میں قید رکھتے ہیں"],
        ["فوٹون کا ماضی کا راستہ (موج یا ذرہ) تب تک غیر متعین رہتا ہے جب تک کہ آج اس کے حتمی معائنے کا طریقہ کار منتخب نہ کیا جائے", "فوٹون وقت میں سچ مچ پیچھے سفر کرتا ہے", "مستقبل کے کیمرے ٹیکیون لہریں چھوڑتے ہیں", "عدسے فوٹون کو شیشے میں قید رکھتے ہیں"][0],
        "جب تک زمین پر ٹیلی سکوپ یہ فیصلہ نہیں کرتی کہ دو راستوں کو آپس میں ملانا ہے یا الگ دیکھنا ہے، تب تک کہکشاؤں کے پاس سے گزرتے ہوئے فوٹون نے دونوں میں سے کون سا راستہ چنا تھا، یہ سوال ہی وجود نہیں رکھتا۔"
    ),
    (
        "In the Quantum Eraser experiment, what happens to the interference pattern when researchers destroy or scramble the 'which-way' path information of the photons?",
        ["The wave interference fringes completely re-emerge, proving that wave-particle duality is governed by information availability", "The detector explodes from energy overload", "Photons turn into dark matter", "The laser beam freezes solid"],
        "The wave interference fringes completely re-emerge, proving that wave-particle duality is governed by information availability",
        "When 'which-way' marker polarization is erased via a diagonal polarizer before detection, quantum complementarity allows wave interference patterns to be recovered via correlation.",
        "کوانٹم ریزر کا تجربہ (Quantum Eraser): جب سائنسدان فوٹون کے سوراخ سے گزرنے کی شناختی معلومات (Which-way Information) کو مٹا دیتے ہیں تو اسکرین پر کیا نتیجہ ظاہر ہوتا ہے؟",
        ["موجوں کے باہمی ٹکراؤ کا پیٹرن (Interference Pattern) دوبارہ لوٹ آتا ہے، جس سے ثابت ہوتا ہے کہ کوانٹم رویے کا دارومدار معلومات کی دستیابی پر ہے", "آلہ زیادہ انرجی کی وجہ سے پھٹ جاتا ہے", "فوٹون تاریک مادے میں تبدیل ہو جاتے ہیں", "لیزر کی شعاع برف کی طرح جم جاتی ہے"],
        ["موجوں کے باہمی ٹکراؤ کا پیٹرن (Interference Pattern) دوبارہ لوٹ آتا ہے، جس سے ثابت ہوتا ہے کہ کوانٹم رویے کا دارومدار معلومات کی دستیابی پر ہے", "آلہ زیادہ انرجی کی وجہ سے پھٹ جاتا ہے", "فوٹون تاریک مادے میں تبدیل ہو جاتے ہیں", "لیزر کی شعاع برف کی طرح جم جاتی ہے"][0],
        "جب تک یہ جاننا ممکن ہو کہ فوٹون کس سوراخ سے گزرا، وہ ذرہ بن کر لکیریں بناتا ہے۔ مگر جیسے ہی وہ معلومات کسی آلے سے کھرچ کر مٹا دی جائیں، فوٹون دوبارہ لہر کا روپ دھار کر خوبصورت پیٹرن بنا دیتا ہے۔"
    ),
    (
        "Why is it physically impossible to build a perfect quantum photocopying machine that clones an arbitrary unknown quantum state (the No-Cloning Theorem)?",
        ["Linearity of quantum unitary operators prohibits cloning superposition states without destroying or collapsing the original state", "Photocopier lenses lack sufficient resolution", "Ink molecules are too heavy for quantum spin", "Quantum states require high voltages"],
        "Linearity of quantum unitary operators prohibits cloning superposition states without destroying or collapsing the original state",
        "Wootters, Zurek, and Dieks proved that a unitary operator U obeying U(|psi>|0>) = |psi>|psi> cannot hold for arbitrary superpositions |psi> = a|0> + b|1> due to quantum linearity.",
        "نان کلوننگ تھیورم (No-Cloning Theorem): کسی نامعلوم کوانٹم حالت (Quantum State) کی بالکل ہو بہو دوسری کاپی بنانا طبعی قوانین کے مطابق قطعی ناممکن کیوں ہے؟",
        ["کوانٹم میکینکس کی یونٹری مساواتوں کی لکیری نوعیت اصل حالت کو مسخ یا تباہ کیے بغیر اس کی ہوبہو نقل بنانے کی اجازت نہیں دیتی", "فوٹو کاپی مشین کے لینز اتنے باریک نہیں ہوتے", "سیاہی کے مالیکیول کوانٹم سپن کے لیے وزنی ہیں", "کوانٹم حالتوں کے لیے ہائی وولٹیج درکار ہوتا ہے"],
        ["کوانٹم میکینکس کی یونٹری مساواتوں کی لکیری نوعیت اصل حالت کو مسخ یا تباہ کیے بغیر اس کی ہوبہو نقل بنانے کی اجازت نہیں دیتی", "فوٹو کاپی مشین کے لینز اتنے باریک نہیں ہوتے", "سیاہی کے مالیکیول کوانٹم سپن کے لیے وزنی ہیں", "کوانٹم حالتوں کے لیے ہائی وولٹیج درکار ہوتا ہے"][0],
        "اگر آپ کسی نامعلوم سپر پوزیشن والے ذرے کو کاپی کرنا چاہیں تو اس کا جائزہ لینا پڑے گا، اور جائزہ لیتے ہی اس کی اصل حالت تباہ ہو جائے گی۔ یہی قانون کوانٹم انکرپشن کو اٹل سیکیورٹی فراہم کرتا ہے۔"
    ),
    (
        "How does Quantum Teleportation transfer the exact quantum state of a photon to a remote location without sending the photon itself across space?",
        ["By using a pre-shared entangled pair, performing a Bell-state measurement, and transmitting 2 classical bits to reconstruct the state", "By converting the photon into sound waves", "By drilling a micro-wormhole through air", "By compressing the photon in a diamond"],
        "By using a pre-shared entangled pair, performing a Bell-state measurement, and transmitting 2 classical bits to reconstruct the state",
        "Bennett et al. showed that measuring the joint state of the input qubit and one half of an EPR pair collapses both, allowing the receiver to rotate the other EPR qubit via classical instructions.",
        "کوانٹم ٹیلی پورٹیشن (Quantum Teleportation): فوٹون کو خلا میں بھیجے بغیر اس کی ہو بہو کوانٹم حالت کو دور دراز مقام پر کیسے منتقل کیا جاتا ہے؟",
        ["پہلے سے جڑے ہوئے اینٹینگلڈ جوڑے کی مدد سے بیل اسٹیٹ پیمائش کر کے اور صرف 2 روایتی بٹس بھیج کر دوسری طرف حالت کو دوبارہ بنا لیا جاتا ہے", "فوٹون کو صوتی لہروں میں بدل کر", "ہوا میں چھوٹا سوراخ کر کے", "فوٹون کو ہیرے میں دبا کر"],
        ["پہلے سے جڑے ہوئے اینٹینگلڈ جوڑے کی مدد سے بیل اسٹیٹ پیمائش کر کے اور صرف 2 روایتی بٹس بھیج کر دوسری طرف حالت کو دوبارہ بنا لیا جاتا ہے", "فوٹون کو صوتی لہروں میں بدل کر", "ہوا میں چھوٹا سوراخ کر کے", "فوٹون کو ہیرے میں دبا کر"][0],
        "اس میں مادہ یا توانائی سفر نہیں کرتی بلکہ معلومات اور کوانٹم اینٹینگلمنٹ کی بدولت دوسری طرف موجود ذرے کو بعینہٖ پہلے ذرے کی حالت میں ڈھال دیا جاتا ہے، جبکہ پہلا ذرہ ختم ہو جاتا ہے۔"
    ),
    (
        "Why did Erwin Schrödinger propose his famous thought experiment involving a cat in a sealed box with radioactive poison (Schrödinger's Cat)?",
        ["To illustrate the absurdity of applying Copenhagen quantum superposition to macroscopic everyday physical objects", "To prove that cats have nine lives", "To test radioactive gas masks", "To design safe animal cages"],
        "To illustrate the absurdity of applying Copenhagen quantum superposition to macroscopic everyday physical objects",
        "Schrödinger intended the paradox as a critique: if Copenhagen interpretation holds without boundary, an unobserved macroscopic cat must be simultaneously dead and alive, which defies physical intuition.",
        "شروڈنگر کی بلی کا معمہ (Schrödinger's Cat): ارون شروڈنگر نے بند ڈبے میں زہر اور بلی کا یہ مشہور فکری تجربہ دراصل کس مقصد کے لیے پیش کیا تھا؟",
        ["کوانٹم سپر پوزیشن کے قانون کو روزمرہ کی بڑی مادی دنیا پر لاگو کرنے کے مضحکہ خیز اور غیر منطقی نتائج کو بے نقاب کرنے کے لیے", "یہ ثابت کرنے کے لیے کہ بلی کی نو زندگیاں ہوتی ہیں", "تابکار گیس ماسک کی جانچ کرنے کے لیے", "جانوروں کے محفوظ پنجرے بنانے کے لیے"],
        ["کوانٹم سپر پوزیشن کے قانون کو روزمرہ کی بڑی مادی دنیا پر لاگو کرنے کے مضحکہ خیز اور غیر منطقی نتائج کو بے نقاب کرنے کے لیے", "یہ ثابت کرنے کے لیے کہ بلی کی نو زندگیاں ہوتی ہیں", "تابکار گیس ماسک کی جانچ کرنے کے لیے", "جانوروں کے محفوظ پنجرے بنانے کے لیے"][0],
        "وہ یہ دکھانا چاہتے تھے کہ اگر ایٹم کی لہر دیکھنے سے پہلے دونوں حالتوں میں رہتی ہے، تو کیا ڈبے میں بند بلی بھی بیک وقت زندہ اور مردہ رہ سکتی ہے؟ اس مضحکہ خیزی سے پیمائش کے اصل مسئلے کی نشان دہی ہوئی۔"
    ),
    (
        "In Eugene Wigner's 'Wigner's Friend' paradox, why does the collapse of the quantum wave function become subjective and relative to the observer?",
        ["To the friend inside the lab the state collapses upon seeing it, but to Wigner waiting outside, friend and lab remain in a joint superposition", "Wigner suffers from memory loss", "The lab rotates at light speed", "The friend wears sunglasses"],
        "To the friend inside the lab the state collapses upon seeing it, but to Wigner waiting outside, friend and lab remain in a joint superposition",
        "Wigner demonstrated that standard Copenhagen mechanics lacks an objective boundary for collapse: what is a collapsed definite outcome for one observer is an uncollapsed entangled state for another.",
        "وگنر کا دوست کا معمہ (Wigner's Friend Paradox): کوانٹم میکینکس میں ویو فنکشن کا گرنا مختلف مشاہدہ کاروں کے لیے الگ اور متضاد کیوں ہو جاتا ہے؟",
        ["لیب کے اندر موجود دوست کے لیے پیمائش کا حتمی نتیجہ آ چکا ہوتا ہے، جبکہ باہر کھڑے وگنر کے لیے دوست اور لیب دونوں ابھی بھی مشترکہ سپر پوزیشن میں ہیں", "وگنر کی یادداشت چلی جاتی ہے", "لیب روشنی کی رفتار سے گھومتی ہے", "دوست نے کالا چشمہ پہنا ہوتا ہے"],
        ["لیب کے اندر موجود دوست کے لیے پیمائش کا حتمی نتیجہ آ چکا ہوتا ہے، جبکہ باہر کھڑے وگنر کے لیے دوست اور لیب دونوں ابھی بھی مشترکہ سپر پوزیشن میں ہیں", "وگنر کی یادداشت چلی جاتی ہے", "لیب روشنی کی رفتار سے گھومتی ہے", "دوست نے کالا چشمہ پہنا ہوتا ہے"][0],
        "اگر اندر والا دوست نتیجہ دیکھ لے تو اس کے لیے حقیقت طے ہو گئی، مگر جب تک وہ باہر آ کر وگنر کو نہ بتائے، باہر والے کے لیے دوست اور ایٹم دونوں تمام ممکنہ حالتوں کے مجموعے میں قید رہتے ہیں۔"
    ),
    (
        "How does Hugh Everett's 'Many-Worlds Interpretation' resolve the quantum measurement problem without requiring wave function collapse?",
        ["Every quantum measurement splits the universe into non-communicating parallel branches representing every possible outcome", "It replaces electrons with miniature planets", "It requires observers to meditate", "It declares that atoms do not exist"],
        "Every quantum measurement splits the universe into non-communicating parallel branches representing every possible outcome",
        "Everett proposed pure unitary Schrödinger evolution: rather than wavefunction collapse, the universal wavefunction continuously branches, realizing every decoherent quantum possibility in parallel realities.",
        "کئی جہانوں کی تھیوری (Many-Worlds Interpretation): ایورٹ کا یہ نظریہ بغیر ویو فنکشن کو گرائے کوانٹم پیمائش کے معمے کو کیسے حل کرتا ہے؟",
        ["ہر کوانٹم امکان کے واقع ہونے پر کائنات متوازی شاخوں میں تقسیم ہو جاتی ہے جس میں ہر ممکنہ نتیجہ کسی نہ کسی الگ جہان میں سچ ہوتا ہے", "یہ الیکٹرانز کو چھوٹے سیاروں سے بدل دیتا ہے", "یہ مشاہدہ کاروں کو مراقبہ کرنے کا کہتا ہے", "یہ کہتا ہے کہ ایٹموں کا کوئی وجود نہیں"],
        ["ہر کوانٹم امکان کے واقع ہونے پر کائنات متوازی شاخوں میں تقسیم ہو جاتی ہے جس میں ہر ممکنہ نتیجہ کسی نہ کسی الگ جہان میں سچ ہوتا ہے", "یہ الیکٹرانز کو چھوٹے سیاروں سے بدل دیتا ہے", "یہ مشاہدہ کاروں کو مراقبہ کرنے کا کہتا ہے", "یہ کہتا ہے کہ ایٹموں کا کوئی وجود نہیں"][0],
        "اس نظریے کے مطابق بلی نہ زندہ رہتی ہے نہ مرتی ہے، بلکہ کائنات دو حصوں میں بٹ جاتی ہے: ایک دنیا میں بلی زندہ ملتی ہے اور دوسری دنیا میں مردہ، اور ہر دنیا کا اپنا خودمختار تسلسل ہوتا ہے۔"
    ),
    (
        "Why do macroscopic objects like chairs and cars never exhibit quantum wave interference in everyday human experience (Quantum Decoherence)?",
        ["Trillions of relentless collisions with surrounding environmental photons and air molecules rapidly destroy quantum phase coherence", "Macroscopic objects possess too much magnetic charge", "Gravity heats objects until waves melt", "Earth rotates too rapidly"],
        "Trillions of relentless collisions with surrounding environmental photons and air molecules rapidly destroy quantum phase coherence",
        "Quantum decoherence theory (Zurek, Zeh) shows that interaction with environmental thermal baths leaks phase information within 10^-20 seconds, forcing the density matrix into apparent classical probabilities.",
        "کوانٹم ڈی کوہیرنس (Quantum Decoherence): کرسی اور گاڑی جیسی روزمرہ کی بڑی چیزیں کوانٹم لہروں کی طرح دو جگہ بیک وقت کیوں نظر نہیں آتیں؟",
        ["ارد گرد کی ہوا کے کھربوں مالیکیولز اور روشنی کے فوٹونز کی مسلسل ٹکریں کوانٹم فیز کے توازن کو پلک جھپکنے میں برباد کر دیتی ہیں", "بڑی چیزوں میں مقناطیسی چارج زیادہ ہوتا ہے", "کشش ثقل چیزوں کو گرم کر کے لہروں کو پگھلا دیتی ہے", "زمین بہت تیز گھومتی ہے"],
        ["ارد گرد کی ہوا کے کھربوں مالیکیولز اور روشنی کے فوٹونز کی مسلسل ٹکریں کوانٹم فیز کے توازن کو پلک جھپکنے میں برباد کر دیتی ہیں", "بڑی چیزوں میں مقناطیسی چارج زیادہ ہوتا ہے", "کشش ثقل چیزوں کو گرم کر کے لہروں کو پگھلا دیتی ہے", "زمین بہت تیز گھومتی ہے"][0],
        "جب تک کوئی چیز ماحول سے بالکل الگ تھلگ نہ ہو، ماحول کے ان گنت ذرات اس کے کوانٹم توازن کو مٹا کر اسے روایتی فزکس کے عام اور ٹھوس اصولوں پر چلنے پر مجبور کر دیتے ہیں۔"
    ),
    (
        "In the Aharonov-Bohm Effect, how can an electron beam shift its quantum wave phase when traveling through a region where the magnetic field is strictly zero?",
        ["The electron couples directly to the magnetic vector potential A, which remains non-zero outside the enclosed magnetic field", "Electrons tunnel through the magnetic core", "The solenoid vibrates with sound", "Earth's crust emits stray ions"],
        "The electron couples directly to the magnetic vector potential A, which remains non-zero outside the enclosed magnetic field",
        "Even when magnetic field B = curl(A) = 0, the magnetic vector potential A along the electron trajectory contributes a gauge-invariant phase shift proportional to the enclosed magnetic flux.",
        "آہارونوف بوم اثر (Aharonov-Bohm Effect): ایک الیکٹران جب اس خالی جگہ سے گزرتا ہے جہاں مقناطیسی فیلڈ مکمل طور پر صفر ہو، تب بھی اس کی لہر کا فیز کیوں بدل جاتا ہے؟",
        ["الیکٹران مقناطیسی ویکٹر پوٹینشل (Vector Potential A) سے متاثر ہوتا ہے جو فیلڈ صفر ہونے کے باوجود اس علاقے میں موجود ہوتا ہے", "الیکٹران مقناطیس کے اندر سرنگ بنا لیتے ہیں", "سلنڈر آواز کی لہروں سے کانپتا ہے", "زمین کی سطح آوارہ آئنز چھوڑتی ہے"],
        ["الیکٹران مقناطیسی ویکٹر پوٹینشل (Vector Potential A) سے متاثر ہوتا ہے جو فیلڈ صفر ہونے کے باوجود اس علاقے میں موجود ہوتا ہے", "الیکٹران مقناطیس کے اندر سرنگ بنا لیتے ہیں", "سلنڈر آواز کی لہروں سے کانپتا ہے", "زمین کی سطح آوارہ آئنز چھوڑتی ہے"][0],
        "کلاسیکی فزکس میں صرف فیلڈ اہم تھی، مگر کوانٹم فزکس میں پوٹینشل زیادہ بنیادی حقیقت ہے۔ اگرچہ مقناطیسی طاقت صفر ہو، مگر اس کا پوٹینشل لہر کی رفتار اور فیز کو موڑ دیتا ہے۔"
    ),
    (
        "Why is the Hall resistance in the Quantum Hall Effect quantized with extreme mathematical precision into exact plateaus of h / (n * e^2)?",
        ["Topological invariants (Chern numbers) protect the chiral edge conduction channels against all impurities and geometric imperfections", "Laboratories calibrate instruments to fixed constants", "Voltmeters round numbers automatically", "Liquid nitrogen freezes copper defects"],
        "Topological invariants (Chern numbers) protect the chiral edge conduction channels against all impurities and geometric imperfections",
        "Thouless, Kohmoto, Nightingale, and den Nijs (TKNN) showed the Hall conductance is directly proportional to the first Chern number, a topological integer immune to continuous deformations and disorder.",
        "کوانٹم ہال اثر (Quantum Hall Effect): انتہائی سردی اور طاقتور مقناطیس میں برقی مزاحمت حیرت انگیز درستگی کے ساتھ خاص مستقل اعداد (h / e^2) کے پہاڑوں پر کیوں رکتی ہے؟",
        ["ٹوپولوجیکل ساخت (Chern Numbers) برقی لہروں کے کناروں کو مادے کی ہر قسم کی ناپاکی اور گندگی سے مکمل محفوظ رکھتی ہے", "لیبارٹری کے آلے خود بخود اعداد فکس کر دیتے ہیں", "وولٹ میٹر راؤنڈ فگر دکھاتا ہے", "ٹھنڈی گیس تانبے کے نقائص جما دیتی ہے"],
        ["ٹوپولوجیکل ساخت (Chern Numbers) برقی لہروں کے کناروں کو مادے کی ہر قسم کی ناپاکی اور گندگی سے مکمل محفوظ رکھتی ہے", "لیبارٹری کے آلے خود بخود اعداد فکس کر دیتے ہیں", "وولٹ میٹر راؤنڈ فگر دکھاتا ہے", "ٹھنڈی گیس تانبے کے نقائص جما دیتی ہے"][0],
        "مادے میں لاکھ خرابیاں یا ملاوٹیں ہوں، کناروں سے بہنے والی برقی لہروں کی ٹوپولوجی بالکل ایسی اٹل ہوتی ہے جیسے کسی ڈونٹ میں سوراخوں کی تعداد۔ اسی لیے یہ عالمی پیمائش کا مستقل معیار بن گیا۔"
    ),
    (
        "What bizarre quasi-particles emerge in the Fractional Quantum Hall Effect that carry a fractional electric charge of 1/3 or 1/5 of an electron?",
        ["Anyons: collective topological excitations formed by electrons bound to vortices of quantized magnetic flux", "Free quarks leaking from atomic nuclei", "Microscopic black holes", "Neutral dark matter condensates"],
        "Anyons: collective topological excitations formed by electrons bound to vortices of quantized magnetic flux",
        "Robert Laughlin explained that 2D electron correlation under extreme magnetic fields produces composite quasiparticles with fractional charge e/3 and fractional braiding statistics (anyons).",
        "فریکشنل کوانٹم ہال اثر (Fractional Quantum Hall Effect): اس حالت میں الیکٹران کے ایک تہائی (1/3) چارج والے عجیب ذرات کیسے وجود میں آ جاتے ہیں؟",
        ["اینیونز (Anyons): الیکٹرانز اور مقناطیسی بھنوروں کے باہمی ملاپ سے بننے والی اجتماعی ٹوپولوجیکل لہریں جو جزوی چارج رکھتی ہیں", "ایٹم سے آزاد کوارکس کا اخراج", "خوردبینی بلیک ہولز کا بننا", "تاریک مادے کا جم جانا"],
        ["اینیونز (Anyons): الیکٹرانز اور مقناطیسی بھنوروں کے باہمی ملاپ سے بننے والی اجتماعی ٹوپولوجیکل لہریں جو جزوی چارج رکھتی ہیں", "ایٹم سے آزاد کوارکس کا اخراج", "خوردبینی بلیک ہولز کا بننا", "تاریک مادے کا جم جانا"][0],
        "شدید مقناطیس میں الیکٹرانز ایک دوسرے کے گرد گھوم کر ایک مشترکہ مائع بناتے ہیں جس کے ارتعاش سے ایسے غیر معمولی ذرات جنم لیتے ہیں جو الیکٹران کا تیسرا حصہ چارج رکھتے ہیں۔"
    ),
    (
        "What occurs when dilute rubidium gas is cooled to within billionths of a degree above absolute zero to form a Bose-Einstein Condensate (BEC)?",
        ["Atomic de Broglie wavelengths overlap, causing millions of atoms to drop into the lowest quantum state and act as a single giant super-atom", "Atoms fuse into heavy uranium", "Electrons stop spinning permanently", "Gas atoms crystallize into solid diamond"],
        "Atomic de Broglie wavelengths overlap, causing millions of atoms to drop into the lowest quantum state and act as a single giant super-atom",
        "When thermal de Broglie wavelength lambda_dB exceeds inter-particle spacing, bosons undergo macroscopic ground-state occupation, forming a single coherent macroscopic wavefunction.",
        "بوس آئن سٹائن کنڈینسیٹ (Bose-Einstein Condensate): گیس کو مطلق صفر (-273 ڈگری) کے انتہائی قریب ٹھنڈا کرنے پر لاکھوں ایٹمز کے ساتھ کیا عجیب واقعہ پیش آتا ہے؟",
        ["ایٹموں کی کوانٹم لہریں آپس میں مدغم ہو جاتی ہیں جس سے لاکھوں ایٹم مل کر ایک واحد دیوہیکل 'سپر ایٹم' کی طرح برتاؤ کرنے لگتے ہیں", "ایٹم فیوز ہو کر یورینیم بن جاتے ہیں", "الیکٹران ہمیشہ کے لیے گھومنا بند کر دیتے ہیں", "گیس جم کر ہیرا بن جاتی ہے"],
        ["ایٹموں کی کوانٹم لہریں آپس میں مدغم ہو جاتی ہیں جس سے لاکھوں ایٹم مل کر ایک واحد دیوہیکل 'سپر ایٹم' کی طرح برتاؤ کرنے لگتے ہیں", "ایٹم فیوز ہو کر یورینیم بن جاتے ہیں", "الیکٹران ہمیشہ کے لیے گھومنا بند کر دیتے ہیں", "گیس جم کر ہیرا بن جاتی ہے"][0],
        "شدید ٹھنڈک میں ایٹموں کی انفرادی پہچان ختم ہو جاتی ہے۔ وہ سب ایک ہی نچلی ترین کوانٹم حالت میں جمع ہو کر ایسے یکجان ہو جاتے ہیں جیسے لاکھوں ساز ایک ہی سر میں بج رہے ہوں۔"
    ),
    (
        "Why does a supercurrent flow continuously across a thin insulating barrier between two superconductors without any applied voltage (the DC Josephson Effect)?",
        ["Cooper pairs of electrons quantum tunnel coherently through the barrier due to a macroscopic phase difference", "High voltage melts the insulator", "Electrons jump through thermal sparks", "Magnetic fields push protons through"],
        "Cooper pairs of electrons quantum tunnel coherently through the barrier due to a macroscopic phase difference",
        "Brian Josephson predicted that macroscopic phase coherence across a barrier allows Cooper pairs to tunnel without dissipation: I = I_c * sin(Delta phi).",
        "جوزفسن اثر (Josephson Effect): دو سپر کنڈکٹرز کے درمیان موصلیت والے پتلے پردے کے باوجود بغیر کسی وولٹیج کے مستقل بجلی کیسے دوڑتی رہتی ہے؟",
        ["الیکٹرانز کے کوپر جوڑے (Cooper Pairs) کوانٹم فیز کے فرق کی وجہ سے موصل پردے کے آر پار کوانٹم سرنگ بنا کر پار نکل جاتے ہیں", "ہائی وولٹیج موصل کو پگھلا دیتا ہے", "حرارتی چنگاریاں الیکٹرانز کو اچھالتی ہیں", "مقناطیس پروٹانز کو دھکیلتا ہے"],
        ["الیکٹرانز کے کوپر جوڑے (Cooper Pairs) کوانٹم فیز کے فرق کی وجہ سے موصل پردے کے آر پار کوانٹم سرنگ بنا کر پار نکل جاتے ہیں", "ہائی وولٹیج موصل کو پگھلا دیتا ہے", "حرارتی چنگاریاں الیکٹرانز کو اچھالتی ہیں", "مقناطیس پروٹانز کو دھکیلتا ہے"][0],
        "سپر کنڈکٹر میں الیکٹرانز جوڑوں کی شکل میں ایک مشترکہ کوانٹم لہر بناتے ہیں۔ یہ لہر اتنی طاقتور ہوتی ہے کہ وہ درمیان کی غیر موصل رکاوٹ سے بغیر کسی مزاحمت کے پار گزر جاتی ہے۔"
    ),
    (
        "How can an alpha particle escape the massive Coulomb electric barrier of an atomic nucleus when its kinetic energy is far below the required escape energy?",
        ["Quantum Tunneling: the alpha particle's wave function extends through the finite potential barrier, allowing non-zero transmission probability", "Nuclear gravity repels the alpha particle", "Electrons pull the alpha particle outside", "The nucleus splits mechanically"],
        "Quantum Tunneling: the alpha particle's wave function extends through the finite potential barrier, allowing non-zero transmission probability",
        "George Gamow explained alpha decay via quantum tunneling: the transmission coefficient T ~ exp(-2 * integral(sqrt(2m(V - E))) dx) allows escape despite E < V_coulomb.",
        "کوانٹم ٹنلنگ اور الفا اخراج (Alpha Decay Tunneling): ایٹم کے مرکزے سے الفا ذرہ اس برقی دیوار کو کیسے پار کر لیتا ہے جس کو توڑنے کی انرجی اس کے پاس ہوتی ہی نہیں؟",
        ["کوانٹم ٹنلنگ (سرنگ سازی): الفا ذرے کی کوانٹم لہر ایٹمی دیوار کے آر پار پھیلتی ہے جس سے اس کے دیوار کے دوسری طرف ظاہر ہونے کا امکان پیدا ہو جاتا ہے", "مرکزے کی کشش ثقل اسے دور پھینکتی ہے", "باہر کے الیکٹران اسے کھینچ لیتے ہیں", "مرکزہ مکینیکل طور پر کٹ جاتا ہے"],
        ["کوانٹم ٹنلنگ (سرنگ سازی): الفا ذرے کی کوانٹم لہر ایٹمی دیوار کے آر پار پھیلتی ہے جس سے اس کے دیوار کے دوسری طرف ظاہر ہونے کا امکان پیدا ہو جاتا ہے", "مرکزے کی کشش ثقل اسے دور پھینکتی ہے", "باہر کے الیکٹران اسے کھینچ لیتے ہیں", "مرکزہ مکینیکل طور پر کٹ جاتا ہے"][0],
        "اگر ایک گیند کو اونچی دیوار کے اوپر سے پھینکنے کی انرجی نہ ہو تو وہ واپس آتی ہے، مگر کوانٹم دنیا میں ذرہ ایک لہر کی طرح دیوار کے اندر سے سرنگ بنا کر اچانک باہر نکل آتا ہے۔"
    ),
    (
        "Why does Stephen Hawking's discovery of Hawking Radiation lead to the profound 'Black Hole Information Paradox'?",
        ["Thermal radiation carries zero information about swallowed matter, meaning complete evaporation would violate quantum unitarity", "Black holes expand infinitely", "The radiation causes stars to freeze", "Event horizons reflect gamma lasers"],
        "Thermal radiation carries zero information about swallowed matter, meaning complete evaporation would violate quantum unitarity",
        "Quantum mechanics dictates that quantum state evolution is strictly unitary (information is conserved). Pure black hole evaporation into thermal radiation would turn pure states into mixed states, destroying information.",
        "بلیک ہول انفارمیشن کا معمہ (Hawking Radiation Paradox): ہاکنگ ریڈی ایشن کے ذریعے بلیک ہول کے آہستہ آہستہ بخارات بن کر اڑنے سے کوانٹم فزکس کا بنیادی اصول خطرے میں کیوں پڑ جاتا ہے؟",
        ["خارج ہونے والی حرارتی لہروں میں نگلی گئی چیزوں کی کوئی کوانٹم معلومات نہیں ہوتیں، جس سے بلیک ہول کے مٹنے پر کائنات کی معلومات ضائع ہو جائیں گی", "بلیک ہولز لامحدود پھیل جاتے ہیں", "اس تابکاری سے ستارے جم جاتے ہیں", "واقعات کا افق گاما لہروں کو اچھالتا ہے"],
        ["خارج ہونے والی حرارتی لہروں میں نگلی گئی چیزوں کی کوئی کوانٹم معلومات نہیں ہوتیں، جس سے بلیک ہول کے مٹنے پر کائنات کی معلومات ضائع ہو جائیں گی", "بلیک ہولز لامحدود پھیل جاتے ہیں", "اس تابکاری سے ستارے جم جاتے ہیں", "واقعات کا افق گاما لہروں کو اچھالتا ہے"][0],
        "کوانٹم فزکس کا اٹل اصول ہے کہ معلومات کبھی فنا نہیں ہو سکتیں۔ اگر بلیک ہول سب کچھ نگل کر صرف بے ترتیب حرارت چھوڑ کر غائب ہو جائے تو ماضی کی تاریخ کائنات سے ہمیشہ کے لیے مٹ جائے گی۔"
    ),
    (
        "What radical cosmological concept is posited by the Holographic Principle (AdS/CFT correspondence)?",
        ["All physical phenomena occurring within a 3D volume of spacetime can be mathematically described on its 2D outer boundary", "The universe is a computer matrix made of glass", "Planets are 2D paper cutouts", "Light is an optical illusion"],
        "All physical phenomena occurring within a 3D volume of spacetime can be mathematically described on its 2D outer boundary",
        "Gerard 't Hooft, Leonard Susskind, and Juan Maldacena showed that quantum gravity in an Anti-de Sitter bulk is dual to a conformal field theory on its boundary, scaling entropy with surface area.",
        "ہولوگرافک اصول (Holographic Principle): جدید نظریاتی طبیعیات کا یہ حیران کن ماڈل ہماری کائنات کے بارے میں کیا انکشاف کرتا ہے؟",
        ["ہمارے سہ رخی (3D) حجم میں ہونے والے تمام مادی و ثقلی واقعات دراصل بیرونی دو رخی (2D) سرحد پر لکھی معلومات کا عکس ہیں", "کائنات شیشے کا بنا کمپیوٹر ہے", "سیارے کاغذ کے گول کٹے ہوئے ٹکڑے ہیں", "روشنی محض ایک نظر کا دھوکہ ہے"],
        ["ہمارے سہ رخی (3D) حجم میں ہونے والے تمام مادی و ثقلی واقعات دراصل بیرونی دو رخی (2D) سرحد پر لکھی معلومات کا عکس ہیں", "کائنات شیشے کا بنا کمپیوٹر ہے", "سیارے کاغذ کے گول کٹے ہوئے ٹکڑے ہیں", "روشنی محض ایک نظر کا دھوکہ ہے"][0],
        "جس طرح کریڈٹ کارڈ پر دو رخی تصویر تھری ڈی نظر آتی ہے، اسی طرح بلیک ہول اور کائنات کے اندرونی حجم کی تمام تر فزکس اور اینٹروپی اس کے گرد لپٹی بیرونی سطح پر پوری طرح کوڈ کی جا سکتی ہے۔"
    ),
    (
        "How can an advanced civilization theoretically extract clean energy from a spinning Kerr black hole (the Penrose Process)?",
        ["By dropping an object into the ergosphere that splits, sending negative energy into the hole while the other piece escapes with surplus energy", "By drilling geothermal pipes into the event horizon", "By shining giant mirrors to reflect gravity", "By towing the black hole near a star"],
        "By dropping an object into the ergosphere that splits, sending negative energy into the hole while the other piece escapes with surplus energy",
        "Roger Penrose showed that within the ergosphere (outside the event horizon), frame-dragging allows negative energy orbits relative to infinity, reducing the black hole's spin and boosting escaping mass-energy.",
        "پینروز کا طریقہ کار (Penrose Process): گھومتے ہوئے بلیک ہول سے توانائی نچوڑنے کا یہ نظریاتی طریقہ کیسے کام کرتا ہے؟",
        ["بلیک ہول کے ارگواسفیئر (Ergosphere) میں کوئی چیز پھینک کر اسے دو ٹکڑوں میں توڑنا، جس سے ایک منفی انرجی نگل جائے اور دوسرا اضافی طاقت لے کر باہر بھاگے", "واقعات کے افق میں پائپ ڈال کر", "بڑے آئینے لگا کر کشش ثقل پلٹانا", "بلیک ہول کو ستارے کے قریب باندھنا"],
        ["بلیک ہول کے ارگواسفیئر (Ergosphere) میں کوئی چیز پھینک کر اسے دو ٹکڑوں میں توڑنا، جس سے ایک منفی انرجی نگل جائے اور دوسرا اضافی طاقت لے کر باہر بھاگے", "واقعات کے افق میں پائپ ڈال کر", "بڑے آئینے لگا کر کشش ثقل پلٹانا", "بلیک ہول کو ستارے کے قریب باندھنا"][0],
        "گھومتا بلیک ہول اپنے گرد خلا کو چرخے کی طرح کاتتا ہے۔ اس کے بیرونی دائرے میں چیز پھینک کر ایک حصہ گرا دیا جائے تو بلیک ہول کے گھماؤ کی رفتار کم ہو جاتی ہے اور دوسرا حصہ اصل سے زیادہ انرجی لے کر نکلتا ہے۔"
    ),
    (
        "Why does an atomic clock placed at the top of a high mountain tick measurably faster than an identical atomic clock at sea level (Gravitational Time Dilation)?",
        ["Stronger gravitational fields at lower altitudes slow down the passage of time relative to weaker fields higher up", "Mountain air has lower barometric pressure", "Cosmic rays energize cesium atoms", "The mountain clock travels faster through space"],
        "Stronger gravitational fields at lower altitudes slow down the passage of time relative to weaker fields higher up",
        "Einstein's General Relativity dictates that clocks in deeper gravitational potentials run slower: t_0 = t_f * sqrt(1 - 2GM / (rc^2)). The Pound-Rebka experiment verified this shift precisely.",
        "کشش ثقل کی وجہ سے وقت کا سست ہونا (Gravitational Time Dilation): بلند پہاڑ کی چوٹی پر رکھی ایٹمی گھڑی سمندر کے کنارے رکھی گھڑی سے تیز کیوں چلتی ہے؟",
        ["زمین کے مرکز کے قریب کشش ثقل زیادہ طاقتور ہوتی ہے جو وقت کے گزرنے کی رفتار کو سست کر دیتی ہے، جبکہ بلندی پر کشش کم ہونے سے وقت تیز گزرتا ہے", "پہاڑ پر ہوا کا دباؤ کم ہوتا ہے", "کائناتی شعاعیں ایٹموں کو تیز کرتی ہیں", "پہاڑ خلا میں زیادہ رفتار سے گھومتا ہے"],
        ["زمین کے مرکز کے قریب کشش ثقل زیادہ طاقتور ہوتی ہے جو وقت کے گزرنے کی رفتار کو سست کر دیتی ہے، جبکہ بلندی پر کشش کم ہونے سے وقت تیز گزرتا ہے", "پہاڑ پر ہوا کا دباؤ کم ہوتا ہے", "کائناتی شعاعیں ایٹموں کو تیز کرتی ہیں", "پہاڑ خلا میں زیادہ رفتار سے گھومتا ہے"][0],
        "کشش ثقل محض چیزوں کو کھینچتی نہیں بلکہ خود وقت کی رفتار کو سست کر دیتی ہے۔ گہری کشش میں وقت کے سیکنڈ لمبے ہو جاتے ہیں، اس لیے پہاڑ پر موجود گھڑی کے سیکنڈ جلدی جلدی گزرتے ہیں۔"
    ),
    (
        "How did NASA's Gravity Probe B experiment physically confirm the 'Frame-Dragging' (Lense-Thirring) effect predicted by Einstein's General Relativity?",
        ["By measuring the microscopic gyroscopic precession caused by Earth dragging the fabric of spacetime along with its spin", "By timing laser flashes sent to the Moon", "By observing solar flares bend", "By dropping bowling balls in orbit"],
        "By measuring the microscopic gyroscopic precession caused by Earth dragging the fabric of spacetime along with its spin",
        "A rotating mass drags spacetime around itself like honey stirred with a spoon. Gravity Probe B's ultra-precise superconducting gyroscopes measured Earth's frame-dragging drift of 37 milliarcseconds per year.",
        "فریم ڈریگنگ اثر (Frame-Dragging / Gravity Probe B): ناسا کے سیٹلائٹ نے زمین کے گھماؤ کے بارے میں آئن سٹائن کی کس حیران کن پیش گوئی کو سچ ثابت کیا؟",
        ["زمین اپنے گھومنے کے ساتھ ساتھ اپنے ارد گرد کے زمان و مکان (Spacetime) کے تانے بانے کو بھی شہد میں چمچ کی طرح اپنے ساتھ گھسیٹتی ہے", "چاند پر لیزر پھینک کر وقت ناپنے سے", "سورج کے شعلوں کو مڑتے دیکھ کر", "مدار میں گیندیں گرا کر"],
        ["زمین اپنے گھومنے کے ساتھ ساتھ اپنے ارد گرد کے زمان و مکان (Spacetime) کے تانے بانے کو بھی شہد میں چمچ کی طرح اپنے ساتھ گھسیٹتی ہے", "چاند پر لیزر پھینک کر وقت ناپنے سے", "سورج کے شعلوں کو مڑتے دیکھ کر", "مدار میں گیندیں گرا کر"][0],
        "انتہائی حساس گھومتے ہوئے کروں (Gyroscopes) نے دکھایا کہ زمین محض خالی جگہ میں نہیں گھوم رہی بلکہ وہ اپنے گرد خلا کی چادر کو بھی موڑ رہی ہے، جس سے قطب نما ہلکا سا ترچھا ہو جاتا ہے۔"
    ),
    (
        "How did LIGO detect gravitational waves emitted by two colliding black holes 1.3 billion light-years away in 2015?",
        ["By detecting laser interference shifts smaller than 1/10,000th the diameter of a proton across 4-kilometer vacuum arms", "By recording sound waves with underwater hydrophones", "By tracking satellite altitude drops", "By measuring ocean temperature rises"],
        "By detecting laser interference shifts smaller than 1/10,000th the diameter of a proton across 4-kilometer vacuum arms",
        "Gravitational waves alter spatial metrics (Delta L / L ~ 10^-21). LIGO's Michelson interferometers detected this metric strain by measuring phase differences between orthogonally split laser beams.",
        "لیگو اور ثقلی لہریں (LIGO Gravitational Waves): سائنسدانوں نے سوا ارب نوری سال دور دو بلیک ہولز کے ٹکراؤ سے پیدا ہونے والی لہروں کو زمین پر کیسے محسوس کیا؟",
        ["4 کلومیٹر لمبی سرنگوں میں لیزر شعاعوں کی مدد سے پروٹون کے سائز کے دس ہزارویں حصے سے بھی چھوٹی لرزش کو ناپ کر", "سمندر کے اندر مائیکروفون لگا کر آواز سن کر", "سیٹلائٹ کی اونچائی گرنے کو دیکھ کر", "سمندر کا درجہ حرارت ناپ کر"],
        ["4 کلومیٹر لمبی سرنگوں میں لیزر شعاعوں کی مدد سے پروٹون کے سائز کے دس ہزارویں حصے سے بھی چھوٹی لرزش کو ناپ کر", "سمندر کے اندر مائیکروفون لگا کر آواز سن کر", "سیٹلائٹ کی اونچائی گرنے کو دیکھ کر", "سمندر کا درجہ حرارت ناپ کر"][0],
        "جب دو بلیک ہول ٹکرائے تو کائنات کے زمان و مکان میں ایسی لہریں اٹھیں جنہوں نے زمین پر موجود لیزر سرنگوں کو ایک بال سے بھی کھرب گنا کم کھینچا اور سکیڑا، جسے لیگو کے آلات نے ریکارڈ کر لیا۔"
    ),
    (
        "Why is the Cosmological Constant Problem considered the worst theoretical prediction in the history of physics?",
        ["Quantum field theory predicts a vacuum zero-point energy density that is roughly 120 orders of magnitude larger than observed reality", "The expansion rate exceeds the speed of light by infinity", "Galaxies collide backwards", "Dark energy turns stars green"],
        "Quantum field theory predicts a vacuum zero-point energy density that is roughly 120 orders of magnitude larger than observed reality",
        "Summing quantum vacuum zero-point energy up to the Planck scale yields rho_vac ~ 10^112 erg/cm^3, whereas astronomical observation measures rho_lambda ~ 10^-8 erg/cm^3, a discrepancy of 10^120.",
        "کاسمولوجیکل کانسٹنٹ کا معمہ (Cosmological Constant Problem): اسے فزکس کی تاریخ کی سب سے بدترین غلط ریاضیاتی پیش گوئی کیوں مانا جاتا ہے؟",
        ["کوانٹم فیلڈ تھیوری کے مطابق خلا کے خالی حصے کی انرجی کا حساب حقیقت میں دیکھی جانے والی کائناتی انرجی سے 120 گنا بڑا (10 کی پاور 120) نکلتا ہے", "کائنات کے پھیلنے کی رفتار روشنی سے لامحدود تیز ہے", "کہکشائیں الٹی ٹکراتی ہیں", "تاریک توانائی تاروں کو ہرا کر دیتی ہے"],
        ["کوانٹم فیلڈ تھیوری کے مطابق خلا کے خالی حصے کی انرجی کا حساب حقیقت میں دیکھی جانے والی کائناتی انرجی سے 120 گنا بڑا (10 کی پاور 120) نکلتا ہے", "کائنات کے پھیلنے کی رفتار روشنی سے لامحدود تیز ہے", "کہکشائیں الٹی ٹکراتی ہیں", "تاریک توانائی تاروں کو ہرا کر دیتی ہے"][0],
        "اگر کوانٹم فزکس کا حساب درست ہوتا تو ویکیوم کی اتنی زیادہ توانائی پوری کائنات کو پہلے ہی ملی سیکنڈ میں اڑا کر تباہ کر چکی ہوتی۔ سائنس اب تک نہیں سمجھ سکی کہ یہ حساب 10^120 گنا غلط کیوں ہے۔"
    ),
    (
        "How did Alan Guth's Cosmic Inflation theory resolve the 'Horizon Problem' of the Cosmic Microwave Background (CMB)?",
        ["A brief burst of exponential expansion stretched a tiny causally connected region in thermal equilibrium into the entire observable universe", "Photons traveled across the universe at infinite speeds", "Gravity was repelling particles uniformly", "The universe was filled with liquid helium"],
        "A brief burst of exponential expansion stretched a tiny causally connected region in thermal equilibrium into the entire observable universe",
        "Opposite sides of the universe have identical temperatures (2.725 K) yet are causally disconnected today. Cosmic inflation explains they shared thermal equilibrium before expanding by a factor of 10^26.",
        "کائناتی افراط کا نظریہ (Cosmic Inflation & Horizon Problem): یہ نظریہ کائنات کے دو مخالف اور اربوں نوری سال دور کناروں کے بالکل ایک جیسے درجہ حرارت کا معمہ کیسے حل کرتا ہے؟",
        ["بگ بینگ کے آغاز میں کائنات کے ایک انتہائی چھوٹے حصے نے روشنی سے بھی تیز رفتاری سے پھیل کر آج کی تمام نظر آنے والی کائنات کی شکل اختیار کی", "فوٹونز لامحدود رفتار سے سفر کرتے تھے", "کشش ثقل تمام چیزوں کو اچھال رہی تھی", "کائنات مائع ہیلیم سے بھری تھی"],
        ["بگ بینگ کے آغاز میں کائنات کے ایک انتہائی چھوٹے حصے نے روشنی سے بھی تیز رفتاری سے پھیل کر آج کی تمام نظر آنے والی کائنات کی شکل اختیار کی", "فوٹونز لامحدود رفتار سے سفر کرتے تھے", "کشش ثقل تمام چیزوں کو اچھال رہی تھی", "کائنات مائع ہیلیم سے بھری تھی"][0],
        "پھیلنے سے پہلے پوری کائنات ایک ننھے سے ذرے میں بند تھی جہاں تمام حصوں کا درجہ حرارت آپس میں مل کر برابر ہو چکا تھا۔ افراط کے اچانک دھماکے نے اس یکساں ماحول کو اربوں نوری سال تک پھیلا دیا۔"
    ),
    (
        "In the Baryon Asymmetry Problem, why is our universe composed almost entirely of matter rather than equal parts matter and antimatter?",
        ["Sakharov conditions: CP-violation, baryon number violation, and departure from thermal equilibrium favored a tiny excess of matter (1 in a billion)", "Antimatter has negative gravitational mass and fell away", "Antimatter evaporated through black holes", "Antimatter never existed"],
        "Sakharov conditions: CP-violation, baryon number violation, and departure from thermal equilibrium favored a tiny excess of matter (1 in a billion)",
        "During early baryogenesis, for every 1,000,000,000 antimatter particles annihilated with matter, 1,000,000,001 matter particles were formed, leaving behind the residual matter that forms our galaxies.",
        "مادے اور ضد مادے کی عدم مساوات (Baryon Asymmetry): اگر بگ بینگ میں مادہ اور اینٹی میٹر برابر بنے تھے تو آج کائنات میں صرف مادہ کیوں باقی ہے؟",
        ["سخاروف شرائط (Sakharov Conditions): ابتدائی کائنات میں طبعی قوانین کی معمولی عدم ہم آہنگی نے ہر ایک ارب اینٹی پارٹیکلز کے مقابلے میں مادے کا ایک اضافی ذرہ پیدا کر دیا", "اینٹی میٹر کشش ثقل سے دور اڑ گیا", "اینٹی میٹر بلیک ہول میں گر کر غائب ہو گیا", "اینٹی میٹر سرے سے کبھی بنا ہی نہیں تھا"],
        ["سخاروف شرائط (Sakharov Conditions): ابتدائی کائنات میں طبعی قوانین کی معمولی عدم ہم آہنگی نے ہر ایک ارب اینٹی پارٹیکلز کے مقابلے میں مادے کا ایک اضافی ذرہ پیدا کر دیا", "اینٹی میٹر کشش ثقل سے دور اڑ گیا", "اینٹی میٹر بلیک ہول میں گر کر غائب ہو گیا", "اینٹی میٹر سرے سے کبھی بنا ہی نہیں تھا"][0],
        "باقی سارا مادہ اور اینٹی میٹر ایک دوسرے کو فنا کر کے خالص روشنی بن گئے۔ مگر ایک ارب میں سے ایک ذرے کی اس معمولی سی اضافی برتری کی وجہ سے آج تمام ستارے، سیارے اور انسان موجود ہیں۔"
    ),
    (
        "Why is the Bullet Cluster (1E 0657-56) widely celebrated as the definitive empirical proof for the physical reality of Dark Matter?",
        ["Gravitational lensing reveals that the center of mass is separated from the hot X-ray emitting intergalactic gas after a cosmic collision", "Dark matter emits glowing green light", "Telescopes saw shadows of black dwarfs", "Neutrinos slowed down to zero"],
        "Gravitational lensing reveals that the center of mass is separated from the hot X-ray emitting intergalactic gas after a cosmic collision",
        "When two clusters collided, normal baryonic gas experienced electromagnetic drag and stalled in the middle, while collisionless dark matter passed through unimpeded, carrying the dominant gravitational mass.",
        "بلٹ کلسٹر اور تاریک مادہ (Bullet Cluster Dark Matter Proof): دو کہکشانی جھرمٹوں کے باہمی تصادم کو ڈارک میٹر کے وجود کا حتمی ثبوت کیوں مانا جاتا ہے؟",
        ["کشش ثقل کا اصل مرکز ٹکرانے والی گرم گیس کے بادلوں سے الگ ہو کر ان سے آگے نکل گیا، جس سے ثابت ہوا کہ نظر نہ آنے والا مادہ الگ موجود ہے", "ڈارک میٹر سے سبز روشنی خارج ہوتی ہے", "دوربینوں نے کالے ستاروں کے سائے دیکھے", "نیوٹرینوز رک کر ساکن ہو گئے"],
        ["کشش ثقل کا اصل مرکز ٹکرانے والی گرم گیس کے بادلوں سے الگ ہو کر ان سے آگے نکل گیا، جس سے ثابت ہوا کہ نظر نہ آنے والا مادہ الگ موجود ہے", "ڈارک میٹر سے سبز روشنی خارج ہوتی ہے", "دوربینوں نے کالے ستاروں کے سائے دیکھے", "نیوٹرینوز رک کر ساکن ہو گئے"][0],
        "ٹکراؤ کے دوران عام گیس ایک دوسرے سے رگڑ کھا کر درمیان میں پھنس گئی، جبکہ ڈارک میٹر بغیر کسی رگڑ کے ایک دوسرے کے اندر سے پار نکل گیا اور روشنی کو موڑنے کی طاقت اپنے ساتھ لے گیا۔"
    ),
    (
        "How did astronomers using Type Ia supernovae in 1998 conclude that the expansion of the universe is not slowing down, but actually accelerating?",
        ["Distant Type Ia supernovae were measurably dimmer and fainter than predicted for a decelerating universe, driven by Dark Energy", "Supernovae were moving toward Earth", "Cosmic dust made stars turn purple", "Supernovae had exploded twice"],
        "Distant Type Ia supernovae were measurably dimmer and fainter than predicted for a decelerating universe, driven by Dark Energy",
        "Perlmutter, Riess, and Schmidt measured standard candles (Type Ia supernovae). Their lower apparent luminosity at high redshifts z proved the universe has been accelerating for the last 5 billion years.",
        "سپر نووا اور تیز رفتار کائناتی پھیلاؤ (Accelerating Universe): 1998 میں سائنسدانوں نے ٹائپ 1 اے سپر نووا کے مشاہدے سے یہ کیسے ثابت کیا کہ کائنات کی رفتار سست ہونے کی بجائے تیز ہو رہی ہے؟",
        ["دور دراز کے سپر نووا توقع سے زیادہ مدہم پائے گئے، جس سے ثابت ہوا کہ وہ تاریک توانائی کے دباؤ کی وجہ سے کہیں زیادہ تیزی سے دور بھاگ رہے ہیں", "سپر نووا زمین کی طرف آ رہے تھے", "خلا کی دھول نے ستاروں کو جامنی کر دیا تھا", "سپر نووا دو دو بار پھٹ رہے تھے"],
        ["دور دراز کے سپر نووا توقع سے زیادہ مدہم پائے گئے، جس سے ثابت ہوا کہ وہ تاریک توانائی کے دباؤ کی وجہ سے کہیں زیادہ تیزی سے دور بھاگ رہے ہیں", "سپر نووا زمین کی طرف آ رہے تھے", "خلا کی دھول نے ستاروں کو جامنی کر دیا تھا", "سپر نووا دو دو بار پھٹ رہے تھے"][0],
        "سب کا خیال تھا کہ کشش ثقل پھیلاؤ کو آہستہ کرے گی۔ مگر جب یہ معیاری ستارے اتنے دور اور مدہم نکلے تو معلوم ہوا کہ کائنات میں 'تاریک توانائی' نامی ایک پراسرار قوت کہکشاؤں کو تیز رفتاری سے دھکیل رہی ہے۔"
    ),
    (
        "Why does a moon orbiting too close to its host planet disintegrate into a ring system of rocky debris (the Roche Limit)?",
        ["Tidal gravitational forces exerted by the host planet exceed the moon's own internal gravitational self-cohesion", "Atmospheric friction incinerates the moon", "Magnetic fields repulse the moon's iron core", "Solar wind shatters the crust"],
        "Tidal gravitational forces exerted by the host planet exceed the moon's own internal gravitational self-cohesion",
        "The differential gravitational force across the moon's diameter overcomes its self-gravitational binding energy: d = R_planet * (2 * rho_planet / rho_moon)^(1/3), tearing it into planetary rings.",
        "روش کی حد (Roche Limit): اگر کوئی چاند اپنے سیارے کے بہت زیادہ قریب آ جائے تو وہ ٹوٹ کر زحل کے چھلوں کی طرح کیوں بکھر جاتا ہے؟",
        ["سیارے کی کھینچنے والی مدوجزر کی غیر مساوی ثقلی قوتیں چاند کی اپنی اندرونی کشش ثقل اور مٹی کے باہمی بندھن کو توڑ دیتی ہیں", "ہوا کی رگڑ چاند کو جلا دیتی ہے", "مقناطیسی قوتیں لوہے کو اچھالتی ہیں", "سورج کی ہوائیں چاند کی سطح پھاڑ دیتی ہیں"],
        ["سیارے کی کھینچنے والی مدوجزر کی غیر مساوی ثقلی قوتیں چاند کی اپنی اندرونی کشش ثقل اور مٹی کے باہمی بندھن کو توڑ دیتی ہیں", "ہوا کی رگڑ چاند کو جلا دیتی ہے", "مقناطیسی قوتیں لوہے کو اچھالتی ہیں", "سورج کی ہوائیں چاند کی سطح پھاڑ دیتی ہیں"][0],
        "چاند کے قریب والے رخ پر سیارے کی کشش اتنی شدید ہو جاتی ہے اور دور والے رخ پر اتنی کم کہ پورا چاند کھنچ کر تسبیح کے دانوں کی طرح بکھر جاتا ہے اور سیارے کے گرد چھلا بن جاتا ہے۔"
    ),
    (
        "What quantum phenomenon prevents a white dwarf star from collapsing under its immense gravity up to 1.44 solar masses (the Chandrasekhar Limit)?",
        ["Electron degeneracy pressure caused by the Pauli Exclusion Principle", "Nuclear fusion of iron in the core", "Centrifugal spinning force", "Thermal photon pressure"],
        "Electron degeneracy pressure caused by the Pauli Exclusion Principle",
        "Electrons cannot occupy identical quantum states. Squeezing electrons generates quantum degeneracy pressure. Above 1.44 M_sun, electrons become ultra-relativistic and cannot resist gravitational collapse.",
        "چندر شیکھر کی حد (Chandrasekhar Limit): سورج سے 1.44 گنا بڑے سفید بونے ستارے (White Dwarf) کو اپنے ہی وزن تلے دبنے سے کون سی طاقت روکے رکھتی ہے؟",
        ["پاؤلی کے اصول کی بدولت پیدا ہونے والا الیکٹرانز کا انحطاطی دباؤ (Electron Degeneracy Pressure)", "مرکز میں لوہے کے فیوژن کا عمل", "تیز گھومنے سے پیدا ہونے والا مرکز گریز دباؤ", "روشنی کی حرارت کا دباؤ"],
        ["پاؤلی کے اصول کی بدولت پیدا ہونے والا الیکٹرانز کا انحطاطی دباؤ (Electron Degeneracy Pressure)", "مرکز میں لوہے کے فیوژن کا عمل", "تیز گھومنے سے پیدا ہونے والا مرکز گریز دباؤ", "روشنی کی حرارت کا دباؤ"][0],
        "کوانٹم فزکس کے مطابق دو الیکٹران ایک ہی حالت میں نہیں رہ سکتے۔ جب کشش ثقل انہیں دباتی ہے تو الیکٹرانز ایک زبردست کوانٹم دباؤ پیدا کرتے ہیں جو ستارے کو سکڑنے سے بچا لیتا ہے۔"
    ),
    (
        "What happens to a dying star whose mass exceeds the Tolman-Oppenheimer-Volkoff (TOV) limit of approximately 2.17 solar masses?",
        ["Neutron degeneracy pressure is overwhelmed, causing the core to collapse into a stellar-mass black hole", "It rebounds into an expanding red giant", "It cools into a solid iron planet", "It converts into pure gamma radiation"],
        "Neutron degeneracy pressure is overwhelmed, causing the core to collapse into a stellar-mass black hole",
        "While neutron stars are supported by neutron degeneracy pressure and strong nuclear repulsions, exceeding the TOV limit (~2.17 M_sun) leaves no known physical force to prevent collapse to a singularity.",
        "اوپن ہائیمر ووولکوف حد (TOV Limit): جب کسی مردہ نیوٹران ستارے کا وزن سورج سے 2.17 گنا سے زیادہ ہو جائے تو اس کا انجام کیا ہوتا ہے؟",
        ["نیوٹرانز کا باہمی دباؤ بھی جواب دے جاتا ہے اور ستارہ کشش ثقل کے ہاتھوں مکمل تباہ ہو کر ایک بلیک ہول بن جاتا ہے", "وہ پلٹ کر سرخ دیو ستارہ بن جاتا ہے", "وہ ٹھنڈا ہو کر لوہے کا سیارہ بن جاتا ہے", "وہ خالص گاما لہروں میں بدل جاتا ہے"],
        ["نیوٹرانز کا باہمی دباؤ بھی جواب دے جاتا ہے اور ستارہ کشش ثقل کے ہاتھوں مکمل تباہ ہو کر ایک بلیک ہول بن جاتا ہے", "وہ پلٹ کر سرخ دیو ستارہ بن جاتا ہے", "وہ ٹھنڈا ہو کر لوہے کا سیارہ بن جاتا ہے", "وہ خالص گاما لہروں میں بدل جاتا ہے"][0],
        "کائنات میں نیوٹرانز کا دباؤ آخری مادی رکاوٹ ہے۔ جب کشش ثقل اس حد کو بھی توڑ دے تو مادہ کسی حالت میں نہیں رک سکتا اور سیدھا ایک بلیک ہول کے سنگولیرٹی نقطے میں گر جاتا ہے۔"
    ),
    (
        "Why do spinning pulsars occasionally undergo sudden, violent 'glitches' where their rotational frequency abruptly speeds up?",
        ["Superfluid vortices in the neutron star's interior mantle unpin and transfer angular momentum to the solid crust", "Incoming asteroids crash into the magnetic poles", "The pulsar hits interstellar dust clouds", "Magnetic fields reverse their polarity"],
        "Superfluid vortices in the neutron star's interior mantle unpin and transfer angular momentum to the solid crust",
        "The interior superfluid crust hosts billions of quantized vortices pinned to nuclear lattices. When the crust slows due to radiation, stress builds until vortices unpin catastrophically, speeding up the crust.",
        "پلسار کا جھٹکا (Pulsar Glitch): تیزی سے گھومتے ہوئے نیوٹران ستارے کی گھومنے کی رفتار اچانک اور غیر متوقع طور پر ایک جھٹکے سے تیز کیوں ہو جاتی ہے؟",
        ["ستارے کے اندرونی مائع کے کوانٹم بھنور اپنی جگہ سے اکھڑ کر بیرونی ٹھوس پرت کو اچانک اضافی رفتار منتقل کر دیتے ہیں", "شہابیے مقناطیسی قطب پر آ کر گرتے ہیں", "پلسار دھول کے بادلوں سے ٹکراتا ہے", "مقناطیسی فیلڈ اپنے رخ الٹ دیتی ہے"],
        ["ستارے کے اندرونی مائع کے کوانٹم بھنور اپنی جگہ سے اکھڑ کر بیرونی ٹھوس پرت کو اچانک اضافی رفتار منتقل کر دیتے ہیں", "شہابیے مقناطیسی قطب پر آ کر گرتے ہیں", "پلسار دھول کے بادلوں سے ٹکراتا ہے", "مقناطیسی فیلڈ اپنے رخ الٹ دیتی ہے"][0],
        "نیوٹران ستارے کا اندرونی سپر فلوئڈ مائع باہر کے چھلکے سے تیز گھوم رہا ہوتا ہے۔ جب اندر کا کھچاؤ بڑھتا ہے تو کوانٹم بھنور باہر کے چھلکے کو ایک زوردار جھٹکا دے کر ستارے کی رفتار بڑھا دیتے ہیں۔"
    ),
    (
        "What happens when a 'starquake' fractures the ultra-dense iron crust of a Magnetar with a magnetic field of 10^11 Tesla?",
        ["It releases a catastrophic burst of gamma rays and X-rays that can disrupt Earth's upper ionosphere from tens of thousands of light-years away", "The magnetar explodes into dark energy", "The magnetar becomes invisible to radar", "It creates a new planetary solar system"],
        "It releases a catastrophic burst of gamma rays and X-rays that can disrupt Earth's upper ionosphere from tens of thousands of light-years away",
        "A 1-millimeter crack in a magnetar's crust twists magnetic field lines, releasing 10^39 joules of energy. In 2004, a flare from SGR 1806-20 (50,000 light-years away) ionized Earth's atmosphere.",
        "میگنیٹار کا ستارہ زلزلہ (Magnetar Starquake): جب کھربوں ٹیسلا طاقتور مقناطیس رکھنے والے ستارے کی پرت میں محض 1 ملی میٹر کا زلزلہ آتا ہے تو کیا قیامت برپا ہوتی ہے؟",
        ["گاما اور ایکس رے لہروں کا ایسا خوفناک طوفان نکلتا ہے جو پچاس ہزار نوری سال دور زمین کے فضائی کرۂ کو بھی ہلا کر رکھ دیتا ہے", "میگنیٹار تاریک توانائی میں پھٹ جاتا ہے", "ستارہ ریڈار پر نظر آنا بند ہو جاتا ہے", "ایک نیا نظام شمسی بن جاتا ہے"],
        ["گاما اور ایکس رے لہروں کا ایسا خوفناک طوفان نکلتا ہے جو پچاس ہزار نوری سال دور زمین کے فضائی کرۂ کو بھی ہلا کر رکھ دیتا ہے", "میگنیٹار تاریک توانائی میں پھٹ جاتا ہے", "ستارہ ریڈار پر نظر آنا بند ہو جاتا ہے", "ایک نیا نظام شمسی بن جاتا ہے"][0],
        "اس کے مقناطیس کا کھچاؤ اتنا بھیانک ہوتا ہے کہ جب پرت ٹوٹتی ہے تو محض دسویں حصے سیکنڈ میں سورج کی ڈھائی لاکھ سال کی کل انرجی کے برابر گاما شعاعیں کائنات میں بکھر جاتی ہیں۔"
    ),
    (
        "Why do relativistic astrophysical jets fired from supermassive black holes appear to travel across the sky at faster-than-light speeds (Apparent Superluminal Motion)?",
        ["An optical geometry illusion caused by the jet moving toward Earth at near light speed, chasing its own emitted photons", "Tachyon particles exceed the speed of light in deep vacuum", "Gravity slingshots matter past c", "Galaxies pull space with wormholes"],
        "An optical geometry illusion caused by the jet moving toward Earth at near light speed, chasing its own emitted photons",
        "If a jet travels at angle theta near 0 to our line of sight at v ~ c, the time difference between received pulses Delta t_obs = Delta t * (1 - beta * cos theta) compresses dramatically, making v_app appear > c.",
        "روشنی سے تیز حرکت کا وہم (Superluminal Motion): بلیک ہول سے نکلنے والے گیس کے فوارے دور سے دیکھنے پر روشنی کی رفتار سے بھی تیز بھاگتے ہوئے کیوں محسوس ہوتے ہیں؟",
        ["ایک بصری دھوکہ، کیونکہ وہ فوارہ تقریباً روشنی کی رفتار سے سیدھا زمین کی طرف آ رہا ہوتا ہے اور اپنی ہی چھوڑی ہوئی روشنی کے پیچھے پہنچتا ہے", "ٹیکیون ذرات خلا میں واقعی روشنی سے تیز ہیں", "کشش ثقل نے مادے کو تیز کر دیا", "کہکشائیں خلا کو موڑ رہی ہیں"],
        ["ایک بصری دھوکہ، کیونکہ وہ فوارہ تقریباً روشنی کی رفتار سے سیدھا زمین کی طرف آ رہا ہوتا ہے اور اپنی ہی چھوڑی ہوئی روشنی کے پیچھے پہنچتا ہے", "ٹیکیون ذرات خلا میں واقعی روشنی سے تیز ہیں", "کشش ثقل نے مادے کو تیز کر دیا", "کہکشائیں خلا کو موڑ رہی ہیں"][0],
        "فوارہ روشنی کے بالکل تعاقب میں سفر کرتا ہے۔ اس لیے اس کے اگلے اور پچھلے سگنلز ہمارے پاس بہت ہی کم وقفے میں پہنچتے ہیں، جس سے ریاضی کا زاویہ دیکھنے والے کو لگتا ہے کہ رفتار روشنی سے پانچ گنا تیز ہے۔"
    ),
    (
        "Why does relativistic beaming make an astrophysical jet pointing directly toward Earth look up to 1,000 times brighter than the identical jet pointing away?",
        ["Lorentz transformations focus photon emission into a tight forward-facing cone and blue-shift the frequency (Doppler boosting)", "The approaching jet burns clean hydrogen", "The counter-jet enters dark nebulae", "Gravity magnifies the approaching cone"],
        "Lorentz transformations focus photon emission into a tight forward-facing cone and blue-shift the frequency (Doppler boosting)",
        "Due to relativistic aberration and Doppler shift, the observed flux density scales as S_obs = S_0 * delta^(3 + alpha), boosting radiation toward the observer while dimming the receding jet.",
        "ڈوپلر بوسٹنگ اور جیٹ کی چمک (Relativistic Beaming): ہماری طرف رخ کر کے نکلنے والا گیس کا فوارہ الٹے رخ جانے والے فوارے سے ہزار گنا زیادہ روشن کیوں نظر آتا ہے؟",
        ["اضافیت کے اصول کے تحت روشنی کی شعاعیں سامنے کی طرف ایک تنگ مخروطی کون (Cone) میں مرتکز ہو کر فریکوئنسی میں بے تحاشا اضافہ کر لیتی ہیں", "سامنے والا جیٹ خالص ہائیڈروجن جلاتا ہے", "پیچھے والا جیٹ تاریک بادلوں میں چھپ جاتا ہے", "کشش ثقل سامنے والے کون کو بڑا کرتی ہے"],
        ["اضافیت کے اصول کے تحت روشنی کی شعاعیں سامنے کی طرف ایک تنگ مخروطی کون (Cone) میں مرتکز ہو کر فریکوئنسی میں بے تحاشا اضافہ کر لیتی ہیں", "سامنے والا جیٹ خالص ہائیڈروجن جلاتا ہے", "پیچھے والا جیٹ تاریک بادلوں میں چھپ جاتا ہے", "کشش ثقل سامنے والے کون کو بڑا کرتی ہے"][0],
        "جب مادہ روشنی کے قریب دوڑتا ہے تو وہ اپنی روشنی ہر طرف پھیلانے کی بجائے آگے کی طرف ایک تیز سرچ لائٹ کی طرح پھینکتا ہے۔ اسی لیے سامنے آنے والا جیٹ اندھا کر دینے والا روشن لگتا ہے۔"
    ),
    (
        "Why do subatomic muons created by cosmic rays in the upper atmosphere reach ground detectors in vast numbers despite a rest-frame lifetime of only 2.2 microseconds?",
        ["Special Relativity: time dilation dilates the muon's internal clock while length contraction shortens the atmospheric distance from the muon's frame", "Muons glide down along magnetic field lines", "Cosmic rays blow muons down like wind", "Atmospheric nitrogen preserves muons"],
        "Special Relativity: time dilation dilates the muon's internal clock while length contraction shortens the atmospheric distance from the muon's frame",
        "At v = 0.9997c, gamma ~ 40. From Earth's frame, the muon lives 40 times longer (~88 microseconds); from the muon's frame, the 10-kilometer atmosphere is compressed to 250 meters.",
        "میوآن کا اضافیتی معمہ (Relativistic Muon Lifespan): محض 2.2 مائیکرو سیکنڈ عمر رکھنے والے میوآن ذرات فضا کے اوپری حصے سے زمین کے نیچے تک ہزاروں کی تعداد میں کیسے پہنچ جاتے ہیں؟",
        ["خصوصی اضافیت کے تحت تیز رفتار کی وجہ سے زمین سے دیکھنے پر ان کا وقت سست ہو جاتا ہے اور ان کے اپنے نقطہ نظر سے فضا کا فاصلہ سکڑ جاتا ہے", "میوآن مقناطیسی لکیروں پر پھسلتے ہیں", "کائناتی شعاعیں ہوا کی طرح انہیں دھکیلتی ہیں", "نائٹروجن گیس میوآن کو محفوظ رکھتی ہے"],
        ["خصوصی اضافیت کے تحت تیز رفتار کی وجہ سے زمین سے دیکھنے پر ان کا وقت سست ہو جاتا ہے اور ان کے اپنے نقطہ نظر سے فضا کا فاصلہ سکڑ جاتا ہے", "میوآن مقناطیسی لکیروں پر پھسلتے ہیں", "کائناتی شعاعیں ہوا کی طرح انہیں دھکیلتی ہیں", "نائٹروجن گیس میوآن کو محفوظ رکھتی ہے"][0],
        "عام رفتار پر وہ محض چند سو میٹر چل کر مر جاتے، مگر 99.9 فیصد روشنی کی رفتار کی بدولت زمین والوں کے لیے ان کی زندگی 40 گنا لمبی ہو جاتی ہے، جس سے وہ باآسانی زمین تک پہنچ جاتے ہیں۔"
    ),
    (
        "In the Twin Paradox of Special Relativity, why is the traveling astronaut twin younger than the stay-at-home Earth twin upon returning?",
        ["The traveling twin experienced physical acceleration and turnaround, breaking inertial frame symmetry and changing reference frames", "Spaceship food contains antioxidants", "Space travel cools human biological cells", "Earth spins faster around the Sun"],
        "The traveling twin experienced physical acceleration and turnaround, breaking inertial frame symmetry and changing reference frames",
        "The traveling twin switches inertial frames when decelerating and accelerating for the return journey. The asymmetry of the spacetime worldline dictates a shorter proper time integral.",
        "جڑواں بھائیوں کا معمہ (Twin Paradox): خلا کا سفر کر کے لوٹنے والا خلاباز بھائی زمین پر رہنے والے اپنے جڑواں بھائی سے عمر میں کافی چھوٹا کیوں نکلتا ہے؟",
        ["خلاباز بھائی نے رفتار بڑھانے اور واپسی کا موڑ کاٹنے کے لیے حقیقی اسراع (Acceleration) برداشت کیا، جس سے فریموں کا توازن ٹوٹ گیا", "خلائی جہاز کے کھانے میں وٹامنز ہوتے ہیں", "خلا کی سردی خلیات کو جوان رکھتی ہے", "زمین سورج کے گرد تیز گھومتی ہے"],
        ["خلاباز بھائی نے رفتار بڑھانے اور واپسی کا موڑ کاٹنے کے لیے حقیقی اسراع (Acceleration) برداشت کیا، جس سے فریموں کا توازن ٹوٹ گیا", "خلائی جہاز کے کھانے میں وٹامنز ہوتے ہیں", "خلا کی سردی خلیات کو جوان رکھتی ہے", "زمین سورج کے گرد تیز گھومتی ہے"][0],
        "زمین کا بھائی ساکن فریم میں رہا، جبکہ خلا کے بھائی نے جہاز کو بریکیں لگا کر واپس موڑا۔ اضافیت میں اس موڑ اور رفتار کی تبدیلی کی وجہ سے خلاباز کی گھڑی کا کل گزرا ہوا وقت کم رہ گیا۔"
    ),
    (
        "In the Ladder Paradox (Barn-Pole Paradox), can a 20-meter relativistic ladder moving near the speed of light fit completely inside a 10-meter barn with both doors closed simultaneously?",
        ["Yes in the barn's frame due to Lorentz contraction, but no in the ladder's frame where door closings are not simultaneous", "No, the ladder explodes upon touching air", "Yes, doors trap light inside mirrors", "No, wood does not contract"],
        "Yes in the barn's frame due to Lorentz contraction, but no in the ladder's frame where door closings are not simultaneous",
        "Relativity of simultaneity: to the barn, the ladder contracts to 8 meters and both doors close simultaneously. To the ladder, the doors close at different moments in time.",
        "سیڑھی اور گودام کا معمہ (Ladder Paradox): کیا روشنی کی رفتار سے دوڑتی ہوئی 20 میٹر کی لمبی سیڑھی 10 میٹر کے چھوٹے گودام میں دونوں دروازے بیک وقت بند کر کے سما سکتی ہے؟",
        ["گودام والے کے لحاظ سے ہاں، کیونکہ سیڑھی سکڑ جاتی ہے؛ مگر سیڑھی والے کے لحاظ سے دونوں دروازے بیک وقت بند نہیں ہوتے", "نہیں، سیڑھی ہوا چھوتے ہی پھٹ جاتی ہے", "ہاں، دروازے روشنی قید کر لیتے ہیں", "نہیں، لکڑی کبھی نہیں سکڑتی"],
        ["گودام والے کے لحاظ سے ہاں، کیونکہ سیڑھی سکڑ جاتی ہے؛ مگر سیڑھی والے کے لحاظ سے دونوں دروازے بیک وقت بند نہیں ہوتے", "نہیں، سیڑھی ہوا چھوتے ہی پھٹ جاتی ہے", "ہاں، دروازے روشنی قید کر لیتے ہیں", "نہیں، لکڑی کبھی نہیں سکڑتی"][0],
        "بیک وقت کا ہونا کوئی مطلق سچ نہیں ہے۔ گودام کے فریم میں سیڑھی سکڑ کر اندر بند ہو جاتی ہے، جبکہ سیڑھی والے کے لیے آگے کا دروازہ کھل جانے کے بعد پیچھے کا دروازہ بند ہوتا ہے۔"
    ),
    (
        "In Bell's Spaceship Paradox, two identical spaceships accelerate identically with a fragile thread stretched between them. Why does the thread snap?",
        ["The distance between the ships increases in their instantaneous co-moving rest frames, while the thread Lorentz contracts", "Exhaust gas melts the thread fibers", "Micro-meteorites sever the thread", "Gravity pulls the ships apart"],
        "The distance between the ships increases in their instantaneous co-moving rest frames, while the thread Lorentz contracts",
        "In the launch frame, the distance remains constant, but the thread tries to Lorentz-contract. In the ships' frame, relativistic simultaneity causes the lead ship to accelerate earlier, stretching and breaking the thread.",
        "بیل کے خلائی جہازوں کا معمہ (Bell's Spaceship Paradox): ایک ہی رفتار سے تیز ہوتے ہوئے دو جہازوں کے درمیان بندھا ہوا نازک دھاگہ اچانک کیوں ٹوٹ جاتا ہے؟",
        ["جہازوں کے اپنے متحرک فریم میں ان کے درمیان کا فاصلہ بڑھ جاتا ہے جبکہ دھاگہ اضافیتی کھچاؤ کی وجہ سے لمبائی برقرار نہیں رکھ پاتا", "انجن کا دھواں دھاگے کو پگھلا دیتا ہے", "خردبینی شہابیے دھاگے کو کاٹ دیتے ہیں", "کشش ثقل جہازوں کو دور دھکیلتی ہے"],
        ["جہازوں کے اپنے متحرک فریم میں ان کے درمیان کا فاصلہ بڑھ جاتا ہے جبکہ دھاگہ اضافیتی کھچاؤ کی وجہ سے لمبائی برقرار نہیں رکھ پاتا", "انجن کا دھواں دھاگے کو پگھلا دیتا ہے", "خردبینی شہابیے دھاگے کو کاٹ دیتے ہیں", "کشش ثقل جہازوں کو دور دھکیلتی ہے"][0],
        "اگرچہ لانچ پیڈ سے دونوں جہاز ایک ہی رفتار سے بڑھتے نظر آتے ہیں، مگر جہازوں کے اپنے اندرونی وقت کے مطابق آگے والا جہاز پیچھے والے سے پہلے تیز ہو رہا ہوتا ہے، جس سے دھاگہ کھنچ کر ٹوٹ جاتا ہے۔"
    ),
    (
        "What paradox did Paul Ehrenfest discover regarding the spatial geometry of a rapidly rotating rigid cylinder in Special Relativity?",
        ["The outer circumference Lorentz-contracts while the radial radius remains uncontracted, proving rigid bodies cannot exist in relativity", "The cylinder turns into a liquid sphere", "Friction with air produces antimatter", "The center evaporates into steam"],
        "The outer circumference Lorentz-contracts while the radial radius remains uncontracted, proving rigid bodies cannot exist in relativity",
        "Because tangential motion causes length contraction along the circumference (2*pi*r < standard) while radius r is orthogonal to motion and unaffected, space geometry becomes non-Euclidean.",
        "احرن فیسٹ کا معمہ (Ehrenfest Paradox): تیزی سے گھومتے ہوئے ٹھوس سلنڈر کے دائرے کی جیومیٹری اضافیت کے تحت غیر متوقع کیوں ہو جاتی ہے؟",
        ["گھومنے کے رخ پر اس کا بیرونی گھیراؤ (Circumference) سکڑ جاتا ہے جبکہ اس کا رداس (Radius) نہیں سکڑتا، جس سے خلا غیر اقلیدسی بن جاتی ہے", "سلنڈر مائع گیند بن جاتا ہے", "ہوا کی رگڑ اینٹی میٹر بناتی ہے", "مرکز بھاپ بن کر اڑ جاتا ہے"],
        ["گھومنے کے رخ پر اس کا بیرونی گھیراؤ (Circumference) سکڑ جاتا ہے جبکہ اس کا رداس (Radius) نہیں سکڑتا، جس سے خلا غیر اقلیدسی بن جاتی ہے", "سلنڈر مائع گیند بن جاتا ہے", "ہوا کی رگڑ اینٹی میٹر بناتی ہے", "مرکز بھاپ بن کر اڑ جاتا ہے"][0],
        "اگر گھیراؤ سکڑ جائے اور رداس نہ سکڑے تو پائی (Pi) کی قیمت بدل جاتی ہے۔ اضافیت نے ثابت کیا کہ دنیا میں کوئی چیز مکمل طور پر 100 فیصد لچک کے بغیر 'ٹھوس' نہیں ہو سکتی۔"
    ),
    (
        "According to the Unruh Effect, what does an observer accelerating through an absolute quantum vacuum perceive instead of empty cold space?",
        ["A warm thermal bath of blackbody radiation with temperature proportional to their physical acceleration", "Pitch-black frozen ice particles", "Supersonic shock waves", "Gravitational blue flashes"],
        "A warm thermal bath of blackbody radiation with temperature proportional to their physical acceleration",
        "William Unruh showed that an accelerating detector experiences a Rindler event horizon. Vacuum fluctuations appear as real thermal particles at temperature T = hbar * a / (2 * pi * c * k_B).",
        "انرو اثر (Unruh Effect): مکمل طور پر خالی اور سرد کوانٹم خلا میں سے جب ایک مشاہدہ کار شدید تیزی (Acceleration) کے ساتھ گزرتا ہے تو اسے کیا محسوس ہوتا ہے؟",
        ["ایک گرم حرارتی تابکاری کا حمام جس کا درجہ حرارت اس کے تیز ہونے کی شرح کے براہ راست تناسب میں ہوتا ہے", "برف کے ٹھنڈے ذرات", "آواز سے تیز جھٹکے", "نیلی ثقلی چمکیں"],
        ["ایک گرم حرارتی تابکاری کا حمام جس کا درجہ حرارت اس کے تیز ہونے کی شرح کے براہ راست تناسب میں ہوتا ہے", "برف کے ٹھنڈے ذرات", "آواز سے تیز جھٹکے", "نیلی ثقلی چمکیں"][0],
        "جو جگہ ساکن کھڑے انسان کے لیے مکمل ٹھنڈی اور خالی ہے، تیز رفتار سے دوڑنے والے کے لیے وہی خلا حقیقی گرم پارٹیکلز کی گرم بھٹی بن جاتی ہے، کیونکہ خلا کی کیفیت مشاہدہ کار کی حرکت پر منحصر ہے۔"
    ),
    (
        "What fundamental principle did Albert Einstein declare as 'the happiest thought of my life' (the Equivalence Principle)?",
        ["An observer falling freely in a gravitational field feels zero weight, making gravitation locally indistinguishable from uniform acceleration", "E = mc^2 explains atomic bombs", "Light consists of wave packets", "Time travel into the past is impossible"],
        "An observer falling freely in a gravitational field feels zero weight, making gravitation locally indistinguishable from uniform acceleration",
        "Inside a closed box, no local experiment can distinguish between standing on Earth's surface and being accelerated at 9.8 m/s^2 through empty space, unifying gravity with curved spacetime geometry.",
        "آئن سٹائن کا اصول مساوات (Equivalence Principle): البرٹ آئن سٹائن نے اپنے کس خیال کو 'میری زندگی کا سب سے خوش کن خیال' قرار دیا تھا؟",
        ["آزادانہ نیچے گرتے ہوئے انسان کو اپنا وزن صفر محسوس ہوتا ہے، جس سے ثابت ہوا کہ کشش ثقل اور اسراع (Acceleration) مقامی طور پر بالکل ایک ہی چیز ہیں", "توانائی اور مادے کا برابر ہونا", "روشنی کا لہروں پر مشتمل ہونا", "ماضی کا سفر ناممکن ہونا"],
        ["آزادانہ نیچے گرتے ہوئے انسان کو اپنا وزن صفر محسوس ہوتا ہے، جس سے ثابت ہوا کہ کشش ثقل اور اسراع (Acceleration) مقامی طور پر بالکل ایک ہی چیز ہیں", "توانائی اور مادے کا برابر ہونا", "روشنی کا لہروں پر مشتمل ہونا", "ماضی کا سفر ناممکن ہونا"][0],
        "ایک بند لفٹ میں کھڑا انسان کبھی یہ نہیں بتا سکتا کہ وہ زمین کی کشش ثقل پر کھڑا ہے یا خلا میں 9.8 کی رفتار سے اوپر کھینچا جا رہا ہے۔ اسی خوبصورت خیال نے جنرل ریلیٹیویٹی کی بنیاد رکھی۔"
    ),
    (
        "Why does a radar signal bouncing off Venus take a few hundred microseconds longer to return when passing close to the Sun's surface (the Shapiro Delay)?",
        ["The Sun's immense mass curves and stretches spacetime, increasing the effective geometric path length of the light signal", "Solar wind blows the radar beam backward", "Sunspots absorb radio wavelengths", "Venus slows down in summer"],
        "The Sun's immense mass curves and stretches spacetime, increasing the effective geometric path length of the light signal",
        "Irwin Shapiro proposed the fourth test of General Relativity: propagating photons through curved spacetime geometry near a mass introduces a logarithmic coordinate time delay.",
        "شاپیرو ٹائم تاخیر (Shapiro Delay): زہرہ سیارے پر پھینکا گیا ریڈار سگنل جب سورج کے کنارے سے چھو کر گزرتا ہے تو اسے واپس لوٹنے میں معمول سے زیادہ وقت کیوں لگتا ہے؟",
        ["سورج کی زبردست کشش ثقل اپنے ارد گرد زمان و مکان کو موڑ اور کھینچ دیتی ہے، جس سے روشنی کے سفر کا حقیقی فاصلہ بڑھ جاتا ہے", "سورج کی ہوائیں ریڈار کو پیچھے دھکیلتی ہیں", "سورج کے دھبے سگنل جذب کرتے ہیں", "زہرہ سیارہ گرمیوں میں سست ہو جاتا ہے"],
        ["سورج کی زبردست کشش ثقل اپنے ارد گرد زمان و مکان کو موڑ اور کھینچ دیتی ہے، جس سے روشنی کے سفر کا حقیقی فاصلہ بڑھ جاتا ہے", "سورج کی ہوائیں ریڈار کو پیچھے دھکیلتی ہیں", "سورج کے دھبے سگنل جذب کرتے ہیں", "زہرہ سیارہ گرمیوں میں سست ہو جاتا ہے"][0],
        "روشنی کی رفتار کم نہیں ہوتی بلکہ خلا خود اتنی پھیل اور مڑ جاتی ہے کہ روشنی کو ایک گہری وادی کے اندر سے گھوم کر گزرنا پڑتا ہے، جس سے سگنل کے سفر میں تاخیر ہو جاتی ہے۔"
    ),
    (
        "What upper mathematical limit on physical information density is defined by the Bekenstein Bound?",
        ["The maximum amount of entropy or information that can be contained within a finite region of space with finite energy", "The maximum hard drive space sold in retail", "The maximum number of electrons in copper", "The maximum speed of sound in steel"],
        "The maximum amount of entropy or information that can be contained within a finite region of space with finite energy",
        "Jacob Bekenstein derived S <= 2 * pi * k * R * E / (hbar * c). Exceeding this bound would allow one to violate the Second Law of Thermodynamics by dropping information into a black hole.",
        "بیکن سٹائن کی حد (Bekenstein Bound): یہ قانون کسی بھی محدود جگہ کے اندر معلومات (Information) ذخیرہ کرنے کی کس حتمی حد کو ظاہر کرتا ہے؟",
        ["ایک مخصوص جگہ اور توانائی کے اندر معلومات اور اینٹروپی کی وہ آخری زیادہ سے زیادہ مقدار جس سے زیادہ معلومات قید کرنا ناممکن ہے", "دکانوں میں ملنے والی ہارڈ ڈرائیو کی حد", "تانبے کے اندر الیکٹرانز کی کل گنتی", "فولاد میں آواز کی رفتار کی حد"],
        ["ایک مخصوص جگہ اور توانائی کے اندر معلومات اور اینٹروپی کی وہ آخری زیادہ سے زیادہ مقدار جس سے زیادہ معلومات قید کرنا ناممکن ہے", "دکانوں میں ملنے والی ہارڈ ڈرائیو کی حد", "تانبے کے اندر الیکٹرانز کی کل گنتی", "فولاد میں آواز کی رفتار کی حد"][0],
        "اگر آپ کسی کمرے یا ایٹم میں اس حد سے زیادہ ڈیٹا بھرنے کی کوشش کریں گے تو اتنی زیادہ توانائی جمع ہو جائے گی کہ وہ جگہ مڑ کر خود ایک بلیک ہول بن جائے گی۔"
    ),
    (
        "Why can a particle undergoing quantum tunneling through a barrier appear to cross the barrier instantly at faster-than-light speed (the Hartman Effect)?",
        ["The group delay becomes independent of barrier thickness for wide barriers, causing the wave peak to exit prematurely via wave reshaping", "The particle enters hyperspace", "The barrier conducts electricity instantly", "Sensors miscount photon arrivals"],
        "The group delay becomes independent of barrier thickness for wide barriers, causing the wave peak to exit prematurely via wave reshaping",
        "Thomas Hartman showed in 1962 that tunneling transit time saturates as thickness increases. The emerging packet is not traveling superluminally, but is an attenuated reshaped portion of the leading edge.",
        "ہارٹ مین اثر اور فوری ٹنلنگ (Hartman Effect): کوانٹم سرنگ سے گزرنے والا ذرہ موٹی رکاوٹ کو پلک جھپکنے میں اور بظاہر روشنی سے تیز پار کرتا ہوا کیوں لگتا ہے؟",
        ["سرنگ پار کرنے کا وقت رکاوٹ کی موٹائی سے آزاد ہو جاتا ہے کیونکہ لہر کا اگلا کٹاؤ والا سرا دوسری طرف ابھر آتا ہے", "ذرہ ہائپر اسپیس میں کود جاتا ہے", "رکاوٹ فوری بجلی پہنچاتی ہے", "سینسر فوٹونز غلط گنتے ہیں"],
        ["سرنگ پار کرنے کا وقت رکاوٹ کی موٹائی سے آزاد ہو جاتا ہے کیونکہ لہر کا اگلا کٹاؤ والا سرا دوسری طرف ابھر آتا ہے", "ذرہ ہائپر اسپیس میں کود جاتا ہے", "رکاوٹ فوری بجلی پہنچاتی ہے", "سینسر فوٹونز غلط گنتے ہیں"][0],
        "یہ سچی سپرلومینل رفتار نہیں ہے۔ چونکہ کوانٹم لہر کا اگلا سرا پہلے ہی دیوار میں پھیلا ہوتا ہے، تو صرف وہ اگلا کٹا ہوا حصہ دوسری طرف بچ کر نکلتا ہے جس سے دیکھنے والے کو لگتا ہے کہ وہ فوری پہنچ گیا۔"
    ),
    (
        "Why does an electron fired between two parallel non-reflective plates experience altered spontaneous emission rates (the Purcell Effect)?",
        ["Modifying the local electromagnetic density of states around an atom directly accelerates or suppresses its photon emission rate", "The plates heat the electron", "Plates block cosmic rays", "The electron loses its spin"],
        "Modifying the local electromagnetic density of states around an atom directly accelerates or suppresses its photon emission rate",
        "Edward Purcell discovered that spontaneous emission is not an intrinsic atomic property, but depends on atom-cavity coupling: F_p = 3/(4*pi^2) * (lambda/n)^3 * (Q/V).",
        "پرسل اثر (Purcell Effect): ایٹم کے دونوں طرف آئینے رکھنے سے اس کے روشنی کا فوٹون خارج کرنے کی قدرتی رفتار کو تیز یا سست کیسے کیا جا سکتا ہے؟",
        ["ایٹم کے ارد گرد کوانٹم الیکٹرو میگنیٹک حالتوں کی گنجائش بدل دینے سے فوٹون کے اخراج کی رفتار براہ راست تبدیل ہو جاتی ہے", "پلیٹیں الیکٹران کو گرم کرتی ہیں", "پلیٹیں کائناتی شعاعیں روکتی ہیں", "الیکٹران اپنا گھماؤ کھو دیتا ہے"],
        ["ایٹم کے ارد گرد کوانٹم الیکٹرو میگنیٹک حالتوں کی گنجائش بدل دینے سے فوٹون کے اخراج کی رفتار براہ راست تبدیل ہو جاتی ہے", "پلیٹیں الیکٹران کو گرم کرتی ہیں", "پلیٹیں کائناتی شعاعیں روکتی ہیں", "الیکٹران اپنا گھماؤ کھو دیتا ہے"][0],
        "روشنی کا اخراج ایٹم کی اکیلی صفت نہیں بلکہ ماحول کے ساتھ اس کے ملاپ پر منحصر ہے۔ اگر خلا میں لہر کے پھیلنے کی جگہ نہ ہو تو ایٹم روشنی خارج ہی نہیں کر سکتا۔"
    ),
    (
        "How can a single photon split by a half-silvered mirror take both paths simultaneously, yet be detected at only a single localized pixel on a CCD camera?",
        ["Wave-particle duality: the photon propagates as a non-local probability amplitude wave, but measurement collapses it into a localized particle", "The mirror creates a duplicate twin photon", "The camera pixel stores sound energy", "The laser turns off automatically"],
        "Wave-particle duality: the photon propagates as a non-local probability amplitude wave, but measurement collapses it into a localized particle",
        "Schrödinger's equation evolves the spatial wave packet continuously across both paths. The Born rule dictates that irreversible interaction with a localized detector collapses the packet to a point.",
        "کوانٹم موج و ذرہ دوئی (Wave-Particle Localization): ایک فوٹون شیشے سے گزر کر بیک وقت دو راستوں پر کیسے چلتا ہے جبکہ کیمرے کی اسکرین پر صرف ایک ہی نقطے پر ریکارڈ ہوتا ہے؟",
        ["فوٹون راستے میں کوانٹم امکانی لہر کی طرح سفر کرتا ہے مگر کیمرے کے ایٹم سے ٹکراتے ہی ویو فنکشن سمٹ کر ایک نقطے کا ذرہ بن جاتا ہے", "شیشہ دوسرا جڑواں فوٹون بنا دیتا ہے", "کیمرہ آواز کی انرجی محفوظ کرتا ہے", "لیزر خود بخود بند ہو جاتی ہے"],
        ["فوٹون راستے میں کوانٹم امکانی لہر کی طرح سفر کرتا ہے مگر کیمرے کے ایٹم سے ٹکراتے ہی ویو فنکشن سمٹ کر ایک نقطے کا ذرہ بن جاتا ہے", "شیشہ دوسرا جڑواں فوٹون بنا دیتا ہے", "کیمرہ آواز کی انرجی محفوظ کرتا ہے", "لیزر خود بخود بند ہو جاتی ہے"][0],
        "جب تک کوئی مداخلت نہ ہو، فوٹون تمام راستوں پر لہر کی طرح بہتا ہے۔ مگر جب وہ سنسر کے کسی ایک ایٹم کو اپنی انرجی منتقل کرتا ہے تو وہ فوراً سمٹ کر ایک ٹھوس ذرے کا روپ لے لیتا ہے۔"
    ),
    (
        "Why does an ice skater spin dramatically faster when pulling their extended arms tightly inward toward their chest?",
        ["Conservation of Angular Momentum: reducing the moment of inertia requires the rotational velocity to increase proportionally", "Friction with ice drops to zero", "Arm muscles generate electrical current", "Air pressure pushes the skater"],
        "Conservation of Angular Momentum: reducing the moment of inertia requires the rotational velocity to increase proportionally",
        "Angular momentum L = I * omega is conserved in the absence of external torque. Pulling arms inward decreases moment of inertia I = sum(m*r^2), forcing spin velocity omega to rise.",
        "گھومنے کی رفتار اور کونیائی مومنٹم (Conservation of Angular Momentum): برف پر اسکیٹنگ کرنے والی کھلاڑی جب اپنے پھیلے ہوئے بازو سمیٹتی ہے تو اس کے گھومنے کی رفتار اچانک اتنی تیز کیوں ہو جاتی ہے؟",
        ["کونیائی مومنٹم کے بقا کے قانون کے تحت جسم کا انرشا کم ہونے سے گھومنے کی رفتار خود بخود اتنے ہی تناسب سے بڑھ جاتی ہے", "برف کی رگڑ صفر ہو جاتی ہے", "بازو کے پٹھے کرنٹ بناتے ہیں", "ہوا کا دباؤ کھلاڑی کو دھکیلتا ہے"],
        ["کونیائی مومنٹم کے بقا کے قانون کے تحت جسم کا انرشا کم ہونے سے گھومنے کی رفتار خود بخود اتنے ہی تناسب سے بڑھ جاتی ہے", "برف کی رگڑ صفر ہو جاتی ہے", "بازو کے پٹھے کرنٹ بناتے ہیں", "ہوا کا دباؤ کھلاڑی کو دھکیلتا ہے"][0],
        "جب کمیت مرکز کے قریب آتی ہے تو گھومنے کی مزاحمت گھٹ جاتی ہے۔ بیرونی رکاوٹ نہ ہونے کی وجہ سے گھومنے کی کل طاقت کو پورا رکھنے کے لیے چکروں کی رفتار خود بخود دگنی تگنی ہو جاتی ہے۔"
    ),
    (
        "Why does a spinning bicycle wheel resist tilting sideways when you attempt to tip its axle while holding it (Gyroscopic Precession)?",
        ["Applying an external torque produces an angular momentum change perpendicular to both the torque and the spin axis", "The rubber tire attracts the floor with static charge", "Air currents inside the tube solidify", "Spokes create magnetic levitation"],
        "Applying an external torque produces an angular momentum change perpendicular to both the torque and the spin axis",
        "Gyroscopic torque tau = dL/dt = omega x L dictates that attempting to tip the wheel sideways causes a reaction torque 90 degrees out of phase, producing steady precession rather than tipping.",
        "جائرواسکوپک مزاحمت (Gyroscopic Precession): گھومتے ہوئے سائیکل کے پہیے کے ایکسل کو جب ہاتھ میں پکڑ کر سائیڈ پر موڑنے کی کوشش کریں تو وہ آپ کے ہاتھ کے خلاف ترچھا زور کیوں لگاتا ہے؟",
        ["لگائی گئی موڑنے والی قوت پہیے کے گھومنے کے مومنٹم کے ساتھ مل کر 90 ڈگری کے سیدھے زاویے پر نیا موڑ پیدا کرتی ہے", "ٹائر کا ربڑ جامد بجلی سے فرش کو کھینچتا ہے", "ٹیوب کے اندر کی ہوا جم جاتی ہے", "تاریں مقناطیسی اڑان پیدا کرتی ہیں"],
        ["لگائی گئی موڑنے والی قوت پہیے کے گھومنے کے مومنٹم کے ساتھ مل کر 90 ڈگری کے سیدھے زاویے پر نیا موڑ پیدا کرتی ہے", "ٹائر کا ربڑ جامد بجلی سے فرش کو کھینچتا ہے", "ٹیوب کے اندر کی ہوا جم جاتی ہے", "تاریں مقناطیسی اڑان پیدا کرتی ہیں"][0],
        "جب ایکسل کو دائیں موڑیں تو پہیہ دائیں مڑنے کی بجائے اوپر یا نیچے کو جھکتا ہے۔ یہ کونیائی مومنٹم کی ویکٹر سمت کا جادو ہے، جس کی وجہ سے تیزی سے دوڑتی ہوئی موٹر سائیکل گرتی نہیں ہے۔"
    ),
    (
        "Why does a heavy spinning top or gyroscope not fall down flat immediately, but instead slowly wobbles in a circle around the vertical axis?",
        ["Gravitational torque acting on the offset center of mass induces continuous gyroscopic precession rather than tipping", "The ground attracts the tip magnetically", "Centrifugal wind blows the top upward", "Friction sharpens the tip needle"],
        "Gravitational torque acting on the offset center of mass induces continuous gyroscopic precession rather than tipping",
        "Gravity pulls the top downward with torque tau = r x mg. Because the top has angular momentum L, dL = tau * dt forces the spin vector to trace out a cone around the vertical axis.",
        "لٹو کا چکر اور کشش ثقل (Precession of a Spinning Top): تیزی سے گھومتا ہوا لٹو کشش ثقل کی وجہ سے فوراً گرنے کی بجائے سیدھا کھڑا رہ کر گولائی میں جھولا کیوں کھاتا رہتا ہے؟",
        ["کشش ثقل کا نیچے گرانے والا زور لٹو کے گھومنے والے مومنٹم سے مل کر اسے گرانے کی بجائے دائرے میں گھمانے لگتا ہے", "زمین لٹو کی نوک کو مقناطیس کی طرح کھینچتی ہے", "مرکز گریز ہوا لٹو کو اوپر اٹھاتی ہے", "رگڑ نوک کو تیز کر دیتی ہے"],
        ["کشش ثقل کا نیچے گرانے والا زور لٹو کے گھومنے والے مومنٹم سے مل کر اسے گرانے کی بجائے دائرے میں گھمانے لگتا ہے", "زمین لٹو کی نوک کو مقناطیس کی طرح کھینچتی ہے", "مرکز گریز ہوا لٹو کو اوپر اٹھاتی ہے", "رگڑ نوک کو تیز کر دیتی ہے"][0],
        "کشش ثقل اسے نیچے گرانا چاہتی ہے، مگر کونیائی مومنٹم اس گراوٹ کے زاویے کو افقی سمت میں موڑ دیتا ہے۔ چنانچہ لٹو نیچے گرنے کی بجائے فضا میں ایک دائرہ بناتا ہوا جھومتا رہتا ہے۔"
    ),
    (
        "Why does water flowing down an ordinary household bathtub drain NOT reliably swirl in opposite directions in the Northern vs Southern hemispheres?",
        ["The Coriolis acceleration on a bathtub drain is millions of times weaker than residual turbulence, container asymmetry, and water filling currents", "The equator blocks Coriolis forces completely", "Drains are magnetized by plumbers", "Soap neutralizes the Earth's spin"],
        "The Coriolis acceleration on a bathtub drain is millions of times weaker than residual turbulence, container asymmetry, and water filling currents",
        "Coriolis force is significant only across macroscopic planetary scales (hurricanes). In a bathtub, a_coriolis ~ 10^-5 m/s^2 is completely dwarfed by initial fluid angular momentum.",
        "کوریولس اثر اور واش بیسن کا پانی (Coriolis Drain Myth): عام گھروں کے سنک میں پانی شمالی نصف کرہ میں گھڑی کی سمت اور جنوبی میں الٹی سمت گھوم کر کیوں نہیں گرتا؟",
        ["زمین کے گھماؤ کی قوت (Coriolis force) چھوٹے بیسن میں پانی کے اندرونی بہاؤ، نلکے کے جھٹکے اور بیسن کی ساخت کے مقابلے میں لاکھوں گنا کمزور ہوتی ہے", "خط استوا اس قوت کو روک دیتا ہے", "پلمبر نالیاں مقناطیسی بناتے ہیں", "صابن زمین کے گھماؤ کو زائل کرتا ہے"],
        ["زمین کے گھماؤ کی قوت (Coriolis force) چھوٹے بیسن میں پانی کے اندرونی بہاؤ، نلکے کے جھٹکے اور بیسن کی ساخت کے مقابلے میں لاکھوں گنا کمزور ہوتی ہے", "خط استوا اس قوت کو روک دیتا ہے", "پلمبر نالیاں مقناطیسی بناتے ہیں", "صابن زمین کے گھماؤ کو زائل کرتا ہے"][0],
        "یہ ایک عام غلط فہمی ہے۔ کوریولس اثر سمندری طوفانوں جیسے بڑے پیمانوں پر کام کرتا ہے۔ چھوٹے بیسن میں پانی کا رخ اس بات سے طے ہوتا ہے کہ نلکا کس رخ سے کھولا گیا تھا اور بیسن کی ڈھلوان کیسی ہے۔"
    ),
    (
        "Why do hurricane cloud spirals always spin counter-clockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere?",
        ["Planetary Coriolis deflection curves rushing air masses toward the right in the North and toward the left in the South around low-pressure centers", "Hurricanes follow ocean magnetic currents", "Solar heating pushes clouds westward", "Trade winds heat the sea"],
        "Planetary Coriolis deflection curves rushing air masses toward the right in the North and toward the left in the South around low-pressure centers",
        "Air rushing toward a central low-pressure eye is deflected to the right by the Coriolis acceleration in the Northern Hemisphere, generating a net counter-clockwise cyclonic circulation.",
        "سمندری طوفانوں کا گھماؤ (Cyclonic Coriolis Rotation): بڑے سمندری طوفان شمالی نصف کرے میں ہمیشہ گھڑی کی مخالف سمت اور جنوبی میں گھڑی کی سمت کیوں گھومتے ہیں؟",
        ["زمین کے گھماؤ کی کوریولس قوت ہوا کے بڑے بہاؤ کو شمال میں دائیں طرف اور جنوب میں بائیں طرف موڑ دیتی ہے", "طوفان سمندر کی مقناطیسی لہروں پر چلتے ہیں", "سورج کی گرمی بادلوں کو مغرب دھکیلتی ہے", "تجارتی ہوائیں سمندر کو گرم کرتی ہیں"],
        ["زمین کے گھماؤ کی کوریولس قوت ہوا کے بڑے بہاؤ کو شمال میں دائیں طرف اور جنوب میں بائیں طرف موڑ دیتی ہے", "طوفان سمندر کی مقناطیسی لہروں پر چلتے ہیں", "سورج کی گرمی بادلوں کو مغرب دھکیلتی ہے", "تجارتی ہوائیں سمندر کو گرم کرتی ہیں"][0],
        "جب ہزاروں کلومیٹر رقبے پر پھیلی ہوا کم دباؤ کے مرکز کی طرف بھاگتی ہے تو زمین کے گھومنے کی وجہ سے شمال میں وہ دائیں طرف مڑتی ہے، جس سے پورے طوفان کا گھماؤ گھڑی کی الٹی سمت بن جاتا ہے۔"
    ),
    (
        "Why does an ocean ship traveling at high speed through a narrow, shallow canal get drawn violently toward the canal embankment (the Bank Suction Effect)?",
        ["Bernoulli's Principle: water squeezed between the ship's hull and the bank accelerates, creating low pressure that sucks the hull toward the shore", "Canal banks contain iron deposits", "Propeller wakes reflect off stone", "Mud exerts electrostatic attraction"],
        "Bernoulli's Principle: water squeezed between the ship's hull and the bank accelerates, creating low pressure that sucks the hull toward the shore",
        "Constricted water flow between ship and bank increases flow velocity (Venturi effect). By Bernoulli's equation, this asymmetric velocity spike produces a pressure drop that pulls the stern toward the bank.",
        "نہر میں جہاز کا کنارے سے ٹکرانا (Bank Suction Effect): ایک بڑا بحری جہاز جب تنگ نہر میں تیز رفتار سے گزرتا ہے تو وہ خود بخود کنارے کی دیوار کی طرف کیوں کھنچ جاتا ہے؟",
        ["برنولی اصول: جہاز اور کنارے کے تنگ راستے میں پانی کی رفتار تیز ہونے سے دباؤ گر جاتا ہے جو جہاز کو کنارے کی طرف چوس لیتا ہے", "نہر کی دیوار میں لوہا ہوتا ہے", "پنکھے کی لہریں پتھر سے ٹکراتی ہیں", "کیچڑ جہاز کو مقناطیس کی طرح کھینچتا ہے"],
        ["برنولی اصول: جہاز اور کنارے کے تنگ راستے میں پانی کی رفتار تیز ہونے سے دباؤ گر جاتا ہے جو جہاز کو کنارے کی طرف چوس لیتا ہے", "نہر کی دیوار میں لوہا ہوتا ہے", "پنکھے کی لہریں پتھر سے ٹکراتی ہیں", "کیچڑ جہاز کو مقناطیس کی طرح کھینچتا ہے"][0],
        "کنارے کے پاس جگہ کم ہونے کی وجہ سے پانی کو تیزی سے گزرنا پڑتا ہے۔ پانی کی رفتار بڑھتے ہی سائیڈ کا پریشر کم ہو جاتا ہے اور دوسری طرف کا اونچا پریشر جہاز کو زبردستی کنارے پر چڑھا دیتا ہے۔"
    ),
    (
        "Why does two large container ships cruising parallel and close to each other in deep water get pulled irresistibly into a collision?",
        ["Water flowing through the narrow constriction between both hulls accelerates, creating a localized hydrodynamic low-pressure suction zone", "Radio antennas attract each other", "Engines generate synchronized magnetic fields", "Vibration softens sea water"],
        "Water flowing through the narrow constriction between both hulls accelerates, creating a localized hydrodynamic low-pressure suction zone",
        "The Venturi effect between two vessels increases fluid speed between them, decreasing hydrostatic pressure. Outer ocean pressure pushes both ships into a lateral collision.",
        "دو متوازی بحری جہازوں کا ٹکراؤ (Hydrodynamic Ship Attraction): کھلے سمندر میں جب دو بڑے جہاز پاس پاس متوازی چل رہے ہوں تو وہ اچانک آپس میں کیوں ٹکرا جاتے ہیں؟",
        ["دونوں جہازوں کے درمیانی تنگ خلا میں پانی کی رفتار بڑھنے سے ہائیڈروڈائنامک کم دباؤ بنتا ہے جو دونوں جہازوں کو ایک دوسرے کی طرف کھینچتا ہے", "ریڈیو اینٹینا ایک دوسرے کو کھینچتے ہیں", "انجن مقناطیسی فیلڈ بناتے ہیں", "تھرتھراہٹ پانی کو نرم کر دیتی ہے"],
        ["دونوں جہازوں کے درمیانی تنگ خلا میں پانی کی رفتار بڑھنے سے ہائیڈروڈائنامک کم دباؤ بنتا ہے جو دونوں جہازوں کو ایک دوسرے کی طرف کھینچتا ہے", "ریڈیو اینٹینا ایک دوسرے کو کھینچتے ہیں", "انجن مقناطیسی فیلڈ بناتے ہیں", "تھرتھراہٹ پانی کو نرم کر دیتی ہے"][0],
        "دونوں کے درمیان کا پانی تیزی سے گزرنے پر ویکیوم جیسا کم پریشر بناتا ہے، جبکہ جہازوں کی بیرونی سائیڈوں پر سمندر کا دباؤ معمول کے مطابق ہوتا ہے جو دونوں کو دبا کر آپس میں ٹکرا دیتا ہے۔"
    ),
    (
        "Why does a spinning ping-pong ball with top-spin dive steeply downward toward the table much faster than gravity alone would dictate (the Magnus Effect)?",
        ["Air dragged over the top moves opposite to oncoming airflow while air beneath moves with it, creating a net downward aerodynamic force", "Air friction pushes the ball down", "The hollow ball cools down", "Top-spin charges the plastic shell"],
        "Air dragged over the top moves opposite to oncoming airflow while air beneath moves with it, creating a net downward aerodynamic force",
        "Top-spin drags air forward over the upper surface, creating a stagnation point above and high velocity below. By Bernoulli's theorem, higher pressure above drives the ball down with Magnus force F_M.",
        "میگنس اثر اور ٹیبل ٹینس (Magnus Effect Top-spin): ٹاپ سپن کے ساتھ ماری گئی پنگ پانگ کی گیند عام گراوٹ کے مقابلے میں اچانک میز پر نیچے کی طرف غوطہ کیوں کھا جاتی ہے؟",
        ["گیند کے گھماؤ کی وجہ سے اوپر کی ہوا سست اور نیچے کی ہوا تیز ہو جاتی ہے جس سے اوپر کا ہوا کا دباؤ گیند کو نیچے کی طرف دھکیلتا ہے", "ہوا کی رگڑ گیند کو نیچے دباتی ہے", "کھوکھلی گیند ٹھنڈی ہو جاتی ہے", "گھمانے سے پلاسٹک پر چارج آ جاتا ہے"],
        ["گیند کے گھماؤ کی وجہ سے اوپر کی ہوا سست اور نیچے کی ہوا تیز ہو جاتی ہے جس سے اوپر کا ہوا کا دباؤ گیند کو نیچے کی طرف دھکیلتا ہے", "ہوا کی رگڑ گیند کو نیچے دباتی ہے", "کھوکھلی گیند ٹھنڈی ہو جاتی ہے", "گھمانے سے پلاسٹک پر چارج آ جاتا ہے"][0],
        "جب گیند آگے کو گھومتی ہے تو وہ اوپر کی ہوا کو روکتی ہے اور نیچے کی ہوا کو اپنے ساتھ پھینکتی ہے۔ اس سے اوپر ہائی پریشر بن جاتا ہے جو گیند کو پرندے کے غوطے کی طرح جھٹکے سے نیچے پٹخ دیتا ہے۔"
    ),
    (
        "Why does a golf ball covered with dimples travel roughly twice as far through the air as a perfectly smooth ball of identical mass and diameter?",
        ["Dimples trigger a turbulent boundary layer of air that clings longer to the ball, dramatically reducing aerodynamic wake drag", "Dimples store compressed air", "Dimpled plastic weighs less", "Smooth balls generate heat friction"],
        "Dimples trigger a turbulent boundary layer of air that clings longer to the ball, dramatically reducing aerodynamic wake drag",
        "Turbulent boundary layers possess higher momentum and resist adverse pressure gradients better than laminar layers, delaying flow separation and shrinking the low-pressure suction wake behind the ball.",
        "گولف کی گیند کے گڑھے (Golf Ball Dimples): گڑھوں والی کھردری گولف بال بالکل چکنی گیند کے مقابلے میں دوگنا زیادہ دور تک کیوں اڑتی ہے؟",
        ["گڑھے ہوا کی سطح پر ہلکا سا انتشار (Turbulence) پیدا کرتے ہیں جس سے ہوا دیر تک گیند کے ساتھ جڑی رہتی ہے اور پیچھے کا کھچاؤ کم ہو جاتا ہے", "گڑھوں میں ہوا قید ہو جاتی ہے", "گڑھوں والی گیند ہلکی ہوتی ہے", "چکنی گیند حرارت پیدا کرتی ہے"],
        "گڑھے ہوا کی سطح پر ہلکا سا انتشار (Turbulence) پیدا کرتے ہیں جس سے ہوا دیر تک گیند کے ساتھ جڑی رہتی ہے اور پیچھے کا کھچاؤ کم ہو جاتا ہے",
        "چکنی گیند کے پیچھے ہوا جلدی بکھر جاتی ہے جس سے پیچھے ایک بڑا خلا اور ڈریگ بنتا ہے جو گیند کو روکتا ہے۔ گڑھے ہوا کو گیند کے پچھلے حصے تک موڑ کر لے جاتے ہیں، جس سے ہوا کا کھچاؤ ادھا رہ جاتا ہے۔"
    ),
]
