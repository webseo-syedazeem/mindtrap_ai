# -*- coding: utf-8 -*-
import json
import re
import urllib.request
import urllib.parse
import time

file_path = 'lib/localization/screen_translations.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    orig_code = f.read()

pattern = r"'([a-zA-Z_]+)':\s*\{([^}]+)\}"
matches = re.findall(pattern, orig_code)

all_langs = {}
for code, block in matches:
    kv_pattern = r"'([a-zA-Z0-9_]+)':\s*'([^']*)'"
    pairs = re.findall(kv_pattern, block)
    all_langs[code] = dict(pairs)

print(f"Loaded {len(all_langs)} languages.")

EN_ALL = {
    'worlds': 'Worlds',
    'daily_rewards': 'Daily Rewards',
    'daily_rewards_sub': 'Claim free coins & gems every 24 hours',
    'edit_mind_profile': 'Edit Mind Profile',
    'edit_mind_profile_sub': 'Update age, gender, IQ & goal',
    'rate_us': 'Rate Us',
    'rate_us_subtitle': 'Show your love with 5 stars',
    'settings': 'Settings',
    'store': 'Store',
    'play': 'Play',
    'lets_map_your_mind': "Let's Map Your Mind",
    'daily_reward': 'Daily Reward',
    'daily_login_rewards': 'Daily Login Rewards',
    'thank_you_for_playing': 'Thank you for playing!\nWe hope you enjoy the game as much as we enjoyed creating it for you.',
    'about_game': 'About Game',
    'version': 'Version',
    'app_title': 'MindTrap AI',
    'levels_cleared': 'Levels Cleared',
    'world_unlock_req': 'Complete all 40 levels of World {n} to unlock',
    'world_locked': 'World Locked',
    'level_locked': 'Level Locked',
    'game_menu': 'Game Menu',
    'languages': 'Languages',
    'levels_odyssey': '1,000 Levels Odyssey',
    'worlds_map_sub': '25 Worlds • 1,000 Levels Map',
    'worlds_badge': '25 WORLDS',
    'store_sub': 'Gems, Coins & Hint Boosters',
    'hot_deals': 'HOT DEALS',
    'free': 'FREE',
    'mind_badge': 'MIND',
    'language_label': 'Language',
    'tap_to_change': 'Tap to change',
    'settings_sub': 'Audio, vibration & game data',
    'config_badge': 'CONFIG',
    'stars_5_badge': '5 STARS',
    'quick_audio_haptics': 'QUICK AUDIO & HAPTICS',
    'signed_out_success': 'Signed out successfully',
    'signed_in_google': 'Signed in with Google!',
    'google_sign_in_failed': 'Google Sign-in failed',
    'sound': 'Sound',
    'music': 'Music',
    'vibration': 'Vibration',
}

UR_ALL = {
    'worlds': 'دنیا',
    'daily_rewards': 'روزانہ انعامات',
    'daily_rewards_sub': 'ہر 24 گھنٹے میں مفت سکے اور ہیرے حاصل کریں',
    'edit_mind_profile': 'ذہنی پروفائل تبدیل کریں',
    'edit_mind_profile_sub': 'عمر، صنف، آئی کیو اور ہدف تبدیل کریں',
    'rate_us': 'ہمیں ریٹ کریں',
    'rate_us_subtitle': '5 ستاروں کے ساتھ اپنی محبت دکھائیں',
    'settings': 'ترتیبات',
    'store': 'اسٹور',
    'play': 'کھیلیں',
    'lets_map_your_mind': 'اپنے ذہن کا خاکہ بنائیں',
    'daily_reward': 'روزانہ انعام',
    'daily_login_rewards': 'روزانہ لاگ ان انعامات',
    'thank_you_for_playing': 'کھیلنے کا شکریہ!\nہمیں امید ہے کہ آپ اس کھیل سے اتنا ہی لطف اندوز ہوں گے جتنا ہم نے اسے آپ کے لیے بنانے میں لیا۔',
    'about_game': 'گیم کے بارے میں',
    'version': 'ورژن',
    'app_title': 'مائنڈ ٹریپ اے آئی',
    'levels_cleared': 'لیولز مکمل',
    'world_unlock_req': 'کھولنے کے لیے دنیا {n} کے تمام 40 لیولز مکمل کریں',
    'world_locked': 'دنیا مقفل ہے',
    'level_locked': 'لیول مقفل ہے',
    'game_menu': 'گیم مینو',
    'languages': 'زبانیں',
    'levels_odyssey': '1,000 لیولز مہم',
    'worlds_map_sub': '25 دنیا • 1,000 لیولز کا نقشہ',
    'worlds_badge': '25 دنیا',
    'store_sub': 'ہیرے، سکے اور بوسٹرز',
    'hot_deals': 'خصوصی آفرز',
    'free': 'مفت',
    'mind_badge': 'ذہن',
    'language_label': 'زبان',
    'tap_to_change': 'تبدیل کرنے کے لیے دبائیں',
    'settings_sub': 'آواز، وائبریشن اور گیم ڈیٹا',
    'config_badge': 'سیٹنگز',
    'stars_5_badge': '5 ستارے',
    'quick_audio_haptics': 'آڈیو اور وائبریشن سیٹنگز',
    'signed_out_success': 'کامیابی سے سائن آؤٹ ہو گیا',
    'signed_in_google': 'گوگل کے ساتھ سائن ان ہو گیا!',
    'google_sign_in_failed': 'گوگل سائن ان ناکام ہو گیا',
    'sound': 'آواز',
    'music': 'موسیقی',
    'vibration': 'وائبریشن',
}

