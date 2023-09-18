import re, collections, math, fractions

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    x = sum(n)
    if(check(x) == False):
        return "NO"
    
    for i in range(0, len(n)):
        if(i % 2 != n[i] % 2):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = list(map(int, input()))
    print(solve(n))
