import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# find keys in 'en' in _translations
idx = text.find("static const Map<String, Map<String, String>> _translations = {")
idx_en = text.find("'en': {", idx)
idx_en_end = text.find("},\n    'ur': {", idx_en)

import re
en_keys = re.findall(r"'([a-zA-Z0-9_]+)':", text[idx_en:idx_en_end])
print(f"Total keys in _translations['en']: {len(en_keys)}")
print("Sample keys:", en_keys[:40])
