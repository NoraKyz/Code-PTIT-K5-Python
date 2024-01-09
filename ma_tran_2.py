n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
sU = 0
sL = 0
for i in range(n):
    for j in range(n):
        if i + j > n-1:
            sU += a[i][j]
        elif i + j < n-1:
            sL += a[i][j]
print("YES") if (abs(sU - sL) <= k) else print("NO")
print(abs(sU - sL)) 