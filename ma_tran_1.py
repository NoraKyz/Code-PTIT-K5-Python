import re, collections, math, fractions, itertools

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

r1 = sum(a[i][j] for i in range(n) for j in range(i+1, n))
r2 = sum(a[i][j] for i in range(n) for j in range(i))

if abs(r1 - r2) > k:
    print("NO")
else:
    print("YES")

print(abs(r1 - r2))
