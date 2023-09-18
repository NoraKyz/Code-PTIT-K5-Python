import re, collections, math, fractions
a = []
while True:
    try:
        b = list(map(int, input().split()))
        for i in b:
            a.append(i)
    except EOFError:
        break

a = list(i % 42 for i in a)
print(len(set(a)))