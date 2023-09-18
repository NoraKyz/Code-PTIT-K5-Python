import re, collections, math, fractions, itertools

def count_divisible(l, r, k):
    l = l // k + (1 if l % k != 0 else 0)
    r = r // k
    return r - l + 1

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

cmb = [] * 100

def prepare():
    f = []
    for i in range(2, 51):
        if isPrime(i):
            f.append(i)

            q = []
            for j in range(len(f)):
                p = []
                tmp = itertools.combinations(f, j+1)              
                for items in tmp:
                    k = 1
                    for item in items:
                        k *= item
                    p.append(k)
                q.append(sorted(p))

            cmb.append(q)

prepare()

while True:
    a = list(map(int, input().split()))

    if(len(a) == 1): break

    n = int(input())

    f = []
    for i in range(2, n+1):
        if isPrime(i):
            f.append(i)

    cnt = 0
    
    l = cmb[len(f)-1]

    dem = 0
    for i in range(len(l)):
        for j in l[i]:
            if(j > a[1]): break
            dem += 1
            if(i % 2 == 0):
                cnt += count_divisible(a[0], a[1], j)
            else:
                cnt -= count_divisible(a[0], a[1], j)   

    print(a[1] - a[0] + 1 - cnt)