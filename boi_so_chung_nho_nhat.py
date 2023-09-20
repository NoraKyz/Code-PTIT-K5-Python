import re, collections, math, fractions, itertools

pr = [0] * 1000005

def sieve():
    for i in range(2, 1000005, 2):
        pr[i] = 2
    
    for i in range(3, 1000005, 2):
        if pr[i] == 0:
            for j in range(i, 1000005, i):
                if pr[j] == 0:
                    pr[j] = i

sieve()

f = [1] * 1000005

def prepare():
    d = {}
    res = 1
    for i in range(2, 1000005):
        res *= i

        x = res 
        while x > 1:
            f[i][pr[x]] = f[i].get(pr[x], 0) + 1
            x //= pr[x]

        for i in d:
            f[i] = f[i] * (d[i] + 1) % 1000000007
        return res * 2 + 1

prepare()

print(f[10])

def solve(a, b):
    d = {}

    for i in range(a, b+1):
        x = i
        while x > 1:
            d[pr[x]] = d.get(pr[x], 0) + 1
            x //= pr[x]

    res = 1

    if(a == b):
        for i in d:
            res = res * (d[i] + 1) % 1000000007
        return res * 2 - 1
    else :
        for i in d:
            res = res * (d[i] + 1) % 1000000007
        return res * 2 + 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))

