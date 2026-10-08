with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    c = f.read()

pa_start = c.find("'pa': {")
if pa_start != -1:
    print("pa found in app_language.dart:")
    print(c[pa_start:pa_start+600])
else:
    print("pa NOT in app_language.dart!")

import re
all_t_langs = re.findall(r"'([a-zA-Z_]+)':\s*\{", c)
print("Languages in app_language.dart _translations:", len(all_t_langs))
print(all_t_langs)
