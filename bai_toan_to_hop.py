import re, collections, math, fractions, itertools

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = set(a)

c_l = list(itertools.combinations(a, k))
for _ in c_l:
    print(*_)
