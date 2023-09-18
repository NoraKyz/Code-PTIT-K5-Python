import re, collections, math, fractions, itertools

n, m = map(int, input().split())

a = [[int(x) for x in input().split()] for i in range(n)]

if n > m:
    cnt = 0
    while n > m:
        del a[cnt]
        n -= 1
        cnt += 1
elif m > n:
    cnt = 1
    while m > n:
        for i in range(len(a)):
            del a[i][cnt]
        m -= 1
        cnt += 1

for i in a:
    print(*i)