import re, collections, math, fractions

t = int(input())

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(t):
    n = list(map(int,input()))
    n = sum(n)
    if(check(n) == True):
        print("YES")
    else:
        print("NO")
