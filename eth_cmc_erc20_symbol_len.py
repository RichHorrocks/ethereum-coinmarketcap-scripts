#!/usr/bin/env python

import urllib, json
from collections import Counter

url = "https://api.coinmarketcap.com/v1/ticker/?limit=0""
response = urllib.urlopen(url)
data = json.loads(response.read())

counts = Counter([len(asset['symbol']) for asset in data])
for i, j in sorted(counts.items()):
    print("Token symbols of length %d: %d" % (i, j))
