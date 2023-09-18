import re
import collections
import math
import fractions
import itertools

# Kiểm tra đẳng thức và bất đẳng thức với chuỗi (string).
print("Is 'a' + 'b' == 'ab'? I predict True.")
print('a' + 'b' == 'ab')
print("Is 'a' + 'b' == 'Ab'? I predict False.")
print('a' + 'b' == 'Ab')
print("Is 'ab' < 'abc'? I predict True.")
print('ab' < 'abc')
print("Is 'ab' < 'bc'? I predict True.")
print('ab' < 'bc')
print("Is '5' + '6' == '11'? I predict False.")
print('5' + '6' == '11')

# Kiểm tra sử dụng phương thức lower()
print("Is 'a' + 'b' == 'Ab'.lower()? I predict True.")
print('a' + 'b' == 'Ab'.lower())

# Kiểm tra có điều kiện với số trong các trường hợp: đẳng thức, bất đẳng thức, lớn hơn, nhỏ hơn, lớn hơn hoặc bằng, nhỏ hơn hoặc bằng.
print("Is 1+1 == 2? I predict True.")
print(1+1 == 2)
print("Is 1+1 > 3? I predict False.")
print(1+1 > 3)
print("Is 1+1 < 3? I predict True.")
print(1+1 < 3)
print("Is 1+1 <= 3? I predict True.")
print(1+1 <= 3)
print("Is 1+1 >= 3? I predict False.")
print(1+1 >= 3)

# Kiểm tra có điều kiện sử dụng từ khóa and hoặc or
a = True
b = False
print("Is a and b == False? I predict True.")
print(a and b == False)
print("Is a or b == True? I predict True.")
print(a or b == True)

# Kiểm tra xem một phần tử có trong danh sách không
a = [1, 2, 3]
print("Is 1 in a? I predict True.")
print(1 in a)
print("Is 4 in a? I predict False.")
print(4 in a)

# Kiểm tra xem một phần tử không có trong danh sách không
print("Is 4 not in a? I predict True.")
print(4 not in a)

