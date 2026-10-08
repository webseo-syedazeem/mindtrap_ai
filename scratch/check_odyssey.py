import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r"'([a-z_]+)':\s*\{[^}]*'levels_odyssey':\s*'([^']*)'", text)
for code, val in m[:15]:
    print(f"{code}: {val}")
