import re, collections, math, fractions, itertools

def solve(n):
    res = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res.append((i, cnt))
    if n > 1:
        res.append((n, 1))
    
    print("1", end="")
    for i in res:
        print(" * ", i[0], "^", i[1], sep="", end="")
    
    print()

t = int(input())

for i in range(t):
    n = int(input())
    solve(n)