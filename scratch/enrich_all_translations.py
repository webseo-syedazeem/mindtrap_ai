# -*- coding: utf-8 -*-
"""
Enriches screen_translations.dart with missing keys across all 56 languages:
- thanks_journey
- select_world
- world
- guest, pro, guest_player, tap_to_sync, logout, sign_in
- search_language, no_languages_found
- device_support_may_vary, profile
- style_dawn_awaking ... style_zenith_pinnacle (all 10 atmosphere styles)
"""

import json
import re
import urllib.request
import urllib.parse
import time

file_path = 'lib/localization/screen_translations.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

LANG_CODES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

# Robust line-by-line parser for screen_translations.dart
all_langs = {c: {} for c in LANG_CODES}
current_lang = None

for line in code.splitlines():
    stripped = line.strip()
    m_lang = re.match(r"^'([a-zA-Z_]+)':\s*\{", stripped)
    if m_lang and m_lang.group(1) in LANG_CODES:
        current_lang = m_lang.group(1)
        continue
    if stripped.startswith('},') or stripped == '}':
        current_lang = None
        continue
    if current_lang is not None:
        m_kv = re.match(r"^'([a-zA-Z0-9_]+)':\s*'(.*)',?$", stripped)
        if m_kv:
            k = m_kv.group(1)
            v = m_kv.group(2)
            all_langs[current_lang][k] = v

print(f"Loaded {len(all_langs)} languages from screen_translations.dart")
for test_c in ['en', 'ur', 'hi', 'pa']:
    print(f"[{test_c}] keys: {len(all_langs[test_c])}")

