from random import randint

x = randint(1, 100)
fin = False
while not fin:
    try:
        a = int(input('Adivina el numero: '))
        if a == x:
            print('Has acertado.')
            fin = True
        elif a == 0:
            print('Adios.')
            fin = True
        else:
            print('Vuelve a intentarlo. Si te rindes introduce 0')
    except ValueError:
        print('Error, debes introducir un numero')
