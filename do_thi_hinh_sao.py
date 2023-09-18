import re, collections, math, fractions, itertools

f = {}

t = int(input())

for _ in range(t-1):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
    
    if a in f:
        f[a] += 1
    else:
        f[a] = 1
    
    if b in f:
        f[b] += 1
    else:
        f[b] = 1

x = list(f.values())

cnt = 0
for i in x:
    if i == t - 1:
        print("Yes")
        cnt = 1
        break
if cnt == 0:
    print("No")

    