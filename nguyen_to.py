import math

def check(n):
    if n <= 1:
        return "NO"

    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return "NO"
    
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    
    for i in range(n):
        if(math.gcd(i, n) == 1):
            cnt += 1

    print(check(cnt))

    
