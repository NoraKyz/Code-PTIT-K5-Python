import re, collections, math, fractions, itertools, datetime

class player:
    id = ""
    name = ""
    timeIn = ""
    timeOut = ""
    totalTime = ""

    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name
        self.timeIn = timeIn
        self.timeOut = timeOut

        x = datetime.datetime.strptime(self.timeOut, '%H:%M')
        y = datetime.datetime.strptime(self.timeIn, '%H:%M')
        self.totalTime = str(x-y)[:-3]


    def __str__(self):
        return self.id + " " + self.name + " " + ("{} gio {} phut".format(int(self.totalTime.split(":")[0]), int(self.totalTime.split(":")[1])))

t = int(input())
a = []
for _ in range(t):
    a.append(player(input(), input(), input(), input()))
    
a.sort(key=lambda x: x.totalTime, reverse=True)
print(*a, sep="\n")
    