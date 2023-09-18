import re, collections, math, fractions, itertools

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    for i in n:
        if(check(int(i)) == False):
            return "No"

    if (check(int(n)) and check(int(n[::-1])) and check(sum((int(i) for i in n)))):
        return "Yes"
    else:
        return "No"

t = int(input())

for _ in range(t):
    n = input()
    print(solve(n))