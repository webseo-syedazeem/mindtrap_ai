import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    text = f.read()

languages = ['en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'ar', 'es', 'fr', 'de', 'ru', 'zh_CN']
for lang in languages:
    m = re.search(rf"'{lang}':\s*\{{(.*?)\}}", text, re.DOTALL)
    if m:
        keys = re.findall(r"'([a-zA-Z0-9_]+)':\s*'([^']*)'", m.group(1))
        # Count how many are in English or same as en
        print(f"Lang {lang}: {len(keys)} keys")
    else:
        print(f"Lang {lang}: NOT FOUND in _translations")
