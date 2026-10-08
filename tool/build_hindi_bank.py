# -*- coding: utf-8 -*-
"""
High-Speed Resilient Hindi Question Bank Builder (1,000 Non-repeating items)
Matches exact tiers:
  Levels 1 - 250: Easy
  Levels 251 - 650: Normal
  Levels 651 - 1000: Tricky
"""

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import translators as ts

sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILE = 'assets/questions/hi.json'
TMP_FILE = 'assets/questions/hi.json.tmp'
SOURCE_FILE = 'assets/questions/en.json'

def load_source():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def translate_single_item(item, max_retries=3):
    """Translate one single item (6 lines) as fallback."""
    lines = [item['question']] + item['options'] + [item['explanation']]
    payload = '\n'.join(lines)
    for attempt in range(max_retries):
        try:
            res = ts.translate_text(payload, from_language='en', to_language='hi', translator='bing')
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
        except Exception as e:
            time.sleep(1 + attempt)
    
    # If still fails, translate parts individually
    try:
        q_trans = ts.translate_text(item['question'], from_language='en', to_language='hi', translator='bing').strip()
        opts_trans = []
        for o in item['options']:
            opts_trans.append(ts.translate_text(o, from_language='en', to_language='hi', translator='bing').strip())
        exp_trans = ts.translate_text(item['explanation'], from_language='en', to_language='hi', translator='bing').strip()
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
        print(f"Fallback error on item {item['id']}: {e}")
        return None

def translate_chunk(chunk, max_retries=2):
    """Translates a chunk of up to 5 items."""
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
            res = ts.translate_text(payload, from_language='en', to_language='hi', translator='bing')
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
        except Exception as e:
            time.sleep(1 + attempt)

    # Fallback to single item translation
    results = []
    for it in chunk:
        res_it = translate_single_item(it)
        if res_it:
            results.append(res_it)
        else:
            raise RuntimeError(f"Failed to translate item {it['id']}")
    return results

def main():
    source_items = load_source()
    total_items = len(source_items)
    print(f"Loaded {total_items} English source items.")

    existing_results = {}
    if os.path.exists(TARGET_FILE):
        try:
            with open(TARGET_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for it in data:
                    existing_results[it['id']] = it
            print(f"Resuming: found {len(existing_results)} already translated items in {TARGET_FILE}")
        except Exception:
            pass

    # Group uncompleted items into chunks of 5
    uncompleted = [it for it in source_items if it['id'] not in existing_results]
    print(f"Remaining items to translate: {len(uncompleted)}")

    if not uncompleted:
        print("All items already translated!")
        return

    chunk_size = 5
    chunks = [uncompleted[i:i + chunk_size] for i in range(0, len(uncompleted), chunk_size)]
    print(f"Processing in {len(chunks)} chunks of size {chunk_size} with 4 threads...")

    completed_count = len(existing_results)
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_chunk = {executor.submit(translate_chunk, chunk): chunk for chunk in chunks}
        for future in as_completed(future_to_chunk):
            try:
                res_list = future.result()
                for r in res_list:
                    existing_results[r['id']] = r
                completed_count += len(res_list)
                
                # Checkpoint save every 20 items
                if len(existing_results) % 20 == 0 or completed_count == total_items:
                    sorted_bank = [existing_results[i] for i in sorted(existing_results.keys())]
                    with open(TMP_FILE, 'w', encoding='utf-8') as f:
                        json.dump(sorted_bank, f, ensure_ascii=False, indent=2)
                    os.replace(TMP_FILE, TARGET_FILE)
                    elapsed = time.time() - start_time
                    rate = (completed_count - len(source_items) + len(uncompleted)) / max(elapsed, 1)
                    print(f"Progress: {completed_count}/{total_items} ({completed_count*100//total_items}%) - Rate: {rate:.1f} items/s")
            except Exception as e:
                print(f"Chunk failed: {e}")

    # Final save and verification
    final_bank = [existing_results[i] for i in sorted(existing_results.keys())]
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_bank, f, ensure_ascii=False, indent=2)

    print(f"\nCompleted! Saved {len(final_bank)} items to {TARGET_FILE}")

    # Integrity verification
    easy_count = sum(1 for x in final_bank if x['difficulty'] == 'easy')
    normal_count = sum(1 for x in final_bank if x['difficulty'] == 'normal')
    tricky_count = sum(1 for x in final_bank if x['difficulty'] == 'tricky')
    print(f"Easy: {easy_count}, Normal: {normal_count}, Tricky: {tricky_count}")
    assert len(final_bank) == 1000, f"Expected 1000 items, got {len(final_bank)}"
    for it in final_bank:
        assert len(it['options']) == 4, f"Item {it['id']} does not have 4 options"
        assert it['correctAnswer'] in it['options'], f"Item {it['id']} answer not in options"

if __name__ == '__main__':
    main()
