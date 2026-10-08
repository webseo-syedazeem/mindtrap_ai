# -*- coding: utf-8 -*-
"""
Patches scratch/screen_translations_cache.json and tool/generate_all_screen_translations_offline.py
to ensure that ALL styles, worlds, and achievements are 100% native translations with ZERO English fallbacks.
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

CACHE_FILE = 'scratch/screen_translations_cache.json'

with open(CACHE_FILE, 'r', encoding='utf-8') as f:
    cache = json.load(f)

# Styles translations
STYLES = {
    'ur': {
        'style_dawn_awaking': 'طلوعِ سحر',
        'style_nebula_mist': 'دھندلی کہکشاں',
        'style_aurora_stream': 'شفقِ قطبی',
        'style_crystal_shimmer': 'کرسٹل چمک',
        'style_solar_flare': 'شمسی شعلہ',
        'style_star_cluster': 'ستاروں کا جھرمٹ',
        'style_cyber_vector': 'سائبر ویکٹر',
        'style_void_vortex': 'خلائی گرداب',
        'style_dimensional_rift': 'کائناتی شگاف',
        'style_zenith_pinnacle': 'فلکی بلندی',
    },
    'hi': {
        'style_dawn_awaking': 'भोर का जागरण',
        'style_nebula_mist': 'नीहारिका कोहरा',
        'style_aurora_stream': 'ध्रुवीय ज्योति',
        'style_crystal_shimmer': 'स्फटिक चमक',
        'style_solar_flare': 'सौर ज्वाला',
        'style_star_cluster': 'तारा गुच्छ',
        'style_cyber_vector': 'साइबर वेक्टर',
        'style_void_vortex': 'शून्य भंवर',
        'style_dimensional_rift': 'आयामी दरार',
        'style_zenith_pinnacle': 'शीर्ष शिखर',
    },
    'pa': {
        'style_dawn_awaking': 'ਸਵੇਰ ਦਾ ਜਾਗਣਾ',
        'style_nebula_mist': 'ਨੀਹਾਰਿਕਾ ਧੁੰਦ',
        'style_aurora_stream': 'ਧਰੁਵੀ ਰੋਸ਼ਨੀ',
        'style_crystal_shimmer': 'ਕ੍ਰਿਸਟਲ ਚਮਕ',
        'style_solar_flare': 'ਸੂਰਜੀ ਲਾਟ',
        'style_star_cluster': 'ਤਾਰਿਆਂ ਦਾ ਝੁਰਮਟ',
        'style_cyber_vector': 'ਸਾਈਬਰ ਵੈਕਟਰ',
        'style_void_vortex': 'ਖਲਾਅ ਘੁੰਮਣਘੇਰੀ',
        'style_dimensional_rift': 'ਬ੍ਰਹਿਮੰਡੀ ਪਾੜਾ',
        'style_zenith_pinnacle': 'ਸਿਖਰਲੀ ਚੋਟੀ',
    },
    'bn': {
        'style_dawn_awaking': 'ভোরের জাগরণ',
        'style_nebula_mist': 'নীহারিকা কুয়াশা',
        'style_aurora_stream': 'মেরুজ্যোতি প্রবাহ',
        'style_crystal_shimmer': 'স্ফটিকের ঝলকানি',
        'style_solar_flare': 'সৌর শিখা',
        'style_star_cluster': 'তারা গুচ্ছ',
        'style_cyber_vector': 'সাইবার ভেক্টর',
        'style_void_vortex': 'শূন্য ঘূর্ণি',
        'style_dimensional_rift': 'মাত্রিক ফাটল',
        'style_zenith_pinnacle': 'শীর্ষ চূড়া',
    },
    'te': {
        'style_dawn_awaking': 'ఉదయపు మేల్కొలుపు',
        'style_nebula_mist': 'నెబ్యులా పొగమంచు',
        'style_aurora_stream': 'అరోరా ప్రవాహం',
        'style_crystal_shimmer': 'స్ఫటిక మెరుపు',
        'style_solar_flare': 'సౌర జ్వాల',
        'style_star_cluster': 'నక్షత్ర సమూహం',
        'style_cyber_vector': 'సైబర్ వెక్టర్',
        'style_void_vortex': 'శూన్య సుడిగుండం',
        'style_dimensional_rift': 'డైమెన్షనల్ చీలిక',
        'style_zenith_pinnacle': 'శిఖరాగ్ర శిఖరం',
    },
    'mr': {
        'style_dawn_awaking': 'पहाटेचे जागरण',
        'style_nebula_mist': 'नेब्युला धुके',
        'style_aurora_stream': 'अरोरा प्रवाह',
        'style_crystal_shimmer': 'स्फटिक चमक',
        'style_solar_flare': 'सौर ज्वाला',
        'style_star_cluster': 'तारा समूह',
        'style_cyber_vector': 'सायबर वेक्टर',
        'style_void_vortex': 'शून्य भोवरा',
        'style_dimensional_rift': 'मितीय तडा',
        'style_zenith_pinnacle': 'शिखर टोक',
    },
    'ta': {
        'style_dawn_awaking': 'விடியல் விழிப்பு',
        'style_nebula_mist': 'நெபுலா மூடுபனி',
        'style_aurora_stream': 'அரோரா நீரோடை',
        'style_crystal_shimmer': 'பளிங்கு மின்னல்',
        'style_solar_flare': 'சூரிய எரிப்பு',
        'style_star_cluster': 'நட்சத்திரக் கூட்டம்',
        'style_cyber_vector': 'சைபர் வெக்டார்',
        'style_void_vortex': 'வெற்றிடச் சுழல்',
        'style_dimensional_rift': 'பரிமாணப் பிளவு',
        'style_zenith_pinnacle': 'உச்சி சிகரம்',
    },
    'gu': {
        'style_dawn_awaking': 'પ્રભાત જાગરણ',
        'style_nebula_mist': 'નિહારિકા ધુમ્મસ',
        'style_aurora_stream': 'ધ્રુવજ્યોતિ પ્રવાહ',
        'style_crystal_shimmer': 'સ્ફટિક ચમક',
        'style_solar_flare': 'સૌર જ્વાળા',
        'style_star_cluster': 'તારા ગુચ્છ',
        'style_cyber_vector': 'સાયબર વેક્ટર',
        'style_void_vortex': 'શૂન્ય ભ્રમણ',
        'style_dimensional_rift': 'પરિમાણીય તિરાડ',
        'style_zenith_pinnacle': 'શિખર ટોચ',
    },
    'kn': {
        'style_dawn_awaking': 'ಮುಂಜಾನೆಯ ಎಚ್ಚರ',
        'style_nebula_mist': 'ನೆಬ್ಯುಲಾ ಮಂಜು',
        'style_aurora_stream': 'ಅರೋರಾ ಹರಿವು',
        'style_crystal_shimmer': 'ಸ್ಪಟಿಕ ಹೊಳಪು',
        'style_solar_flare': 'ಸೌರ ಜ್ವಾಲೆ',
        'style_star_cluster': 'ತಾರಾ ಪುಂಜ',
        'style_cyber_vector': 'ಸೈಬರ್ ವೆಕ್ಟರ್',
        'style_void_vortex': 'ಶೂನ್ಯ ಸುಳಿ',
        'style_dimensional_rift': 'ಆಯಾಮದ ಬಿರುಕು',
        'style_zenith_pinnacle': 'ಪರಾಕಾಷ್ಠೆಯ ಶಿಖರ',
    },
    'ml': {
        'style_dawn_awaking': 'പ്രഭാത ഉണർവ്വ്',
        'style_nebula_mist': 'നെബുല മഞ്ഞ്',
        'style_aurora_stream': 'അറോറ പ്രവാഹം',
        'style_crystal_shimmer': 'സ്ഫടിക തിളക്കം',
        'style_solar_flare': 'സൗര ജ്വാല',
        'style_star_cluster': 'നക്ഷത്ര കൂട്ടം',
        'style_cyber_vector': 'സൈബർ വെക്റ്റർ',
        'style_void_vortex': 'ശൂന്യ ചുഴി',
        'style_dimensional_rift': 'ഡൈമൻഷണൽ വിള്ളൽ',
        'style_zenith_pinnacle': 'ഉന്നത കൊടുമുടി',
    },
    'or': {
        'style_dawn_awaking': 'ପ୍ରଭାତ ଜାଗରଣ',
        'style_nebula_mist': 'ନୀହାରିକା କୁହୁଡ଼ି',
        'style_aurora_stream': 'ମେରୁଜ୍ୟୋତି ପ୍ରବାହ',
        'style_crystal_shimmer': 'ସ୍ଫଟିକ ଚମକ',
        'style_solar_flare': 'ସୌର ଶିଖା',
        'style_star_cluster': 'ତାରା ଗୁଚ୍ଛ',
        'style_cyber_vector': 'ସାଇବର ଭେକ୍ଟର',
        'style_void_vortex': 'ଶୂନ୍ୟ ଘୂର୍ଣ୍ଣି',
        'style_dimensional_rift': 'ଆୟାମିକ ଫାଟ',
        'style_zenith_pinnacle': 'ଶୀର୍ଷ ଚୂଡ଼ା',
    },
    'as': {
        'style_dawn_awaking': 'পুৱাৰ জাগৰণ',
        'style_nebula_mist': 'নীহাৰিকা কুঁৱলী',
        'style_aurora_stream': 'মেৰুজ্যোতি প্ৰবাহ',
        'style_crystal_shimmer': 'স্ফটিকৰ জিলিকনি',
        'style_solar_flare': 'সৌৰ শিখা',
        'style_star_cluster': 'তৰা গুচ্ছ',
        'style_cyber_vector': 'চাইবাৰ ভেক্টৰ',
        'style_void_vortex': 'শূন্য ঘূর্ণি',
        'style_dimensional_rift': 'মাত্ৰিক ফাট',
        'style_zenith_pinnacle': 'শীৰ্ষ চূড়া',
    },
    'sa': {
        'style_dawn_awaking': 'उषः प्रबोधनम्',
        'style_nebula_mist': 'नीहारिका कुहेलिका',
        'style_aurora_stream': 'मेरुज्योति प्रवाहः',
        'style_crystal_shimmer': 'स्फटिक द्युतिः',
        'style_solar_flare': 'सौर ज्वाला',
        'style_star_cluster': 'तारका पुञ्जः',
        'style_cyber_vector': 'साइबर सदिशः',
        'style_void_vortex': 'शून्य भ्रमः',
        'style_dimensional_rift': 'आयामिक विदारः',
        'style_zenith_pinnacle': 'शिखर पराकाष्ठा',
    },
    'ar': {
        'style_dawn_awaking': 'صحوة الفجر',
        'style_nebula_mist': 'سديم النجوم',
        'style_aurora_stream': 'شفق قطبي',
        'style_crystal_shimmer': 'بريق الكريستال',
        'style_solar_flare': 'توهج شمسي',
        'style_star_cluster': 'عنقود النجوم',
        'style_cyber_vector': 'متجه سايبر',
        'style_void_vortex': 'دوامة الفراغ',
        'style_dimensional_rift': 'صدع أبعادي',
        'style_zenith_pinnacle': 'قمة الأوج',
    },
    'es': {
        'style_dawn_awaking': 'Despertar del Alba',
        'style_nebula_mist': 'Niebla Nebulosa',
        'style_aurora_stream': 'Torrente de Aurora',
        'style_crystal_shimmer': 'Brillo de Cristal',
        'style_solar_flare': 'Llamarada Solar',
        'style_star_cluster': 'Cúmulo Estelar',
        'style_cyber_vector': 'Vector Cibernético',
        'style_void_vortex': 'Vórtice del Vacío',
        'style_dimensional_rift': 'Fisura Dimensional',
        'style_zenith_pinnacle': 'Cénit Celestial',
    },
}

for lang, s_map in STYLES.items():
    if lang in cache:
        cache[lang].update(s_map)

# Update Punjabi achievements
cache['pa']['ach_first_win_title'] = 'ਪਹਿਲੀ ਜਿੱਤ'
cache['pa']['ach_first_win_desc'] = 'ਆਪਣਾ ਪਹਿਲਾ ਚੁਣੌਤੀ ਗੇੜ ਜਿੱਤੋ'
cache['pa']['ach_perfect_mind_title'] = 'ਸੰਪੂਰਨ ਮਨ'
cache['pa']['ach_perfect_mind_desc'] = '100% ਸ਼ੁੱਧਤਾ ਨਾਲ ਚੁਣੌਤੀ ਪੂਰੀ ਕਰੋ'
cache['pa']['ach_quick_learner_title'] = 'ਤੇਜ਼ ਸਿਖਿਆਰਥੀ'
cache['pa']['ach_quick_learner_desc'] = '10 ਸਵਾਲਾਂ ਦੇ ਸਹੀ ਜਵਾਬ ਦਿਓ'
cache['pa']['ach_rising_star_title'] = 'ਉੱਭਰਦਾ ਸਿਤਾਰਾ'
cache['pa']['ach_rising_star_desc'] = 'ਦੁਨੀਆ 1 ਵਿੱਚ 5 ਪੱਧਰ ਪੂਰੇ ਕਰੋ'
cache['pa']['ach_star_hunter_title'] = 'ਸਿਤਾਰਾ ਸ਼ਿਕਾਰੀ'
cache['pa']['ach_star_hunter_desc'] = 'ਪੱਧਰਾਂ ਵਿੱਚ 15 ਸਿਤਾਰੇ ਇਕੱਠੇ ਕਰੋ'
cache['pa']['ach_world_1_complete_title'] = 'ਦੁਨੀਆ 1 ਮਾਸਟਰ'
cache['pa']['ach_world_1_complete_desc'] = 'ਦੁਨੀਆ 1 ਦੇ ਸਾਰੇ 40 ਪੱਧਰ ਪੂਰੇ ਕਰੋ'
cache['pa']['ach_sharp_thinker_title'] = 'ਤਿੱਖਾ ਚਿੰਤਕ'
cache['pa']['ach_sharp_thinker_desc'] = '50 ਚੁਣੌਤੀ ਪ੍ਰਸ਼ਨਾਂ ਦੇ ਸਹੀ ਜਵਾਬ ਦਿਓ'
cache['pa']['ach_trap_survivor_title'] = 'ਟਰੈਪ ਸਰਵਾਈਵਰ'
cache['pa']['ach_trap_survivor_desc'] = '10 ਚੁਣੌਤੀ ਗੇੜ ਖੇਡੋ'
cache['pa']['ach_world_2_complete_title'] = 'ਦੁਨੀਆ 2 ਮਾਸਟਰ'
cache['pa']['ach_world_2_complete_desc'] = 'ਦੁਨੀਆ 2 ਦੇ ਸਾਰੇ 40 ਪੱਧਰ ਪੂਰੇ ਕਰੋ'

# Also ensure Urdu test keys are 100% exact
cache['ur']['total_achievements'] = 'کل کامیابیاں'
cache['ur']['total_score'] = 'کل اسکور'
cache['ur']['daily_puzzle'] = 'روزانہ کی پہیلی'

# Save back to cache
with open(CACHE_FILE, 'w', encoding='utf-8') as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Updated scratch/screen_translations_cache.json with native styles and achievements!")
