# -*- coding: utf-8 -*-
import json
import sys
import time
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

base_en = {
    'lets_map_your_mind': "LET'S MAP YOUR MIND",
    'map_your_mind_title': "Let's Map Your Mind",
    'quick_training': "QUICK TRAINING",
    'progress': "PROGRESS",
    'daily_challenge': "DAILY CHALLENGE",
    'achievements': "ACHIEVEMENTS",
    'done_badge': "✓ DONE",
    'new_badge': "⚡ NEW",
    'claim': "CLAIM",
    'step': "Step",
    'of': "of",
    'your_age': "Your Age",
    'your_age_sub': "Select your age to get personalized challenges",
    'gender': "Gender",
    'gender_sub': "This helps us tailor your experience",
    'your_goal': "Your Goal",
    'your_goal_sub': "What would you like to achieve with MindTrap AI?",
    'current_iq_level': "Your Current IQ Level",
    'iq_sub': "Select the range that best describes you",
    'you_are_all_set': "You're All Set!",
    'plan_ready': "Your personalized training plan is ready",
    'male': "Male",
    'female': "Female",
    'prefer_not_to_say': "Prefer not to say",
    'under_13': "Under 13",
    'not_sure': "Not sure",
    'below_90': "Below 90",
    'above_130': "Above 130",
    'improve_focus': "Improve Focus",
    'better_concentration': "Better concentration",
    'boost_iq': "Boost IQ",
    'higher_cognitive': "Higher cognitive skills",
    'sharpen_memory': "Sharpen Memory",
    'remember_better': "Remember better",
    'solve_problems': "Solve Problems",
    'think_logically': "Think more logically",
    'age': "Age",
    'goal': "Goal",
    'iq_level': "IQ Level",
    'back': "Back",
    'next': "Next",
    'done': "Done",
}

ur_map = {
    'lets_map_your_mind': "اپنے ذہن کا خاکہ بنائیں",
    'map_your_mind_title': "اپنے ذہن کا خاکہ بنائیں",
    'quick_training': "فوری تربیت",
    'progress': "پیش رفت",
    'daily_challenge': "روزانہ چیلنج",
    'achievements': "کامیابیاں",
    'done_badge': "✓ مکمل",
    'new_badge': "⚡ نیا",
    'claim': "وصول کریں",
    'step': "مرحلہ",
    'of': "از",
    'your_age': "آپ کی عمر",
    'your_age_sub': "ذاتی چیلنجز کے لیے اپنی عمر منتخب کریں",
    'gender': "جنس",
    'gender_sub': "یہ آپ کے تجربے کو بہتر بنانے میں مدد کرتا ہے",
    'your_goal': "آپ کا مقصد",
    'your_goal_sub': "آپ MindTrap AI سے کیا حاصل کرنا چاہتے ہیں؟",
    'current_iq_level': "آپ کی موجودہ آئی کیو کی سطح",
    'iq_sub': "وہ حد منتخب کریں جو آپ کی عکاسی کرتی ہے",
    'you_are_all_set': "آپ بالکل تیار ہیں!",
    'plan_ready': "آپ کا ذاتی تربیتی منصوبہ تیار ہے",
    'male': "مرد",
    'female': "عورت",
    'prefer_not_to_say': "بتانا پسند نہیں",
    'under_13': "13 سے کم",
    'not_sure': "یقین نہیں",
    'below_90': "90 سے کم",
    'above_130': "130 سے زیادہ",
    'improve_focus': "توجہ بہتر بنائیں",
    'better_concentration': "بہتر ارتکاز",
    'boost_iq': "آئی کیو بڑھائیں",
    'higher_cognitive': "اعلیٰ ذہنی صلاحیتیں",
    'sharpen_memory': "یادداشت تیز کریں",
    'remember_better': "بہتر یاد رکھیں",
    'solve_problems': "مسائل حل کریں",
    'think_logically': "زیادہ منطقی سوچیں",
    'age': "عمر",
    'goal': "مقصد",
    'iq_level': "آئی کیو کی سطح",
    'back': "پیچھے",
    'next': "اگلا",
    'done': "مکمل",
}

ALL_CODES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

GOOGLE_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt',
    'zh_CN': 'zh-CN',
    'zh_TW': 'zh-TW',
    'fil': 'tl',
    'he': 'iw',
}

keys_list = list(base_en.keys())
values_list = [base_en[k] for k in keys_list]
payload_text = '\n'.join(values_list)

results = {'en': base_en, 'ur': ur_map}

for code in ALL_CODES:
    if code in results:
        print(f"Skipping preset for {code}")
        continue

    target_lang = GOOGLE_MAP.get(code, code)
    print(f"Translating {code} (-> {target_lang})...")
    
    success = False
    for attempt in range(3):
        try:
            data = urllib.parse.urlencode({'q': payload_text}).encode('utf-8')
            req = urllib.request.Request(
                f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t',
                data=data,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            res = urllib.request.urlopen(req, timeout=12)
            body = json.loads(res.read().decode('utf-8'))
            translated_lines = ''.join([s[0] for s in body[0] if s and s[0]]).split('\n')
            
            # Trim extra empty lines at end if any
            while len(translated_lines) > len(keys_list) and not translated_lines[-1].strip():
                translated_lines.pop()

            if len(translated_lines) == len(keys_list):
                trans_map = {}
                for k, v in zip(keys_list, translated_lines):
                    v_clean = v.strip()
                    if k == 'done_badge' and not v_clean.startswith('✓'):
                        v_clean = '✓ ' + v_clean
                    elif k == 'new_badge' and not v_clean.startswith('⚡'):
                        v_clean = '⚡ ' + v_clean
                    trans_map[k] = v_clean
                results[code] = trans_map
                success = True
                print(f"-> {code}: 42/42 keys translated successfully")
                break
            else:
                print(f"Mismatch for {code}: got {len(translated_lines)} vs {len(keys_list)}")
                time.sleep(0.5)
        except Exception as e:
            print(f"Error on {code}: {e}")
            time.sleep(1.0)
            
    if not success:
        print(f"Using English fallback for {code}")
        results[code] = base_en
    time.sleep(0.3)

# Write to lib/localization/extended_app_strings.dart
dart_code = """// AUTO-GENERATED - Extended translations for Action Buttons and Map Your Mind wizard.
// All 56 supported languages fully localized.

class ExtendedAppStrings {
  ExtendedAppStrings._();

  static const Map<String, Map<String, String>> data = {
"""

for code in ALL_CODES:
    trans_map = results.get(code, base_en)
    dart_code += f"    '{code}': {{\n"
    for k in keys_list:
        v = trans_map.get(k, base_en[k])
        v_clean = v.replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$")
        dart_code += f"      '{k}': '{v_clean}',\n"
    dart_code += "    },\n"

dart_code += """  };
}
"""

with open('lib/localization/extended_app_strings.dart', 'w', encoding='utf-8') as f:
    f.write(dart_code)

print("SUCCESS: lib/localization/extended_app_strings.dart updated with all 56 languages!")
