from random import choice

class Ficha:
    BLANCA = 'B'
    NEGRA = 'N'

    def __init__(self, color):
        self.__set_color(color)

    def __repr__(self):
        return f'Ficha({self.color()})'

    def __set_color(self, color):
        if color not in ['B', 'N']:
            raise ValueError('La ficha debe ser blanca o negra.')
        self.__color = color

    def color(self):
        return self.__color

class Tablero:
    DER = 'DER'
    IZQ = 'IZQ'

    def __init__(self, blanco, negro):
        self.__blanco = blanco
        self.__negro = negro
        self.__fichas = {}
        self.__turno = blanco
        self.__ganador = None
        off = 0
        for fila in range(1, 4):
            for col in range(1 + off, 8 + off, 2):
                ficha = Ficha(Ficha.BLANCA)
                self.__fichas[(fila, col)] = ficha
                self.__blanco.fichas().append(ficha)
            off = 1 if off == 0 else 0
        off = 1
        for fila in range(6, 9):
            for col in range(1 + off, 8 + off, 2):
                ficha = Ficha(Ficha.NEGRA)
                self.__fichas[(fila, col)] = ficha
                self.__negro.fichas().append(ficha)
            off = 1 if off == 0 else 0

    def ficha(self, fila, columna):
        return self.__fichas.get((fila, columna))

    def mover(self, ficha, direccion):
        pos = None
        for k, v in self.__fichas.items():
            if ficha == v:
                pos = k
                break
        if pos is None:
            raise ValueError('La ficha no está en el tablero')
        fila, col = pos
        try:
            nueva_fila, nueva_col = Tablero.__nueva_posicion(fila, col, ficha.color(), direccion)
        except ValueError:
            return (fila, col)
        ficha_bloq = self.ficha(nueva_fila, nueva_col)
        if ficha_bloq is None:
            self.__mover_ficha(ficha, (fila, col), (nueva_fila, nueva_col))
            return (nueva_fila, nueva_col)
        else:
            if ficha_bloq.color() == ficha.color():
                return (fila, col)
            else:
                try:
                    fila_bloq, col_bloq = nueva_fila, nueva_col
                    nueva_fila, nueva_col = Tablero.__nueva_posicion(nueva_fila, nueva_col, ficha.color(), direccion)
                except ValueError:
                    return (fila, col)
                if self.ficha(nueva_fila, nueva_col) is None:
                    self.__sacar_ficha(fila_bloq, col_bloq)
                    self.__mover_ficha(ficha, (fila, col), (nueva_fila, nueva_col))
                    return (nueva_fila, nueva_col)
                else:
                    return (fila, col)

    def __sacar_ficha(self, fila, col):
        ficha = self.__fichas[(fila, col)]
        del self.__fichas[(fila, col)]
        if ficha.color() == Ficha.BLANCA:
            self.__blanco.remove(ficha)
        elif ficha.color() == Ficha.NEGRA:
            self.__negro.remove(ficha)

    def __mover_ficha(self, ficha, pos_ini, pos_fin):
        fila, col = pos_ini
        nueva_fila, nueva_col = pos_fin
        del self.__fichas[(fila, col)]
        self.__fichas[(nueva_fila, nueva_col)] = ficha

    @staticmethod
    def __nueva_posicion(fila, col, color, direccion):
        if color == Ficha.BLANCA:
            nueva_col = col - 1 if direccion == Tablero.IZQ else col + 1
            if fila == 8 or nueva_col in [0, 9]:
                raise ValueError()
            nueva_fila = fila + 1
        elif color == Ficha.NEGRA:
            nueva_col = col + 1 if direccion == Tablero.IZQ else col - 1
            if fila == 1 or nueva_col in [0, 9]:
                raise ValueError()
            nueva_fila = fila - 1
        return (nueva_fila, nueva_col)

    def diccionario(self):
        return self.__fichas

    def fichas(self):
        return list(self.__fichas.values())

    def siguiente_turno(self):
        otro = self.__blanco if self.__turno == self.__negro \
                             else self.__negro
        if not self.__turno.siguiente_movimiento():
            print(f'El jugador {self.__turno.nombre()} ha perdido')
            self.__ganador = otro
            return
        self.__turno = otro

    def quien_gana(self):
        return self.__ganador

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__fichas = []

    def fichas(self):
        return self.__fichas

    def siguiente_movimiento(self):
        pass
