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
    n = input()
    n1 = n[len(n) - 3 ::]
    n2 = n[0:3]
    print("YES" if check(int(n1)) and check(int(n2)) else "NO")