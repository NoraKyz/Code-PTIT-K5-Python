import re, collections, math, fractions, itertools

primes = [1]*1000005

for i in range(2, 1000005):
    if(primes[i]):
        for j in range(i*i, 1000005, i):
            primes[j] = 0

t = int(input())

for _ in range(t):
    
    n = int(input())

    for i in range(2, n):
        i_d = int(str(i)[::-1])
        if(primes[i] and primes[i_d] and i < i_d and i_d < n) :
            print(i, i_d, end=" ")
    print()