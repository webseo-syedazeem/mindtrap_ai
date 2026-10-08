import json
import re

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    app_lang_text = f.read()

en_world_0_lore = "Bask in golden sunlight across blooming wildflower hills where foundational logic begins."
en_count = app_lang_text.count(en_world_0_lore)
print(f"Occurrences of English world_0_lore in app_language.dart: {en_count}")

# Check which languages in app_language.dart contain it
for m in re.finditer(r"'([a-z_]{2,5})':\s*\{", app_lang_text):
    code = m.group(1)
    start = m.start()
    # search next 6000 chars
    chunk = app_lang_text[start:start+7000]
    if en_world_0_lore in chunk and code != 'en':
        print(f"Language '{code}' in app_language.dart has ENGLISH world_0_lore!")

# Check cache for style_dawn_awaking
with open('scratch/screen_translations_cache.json', 'r', encoding='utf-8') as f:
    cache = json.load(f)

for code, d in cache.items():
    if code == 'en': continue
    s = d.get('style_dawn_awaking', '')
    if s == 'Dawn Awaking' or s == '':
        print(f"Cache language '{code}' has style_dawn_awaking = '{s}'")
