import re, collections, math, fractions, itertools

n = int(input())

a = []

for _ in range(n):
    f = [i for i in input()]
    a.append(f)

cnt = 0
for i in range(n):
    tmp = sum(1 for j in range(n) if a[i][j] == 'C')
    cnt += math.comb(tmp, 2)
    tmp = sum(1 for j in range(n) if a[j][i] == 'C')
    cnt += math.comb(tmp, 2)

print(cnt)