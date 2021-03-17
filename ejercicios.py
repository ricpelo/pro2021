"""
ActiveRecord
"""
class Cuenta:
    __ultimo = 0
    __cuentas = {}

    def __init__(self, titular):
        Cuenta.__ultimo += 1
        self.__numero = Cuenta.__ultimo
        self.__titular = titular
        self.__movimientos = []
        self.__saldo = 0
        Cuenta.__cuentas[self.__numero] = self

    @staticmethod
    def get_cuenta(numero):
        return Cuenta.__cuentas.get(numero)

Cuenta('Ricardo')

c = Cuenta.get_cuenta(1)
