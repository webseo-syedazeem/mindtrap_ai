import urllib.request, urllib.parse, json, sys
sys.stdout.reconfigure(encoding='utf-8')

test_items = [
    "Play",
    "Settings",
    "Worlds",
    "Store",
    "Daily Rewards",
    "Guest Player",
    "1,000 Levels Odyssey",
    "Show your love with 5 stars"
]

delim = "\n"
joined = delim.join(test_items)
url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q={urllib.parse.quote(joined)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req, timeout=5)
data = json.loads(res.read().decode('utf-8'))
translated_full = ''.join(item[0] for item in data[0] if item[0])
translated_list = [s.strip() for s in translated_full.split('\n') if s.strip()]

print(f"Original items: {len(test_items)}")
print(f"Translated items: {len(translated_list)}")
for orig, trans in zip(test_items, translated_list):
    print(f"  {orig} -> {trans}")
