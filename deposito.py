from historial import Historial

class Deposito:
    """
    Invariante: saldo >= 0
    """

    __ERROR_NEGATIVO = 'El saldo no puede ser negativo'

    def __init__(self, saldo):
        assert saldo >= 0, Deposito.__ERROR_NEGATIVO
        self.__saldo = saldo
        self.__historial = Historial()
        self.__historial.anyadir_historial('inicial', saldo)
        assert self.saldo_actual() == saldo

    def saldo_actual(self):
        return self.__saldo

    def ingresar(self, cantidad):
        assert self.saldo_actual() >= -cantidad, Deposito.__ERROR_NEGATIVO
        saldo_anterior = self.saldo_actual()
        self.__saldo += cantidad
        self.__historial.anyadir_historial('ingresar', cantidad)
        assert saldo_anterior + cantidad == self.saldo_actual()

    def retirar(self, cantidad):
        assert self.saldo_actual() >= cantidad, 'Fondos insuficientes'
        saldo_anterior = self.saldo_actual()
        self.__saldo -= cantidad
        self.__historial.anyadir_historial('retirar', cantidad)
        assert saldo_anterior - cantidad == self.saldo_actual()

    def historial(self, pos):
        return self.__historial.elemento_iesimo(pos)

    def longitud_historial(self):
        return self.__historial.longitud()
