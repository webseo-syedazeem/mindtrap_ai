import re

with open('lib/localization/extended_app_strings.dart', 'r', encoding='utf-8') as f:
    text = f.read()

langs = re.findall(r"'([a-zA-Z_]+)':\s*\{", text)
print(f"Total languages in ExtendedAppStrings: {len(langs)}")
print("Sample:", langs[:20])
