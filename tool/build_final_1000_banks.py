# -*- coding: utf-8 -*-
"""
Build final 1000 question banks for EN and UR.
1 - 250: Easy
251 - 650: Normal
651 - 1000: Tricky
"""

import json
import os
import sys

sys.path.insert(0, '.')
sys.path.insert(0, 'tool')

from tool.catalog_easy import EASY_ITEMS as easy_items
from tool.catalog_normal import ITEMS as normal_items
from tool.catalog_tricky import ITEMS as tricky_items

print(f"Loaded Easy: {len(easy_items)}")
print(f"Loaded Normal: {len(normal_items)}")
print(f"Loaded Tricky: {len(tricky_items)}")

assert len(easy_items) == 250, f"Expected 250 easy items, got {len(easy_items)}"
assert len(normal_items) == 400, f"Expected 400 normal items, got {len(normal_items)}"
assert len(tricky_items) == 350, f"Expected 350 tricky items, got {len(tricky_items)}"

en_bank = []
ur_bank = []

# Process Easy (1-250)
for idx, it in enumerate(easy_items, start=1):
    en_it = it['en']
    ur_it = it['ur']
    
    en_bank.append({
        "id": idx,
        "difficulty": "easy",
        "question": en_it[0].strip(),
        "options": [str(o).strip() for o in en_it[1]],
        "correctAnswer": str(en_it[2]).strip(),
        "explanation": str(en_it[3]).strip()
    })
    
    ur_bank.append({
        "id": idx,
        "difficulty": "easy",
        "question": ur_it[0].strip(),
        "options": [str(o).strip() for o in ur_it[1]],
        "correctAnswer": str(ur_it[2]).strip(),
        "explanation": str(ur_it[3]).strip()
    })

# Process Normal (251-650)
for idx, it in enumerate(normal_items, start=251):
    en_bank.append({
        "id": idx,
        "difficulty": "normal",
        "question": it[0].strip(),
        "options": [str(o).strip() for o in it[1]],
        "correctAnswer": str(it[2]).strip(),
        "explanation": str(it[3]).strip()
    })
    
    ur_bank.append({
        "id": idx,
        "difficulty": "normal",
        "question": it[4].strip(),
        "options": [str(o).strip() for o in it[5]],
        "correctAnswer": str(it[6]).strip(),
        "explanation": str(it[7]).strip()
    })

# Process Tricky (651-1000)
for idx, it in enumerate(tricky_items, start=651):
    en_bank.append({
        "id": idx,
        "difficulty": "tricky",
        "question": it[0].strip(),
        "options": [str(o).strip() for o in it[1]],
        "correctAnswer": str(it[2]).strip(),
        "explanation": str(it[3]).strip()
    })
    
    ur_bank.append({
        "id": idx,
        "difficulty": "tricky",
        "question": it[4].strip(),
        "options": [str(o).strip() for o in it[5]],
        "correctAnswer": str(it[6]).strip(),
        "explanation": str(it[7]).strip()
    })

print(f"Final EN bank size: {len(en_bank)}")
print(f"Final UR bank size: {len(ur_bank)}")

# Verification
for name, bank in [("EN", en_bank), ("UR", ur_bank)]:
    questions = set()
    for item in bank:
        q = item["question"]
        assert q not in questions, f"Duplicate question in {name}: {q}"
        questions.add(q)
        assert len(item["options"]) == 4, f"Options count != 4 in {name} id={item['id']}"
        assert item["correctAnswer"] in item["options"], f"Answer not in options in {name} id={item['id']}: '{item['correctAnswer']}'"
        assert not any(tag in q for tag in ["Warm-up", "مرحلہ", "سوال #", "(سوال"]), f"Robotic tag in {name} id={item['id']}"

os.makedirs("assets/questions", exist_ok=True)

with open("assets/questions/en.json", "w", encoding="utf-8") as f:
    json.dump(en_bank, f, ensure_ascii=False, indent=2)

with open("assets/questions/ur.json", "w", encoding="utf-8") as f:
    json.dump(ur_bank, f, ensure_ascii=False, indent=2)

print("SUCCESS: Both assets/questions/en.json and assets/questions/ur.json compiled with exactly 1,000 unique questions!")
