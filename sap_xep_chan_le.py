import re, collections, math, fractions, itertools

n = int(input())
a = []

while EOFError:
    try:
        x = list(map(int, input().split()))
        a.extend(x)
    except EOFError:
        break

b = [x%2 for x in a]
c = [x for x in a if x%2 == 0]
l = [x for x in a if x%2 == 1]

c = sorted(c)
l = sorted(l, reverse=True)

cntc = 0
cntl = 0
for i in range(n):
    if b[i] == 0:
        b[i] = c[cntc]
        cntc += 1
    else:
        b[i] = l[cntl]
        cntl += 1

print(*b)
