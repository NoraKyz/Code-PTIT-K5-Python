import re, collections, math, fractions

t = int(input())

for _ in range(t):
    n = input()
    if(int(n) % 7 == 0):
        print(n)
        continue
    
    cnt = 1000
    for i in range(cnt):
        s = int(n) + int(n[::-1])
        if s % 7 == 0:
            print(s)
            n = str(s)
            break
        else:
            n = str(s)

    if(int(n) % 7 != 0):
        print(-1)