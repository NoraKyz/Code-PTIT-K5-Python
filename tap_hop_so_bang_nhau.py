import re, collections, math, fractions, itertools

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

if a == b:
    print('YES')
else:
    print('NO')