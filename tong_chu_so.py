import re, collections, math, fractions, itertools

res = 0

s = input()

while len(s) > 1:
    s = str(sum((ord(x) - ord('0')) for x in s))
    res+=1

print(res if res > 0 else 1)