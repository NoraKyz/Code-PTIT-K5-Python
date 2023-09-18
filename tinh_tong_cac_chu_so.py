import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    s = input()
    a = re.findall(r'\D', s)
    b = re.findall(r'\d', s)
    
    a = sorted(a)
    res = sum([int(i) for i in b])

    for i in a:
        print(i, end="")
    print(res)

