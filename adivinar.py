import random

def pedir_numero():
    while True:
        try:
            numero = int(input('Introduce un número: '))
            break
        except ValueError:
            print('El dato introducido no es un número')
    return numero

solucion = random.randint(1, 100)

while True:
    numero = pedir_numero()
    if numero > solucion:
        print('Te has pasado')
    elif numero < solucion:
        print('Es demasiado pequeño')
    else:
        print('¡Has acertado!')
        break
