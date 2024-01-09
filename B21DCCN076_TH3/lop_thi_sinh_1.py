class ThiSinh:
    def __init__(self, name, dob, a, b, c):
        self.name = name
        self.dob = dob
        self.a = a
        self.b = b
        self.c = c

    def getGPA(self):
        return f'{(self.a + self.b + self.c):.1f}'

    def __str__(self):
        return f'{self.name} {self.dob} {self.getGPA()}'


if __name__ == '__main__':
    name = input()
    dob = input()
    a = float(input())
    b = float(input())
    c = float(input())
    x = ThiSinh(name, dob, a, b, c)
    print(x)
