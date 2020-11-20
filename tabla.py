"""
inicio
  leer n
  construir la tabla de n × n
fin
"""

"""
inicio
  n = int(input())
  i ← 1
  mientras i ≤ n hacer
      escribir la fila de i
      i ← i + 1
fin
"""

"""
inicio
  n = int(input())
  i = 1
  while i <= n:
      j ← 1
      mientras j ≤ n hacer
          escribir i × j
          j ← j + 1
      escribir un salto de línea
      i += 1
fin
"""

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i * j, end=' ')
        j += 1
    print('')
    i += 1
