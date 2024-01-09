import datetime


class TheLoai:
    cnt = 0
    def __init__(self, name):
        TheLoai.cnt += 1
        self.id = 'TL' + format(TheLoai.cnt, '03d')
        self.name = name

    def __str__(self):
        return f'{self.id} {self.name}'
    
class Phim:
    cnt = 0

    def __init__(self, ten_phim, ngay_khoi_chieu, so_tap_phim, the_loai):
        Phim.cnt += 1
        self.id = 'P' + format(Phim.cnt, '03d')
        self.ten_phim = ten_phim
        self.ngay_khoi_chieu = ngay_khoi_chieu
        self.so_tap_phim = so_tap_phim
        self.the_loai = the_loai

    def __lt__(self, other):
        date1 = datetime.datetime.strptime(self.ngay_khoi_chieu, '%d/%m/%Y')
        date2 = datetime.datetime.strptime(other.ngay_khoi_chieu, '%d/%m/%Y')
        if date1 < date2:
            return True
        elif date1 == date2:
            if self.ten_phim < other.ten_phim:
                return True
            elif self.ten_phim == other.ten_phim:
                if self.so_tap_phim > other.so_tap_phim:
                    return True
        return False

    def __str__(self):
        return f'{self.id} {self.the_loai} {self.ngay_khoi_chieu} {self.ten_phim} {self.so_tap_phim}'
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    list_the_loai = []
    list_phim = []

    for i in range(n):
        name = input()
        list_the_loai.append(TheLoai(name))
    for i in range(m):
        id_the_loai = input()
        ngay_khoi_chieu = input()
        ten_phim = input()
        so_tap_phim = int(input())
        for j in list_the_loai:
            if j.id == id_the_loai:
                list_phim.append(
                    Phim(ten_phim, ngay_khoi_chieu, so_tap_phim, j.name))
                break
    list_phim.sort()
    for i in list_phim:
        print(i)