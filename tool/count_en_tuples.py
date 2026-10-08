# -*- coding: utf-8 -*-
with open('tool/build_en_bank.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find all string tuples
pattern = r'\(\s*"([^"]+)",\s*\[([^\]]+)\],\s*"([^"]+)",\s*"([^"]+)"\s*\)'
matches = re.findall(pattern, text)
print(f"Total tuple matches in build_en_bank.py: {len(matches)}")

# Let's inspect unique question stems
stems = [m[0].strip() for m in matches]
print(f"Unique question stems: {len(set(stems))}")
