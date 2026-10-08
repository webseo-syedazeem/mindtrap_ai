# -*- coding: utf-8 -*-
import json
import re
import urllib.request
import urllib.parse
import time

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

print(f"Loaded {len(all_langs)} languages.")

CURATED_EXTRA = {
    'en': {
        'levels_cleared': 'Levels Cleared',
        'world_unlock_req': 'Complete all 40 levels of World {n} to unlock',
        'world_locked': 'World Locked',
        'level_locked': 'Level Locked',
    },
    'ur': {
        'levels_cleared': 'لیولز مکمل',
        'world_unlock_req': 'کھولنے کے لیے دنیا {n} کے تمام 40 لیولز مکمل کریں',
        'world_locked': 'دنیا مقفل ہے',
        'level_locked': 'لیول مقفل ہے',
    },
    'hi': {
        'levels_cleared': 'लेवल पूरे हुए',
        'world_unlock_req': 'अनलॉक करने के लिए वर्ल्ड {n} के सभी 40 लेवल पूरे करें',
        'world_locked': 'वर्ल्ड लॉक है',
        'level_locked': 'लेवल लॉक है',
    },
    'ar': {
        'levels_cleared': 'مستويات مكتملة',
        'world_unlock_req': 'أكمل جميع مستويات العالم {n} الـ 40 لفتحه',
        'world_locked': 'العالم مغلق',
        'level_locked': 'المستوى مغلق',
    },
    'es': {
        'levels_cleared': 'Niveles Completados',
        'world_unlock_req': 'Completa los 40 niveles del Mundo {n} para desbloquear',
        'world_locked': 'Mundo Bloqueado',
        'level_locked': 'Nivel Bloqueado',
    },
    'fr': {
        'levels_cleared': 'Niveaux Terminés',
        'world_unlock_req': 'Terminez les 40 niveaux du Monde {n} pour débloquer',
        'world_locked': 'Monde Verrouillé',
        'level_locked': 'Niveau Verrouillé',
    },
    'de': {
        'levels_cleared': 'Level Abgeschlossen',
        'world_unlock_req': 'Schließe alle 40 Level von Welt {n} ab, um freizuschalten',
        'world_locked': 'Welt Gesperrt',
        'level_locked': 'Level Gesperrt',
    },
}

GOOGLE_MAP = {
    'pt_BR': 'pt', 'pt_PT': 'pt', 'zh_CN': 'zh-CN', 'zh_TW': 'zh-TW',
    'fil': 'tl', 'he': 'iw'
}

keys_to_add = ['levels_cleared', 'world_unlock_req', 'world_locked', 'level_locked']

for code in all_langs:
    if code in CURATED_EXTRA:
        for k, v in CURATED_EXTRA[code].items():
            all_langs[code][k] = v
        print(f"[{code}] Used curated extra")
    else:
        # Translate via Google GTX
        target_lang = GOOGLE_MAP.get(code, code)
        texts = [
            'Levels Cleared',
            'Complete all 40 levels of World {n} to unlock',
            'World Locked',
            'Level Locked'
        ]
        payload = ' ||| '.join(texts)
        try:
            data = urllib.parse.urlencode({'q': payload}).encode('utf-8')
            req = urllib.request.Request(
                f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t',
                data=data,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            res = urllib.request.urlopen(req, timeout=8)
            body = json.loads(res.read().decode('utf-8'))
            translated_chunks = [part[0] for part in body[0] if part and part[0]]
            full_str = ''.join(translated_chunks)
            parts = [p.strip() for p in full_str.split('|||')]
            if len(parts) == 4:
                for k, v in zip(keys_to_add, parts):
                    all_langs[code][k] = v
                print(f"[{code}] Translated extra 4 keys")
            else:
                for k, v in zip(keys_to_add, texts):
                    all_langs[code][k] = v
                print(f"[{code}] Fallback to default")
        except Exception as e:
            for k, v in zip(keys_to_add, texts):
                all_langs[code][k] = v
            print(f"[{code}] Exception {e}, used fallback")

# Re-write screen_translations.dart
output = [
    "// AUTO-GENERATED - DO NOT MODIFY DIRECTLY",
    "// Screen Translations for MindTrap AI (Achievements, Stats/Progress, Daily Challenge, Drawer, Settings, Form, Worlds).",
    "// Complete coverage for all 56 supported languages.",
    "",
    "class ScreenTranslations {",
    "  ScreenTranslations._();",
    "",
    "  static const Map<String, Map<String, String>> data = {",
]

for code, kvs in all_langs.items():
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

print("Successfully updated screen_translations.dart with world unlock & cleared keys for all 56 languages!")
