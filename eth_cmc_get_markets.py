#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup
import csv

page = urllib.urlopen("https://coinmarketcap.com/currencies/ethereum/#markets")
soup = BeautifulSoup(page.read())

with open('output.csv', 'wb') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(map(str, "# Source Pair Volume Price Volume Updated".split()))
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        rows = [0] * len(tds)
        for i in xrange(len(tds)):
            rows[i] = tds[i].get_text()
        wr.writerow(rows)
