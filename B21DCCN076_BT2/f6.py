def solve(s = ""):
    res = ""
    for i in s.split():
        res += i + " "
    return res

print(solve("Hello World"))
