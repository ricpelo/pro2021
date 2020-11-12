"""
sdflksdfjklhsdkjfs
sdfkljshfkjskjs
"""

x = 25 # kdalksjdlkajdlkasjlkdadlk
z = 99 # sldjflskjdflksjflkdsjflksd
y = z

factorial = lambda n: 1 if n == 0 else \
                      n * factorial(n - 1)


"""
Diseñar una función que calcule el número de dígitos de un número.

Especificación:

Pre: n >= 0
digitos(n: int) -> int
Post: digitos(n) = el número de dígitos de n
"""

"""
1     si n < 10 (caso base)

digitos(n // 10) + 1 en otro caso (caso recursivo)
"""

digitos = lambda n: 1 if n < 10 else digitos(n // 10) + 1

"""
digitos(235)                  # evalúa digitos y devuelve lambda
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(235) # evalúa 235
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(235) # beta-reducción
= (1 if 235 < 10 else digitos(235 // 10) + 1) # evalúa el if
= digitos(235 // 10) + 1      # evalúa digitos y devuelve lambda
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(235 // 10) + 1
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(23) + 1
= (1 if 23 < 10 else digitos(23 // 10) + 1) + 1
= digitos(23 // 10) + 1 + 1
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(23 // 10) + 1 + 1
= (lambda n: 1 if n < 10 else digitos(n // 10) + 1)(2) + 1 + 1
= (1 if 2 < 10 else digitos(2 // 10) + 1) + 1 + 1
= 1 + 1 + 1
= 3
"""

"""
digitos(235)
= digitos(23) + 1
= digitos(2) + 1 + 1
= 1 + 1 + 1
= 3

digitos(235) = digitos(23) + 1
"""

"""
Diseñar una función recursiva que calcule la suma de los números
comprendidos entre a y b, siendo a y b dos números enteros que se
reciben como argumentos.

Especificación:

Pre: True
suma_rango(a: int, b: int) -> int
Post: suma_rango(a, b) = la suma de los números
                         comprendidos entre a y b.
      suma_rango(a, b) = 0 cuando a > b
"""

"""
suma_rango(4, 7) = 4 + 5 + 6 + 7 = 4 + suma_rango(5, 7)
suma_rango(1, 5) = 1 + 2 + 3 + 4 + 5
suma_rango(3, 3) = 3
suma_rango(4, 3) = 0

suma_rango(a, b) = 0 si a > b (caso base)
suma_rango(a, b) = a + suma_rango(a + 1, b) (caso recursivo)

suma_rango(6, 7)
= 6 + suma_rango(7, 7)
= 6 + 7 + suma_rango(8, 7)
= 6 + 7 + 0
"""

suma_rango = lambda a, b: 0 if a > b else \
                          a + suma_rango(a + 1, b)

"""
suma_rango(4, 7)
= 4 + suma_rango(5, 7)
= 4 + 5 + suma_rango(6, 7)
= 4 + 5 + 6 + suma_rango(7, 7)
= 4 + 5 + 6 + 7 + suma_rango(8, 7)
= 4 + 5 + 6 + 7 + 0
"""


"""
Escribir una función que calcule la suma de todos los números enteros
comprendidos entre 1 y n.

Especificación:

Pre: n >= 0
suma_hasta(n: int) -> int
Post: suma_hasta(n) = 1 + 2 + 3 + 4 + ... + n
"""

"""
suma_hasta(n) = 1 + 2 + 3 + 4 + ... + n = n * (n + 1) / 2

suma_hasta(n) = 0 si n == 0 (caso base)
suma_hasta(n) = suma_hasta(n - 1) + n
"""

suma_hasta1 = lambda n: suma_rango(1, n)
suma_hasta2 = lambda n: 0 if n == 0 else suma_hasta2(n - 1) + n
suma_hasta3 = lambda n: n * (n + 1) / 2


suma_rango = lambda a, b: 0 if a > b else a + suma_rango(a + 1, b)

"""
Diseñar una función recursiva que calcule el producto de los números
comprendidos entre a y b, siendo a y b dos números enteros que se
reciben como argumentos.

Especificación:

Pre: True
producto_rango(a: int, b: int) -> int
Post: producto_rango(a, b) = el producto de los números
                             comprendidos entre a y b.
      producto_rango(a, b) = 1 cuando a > b
"""

"""
producto_rango(4, 7) = 4 * 5 * 6 * 7
producto_rango(7, 7) = 7
producto_rango(8, 7) = 1

producto_rango(4, 7) = 4 * producto_rango(5, 7)

producto_rango = lambda a, b: 1 if a > b else a * producto_rango(a + 1, b)
producto_hasta(n) = 1 * 2 * 3 * 4 * 5 * ... * n
producto_hasta1 = lambda n: factorial(n)
producto_hasta2 = lambda n: producto_rango(1, n)
|    X      |
|    XX     |
|    XXX    |
A     B     C
"""

"""
Pre: n >= 0
hanoi(n: int, a: str, b: str, c: str) -> str
Post: hanoi(n, a, b, c) = una cadena que contiene los movimientos que
                          hay que realizar para solucionar el puzzle
                          de mover n discos de a a b, con c como pivote
                          auxiliar en el puzzle de las Torres de Hanoi.
"""

hanoi = lambda n, a, b, c: '' if n == 0 else \
                           hanoi(n - 1, a, c, b) + \
                           'mueve un disco del ' + a + ' al ' + b + '\n' + \
                           hanoi(n - 1, c, b, a)

suma_rango = lambda a, b: 0 if a > b else a + suma_rango(a + 1, b)

suma_rango_iter = lambda a, b, acc: acc if a > b else \
                                    suma_rango_iter(a + 1, b, acc + a)
suma_rang = lambda a, b: suma_rango_iter(a, b, 0)

fib_iter = lambda cont, a, b: a if cont == 0 else \
                              fib_iter(cont - 1, b, a + b)
fib = lambda n: fib_iter(n, 0, 1)

fact_iter = lambda cont, acc: acc if cont == 0 else \
                              fact_iter(cont - 1, cont * acc)
factorial = lambda n: fact_iter(n, 1)

"""
Escribir una función que calcule la longitud de una cadena.

Especificación:

Pre:  True
      longitud(s: str) -> int
Post: longitud(s) = len(s)
"""

"""
s == ''                ==> longitud(s) == 0
s == s[0] + s[1:]      ==> longitud(s) = 1 + longitud(s[1:])
"""

longitud = lambda s: 0 if s == '' else 1 + longitud(s[1:])

"""
longitud('hola')
= 1 + longitud('ola')
= 1 + 1 + longitud('la')
= 1 + 1 + 1 + longitud('a')
= 1 + 1 + 1 + 1 + longitud('')
= 1 + 1 + 1 + 1 + 0
= 1 + 1 + 1 + 1
= 1 + 1 + 2
= 1 + 3
= 4
"""

long_iter = lambda s, acc: acc if s == '' else \
                           long_iter(s[1:], acc + 1)
longitud = lambda s: long_iter(s, 0)

"""
s_nuevo = s_viejo[1:]
acc_nuevo = acc_viejo + 1
"""

"""
  s        acc
-------- -------
 'hola'     0
 'ola'      1
 'la'       2
 'a'        3
 ''         4
"""

"""
longitud('hola')
= long_iter('hola', 0)
= long_iter('ola', 1)
= long_iter('la', 2)
= long_iter('a', 3)
= long_iter('', 4)
= 4
"""

"""
Escribir una función que cuente cuántas vocales hay en una cadena.

Especificación:

Pre:  True
      vocales(s: str) -> int
Post: vocales(s) = el número de vocales de s

Indicación: crearse una función que compruebe si un carácter es vocal o no.

Especificación:

Pre:  len(s) == 1
      vocal(s: str) -> bool
Post: vocal(s) == True si s es una vocal, False en caso contrario.
                  No se deben distinguir mayúsculas de minúsculas,
                  y las vocales acentuadas también son vocales.
"""

vocal = lambda s: s.lower() == 'a' or s.lower() == 'e' or \
                  s.lower() == 'i' or s.lower() == 'o' or \
                  s.lower() == 'u'

vocales = lambda s: 0 if s == '' else \
                    vocales(s[1:]) + (1 if vocal(s[0]) else 0)

vocales_iter = lambda s, acc: acc if s == '' else \
                              vocales_iter(s[1:], acc + (1 if vocales(s[0]) else 0))
vocales_iterativo = lambda s: vocales_iter(s, 0)

long_tupla = lambda t: 0 if t == () else 1 + long_tupla(t[1:])

suma_range = lambda r: 0 if r == range(0) else \
                       r[0] + suma_range(r[1:])

prod_range = lambda r: 1 if r == range(0) else \
                       r[0] * prod_range(r[1:])

fact_range = lambda n: prod_range(range(1, n + 1))

cubo = lambda n: n * n * n

"""
Especificación:

Pre:  los elementos de t deben ser números
Sig:  tupla_cubos(t: tuple) -> tuple
Post: tupla_cubos(t) = una tupla formada por los elementos de t
                       elevados al cubo
"""

import math

tupla_cubos = lambda t: () if t == () else \
                        (t[0] ** 3,) + tupla_cubos(t[1:])

tupla_cuadrados = lambda t: () if t == () else \
                            (t[0] ** 2,) + tupla_cuadrados(t[1:])

tupla_raiz = lambda t: () if t == () else \
                       (math.sqrt(t[0]),) + tupla_raiz(t[1:])

mi_map = lambda f, t: () if tuple(t) == () else \
                      (f(t[0]),) + mi_map(f, t[1:])

mi_filter = lambda f, t: () if t == () else \
                         ((t[0],) if f(t[0]) else ()) + mi_filter(f, t[1:])

from functools import reduce
suma = lambda tupla: reduce(lambda x, y: x + y, tupla, 0)
producto = lambda tupla: reduce(lambda x, y: x * y, tupla, 1)

"""
Escribir una función que devuelva el máximo de una tupla.

Pre:  Todos los elementos de t son números enteros y t != ()
      maximo(t: tuple) -> int
Post: maximo(t) = el mayor elemento de t
"""

maximo = lambda t: t[0] if t[1:] == () else \
                   max(t[0], maximo(t[1:]))

max_iter = lambda t, acc: acc if t == () else \
                          max_iter(t[1:], max(acc, t[0]))
maxi = lambda t: max_iter(t, t[0])

maximo = lambda t: reduce(max, t)
minimo = lambda t: reduce(min, t)

"""
    t           acc
  -----       -------
 (4, 2, 5)       4
   (2, 5)       max(4, 2) = 4
   (5,)         max(4, 5) = 5
   ()            5
"""




"""
maximo((4, 2, 5))
= max(4, maximo((2, 5)))
= max(4, max(2, maximo((5,))))
= max(4, max(2, 5))
= max(4, 5)
= 5
"""


"""
Escribir una función que devuelva cuántos elementos hay en la tupla

Pre:  True
      cuantos(t: tuple) -> int
Post: cuantos(t) = len(t)
"""

cuantos = lambda t: 0 if t == () else 1 + cuantos(t[1:])

cuantos_iter = lambda t, acc: acc if t == () else \
                              cuantos_iter(t[1:], acc + 1)
cuant = lambda t: cuantos_iter(t, 0)

cuantos = lambda t: reduce(lambda x, y: x + 1, t, 0)

"""
cuantos((4, 3, 2))
= reduce(lambda x, y: x + 1, (4, 3, 2), 0)
= ((0 + 1) + 1) + 1 = 3
"""


reduce = lambda f, t, i: i if t == () else \
                         reduce(f, t[1:], f(i, t[0]))

reduce(suma, (1, 2, 3), 0)
= reduce_iter(suma, (1, 2, 3), 0)
= reduce_iter(suma, (2, 3), suma(0, 1))
= reduce_iter(suma, (2, 3), 1)
= reduce_iter(suma, (3,), suma(1, 2))
= reduce_iter(suma, (3,), 3)
= reduce_iter(suma, (), suma(3, 3))
= reduce_iter(suma, (), 6)
= 6




reduce(suma, (1, 2, 3), 0)
= reduce_aux(suma, (0, 1, 2, 3))
= suma(0, reduce_aux(suma, (1, 2, 3)))
= suma(0, suma(1, reduce_aux(suma, (2, 3))))
= suma(0, suma(1, suma(2, reduce_aux(suma, (3,)))))
= suma(0, suma(1, suma(2, 3)))


suma = lambda x, y: x + y
reduce(suma, (1, 2, 3), 0))
= reduce_aux(suma, (0, 1, 2, 3))
= suma(reduce_aux(suma, (1, 2, 3), 0)
= suma(suma(reduce_aux(suma, (2, 3)), 1), 0)
= suma(suma(suma(reduce_aux(suma, (3,)), 2), 1), 0)
= suma(suma(suma(3, 2), 1), 0)
= suma(suma(5, 1), 0)
= suma(6, 0)
= 6






= suma(reduce_aux(suma, reduce_aux(suma, (2, 3)), 1)), 0)
= suma(reduce_aux(suma, reduce_aux(suma, reduce_aux(suma, (3,), 2), 1), 0))

reduce(max, (1, 2, 3), 1)
= max(reduce(max, (2, 3), 1), 1)
= max(max(reduce(max, (3,), 1), 1)))
= max(max(3, 1), 1)
= max(3, 1)
= 3


reduce(max, (1, 2, 3), 1)
= max(1, reduce(max, (2, 3), 1))
= max(1, max(2, reduce(max, (3,), 1)))
= max(1, max(2, 3))
= max(1, 3)
= 3
