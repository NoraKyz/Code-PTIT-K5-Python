def find_zodiac_sign(day, month):
    zodiac_signs = [
        ("Bach Duong", [(3, 21), (4, 19)]),
        ("Kim Nguu", [(4, 20), (5, 20)]),
        ("Song Tu", [(5, 21), (6, 20)]),
        ("Cu Giai", [(6, 21), (7, 22)]),
        ("Su Tu", [(7, 23), (8, 22)]),
        ("Xu Nu", [(8, 23), (9, 22)]),
        ("Thien Binh", [(9, 23), (10, 22)]),
        ("Thien Yet", [(10, 23), (11, 22)]),
        ("Nhan Ma", [(11, 23), (12, 21)]),
        ("Ma Ket", [(12, 22), (1, 19)]),
        ("Bao Binh", [(1, 20), (2, 18)]),
        ("Song Ngu", [(2, 19), (3, 20)])
    ]
    
    for sign, (start_date, end_date) in zodiac_signs:
        if (month == start_date[0] and day >= start_date[1]) or \
           (month == end_date[0] and day <= end_date[1]):
            return sign
    return ""

t = int(input())
for _ in range(t):
    day, month = map(int, input().split())
    zodiac_sign = find_zodiac_sign(day, month)
    if zodiac_sign:
        print(zodiac_sign)