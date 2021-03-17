import random

class Brujula:
    def __init__(self, puntos=None):
        if puntos is not None:
            if len(puntos) == 0:
                raise ValueError('Debe haber al menos un punto cardinal')
            self.__puntos = puntos
        else:
            self.__puntos = ('N', 'E', 'S', 'O')

    def __comprobar_punto_cardinal(self, punto):
        if not self.es_punto_cardinal(punto):
            raise ValueError('No es un punto cardinal')

    def punto_aleatorio(self):
        return random.choice(self.__puntos)

    def es_punto_cardinal(self, punto):
        return punto in self.__puntos

    def derecha(self, punto):
        """
        Devuelve el punto cardinal que está a la derecha de uno dado.
        - Pre: self.es_punto_cardinal(punto) == True
        - Args:
          punto: un punto cardinal.
        - Devuelve:
          El punto cardinal que está a la derecha del indicado.
        - Lanza:
          ValueError si el argumento recibido no es un punto cardinal válido.
        """
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) + 1
        return self.__puntos[pos % len(self.__puntos)]

    def izquierda(self, punto):
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) - 1
        return self.__puntos[pos]
