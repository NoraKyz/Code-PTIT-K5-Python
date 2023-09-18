import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = input()

    cnt = 0
    for i in n:
        cnt += math.factorial(int(i))
    
    if(cnt == int(n)):
        print("Yes")
    else:
        print("No")