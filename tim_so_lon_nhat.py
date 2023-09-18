import re

t = int(input())

for i in range(t):
    list_num = list(map(int, re.findall('\d+', input())))
    print(max(list_num))