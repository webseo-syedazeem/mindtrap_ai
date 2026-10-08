import os
import re

lib_dir = 'c:\\Users\\ZESTRO\\Desktop\\mindtrap_ai-main\\lib'
dart_files = []
for root, _, files in os.walk(lib_dir):
    for f in files:
        if f.endswith('.dart'):
            dart_files.append(os.path.join(root, f))

# Find all tr('...') calls in all dart files
tr_keys = set()
for fpath in dart_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r"tr\(['\"]([a-zA-Z0-9_{}]+)['\"]\)", content)
    for m in matches:
        tr_keys.add(m)

print(f"Total distinct tr() keys used in code: {len(tr_keys)}")
print(sorted(list(tr_keys)))
