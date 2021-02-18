from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    @abstractmethod
    def dibujar(self):
        ...

class Triangulo(Figura):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.__base = base
        self.__altura = altura

    def base(self):
        return self.__base

    def altura(self):
        return self.__altura

    def dibujar(self):
        print('Dibujo el triángulo')

class Circulo(Figura):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.__radio = radio

    def radio(self):
        return self.__radio

    def dibujar(self):
        print('Dibujo el círculo')

t = Triangulo(320, 200, 400, 20)
c = Circulo(800, 600, 80)
