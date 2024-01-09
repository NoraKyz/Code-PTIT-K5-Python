import re
import collections
import math
import fractions
import itertools
import datetime

class Rider:
    def __init__(self, name, horse, fiTime):
        self.name = name
        self.horse = horse
        self.fiTime = fiTime

        self.setID()
        self.setV()

    def setID(self):
        self.id = ""

        for i in self.horse.split():
            self.id += i[0]
        for i in self.name.split():
            self.id += i[0]

    def setV(self):
        self.v = 0

        self.stTime = datetime.datetime.strptime("6:00", '%H:%M')
        self.fiTime = datetime.datetime.strptime(self.fiTime, '%H:%M')

        totalHour = (self.fiTime - self.stTime).total_seconds() / 3600

        self.v = 120 / totalHour


    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.horse} {round(self.v)} Km/h'
    
t = int(input())

riders = []

for i in range(t):
    riders.append(Rider(input(), input(), input()))

riders.sort(key=lambda x: x.v, reverse=True)

print(*riders, sep="\n")