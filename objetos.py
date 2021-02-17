class Trabajador:
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def imprimir_trabajador(self):
        print(f'Soy un trabajador y me llamo {self.get_nombre()}')

juan = Trabajador()
juan.set_nombre('Juan')
pepe = Trabajador()
pepe.set_nombre('Pepe')
juan.imprimir_trabajador()
pepe.imprimir_trabajador()

class Docente(Trabajador):
    def set_nrp(self, nrp):
        self.__nrp = nrp

    def get_nrp(self):
        return self.__nrp

    def imprimir_docente(self):
        print(f'Soy un docente que se llama {self.get_nombre()} y tiene NRP {self.get_nrp()}')

africa = Docente()
africa.set_nombre('África')
africa.set_nrp(123123)
africa.imprimir_docente()

class Investigador(Docente):
    def set_proyecto(self, proyecto):
        self.__proyecto = proyecto

    def get_proyecto(self):
        return self.__proyecto

    def imprimir_investigador(self):
        print(f'Soy un investigador llamado {self.get_nombre()}')
        print(f'Mi NRP es {self.get_nrp()} y mi proyecto es {self.get_proyecto()}')

antonio = Investigador()
antonio.set_nombre('Antonio')
antonio.set_nrp(222222)
antonio.set_proyecto('Innovación educativa')
antonio.imprimir_investigador()

print(isinstance(africa, Investigador))
