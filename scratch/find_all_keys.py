import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

keys = set()
for root, dirs, files in os.walk('lib'):
    for f in files:
        if f.endswith('.dart'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
                # find tr('key') or tr("key")
                found = re.findall(r"tr\(\s*['\"]([a-zA-Z0-9_]+)['\"]\s*[\),]", content)
                keys.update(found)
                # find AppStrings.get('key')
                found2 = re.findall(r"AppStrings\.get\(\s*['\"]([a-zA-Z0-9_]+)['\"]\s*\)", content)
                keys.update(found2)

print(f"Total unique keys in code: {len(keys)}")
for k in sorted(keys):
    print(k)
