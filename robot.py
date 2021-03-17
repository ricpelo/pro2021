"""
- Crear robots con una serie de características.
- Cada robot está identificado por un número único, comenzando por el 1,
  y no puede variar.
- Cada robot tiene un alias.
- Cada robot pertenece a una generación ('A', 'B', 'M').
- Un robot puede girar sobre sí mismo apuntando hacia uno de los 4 puntos
  cardinales, en el sentido de las agujas del reloj ('N', 'E', 'S', 'O').
- Por defecto un robot apunta a una dirección aleatoria.
- Un robot puede avanzar en la dirección del punto cardinal en metros
  comenzando por el 1.
- Todo robot nace con un alias no vacío y no cambia nunca a lo largo de
  su vida.
- Un robot puede saludar indicando su nombre completo
  (código del robot + " " + (alias).
- El código de un robot es la generación concatenado con el número
  (P.e. M1)
- Cuando se muestre la información de un robot por pantalla aparecerá
  su nombre, su orientación, la distancia total recorrida en su vida y
  su posicion.
- El robot contabilizará la distancia total recorrida en su vida.
- El robot es capaz de ejecutar los siguientes comandos: GIRAR, AVANZAR,
  SALUDAR.
"""
class Posicion:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.x() == otro.x() and self.y() == otro.y()

    def __repr__(self):
        return f'Posicion({self.x()}, {self.y()})'

    def x(self):
        return self.__x

    def y(self):
        return self.__y

from brujula import Brujula

class Robot:
    __ultimo_numero = 0

    def __init__(self, alias, generacion, posicion=Posicion(0, 0)):
        Robot.__ultimo_numero += 1
        self.__numero = Robot.__ultimo_numero
        self.set_alias(alias)
        self.set_generacion(generacion)
        self.__brujula = Brujula()
        self.__orientacion = self.__brujula.punto_aleatorio()
        self.__distancia = 0
        self.__posicion = posicion

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.numero() == otro.numero()

    def __str__(self):
        ret = 'Nombre: ' + self.alias() + '\n' \
            + 'Orientado hacia el: ' + self.orientacion() + '\n' \
            + 'Distancia recorrida: ' + self.distancia() + '\n'

    def posicion(self):
        return self.__posicion

    def numero(self):
        return self.__numero

    def alias(self):
        return self.__alias

    def set_alias(self, alias):
        if not isinstance(alias, str):
            raise TypeError('El alias no es una cadena')
        if alias == '':
            raise ValueError('El alias no puede ser vacío')
        self.__alias = alias

    def orientacion(self):
        return self.__orientacion


    def generacion(self):
        return self.__generacion

    def set_generacion(self, generacion):
        if not Robot.es_generacion_valida(generacion):
            raise ValueError('La generación no es válida')
        self.__generacion = generacion

    def distancia(self):
        return self.__distancia

    def avanzar(self, metros=1):
        self.__posicion = Posicion()
        self.__distancia += abs(metros)

    def codigo(self):
        return self.generacion() + str(self.numero())

    def saludar(self):
        return self.codigo() + ' ' + self.alias()

    @staticmethod
    def es_generacion_valida(generacion):
        return generacion in ('A', 'B', 'M')
