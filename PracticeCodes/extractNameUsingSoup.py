import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter URL: ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))
for i in range(cnt):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        if i == pos:
            url = tag.get('href',None)
            print('Retrieving: ' + url)
            break
