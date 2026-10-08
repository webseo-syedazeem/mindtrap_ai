import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

def parse_lang(code):
    m = re.search(rf"'{code}':\s*\{{(.*?)\}}\s*,\s*'", text, re.DOTALL)
    if not m:
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

core_keys = [
    'play', 'worlds', 'worlds_badge', 'worlds_map_sub', 'store', 'hot_deals',
    'daily_rewards', 'free', 'edit_mind_profile', 'language_label', 'tap_to_change',
    'settings', 'config_badge', 'rate_us', 'stars_5_badge', 'levels_odyssey',
    'guest_player', 'sign_in', 'logout', 'sound', 'music', 'vibration'
]

print("Marathi Core Keys Inspection:")
for k in core_keys:
    print(f"  {k} -> {mr_data.get(k)}")
