import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = int(input())
    d = {}
    a = list(map(int, input().split()))

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in d:
        if d[i] % 2 == 1:
            print(i)
            break