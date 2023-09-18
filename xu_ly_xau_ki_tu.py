import re, collections, math, fractions, itertools

a = list(map(str, input().lower().split()))
b = list(map(str, input().lower().split()))

a = set(a)
b = set(b)

print(*sorted(a | b))
print(*sorted(a & b))
