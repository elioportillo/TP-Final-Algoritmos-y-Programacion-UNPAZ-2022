class Alumno:
    def __init__(self,codigo_identificador, nombre, apellido, genero):
        self.__codigo_identificador = codigo_identificador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero

    def __str__(self):
        return f"Código: {self.__codigo_identificador}    | Nombre: {self.__nombre}     |   Apellido: {self.__apellido}   | Género: {self.__genero}"

    def get_cod_identificador_alum(self):
        return self.__codigo_identificador

    def modificar_nombre(self, nombre):
        self.__nombre = nombre

    def modificar_apellido(self, apellido):
        self.__apellido = apellido

    def modificar_genero(self, genero):
        self.__genero = genero

    def get_nombre_alumno(self):
        return self.__nombre

    def get_apellido_alumno(self):
        return self.__apellido
