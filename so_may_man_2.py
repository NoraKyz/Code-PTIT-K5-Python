
t = int(input())
for _ in range(t):
    n = input()
    res = n.count('4') + n.count('7')
    if (res == len(n)):
        print("YES")
    else:
        print("NO")