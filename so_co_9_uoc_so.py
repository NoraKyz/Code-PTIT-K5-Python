import re, collections, math, fractions, itertools

n = int(input())

prime = [2, 3, 5, 7, 11, 13, 17]

res = 0

for i in prime:
    if i ** 8 <= n:
        res += 1

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i * i != n:
            if isPrime(i) and isPrime(n // i):
                return True
    
    return False

for i in range(2, int(n ** 0.5) + 1):
    if not isPrime(i):
        res += 1 if check(i) else 0

print(res)