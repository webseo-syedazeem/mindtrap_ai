# -*- coding: utf-8 -*-
import json
import os
import sys
import time
import urllib.request
import urllib.parse

def translate_batch(strings, target_lang):
    text = ' ||| '.join(strings)
    encoded = urllib.parse.quote(text)
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={encoded}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    for attempt in range(3):
        try:
            res = urllib.request.urlopen(req, timeout=12)
            data = json.loads(res.read().decode('utf-8'))
            translated = ''.join([part[0] for part in data[0] if part[0]])
            parts = [p.strip() for p in translated.split('|||')]
            if len(parts) == len(strings):
                return parts
            time.sleep(0.5)
        except Exception as e:
            time.sleep(1)
    return strings

def translate_file(target_lang, output_path):
    with open('assets/questions/en.json', 'r', encoding='utf-8') as f:
        en_items = json.load(f)

    print(f"Translating {len(en_items)} questions to {target_lang}...")
    batch_size = 25
    translated_items = []

    for i in range(0, len(en_items), batch_size):
        chunk = en_items[i:i + batch_size]
        batch_strings = []
        for item in chunk:
            batch_strings.append(item['question'])
            batch_strings.extend(item['options'])
            batch_strings.append(item['explanation'])

        res_strings = translate_batch(batch_strings, target_lang)
        
        idx = 0
        for item in chunk:
            q_trans = res_strings[idx] if idx < len(res_strings) else item['question']
            idx += 1
            opts_trans = []
            for _ in range(4):
                opts_trans.append(res_strings[idx] if idx < len(res_strings) else 'Option')
                idx += 1
            exp_trans = res_strings[idx] if idx < len(res_strings) else item['explanation']
            idx += 1

            # Match answer
            orig_ans_idx = item['options'].index(item['correctAnswer']) if item['correctAnswer'] in item['options'] else 0
            ans_trans = opts_trans[orig_ans_idx]

            translated_items.append({
                "id": item['id'],
                "difficulty": item['difficulty'],
                "question": q_trans,
                "options": opts_trans,
                "correctAnswer": ans_trans,
                "explanation": exp_trans
            })
        print(f"[{target_lang}] Translated {len(translated_items)} / {len(en_items)}")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translated_items, f, ensure_ascii=False, indent=2)
    print(f"Saved: {output_path}")

if __name__ == '__main__':
    langs = sys.argv[1:]
    for l in langs:
        translate_file(l, f'assets/questions/{l}.json')
