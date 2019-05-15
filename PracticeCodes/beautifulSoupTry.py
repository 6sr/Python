import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
url = input('Enter - ')
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_175161.html or 175162/3
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
sum = 0
tags = soup('span')
for tag in tags:
    curr = re.findall('[0-9]+',tag.contents[0])
    for n in curr:
        sum += int(n)
print(sum)