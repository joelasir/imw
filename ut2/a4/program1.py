import sys
dni = sys.argv[1]

let = 'TRWAGMYFPDXBNJZSQVHLCKE'

if len(dni) != 8:
    print('Error')
else:
    rest = int(dni) % 23
    print(f'{dni}{let[rest]}')
