import re, collections, math, fractions

s = input()

s = s[len(s) - 3::]
s = s.lower()

print( "yes" if s == ".py" else "no" )