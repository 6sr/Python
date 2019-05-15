import re

x = 'From 9 sachin@gmail.com hi: my name is : Sachin 892722 9 90 2 1234567890 '
y = re.findall('^From.*:',x)    #startswith From   endswith :

y = re.findall('\S+@\S+',x)     #Checks for email id
print(str(y[0]))

y = re.findall('[0-9]\S+',x)
print(y)

y = re.findall('^From (\S+@\S+)',x)     #Checks for email id
#matching From ....@... but extracting ....@...

y = re.findall('@([^ ]*) ',x)     #Checks for domain name
y = re.findall('^From .*@([^ ]*) ',x)     #Checks for domain name

print(float("1"))

# [^ ]
# ^ startswith
# .+   >= 1 in b/w
# .*  >= 0 in b/w
# \S checks non blank character
# . does not checks non blank character
# ? prevents . and * from being greedy i.e. the shortest string
# [0-9] list for 0,1,...,9
# [AEIOU] list for A,E,I,O,U
# \$ checks for real dollar sign we have to write like this as $ also has other meanings