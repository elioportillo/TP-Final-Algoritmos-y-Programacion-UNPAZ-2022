class Materia:
    def __init__(self, codigo_identificador, nombre, correlativas):
        self.__codigo_identificador = codigo_identificador
        self.__nombre = nombre
        self.__correlativas = correlativas

    def __str__(self):
        return f"Código: {self.__codigo_identificador}    | Nombre: {self.__nombre}     | Correlativas: {self.__correlativas}"

    def get_cod_identificador_mat(self):
        return self.__codigo_identificador

    def get_correlativas(self):
        return self.__correlativas

    def modificar_nombre(self, nombre):
        self.__nombre = nombre

    def modificar_correlativas(self, correlativas):
        self.__correlativas = correlativas

    def get_nombre_materia(self):
        return self.__nombre