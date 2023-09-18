import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    a = a[d::] + a[:d:]
    print(*a)
