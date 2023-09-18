import re, collections, math, fractions, itertools

def isPrime(n):
    if int(n) < 2:
        return False
    for i in range(2, int(math.sqrt(int(n)))+1):
        if int(n) % i == 0: return False
    return True

n, m = map(int, input().split())

a = [[x for x in input().split()] for i in range(n)]

b = [a[i][j] for i in range(n) for j in range(m) if isPrime(a[i][j])]

if b == []:
    print('NOT FOUND')
else:
    target = max(b)
    print(target)
    for i in range(n):
        for j in range(m):
            if a[i][j] == target:
                print("Vi tri ", end='')
                print('[', i, ']', sep='', end='')
                print('[', j, ']', sep='')