import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/screen_translations_cache.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total languages in cache: {len(d)}")
for lang, kvs in d.items():
    print(f"{lang}: {len(kvs)} keys")
