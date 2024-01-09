
class SinhVien:
    cnt = 0
    def __init__(self, ma_sv, ho_ten, lop):
        SinhVien.cnt += 1
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.lop = lop
        self.diem = 10
        self.ghi_chu = ''

    def __str__(self):
        if self.diem == 0:
            self.ghi_chu = 'KDDK'
        res = f'{self.ma_sv} {self.ho_ten} {self.lop} {self.diem}'
        if self.ghi_chu != '':
            res += f' {self.ghi_chu}'
        return res
    
if __name__ == '__main__':
    n = int(input())
    list_sv = []
    for i in range(n):
        ma_sv = input()
        ho_ten = input()
        lop = input()
        list_sv.append(SinhVien(ma_sv, ho_ten, lop))
    for i in range(n):
        ma_sv, diem_danh = input().split()
        for sv in list_sv:
            if sv.ma_sv == ma_sv:
                for c in diem_danh:
                    if c == 'm':
                        sv.diem -= 1
                    elif c == 'v':
                        sv.diem -= 2
                break
            if sv.diem < 0:
                sv.diem = 0

    for sv in list_sv:
        print(sv)
