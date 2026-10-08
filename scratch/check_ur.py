import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r"'ur':\s*\{(.*?)\}", text, re.DOTALL)
if m:
    for line in m.group(1).splitlines():
        if 'daily_reward' in line:
            print(line)
