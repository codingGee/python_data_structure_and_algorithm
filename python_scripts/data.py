''' working with decimal  '''

import decimal

x = decimal.Decimal(3.14); y = decimal.Decimal(2.74)

print(x * y)

decimal.getcontext().prec = 4

print(x * y)


''' working with fraction '''

import fractions
print(fractions.Fraction(3, 4))
# create a fraction from a floating nmber
print(fractions.Fraction(0.5))
#crate a franction from a string
print(fractions.Fraction('.25'))


