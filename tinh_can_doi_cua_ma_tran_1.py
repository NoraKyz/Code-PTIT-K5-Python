import re, collections, math, fractions, itertools

n = int(input())

a = [[i for i in map(int, input().split())] for j in range(n)]

k = int(input())

s = sum(sum(a[i]) for i in range(n))

st = sum(a[i][j] for i in range(n) for j in range(i,n) if i != j)

s -= sum(a[i][i] for i in range(n))

cnt = abs(2 * st - s)
if cnt <= k:
    print('YES')
else:
    print('NO')

print(cnt)