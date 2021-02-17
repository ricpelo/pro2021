class Cuenta:
    __cuentas = []
    __total = 0

    def __init__(self, saldo):
        if Cuenta.__cuentas == []:
            self.__numero = 1
        else:
            self.__numero = Cuenta.__cuentas[-1].numero() + 1
        self.__saldo = saldo
        Cuenta.__cuentas.append(self)
        Cuenta.__total += saldo

    def numero(self):
        return self.__numero

    def saldo(self):
        return self.__saldo

    @staticmethod
    def cuenta_iesima(i):
        return Cuenta.__cuentas[i]

    @staticmethod
    def cantidad():
        return len(Cuenta.__cuentas)

    @staticmethod
    def total():
        return Cuenta.__total

Cuenta(500)
Cuenta(800)
Cuenta(1200)
print(Cuenta.cantidad())
print(Cuenta.cuenta_iesima(1).saldo())
print(Cuenta.total())
