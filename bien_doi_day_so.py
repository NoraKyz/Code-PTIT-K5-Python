import re, collections, math, fractions, itertools

while True :
    a = list(map(int, input().split()))

    if all(x == 0 for x in a) :
        break

    cnt = 0

    while True:
        if all(x == a[0] for x in a) :
            print(cnt)
            break

        b = a.copy()
        for i in range(len(a)-1) :
            a[i] = abs(b[i] - b[i + 1])
        a[3] = abs(b[3] - b[0])

        cnt += 1

        