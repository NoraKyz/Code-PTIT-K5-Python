import re
import collections
import math
import fractions
import itertools

users_list = []

if len(users_list) == 0:
    print("We need to find some users!")
else:
    for user in users_list:
        if user == 'quản trị viên':
            print("Xin chào " + user + ", bạn muốn xem báo cáo nào hôm nay?")
        else:
            print("Xin chào " + user + ", cảm ơn vì đăng nhập lại.")
