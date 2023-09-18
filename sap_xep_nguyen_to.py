import re, collections, math, fractions, itertools

n = int(input())
a = list(map(int, input().split()))

def isPrime(n):
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

p = [i for i in a if isPrime(i)]
p.sort()

for i in a:
    if i not in p and not isPrime(i):
        print(i, end=' ')
    else :
        print(p.pop(0), end=' ')