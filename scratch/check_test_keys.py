import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

for lang in ['ur', 'es', 'fr']:
    m = re.search(r"'" + lang + r"':\s*\{(.*?)\n    \},", text, re.DOTALL)
    if m:
        block = m.group(1)
        for k in ['total_achievements', 'total_score', 'daily_puzzle']:
            km = re.search(r"'" + k + r"':\s*'([^']*)'", block)
            print(f"{lang} {k} = {km.group(1) if km else None}")