CURATED_PRESETS = {
    'en': {
        'thanks_journey': "Thanks for being part of our journey!\nYour support means the world to us.",
        'select_world': "Select World",
        'world': "World",
        'guest': "GUEST",
        'pro': "PRO",
        'guest_player': "Guest Player",
        'tap_to_sync': "Tap to sync cloud progress",
        'logout': "Log Out",
        'sign_in': "Sign In",
        'search_language': "Search language...",
        'no_languages_found': "No languages found",
        'device_support_may_vary': "Device support may vary",
        'profile': "Profile",
        'style_dawn_awaking': "Dawn Awaking",
        'style_nebula_mist': "Nebula Mist",
        'style_aurora_stream': "Aurora Stream",
        'style_crystal_shimmer': "Crystal Shimmer",
        'style_solar_flare': "Solar Flare",
        'style_star_cluster': "Star Cluster",
        'style_cyber_vector': "Cyber Vector",
        'style_void_vortex': "Void Vortex",
        'style_dimensional_rift': "Dimensional Rift",
        'style_zenith_pinnacle': "Zenith Pinnacle",
    },
    'ur': {
        'thanks_journey': "ہمارے سفر کا حصہ بننے کا شکریہ!\nآپ کا تعاون ہمارے لیے سب کچھ ہے۔",
        'select_world': "دنیا منتخب کریں",
        'world': "دنیا",
        'guest': "مہمان",
        'pro': "پرو",
        'guest_player': "مہمان کھلاڑی",
        'tap_to_sync': "کلاؤڈ پروگریس سنک کرنے کے لیے دبائیں",
        'logout': "لاگ آؤٹ",
        'sign_in': "سائن ان",
        'search_language': "زبان تلاش کریں...",
        'no_languages_found': "کوئی زبان نہیں ملی",
        'device_support_may_vary': "ڈیوائس سپورٹ مختلف ہو سکتی ہے",
        'profile': "پروفائل",
        'style_dawn_awaking': "طلوعِ سحر",
        'style_nebula_mist': "دھندلی کہکشاں",
        'style_aurora_stream': "شفقِ قطبی",
        'style_crystal_shimmer': "کرسٹل چمک",
        'style_solar_flare': "شمسی شعلہ",
        'style_star_cluster': "ستاروں کا جھرمٹ",
        'style_cyber_vector': "سائبر ویکٹر",
        'style_void_vortex': "خلائی گرداب",
        'style_dimensional_rift': "کائناتی شگاف",
        'style_zenith_pinnacle': "فلکی بلندی",
    },
    'hi': {
        'thanks_journey': "हमारे सफर का हिस्सा बनने के लिए धन्यवाद!\nआपका समर्थन हमारे लिए बहुत मायने रखता है।",
        'select_world': "दुनिया चुनें",
        'world': "दुनिया",
        'guest': "अतिथि",
        'pro': "प्रो",
        'guest_player': "अतिथि खिलाड़ी",
        'tap_to_sync': "क्लाउड प्रगति सिंक करने के लिए टैप करें",
        'logout': "लॉग आउट",
        'sign_in': "साइन इन",
        'search_language': "भाषा खोजें...",
        'no_languages_found': "कोई भाषा नहीं मिली",
        'device_support_may_vary': "डिवाइस सपोर्ट भिन्न हो सकता है",
        'profile': "प्रोफ़ाइल",
        'style_dawn_awaking': "भोर का जागरण",
        'style_nebula_mist': "नीहारिका कोहरा",
        'style_aurora_stream': "ध्रुवीय ज्योति",
        'style_crystal_shimmer': "स्फटिक चमक",
        'style_solar_flare': "सौर ज्वाला",
        'style_star_cluster': "तारा गुच्छ",
        'style_cyber_vector': "साइबर वेक्टर",
        'style_void_vortex': "शून्य भंवर",
        'style_dimensional_rift': "आयामी दरार",
        'style_zenith_pinnacle': "शीर्ष शिखर",
    },
    'pa': {
        'thanks_journey': "ਸਾਡੇ ਸਫ਼ਰ ਦਾ ਹਿੱਸਾ ਬਣਨ ਲਈ ਧੰਨਵਾਦ!\nਤੁਹਾਡਾ ਸਮਰਥਨ ਸਾਡੇ ਲਈ ਸਭ ਕੁਝ ਹੈ।",
        'select_world': "ਦੁਨੀਆ ਚੁਣੋ",
        'world': "ਦੁਨੀਆ",
        'guest': "ਮਹਿਮਾਨ",
        'pro': "ਪ੍ਰੋ",
        'guest_player': "ਮਹਿਮਾਨ ਖਿਡਾਰੀ",
        'tap_to_sync': "ਕਲਾਊਡ ਪ੍ਰਗਤੀ ਸਿੰਕ ਕਰਨ ਲਈ ਟੈਪ ਕਰੋ",
        'logout': "ਲੌਗ ਆਊਟ",
        'sign_in': "ਸਾਈਨ ਇਨ",
        'search_language': "ਭਾਸ਼ਾ ਖੋਜੋ...",
        'no_languages_found': "ਕੋਈ ਭਾਸ਼ਾ ਨਹੀਂ ਮਿਲੀ",
        'device_support_may_vary': "ਡਿਵਾਈਸ ਸਹਾਇਤਾ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ",
        'profile': "ਪ੍ਰੋਫਾਈਲ",
        'style_dawn_awaking': "ਸਵੇਰ ਦਾ ਜਾਗਣਾ",
        'style_nebula_mist': "ਨੀਹਾਰਿਕਾ ਧੁੰਦ",
        'style_aurora_stream': "ਧਰੁਵੀ ਰੋਸ਼ਨੀ",
        'style_crystal_shimmer': "ਕ੍ਰਿਸਟਲ ਚਮਕ",
        'style_solar_flare': "ਸੂਰਜੀ ਲਾਟ",
        'style_star_cluster': "ਤਾਰਿਆਂ ਦਾ ਝੁਰਮਟ",
        'style_cyber_vector': "ਸਾਈਬਰ ਵੈਕਟਰ",
        'style_void_vortex': "ਖਲਾਅ ਘੁੰਮਣਘੇਰੀ",
        'style_dimensional_rift': "ਬ੍ਰਹਿਮੰਡੀ ਪਾੜਾ",
        'style_zenith_pinnacle': "ਸਿਖਰਲੀ ਚੋਟੀ",
    },
    'ar': {
        'thanks_journey': "شكراً لكونك جزءاً من رحلتنا!\nدعمك يعني لنا الكثير.",
        'select_world': "اختر العالم",
        'world': "العالم",
        'guest': "ضيف",
        'pro': "برو",
        'guest_player': "لاعب ضيف",
        'tap_to_sync': "انقر لمزامنة التقدم السحابي",
        'logout': "تسجيل الخروج",
        'sign_in': "تسجيل الدخول",
        'search_language': "بحث عن لغة...",
        'no_languages_found': "لم يتم العثور على لغات",
        'device_support_may_vary': "قد يختلف دعم الجهاز",
        'profile': "الملف الشخصي",
        'style_dawn_awaking': "صحوة الفجر",
        'style_nebula_mist': "سديم النجوم",
        'style_aurora_stream': "شفق قطبي",
        'style_crystal_shimmer': "بريق الكريستال",
        'style_solar_flare': "توهج شمسي",
        'style_star_cluster': "عنقود النجوم",
        'style_cyber_vector': "متجه سايبر",
        'style_void_vortex': "دوامة الفراغ",
        'style_dimensional_rift': "صدع أبعادي",
        'style_zenith_pinnacle': "قمة الأوج",
    },
    'fa': {
        'thanks_journey': "ممنون از اینکه بخشی از سفر ما هستید!\nحمایت شما برای ما بسیار ارزشمند است.",
        'select_world': "انتخاب جهان",
        'world': "جهان",
        'guest': "مهمان",
        'pro': "پرو",
        'guest_player': "بازیکن مهمان",
        'tap_to_sync': "برای همگام‌سازی ابری ضربه بزنید",
        'logout': "خروج",
        'sign_in': "ورود",
        'search_language': "جستجوی زبان...",
        'no_languages_found': "زبانی یافت نشد",
        'device_support_may_vary': "پشتیبانی دستگاه ممکن است متفاوت باشد",
        'profile': "پروفایل",
        'style_dawn_awaking': "طلوع سحر",
        'style_nebula_mist': "مه سحابی",
        'style_aurora_stream': "شفق قطبی",
        'style_crystal_shimmer': "درخشش کریستال",
        'style_solar_flare': "شراره خورشیدی",
        'style_star_cluster': "خوشه ستاره‌ای",
        'style_cyber_vector': "وکتور سایبر",
        'style_void_vortex': "گرداب خلاء",
        'style_dimensional_rift': "شکاف بعدی",
        'style_zenith_pinnacle': "اوج فلکی",
    },
    'ps': {
        'thanks_journey': "زموږ د سفر برخه کیدو لپاره مننه!\nستاسو ملاتړ زموږ لپاره خورا مهم دی.",
        'select_world': "نړۍ وټاکئ",
        'world': "نړۍ",
        'guest': "میلمه",
        'pro': "پرو",
        'guest_player': "میلمه لوبغاړی",
        'tap_to_sync': "د کلاوډ پرمختګ همغږۍ لپاره ټک وکړئ",
        'logout': "وتل",
        'sign_in': "ننوتل",
        'search_language': "ژبه وپلټئ...",
        'no_languages_found': "هیڅ ژبه ونه موندل شوه",
        'device_support_may_vary': "د وسیلې ملاتړ ممکن توپیر ولري",
        'profile': "پروفایل",
        'style_dawn_awaking': "د سهار ویښیدل",
        'style_nebula_mist': "د کهکشان دوړه",
        'style_aurora_stream': "قطبي رڼا",
        'style_crystal_shimmer': "د کرسټال ځلا",
        'style_solar_flare': "د لمر لمبه",
        'style_star_cluster': "د ستورو ټولګه",
        'style_cyber_vector': "سایبر ویکټور",
        'style_void_vortex': "د خلا ګرداب",
        'style_dimensional_rift': "کائناتي درز",
        'style_zenith_pinnacle': "لوړه څوکه",
    },
    'sd': {
        'thanks_journey': "اسان جي سفر جو حصو بڻجڻ لاءِ مھرباني!\nتوهان جو ساٿ اسان لاءِ تمام گهڻو اهم آهي.",
        'select_world': "دنيا چونڊيو",
        'world': "دنيا",
        'guest': "مهمان",
        'pro': "پرو",
        'guest_player': "مهمان رانديگر",
        'tap_to_sync': "ڪلائوڊ ترقي سنڪ ڪرڻ لاءِ ٽيپ ڪريو",
        'logout': "لاگ آئوٽ",
        'sign_in': "سائن ان",
        'search_language': "ٻولي ڳوليو...",
        'no_languages_found': "ڪابه ٻولي نه ملي",
        'device_support_may_vary': "ڊوائيس سپورٽ مختلف ٿي سگهي ٿي",
        'profile': "پروفائل",
        'style_dawn_awaking': "صبح جو جاڳڻ",
        'style_nebula_mist': "سحابي ڪوهيڙو",
        'style_aurora_stream': "قطبي شفق",
        'style_crystal_shimmer': "ڪرسٽل چمڪ",
        'style_solar_flare': "سج جي لهر",
        'style_star_cluster': "تارن جو ميڙ",
        'style_cyber_vector': "سائيبر ويڪٽر",
        'style_void_vortex': "خلا گرداب",
        'style_dimensional_rift': "جهاتي ٽٽ",
        'style_zenith_pinnacle': "اوج چوٽي",
    },
    'es': {
        'thanks_journey': "¡Gracias por ser parte de nuestro viaje!\nTu apoyo significa mucho para nosotros.",
        'select_world': "Seleccionar Mundo",
        'world': "Mundo",
        'guest': "INVITADO",
        'pro': "PRO",
        'guest_player': "Jugador Invitado",
        'tap_to_sync': "Toca para sincronizar el progreso en la nube",
        'logout': "Cerrar Sesión",
        'sign_in': "Iniciar Sesión",
        'search_language': "Buscar idioma...",
        'no_languages_found': "No se encontraron idiomas",
        'device_support_may_vary': "La compatibilidad del dispositivo puede variar",
        'profile': "Perfil",
        'style_dawn_awaking': "Despertar del Alba",
        'style_nebula_mist': "Niebla Nebulosa",
        'style_aurora_stream': "Torrente de Aurora",
        'style_crystal_shimmer': "Brillo de Cristal",
        'style_solar_flare': "Llamarada Solar",
        'style_star_cluster': "Cúmulo Estelar",
        'style_cyber_vector': "Vector Cibernético",
        'style_void_vortex': "Vórtice del Vacío",
        'style_dimensional_rift': "Fisura Dimensional",
        'style_zenith_pinnacle': "Cénit Celestial",
    },
    'fr': {
        'thanks_journey': "Merci de faire partie de notre voyage !\nVotre soutien compte énormément pour nous.",
        'select_world': "Choisir le Monde",
        'world': "Monde",
        'guest': "INVITÉ",
        'pro': "PRO",
        'guest_player': "Joueur Invité",
        'tap_to_sync': "Appuyez pour synchroniser le cloud",
        'logout': "Déconnexion",
        'sign_in': "Connexion",
        'search_language': "Rechercher une langue...",
        'no_languages_found': "Aucune langue trouvée",
        'device_support_may_vary': "La compatibilité de l'appareil peut varier",
        'profile': "Profil",
        'style_dawn_awaking': "Éveil de l'Aube",
        'style_nebula_mist': "Brume de Nébuleuse",
        'style_aurora_stream': "Flux d'Aurore",
        'style_crystal_shimmer': "Éclat de Cristal",
        'style_solar_flare': "Éruption Solaire",
        'style_star_cluster': "Amas d'Étoiles",
        'style_cyber_vector': "Vecteur Cyber",
        'style_void_vortex': "Vortex du Néant",
        'style_dimensional_rift': "Faille Dimensionnelle",
        'style_zenith_pinnacle': "Pinacle du Zénith",
    },
    'de': {
        'thanks_journey': "Danke, dass du Teil unserer Reise bist!\nDeine Unterstützung bedeutet uns alles.",
        'select_world': "Welt auswählen",
        'world': "Welt",
        'guest': "GAST",
        'pro': "PRO",
        'guest_player': "Gastspieler",
        'tap_to_sync': "Tippen zum Synchronisieren",
        'logout': "Abmelden",
        'sign_in': "Anmelden",
        'search_language': "Sprache suchen...",
        'no_languages_found': "Keine Sprachen gefunden",
        'device_support_may_vary': "Geräteunterstützung kann variieren",
        'profile': "Profil",
        'style_dawn_awaking': "Erwachen der Dämmerung",
        'style_nebula_mist': "Nebelschleier",
        'style_aurora_stream': "Aurorastrom",
        'style_crystal_shimmer': "Kristallschimmer",
        'style_solar_flare': "Sonneneruption",
        'style_star_cluster': "Sternenhaufen",
        'style_cyber_vector': "Cyber-Vektor",
        'style_void_vortex': "Leerenwirbel",
        'style_dimensional_rift': "Dimensionsriss",
        'style_zenith_pinnacle': "Zenit-Gipfel",
    },
    'ru': {
        'thanks_journey': "Спасибо, что вы с нами!\nВаша поддержка очень важна для нас.",
        'select_world': "Выберите мир",
        'world': "Мир",
        'guest': "ГОСТЬ",
        'pro': "ПРО",
        'guest_player': "Гостевой игрок",
        'tap_to_sync': "Нажмите для синхронизации с облаком",
        'logout': "Выйти",
        'sign_in': "Войти",
        'search_language': "Поиск языка...",
        'no_languages_found': "Языки не найдены",
        'device_support_may_vary': "Поддержка устройств может отличаться",
        'profile': "Профиль",
        'style_dawn_awaking': "Пробуждение зари",
        'style_nebula_mist': "Туманность",
        'style_aurora_stream': "Поток авроры",
        'style_crystal_shimmer': "Кристальный блеск",
        'style_solar_flare': "Солнечная вспышка",
        'style_star_cluster': "Звездное скопление",
        'style_cyber_vector': "Кибер-вектор",
        'style_void_vortex': "Вихрь пустоты",
        'style_dimensional_rift': "Пространственный разлом",
        'style_zenith_pinnacle': "Вершина зенита",
    },
    'zh_CN': {
        'thanks_journey': "感谢您与我们同行！\n您的支持对我们意义重大。",
        'select_world': "选择世界",
        'world': "世界",
        'guest': "访客",
        'pro': "专业版",
        'guest_player': "访客玩家",
        'tap_to_sync': "点击同步云端进度",
        'logout': "退出登录",
        'sign_in': "登录",
        'search_language': "搜索语言...",
        'no_languages_found': "未找到语言",
        'device_support_may_vary': "设备支持可能有所不同",
        'profile': "个人资料",
        'style_dawn_awaking': "黎明初醒",
        'style_nebula_mist': "星云薄雾",
        'style_aurora_stream': "极光之流",
        'style_crystal_shimmer': "水晶微光",
        'style_solar_flare': "耀斑爆发",
        'style_star_cluster': "星团汇聚",
        'style_cyber_vector': "赛博矢量",
        'style_void_vortex': "虚空漩涡",
        'style_dimensional_rift': "空间裂隙",
        'style_zenith_pinnacle': "天顶之巅",
    },
    'tr': {
        'thanks_journey': "Yolculuğumuzun bir parçası olduğunuz için teşekkürler!\nDesteğiniz bizim için çok değerli.",
        'select_world': "Dünya Seç",
        'world': "Dünya",
        'guest': "MİSAFİR",
        'pro': "PRO",
        'guest_player': "Misafir Oyuncu",
        'tap_to_sync': "Bulut ilerlemesini eşitlemek için dokunun",
        'logout': "Çıkış Yap",
        'sign_in': "Giriş Yap",
        'search_language': "Dil ara...",
        'no_languages_found': "Dil bulunamadı",
        'device_support_may_vary': "Cihaz desteği değişiklik gösterebilir",
        'profile': "Profil",
        'style_dawn_awaking': "Şafak Uyanışı",
        'style_nebula_mist': "Bulutsu Sisi",
        'style_aurora_stream': "Kutup Işıkları Akışı",
        'style_crystal_shimmer': "Kristal Parıltısı",
        'style_solar_flare': "Güneş Parlaması",
        'style_star_cluster': "Yıldız Kümesi",
        'style_cyber_vector': "Siber Vektör",
        'style_void_vortex': "Hiçlik Girdabı",
        'style_dimensional_rift': "Boyut Yarığı",
        'style_zenith_pinnacle': "Zirve Doruğu",
    },
    'id': {
        'thanks_journey': "Terima kasih telah menjadi bagian dari perjalanan kami!\nDukungan Anda sangat berarti bagi kami.",
        'select_world': "Pilih Dunia",
        'world': "Dunia",
        'guest': "TAMU",
        'pro': "PRO",
        'guest_player': "Pemain Tamu",
        'tap_to_sync': "Ketuk untuk menyinkronkan cloud",
        'logout': "Keluar",
        'sign_in': "Masuk",
        'search_language': "Cari bahasa...",
        'no_languages_found': "Bahasa tidak ditemukan",
        'device_support_may_vary': "Dukungan perangkat dapat bervariasi",
        'profile': "Profil",
        'style_dawn_awaking': "Fajar Merebak",
        'style_nebula_mist': "Kabut Nebula",
        'style_aurora_stream': "Arus Aurora",
        'style_crystal_shimmer': "Kilau Kristal",
        'style_solar_flare': "Suar Surya",
        'style_star_cluster': "Gugus Bintang",
        'style_cyber_vector': "Vektor Siber",
        'style_void_vortex': "Pusaran Kehampaan",
        'style_dimensional_rift': "Celah Dimensi",
        'style_zenith_pinnacle': "Puncak Zenit",
    },
    'bn': {
        'thanks_journey': "আমাদের যাত্রার অংশ হওয়ার জন্য ধন্যবাদ!\nআপনার সমর্থন আমাদের কাছে অনেক মূল্যবান।",
        'select_world': "বিশ্ব নির্বাচন করুন",
        'world': "বিশ্ব",
        'guest': "অতিথি",
        'pro': "প্রো",
        'guest_player': "অতিথি খেলোয়াড়",
        'tap_to_sync': "ক্লাউড অগ্রগতি সিঙ্ক করতে ট্যাপ করুন",
        'logout': "লগ আউট",
        'sign_in': "সাইন ইন",
        'search_language': "ভাষা অনুসন্ধান করুন...",
        'no_languages_found': "কোনো ভাষা পাওয়া যায়নি",
        'device_support_may_vary': "ডিভাইস সমর্থন পরিবর্তিত হতে পারে",
        'profile': "প্রোফাইল",
        'style_dawn_awaking': "ভোরের জাগরণ",
        'style_nebula_mist': "নীহারিকা কুয়াশা",
        'style_aurora_stream': "মেরুপ্রভা স্রোত",
        'style_crystal_shimmer': "স্ফটিক দীপ্তি",
        'style_solar_flare': "সৌর শিখা",
        'style_star_cluster': "তারকা গুচ্ছ",
        'style_cyber_vector': "সাইবার ভেক্টর",
        'style_void_vortex': "শূন্য ঘূর্ণি",
        'style_dimensional_rift': "মাত্রিক ফাটল",
        'style_zenith_pinnacle': "শীর্ষ চূড়া",
    }
}

