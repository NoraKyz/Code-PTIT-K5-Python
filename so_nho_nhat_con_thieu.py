import re, collections, math, fractions, itertools

n = int(input())
a = list(map(int, input().split()))

a = set(a)
print(min(m for m in range(1, 30001) if m not in a))