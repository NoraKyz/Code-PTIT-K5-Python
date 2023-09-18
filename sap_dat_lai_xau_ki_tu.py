import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    a = [i for i in input()]
    b = [i for i in input()]

    print("Test", str(_+1) + ':', end=" ")

    print('YES' if sorted(a) == sorted(b) else 'NO')

    
