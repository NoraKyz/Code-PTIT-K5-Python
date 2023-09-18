import re, collections, math, fractions

t = int(input())

def solve(a):
    a = list(map(int, a))
    if(len(a) < 3):
        return "NO"
    
    mid = 0
    for i in range(len(a)-1):
        if(a[i] >= a[i+1]):
            mid = i
            break
    
    for i in range(mid, len(a)-1):
        if(a[i] <= a[i+1]):
            return "NO"
            
    return "YES"

for _ in range(t):
    print(solve(input()))
    
    