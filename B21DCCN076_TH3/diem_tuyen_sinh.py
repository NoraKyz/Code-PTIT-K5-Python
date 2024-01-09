import re

class Student:
    cnt = 0
    def __init__(self, name : str, score, nation, area):
        Student.cnt += 1
        self.id = 'TS' + format(Student.cnt, '02d')
        #   Nguyen  Hong     Ngat   => Nguyen Hong Ngat
        self.name = ' '.join(re.findall(r'\w+', name.title()))
        self.score = score
        self.nation = nation
        self.area = area  
        self.total_score = 0
        self.status = ''

    def get_total_score(self):
        if self.area == 1:
            self.total_score = self.score + 1.5
        elif self.area == 2:
            self.total_score = self.score + 1
        elif self.area == 3:
            self.total_score = self.score
        if self.nation != 'Kinh':
            self.total_score += 1.5
        return self.total_score

    def get_status(self):
        if self.total_score >= 20.5:
            self.status = 'Do'
        else:
            self.status = 'Truot'
        return self.status

    def __str__(self):
        return f'{self.id} {self.name} {self.get_total_score():.1f} {self.get_status()}'
    

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        score = float(input())
        nation = input()
        area = int(input())
        arr.append(Student(name, score, nation, area))
    arr.sort(key = lambda x: (-x.get_total_score(), x.id))
    for i in arr:
        print(i)
