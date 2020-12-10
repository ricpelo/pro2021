import sys
try:
    x = float(sys.argv[1])
except IndexError:
    print('El dato de entrada no es un número real.')
except ValueError:
    print('No hay dato de entrada.')
else:
    print('El cuadrado de x es', x ** 2)

"""
a. No, porque los nombres de las excepciones están intercambiados.

b. Ninguna de las anteriores.

c. Sí.

d. No, porque la expresión x ** 2 puede fallar y debería ir dentro de un try.
"""


"""
¿Cuántos marcos como máximo habrá en el entorno durante la ejecución del siguiente programa?
"""

def prueba(n):
    def auxiliar():
        return True
    print(n)
    if n == 0:
        return 1
    else:
        return prueba(n - 1)

prueba(5)

"""
a. 4.

b. Ninguna de las anteriores.

c. 2. (correcta)

d. 3.
"""


"""
Suponiendo que el marco global también se almacena en la pila de control,
¿cuántos marcos como máximo se almacenarán en la pila de control
durante la ejecución del siguiente programa?
"""

def prueba(n):
    def auxiliar():
        return (lambda x: x + 1)(9)
    print(n)
    print(auxiliar())
    if n == 0:
        return 1
    else:
        return prueba(n - 1)

prueba(5)

"""
Seleccione una:

a. 7. (correcta)

b. Ninguna de las anteriores.


c. 6.


d. 8.
"""
