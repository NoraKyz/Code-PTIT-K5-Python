with open('DATA.in', 'r') as file:

    t = int(file.readline().strip())

    for _ in range(t):

        b = int(file.readline().strip())
        a = int(file.readline().strip(), 2)

        res = ""
        while a > 0:
            x = a % b
            if (x > 9):
                x = chr(x + 55)
            res = str(x) + res
            a //= b
        print(res)
