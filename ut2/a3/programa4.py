import sys
num = int(sys.argv[1])
fact = 1
if num < 0:
    print('Error, el número no es positivo')
    sys.exit()
else:
    for i in range(1, num + 1):
        fact = fact * i
        print(i, '!=', fact)
