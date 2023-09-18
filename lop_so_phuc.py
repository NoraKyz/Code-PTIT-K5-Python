import re, collections, math, fractions, itertools

t = int(input())
a = []
for _ in range(t):
    for i in map(int, input().split()):
        a.append(i)
    
    if(len(a) == 4):
        x1 = complex(a[0], a[1])
        x2 = complex(a[2], a[3])

        x3 = x1 + x2

        res1 = x3 * x1
        res2 = x3 * x3

        print("{} {} {}i".format(int(res1.real), '+' if int(res1.imag) >= 0 else '-', abs(int(res1.imag))), end=', ')
        print("{} {} {}i".format(int(res2.real), '+' if int(res2.imag) >= 0 else '-', abs(int(res2.imag))))

        a.clear()
