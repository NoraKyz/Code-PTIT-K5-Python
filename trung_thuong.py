import re, collections, math, fractions

for _ in range(int(input())):
    a = {}
    n = int(input())
    cnt = 0
    for i in range(n):
        x = int(input())
        if x in a:
            a[x] += 1   
        else:
            a[x] = 1
        cnt = max(cnt, a[x])
    print(min(key for key, value in a.items() if value == cnt))