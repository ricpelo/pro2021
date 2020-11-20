numero = int(input('Introduzca el número: '))

i = 0
res = 1

while i < numero:
    i += 1
    res *= i

print('El factorial de', numero, 'es', res)


fact = lambda n: fact_iter(n, 1)

fact_iter = lambda cont, acc: acc if cont == 0 else \
                              fact_iter(cont - 1, acc * cont)

cont = numero
acc = 1

while cont > 0:
    acc, cont = acc * cont, cont - 1

print(acc)
