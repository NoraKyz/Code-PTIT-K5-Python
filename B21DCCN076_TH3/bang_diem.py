from math import *


class HocSinh:
    def __init__(self, id, name, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        self.id = f"HS{id:02}"
        self.name = name
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.a9 = a9
        self.a10 = a10

    def getTB(self):
        tb = (self.a1*2.0 + self.a2*2.0 + self.a3 + self.a4 + self.a5 +
              self.a6 + self.a7 + self.a8 + self.a9 + self.a10) / 10.0 / 1.2
        return tb

    def getXL(self):
        if self.getTB() < 5:
            return 'YEU'
        elif self.getTB() < 6.9:
            return 'TB'
        elif self.getTB() < 7.9:
            return 'KHA'
        elif self.getTB() < 8.9:
            return 'GIOI'
        return 'XUAT SAC'

    def __str__(self):
        return '{} {} {:.1f} {}'.format(self.id, self.name, round(self.getTB(), 1), self.getXL())

    def __lt__(self, o):
        if self.getTB() != o.getTB():
            return self.getTB() > o.getTB()
        return self.id < o.id


if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(1, n + 1):
        name = input()
        b = [float(i) for i in input().split()]
        x = HocSinh(i, name, b[0], b[1], b[2], b[3],
                    b[4], b[5], b[6], b[7], b[8], b[9])
        a.append(x)
    a.sort()
    for i in a:
        print(i)
