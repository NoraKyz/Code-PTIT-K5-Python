import re, collections, math, fractions

t = int(input())

for _ in range(t):
    a = input()
    b = a[::-1]
    r = math.gcd(int(a), int(b))
    if r == 1:
        print("YES")
    else:
        print("NO") 