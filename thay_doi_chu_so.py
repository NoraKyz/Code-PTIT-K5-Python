t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    p = a[0]
    q = a[1]
    if (p > q) :
        p, q = q, p

    x = list(input().split())

    if(len(x) == 1):
        x = x[0]
        y = input()
    else:
        y = x[1]
        x = x[0]
    

    x1 = x.replace(str(q), str(p))
    x2 = y.replace(str(q), str(p))

    y1 = x.replace(str(p), str(q))
    y2 = y.replace(str(p), str(q))

    print(int(x1) + int(x2), int(y1) + int(y2))

