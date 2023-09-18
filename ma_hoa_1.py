import re, collections, math, fractions

t = int(input())

for _ in range(t):
    s = input()
    res = ""
    for i in re.finditer(r'(.)\1*', s):
        c = i.group(1)
        cnt = len(i.group(0))
        res += str(cnt) + c  
    print(res)
