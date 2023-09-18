import re, collections, math, fractions

t = int(input())

for _ in range(t):
    a = input()
    b = input()
    print(math.gcd(int(a), int(b)))