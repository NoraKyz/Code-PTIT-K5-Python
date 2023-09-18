import re, collections, math, fractions

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    for i in range(len(n)):
        if(check(i) != check(n[i])):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = list(map(int, input()))
    print(solve(n))
