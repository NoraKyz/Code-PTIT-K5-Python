t = int(input())

for _ in range(t):
    n = input()
    res = []
    for i in range (int(n)):
        if str(i) != str(i)[::-1] or (len(str(i)) % 2 == 1):
            continue
                   
        if all(digit not in "13579" for digit in str(i)):
            res.append(i)

    
    for _ in res:
        print(_, end= " ")
    print()