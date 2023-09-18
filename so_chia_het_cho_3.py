import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = list(map(int,input()))
    n = sum(n)
    if n % 3 == 0:
        print("YES")
    else:
        print("NO")
