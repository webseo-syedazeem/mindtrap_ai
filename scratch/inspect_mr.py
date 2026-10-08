import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("'mr':")
end_idx = text.find("},\n    'ta':", idx)
mr_block = text[idx:end_idx]

for line in mr_block.splitlines():
    if any(k in line for k in ['play', 'guest', 'world', 'store', 'reward', 'setting', 'rate', 'language']):
        print(line)
