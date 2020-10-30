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
1     si n < 10 (caso base)

digitos(n // 10) + 1 en otro caso (caso recursivo)


digitos = lambda n: 1 if n < 10 else digitos(n // 10) + 1

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


digitos(235)
= digitos(23) + 1
= digitos(2) + 1 + 1
= 1 + 1 + 1
= 3




digitos(235) = digitos(23) + 1


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




suma_rango = lambda a, b: 0 if a > b else \
                          a + suma_rango(a + 1, b)

suma_rango(4, 7)
= 4 + suma_rango(5, 7)
= 4 + 5 + suma_rango(6, 7)
= 4 + 5 + 6 + suma_rango(7, 7)
= 4 + 5 + 6 + 7 + suma_rango(8, 7)
= 4 + 5 + 6 + 7 + 0
