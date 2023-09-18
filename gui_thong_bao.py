import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = input().split()
    cnt = 0
    for i in n:
        cnt += len(i)
        if cnt > 100:
            break
        else:
            print(i, end=' ')
            cnt += 1
    print()