import urllib.request
import json
import urllib.parse
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

GT_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt',
    'zh_CN': 'zh-CN',
    'zh_TW': 'zh-TW',
    'fil': 'tl',
    'he': 'iw',
}

LANGUAGES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

def translate(text, lang):
    tl = GT_MAP.get(lang, lang)
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={tl}&dt=t&q=" + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read().decode('utf-8'))
        return ''.join([p[0] for p in data[0] if p and p[0]])
    except Exception as e:
        return None

print(f"Testing translation of 'Level' and 'Dawn Awaking' across all {len(LANGUAGES)} languages...")
success = 0
for lang in LANGUAGES:
    if lang == 'en':
        continue
    t = translate('Dawn Awaking', lang)
    if t:
        success += 1
    else:
        print(f"Failed for {lang}")
    time.sleep(0.05)

print(f"Successfully translated {success}/{len(LANGUAGES)-1} languages!")
