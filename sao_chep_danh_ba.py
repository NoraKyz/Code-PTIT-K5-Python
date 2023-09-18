import re, collections, math, fractions, itertools

m = []
currDate = []

with open('SOTAY.txt', 'r') as src:
    while True:
        try:
            x = src.readline().strip().split()
            if x[0] == 'Ngay':
                currDate.append("".join(x[1]))
                continue
            else :
                name = x
                pN = src.readline().strip()
                m.append({'date': currDate[-1], 'name': name, 'pN': pN})
        except:
            break

def cmp(a):
    return (a['name'][-1], a['name'][0:-1])

m.sort(key=cmp)

with open('DIENTHOAI.txt', 'w') as dst: 
    for i in m:
        name = " ".join(i['name']) + ': ' + i['pN'] + ' ' + i['date']
        dst.write(name + '\n')
        