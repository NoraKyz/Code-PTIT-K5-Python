import re

n = input()
a = re.findall(r'\d+', n)


if(int(a[0]) + int(a[1]) == int(a[2])):
    print("YES")
else:
    print("NO")