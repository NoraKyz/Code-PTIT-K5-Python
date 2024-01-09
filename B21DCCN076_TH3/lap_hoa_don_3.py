class Hoadon:
    def __init__(self, ma, ten, sl, dg, ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.tong = sl * dg - ck

    def __str__(self):
        return f'{self.ma} {self.ten} {self.sl} {self.dg} {self.ck} {self.tong}'


n = int(input())
ds = []
for i in range(n):
    ma = input()
    ten = input()
    sl = int(input())
    dg = int(input())
    ck = int(input())
    ds.append(Hoadon(ma, ten, sl, dg, ck))

ds.sort(key=lambda x: x.tong, reverse=True)

for i in ds:
    print(i)
