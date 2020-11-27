import sys

try:
    if len(sys.argv) >= 2:
        x = float(sys.argv[1])
    else:
        x = float(input('Introduce el número: '))
    print('El cuadrado de', x, 'es', x ** 2)
except ValueError:
    print('El dato de entrada no es un número real.')
