import re, collections, math, fractions

t = int(input())

def solve(n):
    n = n + n[::-1]
    
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            return -1 
    
    return n

for _ in range(t):
    n = int(input())

    for i in range(1, 10 ** int(len(str(n)) / 2)):
        res = int(solve(str(i)))
        if(res >= n):
            break
        elif (res != -1) :
            print(res, end = ' ')
    print()