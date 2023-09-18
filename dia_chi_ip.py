import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = list(map(str, input().split('.')))

    if len(n) != 4:
        print('NO')
        continue

    kt = True
    for i in n :
        try:
            if int(i) > 255 or int(i) < 0:
                print('NO')
                kt = False
                break
        except:
            print('NO')
            kt = False
            break
    if kt:
        print('YES')
