t = int(input())

for _ in range(t):
    b = int(input())
    a = int(input(), 2)
    
    res = ""
    while a > 0:
        x = a % b
        if(x > 9):
            x = chr(x + 55)
        res = str(x) + res
        a //= b
    print(res)