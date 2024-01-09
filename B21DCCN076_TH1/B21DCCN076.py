import math


def cau_1(a: int):
    return a % 3 == 0 and 50 <= a <= 100


def cau_2(a: float):
    return a.is_integer()


def cau_3(a, b, c):
    d = (a + b) ** c
    return 100 <= d <= 200


def cau_4(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Vo Nghiem"


def cau_5(month: int, year: int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    else:
        return 30


def cau_6(math, literature, english):
    if (math < 0 or math > 10 or literature < 0 or literature > 10 or english < 0 or english > 10):
        return "Diem khong hop le"

    if 8 <= (math + literature + english) / 3 <= 10 and math >= 8 and literature >= 8 and english >= 6.5:
        return "Học sinh giỏi"
    elif 6.5 <= (math + literature + english) / 3 <= 7.9 and math >= 6.5 and literature >= 6.5 and english >= 5:
        return "Học sinh khá"
    elif 5 <= (math + literature + english) / 3 <= 6.4 and math >= 5 and literature >= 5 and english >= 3.5:
        return "Học sinh trung bình"
    elif 3.5 <= (math + literature + english) / 3 <= 4.9 and math >= 3.5 and literature >= 3.5 and english >= 2:
        return "Học sinh yếu"
    else:
        return "Học sinh kém"


def cau_7(n: int):
    return (n+1) * n / 2


def cau_8(a: int):
    divisor = []
    for i in range(1, math.sqrt(a)+1):
        if a % i == 0:
            divisor.append(i)
            if i != a // i:
                divisor.append(a // i)

    return sorted(divisor)


def cau_9(a, b):
    divisor_a_and_b = []
    divisor_a = cau_8(a)
    for i in divisor_a:
        if b % i == 0:
            divisor_a_and_b.append(i)
    return divisor_a_and_b


def cau_10(A):
    if A <= 0:
        return "Khong co so Fibonacci nao nho hon A"

    fi = [1, 1]
    while fi[-1] <= A:
        fi.append(fi[-1] + fi[-2])

    return fi[-2]


def cau_11():
    max_num = -math.inf
    min_num = math.inf

    while True:
        num = int(input())
        if num == -1:
            break
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    return max_num, min_num


def cau_12(N, tours):
    rooms : list = [0] * N
    idx = 0
    for num_people in tours:
        while idx < N and num_people > 0:
            rooms[idx] += 2 if num_people >= 2 else 1
            num_people -= rooms[idx]
            idx += 1 

        if num_people > 0:
            for i in range(N):
                if num_people == 0:
                    break

                if rooms[i] == 1:
                    rooms[i] += 1
                    num_people -= 1
            
            if num_people > 0:
                return "Khong du phong"
        
    return rooms

def cau_13():
    prices = {"Gà rán": 30000, "hamburger": 25000, "cocacola": 10000}
    quantities = {}
    total_cost = 0
    for item, price in prices.items():
        quantity = int(input(f"Nhap so luong {item}: "))
        quantities[item] = quantity
        total_cost += quantity * price

    pre_tax_total = sum(quantities[item] *
                        price for item, price in prices.items())
    tax = pre_tax_total * 0.1
    total_cost += tax

    print("Hoa don:")
    for item, quantity in quantities.items():
        print(
            f"{item}: {quantity} x {prices[item]}đ = {quantity * prices[item]}đ")
    print(f"Tong truoc thue: {pre_tax_total}đ")
    print(f"Thue: {tax}đ")
    print(f"Tong sau thue: {total_cost}đ")


def main():
    choice = int(input("Nhap bai tap: "))

    if choice == 1:
        a = int(input("Nhap so nguyen a: "))
        print(cau_1(a))
    elif choice == 2:
        a = float(input("Nhap so thuc a: "))
        print(cau_2(a))
    elif choice == 3:
        a = int(input("Nhap a: "))
        b = int(input("Nhap b: "))
        c = int(input("Nhap c: "))
        print(cau_3(a, b, c))
    elif choice == 4:
        a = float(input("Nhap a: "))
        b = float(input("Nhap b: "))
        c = float(input("Nhap c: "))
        print(cau_4(a, b, c))
    elif choice == 5:
        month = int(input("Nhap thang: "))
        year = int(input("Nhap nam: "))
        print(cau_5(month, year))
    elif choice == 6:
        math = float(input("Nhap diem toan: "))
        literature = float(input("Nhap diem van: "))
        english = float(input("Nhap diem anh: "))
        print(cau_6(math, literature, english))
    elif choice == 7:
        n = int(input("Nhap n: "))
        print(cau_7(n))
    elif choice == 8:
        a = int(input("Nhap so nguyen duong a: "))
        print(cau_8(a))
    elif choice == 9:
        a = int(input("Nhap so nguyen duong a: "))
        b = int(input("Nhap so nguyen duong b: "))
        print(cau_9(a, b))
    elif choice == 10:
        A = int(input("Nhap so A: "))
        print(cau_10(A))
    elif choice == 11:
        max_num, min_num = cau_11()
        print(f"So lon nhat: {max_num}")
        print(f"So lon nhat: {min_num}")
    elif choice == 12:
        N = int(input("Nhap so phong: "))
        M = int(input("Nhap so doan: "))
        doankhach = []
        for i in range(M):
            num_people = int(input(f"Nhap so nguoi trong doan {i+1}: "))
            doankhach.append(num_people)
        room_assignments = cau_12(N, doankhach)
        print(*room_assignments)

    elif choice == 13:
        cau_13()
    else:
        print("So ban nhap khong phu hop voi bai tap nao!")


if __name__ == "__main__":
    main()
