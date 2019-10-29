import sys

cantidad = int(sys.argv[1])

if cantidad > 0:
    bill50 = cantidad // 50
    cantidad = cantidad % 50
    bill20 = cantidad // 20
    cantidad = cantidad % 20
    bill10 = cantidad // 10
    cantidad = cantidad % 10
    bill5 = cantidad // 5
    cantidad = cantidad % 5
    mon2 = cantidad // 2
    cantidad = cantidad % 2
    mon1 = cantidad // 1
    cantidad = cantidad % 1
    if bill50 > 0:
        if bill50 > 1:
            print(bill50, 'billetes de 50')
        else:
            print(bill50, 'billete de 50')
    if bill20 > 0:
        if bill20 > 1:
            print(bill20, 'billetes de 20')
        else:
            print(bill20, 'billete de 20')
    if bill10 > 0:
        print(bill10, 'billete de 10')
    if bill5 > 0:
        print(bill5, 'billete de 5')
    if mon2 > 0:
        if mon2 > 1:
            print(mon2, 'monedas de 2')
        else:
            print(mon2, 'moneda de 2')
    if mon1 > 0:
        print(mon1, 'moneda de 1')
