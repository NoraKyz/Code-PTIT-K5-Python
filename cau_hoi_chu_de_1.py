import re, collections, math, fractions, itertools

t = int(input())

m = {}
title = True
currTitle = ""
a = []

for _ in range(t):
    n = input()

    if n == "":
        title = True
        continue

    if title:
        currTitle = n
        title = False

        if currTitle not in m:
            m[currTitle] = 0
    else:
        m[currTitle] += 1

for i in m:
    print(str(i) + ": " + str(m[i]))