def solve(s = ""):
    return sum(1 for i in s if i.isupper()), sum(1 for i in s if i.islower())
