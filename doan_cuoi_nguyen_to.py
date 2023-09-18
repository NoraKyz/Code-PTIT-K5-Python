import re, collections, math, fractions

t = int(input())

def check(n):
    if n < 2:
        return "NO"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "NO"
    return "YES"

for _ in range(t):
    n = input()
    n = n[len(n) - 4 ::]
    print(check(int(n)))