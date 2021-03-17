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











class Terrestre(ABC):
    def __init__(self, numero_ruedas):
        self.__numero_ruedas = numero_ruedas

    def numero_ruedas(self):
        return self.__numero_ruedas

    def set_numero_ruedas(self, numero_ruedas):
        self.__numero_ruedas = numero_ruedas

    @abstractmethod
    def mover(self):
        ...

class Coche(Terrestre):
    def __init__(self, numero_puertas):
        super().__init__(4)
        self.__numero_puertas = numero_puertas

    def numero_puertas(self):
        return self.__numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self.__numero_puertas = numero_puertas

    def mover(self):
        print("Brrrrrrrrrrrrmmmmm")

class Moto(Terrestre):
    def __init__(self):
        super().__init__(2)

    def mover(self):
        print('Ñiaaaaaaooooooooooo')

def mover_3_km(t):
    t.mover()
    t.mover()
    t.mover()
