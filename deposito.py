from historial import Historial

class Deposito:
    """
    Invariante: saldo >= 0
    """

    __ERROR_NEGATIVO = 'El saldo no puede ser negativo'

    def __init__(self, saldo, historial=None):
        assert saldo >= 0, Deposito.__ERROR_NEGATIVO
        self.__saldo = saldo
        if historial is None:
            self.__historial = Historial()
            self.__historial.anyadir_historial('inicial', saldo)
        else:
            self.__historial = historial
        assert self.saldo_actual() == saldo

    def __repr__(self):
        saldo = self.saldo_actual()
        historial = repr(self.__historial)
        return f'Deposito({saldo}, {historial})'

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        if self.longitud_historial() != otro.longitud_historial():
            return False
        for i in range(self.longitud_historial()):
            if self.historial(i) != otro.historial(i):
                return False
        return self.saldo_actual() == otro.saldo_actual()

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
