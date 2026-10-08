# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lib/localization/extended_app_strings.dart', 'r', encoding='utf-8') as f:
    text = f.read()

test_langs = ['en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'es', 'ar', 'fr', 'de', 'ru', 'tr', 'zh_CN', 'ja']
for l in test_langs:
    tag = f"'{l}':"
    idx = text.find(tag)
    if idx == -1:
        print(f"FAIL: {l} not found")
        continue
    first_line = text[idx:idx+400].splitlines()[1].strip()
    print(f"{l:6} -> {first_line[:50]}")
