
t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    cnt = 0
    while n < m:
        cnt += 1
        n = n * (1 + x / 100)
    
    print(cnt)