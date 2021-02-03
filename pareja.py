def pareja(x, y):
    def select(i):
        if i == 0:
            return x
        return y

    def set_pareja(i, v):
        nonlocal x
        nonlocal y
        if i == 0:
            x = v
        else:
            y = v

    def despacho(mensaje):
        if mensaje == 'select':
            return select
        elif mensaje == 'set_pareja':
            return set_pareja
        else:
            raise ValueError('Operación incorrecta')

    return despacho
