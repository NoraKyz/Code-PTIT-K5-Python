# 3.1
names = ["Duc", "Quan", "Toan", "Dang", "D.A"]
for i in names:
    print(i)

# 3.2
for i in names:
    print("Xin chao", i)

# 3.3
traffix = ["motor", "car", "bus", "bike"]
for i in traffix:
    print("I would like to own a", i)

# 3.4
guest_list = ["Duc", "Quan", "Toan", "Dang", "D.A"]
for i in guest_list:
    print("Would you like to have dinner with me?", i)

# 3.5 3.6 3.7


def GuestList(names):
    for i in names:
        print("Moi", i, "di an toi")
    print(names[0], names[2])
    names[0] = "Duc Anh"
    names[2] = "Toan"
    for i in names:
        print("Moi", i, "di an toi")

    print("Ban an co them nhieu cho moi:")
    names.insert(0, "Quan")
    names.insert(len(names) // 2, "Khanh")
    names.append("Quang")
    for i in names:
        print("Moi", i, "di an toi")
    print("Xin loi toi chi co the moi hai khach:")
    for i in range(len(names) - 2):
        print("Xin loi", names.pop())

    for i in names:
        print("Toi van moi", i, "di an toi")
    for i in range(2):
        del (names[len(names) - 1])
    print("Sau khi xoa, con lai so nguoi la:", end=" ")
    print(len(names))


GuestList(["Quan", "Long", "Dang", "Duc"])

# 3.8
visited_places = ["HaNoi", "CatBa", "DaNang", "HoiAn", "NhaTrang"]

print(*visited_places)
print(*sorted(visited_places))
print(*visited_places)
print(*sorted(visited_places, reverse=True))
print(*visited_places)
visited_places.reverse()
print(*visited_places)
visited_places.reverse()
print(*visited_places)
visited_places.sort()
print(*visited_places)
visited_places.sort(reverse=True)
print(*visited_places)

# 3.9
print(len(visited_places))

# 3.10


def EveryFuncition():
    ds = []
    print("Nhap so luong phan tu trong danh sach:")
    n = int(input())
    for i in range(n):
        ds.append(
            input("Nhap ten thanh pho, mon an, quoc gia ma ban thich: ", end=""))
    print("Danh sach vua nhap la:")
    for i in ds:
        print(i, end=" ")
    print()


EveryFuncition()

# 3.11
pizzas = ["Hawaiian", "Pepperoni", "Cheese"]
for i in pizzas:
    print(i, step=" ")
for i in pizzas:
    print("I like", i, "pizza.")
print("I really love pizza!")

# 3.12
animals = ["dog", "cat", "bird"]
for i in animals:
    print(i, step=" ")
for i in animals:
    print("A", i, "would make a great pet.")
print("Any of these animals would make a great pet!")

# 3.13
for i in range(1, 21):
    print(i, step=" ")

# 3.14
a = [i for i in range(1, 1000001)]
for i in a:
    print(i, step=" ")

# 3.15
print(min(a))
print(max(a))
print(sum(a))

# 3.16
for i in range(1, 21, 2):
    print(i, step=" ")

# 3.17
for i in range(3, 31, 3):
    print(i, step=" ")

# 3.18
a = []
for i in range(1, 11):
    a.append(i ** 3)
for i in a:
    print(i, step=" ")

# 3.19
a = [i ** 3 for i in range(1, 11)]
for i in a:
    print(i, step=" ")

# 3.20
print("the first three items in the list are:", *a[:3])
print("three items from the middle of the list are:", *a[4:7])
print("the last three items in the list are:", *a[-3:])

# 3.21
names = ["Hawaiian", "Pepperoni", "Cheese"]
print("Cac loai pizzas la:")
for i in names:
    print(i)
for i in names:
    print(" I like", i, "pizza.")
like = ["It make by ...", "It is from ...", "It is very big..."]
print("Mo ta pizzas:")
for i in like:
    print(i)
print("I really love pizza!")

friend_pizzas_list = names
names.append("Pizzas D")
friend_pizzas_list.append("Pizza E")
print("My favorite pizzas are: ")
for i in names:
    print(i, end=" ")
print()
print("My friend's favorite pizzas are:")
for i in friend_pizzas_list:
    print(i, end=" ")
print()

# 3.22
ds = ["dua hau", "vai", "cam", "chanh", "rau"]
print("Danh sach cac thuc pham la:")
for i in ds:
    print(i, end=" ")
print()
print("Danh sach cac loai thuc pham la:")
for i in range(len(ds)):
    print(ds[i], end=" ")
print()

# 3.23
ds = ["dua hau", "vai", "cam", "chanh", "rau"]
tupleds = (tuple)(ds)
print("Danh sach cac mon an la:")
for i in tupleds:
    print(i, end=" ")
print()
ds[0] = "trau"
ds[1] = "voi"
tupleds = (tuple)(ds)
print("Danh sach cac mon an moi la:")
for i in tupleds:
    print(i, end=" ")
print()
