class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def is_valid(self):
        return self.length > 0 and self.width > 0

    def __str__(self):
        if self.is_valid():
            return f"{self.perimeter()} {self.area()} {self.color.capitalize()}"
        else:
            return "INVALID"


arr = input().split()
length = int(arr[0])
width = int(arr[1])
color = arr[2]
rectangle = Rectangle(length, width, color)
print(rectangle)
