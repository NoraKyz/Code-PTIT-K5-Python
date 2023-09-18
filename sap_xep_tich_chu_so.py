import re, collections, math, fractions, itertools

t = int(input())

def mul_of_digits(number):
    total = 1
    while number > 0:
        total *= number % 10
        number //= 10
    return total

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a, key=lambda x: (mul_of_digits(x), x))
    print(*sorted_a)