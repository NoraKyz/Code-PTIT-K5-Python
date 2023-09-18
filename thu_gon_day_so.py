n = int(input())
a = list(map(int, input().split()))

res = []

for i in range(n):
    if len(res) == 0:
        res.append(a[i])
    else :
        if((res[-1] + a[i]) % 2 == 0):
            res.pop()
        else:
            res.append(a[i])

print(len(res))