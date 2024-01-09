class Teacher:
    cnt = 0
    def __init__(self, name, code, tin_hoc, chuyen_mon):
        Teacher.cnt += 1
        self.id = 'GV' + format(Teacher.cnt, '02d')
        self.name = name
        self.code = code
        self.tin_hoc = tin_hoc
        self.chuyen_mon = chuyen_mon
        self.total = self.tin_hoc * 2 + self.chuyen_mon + self.get_diem_uu_tien()
        self.result = 'TRUNG TUYEN' if self.total >= 18 else 'LOAI'

    def get_diem_uu_tien(self):
        if self.code[1] == '1':
            return 2
        elif self.code[1] == '2':
            return 1.5
        elif self.code[1] == '3':
            return 1
        else:
            return 0
        
    def get_mon(self):
        if self.code[0] == 'A':
            return 'TOAN'
        elif self.code[0] == 'B':
            return 'LY'
        else:
            return 'HOA'

    def __str__(self):
        return f'{self.id} {self.name} {self.get_mon()} {self.total:.1f} {self.result}'

if __name__ == '__main__':
    n = int(input())
    list_teacher = []
    for i in range(n):
        name = input()
        code = input()
        tin_hoc = float(input())
        chuyen_mon = float(input())
        list_teacher.append(Teacher(name, code, tin_hoc, chuyen_mon))
    list_teacher.sort(key= lambda x: x.total, reverse=True)
    for teacher in list_teacher:
        print(teacher)