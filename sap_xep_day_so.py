import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = max(a)
    id = a.index(x)
    a = a[:id] + [m] + a[id:]

    a = [x for x in a if x < 0] + [x for x in a if x >= 0]

    print(*a)
