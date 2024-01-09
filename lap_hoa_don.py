import re, collections, math, fractions, itertools

def clamp(x, a, b):
    return max(a, min(x, b))

class KhachHang:
    cnt = 1

    def __init__(self, name, C, M) -> None:
        self.id = "KH" + format(KhachHang.cnt, '02d')
        KhachHang.cnt += 1

        self.name = name
        self.C = C
        self.M = M

        T = M - C

        self.total = 0

        self.total += clamp(T, 0, 50) * 100 * 1.02
        T -= clamp(T, 0, 50)
        self.total += clamp(T, 0, 50) * 150 * 1.03
        T -= clamp(T, 0, 50)
        self.total += T * 200 * 1.05

        # self.total *= 10
        # du = self.total % 10

        # if du >= 5:
        #     self.total += 10 - du
        # else:
        #     self.total -= du
a = []

t = int(input())

for _ in range(t): 
    a.append(KhachHang(input(), int(input()), int(input())))

a.sort(key=lambda x: (-x.total))

for it in a:
    print(it.id, it.name, it.total, sep=' ')