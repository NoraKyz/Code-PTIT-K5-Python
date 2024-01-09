import re, collections, math, fractions, itertools

class SV:
    def __init__(self, name, C, T) -> None:
        self.name = name
        self.C = C
        self.T = T
    
    def __str__(self) -> str:
        return self.name + ' ' + str(self.C) + ' ' + str(self.T)
    
a = []

t = int(input())

for _ in range(t):
    name = input()
    C, T = map(int, input().split())
    
    a.append(SV(name, C, T))

a.sort(key=lambda x: (-x.C, x.T, x.name))

for it in a:
    print(it)
