class Socio:
    numero = 0

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        Socio.numero += 1

    def dni(self):
        return self.__dni

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.dni() == otro.dni()

    def __hash__(self):
        return hash(self.__dni)
