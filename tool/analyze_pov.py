# -*- coding: utf-8 -*-
import json
import re
from collections import Counter

with open('assets/questions/en.json', 'r', encoding='utf-8') as f:
    en_items = json.load(f)

print(f"Total EN items: {len(en_items)}")

# Group by normalized sentence structure
def get_signature(q):
    q_clean = re.sub(r'\b\d+\b', 'NUM', q)
    # take first 6 words
    words = q_clean.split()[:6]
    return ' '.join(words)

signatures = Counter(get_signature(x['question']) for x in en_items)
print("Top 15 repeated POV structures in EN:")
for sig, count in signatures.most_common(15):
    print(f"  [{count}x]: {sig}")
