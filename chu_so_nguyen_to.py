import re, collections, math, fractions

t = int(input())

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    if(check(len(n)) == False):
        return "NO"

    cnt = 0
    for i in n:
        if(check(i) == True):
            cnt += 1
    
    if(cnt * 2 > len(n)):
        return "YES"
    return "NO"

for _ in range(t):
    n = list(map(int, input()))

    print(solve(n))