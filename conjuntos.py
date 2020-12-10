""""
empleados = {(1000, 'Manuel', 654233858),
             (2000, 'Ana', 232323232),
             (1500, 'Julia', None)}
"""

empleados = {1000: ('Manuel', 654233858),
             2000: ('Ana', 232323232),
             1500: ('Julia', None)}

for k, v in empleados.items():
    print(v[0], v[1])
