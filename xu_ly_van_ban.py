import re, collections, math, fractions, itertools

res = ""
while True:
    try:
        res += input()
    except:
        break

res = re.split(r'[.?!]', res)
for i in res:
    a = i.lower().strip().split()
    if len(a) == 0:
        continue
    a[0] = a[0].capitalize()
    print(*a)
    
