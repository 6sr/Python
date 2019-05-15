import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
#input = http://py4e-data.dr-chuck.net/comments_175163.json
#       http://py4e-data.dr-chuck.net/comments_42.json
print("Retrieving",url)
fhand = urllib.request.urlopen(url)
data = ""
num = 0
for line in fhand:
    curr = line.decode().strip()
    data += curr + "\n"
    num += len(curr)
print("Retrieved",len(data),"characters")
info = json.loads(data)
sum = 0
cnt = 0
for i in info['comments']:
    cnt += 1
    sum += int(i['count'])

print("Count:",cnt)
print("Sum:",sum)