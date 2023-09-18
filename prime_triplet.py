import re, collections, math, fractions, itertools

primes = [1]*1000005

for i in range(2, 1000005):
    if(primes[i]):
        for j in range(i*i, 1000005, i):
            primes[j] = 0

t = int(input())

for _ in range(t):
    
    n = int(input())
    cnt = 0
    for i in range(2, n):
        if(((primes[i] and primes[i+2] and primes[i+6]) or (primes[i] and primes[i+4] and primes[i+6])) and i+6 < n) :
            cnt += 1
    print(cnt)