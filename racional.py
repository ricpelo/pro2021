from math import gcd

class Racional:
    def __init__(self, num, den):
        """
        Constructor que crea un racional a partir de un numerador y
        un denominador.
        """
        Racional.__simp = False
        self.set_numer(num)
        self.set_denom(den)
        Racional.__simp = True
        self.__simplificar()

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numer() * otro.denom() == self.denom() * otro.numer()

    def __str__(self):
        return str(self.numer()) + ' / ' + str(self.denom())

    def __repr__(self):
        num = self.numer()
        den = self.denom()
        return f'Racional({num}, {den})'

    def numer(self):
        """Accesor (getter) que devuelve el numerador del racional."""
        return self.__num

    def denom(self):
        """Accesor que devuelve el denominador del racional."""
        return self.__den

    def set_numer(self, num):
        """Mutador (setter) que asigna el numerador del racional."""
        self.__num = num
        if Racional.__simp:
            self.__simplificar()

    def set_denom(self, den):
        """Mutador que asigna el denominador del racional."""
        self.__den = den
        if Racional.__simp:
            self.__simplificar()

    def __simplificar(self):
        g = gcd(self.numer(), self.denom())
        self.__num = self.numer() // g
        self.__den = self.denom() // g
