import re, collections, math, fractions, itertools

n = int(input())
a = map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

m = {}

for i in a:
    if i in m:
        m[i] += 1
    else :
        m[i] = 1

b = [i for i in m.keys()]

f = [0] * len(b)
f[0] = b[0]

for i in range(1,len(b)):
    f[i] = f[i-1] + b[i]

check = False
for i in range(len(b)):
    if is_prime(f[i]) and is_prime(f[len(b)-1] - f[i]):
        print(i)
        check = True
        break

if not check:
    print('NOT FOUND')