# -*- coding: utf-8 -*-
import urllib.request
import re

url = 'https://translate.google.com/m?sl=en&tl=hi&q=A+hurricane'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'})
try:
    res = urllib.request.urlopen(req, timeout=5)
    html = res.read().decode('utf-8')
    m = re.search(r'class="result-container">([^<]+)', html)
    if m:
        print('SUCCESS:', repr(m.group(1)))
    else:
        print('No match, html length:', len(html))
except Exception as e:
    print('ERROR:', e)
