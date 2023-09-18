import re, collections, math, fractions, itertools

s = input()
k = int(input())

if len(s) % 2 == 1:
    s = s[:len(s) - 1]
d = {}
s = re.findall('\\w{2}', s)
s = [int(i) for i in s]

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

res = 0

def cmp(x):
    return x[0]

d = sorted(d.items(), key = cmp)

for i in d:
    if i[1] >= k:
        print(i[0], i[1])
        res += 1

if res == 0:
    print('NOT FOUND')