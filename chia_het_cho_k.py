import re, collections, math, fractions

a, k ,n = map(int, input().split())

cnt = 0

for i in range(k, n+1, k):
    if(i - a > 0):
        cnt += 1
        print(i - a, end = " ")

if(cnt == 0):
    print(-1)