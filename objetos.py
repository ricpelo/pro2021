class Trabajador:
    def __init__(self, nombre):
        self.__nombre = nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def imprimir(self):
        print(f'Me llamo {self.get_nombre()}')

juan = Trabajador('Juan')
pepe = Trabajador('Pepe')

class Docente(Trabajador):
    def __init__(self, nombre, nrp):
        super().__init__(nombre)
        self.__nrp = nrp

    def set_nrp(self, nrp):
        self.__nrp = nrp

    def get_nrp(self):
        return self.__nrp

    def imprimir(self):
        super().imprimir()
        print(f'Tengo el NRP {self.get_nrp()}')

africa = Docente('África', 123123)

class Investigador(Docente):
    def __init__(self, nombre, nrp, proyecto):
        super().__init__(nombre, nrp)
        self.__proyecto = proyecto

    def set_proyecto(self, proyecto):
        self.__proyecto = proyecto

    def get_proyecto(self):
        return self.__proyecto

    def imprimir(self):
        super().imprimir()
        print(f'Mi proyecto es {self.get_proyecto()}')

antonio = Investigador('Antonio', 222222, 'Innovación educativa')
antonio.imprimir()
