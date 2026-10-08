import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# For each language, check world_0_title, world_0_subtitle, world_0_lore
pattern = re.compile(r"'([a-z_]{2,5})':\s*\{(.*?)\}(?=,\s*'|\s*\};)", re.DOTALL)
langs = {}
for m in pattern.finditer(text):
    code = m.group(1)
    body = m.group(2)
    w0_title = re.search(r"'world_0_title':\s*'([^']*)'", body)
    w0_lore = re.search(r"'world_0_lore':\s*'([^']*)'", body)
    langs[code] = {
        'title': w0_title.group(1) if w0_title else None,
        'lore': w0_lore.group(1) if w0_lore else None,
    }

print(f"Total parsed languages: {len(langs)}")
en_title = "Sunset Meadow"
en_lore = "Bask in golden sunlight across blooming wildflower hills where foundational logic begins."

translated_count = 0
for code, vals in langs.items():
    is_trans = vals['title'] != en_title and vals['lore'] != en_lore and vals['title'] is not None
    if is_trans:
        translated_count += 1
        print(f"TRANSLATED: {code} -> Title: {vals['title']}")
    else:
        print(f"ENGLISH: {code} -> Title: {vals['title']}")

print(f"\nTotal translated: {translated_count}, Total English: {len(langs) - translated_count}")
