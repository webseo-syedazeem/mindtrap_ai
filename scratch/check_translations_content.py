import re

with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r"'([a-zA-Z_]+)':\s*\{([^}]+)\}"
matches = re.findall(pattern, c)

for code, block in matches:
    if code in ['pa', 'bn', 'es', 'fr', 'ru']:
        kv = dict(re.findall(r"'([a-zA-Z0-9_]+)':\s*'([^']*)'", block))
        print(f"[{code}] settings={ascii(kv.get('settings'))}, store={ascii(kv.get('store'))}, play={ascii(kv.get('play'))}")
