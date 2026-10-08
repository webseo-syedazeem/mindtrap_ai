import re

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    t = f.read()

# Match AppLanguage(...)
langs = re.findall(r"AppLanguage\(\s*code:\s*'([^']+)',\s*englishName:\s*'([^']+)',\s*nativeName:\s*'([^']+)'", t)
print(f"Total languages: {len(langs)}")
for c, en, nat in langs:
    print(f"'{c}': {en} ({nat})")
