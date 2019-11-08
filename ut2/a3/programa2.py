import sys
num = int(sys.argv[1])
sum = 0
if num < 0:
    print('Error, el número no es positivo')
    sys.exit()
else:
    for i in range(1, num + 1):
        sum = sum + (i ** 2)
print(sum)
