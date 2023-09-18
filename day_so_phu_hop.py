import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    res = "YES"
    for i in range(n):
        if(a[i] > b[i]):
            res = "NO"
            break
    print(res)