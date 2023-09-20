import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = []

    while n > 0:
        x = input().split()
        for i in x:
            a.append(int(i))

        n -= len(x)

    res = 10**9
    for i in range(len(a)):
        currGcd = a[i]
        for j in range(i, len(a)):
            currGcd = math.gcd(currGcd, a[j])
            if(currGcd == k):
                res = min(res, j - i + 1)

    if(res == 10**9):
        print(-1)
    else:
        print(res)
