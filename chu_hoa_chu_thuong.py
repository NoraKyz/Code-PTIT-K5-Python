s = input()
cnt = sum(1 for c in s if c.isupper())

if(cnt * 2 > len(s)):
    print(s.upper())
else :
    print(s.lower())