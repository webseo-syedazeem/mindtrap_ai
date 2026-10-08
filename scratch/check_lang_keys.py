import re

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    c = f.read()

all_codes = ['en', 'ur', 'hi', 'pa', 'bn', 'es', 'fr', 'de', 'ar', 'ru', 'zh_CN']
for code in all_codes:
    p = c.find(f"'{code}': {{")
    if p != -1:
        e = c.find("},", p)
        sub = c[p:e]
        keys = re.findall(r"'([a-zA-Z0-9_]+)':", sub)
        print(f"{code}: {len(keys)} keys")
