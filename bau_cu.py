import re, collections, math, fractions, itertools

n, m = map(int, input().split())    
a = list(map(int, input().split()))

d = {}

for i in a:
    if i in d:
        d[i] += 1
    else :
        d[i] = 1

d = sorted(d.items(), key= lambda x: x[1], reverse=True)

if len(d) == 1:
    print('NONE')
else:    
    x = d[0][1]
    for i in d:
        if i[1] < x:
            x = i[1]
            break
    if(x == d[0][1]):
        print('NONE')
    else:
        print(min([i[0] for i in d if i[1] == x]))



