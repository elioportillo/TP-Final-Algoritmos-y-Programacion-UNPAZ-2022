ALUMNOS = []
MATERIAS = []
INSCRIPCIONES = []


def buscar_alumno_por_codigo_identificador(codigo_identificador):
    """
    Búsqueda binaria
        Precondición: lista de alumnos ordenada por código identificador
        Devuelve None si no existe un alumno con ese codigo_identificador.
        Devuelve la instancia del alumno cuyo codigo_identificador coincida.
    """
    izq = 0  # izq guarda el índice inicio del segmento
    der = len(ALUMNOS) - 1  # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = round((izq + der) / 2)  # el punto medio del segmento
        if ALUMNOS[medio].get_cod_identificador_alum() == codigo_identificador:
            # si el codigo_identificador del alumno en la posición medio es igual al valor buscado,
            # devuelve el objeto alumno en la posición medio.
            return ALUMNOS[medio]
        elif ALUMNOS[medio].get_cod_identificador_alum() > codigo_identificador:
            der = medio - 1
        else:
            izq = medio + 1
    return None


def buscar_materia_por_codigo_identificador(codigo_identificador):

    izq = 0  # izq guarda el índice inicio del segmento
    der = len(MATERIAS) - 1  # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = round((izq + der) / 2)  # el punto medio del segmento
        if MATERIAS[medio].get_cod_identificador_mat() == codigo_identificador:
            # si el codigo_identificador de la materia en la posición medio es igual al valor buscado,
            # devuelve el objeto alumno en la posición medio.
            return MATERIAS[medio]
        elif MATERIAS[medio].get_cod_identificador_mat() > codigo_identificador:
            der = medio - 1
        else:
            izq = medio + 1
    return None
