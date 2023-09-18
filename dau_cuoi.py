t = int(input())

for _ in range(t):
    n = input()
    x = n[:2]
    y = n[-2:]
    if(x == y) :
        print("YES")
    else :
        print("NO")