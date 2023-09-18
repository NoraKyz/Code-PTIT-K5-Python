import re, collections, math, fractions

t = int(input())
f = [0] * 100
f[1] = 1
f[2] = 1
for i in range(3, 100):
    f[i] = f[i - 1] + f[i - 2]

for _ in range(t):
    a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        print(f[i], end=" ")
    print()