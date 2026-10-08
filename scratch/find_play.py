import re

with open('lib/main.dart', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'lets_map_your_mind', text)]
for idx in matches:
    print(text[max(0, idx-200):min(len(text), idx+300)])
    print('='*50)
