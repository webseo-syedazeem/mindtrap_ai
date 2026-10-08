# -*- coding: utf-8 -*-
"""
Normal Extra Part 1 (82 items: Items 1 to 82)
Forensics, detective mysteries, and applied real-world physics.
8-tuple format: (q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

ITEMS = [
    # 1: Soot on rug from chimney burglar
    (
        "A detective investigates a burglary in an antique mansion with all windows and doors bolted securely from inside. What fireplace floor clue proves the entry point?",
        ["Soot particles and chimney mortar crumbs scattered across the hearth rug directly beneath the open flue", "Ashes were hot", "Firewood was dry", "Smoke was rising"],
        "Soot particles and chimney mortar crumbs scattered across the hearth rug directly beneath the open flue",
        "Climbing down an interior fireplace chimney dislodges chimney creosote soot deposits onto the hearthstone below.",
        "ایک قدیم حویلی میں چوری ہوئی جہاں تمام کھڑکیاں اور دروازے اندر سے بند تھے۔ آتش دان کے فرش پر کیا ثبوت ملا؟",
        ["آتش دان کے فرش پر چمنی کی کالک اور باریک پلستر کے ذرات بکھرے ہوئے تھے جس سے چمنی کا راستہ ظاہر ہوا", "راکھ گرم تھی", "لکڑیاں خشک تھیں", "دھواں اٹھ رہا تھا"],
        "آتش دان کے فرش پر چمنی کی کالک اور باریک پلستر کے ذرات بکھرے ہوئے تھے جس سے چمنی کا راستہ ظاہر ہوا",
        "چمنی کے اندر سے نیچے اترتے وقت دیواروں سے کالک لازمی نیچے گرتی ہے جو اندر آنے کا راستہ ثابت کرتی ہے۔"
    ),
    # 2: Forged check microprinting flaws
    (
        "How do forensic bank document examiners identify a counterfeit cashier's check printed on a modern desktop color laser printer?",
        ["Magnification reveals the fine microprinted security border line is blurred and rasterized into dot matrices rather than solid text", "Counterfeit ink is darker", "The paper is too light", "The watermark is printed upside down"],
        "Magnification reveals the fine microprinted security border line is blurred and rasterized into dot matrices rather than solid text",
        "Authentic bank notes utilize intaglio steel-die presses with microscopic legibility; laser printers render microtext as jagged dot pixels.",
        "بینک کے ماہرین جدید کلر پرنٹر سے چھاپے گئے جعلی چیک کو خوردبین سے کیسے فوراً پہچان لیتے ہیں؟",
        ["باریک مائیکرو پرنٹنگ کی حفاظتی لکیر حروف کے بجائے نقطوں اور دھبوں میں بدلی نظر آتی ہے", "سیاہی زیادہ کالی ہوتی ہے", "کاغذ بہت ہلکا ہوتا ہے", "واٹر مارک الٹا ہوتا ہے"],
        "باریک مائیکرو پرنٹنگ کی حفاظتی لکیر حروف کے بجائے نقطوں اور دھبوں میں بدلی نظر آتی ہے",
        "اصلی چیک پر باریک حفاظتی الفاظ واضح لکھے ہوتے ہیں جبکہ عام پرنٹر انہیں باریک نقطوں میں چھاپتا ہے۔"
    ),
    # 3: Fire puddle shape v-pattern accelerant
    (
        "How do arson forensic investigators prove that a residential living room fire was ignited using poured liquid gasoline?",
        ["Irregular puddle-shaped downward burn patterns and char lines beneath baseboards where liquid fuel pooled", "The room was completely burned", "The smoke smelled of wood", "The roof collapsed inward"],
        "Irregular puddle-shaped downward burn patterns and char lines beneath baseboards where liquid fuel pooled",
        "Ignitable liquid accelerants flow into lowest floor cracks, creating distinctive irregular pour borders with localized floor charring.",
        "آگ کے حادثات کی تفتیش کرنے والی ٹیم کیسے ثابت کرتی ہے کہ کمرے میں جان بوجھ کر پیٹرول چھڑک کر آگ لگائی گئی تھی؟",
        ["فرش پر پیٹرول کے بہاؤ اور تلچھٹ کی بے ترتیب جلی ہوئی لکیریں اور گہرے تالاب نما نشانات پائے گئے", "کمرہ پورا جل گیا تھا", "دھوئیں میں لکڑی کی بو تھی", "چھت اندر گر گئی تھی"],
        "فرش پر پیٹرول کے بہاؤ اور تلچھٹ کی بے ترتیب جلی ہوئی لکیریں اور گہرے تالاب نما نشانات پائے گئے",
        "پیٹرول فرش پر جہاں جہاں بہتا ہے وہاں لکڑی کے اندر تک جلنے کے خاص گڑھے اور نشانات چھوڑ جاتا ہے۔"
    ),
    # 4: Bullet ricochet angle shooter kneeling
    (
        "A bullet ricochet mark on a plastered hallway wall angles upward toward the ceiling at twenty degrees. What does this ballistics angle establish about the shooter?",
        ["The firearm was fired from a low elevation near the floor, indicating the shooter was crouching or kneeling", "The shooter was standing on a ladder", "The shooter fired through the roof", "The bullet bounced three times"],
        "The firearm was fired from a low elevation near the floor, indicating the shooter was crouching or kneeling",
        "Ballistics trajectory laser rods reconstruct bullet impact vectors backward to the geometric origin point of the muzzle.",
        "دیوار پر گولی لگنے اور اچھلنے کا نشان اوپر چھت کی طرف 20 درجے کے زاویے پر تھا۔ اس سے نشانہ باز کے متعلق کیا پتہ چلا؟",
        ["بندوق فرش کے قریب نیچے سے چلائی گئی تھی جس سے ظاہر ہوا کہ قاتل گھٹنوں کے بل جھکا ہوا تھا", "قاتل سیڑھی پر کھڑا تھا", "گولی چھت سے آئی تھی", "گولی تین بار اچھلی تھی"],
        "بندوق فرش کے قریب نیچے سے چلائی گئی تھی جس سے ظاہر ہوا کہ قاتل گھٹنوں کے بل جھکا ہوا تھا",
        "گولی کے ٹکرانے کا اوپر اٹھتا ہوا زاویہ ثابت کرتا ہے کہ بندوق کا رخ نیچے سے اوپر کی طرف تھا۔"
    ),
    # 5: Alibi disproved by TV sports rain delay
    (
        "A robbery suspect claims he was at home watching a live championship baseball game from 8:00 PM to 10:00 PM. How did the detective break his alibi?",
        ["The televised sports broadcast was rained out and postponed, replaced by old movie reruns at 8:05 PM", "The TV set was broken", "The suspect had no cable TV", "The TV was muted"],
        "The televised sports broadcast was rained out and postponed, replaced by old movie reruns at 8:05 PM",
        "Broadcast program logs verify real-time scheduling disruptions, catching suspects reciting unbroadcasted events.",
        "ملزم نے بیان دیا کہ وہ رات 8 سے 10 بجے تک لائیو کرکٹ میچ ٹی وی پر دیکھ رہا تھا۔ انسپکٹر نے اس کا جھوٹ کیسے پکڑا؟",
        ["بارش کی وجہ سے میچ 8:05 پر منسوخ ہو گیا تھا اور اس وقت پرانی فلم دکھائی جا رہی تھی", "ٹی وی خراب تھا", "کیبل کٹی ہوئی تھی", "ٹی وی کی آواز بند تھی"],
        "بارش کی وجہ سے میچ 8:05 پر منسوخ ہو گیا تھا اور اس وقت پرانی فلم دکھائی جا رہی تھی",
        "ٹی وی چینل کے ریکارڈ سے پتہ چلا کہ اس وقت میچ ہوا ہی نہیں تھا، ملزم کا من گھڑت بیان پکڑا گیا۔"
    ),
    # 6: Wet bathroom towel recent use
    (
        "A suspect claims he arrived home five minutes before police knocked on his door. Why does feeling the bath towel in his master bathroom disprove his statement?",
        ["The thick terrycloth bath towel is completely dry, but the shower floor drain is soaking wet with hot water", "The towel is folded neatly", "The soap is green", "The mirror is cold"],
        "The thick terrycloth bath towel is completely dry, but the shower floor drain is soaking wet with hot water",
        "Mismatched moisture timelines between absorbent cotton towels and hot water drain traps expose fabricated routines.",
        "ملزم نے کہا کہ وہ پولیس کے پہنچنے سے صرف 5 منٹ پہلے گھر آیا تھا اور نہایا نہیں تھا۔ باتھ روم سے کیا راز کھلا؟",
        ["تولیہ تو سوکھا تھا مگر شاور کے فرش پر گرم پانی کھڑا تھا اور پائپ سے گرم بھاپ نکل رہی تھی", "تولیہ استری تھا", "صابن کا رنگ ہرا تھا", "آئینہ ٹھنڈا تھا"],
        "تولیہ تو سوکھا تھا مگر شاور کے فرش پر گرم پانی کھڑا تھا اور پائپ سے گرم بھاپ نکل رہی تھی",
        "شاور کے گیلے پن اور گرمی نے ثابت کر دیا کہ ملزم تھوڑی دیر پہلے نہا کر کپڑے بدل چکا تھا۔"
    ),
    # 7: Chalk dust on burglar gloves
    (
        "A burglary suspect with zero criminal record is detained near a secondary school. What microscopic particulate found on his leather gloves links him to the crime scene?",
        ["Calcium carbonate school blackboard chalk dust matching the broken gymnasium window frame", "Pollen grains from roses", "Brick dust from chimneys", "Beach sand minerals"],
        "Calcium carbonate school blackboard chalk dust matching the broken gymnasium window frame",
        "Trace chemical spectroscopy links mineral particulates on suspects to distinct environmental transfer points.",
        "اسکول میں چوری کے بعد پکڑے گئے مشتبہ شخص کے چمڑے کے دستانوں سے کیا اہم کیمیائی ثبوت ملا؟",
        ["دستانوں پر جمی کیلشیم کاربونیٹ چاک کی دھول جو کلاس روم کی ٹوٹی کھڑکی کے چاک سے ہو بہو مل گئی", "گلاب کے زردانے", "چمنی کی اینٹ کی مٹی", "ساحل کی ریت"],
        "دستانوں پر جمی کیلشیم کاربونیٹ چاک کی دھول جو کلاس روم کی ٹوٹی کھڑکی کے چاک سے ہو بہو مل گئی",
        "لیبارٹری ٹیسٹ نے دستانوں پر لگی باریک چاک کی دھول کو جائے وقوعہ کے بلیک بورڈ چاک سے ملا دیا۔"
    ),
    # 8: Poison eye drops conjunctival absorption
    (
        "An executive dies of cardiac arrest with zero poisons detected in his stomach contents or bloodstream injection marks. How was aconite toxin administered?",
        ["Through his daily prescription eye drops, absorbed directly through conjunctival mucous membranes", "Through poisoned soap", "Through inhaled incense", "Through a poisoned watch strap"],
        "Through his daily prescription eye drops, absorbed directly through conjunctival mucous membranes",
        "Conjunctival sac capillary absorption bypasses first-pass hepatic metabolism, delivering potent cardio-toxins rapidly into the bloodstream.",
        "ایک افسر دل کا دورہ پڑنے سے ہلاک ہوا، معدے میں زہر نہیں تھا اور جسم پر کوئی انجکشن کا نشان نہ تھا۔ زہر کیسے پہنچا؟",
        ["آنکھ کے روزانہ ڈالنے والے ڈراپس میں زہر ملا دیا گیا تھا جو آنکھ کی باریک رگوں سے فوراً خون میں چلا گیا", "زہریلے صابن سے", "خوشبو کی دھونی سے", "گھڑی کے فیتے سے"],
        "آنکھ کے روزانہ ڈالنے والے ڈراپس میں زہر ملا دیا گیا تھا جو آنکھ کی باریک رگوں سے فوراً خون میں چلا گیا",
        "آنکھ کا پردہ باریک خون کی نالیوں کا جال ہوتا ہے، زہریلے قطرے معدے میں جائے بغیر خون میں شامل ہو گئے۔"
    ),
    # 9: Rock thrown from outside inward glass shards
    (
        "A store owner claims a competitor threw a stone from the sidewalk through his window. The investigator notes glass fragments inside and outside. What confirms the stone came from outside?",
        ["Radial fracture lines develop on the opposite side of impact, projecting cone spalling inward into the store", "The stone was dirty", "The window pane was tinted", "The glass was tempered"],
        "Radial fracture lines develop on the opposite side of impact, projecting cone spalling inward into the store",
        "Impact tensile stresses generate expanding concentric Hertzian cone fractures propagating in the direction of projectile flight.",
        "دکان دار نے دعویٰ کیا کہ باہر سے کسی نے کھڑکی پر پتھر مار کر توڑا۔ ماہرین نے کیسے تصدیق کی کہ پتھر واقعی باہر سے آیا تھا؟",
        ["شیشے کے ٹوٹنے کے مخروطی دائرے اور ریشے اندر کی طرف پھیلے ہوئے تھے جو بیرونی چوٹ کا ثبوت تھے", "پتھر پر مٹی لگی تھی", "شیشہ رنگین تھا", "شیشہ موٹا تھا"],
        "شیشے کے ٹوٹنے کے مخروطی دائرے اور ریشے اندر کی طرف پھیلے ہوئے تھے جو بیرونی چوٹ کا ثبوت تھے",
        "شیشہ جس طرف سے ٹوٹتا ہے اس کے برعکس رخ پر لکیروں کا جال پھیلتا ہے، اندر پھیلے جال نے بیرونی پتھر کی تصدیق کی۔"
    ),
    # 10: Watch set to wrong time zone travel alibi
    (
        "A globetrotting suspect claims he was asleep in his London flat at 3:00 AM local time. What finding on his mechanical wristwatch reveals he had just flown in from Tokyo?",
        ["His wristwatch was set exactly nine hours ahead, matching Tokyo local solar time (12:00 PM)", "His watch was broken", "The watch was made in Switzerland", "The strap was wet"],
        "His wristwatch was set exactly nine hours ahead, matching Tokyo local solar time (12:00 PM)",
        "Travelers often retain departure time zones on analog watches, betraying recent intercontinental flights.",
        "لندن میں قتل کے ملزم نے دعویٰ کیا کہ وہ رات کے 3 بجے اپنے فلیٹ پر سو رہا تھا۔ اس کی کلائی کی گھڑی نے ٹوکیو سے آنے کا راز کیسے کھولا؟",
        ["اس کی گھڑی لندن کے وقت سے ٹھیک 9 گھنٹے آگے تھی جو ٹوکیو کے مقامی وقت کے مطابق تھی", "گھڑی بند تھی", "گھڑی سوئس تھی", "پٹا گیلا تھا"],
        "اس کی گھڑی لندن کے وقت سے ٹھیک 9 گھنٹے آگے تھی جو ٹوکیو کے مقامی وقت کے مطابق تھی",
        "ملزم گھڑی کا ٹائم بدلنا بھول گیا تھا، گھڑی پر ٹوکیو کا وقت دیکھ کر تفتیش کار نے اس کے سفر کا سچ اگلوا لیا۔"
    ),
    # 11: Multiple fire origins arson proof
    (
        "Why does a municipal fire investigator immediately classify a commercial warehouse fire as intentional criminal arson?",
        ["Three separate, disconnected origin burn seats were located in separate storage bays with zero connecting wiring", "The building was made of wood", "The fire was extinguished fast", "The warehouse had no fire alarms"],
        "Three separate, disconnected origin burn seats were located in separate storage bays with zero connecting wiring",
        "Accidental structural fires begin at a single ignition point; multiple unconnected seats prove deliberate incendiary placement.",
        "فائر بریگیڈ کے تفتیش کار نے گودام کی آگ کو حادثے کے بجائے دانستہ لگائی گئی مجرمانہ آگ کیوں قرار دیا؟",
        ["تین مختلف الگ الگ کمروں میں بیک وقت آگ کے آزاد مراکز پائے گئے جن کا آپس میں کوئی برقی رابطہ نہ تھا", "عمارت لکڑی کی تھی", "آگ جلدی بجھ گئی تھی", "الارم نہیں بجا تھا"],
        "تین مختلف الگ الگ کمروں میں بیک وقت آگ کے آزاد مراکز پائے گئے جن کا آپس میں کوئی برقی رابطہ نہ تھا",
        "قدرتی آگ ایک ہی جگہ سے شروع ہوتی ہے، تین مختلف کونوں سے بیک وقت آگ لگنا کھلا ثبوت تھا کہ آگ جان بوجھ کر لگائی گئی۔"
    ),
    # 12: Footprints in snow filled with fresh flakes
    (
        "A robbery occurred between 11:00 PM and 3:00 AM while gentle snow fell steadily. The suspect's boot prints have one inch of fresh snow covering them. When did he leave?",
        ["Closer to 11:00 PM, allowing several hours of snowfall accumulation inside the tracks", "At exactly 3:00 AM", "The next morning", "He never left"],
        "Closer to 11:00 PM, allowing several hours of snowfall accumulation inside the tracks",
        "Snow accumulation rates inside shoe impressions provide a natural stratigraphic timeline of departure.",
        "رات 11 سے صبح 3 بجے تک ہلکی برفباری جاری تھی۔ چور کے پاؤں کے گڑھوں کے اندر ایک انچ تازہ برف جمی ہوئی تھی۔ وہ کب بھاگا تھا؟",
        ["رات 11 بجے کے قریب، تاکہ گھنٹوں کی برفباری ان قدموں کے اندر جمع ہو سکے", "ٹھیک 3 بجے", "اگلی صبح", "وہ گیا ہی نہیں تھا"],
        "رات 11 بجے کے قریب، تاکہ گھنٹوں کی برفباری ان قدموں کے اندر جمع ہو سکے",
        "قدموں کے اندر اتنی موٹی برف جمنا ظاہر کرتا ہے کہ وہ واردات کے شروع میں ہی نکل گیا تھا اور برف اس پر گرتی رہی۔"
    ),
    # 13: Safe combination scratched in hidden drawer
    (
        "A bank manager claims an armed robber forced him at gunpoint to reveal the vault combination code. Why does the detective suspect inside collusion?",
        ["The combination digits were found lightly inscribed on the underside of the manager's pull-out desk drawer", "The safe was empty", "The alarm was silent", "The vault door was open"],
        "The combination digits were found lightly inscribed on the underside of the manager's pull-out desk drawer",
        "Physical inscribed aids reveal premeditated information storage accessible to internal staff.",
        "بینک منیجر نے کہا کہ ڈاکوؤں نے بندوق کے زور پر تجوری کا خفیہ کوڈ اگلوا لیا۔ تفتیش کار کو منیجر پر شک کیوں ہوا؟",
        ["خفیہ کوڈ منیجر کی میز کی دراز کے نچلے حصے پر باریک لکھا ہوا ملا جس سے اندرونی سازش پکڑی گئی", "تجوری خالی تھی", "الارم بند تھا", "دروازہ کھلا تھا"],
        "خفیہ کوڈ منیجر کی میز کی دراز کے نچلے حصے پر باریک لکھا ہوا ملا جس سے اندرونی سازش پکڑی گئی",
        "دراز کے خفیہ پیندے پر کوڈ کا لکھا ہونا ثابت کر گیا کہ منیجر پہلے ہی سے واردات کی تیاری کر رہا تھا۔"
    ),
    # 14: Forged signature line hesitation tremors
    (
        "How does a forensic handwriting document expert prove a signed signature on a contract was forged by freehand tracing?",
        ["Magnification shows microscopic pen hesitations, blunt pen lifts, and uniform speed tremors lacking natural ballistic strokes", "The ink color was blue", "The signature was too small", "The paper was wrinkled"],
        "Magnification shows microscopic pen hesitations, blunt pen lifts, and uniform speed tremors lackluster of natural ballistic strokes",
        "Genuine signatures display fluent ballistic acceleration and tapered endings; tracing exhibits slow, tremulous drawing strokes.",
        "دستاویزات کے ماہر نے کیسے ثابت کیا کہ معاہدے پر کیا گیا دستخط کسی دوسرے شخص نے نقل کر کے جعلی بنایا تھا؟",
        ["خوردبین سے قلم کے رکنے، کانپنے اور بار بار اٹھائے جانے کے نشانات نظر آئے جو قدرتی روانی کے خلاف تھے", "سیاہی نیلی تھی", "دستخط چھوٹا تھا", "کاغذ مڑا ہوا تھا"],
        "خوردبین سے قلم کے رکنے، کانپنے اور بار بار اٹھائے جانے کے نشانات نظر آئے جو قدرتی روانی کے خلاف تھے",
        "انسان کا اپنا دستخط تیز روانی سے ہوتا ہے، جب کوئی دوسرا نقل کرتا ہے تو قلم سست چلتا ہے اور کپکپاہٹ آ جاتی ہے۔"
    ),
    # 15: Gunshot residue on shooter hand barium antimony
    (
        "What chemical scanning electron microscopy test proves a suspect fired a firearm within the past two hours?",
        ["Detecting fused spherical microscopic particles of lead, barium, and antimony on the webbing of the thumb and forefinger", "Testing for gunpowder scent", "Checking for hand blisters", "Measuring skin temperature"],
        "Detecting fused spherical microscopic particles of lead, barium, and antimony on the webbing of the thumb and forefinger",
        "Primer discharge vaporizes lead styphnate, barium nitrate, and antimony sulfide, condensing into distinctive microscopic spheroids on the shooter's hand.",
        "لیبارٹری ٹیسٹ سے کیسے ثابت ہوا کہ ملزم نے پچھلے دو گھنٹوں کے دوران خود اپنے ہاتھ سے پستول سے گولی چلائی تھی؟",
        ["انگوٹھے اور شہادت کی انگلی کے جوڑ پر سیسہ، بیریم اور اینٹیمنی کے باریک بارودی نینو ذرات چپکے ہوئے پائے گئے", "بارود کی خوشبو سونگھ کر", "ہاتھ پر چھالے دیکھ کر", "جلد کی گرمی ناپ کر"],
        "انگوٹھے اور شہادت کی انگلی کے جوڑ پر سیسہ، بیریم اور اینٹیمنی کے باریک بارودی نینو ذرات چپکے ہوئے پائے گئے",
        "فائر کرتے وقت پستول سے بارود کی دھاتی گیس ہاتھ پر جم جاتی ہے، یہ کیمیائی ٹیسٹ گولی چلانے والے کو فوراً بے نقاب کرتا ہے۔"
    ),
    # 16: Car radiator cold from severed hose
    (
        "A driver claims his car engine overheated accidentally and caught fire on the highway. What radiator inspection proves sabotage?",
        ["The lower radiator coolant hose had a clean razor blade slice mark rather than a jagged burst pressure rupture", "The coolant was green", "The radiator had bugs on it", "The fan belt was tight"],
        "The lower radiator coolant hose had a clean razor blade slice mark rather than a jagged burst pressure rupture",
        "Mechanical sabotage produces sharp planar incision kerfs; hydraulic overpressure failure tears ragged tensile blowouts.",
        "ڈرائیور نے دعویٰ کیا کہ ہائی وے پر گاڑی کا انجن خود بخود گرم ہو کر پھٹ گیا۔ تفتیش کار نے جان بوجھ کر کی گئی سازش کیسے پکڑی؟",
        ["ریڈی ایٹر کے نچلے پائپ پر تیز دھار بلیڈ سے کٹا ہوا صاف نشان ملا نہ کہ دباؤ سے پھٹنے کا کھردرا نشان", "کولنٹ کا رنگ ہرا تھا", "جالی پر مکھیاں تھیں", "بیلٹ ٹائٹ تھی"],
        "ریڈی ایٹر کے نچلے پائپ پر تیز دھار بلیڈ سے کٹا ہوا صاف نشان ملا نہ کہ دباؤ سے پھٹنے کا کھردرا نشان",
        "دباؤ سے پائپ پھٹے تو اس کے کنارے کھردرے ہوتے ہیں، بلیڈ کے صاف کٹ نے ثابت کیا کہ پائپ جان بوجھ کر کاٹا گیا تھا۔"
    ),
    # 17: Sprint stride length footprints
    (
        "Police track shoe impressions across wet sand. The distance between consecutive footprints suddenly expands from 2.5 feet to 6.5 feet. What occurred?",
        ["The individual transitioned abruptly from walking to a full sprint", "The individual was wearing stilts", "The individual jumped once", "The sand washed away"],
        "The individual transitioned abruptly from walking to a full sprint",
        "Stride length expands dramatically with forward velocity as the human gait cycle shifts into the double-float running phase.",
        "گیلی ریت پر پاؤں کے نشانات کے درمیان کا فاصلہ اچانک ڈھائی فٹ سے بڑھ کر ساڑھے چھ فٹ ہو گیا۔ تفتیش کار نے کیا سمجھا؟",
        ["چلنے والے شخص نے اچانک پوری طاقت سے دوڑنا شروع کر دیا تھا", "وہ لکڑی کی لمبی ٹانگوں پر تھا", "اس نے اونچی چھلانگ ماری تھی", "ریت بہہ گئی تھی"],
        "چلنے والے شخص نے اچانک پوری طاقت سے دوڑنا شروع کر دیا تھا",
        "دوڑتے وقت انسان کے ہر قدم کا فاصلہ دگنا سے زیادہ لمبا ہو جاتا ہے، جس سے تیز رفتار دوڑنے کا صاف ثبوت ملا۔"
    ),
    # 18: Bullet exit wound larger than entrance
    (
        "Why is a through-and-through bullet exit wound on a human body almost always significantly larger and more irregular than the entrance wound?",
        ["The projectile deforms, tumbles, and drags expanding cavitation tissue fragments outward as it exits", "The bullet gains speed inside the body", "Exit wounds heal slower", "Air pressure expands the wound"],
        "The projectile deforms, tumbles, and drags expanding cavitation tissue fragments outward as it exits",
        "Hydrodynamic drag yaws and mushrooms lead projectiles, transferring kinetic energy into a tearing, everted exit wound.",
        "گولی جسم سے جب پار ہو کر نکلتی ہے تو نکلنے کا سوراخ داخل ہونے والے سوراخ سے کہیں زیادہ بڑا اور پھٹا ہوا کیوں ہوتا ہے؟",
        ["گولی جسم کے اندر گھوم کر پھیل جاتی ہے اور ٹشوز کو دھکیلتے ہوئے باہر کا بڑا اور بے ڈھنگا سوراخ بناتی ہے", "گولی کی رفتار جسم کے اندر بڑھ جاتی ہے", "زخم دیر سے بھرتا ہے", "ہوا کا دباؤ سوراخ بڑا کرتا ہے"],
        "گولی جسم کے اندر گھوم کر پھیل جاتی ہے اور ٹشوز کو دھکیلتے ہوئے باہر کا بڑا اور بے ڈھنگا سوراخ بناتی ہے",
        "گولی جسم کے اندر ہڈیوں اور گوشت کی رگڑ سے چپٹی ہو جاتی ہے اور نکلتے ہوئے بڑے دہانے کے ساتھ گوشت چیر دیتی ہے۔"
    ),
    # 19: Poison in teabag string delayed dunking
    (
        "A tea drinker dies of poisoning while three guests sharing the exact same teapot remain unharmed. Forensic analysis finds the ceramic tea mug was clean. Where was the toxin applied?",
        ["Laced onto the woven cotton string of the single teabag, which poisoned only the mug where the bag was steeped", "The sugar was poisoned", "The spoon was poisoned", "The milk was spoiled"],
        "Laced onto the woven cotton string of the single teabag, which poisoned only the mug where the bag was steeped",
        "Capillary wicking draws dried toxins down the cotton string into hot tea water exclusively during manual steeping.",
        "ایک ہی کیتلی کی چائے پینے والے چار لوگوں میں سے صرف ایک شخص زہر سے مرا جبکہ اس کا کپ بھی صاف تھا۔ زہر کہاں لگایا گیا تھا؟",
        ["اس کے ٹی بیگ کے باریک سوت کے دھاگے پر زہر لگایا گیا تھا جو پانی میں ڈبونے پر اس کے کپ میں گھل گیا", "چینی میں زہر تھا", "چمچ زہریلا تھا", "دودھ خراب تھا"],
        "اس کے ٹی بیگ کے باریک سوت کے دھاگے پر زہر لگایا گیا تھا جو پانی میں ڈبونے پر اس کے کپ میں گھل گیا",
        "دھاگے میں جذب زہر گرم پانی میں ہلانے پر فورا نکل کر صرف اسی ایک کپ میں گیا، باقی کیتلی محفوظ رہی۔"
    ),
    # 20: Suicide note on company letterhead
    (
        "A corporate CEO is found dead in his apartment with an alleged suicide note. The detective immediately suspects murder. What typographic detail gave it away?",
        ["The note was printed using an office laser printer with watermarked company letterhead from a branch two hundred miles away", "The note was typed in English", "The CEO had no pen", "The note was too polite"],
        "The note was printed using an office laser printer with watermarked company letterhead from a branch two hundred miles away",
        "Paper stock and machine tracking yellow dots pinpoint the precise origin of printed fraudulent documents.",
        "سی ای او کے فلیٹ سے خودکشی کا خط ملا مگر تفتیش کار نے فوری قتل کا شبہ ظاہر کیا۔ کاغذ پر کیا خاص بات تھی؟",
        ["خط کمپنی کے ایسے واٹر مارک والے لیٹر پیڈ پر پرنٹ تھا جو دو سو میل دور کی برانچ میں استعمال ہوتا تھا", "خط انگریزی میں لکھا تھا", "سی ای او کے پاس قلم نہ تھا", "خط بہت شائستہ تھا"],
        "خط کمپنی کے ایسے واٹر مارک والے لیٹر پیڈ پر پرنٹ تھا جو دو سو میل دور کی برانچ میں استعمال ہوتا تھا",
        "کاغذ اور پرنٹر کے خفیہ ٹریکنگ ڈاٹس نے ثابت کر دیا کہ یہ خط دور بیٹھے حریف نے خود تیار کر کے لاش کے پاس رکھا تھا۔"
    ),
    # 21: Car exhaust blocked with potato carbon monoxide
    (
        "A driver is found dead inside a closed garage with the car engine running. What tailpipe inspection proves murder rather than suicide?",
        ["A raw potato was rammed deep into the tailpipe exhaust pipe, forcing exhaust fumes back into the vehicle cabin", "The gas tank was full", "The muffler was rusty", "The exhaust was warm"],
        "A raw potato was rammed deep into the tailpipe exhaust pipe, forcing exhaust fumes back into the vehicle cabin",
        "Occluding the exhaust manifold forces toxic carbon monoxide gases through cabin ventilation floor seams under backpressure.",
        "گیراج میں بند گاڑی کے اندر ڈرائیور کی دم گھٹنے سے لاش ملی۔ سائلنسر کے پائپ سے قتل کا کیا ثبوت ملا؟",
        ["سائلنسر کے اندر زبردستی کچا آلو ٹھونکا گیا تھا جس نے دھواں بلاک کر کے کار کے کیبن کے اندر بھر دیا تھا", "پیٹرول کا ٹینک بھرا تھا", "سائلنسر پر زنگ تھا", "دھواں گرم تھا"],
        "سائلنسر کے اندر زبردستی کچا آلو ٹھونکا گیا تھا جس سے دھواں بلاک ہو کر کار کے کیبن کے اندر بھر گیا تھا",
        "سائلنسر بند ہونے سے کاربن مونو آکسائیڈ گیس کیبن کی دراڑوں سے اندر گھس گئی اور ڈرائیور سوتے میں دم توڑ گیا۔"
    ),
    # 22: Fake kidnapping background train horn
    (
        "A father receives an audio recording of his kidnapped daughter weeping. Forensic acoustic experts pinpoint the hostage's location within miles. How?",
        ["Analyzing the unique acoustic frequency and schedule of a passing freight train horn blowing in the recording background", "Enhancing the girl's breath sounds", "Counting birds chirping", "Measuring room echo"],
        "Analyzing the unique acoustic frequency and schedule of a passing freight train horn blowing in the recording background",
        "Railway horn patterns and spatial Doppler curves match precise rail line junctions at recorded broadcast timestamps.",
        "اغوا کاروں نے مغوی لڑکی کی روتی ہوئی آڈیو بھیجی۔ فارنزک ماہرین نے لڑکی کے قید ہونے کی جگہ کا سراغ کیسے لگایا؟",
        ["آڈیو کے پس منظر میں دور سے گزرتی مال گاڑی کی سیٹی کی آواز اور شیڈول کے تجزیے سے مخصوص ریلوے لائن کا پتہ چلا", "لڑکی کے سانس کی آواز سے", "پرندوں کی آواز سن کر", "کمرے کی گونج ناپ کر"],
        "آڈیو کے پس منظر میں دور سے گزرتی مال گاڑی کی سیٹی کی آواز اور شیڈول کے تجزیے سے مخصوص ریلوے لائن کا پتہ چلا",
        "سیٹی کی خاص فریکوئنسی اور ٹرین کے ٹائم ٹیبل نے پولیس کو اس مخصوص ریلوے ٹریک کے پاس موجود ویران مکان تک پہنچا دیا۔"
    ),
    # 23: Driver door handle muddy passenger handle clean
    (
        "A car involved in a rural hit-and-run is found abandoned. Both passenger handles are clean, but the driver exterior handle is coated in loam. What does this tell police?",
        ["Only a single occupant operated the vehicle when fleeing across the muddy field", "The car had four passengers", "The driver wore clean gloves", "The car was washed in rain"],
        "Only a single occupant operated the vehicle when fleeing across the muddy field",
        "Differential soil contamination across vehicle contact points establishes single-occupant ingress/egress profiles.",
        "حادثے کے بعد چھوڑی گئی گاڑی کے تمام ہینڈل صاف تھے مگر ڈرائیور کی کھڑکی کا بیرونی ہینڈل کیچڑ سے لت پت تھا۔ اس سے کیا ثابت ہوا؟",
        ["واردات کے وقت گاڑی میں ڈرائیور اکیلا تھا اور کیچڑ سے بھاگ کر وہی اکیلا گاڑی میں بیٹھا تھا", "گاڑی میں چار لوگ تھے", "ڈرائیور کے دستانے صاف تھے", "گاڑی بارش میں دھلی تھی"],
        "واردات کے وقت گاڑی میں ڈرائیور اکیلا تھا اور کیچڑ سے بھاگ کر وہی اکیلا گاڑی میں بیٹھا تھا",
        "باقی دروازوں کا بالکل صاف ہونا ظاہر کرتا ہے کہ کوئی دوسرا سوار گاڑی میں موجود نہیں تھا۔"
    ),
    # 24: Folded spectacles on desk victim surprised
    (
        "An elderly scholar is discovered dead on his study floor. The detective observes his reading glasses neatly folded and sitting on his open textbook. What does this reveal?",
        ["The scholar had voluntarily set his glasses down, indicating he was not under violent attack when he left the desk", "The scholar was blind", "The room was in total disarray", "The glasses were broken"],
        "The scholar had voluntarily set his glasses down, indicating he was not under violent attack when he left the desk",
        "Orderly placement of delicate personal optical aids indicates calm, voluntary cessation of activity prior to an incident.",
        "کمرے میں بزرگ کی لاش فرش پر پڑی تھی مگر اس کا پڑھنے کا چشمہ میز پر کھلی کتاب پر صفائی سے تہہ کر کے رکھا تھا۔ اس سے کیا پتہ چلا؟",
        ["بزرگ پر اچانک پیچھے سے حملہ نہیں ہوا تھا بلکہ وہ پرسکون انداز میں خود چشمہ رکھ کر میز سے اٹھا تھا", "بزرگ نابینا تھا", "کمرے میں شدید توڑ پھوڑ ہوئی تھی", "چشمہ ٹوٹا ہوا تھا"],
        "بزرگ پر اچانک پیچھے سے حملہ نہیں ہوا تھا بلکہ وہ پرسکون انداز میں خود چشمہ رکھ کر میز سے اٹھا تھا",
        "اگر اچانک حملہ ہوتا تو چشمہ گر کر ٹوٹ جاتا، صفائی سے رکھنا ظاہر کرتا ہے کہ حملہ بعد میں ہوا جب وہ خود اٹھا۔"
    ),
    # 25: Jewelry store glass shattered inside
    (
        "A store owner claims thieves smashed his glass display case with a crowbar during the night. The investigator arrests the owner. What did the glass reveal?",
        ["Ninety percent of the glass shards were scattered on the display shelves rather than the floor, proving it was smashed from inside the counter", "The glass was bulletproof", "The crowbar was clean", "The store had motion sensors"],
        "Ninety percent of the glass shards were scattered on the display shelves rather than the floor, proving it was smashed from inside the counter",
        "Impact kinetic energy drives fragment dispersion in the vector of applied force; glass inside the counter indicates an interior strike.",
        "دکاندار نے کہا کہ چوروں نے رات کو شوکیس توڑا۔ تفتیش کار نے دکاندار کو ہی انشورنس فراڈ میں کیوں پکڑا؟",
        ["شیشے کے بیشتر ٹکڑے شوکیس کی شیلفوں کے اندر گرے تھے جس سے ثابت ہوا کہ ہتھوڑا اندر سے مارا گیا تھا", "شیشہ بلٹ پروف تھا", "ہتھوڑا صاف تھا", "دکان میں کیمرے لگے تھے"],
        "شیشے کے بیشتر ٹکڑے شوکیس کی شیلفوں کے اندر گرے تھے جس سے ثابت ہوا کہ ہتھوڑا اندر سے مارا گیا تھا",
        "اگر باہر سے ہتھوڑا مارا جاتا تو شیشہ نیچے فرش پر گرتا، اندر گرے شیشے نے خود دکاندار کا فراڈ بے نقاب کیا۔"
    ),
    # 26: Alibi reading newspaper during eclipse
    (
        "A murder suspect claims he was sitting on his front porch reading the newspaper in bright sunlight at 1:30 PM. Why does astronomy disprove his alibi?",
        ["A total solar eclipse blanketed the city in total nighttime darkness from 1:28 PM to 1:33 PM", "The sun never shines at 1:30 PM", "Newspapers are printed at night", "The porch was enclosed"],
        "A total solar eclipse blanketed the city in total nighttime darkness from 1:28 PM to 1:33 PM",
        "Solar eclipse totality ephemerides provide absolute celestial markers contradicting fabricated daylight alibis.",
        "ملزم نے بیان دیا کہ وہ دوپہر 1:30 بجے اپنے صحن میں تیز دھوپ میں بیٹھ کر اخبار پڑھ رہا تھا۔ ماہر فلکیات نے اسے جھوٹا کیسے ثابت کیا؟",
        ["اس وقت شہر پر سورج گرہن کی وجہ سے رات جیسا مکمل گھپ اندھیرا چھایا ہوا تھا", "دوپہر کو دھوپ نہیں ہوتی", "اخبار رات کو چھپتا ہے", "صحن بند تھا"],
        "اس وقت شہر پر سورج گرہن کی وجہ سے رات جیسا مکمل گھپ اندھیرا چھایا ہوا تھا",
        "مکمل سورج گرہن کے وقت دن میں رات کا سماں ہو گیا تھا، تیز دھوپ میں اخبار پڑھنے کا دعویٰ صریح جھوٹ تھا۔"
    ),
    # 27: Toll road ALPR automated photo
    (
        "A hit-and-run driver replaces his dented front bumper with a clean spare and claims his car was garaged all day. What highway camera catches him?",
        ["An automated license plate recognition camera captured his vehicle speeding through an express toll lane with a crushed bumper", "A satellite photographed him", "A police drone chased him", "A cell tower tracked him"],
        "An automated license plate recognition camera captured his vehicle speeding through an express toll lane with a crushed bumper",
        "High-speed infrared ALPR cameras record vehicle damage profiles and plate OCR data at timestamped toll gantries.",
        "گاڑی کے مالک نے ٹکر کے بعد ٹوٹا ہوا بمپر بدل کر دعویٰ کیا کہ اس کی گاڑی دن بھر گیراج میں تھی۔ پولیس نے کیسے پکڑا؟",
        ["ہائی وے کے ٹول پلازہ کے تیز رفتار کیمرے نے ٹوٹی ہوئی گاڑی کی ہائی ریزولوشن تصویر کھینچ رکھی تھی", "سیٹلائٹ نے دیکھا تھا", "ڈرون نے پیچھا کیا تھا", "موبائل ٹاور نے بتایا تھا"],
        "ہائی وے کے ٹول پلازہ کے تیز رفتار کیمرے نے ٹوٹی ہوئی گاڑی کی ہائی ریزولوشن تصویر کھینچ رکھی تھی",
        "ٹول گیٹ کے خودکار کیمرے کے ریکارڈ میں گاڑی کا نمبر اور ٹوٹا ہوا اگلا حصہ صاف محفوظ تھا۔"
    ),
    # 28: Letter postmark date precedes claimed writing date
    (
        "A blackmailer claims he only penned a threatening letter on June 15th in response to an insult. What postal detail exposes his premeditation?",
        ["The postal sorting cancellation postmark stamped across the envelope was dated June 12th", "The stamp was upside down", "The ink was red", "The letter had no address"],
        "The postal sorting cancellation postmark stamped across the envelope was dated June 12th",
        "Post office automated optical cancellation timestamps prove physical mailing dates preceding fabricated composition dates.",
        "بلیک میلر نے کہا کہ اس نے دھمکی آمیز خط 15 جون کو غصے میں لکھا تھا۔ ڈاک خانے کی مہر نے اس کی پہلے سے کی گئی سازش کیسے کھولی؟",
        ["لفافے پر ڈاک خانے کی لگی ہوئی سرکاری مہر 12 جون کی تھی یعنی خط پہلے ہی پوسٹ ہو چکا تھا", "ٹکٹ الٹا لگا تھا", "سیاہی لال تھی", "خط پر پتہ نہیں تھا"],
        "لفافے پر ڈاک خانے کی لگی ہوئی سرکاری مہر 12 جون کی تھی یعنی خط پہلے ہی پوسٹ ہو چکا تھا",
        "ڈاک کی مہر کا وقت خط پر لکھی تاریخ سے تین دن پہلے کا تھا، جس سے ثابت ہوا کہ سازش پہلے سے تیار تھی۔"
    ),
    # 29: Wet hair under dry wig
    (
        "A suspect in a marina boat theft claims he was asleep in his hotel room. What personal inspection by the detective exposes his recent swim?",
        ["Lifting his styled dry toupee wig reveals damp, chlorine-soaked hair underneath", "His fingernails were clean", "His shoes were polished", "He smelled of cologne"],
        "Lifting his styled dry toupee wig reveals damp, chlorine-soaked hair underneath",
        "Wearing a synthetic hairpiece traps water and swimming pool chemicals against scalp hair follicles, slowing evaporation.",
        "کشتی چوری کے ملزم نے کہا کہ وہ ہوٹل میں سو رہا تھا اور پانی کے قریب نہیں گیا۔ انسپکٹر نے اس کا تیرنا کیسے ثابت کیا؟",
        ["اس کی خشک نقلی وگ اٹھاتے ہی اس کے اپنے اصل بال گیلے اور کلورین والے پانی سے نم نکلے", "اس کے ناخن صاف تھے", "اس کے جوتے چمکدار تھے", "اس پر عطر لگا تھا"],
        "اس کی خشک نقلی وگ اٹھاتے ہی اس کے اپنے اصل بال گیلے اور کلورین والے پانی سے نم نکلے",
        "وگ کے نیچے قدرتی بال ہوا نہ لگنے کی وجہ سے گیلے رہ گئے تھے، جس نے اس کے پانی میں تیرنے کا بھانڈا پھوڑ دیا۔"
    ),
    # 30: Cold radiator in running car
    (
        "A driver claims he has been driving on the highway for two hours straight. The detective touches the front radiator grille and finds it freezing cold. What happened?",
        ["The water pump impeller failed or coolant leaked completely, leaving the radiator devoid of hot engine fluid", "The car was powered by solar cells", "The driver had air conditioning on", "Winter wind cooled the engine block"],
        "The water pump impeller failed or coolant leaked completely, leaving the radiator devoid of hot engine fluid",
        "Circulation loss prevents engine block heat from reaching front heat exchangers, leaving radiator cores ice-cold despite a boiling block.",
        "گاڑی کے ڈرائیور نے کہا کہ وہ پچھلے دو گھنٹے سے مسلسل تیز رفتاری سے گاڑی چلا رہا تھا۔ ریڈی ایٹر کی جالی برف جیسی ٹھنڈی کیوں نکلی؟",
        ["واٹر پمپ خراب ہونے سے یا کولنٹ لیک ہونے کی وجہ سے انجن کا گرم پانی ریڈی ایٹر تک پہنچ ہی نہیں رہا تھا", "گاڑی سولر پر چل رہی تھی", "اے سی چل رہا تھا", "سرد ہوا نے انجن ٹھنڈا کر دیا تھا"],
        "واٹر پمپ خراب ہونے سے یا کولنٹ لیک ہونے کی وجہ سے انجن کا گرم پانی ریڈی ایٹر تک پہنچ ہی نہیں رہا تھا",
        "پانی کی گردش رک جانے کی وجہ سے ریڈی ایٹر ٹھنڈا پڑا تھا جبکہ انجن اندر سے آگ بن کر جل رہا تھا۔"
    )
]

print(f"Normal Extra Part 1 loaded {len(ITEMS)} items.")
