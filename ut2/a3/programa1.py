import sys
num = int(sys.argv[1])
if num < 0:
    print('Error, el número no es positivo')
    sys.exit()
else:
    for i in range(2, num):
        if (num % i) == 0:
            print('Es un número primo')
            break
        else:
            print('No es un número primo')
            break
