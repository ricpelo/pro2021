def deposito(saldo):
    def saldo_actual():
        return saldo

    def ingresar(cantidad):
        nonlocal saldo
        saldo += cantidad

    def retirar(cantidad):
        nonlocal saldo
        if cantidad <= saldo:
            saldo -= cantidad
        else:
            raise ValueError('Fondos insuficientes')

    dispatch = {
        'saldo_actual': saldo_actual,
        'ingresar': ingresar,
        'retirar': retirar
    }

    def despacho(mensaje):
        if mensaje in dispatch:
            return dispatch[mensaje]
        else:
            raise ValueError('Operación incorrecta')

    return despacho
