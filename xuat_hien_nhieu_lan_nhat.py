import re, collections, math, fractions, itertools

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    
    max_count = max(m.values())
    if max_count * 2 <= n:
        print("NO")
        continue
    
    candidates = [key for key, value in m.items() if value == max_count]
    print(min(candidates))