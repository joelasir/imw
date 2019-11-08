import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
if num1 < 0 or num2 < 0:
    print('Error, introduzca solo números positivos')
    sys.exit()
else:
    if num1 > num2:
        for i in range(num2, 0, -1):
            if num2 % i == 0 and num1 % i == 0:
                print(i)
                break
    else:
        if num2 > num1:
             for i in range(num1, 0, -1):
                 if num1 % i == 0 and num2 % i == 0:
                     print(i)
                     break
