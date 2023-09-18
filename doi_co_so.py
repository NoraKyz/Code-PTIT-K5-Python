import re, collections, math, fractions, itertools

arr = []

for i in range(0, 10):
    arr.append(str(i))
for i in range(ord('A'), ord('Z') + 1):
    arr.append(chr(i))

def solve(n, b):
    res = ''
    while n > 0:
        res = arr[n % b] + res
        n = n // b
    return res

t = int(input())

for _ in range(t):
    n, b = map(int, input().split())
    print(solve(n, b))