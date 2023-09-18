import re, collections, math, fractions
t = int(input())

def solve(s):
    if(s == 1):
        return "NO"
    for i in range(2, int(math.sqrt(s)) + 1):
        if s % i == 0:
            return "NO"
    return "YES"

for _ in range(t):
    a, b = map(int, input().split())
    res = math.gcd(a, b)
    res = sum(map(int, str(res)))
    print(solve(res))
    