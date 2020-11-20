"""
Escribir un programa que imprima el número que se le pide al usuario
por el teclado. El programa pide números continuamente hasta que el
usuario escribe un 0 (en ese caso, se sale). Si escribe algo que no sea
un número, se queja.
"""

while True:
    try:
        x = int(input('Introduce el primer número: '))
        if x == 0:
            break
        y = int(input('Introduce el segundo número: '))
        print(x / y)
    except ValueError:
        print('Eso que me has escrito no es un número')
    except ZeroDivisionError:
        print('Has intentado dividir entre cero')
