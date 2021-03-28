"""
arccos = math.acos()
arch = math.acosh()
arsh = math.asinh()
sh = math.sinh()
ch = math.cosh()
sgn = math.copysign(1, x)
"""

import math

# print('Решение уравнения вида ax^3 + bx^2 + cx + d = 0')
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))
d = float(input('Введите коэффициент d: '))

b, c, d = b / a, c / a, d / a  # сокращение на a

q = (b ** 2 - 3 * c) / 9

r = (2 * b ** 3 - 9 * b * c + 27 * d) / 54

s = q ** 3 - r ** 2

i = 1j

if s > 0:
    phi = (1 / 3) * math.acos(r / math.sqrt(q ** 3))
    firstroot = -2 * math.sqrt(q) * math.cos(phi) - (b / 3)
    secondroot = -2 * math.sqrt(q) * math.cos(phi + (2 / 3) * math.pi) - (b / 3)
    thirdroot = -2 * math.sqrt(q) * math.cos(phi - (2 / 3) * math.pi) - (b / 3)
elif s < 0:
    if q > 0:
        phi = (1 / 3) * math.acosh(math.fabs(r) / math.sqrt(q ** 3))
        firstroot = -2 * math.copysign(1, r) * math.sqrt(q) * math.cosh(phi) - (b / 3)
        secondroot = math.copysign(1, r) * math.sqrt(q) * math.cosh(phi) - (b / 3) + i * math.sqrt(3) * math.sqrt(q) * math.sinh(phi)
        thirdroot = math.copysign(1, r) * math.sqrt(q) * math.cosh(phi) - (b / 3) - i * math.sqrt(3) * math.sqrt(q) * math.sinh(phi)
    elif q < 0:
        phi = (1 / 3) * math.asinh(math.fabs(r) / math.sqrt(math.fabs(q) ** 3))
        firstroot = -2 * math.copysign(1, r) * math.sqrt(math.fabs(q)) * math.sinh(phi) - (b / 3)
        secondroot = math.copysign(1, r) * math.sqrt(math.fabs(q)) * math.sinh(phi) - (b / 3) + i * math.sqrt(3) * math.sqrt(math.fabs(q)) * math.cosh(phi)
        thirdroot = math.copysign(1, r) * math.sqrt(math.fabs(q)) * math.sinh(phi) - (b / 3) - i * math.sqrt(3) * math.sqrt(math.fabs(q)) * math.cosh(phi)
else:
    firstroot = -2 * math.copysign(1, r) * math.sqrt(q) - (b / 3)
    secondroot = math.copysign(1, r) * math.sqrt(q) - (b / 3)
    thirdroot = math.nan

"""
print('x1 =', firstroot)
print('x2 =', secondroot)
print('x3 =', thirdroot)
print()
print('Q =', q)
print('R =', r)
print('S =', s)
"""