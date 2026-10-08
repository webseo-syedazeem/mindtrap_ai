import json
import re

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    app_text = f.read()

# Extract 'en' dictionary from app_language.dart
en_match = re.search(r"'en':\s*\{([^}]+)\}", app_text)
en_keys_app = []
if en_match:
    en_keys_app = re.findall(r"'([a-zA-Z0-9_]+)':", en_match.group(1))

print(f"Total EN keys in app_language.dart: {len(en_keys_app)}")

# Extract 'en' from ScreenTranslations
with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    screen_text = f.read()

en_screen_match = re.search(r"'en':\s*\{([^}]+)\}", screen_text)
en_keys_screen = []
if en_screen_match:
    en_keys_screen = re.findall(r"'([a-zA-Z0-9_]+)':", en_screen_match.group(1))

print(f"Total EN keys in screen_translations.dart: {len(en_keys_screen)}")

# Extract 'en' from ExtendedAppStrings
with open('lib/localization/extended_app_strings.dart', 'r', encoding='utf-8') as f:
    ext_text = f.read()

en_ext_match = re.search(r"'en':\s*\{([^}]+)\}", ext_text)
en_keys_ext = []
if en_ext_match:
    en_keys_ext = re.findall(r"'([a-zA-Z0-9_]+)':", en_ext_match.group(1))

print(f"Total EN keys in extended_app_strings.dart: {len(en_keys_ext)}")

print("\nSample EN keys in app_language:", en_keys_app[:20])
print("\nSample EN keys in screen_translations:", en_keys_screen[:20])
