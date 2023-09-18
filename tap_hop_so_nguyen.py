import re, collections, math, fractions, itertools

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

print(*sorted(a.intersection(b)))
print(*sorted(a - b))
print(*sorted(b-a))