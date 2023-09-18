import re, collections, math, fractions, itertools

def phi(loaixe, soghe, huong):
    if(huong == "OUT"):
        return 0
    
    if loaixe == "Xe_con":
        if soghe == "5":
            return 10000
        else :
            return 15000
    elif loaixe == "Xe_tai":
        return 20000
    else:
        if soghe == "29":
            return 50000
        else :
            return 70000

t = int(input())
res = {}
for _ in range(t):
    n = input()

    bienso, loaixe, soghe, huong, time = n.split(" ")

    if time in res:
        res[time] += phi(loaixe, soghe, huong)
    else:
        res[time] = phi(loaixe, soghe, huong)

for i in res:
    print(str(i) + ": " + str(res[i]))