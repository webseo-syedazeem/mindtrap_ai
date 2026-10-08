import os
import re

# 1. Collect all tr('...') keys used in lib/
tr_regex = re.compile(r"tr\(\s*'([a-zA-Z0-9_-]+)'\s*\)")
used_keys = set()

for root, dirs, files in os.walk('lib'):
    for f in files:
        if f.endswith('.dart') and f != 'screen_translations.dart':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
                keys = tr_regex.findall(content)
                for k in keys:
                    used_keys.add((k, path))

# 2. Collect all keys defined in en in screen_translations.dart
with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as fp:
    trans_content = fp.read()

en_block_match = re.search(r"'en':\s*\{(.*?)\n\s*\},", trans_content, re.DOTALL)
if not en_block_match:
    print("Could not find 'en' block!")
    exit(1)

en_keys = set(re.findall(r"'([a-zA-Z0-9_-]+)'\s*:", en_block_match.group(1)))

missing_keys = {}
for k, path in used_keys:
    if k not in en_keys:
        missing_keys[k] = path

print(f"Total keys used: {len({k for k, p in used_keys})}")
print(f"Total keys defined in 'en': {len(en_keys)}")
print(f"Missing keys: {len(missing_keys)}")
for k, path in sorted(missing_keys.items()):
    print(f"  MISSING: '{k}' used in {path}")
