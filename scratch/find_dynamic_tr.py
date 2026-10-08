import os
import re

lib_dir = 'c:\\Users\\ZESTRO\\Desktop\\mindtrap_ai-main\\lib'
for root, _, files in os.walk(lib_dir):
    for f in files:
        if f.endswith('.dart'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fl:
                for idx, line in enumerate(fl, 1):
                    if 'tr(' in line and not re.search(r"tr\(['\"][a-zA-Z0-9_{}]+['\"]\)", line):
                        print(f"{f}:{idx}: {line.strip()}")
