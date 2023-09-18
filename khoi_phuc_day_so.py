import re, collections, math, fractions, itertools

n = int(input())

a = [[i for i in map(int, input().split())] for j in range(n)]

if n == 2:
    print(a[0][1] // 2, a[0][1] // 2)
    exit()

s = sum(sum(a[i]) for i in range(n)) // ((n-1) * 2)

for i in range(n):
    print((sum(a[i]) - s) // (n-2), end= ' ')