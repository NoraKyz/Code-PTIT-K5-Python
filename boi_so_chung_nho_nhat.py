import re, collections, math, fractions, itertools

isPrime = [True] * 1000005
prime = [2]

def sieve():
    for i in range(4, 1000005, 2):
        isPrime[i] = False
    
    for i in range(3, 1000005, 2):
        if isPrime[i] == True:
            prime.append(i)
            for j in range(i*i, 1000005, i):
                isPrime[j] = False

sieve()

def phantich(n):
    d = {}
    for i in prime:
        if i > n:
            break

        tmp = n

        while tmp > 0:
            d[i] = d.get(i, 0) + tmp // i
            tmp = tmp // i

    return d

def solve(a, b):
    d = {}

    d1 = phantich(a-1) 
    d2 = phantich(b)

    for i in d2:
        d[i] = d2[i] - d1.get(i, 0)

    res = 1
    for i in d:
        res = res * (d[i] * 2 + 1) % 1000000007

    return res

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))

