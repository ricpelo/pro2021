def suma_tupla(t):
    suma = 0
    it = iter(t)
    while True:
        try:
            suma += next(it)
        except StopIteration:
            return suma

def suma_for(t):
    suma = 0
    for x in t:
        suma += x ** 2
    return suma

print(suma_for(range(2, 15)))
