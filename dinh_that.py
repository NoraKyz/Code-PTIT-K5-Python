import re, collections, math, fractions, itertools

res = []
def dfs(u, v, path = []):
    if u == v:
        res.append(path)
    else :
        for x in a[u]:
            if not visited[x]:
                visited[x] = True
                dfs(x, v, path + [x])
                visited[x] = False
            
t = int(input())

for _ in range(t):
    a = [[] for _ in range(105)]
    visited = [False] * 105
    res.clear()

    n, m, u, v = map(int, input().split())

    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y) 

    dfs(u, v, [u])

    b = set()
    for i in range(1,n+1):
        b.add(i)

    for i in res:
        c = set(i)
        b = b & c

    print(len(b) - 2)


