import re, collections, math, fractions, itertools

n = int(input())
s = [input() for i in range(n)]

def countMin(root, target):
    res = 0
    tmp = root

    while True:
        if tmp == target:
            return res
        
        tmp = tmp[1:] + tmp[0]
        res += 1

        if tmp == root:
            break
    
    return -1

res = 10**9

for i in s:
    tmp = i
    

    while True:
        x = 0

        for j in s:
            x += countMin(j, tmp)

        res = min(res, x)

        tmp = tmp[1:] + tmp[0]

        if tmp == i:
            break

if res < 0:
    print(-1)
else:
    print(res)
            
