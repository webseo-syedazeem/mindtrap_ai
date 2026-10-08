import re

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

langs = re.findall(r"'([a-zA-Z_]+)':\s*\{", text)
print(f"Total languages in ScreenTranslations: {len(langs)}")

# Check keys in 'mr'
m = re.search(r"'mr':\s*\{(.*?)\}\s*,\s*'", text, re.DOTALL)
if m:
    lines = m.group(1).strip().splitlines()
    print(f"Total keys in 'mr': {len(lines)}")
