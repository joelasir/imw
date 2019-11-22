import sys

k = int(sys.argv[1])
str = sys.argv[2]
count = 0
str_as_list = str.split()

if k < 0:
    print('Error')
else:
    for word in str_as_list:
        if k == len(word):
            count += 1

print(f'Hay {count} palabras de tamaño {k}')
