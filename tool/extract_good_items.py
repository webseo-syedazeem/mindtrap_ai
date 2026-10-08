# -*- coding: utf-8 -*-
import json
import re
from collections import Counter

with open('assets/questions/en.json', 'r', encoding='utf-8') as f:
    en_items = json.load(f)

with open('assets/questions/ur.json', 'r', encoding='utf-8') as f:
    ur_items = json.load(f)

print(f"Total EN: {len(en_items)}, Total UR: {len(ur_items)}")

def get_sig(q):
    q_clean = re.sub(r'\b\d+\b', 'NUM', q)
    return ' '.join(q_clean.split()[:5])

# Count signature frequencies across EN
sigs = Counter(get_sig(x['question']) for x in en_items)

# Separate by difficulty
en_normal = [x for x in en_items if x['difficulty'] == 'normal']
ur_normal = [x for x in ur_items if x['difficulty'] == 'normal']

en_tricky = [x for x in en_items if x['difficulty'] == 'tricky']
ur_tricky = [x for x in ur_items if x['difficulty'] == 'tricky']

# Items whose signature appears <= 2 times across the EN bank
good_normal = []
for e, u in zip(en_normal, ur_normal):
    if sigs[get_sig(e['question'])] <= 2:
        good_normal.append((e, u))

good_tricky = []
for e, u in zip(en_tricky, ur_tricky):
    if sigs[get_sig(e['question'])] <= 2:
        good_tricky.append((e, u))

print(f"Good Normal items (freq <= 2): {len(good_normal)}")
print(f"Good Tricky items (freq <= 2): {len(good_tricky)}")

if good_normal:
    print("Sample Good Normal EN:", good_normal[0][0]['question'])
    print("Sample Good Normal UR:", good_normal[0][1]['question'])
