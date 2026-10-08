# -*- coding: utf-8 -*-
import json
import os
import re
import time
import urllib.request
import urllib.parse
from base_dictionaries import EN_ACH, EN_DRAWER, UR_ACH, UR_DRAWER, HI_ACH, HI_DRAWER, AR_ACH, AR_DRAWER

ALL_CODES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

GOOGLE_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt',
    'zh_CN': 'zh-CN',
    'zh_TW': 'zh-TW',
    'fil': 'tl',
    'he': 'iw',
}

PRESETS = {
    'en': {**EN_ACH, **EN_DRAWER},
    'ur': {**UR_ACH, **UR_DRAWER},
    'hi': {**HI_ACH, **HI_DRAWER},
    'ar': {**AR_ACH, **AR_DRAWER},
}

# The keys and English values to translate
NEW_KEYS = list(EN_ACH.keys()) + list(EN_DRAWER.keys())
EN_VALUES = [EN_ACH.get(k, EN_DRAWER.get(k)) for k in NEW_KEYS]

print(f"Total keys to ensure across all 56 languages: {len(NEW_KEYS)}")

# Read current screen_translations.dart
file_path = 'lib/localization/screen_translations.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    orig_code = f.read()

pattern = r"'([a-zA-Z_]+)':\s*\{([^}]+)\}"
matches = re.findall(pattern, orig_code)

all_langs = {}
for code, block in matches:
    kv_pattern = r"'([a-zA-Z0-9_]+)':\s*'([^']*)'"
    pairs = re.findall(kv_pattern, block)
    all_langs[code] = dict(pairs)

print(f"Parsed {len(all_langs)} languages from current file.")

def translate_batch(target_code, texts):
    lang = GOOGLE_MAP.get(target_code, target_code)
    # Join with distinct delimiter that survives translation
    delimiter = " ||| "
    payload = delimiter.join(texts)
    data = urllib.parse.urlencode({'q': payload}).encode('utf-8')
    req = urllib.request.Request(
        f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={lang}&dt=t',
        data=data,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    for attempt in range(3):
        try:
            res = urllib.request.urlopen(req, timeout=12)
            body = json.loads(res.read().decode('utf-8'))
            translated_chunks = [part[0] for part in body[0] if part and part[0]]
            full_str = ''.join(translated_chunks)
            parts = [p.strip() for p in full_str.split("|||")]
            if len(parts) == len(texts):
                return parts
            # If length mismatch, retry with newlines
            lines = [p.strip() for p in full_str.split("\n") if p.strip()]
            if len(lines) == len(texts):
                return lines
            print(f"Warning: split count {len(parts)} != expected {len(texts)} for {target_code}")
        except Exception as e:
            print(f"Attempt {attempt+1} failed for {target_code}: {e}")
            time.sleep(1)
    return texts

for code in ALL_CODES:
    if code in PRESETS:
        preset_map = PRESETS[code]
        if code not in all_langs:
            all_langs[code] = {}
        for k, v in preset_map.items():
            all_langs[code][k] = v
        print(f"[{code}] Used handcrafted preset ({len(preset_map)} keys)")
    else:
        print(f"[{code}] Translating {len(NEW_KEYS)} keys...")
        translated = translate_batch(code, EN_VALUES)
        if code not in all_langs:
            all_langs[code] = {}
        for k, v in zip(NEW_KEYS, translated):
            all_langs[code][k] = v
        time.sleep(0.3)

# Write output file
output = [
    "// AUTO-GENERATED - DO NOT MODIFY DIRECTLY",
    "// Screen Translations for MindTrap AI (Achievements, Stats/Progress, Daily Challenge, Drawer, Settings, Form).",
    "// Complete coverage for all 56 supported languages.",
    "",
    "class ScreenTranslations {",
    "  ScreenTranslations._();",
    "",
    "  static const Map<String, Map<String, String>> data = {",
]

for code in ALL_CODES:
    kvs = all_langs.get(code, {})
    output.append(f"    '{code}': {{")
    for k, v in kvs.items():
        escaped_v = v.replace("\\", "\\\\").replace("'", "\\'")
        output.append(f"      '{k}': '{escaped_v}',")
    output.append("    },")

output.append("  };")
output.append("}")
output.append("")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(output))

print(f"SUCCESS! Wrote full screen_translations.dart for all {len(ALL_CODES)} languages!")