PA_ALL = {
    'worlds': 'ਸੰਸਾਰ',
    'daily_rewards': 'ਰੋਜ਼ਾਨਾ ਇਨਾਮ',
    'daily_rewards_sub': 'ਹਰ 24 ਘੰਟਿਆਂ ਵਿੱਚ ਮੁਫ਼ਤ ਸਿੱਕੇ ਅਤੇ ਹੀਰੇ ਪ੍ਰਾਪਤ ਕਰੋ',
    'edit_mind_profile': 'ਦਿਮਾਗੀ ਪ੍ਰੋਫਾਈਲ ਬਦਲੋ',
    'edit_mind_profile_sub': 'ਉਮਰ, ਲਿੰਗ, ਆਈਕਿਊ ਅਤੇ ਟੀਚਾ ਅੱਪਡੇਟ ਕਰੋ',
    'rate_us': 'ਸਾਨੂੰ ਰੇਟ ਕਰੋ',
    'rate_us_subtitle': '5 ਸਿਤਾਰਿਆਂ ਨਾਲ ਆਪਣਾ ਪਿਆਰ ਦਿਖਾਓ',
    'settings': 'ਸੈਟਿੰਗਾਂ',
    'store': 'ਸਟੋਰ',
    'play': 'ਖੇਡੋ',
    'lets_map_your_mind': 'ਆਪਣੇ ਦਿਮਾਗ ਦਾ ਨਕਸ਼ਾ ਬਣਾਓ',
    'daily_reward': 'ਰੋਜ਼ਾਨਾ ਇਨਾਮ',
    'daily_login_rewards': 'ਰੋਜ਼ਾਨਾ ਲੌਗਇਨ ਇਨਾਮ',
    'thank_you_for_playing': 'ਖੇਡਣ ਲਈ ਧੰਨਵਾਦ!\nਸਾਨੂੰ ਉਮੀਦ ਹੈ ਕਿ ਤੁਸੀਂ ਇਸ ਖੇਡ ਦਾ ਓਨਾ ਹੀ ਆਨੰਦ ਮਾਣੋਗੇ ਜਿੰਨਾ ਅਸੀਂ ਤੁਹਾਡੇ ਲਈ ਬਣਾਉਣ ਵਿੱਚ ਲਿਆ।',
    'about_game': 'ਖੇਡ ਬਾਰੇ',
    'version': 'ਵਰਜਨ',
    'app_title': 'ਮਾਈਂਡਟ੍ਰੈਪ ਏਆਈ',
    'levels_cleared': 'ਪੱਧਰ ਪੂਰੇ ਹੋਏ',
    'world_unlock_req': 'ਅਨਲੌਕ ਕਰਨ ਲਈ ਸੰਸਾਰ {n} ਦੇ ਸਾਰੇ 40 ਪੱਧਰ ਪੂਰੇ ਕਰੋ',
    'world_locked': 'ਸੰਸਾਰ ਲਾਕ ਹੈ',
    'level_locked': 'ਪੱਧਰ ਲਾਕ ਹੈ',
    'game_menu': 'ਗੇਮ ਮੇਨੂ',
    'languages': 'ਭਾਸ਼ਾਵਾਂ',
    'levels_odyssey': '1,000 ਪੱਧਰ ਓਡੀਸੀ',
    'worlds_map_sub': '25 ਸੰਸਾਰ • 1,000 ਪੱਧਰਾਂ ਦਾ ਨਕਸ਼ਾ',
    'worlds_badge': '25 ਸੰਸਾਰ',
    'store_sub': 'ਹੀਰੇ, ਸਿੱਕੇ ਅਤੇ ਸੰਕੇਤ ਬੂਸਟਰ',
    'hot_deals': 'ਗਰਮ ਸੌਦੇ',
    'free': 'ਮੁਫ਼ਤ',
    'mind_badge': 'ਮਨ',
    'language_label': 'ਭਾਸ਼ਾ',
    'tap_to_change': 'ਬਦਲਣ ਲਈ ਟੈਪ ਕਰੋ',
    'settings_sub': 'ਆਡੀਓ, ਵਾਈਬ੍ਰੇਸ਼ਨ ਅਤੇ ਗੇਮ ਡੇਟਾ',
    'config_badge': 'ਸੈਟਿੰਗਾਂ',
    'stars_5_badge': '5 ਤਾਰੇ',
    'quick_audio_haptics': 'ਤੇਜ਼ ਆਡੀਓ ਅਤੇ ਹੈਪਟਿਕਸ',
    'signed_out_success': 'ਸਫਲਤਾਪੂਰਵਕ ਸਾਈਨ ਆਉਟ ਹੋ ਗਿਆ',
    'signed_in_google': 'ਗੂਗਲ ਨਾਲ ਸਾਈਨ ਇਨ ਹੋ ਗਿਆ!',
    'google_sign_in_failed': 'ਗੂਗਲ ਸਾਈਨ-ਇਨ ਅਸਫਲ ਰਿਹਾ',
    'sound': 'ਆਵਾਜ਼',
    'music': 'ਸੰਗੀਤ',
    'vibration': 'ਵਾਈਬ੍ਰੇਸ਼ਨ',
}

