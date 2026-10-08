# -*- coding: utf-8 -*-
import sys
sys.path.append('tool')
import re

with open('tool/build_en_bank.py', 'r', encoding='utf-8') as f:
    en_content = f.read()

with open('tool/build_ur_bank.py', 'r', encoding='utf-8') as f:
    ur_content = f.read()

# Let's see how many items in deduction_puzzles etc.
print("Length of build_en_bank:", len(en_content))
print("Length of build_ur_bank:", len(ur_content))
