# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse

payload_text = "Game Menu\nLanguages\n1,000 Levels Odyssey\nFirst Win\nWin your first challenge round"
data = urllib.parse.urlencode({'q': payload_text}).encode('utf-8')
req = urllib.request.Request(
    'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t',
    data=data,
    headers={'User-Agent': 'Mozilla/5.0'}
)
res = urllib.request.urlopen(req, timeout=10)
body = json.loads(res.read().decode('utf-8'))
translated_chunks = [part[0] for part in body[0] if part and part[0]]
full_text = ''.join(translated_chunks)
print("ES Translation:\n", full_text)
