import re, collections, math, fractions, itertools

current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['User1', 'user2', 'user6', 'user7', 'user8']

clone_current_users = [current_user.lower() for current_user in current_users]

for user in new_users:
    if user.lower() in clone_current_users:
        print("Tên người dùng " + user + " đã được sử dụng, vui lòng chọn tên khác.")
    else:
        print("Tên người dùng " + user + " có thể sử dụng.")
