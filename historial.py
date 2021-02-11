class Historial:
    def __init__(self, historial=None):
        if historial is None:
            self.__historial = []
        else:
            self.__historial = historial

    def __repr__(self):
        historial = repr(self.__historial)
        return f'Historial({historial})'

    def anyadir_historial(self, op, cantidad):
        if self.__historial == []:
            saldo = cantidad
        else:
            saldo = self.__historial[-1]['saldo']
            if op == 'retirar':
                saldo -= cantidad
            else:
                saldo += cantidad

        self.__historial.append({'op': op,
                                 'cantidad': cantidad,
                                 'saldo': saldo})

    def elemento_iesimo(self, i):
        if i < len(self.__historial):
            return self.__historial[i]
        return None

    def longitud(self):
        return len(self.__historial)
