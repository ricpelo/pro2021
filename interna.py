def operar(n1, n2, op):
    def suma(x, y):
        return x + y
    def resta(x, y):
        return x - y
    if op == '+':
        return suma(n1, n2)
    return resta(n1, n2)

print(operar(4, 3, '+'))
