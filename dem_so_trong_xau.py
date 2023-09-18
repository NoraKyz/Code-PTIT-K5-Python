import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = input()
    k = input()
    cnt = 0
    while k in n:
        n = n.replace(k, "", 1)
        cnt += 1
    print(cnt)