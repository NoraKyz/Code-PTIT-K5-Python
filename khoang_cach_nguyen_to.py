import re, collections, math, fractions

f = []
c = [False] * 10005

def sieve(n):
    for i in range(2, n + 1):
        if c[i] == False:
            f.append(i)
            for j in range(i * i, n + 1, i):
                c[j] = True

sieve(10000)

n, k = list(map(int, input().split()))

cnt = k

print(cnt, end= " ")
for i in range(n):
    cnt += f[i]
    print(cnt, end= " ")