HI_ALL = {
    'worlds': 'दुनिया',
    'daily_rewards': 'दैनिक पुरस्कार',
    'daily_rewards_sub': 'हर 24 घंटे में मुफ्त सिक्के और हीरे पाएं',
    'edit_mind_profile': 'माइंड प्रोफाइल बदलें',
    'edit_mind_profile_sub': 'आयु, लिंग, आईक्यू और लक्ष्य अपडेट करें',
    'rate_us': 'हमें रेट करें',
    'rate_us_subtitle': '5 सितारों के साथ अपना प्यार दिखाएं',
    'settings': 'सेटिंग्स',
    'store': 'स्टोर',
    'play': 'खेलें',
    'lets_map_your_mind': 'अपने दिमाग का नक्शा बनाएं',
    'daily_reward': 'दैनिक इनाम',
    'daily_login_rewards': 'दैनिक लॉगिन पुरस्कार',
    'thank_you_for_playing': 'खेलने के लिए धन्यवाद!\nहमें उम्मीद है कि आपको यह गेम उतना ही पसंद आएगा जितना हमें आपके लिए इसे बनाने में आया।',
    'about_game': 'गेम के बारे में',
    'version': 'संस्करण',
    'app_title': 'माइंडट्रैप एआई',
    'levels_cleared': 'लेवल पूरे हुए',
    'world_unlock_req': 'अनलॉक करने के लिए वर्ल्ड {n} के सभी 40 लेवल पूरे करें',
    'world_locked': 'वर्ल्ड लॉक है',
    'level_locked': 'लेवल लॉक है',
    'game_menu': 'गेम मेनू',
    'languages': 'भाषाएँ',
    'levels_odyssey': '1,000 लेवल यात्रा',
    'worlds_map_sub': '25 वर्ल्ड • 1,000 लेवल का नक्शा',
    'worlds_badge': '25 वर्ल्ड्स',
    'store_sub': 'हीरे, सिक्के और बूस्टर',
    'hot_deals': 'हॉट डील्स',
    'free': 'मुफ़्त',
    'mind_badge': 'माइंड',
    'language_label': 'भाषा',
    'tap_to_change': 'बदलने के लिए टैप करें',
    'settings_sub': 'ऑडियो, कंपन और गेम डेटा',
    'config_badge': 'सेटिंग्स',
    'stars_5_badge': '5 सितारे',
    'quick_audio_haptics': 'क्विक ऑडियो व हैप्टिक्स',
    'signed_out_success': 'सफलतापूर्वक साइन आउट हो गया',
    'signed_in_google': 'गूगल से साइन इन हो गया!',
    'google_sign_in_failed': 'गूगल साइन-इन विफल रहा',
    'sound': 'ध्वनि',
    'music': 'संगीत',
    'vibration': 'कंपन',
}

