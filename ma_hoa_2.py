import re, collections, math, fractions

p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

p = list(map(str, p))

while True:
    n = list(map(str, input().split()))
    if(len(n) == 1):
        break

    k = int(n[0])
    s = list(map(str, n[1]))

    for i in range(len(s)) :
        s[i] = p[(p.index(s[i])+k)%28]
    s = s[::-1]
    print("".join(s))