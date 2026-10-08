import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

def parse_lang(code):
    m = re.search(rf"'{code}':\s*\{{(.*?)\}}\s*,\s*'", text, re.DOTALL)
    if not m:
        m = re.search(rf"'{code}':\s*\{{(.*?)\}}\s*\}};", text, re.DOTALL)
    if not m:
        return {}
    res = {}
    for line in m.group(1).splitlines():
        km = re.match(r"\s*'([a-zA-Z0-9_]+)':\s*'(.*)',?", line)
        if km:
            res[km.group(1)] = km.group(2)
    return res

test_langs = ['ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'ar', 'es', 'fr', 'de', 'ru', 'zh_CN', 'ja', 'ko', 'tr', 'id']
print("Language Verification for core 'play' and 'settings':")
for l in test_langs:
    data = parse_lang(l)
    print(f"[{l}] play: '{data.get('play')}', settings: '{data.get('settings')}', worlds: '{data.get('worlds')}'")
