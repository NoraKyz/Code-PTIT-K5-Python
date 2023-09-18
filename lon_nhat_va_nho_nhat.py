import re, collections, math, fractions, itertools

while True:
    n = int(input())
    if n == 0:
        break
    else :
        a = [int(input()) for i in range(n)] 
        # print(a)
        if(min(a) == max(a)):
            print("BANG NHAU")
        else:
            print(min(a), max(a))
