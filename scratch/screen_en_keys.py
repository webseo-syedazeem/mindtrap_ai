import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', encoding='utf-8') as f:
    text = f.read()

idx_en = text.find("'en': {")
idx_en_end = text.find("},\n    'ur': {")

import re
keys = re.findall(r"'([a-zA-Z0-9_]+)':\s*'([^']*)'", text[idx_en:idx_en_end])
print(f"Total keys in ScreenTranslations['en']: {len(keys)}")
for k, v in keys:
    print(f"{k}: {v}")
