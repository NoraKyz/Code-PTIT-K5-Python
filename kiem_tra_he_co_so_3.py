import re, collections, math, fractions

t = int(input())

def solve(a):
    a = set(list(map(str, a)))

    for i in a:
        if(i != '0' and i != '1' and i != '2'):
            return "NO"
    return "YES"

for _ in range(t):
    print(solve(input()))