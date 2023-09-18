import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    k+= 1
    
    a = []

    for i in range(0, 64):
        cnt = 2 ** i
        check = k // cnt + (1 if k % cnt != 0 else 0)
        a.append(0 if check % 2 == 1 else 1)

    res = 0
    for i in range(len(a)):
        res += n ** i if a[i] == 1 else 0
        res %= 1000000007

    print(res)