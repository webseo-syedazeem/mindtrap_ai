# -*- coding: utf-8 -*-
with open('tool/build_en_bank.py', 'r', encoding='utf-8') as f:
    text_en = f.read()

with open('tool/build_ur_bank.py', 'r', encoding='utf-8') as f:
    text_ur = f.read()

print("EN total characters:", len(text_en))
print("UR total characters:", len(text_ur))

# Let's count how many questions are defined without puzzle_families
pf_en_pos = text_en.find('import puzzle_families')
print("EN code before puzzle_families length:", pf_en_pos)

import re
tuples_en = re.findall(r'\(\s*"([^"]+)",\s*\[([^\]]+)\],\s*"([^"]+)",\s*"([^"]+)"\s*\)', text_en[:pf_en_pos])
print("EN explicit tuples before pf:", len(tuples_en))

tuples_ur = re.findall(r'\(\s*"([^"]+)",\s*\[([^\]]+)\],\s*"([^"]+)",\s*"([^"]+)"\s*\)', text_ur)
print("UR explicit tuples total in file:", len(tuples_ur))
