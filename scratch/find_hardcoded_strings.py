import os
import re

lib_dir = 'c:\\Users\\ZESTRO\\Desktop\\mindtrap_ai-main\\lib'

# Regex for Text('...') or Text("...")
pattern = re.compile(r"Text\(\s*['\"]([^'\"]+)['\"]")

ignore_extensions = ['translations.dart', 'app_language.dart', 'extended_app_strings.dart']

hardcoded_findings = []

for root, _, files in os.walk(lib_dir):
    for f in files:
        if f.endswith('.dart') and not any(ign in f for ign in ignore_extensions):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fl:
                for idx, line in enumerate(fl, 1):
                    for match in pattern.finditer(line):
                        text = match.group(1).strip()
                        # ignore icon fonts, numbers, asset paths, empty
                        if (re.search(r'[a-zA-Z]{3,}', text) and 
                            not text.startswith('assets/') and 
                            not text.startswith('http') and 
                            not text.startswith('package:') and
                            not text.endswith('.png') and
                            not text.endswith('.webp') and
                            not text.endswith('.jpg')):
                            hardcoded_findings.append((f, idx, text, line.strip()))

print(f"Total potential hardcoded English strings in UI: {len(hardcoded_findings)}")
for f, idx, text, line in hardcoded_findings[:50]:
    print(f"{f}:{idx} -> '{text}'")
