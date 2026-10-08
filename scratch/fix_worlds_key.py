# -*- coding: utf-8 -*-
with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    c = f.read()

target = "'worlds': 'دنیا (WORLDS)',"
repl = "'worlds': 'دنیا',"
if target in c:
    c = c.replace(target, repl)
    with open('lib/localization/app_language.dart', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced worlds key successfully!")
else:
    print("Target not found!")
