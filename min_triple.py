
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    x1 = min(a)
    a.remove(x1)
    x2 = min(a)
    a.remove(x2)
    x3 = min(a)
    a.remove(x3)

    print(x1 + x2 + x3)
    