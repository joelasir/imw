import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100
Adenine = 0
Thymine = 0
Guanine = 0
Cytosine = 0

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
for i in sequence:
    if i == 'A':
        Adenine += 1
    elif i == 'T':
        Thymine += 1
    elif i == 'G':
        Guanine += 1
    elif i == 'C':
        Cytosine += 1

print('Adenine:', Adenine)
print('Thymine:', Thymine)
print('Guanine:', Guanine)
print('Cytosine:', Cytosine)
