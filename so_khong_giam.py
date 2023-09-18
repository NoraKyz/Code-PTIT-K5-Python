import re, collections, math, fractions

t = int(input())

def solve(n):
    l = len(n)
    for i in range(0, l-1):
        if n[i] > n[i+1]:
            return "NO"
    
    return "YES"

for _ in range(t):
    n = input()
    print(solve(n))