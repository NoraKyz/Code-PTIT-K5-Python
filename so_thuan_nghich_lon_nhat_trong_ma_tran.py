import re, collections, math, fractions, itertools

def check(n):
    if len(n) == 1:
        return False
    
    return n == n[::-1]

n, m = map(int, input().split())

a = [[x for x in input().split()] for i in range(n)]

b = [a[i][j] for i in range(n) for j in range(m) if check(a[i][j])]

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


