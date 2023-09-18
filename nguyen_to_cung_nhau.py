import re, collections, math, fractions

n, k = map(int, input().split())
cnt = 0
for i in range(10**(k-1), 10**k):
    if (math.gcd(i, n) == 1):
        cnt += 1
        if(cnt < 10):
            print(i, end = ' ')
        else:
            print(i)
            cnt = 0