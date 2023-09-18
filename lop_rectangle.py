import re, collections, math, fractions, itertools

class Rectangle:
    def __init__(self, h, w, color):
        self.h = h
        self.w = w
        self.c = color
    
    def perimeter(self):
        return 2*(self.h + self.w)
    def area(self):
        return self.h * self.w 
    def color(self):
        return self.c.title()
    
def Decimal(n):
    return float(n)

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')