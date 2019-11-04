import sys
from math import pi
r = float(sys.argv[1])
print('(1) Calcular el diámetro de la circuferencia')
print('(2) Calcular el perímetro de la circuferencia')
print('(3) Calcular el área del círculo')
print('(4) Salir')
eleccion = int(input('Selecciona algo '))
d =  2 * r
p = 2 * pi * r
a = pi *(r ** 2)
if eleccion == 1:
    print('Diámetro', d)
elif eleccion == 2:
    print('Perímetro', p)
elif eleccion == 3:
    print('Área', a)
elif eleccion == 4:
    sys.exit()
else:
    print('Error, selecciona una opción válida')
