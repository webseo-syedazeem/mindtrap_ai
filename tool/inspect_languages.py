# -*- coding: utf-8 -*-
with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    lines = f.readlines()

langs = []
for line in lines:
    if "code: '" in line:
        code = line.split("code: '")[1].split("'")[0]
        langs.append(code)

print(f"Total languages: {len(langs)}")
print(langs)
