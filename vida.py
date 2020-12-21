import random

def dibujar(tablero):
    print('\033c')
    for fila in tablero:
        for cel in fila:
            print(cel, end='')
        print()

def vecindad(tablero, i, j):
    def valor(x, y):
        lx = len(tablero)
        ly = len(tablero[0])
        return 1 if tablero[x % lx][y % ly] == 'X' else 0

    return valor(i - 1, j - 1) + valor(i - 1, j) + valor(i - 1, j + 1) \
           + valor(i, j - 1) + valor(i, j + 1) \
           + valor(i + 1, j - 1) + valor(i + 1, j) + valor(i + 1, j + 1)

def copiar(tabl):
    nuevo_tabl = tabl[:]
    for i, e in enumerate(tabl):
        nuevo_tabl[i] = e[:]
    return nuevo_tabl

# pedirle al usuario el número de generaciones que queremos
while True:
    try:
        max_gen = int(input('Introduce el número máximo de generaciones: '))
        break
    except ValueError:
        print('El número introducido es incorrecto.')
# crear una configuración inicial aleatoria del tablero

"""
tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
"""

tablero = [[random.choice(['X', ' ', ' ', ' ']) for i in range(25)] for j in range(25)]

# Hago una copia profunda (a dos niveles) de la lista:
nuevo_tablero = copiar(tablero)

# repetir lo siguiente tantas veces como indique el número de generaciones:
# - comprobar la vecindad de cada célula
# - mostrar el tablero
dibujar(tablero)

for gen in range(max_gen):
    for i, fila in enumerate(tablero):
        for j, cel in enumerate(tablero[i]):
            if tablero[i][j] == ' ':
                if vecindad(tablero, i, j) == 3:
                    nuevo_tablero[i][j] = 'X'
            else:
                if vecindad(tablero, i, j) not in [2, 3]:
                    nuevo_tablero[i][j] = ' '
    tablero = copiar(nuevo_tablero)
    dibujar(tablero)
    input()
