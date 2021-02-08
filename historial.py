class Historial:
    def __init__(self):
        self.__historial = []

    def anyadir_historial(self, op, cantidad):
        if self.__historial == []:
            saldo = 0
        else:
            saldo = self.__historial[-1]['saldo']
        self.__historial.append({'op': op,
                                 'cantidad': cantidad,
                                 'saldo': saldo})

    def elemento_iesimo(self, i):
        if i < len(self.__historial):
            return self.__historial[i]
        return None

    def longitud(self):
        return len(self.__historial)
