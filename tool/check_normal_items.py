# -*- coding: utf-8 -*-
import sys
sys.path.append('tool')
import re

mods = [
    'normal_catalog_a',
    'data_normal_part1',
    'catalog_normal_supp1',
    'normal_extra_1',
    'catalog_normal_part1'
]

unique_items = []
seen_en = set()

for mod in mods:
    m = __import__(mod)
    items = getattr(m, 'ITEMS', [])
    for it in items:
        # it can be dict {'en': ..., 'ur': ...} or 8-tuple or 4-tuple
        en = it['en'] if isinstance(it, dict) else it
        q_en = en[0]
        norm = ' '.join(re.sub(r'[^\w\s]', '', q_en.lower()).split())
        if norm not in seen_en:
            seen_en.add(norm)
            unique_items.append(it)

print(f"Total unique normal items from existing catalog files: {len(unique_items)}")

# Check their structure
sample = unique_items[0]
print("Sample type:", type(sample))
if isinstance(sample, dict):
    print("Sample keys:", sample.keys())
    print("EN q:", sample['en'][0])
    print("UR q:", sample['ur'][0])
