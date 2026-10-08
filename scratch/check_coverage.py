# -*- coding: utf-8 -*-
import re

with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

LANG_CODES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

all_langs = {c: {} for c in LANG_CODES}
current_lang = None

for line in text.splitlines():
    stripped = line.strip()
    m_lang = re.match(r"^'([a-zA-Z_]+)':\s*\{", stripped)
    if m_lang and m_lang.group(1) in LANG_CODES:
        current_lang = m_lang.group(1)
        continue
    if stripped.startswith('},') or stripped == '}':
        current_lang = None
        continue
    if current_lang is not None:
        m_kv = re.match(r"^'([a-zA-Z0-9_]+)':\s*'(.*)',?$", stripped)
        if m_kv:
            all_langs[current_lang][m_kv.group(1)] = m_kv.group(2)

print(f'Total langs: {len(all_langs)}')

keys_to_check = [
    'thanks_journey', 'select_world', 'world', 'guest', 'pro',
    'guest_player', 'tap_to_sync', 'logout', 'sign_in',
    'search_language', 'no_languages_found', 'device_support_may_vary', 'profile',
    'worlds', 'worlds_map_sub', 'worlds_badge', 'game_menu', 'languages',
    'levels_odyssey', 'daily_rewards', 'rate_us', 'settings',
    'style_dawn_awaking', 'style_star_cluster', 'style_cyber_vector',
    'style_void_vortex', 'style_dimensional_rift', 'style_zenith_pinnacle'
]

for k in keys_to_check:
    missing = [c for c in LANG_CODES if k not in all_langs[c]]
    if missing:
        print(f"Key [{k}] MISSING in {len(missing)}: {missing}")
    else:
        print(f"Key [{k}] PRESENT in all 56 langs!")
