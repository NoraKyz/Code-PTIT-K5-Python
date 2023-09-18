import re, collections, math, fractions

t = int(input())

for _ in range(t):
    s = input()
    s = s[len(s) - 2::]
    
    if(s == "86"):
        print("YES")
    else:
        print("NO")