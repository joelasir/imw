import sys

def menu():
    phone_book = {}
    while True:
        print('1. Mostrar lista de contactos')
        print('2. Añadir contacto (nombre y teléfono)')
        print('3. Borrar contacto (nombre)')
        print('4. Salir')

        menu = input('Escoja una opción: ')

        if menu == "1":
            show_contacts(phone_book)
        elif menu == "2":
            name = input('¿Qué contacto que desea añadir?: ')
            if name not in phone_book:
                phone = input('Teléfono:')
                add_contact(phone_book, name, phone)
            else:
                print('El contacto ya existe \n')
        elif menu == "3":
            name = input('¿Qué contacto desea eliminar?: ')
            remove_contact(phone_book, name)
        elif menu == "4":
            sys.exit()
        else:
            print('ERROR: seleccione una opción válida. \n')

def show_contacts(phone_book):
    if phone_book == {}:
        print('No hay ningún contacto. \n')
    else:
        for name, phone in phone_book.items():
            print(name, ':', phone)

def add_contact(phone_book, name, phone):
        phone_book[name] = phone

def remove_contact(phone_book, name):
    if name in phone_book:
        del(phone_book[name])
    else:
        print('ERROR: el contacto no existe. \n')

if __name__ == '__main__':
    menu()
