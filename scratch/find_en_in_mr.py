import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

def parse_lang(code):
    m = re.search(rf"'{code}':\s*\{{(.*?)\}}\s*,\s*'", text, re.DOTALL)
    if not m:
        # try at the end
        m = re.search(rf"'{code}':\s*\{{(.*?)\}}\s*\}};", text, re.DOTALL)
    if not m:
        return {}
    res = {}
    for line in m.group(1).splitlines():
        km = re.match(r"\s*'([a-zA-Z0-9_]+)':\s*'(.*)',?", line)
        if km:
            res[km.group(1)] = km.group(2)
    return res

en_data = parse_lang('en')
mr_data = parse_lang('mr')

print(f"EN keys: {len(en_data)}, MR keys: {len(mr_data)}")

english_in_mr = []
for k, v in mr_data.items():
    if k in en_data and v == en_data[k] and any(c.isalpha() for c in v):
        english_in_mr.append((k, v))

print(f"Total keys in MR that are identical to EN: {len(english_in_mr)}")
for k, v in sorted(english_in_mr):
    print(f"  {k}: {v}")
