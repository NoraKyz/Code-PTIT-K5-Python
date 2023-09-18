import re, collections, math, fractions, itertools

n = int(input())

a = list(map(float, input().split()))
a = [i for i in a if i != max(a) and i != min(a)]
print(format(sum(a) / len(a), '.2f'))