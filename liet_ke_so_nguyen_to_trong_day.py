import re, collections, math, fractions, itertools

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i in d and check(i):
        d[i] += 1
    elif check(i):
        d[i] = 1
for i in d:
    print(i, d[i])
