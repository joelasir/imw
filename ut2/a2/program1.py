import sys
from math import sqrt
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
if a == 0:
    x = float(-c / b)
    print('x =', x)
    sys.exit()
if (b ** 2) - (4 * a * c) < 0:
    print('No tiene solución real')
x1 = ((-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a))
x2 = ((-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a))
print('x1 =', x1)
print('x2 =', x2)
