import re, collections, math, fractions, itertools

n = int(input())

a = list(map(int, input().split()))
a.sort()

result = [(i, j) for i in a for j in a if math.gcd(i, j) == 1 and i < j]

for i, j in result:
    print(i, j)