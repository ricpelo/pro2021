x = 5
y = 6

aux = x        # x = 5, y = 6, aux = 5
x = y          # x = 6, y = 6, aux = 5
y = aux        # x = 6, y = 5, aux = 5

x, y = y, x

"""
Asignación simple         x = 5
Asignación compuesta      x += 3
Asignación múltiple       x, y = 4, 3
"""
