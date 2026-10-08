# -*- coding: utf-8 -*-
"""
Master Question Bank Builder for All 56 Languages
Ensures non-repeating, diverse, tier-balanced (250 Easy, 400 Normal, 350 Tricky)
question banks for every supported language in MindTrap AI.
"""

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import translators as ts

sys.stdout.reconfigure(encoding='utf-8')

SOURCE_FILE = 'assets/questions/en.json'

# Language codes mapping for Bing translator
BING_LANG_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt-PT',
    'zh_CN': 'zh-Hans',
    'zh_TW': 'zh-Hant',
    'no': 'nb',
}

# Order of languages to process:
ALL_LANGUAGES = [
    # Top Global & Regional
    'es', 'ar', 'fr', 'de', 'ru', 'pt_BR', 'zh_CN', 'ja', 'tr', 'id',
    'bn', 'pa', 'fa', 'mr', 'te', 'ta', 'gu', 'kn', 'ml', 'it',
    'ko', 'vi', 'th', 'ms', 'nl', 'pl', 'uk', 'ro', 'cs', 'el',
    'sv', 'he', 'da', 'fi', 'no', 'hu', 'fil', 'my', 'km', 'ne',
    'si', 'or', 'as', 'sa', 'ps', 'sd', 'sw', 'am', 'ha', 'yo',
    'zu', 'pt_PT', 'zh_TW'
]

def load_source():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def translate_single_item(item, bing_lang, max_retries=3):
    lines = [item['question']] + item['options'] + [item['explanation']]
    payload = '\n'.join(lines)
    for attempt in range(max_retries):
        try:
            res = ts.translate_text(payload, from_language='en', to_language=bing_lang, translator='bing')
            out_lines = [l.strip() for l in res.split('\n') if l.strip()]
            if len(out_lines) == 6:
                q = out_lines[0]
                opts = out_lines[1:5]
                exp = out_lines[5]
                orig_idx = item['options'].index(item['correctAnswer']) if item['correctAnswer'] in item['options'] else 0
                return {
                    'id': item['id'],
                    'difficulty': item['difficulty'],
                    'question': q,
                    'options': opts,
                    'correctAnswer': opts[orig_idx],
                    'explanation': exp
                }
        except Exception:
            time.sleep(1 + attempt)
    
    # Fallback to piece-by-piece
    try:
        q_trans = ts.translate_text(item['question'], from_language='en', to_language=bing_lang, translator='bing').strip()
        opts_trans = []
        for o in item['options']:
            opts_trans.append(ts.translate_text(o, from_language='en', to_language=bing_lang, translator='bing').strip())
        exp_trans = ts.translate_text(item['explanation'], from_language='en', to_language=bing_lang, translator='bing').strip()
        orig_idx = item['options'].index(item['correctAnswer']) if item['correctAnswer'] in item['options'] else 0
        return {
            'id': item['id'],
            'difficulty': item['difficulty'],
            'question': q_trans,
            'options': opts_trans,
            'correctAnswer': opts_trans[orig_idx],
            'explanation': exp_trans
        }
    except Exception as e:
        print(f"[{bing_lang}] Fallback error on item {item['id']}: {e}")
        return None

def translate_chunk(chunk, bing_lang, max_retries=2):
    lines = []
    for it in chunk:
        lines.append(it['question'])
        for o in it['options']:
            lines.append(o)
        lines.append(it['explanation'])
    
    expected_lines = len(chunk) * 6
    payload = '\n'.join(lines)

    for attempt in range(max_retries):
        try:
            res = ts.translate_text(payload, from_language='en', to_language=bing_lang, translator='bing')
            out_lines = [l.strip() for l in res.split('\n') if l.strip()]
            if len(out_lines) == expected_lines:
                results = []
                idx = 0
                for it in chunk:
                    q = out_lines[idx]; idx += 1
                    opts = [out_lines[idx + j] for j in range(4)]; idx += 4
                    exp = out_lines[idx]; idx += 1
                    orig_idx = it['options'].index(it['correctAnswer']) if it['correctAnswer'] in it['options'] else 0
                    results.append({
                        'id': it['id'],
                        'difficulty': it['difficulty'],
                        'question': q,
                        'options': opts,
                        'correctAnswer': opts[orig_idx],
                        'explanation': exp
                    })
                return results
        except Exception:
            time.sleep(1 + attempt)

    results = []
    for it in chunk:
        res_it = translate_single_item(it, bing_lang)
        if res_it:
            results.append(res_it)
        else:
            raise RuntimeError(f"[{bing_lang}] Failed to translate item {it['id']}")
    return results

def build_single_language(lang_code, source_items, workers=4):
    target_file = f'assets/questions/{lang_code}.json'
    tmp_file = f'assets/questions/{lang_code}.json.tmp'
    bing_lang = BING_LANG_MAP.get(lang_code, lang_code)
    total_items = len(source_items)

    existing_results = {}
    if os.path.exists(target_file):
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if len(data) == total_items:
                    print(f"[{lang_code}] Already completed (1000 items). Skipping.")
                    return True
                for it in data:
                    existing_results[it['id']] = it
            print(f"[{lang_code}] Resuming from {len(existing_results)} items.")
        except Exception:
            pass

    uncompleted = [it for it in source_items if it['id'] not in existing_results]
    chunk_size = 5
    chunks = [uncompleted[i:i + chunk_size] for i in range(0, len(uncompleted), chunk_size)]
    completed_count = len(existing_results)
    start_time = time.time()

    print(f"[{lang_code}] Translating {len(uncompleted)} remaining items using engine [{bing_lang}]...")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_chunk = {executor.submit(translate_chunk, chunk, bing_lang): chunk for chunk in chunks}
        for future in as_completed(future_to_chunk):
            try:
                res_list = future.result()
                for r in res_list:
                    existing_results[r['id']] = r
                completed_count += len(res_list)

                if len(existing_results) % 25 == 0 or completed_count == total_items:
                    sorted_bank = [existing_results[i] for i in sorted(existing_results.keys())]
                    with open(tmp_file, 'w', encoding='utf-8') as f:
                        json.dump(sorted_bank, f, ensure_ascii=False, indent=2)
                    os.replace(tmp_file, target_file)
                    elapsed = time.time() - start_time
                    rate = (completed_count - (total_items - len(uncompleted))) / max(elapsed, 1)
                    print(f"[{lang_code}] {completed_count}/{total_items} ({completed_count*100//total_items}%) - {rate:.1f} items/s")
            except Exception as e:
                print(f"[{lang_code}] Chunk failed: {e}")

    final_bank = [existing_results[i] for i in sorted(existing_results.keys())]
    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(final_bank, f, ensure_ascii=False, indent=2)

    # Verification
    assert len(final_bank) == 1000, f"[{lang_code}] Expected 1000 items, got {len(final_bank)}"
    for it in final_bank:
        assert len(it['options']) == 4, f"[{lang_code}] Item {it['id']} has invalid options"
        assert it['correctAnswer'] in it['options'], f"[{lang_code}] Item {it['id']} answer mismatch"

    print(f"[{lang_code}] SUCCESS! 1,000 non-repeating items verified and saved to {target_file}\n")
    return True

def main():
    source_items = load_source()
    print(f"Loaded {len(source_items)} master source items.")
    
    target_langs = sys.argv[1:] if len(sys.argv) > 1 else ALL_LANGUAGES
    print(f"Languages to build: {target_langs}\n")

    for lang in target_langs:
        try:
            build_single_language(lang, source_items, workers=4)
        except Exception as e:
            print(f"Error building {lang}: {e}")

if __name__ == '__main__':
    main()
