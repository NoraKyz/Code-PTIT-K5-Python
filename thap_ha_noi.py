import re, collections, math, fractions

t = int(input())

def solve(n, a, b, c):
    if n == 1:
        print(a + " -> " + c) 
        return
    solve(n - 1, a, c, b)
    print(a + " -> " + c) 
    solve(n - 1, b, a, c)

solve(t, "A", "B", "C")