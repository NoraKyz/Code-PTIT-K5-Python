import re, collections, math, fractions

t = int(input())

def solve(n):
    n = list(map(int, n))
    
    c = set(n)
    if(len(c) != 2):
        return "NO"
    
    for i in range(len(n)):
        if(i + 2 < len(n)):
            if(n[i] != n[i + 2]):
                return "NO"
            
    return "YES"
        

for _ in range(t):
    print(solve(input()))