import fractions

a = list(map(int, input().split()))

res = fractions.Fraction(a[0], a[1]) + fractions.Fraction(a[2], a[3])

print(f'{res.numerator}/{res.denominator}')