import re, collections, math, fractions, itertools

t = int(input())
res = 0
types = []
check = 0
socau = 0

for _ in range(t):
    n = input().split()
    if(len(n) == 6):
        if check != 1 :
            res += 1
            types.append(1)
            check = 1   
    elif(len(n) == 7):
        if check != 2 :
            res += 1
            types.append(2)
            check = 2
            socau += 1
        else:
            socau += 1
            if socau % 4 == 0:
                check = 0

print(res)
for i in types:
    print(i)