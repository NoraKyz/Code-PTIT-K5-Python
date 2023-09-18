import re, collections, math, fractions

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())

for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if check(a[i]):
            a[i] = 1
        else:
            a[i] = 0
    print(*a)