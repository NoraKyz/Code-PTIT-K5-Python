import re, collections, math, fractions, itertools

s = input()

if len(s) % 2 == 1:
    s = s[:len(s) - 1]
d = {}
s = re.findall('\\w{2}', s)

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d:
    print(i, d[i])