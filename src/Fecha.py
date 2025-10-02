from datetime import date

class Fecha:
    def __init__(self, dia, mes, anio):
        if isinstance(dia, int) and isinstance(mes, int) and isinstance(anio, int):
            if 0 < dia <= 31 and 0 < mes <= 12 and 1900 <= anio <= 2100:
                self.__dia = dia
                self.__mes = mes
                self.__anio = anio
                self.fecha = date(anio, mes, dia)
            else:
                raise ValueError("El día debe estar entre 1 - 31, el mes entre 1 - 12 y el año entre 1900 - 2100.")
        else:
            raise TypeError("Día, Mes y Año deben ser del tipo int.")

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__anio}'

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_anio(self):
        return self.__anio