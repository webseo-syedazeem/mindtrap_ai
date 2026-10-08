with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    c = f.read()

pa_start = c.find("'pa': {")
if pa_start != -1:
    pa_end = c.find("},", pa_start)
    block = c[pa_start:pa_end]
    import re
    pairs = re.findall(r"'([a-zA-Z0-9_]+)':\s*'([^']*)'", block)
    print("Total keys in 'pa':", len(pairs))
    d = dict(pairs)
    for k in ['worlds', 'daily_rewards', 'edit_mind_profile', 'rate_us', 'settings', 'store']:
        print(f"Key {k}: {repr(d.get(k))}")
