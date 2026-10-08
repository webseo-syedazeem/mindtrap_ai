# -*- coding: utf-8 -*-
"""
Tricky Batch 5 (54 items: 247-300).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    (
        "Why did Alan Turing prove that it is mathematically impossible to write a master computer program that can determine whether any arbitrary program will finish running or run forever (the Halting Problem)?",
        ["Self-referential contradiction: feeding an inverted program into itself creates an unavoidable logical paradox (diagonalization)", "Computer memory chips overheat", "Compilers cannot read while loops", "Turing machines lack sufficient clock speed"],
        "Self-referential contradiction: feeding an inverted program into itself creates an unavoidable logical paradox (diagonalization)",
        "Turing used Cantor's diagonalization: suppose program H(P, i) decides halting. Construct program D that halts if H says it loops, and loops if H says it halts. Running D(D) yields a direct contradiction.",
        "ہالٹنگ پرابلم (Turing's Halting Problem): ایلن ٹیورنگ نے ریاضیاتی طور پر یہ کیوں ثابت کیا کہ کوئی ایسا ماسٹر سوفٹ ویئر بنانا ناممکن ہے جو یہ بتا سکے کہ آیا کوئی بھی دوسرا پروگرام کبھی رکے گا یا ہمیشہ چلتا رہے گا؟",
        ["خود حوالہ جاتی تضاد (Self-referential contradiction): اگر ایسا پروگرام اپنے ہی الٹے عکس کا تجزیہ کرے تو وہ ایک ناممکن منطقی بند گلی میں پھنس جاتا ہے", "کمپیوٹر کی میموری گرم ہو جاتی ہے", "کمپائلر لوپ نہیں پڑھ سکتے", "پرانے کمپیوٹرز کی رفتار کم تھی"],
        "خود حوالہ جاتی تضاد (Self-referential contradiction): اگر ایسا پروگرام اپنے ہی الٹے عکس کا تجزیہ کرے تو وہ ایک ناممکن منطقی بند گلی میں پھنس جاتا ہے",
        "اگر ہم ایسا جج پروگرام بنائیں، اور اس کے آگے ایک ایسا الٹا پروگرام لگا دیں جو جج کے 'رکنے' کے فیصلے پر ہمیشہ چلے اور 'چلنے' کے فیصلے پر رک جائے، تو وہ جج اپنے ہی بارے میں سچ نہیں بول سکتا۔"
    ),
    (
        "What devastating truth about mathematics was revealed by Kurt Gödel's First Incompleteness Theorem in 1931?",
        ["Any consistent axiomatic mathematical system capable of doing basic arithmetic contains true statements that can never be proven within the system", "All mathematical equations are fundamentally incorrect", "Computers will replace mathematicians", "Prime numbers end at one trillion"],
        "Any consistent axiomatic mathematical system capable of doing basic arithmetic contains true statements that can never be proven within the system",
        "Gödel constructed a self-referential statement G: 'This statement is not provable in system T'. If G is provable, T is inconsistent; if G is unprovable, G is true, proving T is incomplete.",
        "گوئڈل کا نامکملیت کا تھیورم (Gödel's Incompleteness Theorem): 1931 میں ریاضی دان کرٹ گوئڈل نے ریاضی کی بنیادوں کے بارے میں کیا چونکا دینے والا انکشاف کیا؟",
        ["حساب کا کوئی بھی باقاعدہ اور درست نظام اپنے اندر ایسے سچے بیانات ضرور رکھتا ہے جنہیں اسی نظام کے اصولوں سے کبھی ثابت نہیں کیا جا سکتا", "تمام ریاضیاتی مساواتیں بنیادی طور پر غلط ہیں", "کمپیوٹر ریاضی دانوں کی جگہ لے لیں گے", "پرائم نمبرز ایک کھرب پر ختم ہو جاتے ہیں"],
        "حساب کا کوئی بھی باقاعدہ اور درست نظام اپنے اندر ایسے سچے بیانات ضرور رکھتا ہے جنہیں اسی نظام کے اصولوں سے کبھی ثابت نہیں کیا جا سکتا",
        "گوئڈل نے ثابت کیا کہ ریاضی کا کوئی بھی مکمل نظام اپنے ہی سچ کا احاطہ نہیں کر سکتا۔ کچھ سچائیاں ایسی ہوتی ہیں جو سچی تو ہیں مگر کتاب کے اصولوں کے دائرے میں رہ کر انہیں ثابت کرنا ناممکن ہوتا ہے۔"
    ),
    (
        "In theoretical computer science, what core question is posed by the million-dollar Millennium Prize problem 'P versus NP'?",
        ["Whether every computational problem whose proposed solution can be verified quickly (in polynomial time) can also be solved quickly", "Whether computers can think like humans", "Whether quantum computers can break glass", "Whether internet speeds can exceed light"],
        "Whether every computational problem whose proposed solution can be verified quickly (in polynomial time) can also be solved quickly",
        "P is the class of problems solvable in polynomial time; NP is the class verifiable in polynomial time. If P = NP, then finding a needle in a haystack is computationally as easy as recognizing the needle once found.",
        "پی بمقابلہ این پی کا معمہ (P versus NP Problem): کمپیوٹر سائنس کا یہ دس لاکھ ڈالر کا انعام یافتہ بنیادی سوال دراصل کیا پوچھتا ہے؟",
        ["کیا ہر وہ پیچیدہ مسئلہ جس کا دیا گیا جواب تیزی سے چیک اور تصدیق کیا جا سکتا ہے، اسے خود حل کرنا بھی اتنا ہی تیز اور آسان ہو سکتا ہے؟", "کیا کمپیوٹر انسان کی طرح سوچ سکتے ہیں؟", "کیا کوانٹم کمپیوٹر شیشہ توڑ سکتے ہیں؟", "کیا انٹرنیٹ کی رفتار روشنی سے تیز ہو سکتی ہے؟"],
        "کیا ہر وہ پیچیدہ مسئلہ جس کا دیا گیا جواب تیزی سے چیک اور تصدیق کیا جا سکتا ہے، اسے خود حل کرنا بھی اتنا ہی تیز اور آسان ہو سکتا ہے؟",
        "مثال کے طور پر سوڈوکو یا پاس ورڈ کا صحیح حل چیک کرنا چند سیکنڈ کا کام ہے، مگر حل تلاش کرنے میں صدیاں لگ سکتی ہیں۔ سوال یہ ہے کہ کیا کوئی ایسا جادوئی شارٹ کٹ موجود ہے جو تلاش کو بھی تصدیق جتنا آسان بنا دے؟"
    ),
    (
        "Why is John Conway's zero-player cellular automaton 'The Game of Life' proved to be Turing-Complete?",
        ["Its simple 2D grid rules of live and dead cells can simulate logic gates, memory registers, and emulate any universal computer", "It evolves real living biological bacteria", "It predicts real human lifespans", "It operates without consuming electricity"],
        "Its simple 2D grid rules of live and dead cells can simulate logic gates, memory registers, and emulate any universal computer",
        "Gliders, glider guns, and eaters construct logic circuits (AND, OR, NOT gates) and sliding memory tapes. Consequently, the Game of Life can simulate any algorithm or a full Turing machine.",
        "کونوے کی گیم آف لائف (Conway's Game of Life Turing Completeness): کالے اور سفید چوکوروں کے چند سادہ اصولوں والی یہ گیم ایک مکمل کمپیوٹر کی طرح کیسے کام کر سکتی ہے؟",
        ["زندہ اور مردہ خانوں کے ملاپ سے بننے والے گلائیڈرز اور نمونے لاجک گیٹس (AND, OR, NOT) بنا کر دنیا کے کسی بھی کمپیوٹر پروگرام کو چلا سکتے ہیں", "یہ اصلی حیاتیاتی بیکٹیریا پیدا کرتی ہے", "یہ انسان کی عمر کی پیشن گوئی کرتی ہے", "یہ بغیر بجلی کے چلتی ہے"],
        "زندہ اور مردہ خانوں کے ملاپ سے بننے والے گلائیڈرز اور نمونے لاجک گیٹس (AND, OR, NOT) بنا کر دنیا کے کسی بھی کمپیوٹر پروگرام کو چلا سکتے ہیں",
        "اگرچہ اس میں کوئی کھلاڑی نہیں ہوتا، مگر خانوں کے نمونے آپس میں ٹکرا کر برقی سرکٹوں کی طرح لاجک حل کرتے ہیں، یہاں تک کہ اس گیم کے اندر پوری گیم آف لائف کی دوسری کاپی بھی چلائی جا سکتی ہے۔"
    ),
    (
        "Why is the Busy Beaver function BB(n)—the maximum number of steps an n-state Turing machine can execute before halting—fundamentally non-computable?",
        ["It grows strictly faster than any computable function that can ever be defined or programmed in mathematics", "Turing machines run out of paper tape", "Beaver algorithms cause memory leaks", "Numbers exceed the atoms in the universe"],
        "It grows strictly faster than any computable function that can ever be defined or programmed in mathematics",
        "Tibor Radó proved that if BB(n) were computable, one could solve the Halting Problem by simulating any n-state machine for BB(n) steps. Hence BB(n) outpaces all recursive functions, including Ackermann's.",
        "بزی بیور فنکشن (Busy Beaver Non-Computable Function): ریاضی کا یہ فنکشن کسی بھی کمپیوٹر پروگرام کے ذریعے حساب لگانا قطعی ناممکن کیوں ہے؟",
        ["اس کے بڑھنے کی رفتار دنیا کے کسی بھی ممکنہ پروگرام شدہ فنکشن سے اتنی زیادہ تیز ہے کہ یہ ہر حسابی حد کو توڑ دیتا ہے", "کمپیوٹر کے پاس کاغذ کا فیتہ ختم ہو جاتا ہے", "یہ پروگرام میموری لیک کر دیتے ہیں", "اعداد کائنات کے ایٹموں سے بڑے ہو جاتے ہیں"],
        "اس کے بڑھنے کی رفتار دنیا کے کسی بھی ممکنہ پروگرام شدہ فنکشن سے اتنی زیادہ تیز ہے کہ یہ ہر حسابی حد کو توڑ دیتا ہے",
        "اگر ہم اسے حل کر سکیں تو ہم ٹیورنگ کا ہالٹنگ پرابلم حل کر لیں گے جو کہ ناممکن ہے۔ بزی بیور کے ابتدائی چند نمبر ہی اتنے دیوہیکل ہو جاتے ہیں کہ انہیں کائنات کے تمام کاغذوں پر بھی لکھنا ممکن نہیں۔"
    ),
    (
        "In John Searle's famous 'Chinese Room' thought experiment, why does manipulating symbol cards inside a closed room fail to constitute true artificial intelligence?",
        ["Syntax does not equal semantics: purely formal rule-following lacks intentionality, subjective meaning, and genuine understanding", "The person inside translates too slowly", "Chinese characters are too complex for paper", "The room lacks ventilation"],
        "Syntax does not equal semantics: purely formal rule-following lacks intentionality, subjective meaning, and genuine understanding",
        "Searle argued that a person who understands zero Chinese can follow an English rulebook to output perfect Chinese answers. The system possesses syntactic symbol manipulation without intentional semantics.",
        "چینی کمرے کا فکری تجربہ (Searle's Chinese Room Argument): ایک کمرے میں بند شخص جو چینی زبان کا ایک لفظ نہیں جانتا، کتاب دیکھ کر چینی سوالوں کے بالکل درست جواب کیسے دے سکتا ہے مگر پھر بھی کچھ نہیں سمجھتا؟",
        ["نشانات کی ترتیب (Syntax) مفہوم و ادراک (Semantics) کے برابر نہیں ہوتی؛ محض قواعد پر لکیر کے فقیر کی طرح عمل کرنا سچی سمجھ بوجھ نہیں کہلاتا", "کمرے والا شخص بہت سست ہے", "چینی حروف کاغذ پر نہیں آتے", "کمرے میں ہوا کی کمی ہے"],
        "نشانات کی ترتیب (Syntax) مفہوم و ادراک (Semantics) کے برابر نہیں ہوتی؛ محض قواعد پر لکیر کے فقیر کی طرح عمل کرنا سچی سمجھ بوجھ نہیں کہلاتا",
        "باہر والے سمجھیں گے کہ اندر کوئی چینی اسکالر بیٹھا ہے، جبکہ اندر والا شخص صرف یہ دیکھ رہا ہے کہ فلاں لکیر کے بعد فلاں ڈبہ باہر پھینکنا ہے۔ یہ دلیل ثابت کرتی ہے کہ کمپیوٹر الفاظ کے اصل معانی کو نہیں جانتا۔"
    ),
    (
        "In Frank Jackson's 'Mary's Room' thought experiment, what philosophical revelation occurs when Mary—a neuroscientist who knows all physical facts about color from a black-and-white room—steps outside and sees a red rose?",
        ["She gains non-physical experiential knowledge (qualia), demonstrating that physicalism cannot completely describe conscious experience", "She discovers roses are made of wax", "Her optic nerves go blind from sunlight", "She realizes red is an acoustic illusion"],
        "She gains non-physical experiential knowledge (qualia), demonstrating that physicalism cannot completely describe conscious experience",
        "The Knowledge Argument argues that despite knowing all objective physical facts (wavelengths, neural firing), seeing red gives Mary new experiential knowledge of 'what it is like' to see red (qualia).",
        "میری کا کمرہ اور رنگوں کا ادراک (Mary's Room & Qualia): بلیک اینڈ وائٹ کمرے میں بیٹھ کر رنگوں کی تمام فزکس جاننے والی سائنسدان جب باہر نکل کر پہلی بار سرخ گلاب دیکھتی ہے تو اسے کیا نیا علم ملتا ہے؟",
        ["اسے احساس کی ذاتی اور غیر مادی کیفیت (Qualia) کا تجربہ ہوتا ہے، جس سے ثابت ہوا کہ صرف مادی فزکس کا علم انسان کے اندرونی شعور کو مکمل بیان نہیں کر سکتا", "اسے پتہ چلتا ہے کہ گلاب موم کا بنا ہے", "دھوپ سے اس کی آنکھیں خراب ہو جاتی ہیں", "اسے لگتا ہے سرخ رنگ آواز کا دھوکہ ہے"],
        "اسے احساس کی ذاتی اور غیر مادی کیفیت (Qualia) کا تجربہ ہوتا ہے، جس سے ثابت ہوا کہ صرف مادی فزکس کا علم انسان کے اندرونی شعور کو مکمل بیان نہیں کر سکتا",
        "وہ جانتی تھی کہ 700 نینو میٹر کی لہر دماغ کے کس خلیے کو روشن کرتی ہے، مگر سرخ رنگ کو 'محسوس کرنا کیسا ہوتا ہے' یہ تجربہ اسے پہلی بار گلاب کو دیکھ کر ہی ملا۔"
    ),
    (
        "What is a 'Philosophical Zombie' (p-zombie) in David Chalmers' philosophy of mind?",
        ["A hypothetical entity physically and behaviorally identical to a human being in every subatomic detail, yet completely lacking subjective conscious experience", "A deceased human reanimated by fungal toxins", "A humanoid robot covered in silicone skin", "A sleepwalker carrying a flashlight"],
        "A hypothetical entity physically and behaviorally identical to a human being in every subatomic detail, yet completely lacking subjective conscious experience",
        "Chalmers uses p-zombies to formulate the Hard Problem of Consciousness: if a zombie world is logically conceivable where all physical facts hold without qualia, consciousness is not purely physical.",
        "فلسفیانہ زومبی کا تصور (Philosophical Zombie / P-Zombie): شعور کے فلسفے میں ڈیوڈ چامرز کا پیش کردہ 'پی زومبی' عام انسان سے کیسے مختلف ہوتا ہے؟",
        ["ایسا فرضی انسان جو ایٹمی ساخت، حرکات، باتوں اور رویے میں ہو بہو عام انسان جیسا ہو مگر اس کے اندر کوئی باطنی شعور اور ذاتی احساس موجود نہ ہو", "مردہ انسان جسے زہر سے زندہ کیا گیا ہو", "سلیکون کی کھال والا روبوٹ", "نیند میں چلنے والا انسان"],
        "ایسا فرضی انسان جو ایٹمی ساخت، حرکات، باتوں اور رویے میں ہو بہو عام انسان جیسا ہو مگر اس کے اندر کوئی باطنی شعور اور ذاتی احساس موجود نہ ہو",
        "اگر اسے سوئی چبھوئی جائے تو وہ عام انسان کی طرح چیخے گا اور آنسو بہائے گا، مگر اندرونی طور پر وہ درد کی تکلیف کو محسوس کرنے والے کسی شعوری وجود سے مکمل خالی ہو گا۔"
    ),
    (
        "In Derek Parfit's Teletransporter Paradox, a machine scans your atoms, destroys your body on Earth, and reassembles an identical molecule-for-molecule copy on Mars. Did you travel to Mars, or were you murdered?",
        ["If personal identity requires continuous physical survival, you were killed and replaced by an identical psychological replica", "Your soul teleported through radio antennas", "Mars air changes your memories", "The scanner turns matter into pure energy"],
        "If personal identity requires continuous physical survival, you were killed and replaced by an identical psychological replica",
        "Parfit used this to challenge non-reductionist views of identity: psychological continuity is preserved, but if the original machine fails to destroy the Earth body, two identical 'yous' exist simultaneously.",
        "ٹیلی ٹرانسپورٹر کا معمہ (Teletransporter Paradox): اگر ایک مشین آپ کے ایٹم اسکین کر کے زمین پر آپ کو تحلیل کر دے اور مریخ پر ہو بہو کاپی بنا دے، تو کیا آپ مریخ پہنچے یا قتل ہو گئے؟",
        ["اگر انسان کی بقا جسم اور شعور کے غیر منقطع تسلسل سے جڑی ہے، تو زمین والا انسان سچ مچ مر گیا اور مریخ پر صرف اس کی ہم شکل کاپی پیدا ہوئی", "روح انٹینا کے ذریعے مریخ پہنچ گئی", "مریخ کی ہوا یادداشت بدل دیتی ہے", "مشین مادے کو روشنی بنا دیتی ہے"],
        "اگر انسان کی بقا جسم اور شعور کے غیر منقطع تسلسل سے جڑی ہے، تو زمین والا انسان سچ مچ مر گیا اور مریخ پر صرف اس کی ہم شکل کاپی پیدا ہوئی",
        "اگر مشین زمین والے جسم کو مٹانا بھول جائے، تو دونوں انسان بیک وقت زندہ ہوں گے۔ اس سے ثابت ہوتا ہے کہ مریخ پر جانے والا انسان آپ کی صرف ایک نئی کاپی ہے، آپ کا اپنا شعوری تسلسل تو زمین پر ہی ختم ہو گیا۔"
    ),
    (
        "In Donald Davidson's 'Swampman' thought experiment, lightning strikes a swamp, simultaneously vaporizing Davidson and accidentally organizing swamp mud into his identical molecular clone. Does Swampman have thoughts?",
        ["Externalism argues Swampman lacks genuine mental content because his brain states have zero causal historical connection to the real world", "Swampman melts back into green slime", "Lightning electrifies his speech center", "Swampman has double memory capacity"],
        "Externalism argues Swampman lacks genuine mental content because his brain states have zero causal historical connection to the real world",
        "Semantic externalism contends that meaning and mental states depend on causal history with objects in the environment. Swampman recognizes Davidson's friends purely by accidental structure without historic reference.",
        "دلدلی انسان کا معمہ (Swampman Thought Experiment): آسمانی بجلی گرنے سے ایک انسان بھاپ بن جائے اور دلدل کے کیچڑ سے اس کا ہو بہو مالیکیولر کلون بن جائے، تو کیا وہ کلون سچی سوچ رکھ سکتا ہے؟",
        ["خارجی فلسفے کے مطابق اس کے پاس حقیقی خیالات نہیں ہو سکتے کیونکہ اس کے دماغی رابطوں کی دنیا کی چیزوں کے ساتھ کوئی تاریخی اور تجرباتی جڑت موجود نہیں ہے", "وہ پگھل کر کیچڑ بن جاتا ہے", "بجلی اس کے بولنے کی صلاحیت ختم کرتی ہے", "اس کی یادداشت دگنی ہو جاتی ہے"],
        "خارجی فلسفے کے مطابق اس کے پاس حقیقی خیالات نہیں ہو سکتے کیونکہ اس کے دماغی رابطوں کی دنیا کی چیزوں کے ساتھ کوئی تاریخی اور تجرباتی جڑت موجود نہیں ہے",
        "اگرچہ وہ گھر جا کر انسان کے دوستوں سے گلے ملے گا، مگر وہ دراصل کسی کو نہیں جانتا کیونکہ اس کے دماغ میں وہ یادیں زندگی کے حقیقی تجربات سے نہیں بلکہ کیچڑ پر بجلی گرنے کے محض ایک اتفاقی حادثے سے بنی ہیں۔"
    ),
    (
        "In Edmund Gettier's famous 1963 counterexamples, why is having a 'Justified True Belief' shown to be insufficient to constitute genuine Knowledge?",
        ["Beliefs can be justified and happen to be objectively true entirely through good epistemic luck or coincidence", "People lie about their beliefs", "Beliefs require mathematical equations", "Perception is always an illusion"],
        "Beliefs can be justified and happen to be objectively true entirely through good epistemic luck or coincidence",
        "Gettier refuted Plato's classic definition of knowledge: if John has justified evidence that Smith owns a Ford, and by pure luck his friend Brown happens to be in Barcelona, his true belief is founded on accidental luck.",
        "گیٹیئر کا مسئلہ (Gettier Problem): 1963 میں ایڈمنڈ گیٹیئر نے افلاطون کے اس قدیم دعوے کو کیسے غلط ثابت کیا کہ 'دلیل کے ساتھ سچا یقین ہی اصل علم ہوتا ہے'؟",
        ["انسان کا یقین مکمل دلیل پر مبنی ہونے اور اتفاق سے سچ ثابت ہونے کے باوجود محض ایک اندھی قسمت اور تکے کی بنیاد پر سچ ہو سکتا ہے", "لوگ اپنے یقین کے بارے میں جھوٹ بولتے ہیں", "یقین کے لیے حسابی مساواتیں درکار ہیں", "دیکھنا ہمیشہ دھوکہ ہوتا ہے"],
        "انسان کا یقین مکمل دلیل پر مبنی ہونے اور اتفاق سے سچ ثابت ہونے کے باوجود محض ایک اندھی قسمت اور تکے کی بنیاد پر سچ ہو سکتا ہے",
        "مثال کے طور پر آپ بند گھڑی دیکھ کر اندازہ لگائیں کہ 12 بجے ہیں، اور اتفاق سے اس وقت واقعی 12 بج رہے ہوں۔ آپ کا یقین سچا بھی ہے اور دلیل بھی ہے، مگر یہ علم نہیں بلکہ محض ایک اتفاق ہے۔"
    ),
    (
        "In Molyneux's Problem posed to John Locke in 1688, if a man born completely blind learns to distinguish a sphere from a cube by touch alone, can he instantly identify them by sight if his vision is suddenly restored?",
        ["Empirical experiments show no: cross-modal mapping between tactile representations and visual percepts must be learned through sensory experience", "Yes, human geometry is innate", "Yes, cubes feel sharp to the eyes", "No, the restored eyes can only see red"],
        "Empirical experiments show no: cross-modal mapping between tactile representations and visual percepts must be learned through sensory experience",
        "Project Prakash tested congenitally blind patients whose sight was surgically restored. Patients could distinguish shapes visually, but failed to map tactile touch memories onto novel visual images without practice.",
        "مولینکس کا سوال (Molyneux's Problem): پیدائشی نابینا جو چھو کر گیند اور ڈبے میں فرق کرتا ہے، اگر اس کی بینائی اچانک آ جائے تو کیا وہ محض دیکھ کر بتا سکتا ہے کہ کون سی گیند ہے اور کون سا ڈبہ؟",
        ["طبی تجربات نے ثابت کیا کہ نہیں؛ چھونے کے احساس اور آنکھوں سے دیکھنے کے احساس کے درمیان دماغی پل تجربے اور وقت کے ساتھ ہی بنتا ہے", "ہاں، جیومیٹری پیدائشی طور پر دماغ میں ہوتی ہے", "ہاں، چوکور چیز آنکھوں کو چبھتی ہے", "نہیں، نئی آنکھیں صرف لال دیکھتی ہیں"],
        "طبی تجربات نے ثابت کیا کہ نہیں؛ چھونے کے احساس اور آنکھوں سے دیکھنے کے احساس کے درمیان دماغی پل تجربے اور وقت کے ساتھ ہی بنتا ہے",
        "آنکھیں کھلنے پر وہ دونوں چیزیں دیکھ سکتا ہے، مگر اس کا دماغ یہ نہیں جوڑ پاتا کہ ہاتھ سے چھوئی جانے والی گولائی آنکھ سے دیکھنے پر کیسی لگتی ہے۔ یہ ربط چند ہفتوں کی مشق کے بعد ہی پیدا ہوتا ہے۔"
    ),
    (
        "In the Sorites Paradox (Paradox of the Heap), removing a single grain of sand from a heap still leaves a heap. Why does this create an intractable logical problem?",
        ["Repeatedly applying an uncontroversial inductive premise forces the absurd conclusion that a single grain of sand is a 'heap' due to vague semantic boundaries", "Sand grains dissolve into air", "Mathematics cannot count grains", "Heaps require exactly 10,000 grains"],
        "Repeatedly applying an uncontroversial inductive premise forces the absurd conclusion that a single grain of sand is a 'heap' due to vague semantic boundaries",
        "The paradox demonstrates the problem of vagueness in classical binary logic: natural language predicates ('heap', 'bald') lack crisp cutoff boundaries, challenging bivalence and modus ponens.",
        "ریت کے ڈھیر کا معمہ (Sorites Paradox / Paradox of the Heap): ریت کے بڑے ڈھیر سے ایک دانہ ہٹانے پر وہ ڈھیر ہی رہتا ہے، مگر اس منطق سے کیسا مضحکہ خیز نتیجہ نکلتا ہے؟",
        ["ایک ایک دانہ ہٹاتے ہٹاتے منطق یہ ماننے پر مجبور کر دیتی ہے کہ صرف ایک اکیلا دانہ بھی ریت کا 'ڈھیر' ہے، کیونکہ الفاظ کی کوئی قطعی حد مقرر نہیں ہوتی", "ریت کے دانے ہوا میں گھل جاتے ہیں", "ریاضی دان دانوں کو گن نہیں سکتے", "ڈھیر کے لیے ٹھیک دس ہزار دانے درکار ہیں"],
        "ایک ایک دانہ ہٹاتے ہٹاتے منطق یہ ماننے پر مجبور کر دیتی ہے کہ صرف ایک اکیلا دانہ بھی ریت کا 'ڈھیر' ہے، کیونکہ الفاظ کی کوئی قطعی حد مقرر نہیں ہوتی",
        "کوئی نہیں بتا سکتا کہ کس دانے پر ڈھیر، ڈھیر نہیں رہتا۔ زبان کے مبہم الفاظ روایتی منطق کی دو ٹوک سچ اور جھوٹ کی سرحدوں میں فٹ نہیں بیٹھتے۔"
    ),
    (
        "Why did Bertrand Russell's famous paradox about 'the set of all sets that do not contain themselves' shake the foundations of set theory?",
        ["If the set belongs to itself, it violates its definition; if it does not belong to itself, it must belong to itself (R in R <=> R not in R)", "Sets are too heavy for mathematics", "Cantor's pencils broke during calculation", "Zero is not an allowed mathematical number"],
        "If the set belongs to itself, it violates its definition; if it does not belong to itself, it must belong to itself (R in R <=> R not in R)",
        "Naive set theory allowed unrestricted comprehension {x : P(x)}. Russell's paradox proved naive comprehension leads to fatal contradictions, necessitating axiomatic Zermelo-Fraenkel set theory with type hierarchies.",
        "رسل کا پیراڈاکس (Russell's Paradox): برٹرینڈ رسل کے اس معمے نے کہ 'کیا ان تمام سیٹس کا سیٹ جو اپنے آپ میں شامل نہیں ہیں، خود میں شامل ہے؟' پوری ریاضی کو کیوں ہلا دیا؟",
        ["اگر وہ سیٹ اپنے آپ میں شامل ہو تو وہ اپنی ہی تعریف کی خلاف ورزی کرتا ہے، اور اگر شامل نہ ہو تو قانون کے مطابق اسے شامل ہونا پڑے گا", "سیٹس ریاضی کے لیے بہت وزنی ہوتے ہیں", "حساب لگاتے وقت پنسل ٹوٹ گئی تھی", "صفر ریاضی میں ممنوع ہے"],
        "اگر وہ سیٹ اپنے آپ میں شامل ہو تو وہ اپنی ہی تعریف کی خلاف ورزی کرتا ہے، اور اگر شامل نہ ہو تو قانون کے مطابق اسے شامل ہونا پڑے گا",
        "جیسے گاؤں کا وہ نائی جو صرف ان لوگوں کی داڑھی بناتا ہے جو اپنی داڑھی خود نہیں بناتے؛ اب سوال یہ ہے کہ کیا وہ اپنی داڑھی بنائے گا؟ دونوں صورتوں میں شدید تضاد پیدا ہوتا ہے۔"
    ),
    (
        "Why is Berry's Paradox ('The smallest positive integer not definable in under eleven words') a self-contradictory linguistic mind trap?",
        ["The phrase contains exactly ten words and defines the integer, directly violating the premise that the integer cannot be defined in under eleven words", "Numbers cannot be written in words", "Eleven is a prime number", "Printers omit small numbers"],
        "The phrase contains exactly ten words and defines the integer, directly violating the premise that the integer cannot be defined in under eleven words",
        "The English description 'The smallest positive integer not definable in under eleven words' has 10 words. If it successfully names an integer N, then N has just been defined in under eleven words.",
        "بیری کا معمہ (Berry's Paradox): 'وہ سب سے چھوٹا عدد جو گیارہ سے کم الفاظ میں بیان نہ ہو سکے' جملہ خود اپنے ہی بیان کی دھجیاں کیسے اڑا دیتا ہے؟",
        ["یہ پورا جملہ خود دس الفاظ پر مشتمل ہے اور اس عدد کی بالکل درست نشاندہی کر دیتا ہے، جس سے اس کا اپنا ہی دعویٰ باطل ہو جاتا ہے", "نمبروں کو الفاظ میں نہیں لکھا جا سکتا", "گیارہ ایک پرائم نمبر ہے", "پرنٹرز چھوٹے نمبر نہیں چھاپتے"],
        "یہ پورا جملہ خود دس الفاظ پر مشتمل ہے اور اس عدد کی بالکل درست نشاندہی کر دیتا ہے، جس سے اس کا اپنا ہی دعویٰ باطل ہو جاتا ہے",
        "اگر وہ عدد دس الفاظ میں بیان ہو گیا، تو وہ اس تعریف پر پورا نہیں اترتا؛ اور اگر نہیں ہوا تو وہ اس تعریف پر پورا اترتا ہے۔ یہ قدرتی زبان کی مبہم تعریفوں کا تضاد ہے۔"
    ),
    (
        "How did Georg Cantor's Diagonal Argument prove that there are strictly more real numbers (decimals) between 0 and 1 than all the infinite counting integers combined?",
        ["By constructing a new decimal number whose nth digit differs from the nth digit of the nth number in any proposed list, proving real numbers are uncountably infinite", "Decimals have infinite decimal points", "Integers end at one billion", "Rulers cannot measure fractions"],
        "By constructing a new decimal number whose nth digit differs from the nth digit of the nth number in any proposed list, proving real numbers are uncountably infinite",
        "Cantor assumed an exhaustive list of reals exists. By flipping the diagonal digit (e.g. if d_nn = 1 set to 2), he constructed a real number guaranteed to be missing from the list, proving |R| > |N|.",
        "کینٹور کا ڈائیگنل طریقہ (Cantor's Diagonal Argument): جارج کینٹور نے یہ کیسے ثابت کیا کہ صفر اور ایک کے درمیان اعشاریہ والے اعداد کی لامتناہی گنتی دنیا کے تمام مکمل اعداد کی لامتناہی گنتی سے بھی زیادہ بڑی ہے؟",
        ["ایک ایسا نیا اعشاریہ عدد بنا کر جس کا ہر ہندسہ لسٹ کے ترچھے ہندسے سے مختلف ہو، جس سے ثابت ہوا کہ تمام اعداد کی کبھی مکمل لسٹ بن ہی نہیں سکتی", "اعشاریہ کے کئی نقطے ہوتے ہیں", "گنتی ایک ارب پر ختم ہو جاتی ہے", "فیتے کسریں نہیں ناپ سکتے"],
        "ایک ایسا نیا اعشاریہ عدد بنا کر جس کا ہر ہندسہ لسٹ کے ترچھے ہندسے سے مختلف ہو، جس سے ثابت ہوا کہ تمام اعداد کی کبھی مکمل لسٹ بن ہی نہیں سکتی",
        "کینٹور نے دنیا کو دکھایا کہ لامتناہی (Infinity) کے بھی مختلف درجے ہوتے ہیں۔ گنتی کے اعداد لامتناہی ہیں، مگر اعشاریہ کے اعداد کی لامتناہی اس سے بھی کہیں زیادہ دیوہیکل اور لا محدود ہے۔"
    ),
    (
        "In David Hilbert's Grand Hotel with an infinite number of fully occupied rooms, how can the manager easily accommodate a newly arriving guest without evicting anyone?",
        ["By shifting the guest in room n to room n + 1, freeing up Room 1 for the newcomer", "By building a new penthouse floor", "By making two guests share a bed", "By turning the hotel upside down"],
        "By shifting the guest in room n to room n + 1, freeing up Room 1 for the newcomer",
        "Hilbert demonstrated the counter-intuitive arithmetic of transfinite cardinals: aleph_0 + 1 = aleph_0. Shifting each occupant to room n+1 frees room 1 while everyone still has a private room.",
        "ہلبرٹ کا انفینٹ ہوٹل (Hilbert's Grand Hotel): اگر ایک ہوٹل کے تمام لامتناہی کمرے پہلے ہی مکمل بھرے ہوں، تو نیا مہمان آنے پر منیجر کسی کو نکالے بغیر نیا کمرہ کیسے خالی کر لیتا ہے؟",
        ["ہر کمرے کے مہمان کو اگلے کمرے (n کو n+1) میں منتقل کر کے، جس سے پہلا کمرہ نئے مہمان کے لیے بالکل خالی ہو جاتا ہے", "ہوٹل کی چھت پر نیا کمرہ بنا کر", "دو مہمانوں کو ایک بستر پر سلا کر", "ہوٹل کو الٹا گھما کر"],
        "ہر کمرے کے مہمان کو اگلے کمرے (n کو n+1) میں منتقل کر کے، جس سے پہلا کمرہ نئے مہمان کے لیے بالکل خالی ہو جاتا ہے",
        "چونکہ کمرے لامتناہی ہیں اس لیے کوئی آخری کمرہ نہیں ہوتا۔ پہلے والا دوسرے میں، دوسرا تیسرے میں جائے گا، اور کمرہ نمبر 1 باآسانی خالی ہو جائے گا۔ یہ لامتناہی ریاضی کا انوکھا اعجاز ہے۔"
    ),
    (
        "Why is predicting long-term weather beyond 10 to 14 days fundamentally impossible, even with infinitely fast supercomputers (the Butterfly Effect)?",
        ["Deterministic Chaos: nonlinear atmospheric dynamics exhibit sensitive dependence on initial conditions, where microscopic rounding errors amplify exponentially", "Computer fans disturb air currents", "Weather satellites run out of fuel", "Thermometers freeze in winter"],
        "Deterministic Chaos: nonlinear atmospheric dynamics exhibit sensitive dependence on initial conditions, where microscopic rounding errors amplify exponentially",
        "Edward Lorenz discovered that chaotic systems have positive Lyapunov exponents. Small perturbations Delta x_0 grow as Delta x_0 * exp(lambda * t), rapidly destroying predictive horizons.",
        "بٹر فلائی اثر اور موسم کا اندازہ (The Butterfly Effect & Chaos): دنیا کا تیز ترین سپر کمپیوٹر بھی دو ہفتے سے آگے کے موسم کی 100 فیصد درست پیش گوئی کیوں نہیں کر سکتا؟",
        ["طیورانہ انتشار (Deterministic Chaos): ہوا کے دباؤ کے حسابی مساوات میں معمولی ترین فرق بھی وقت کے ساتھ ضرب کھا کر نتائج کو مکمل الٹ پلٹ کر دیتا ہے", "کمپیوٹر کے پنکھے ہوا بگاڑتے ہیں", "سیٹلائٹ کا ایندھن ختم ہو جاتا ہے", "تھرمامیٹر سردی میں جم جاتے ہیں"],
        "طیورانہ انتشار (Deterministic Chaos): ہوا کے دباؤ کے حسابی مساوات میں معمولی ترین فرق بھی وقت کے ساتھ ضرب کھا کر نتائج کو مکمل الٹ پلٹ کر دیتا ہے",
        "جیسے برازیل میں تتلی کے پر ہلانے کا معمولی ارتعاش چند ہفتوں بعد ٹیکساس میں طوفان کا رخ بدل سکتا ہے۔ پیمائش کا معمولی ترین اعشاریہ بھی چند دنوں میں پیش گوئی کو مکمل ناکارہ بنا دیتا ہے۔"
    ),
    (
        "In the Three-Body Problem, why is there no general analytical mathematical closed-form equation to predict the exact motion of three gravitational bodies orbiting each other?",
        ["The system is non-integrable with insufficient conserved first integrals to constrain chaotic orbital phase space", "Gravity turns off between three bodies", "Planets collide and fuse instantly", "The speed of light varies near three masses"],
        "The system is non-integrable with insufficient conserved first integrals to constrain chaotic orbital phase space",
        "Henri Poincaré proved in 1887 that the general three-body problem lacks algebraic first integrals beyond energy, momentum, and angular momentum, leading to homoclinic tangles and deterministic chaos.",
        "تین اجسام کا مسئلہ (The Three-Body Problem): کشش ثقل میں ایک دوسرے کے گرد گھومتے تین سیاروں کے مستقبل کے راستے کا کوئی حتمی ریاضیاتی فارمولا کیوں نہیں ہے؟",
        ["یہ نظام غیر مربوط (Non-integrable) ہے اور اس کی حسابی پیچیدگی میں راستے انتشار اور بے ترتیبی (Chaos) کا شکار ہو کر غیر متوقع ہو جاتے ہیں", "تین اجسام کے درمیان کشش ثقل بند ہو جاتی ہے", "سیارے فوراً آپس میں ٹکرا جاتے ہیں", "تین اجسام کے قریب روشنی کی رفتار بدل جاتی ہے"],
        "یہ نظام غیر مربوط (Non-integrable) ہے اور اس کی حسابی پیچیدگی میں راستے انتشار اور بے ترتیبی (Chaos) کا شکار ہو کر غیر متوقع ہو جاتے ہیں",
        "دو سیاروں کا راستہ نیوٹن کے فارمولے سے کمال حل ہو جاتا ہے، مگر جیسے ہی تیسرا سیارہ داخل ہوتا ہے، تینوں کی کشش ایک دوسرے کو اس قدر بے ترتیب جھٹکے دیتی ہے کہ حل صرف عددی اندازوں سے ہی ممکن رہتا ہے۔"
    ),
    (
        "Why did Henri Poincaré's Recurrence Theorem trouble classical thermodynamicists who believed in the irreversible Second Law of Thermodynamics?",
        ["Any closed Hamiltonian dynamical system with finite energy will eventually return arbitrarily close to its initial microstate given sufficient time", "Heat flows backwards in cold rooms", "Atoms evaporate into nothingness", "Molecules stop moving at equilibrium"],
        "Any closed Hamiltonian dynamical system with finite energy will eventually return arbitrarily close to its initial microstate given sufficient time",
        "Liouville's theorem ensures volume conservation in phase space. Poincaré proved almost every trajectory returns infinitely often near its initial point, implying broken eggs should eventually spontaneously reassemble.",
        "پوائنکارے کا مراجعت کا تھیورم (Poincaré Recurrence Theorem): کلاسیکی فزکس کا یہ قانون تھرمو ڈائنامکس کے اس اصول سے کیسے ٹکراتا ہے کہ گرمی اور اینٹروپی صرف ایک رخ پر بڑھتی ہے؟",
        ["ایک بند کمرے میں گیس کے تمام ایٹم کھربوں سالوں کے بعد گھوم پھر کر بالکل اپنی ابتدائی ترتیب پر دوبارہ واپس ضرور پہنچ جاتے ہیں", "ٹھنڈے کمرے میں گرمی الٹی بہتی ہے", "ایٹم غائب ہو جاتے ہیں", "مالیکیول حرکت کرنا چھوڑ دیتے ہیں"],
        "ایک بند کمرے میں گیس کے تمام ایٹم کھربوں سالوں کے بعد گھوم پھر کر بالکل اپنی ابتدائی ترتیب پر دوبارہ واپس ضرور پہنچ جاتے ہیں",
        "اگر وقت لامحدود ہو تو چائے میں گھل جانے والی چینی بھی کسی دن دوبارہ اچھل کر چمچ میں جمع ہو سکتی ہے۔ مگر اس واپسی کا متوقع وقت کائنات کی موجودہ عمر سے بھی کھربوں گنا زیادہ ہے۔"
    ),
    (
        "How did Rolf Landauer resolve the apparent thermodynamic paradox of Maxwell's Demon (Landauer's Principle)?",
        ["Erasing or resetting 1 bit of physical information in computer memory dissipates a minimum of k_B * T * ln(2) of heat into the environment", "The Demon dies of starvation", "Trapdoors freeze from air friction", "Molecules carry magnetic passwords"],
        "Erasing or resetting 1 bit of physical information in computer memory dissipates a minimum of k_B * T * ln(2) of heat into the environment",
        "Information is physical. While the Demon can sort molecules without work, erasing its internal memory of which molecules passed increases environmental entropy, perfectly preserving the Second Law.",
        "میکس ویل کا جن اور لینڈور کا اصول (Landauer's Principle & Maxwell's Demon): دروازہ کھول کر گرم اور ٹھنڈے مالیکیولز الگ کرنے والا فرضی جن تھرمو ڈائنامکس کے قانون کو کیوں نہیں توڑ سکتا؟",
        ["کمپیوٹر یا جن کے دماغ سے معلومات کا صرف 1 بٹ مٹانے کے لیے بھی ماحول میں حرارت (kT ln 2) خارج کرنا لازمی ہوتا ہے جو اینٹروپی کو متوازن کر دیتا ہے", "جن بھوک سے مر جاتا ہے", "دروازے ہوا کی رگڑ سے جام ہو جاتے ہیں", "مالیکیولز پر خفیہ کوڈ ہوتے ہیں"],
        "کمپیوٹر یا جن کے دماغ سے معلومات کا صرف 1 بٹ مٹانے کے لیے بھی ماحول میں حرارت (kT ln 2) خارج کرنا لازمی ہوتا ہے جو اینٹروپی کو متوازن کر دیتا ہے",
        "معلومات کوئی خیالی چیز نہیں بلکہ مادی حقیقت ہے۔ جب جن اپنی میموری خالی کرتا ہے تاکہ نئے مالیکیولز یاد رکھے، تو اس ڈیٹا کو مٹانے میں اتنی حرارت نکلتی ہے جو بچائی گئی توانائی کو برابر کر دیتی ہے۔"
    ),
    (
        "Why is the concept of a 'Boltzmann Brain' considered a reductio ad absurdum of certain cosmological fluctuation models?",
        ["Thermal fluctuations in a decaying universe are statistically far more likely to spontaneously assemble a single isolated brain with false memories than an entire cosmos", "Brains require oxygen tanks in space", "Skulls cannot withstand cosmic vacuum", "Neurons freeze below absolute zero"],
        "Thermal fluctuations in a decaying universe are statistically far more likely to spontaneously assemble a single isolated brain with false memories than an entire cosmos",
        "Ludwig Boltzmann noted entropy fluctuates. Spontaneously fluctuating a 1-kg brain with false memories requires far less entropy decrease (Delta S ~ 10^28) than fluctuating an entire 10^80 particle universe, threatening empirical observers.",
        "بولٹزمین برین کا معمہ (Boltzmann Brain Paradox): کائنات کے تھرمو ڈائنامک ماڈل میں یہ عجیب و غریب اور مضحکہ خیز نتیجہ کیوں نکلتا ہے؟",
        ["خلا کے بے ترتیب ایٹموں کے محض اتفاق سے جڑ کر جھوٹی یادوں والا ایک اکیلا دماغ بننے کا امکان پوری کائنات کے بننے کے امکان سے کھربوں گنا زیادہ ہے", "خلا میں دماغ کو آکسیجن سلنڈر چاہیے", "کھوپڑی خلا کا دباؤ نہیں سہہ سکتی", "نیورونز مطلق صفر پر جم جاتے ہیں"],
        "خلا کے بے ترتیب ایٹموں کے محض اتفاق سے جڑ کر جھوٹی یادوں والا ایک اکیلا دماغ بننے کا امکان پوری کائنات کے بننے کے امکان سے کھربوں گنا زیادہ ہے",
        "اگر کائنات خالص تھرمل اتار چڑھاؤ سے بنی ہے، تو آپ کا کمرہ، زمین اور اربوں کہکشائیں بننے کی بجائے خلا میں صرف ایک دماغ کا اتفاقیہ بن جانا کہیں آسان تھا۔ یہ مضحکہ خیزی ثابت کرتی ہے کہ کائناتی ماڈل میں کچھ گڑبڑ ہے۔"
    ),
    (
        "In the Anthropic Principle, why is our universe's physical constants (like the fine-structure constant and cosmological constant) exquisitely fine-tuned for carbon life?",
        ["Observational selection bias: only in universes where constants permit stable atoms and stars can conscious observers exist to ask the question", "God designed constants to match human DNA", "Planets vote on physical laws", "Gravity adjusts itself to match water"],
        "Observational selection bias: only in universes where constants permit stable atoms and stars can conscious observers exist to ask the question",
        "The Weak Anthropic Principle states that conditions observed in the universe must allow the observer to exist. If the strong force differed by 2%, carbon and oxygen could never synthesize in stellar nucleosynthesis.",
        "انسانی اصول اور کائناتی توازن (The Anthropic Principle): کائنات کے بنیادی قوانین اور ایٹمی قوتیں انسان اور زندگی کی بقا کے لیے اتنے حیرت انگیز اور باریک توازن پر کیوں سیٹ ہیں؟",
        ["مشاہداتی انتخاب کا اصول: ہم صرف ایسی ہی کائنات میں زندہ رہ کر یہ سوال پوچھ سکتے ہیں جس کے قوانین نے ایٹموں اور ستاروں کو بننے کی اجازت دی", "سیارے قوانین پر ووٹ دیتے ہیں", "کشش ثقل پانی کے مطابق بدلتی ہے", "خلا میں زندگی خود قوانین بناتی ہے"],
        "مشاہداتی انتخاب کا اصول: ہم صرف ایسی ہی کائنات میں زندہ رہ کر یہ سوال پوچھ سکتے ہیں جس کے قوانین نے ایٹموں اور ستاروں کو بننے کی اجازت دی",
        "اگر ایٹمی طاقت 2 فیصد مختلف ہوتی تو نہ ستارے بنتے نہ کاربن۔ ہم حیران اس لیے ہیں کیونکہ جن اربوں ممکنہ کائناتوں میں یہ توازن نہیں تھا، وہاں کوئی دیکھنے اور حیران ہونے والا پیدا ہی نہیں ہو سکا۔"
    ),
    (
        "In solutions to the Fermi Paradox, what terrifying premise is proposed by the 'Dark Forest Hypothesis' (Liu Cixin)?",
        ["All interstellar civilizations maintain total radio silence and eliminate any detected civilization preemptively to ensure self-survival in a resource-scarce universe", "Alien stars are shrouded in dark nebulae", "Alien civilizations sleep through cosmic winters", "Space is too dark for optical cameras"],
        "All interstellar civilizations maintain total radio silence and eliminate any detected civilization preemptively to ensure self-survival in a resource-scarce universe",
        "With chains of suspicion and technological explosions, communicating poses existential risk. The optimal game-theoretic survival strategy is to stay hidden and instantly annihilate any civilization that reveals its location.",
        "تاریک جنگل کا نظریہ (The Dark Forest Hypothesis): فرمی پیراڈاکس کا یہ خوفناک حل کیا بتاتا ہے کہ خلائی مخلوق زمین پر کوئی ریڈیو سگنل کیوں نہیں بھیجتی؟",
        ["تمام کہکشانی تہذیبیں شکار ہونے کے خوف سے خاموش چھپی ہوئی ہیں اور اپنے تحفظ کے لیے سامنے آنے والی کسی بھی نئی تہذیب کو فوری تباہ کرنا ہی محفوظ ترین راستہ سمجھتی ہیں", "خلائی ستارے کالے بادلوں میں چھپے ہیں", "خلائی مخلوق سردیوں میں سو جاتی ہے", "خلا کیمروں کے لیے بہت اندھیری ہے"],
        "تمام کہکشانی تہذیبیں شکار ہونے کے خوف سے خاموش چھپی ہوئی ہیں اور اپنے تحفظ کے لیے سامنے آنے والی کسی بھی نئی تہذیب کو فوری تباہ کرنا ہی محفوظ ترین راستہ سمجھتی ہیں",
        "کائنات ایک اندھے جنگل کی طرح ہے جہاں ہر تہذیب بندوق تانے چھپی بیٹھی ہے۔ اگر کوئی کیمپ فائر جلا کر آواز دے گا، تو دوسرے شکاری اپنے دفاع کے لیے اسے پلک جھپکنے میں گولی مار دیں گے۔"
    ),
    (
        "What is a 'Matrioshka Brain' in advanced speculative megastructure engineering?",
        ["A nested series of Dyson spheres surrounding a star, powering a colossal nested supercomputer using stellar radiation at cascading temperatures", "A synthetic neural network grown inside a moon", "A biological brain cloned from dinosaur DNA", "A supercomputer buried in volcanic magma"],
        "A nested series of Dyson spheres surrounding a star, powering a colossal nested supercomputer using stellar radiation at cascading temperatures",
        "Robert Bradbury proposed powering computation via stellar energy: the innermost Dyson shell captures star light at high temperature, radiating waste heat to outer shells at lower temperatures, maximizing thermodynamic computational efficiency.",
        "ماتریوشکا برین (Matrioshka Brain Megastructure): ستاروں کی توانائی سے چلنے والا یہ دیوہیکل کائناتی سپر کمپیوٹر کس طرح کام کرتا ہے؟",
        ["ستارے کے گرد تہوں در تہوں لپٹے ہوئے ڈائیسن اسفیئرز جو ستارے کی تمام حرارت اور روشنی کو مختلف درجہ حرارت پر استعمال کر کے کھربوں حسابات کرتے ہیں", "چاند کے اندر اگایا گیا حیاتیاتی دماغ", "ڈائنوسار کا کلون شدہ کمپیوٹر", "آتش فشاں میں دبا ہوا پروسیسر"],
        "ستارے کے گرد تہوں در تہوں لپٹے ہوئے ڈائیسن اسفیئرز جو ستارے کی تمام حرارت اور روشنی کو مختلف درجہ حرارت پر استعمال کر کے کھربوں حسابات کرتے ہیں",
        "روسی گڑیوں کی طرح ایک خول کے اندر دوسرا خول ہوتا ہے۔ اندرونی خول ستارے کی تیز گرمی استعمال کرتا ہے اور اپنا فضلہ باہر والے خول کو پھینکتا ہے، جس سے پوری کہکشاں کا ڈیٹا ایک ستارے کی بھٹی پر چلایا جا سکتا ہے۔"
    ),
    (
        "Why does a theoretical Alcubierre Warp Drive require exotic matter with negative mass or negative energy density to travel faster than light?",
        ["To expand spacetime behind the starship and contract spacetime in front of it without violating local Special Relativity", "To cool spaceship engines to absolute zero", "To shield astronauts from micrometeorites", "To generate artificial oxygen in deep vacuum"],
        "To expand spacetime behind the starship and contract spacetime in front of it without violating local Special Relativity",
        "Miguel Alcubierre showed that contracting space ahead and expanding space behind allows a bubble to move at arbitrary coordinate speeds. General Relativity requires negative energy density (T_00 < 0) to sustain the warp metric.",
        "الکوبیرے وارپ ڈرائیو (Alcubierre Warp Drive): روشنی سے تیز سفر کرنے والے اس نظریاتی جہاز کو منفی توانائی یا منفی مادے کی ضرورت کیوں ہوتی ہے؟",
        ["جہاز کے آگے کی خلا کو سکیڑنے اور پیچھے کی خلا کو پھیلانے کے لیے، تاکہ جہاز اپنی جگہ ساکن رہ کر بھی خلا کی لہر پر سوار ہو کر تیر سکے", "انجن کو مطلق صفر پر ٹھنڈا کرنے کے لیے", "شہابیوں سے جہاز کو بچانے کے لیے", "خلا میں آکسیجن بنانے کے لیے"],
        "جہاز کے آگے کی خلا کو سکیڑنے اور پیچھے کی خلا کو پھیلانے کے لیے، تاکہ جہاز اپنی جگہ ساکن رہ کر بھی خلا کی لہر پر سوار ہو کر تیر سکے",
        "خصوصی اضافیت کے تحت مادہ روشنی سے تیز نہیں چل سکتا، مگر خود خلا کے تانے بانے پر یہ پابندی نہیں۔ منفی توانائی کی چادر جہاز کے آگے کی جگہ کو لپیٹتی ہے جس سے وہ روشنی سے دس گنا تیز منزل پر پہنچ سکتا ہے۔"
    ),
    (
        "Why is building a Space Elevator tether from Earth's equator to geostationary orbit physically impossible with ordinary high-strength structural steel?",
        ["Steel's tensile-strength-to-density ratio is far too low; the cable would snap under its own immense gravitational and centrifugal weight", "Steel melts from lightning strikes in the stratosphere", "Earth's magnetic field repels steel cables", "Meteors oxidize iron in the exosphere"],
        "Steel's tensile-strength-to-density ratio is far too low; the cable would snap under its own immense gravitational and centrifugal weight",
        "A 36,000-kilometer tether requires a breaking length exceeding Earth's radius. Steel's tensile strength (~1-2 GPa) yields a taper ratio of 10^33, requiring materials like carbon nanotubes (>60 GPa).",
        "خلائی لفٹ اور اسٹیل کا تار (Space Elevator Cable Tensile Limit): زمین سے 36 ہزار کلومیٹر اونچے مدار تک خلائی لفٹ کا تار مضبوط ترین اسٹیل سے بنانا ناممکن کیوں ہے؟",
        ["اسٹیل کی کثافت کے مقابلے میں کھنچاؤ برداشت کرنے کی طاقت اتنی کم ہے کہ تار اپنے ہی کائناتی وزن کے بوجھ سے ٹوٹ جائے گا", "اسٹیل آسمانی بجلی سے پگھل جائے گا", "زمین کی مقناطیسیت تار کو دھکیلتی ہے", "شہابیے لوہے کو زنگ لگا دیتے ہیں"],
        "اسٹیل کی کثافت کے مقابلے میں کھنچاؤ برداشت کرنے کی طاقت اتنی کم ہے کہ تار اپنے ہی کائناتی وزن کے بوجھ سے ٹوٹ جائے گا",
        "اتنی لمبی رسی کو اپنے اور مدار کے سینٹری فیوگل کھچاؤ کو سنبھالنا ہوتا ہے۔ اگر اسٹیل استعمال کیا جائے تو رسی کو اتنی موٹی کرنا پڑے گا کہ اس کا وزن پوری دنیا کے لوہے سے بھی بڑھ جائے گا۔ صرف کاربن نینو ٹیوبز ہی یہ بوجھ اٹھا سکتی ہیں۔"
    ),
]
