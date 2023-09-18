import re, collections, math, fractions, itertools

users_list = ['quản trị viên', 'user1', 'user2', 'user3', 'user4']

for user in users_list:
    if user == 'quản trị viên':
        print("Xin chào " + user + ", bạn muốn xem báo cáo nào hôm nay?")
    else:
        print("Xin chào " + user + ", cảm ơn vì đăng nhập lại.")

