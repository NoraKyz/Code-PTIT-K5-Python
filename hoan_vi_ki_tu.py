import re, collections, math, fractions, itertools

s = input()
l = list(itertools.permutations(s))
for _ in l:
    for i in _:
        print(i, end="")
    print()