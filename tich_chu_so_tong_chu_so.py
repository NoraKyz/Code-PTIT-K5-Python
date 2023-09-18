import re, collections, math, fractions

def solve(n):
    s = sum(n[i] for i in range(1,len(n),2))

    mul = 1
    for i in range(0, len(n), 2):
        if n[i] != 0:
            mul *= n[i]
        

    return mul, s

t = int(input())
for _ in range(t):
    print(*solve(list(map(int, input()))))