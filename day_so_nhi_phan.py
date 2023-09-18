import re, collections, math, fractions

n = int(input())
a = list(map(int, input().split()))

count = sum(1 for i in range(n - 1) if (a[i] == 0 and a[i + 1] == 1) or (a[i] == 1 and a[i + 1] == 0))
print(count)