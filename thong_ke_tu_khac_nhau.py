import re, collections, math, fractions, itertools

t = int(input())
d = {}
for _ in range(t):
    s = input()
    s = s.lower()
    w = re.findall(r'\w+', s)
    for i in w:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

a = list(d.items())
a.sort(key=lambda x: (-x[1], x[0]))
for i in a:
    print(i[0], i[1])