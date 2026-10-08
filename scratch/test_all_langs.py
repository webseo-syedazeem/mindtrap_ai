import sys, urllib.request, json, urllib.parse, time
sys.stdout.reconfigure(encoding='utf-8')

LANG_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt',
    'zh_CN': 'zh-CN',
    'zh_TW': 'zh-TW',
    'fil': 'tl',
    'he': 'iw',
}

TEST_LANGS = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

print(f"Total languages to test: {len(TEST_LANGS)}")

for code in TEST_LANGS:
    gt_code = LANG_MAP.get(code, code)
    try:
        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={gt_code}&dt=t&q=Play'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read().decode('utf-8'))
        trans = ''.join(item[0] for item in data[0] if item[0])
        print(f"{code} ({gt_code}) -> {trans}")
    except Exception as e:
        print(f"ERROR for {code} ({gt_code}): {e}")
