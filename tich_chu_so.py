import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = list(map(int,input()))
    
    cnt = 1
    for i in n:
        if i != 0:
            cnt *= i
    
    print(cnt)
