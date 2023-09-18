import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = min(a)
    r = max(a)
    s = set(a)
    print(r - l + 1 - len(s))