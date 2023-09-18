import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = list(map(int,input()))
    n = str(sum(n))
    if n == n[::-1] and len(n) > 1:
        print("YES")
    else:
        print("NO")
