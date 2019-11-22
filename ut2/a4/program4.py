import sys

list = sys.argv[1:]

sum = 0

for numbers in list:
    count = len(list)
    sum = sum + float(numbers)
avg = sum / count
print('La media de los valores es', avg)
