import re, collections, math, fractions

t = int(input())

def solve(n):
    s = sum(n)
    if(s % 10 != 0):
        return "NO"
    
    for i in range(1,len(n)):
       if(abs(n[i] - n[i-1]) != 2):
           return "NO"
    return "YES"

for _ in range(t):
    n = list(map(int, input()))
    print(solve(n))