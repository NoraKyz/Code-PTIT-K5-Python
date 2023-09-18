import re, collections, math, fractions, itertools

prime = []
isPrime = [True] * 1000001
def solve(n):
    prime.append(2)

    for i in range(4, n+1, 2):
        isPrime[i] = False

    for i in range(3, n+1, 2):
        if isPrime[i]:
            prime.append(i)
            for j in range(i*i, n+1, i):
                isPrime[j] = False
solve(20000)


n = int(input())
a = list(map(int, input().split()))

res = []

for i in a:
    if not isPrime[i]:
        x = min(j for j in prime if j > i)
        y = max(j for j in prime if j < i)
        res.append(min(abs(x-i), abs(y-i)))

if len(res) == 0:
    print(0)
else:
    print(max(res))
