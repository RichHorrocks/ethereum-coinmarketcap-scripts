#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup
import operator

page = urllib.urlopen("https://coinmarketcap.com/tokens/views/all/")
soup = BeautifulSoup(page.read())

token_dict = {}
token_count = 0

for token in soup.find_all('td', { 'class' : 'platform-name' }):
    token_count += 1
    if token.a.get_text() in token_dict:
        token_dict[token.a.get_text()] += 1
    else:
        token_dict[token.a.get_text()] = 1

# Sort the dictionary, which creates a list of sorted tuples.
sorted_dict = sorted(token_dict.items(),
                     key = operator.itemgetter(1),
                     reverse = True)

print("\n{0:25} {1:10}".format("Total token count:", str(token_count)))
print("-----------------------------")
for i in sorted_dict:
    print("{0:18} {1:10}".format(i[0], i[1]))