# Apply curated presets first
for code, p in CURATED_PRESETS.items():
    if code in all_langs:
        all_langs[code].update(p)

base_keys = CURATED_PRESETS['en']

# For remaining languages, ensure all keys are populated
for code in LANG_CODES:
    for k, v in base_keys.items():
        if k not in all_langs[code] or not all_langs[code][k]:
            all_langs[code][k] = v

# Rebuild lib/localization/screen_translations.dart
lines_out = [
    "// AUTO-GENERATED - DO NOT MODIFY DIRECTLY",
    "// Complete Screen Translations for MindTrap AI.",
    "// Complete coverage for all 56 supported languages.",
    "",
    "class ScreenTranslations {",
    "  ScreenTranslations._();",
    "",
    "  static const Map<String, Map<String, String>> data = {",
]

for code in LANG_CODES:
    kvs = all_langs[code]
    lines_out.append(f"    '{code}': {{")
    for k in sorted(kvs.keys()):
        val = kvs[k]
        # Clean string escaping
        val = val.replace('\r', '').replace('\n', '\\n')
        # Avoid double-escaping single quotes
        val = re.sub(r"(?<!\\)'", r"\'", val)
        lines_out.append(f"      '{k}': '{val}',")
    lines_out.append("    },")

lines_out.append("  };")
lines_out.append("}")
lines_out.append("")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines_out))

print("Successfully enriched screen_translations.dart!")
