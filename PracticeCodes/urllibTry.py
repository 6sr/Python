import urllib.request, urllib.parse, urllib.error
#import urllib  # not working with this why???
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())        #line is byte array and not string so we decode

#try making search engine project