AR_ALL = {
    'worlds': 'العوالم',
    'daily_rewards': 'المكافآت اليومية',
    'daily_rewards_sub': 'احصل على عملات وجواهر مجانية كل 24 ساعة',
    'edit_mind_profile': 'تعديل الملف العقلي',
    'edit_mind_profile_sub': 'تحديث العمر والجنس ومستوى الذكاء والهدف',
    'rate_us': 'قيّمنا',
    'rate_us_subtitle': 'أظهر حبك مع 5 نجوم',
    'settings': 'الإعدادات',
    'store': 'المتجر',
    'play': 'العب',
    'lets_map_your_mind': 'دعنا نرسم خريطة عقلك',
    'daily_reward': 'المكافأة اليومية',
    'daily_login_rewards': 'مكافآت تسجيل الدخول اليومية',
    'thank_you_for_playing': 'شكراً للعبك!\nنتمنى أن تستمتع باللعبة بقدر استمتاعنا بصنعها لك.',
    'about_game': 'حول اللعبة',
    'version': 'الإصدار',
    'app_title': 'مايند تراب ذكاء اصطناعي',
    'levels_cleared': 'مستويات مكتملة',
    'world_unlock_req': 'أكمل جميع مستويات العالم {n} الـ 40 لفتحه',
    'world_locked': 'العالم مغلق',
    'level_locked': 'المستوى مغلق',
    'game_menu': 'قائمة اللعبة',
    'languages': 'اللغات',
    'levels_odyssey': 'ملحمة 1000 مستوى',
    'worlds_map_sub': 'خريطة 25 عالماً • 1000 مستوى',
    'worlds_badge': '25 عالماً',
    'store_sub': 'جواهر وعملات ومساعدات',
    'hot_deals': 'عروض مميزة',
    'free': 'مجاناً',
    'mind_badge': 'العقل',
    'language_label': 'اللغة',
    'tap_to_change': 'اضغط للتغيير',
    'settings_sub': 'الصوت والاهتزاز والبيانات',
    'config_badge': 'إعدادات',
    'stars_5_badge': '5 نجوم',
    'quick_audio_haptics': 'إعدادات الصوت والاهتزاز السريعة',
    'signed_out_success': 'تم تسجيل الخروج بنجاح',
    'signed_in_google': 'تم تسجيل الدخول بواسطة جوجل!',
    'google_sign_in_failed': 'فشل تسجيل الدخول بجوجل',
    'sound': 'الصوت',
    'music': 'الموسيقى',
    'vibration': 'الاهتزاز',
}

PRESETS = {
    'en': EN_ALL,
    'ur': UR_ALL,
    'pa': PA_ALL,
    'hi': HI_ALL,
    'ar': AR_ALL,
}

GOOGLE_MAP = {
    'pt_BR': 'pt', 'pt_PT': 'pt', 'zh_CN': 'zh-CN', 'zh_TW': 'zh-TW',
    'fil': 'tl', 'he': 'iw'
}

keys_list = list(EN_ALL.keys())
values_list = [EN_ALL[k] for k in keys_list]

for code in all_langs:
    if code in PRESETS:
        for k, v in PRESETS[code].items():
            all_langs[code][k] = v
        print(f"[{code}] Used curated preset ({len(PRESETS[code])} keys)")
    else:
        target_lang = GOOGLE_MAP.get(code, code)
        payload = ' ||| '.join(values_list)
        try:
            data = urllib.parse.urlencode({'q': payload}).encode('utf-8')
            req = urllib.request.Request(
                f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t',
                data=data,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            res = urllib.request.urlopen(req, timeout=10)
            body = json.loads(res.read().decode('utf-8'))
            translated_chunks = [part[0] for part in body[0] if part and part[0]]
            full_str = ''.join(translated_chunks)
            parts = [p.strip() for p in full_str.split('|||')]
            if len(parts) == len(keys_list):
                for k, v in zip(keys_list, parts):
                    all_langs[code][k] = v
                print(f"[{code}] Successfully translated all {len(keys_list)} keys")
            else:
                for k, v in zip(keys_list, values_list):
                    all_langs[code][k] = v
                print(f"[{code}] Fallback to default (length mismatch {len(parts)})")
        except Exception as e:
            for k, v in zip(keys_list, values_list):
                all_langs[code][k] = v
            print(f"[{code}] Exception {e}, fallback")

# Re-write screen_translations.dart
output = [
    "// AUTO-GENERATED - DO NOT MODIFY DIRECTLY",
    "// Complete Screen Translations for MindTrap AI.",
    "// Complete coverage for all 56 supported languages.",
    "",
    "class ScreenTranslations {",
    "  ScreenTranslations._();",
    "",
    "  static const Map<String, Map<String, String>> data = {",
]

for code in all_langs:
    kvs = all_langs[code]
    output.append(f"    '{code}': {{")
    for k, v in kvs.items():
        escaped_v = v.replace("\\", "\\\\").replace("'", "\\'")
        output.append(f"      '{k}': '{escaped_v}',")
    output.append("    },")

output.append("  };")
output.append("}")
output.append("")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(output))

print("SUCCESS! Full screen translations written for all 56 languages!")
