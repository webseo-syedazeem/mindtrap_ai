# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import time

def translate_phrase(text, target_lang):
    if target_lang == 'en':
        return text
    # mapping of lang codes to google translate codes
    gt_map = {
        'pt_BR': 'pt', 'pt_PT': 'pt', 'zh_CN': 'zh-CN', 'zh_TW': 'zh-TW',
        'fil': 'tl', 'he': 'iw'
    }
    lang = gt_map.get(target_lang, target_lang)
    q = urllib.parse.quote(text)
    url = f'https://translate.google.com/m?sl=en&tl={lang}&q={q}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'})
    try:
        res = urllib.request.urlopen(req, timeout=4)
        html = res.read().decode('utf-8')
        m = re.search(r'class="result-container">([^<]+)', html)
        if m:
            import html as html_module
            return html_module.unescape(m.group(1).strip())
    except Exception as e:
        pass
    return text

# Test for Spanish and French
print("ES:", translate_phrase("Game Menu", "es"))
print("FR:", translate_phrase("1,000 Levels Odyssey", "fr"))
