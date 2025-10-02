from globales import buscar_alumno_por_codigo_identificador
from globales import buscar_materia_por_codigo_identificador


class Inscripcion:

    def __init__(self, p_id_alumno, p_id_materia, p_fecha_desde, p_fecha_hasta, p_aprobada):
        self.id_alumno = p_id_alumno
        self.id_materia = p_id_materia
        # p_fecha_desde debe ser un objeto de la clase Fecha
        self.fecha_desde = p_fecha_desde
        # p_fecha_hasta debe ser un objeto de la clase Fecha
        self.fecha_hasta = p_fecha_hasta
        self.aprobada = p_aprobada

    def __str__(self):
        alumno = buscar_alumno_por_codigo_identificador(self.id_alumno)
        materia = buscar_materia_por_codigo_identificador(self.id_materia)
        return f"Inscripción de alumno ({alumno}) en materia ({materia}) desde {self.fecha_desde} hasta {self.fecha_hasta}. Aprobado: {'Sí' if self.aprobada else 'No'}"

    def modificar_id_alumno(self, nueva_id_alumno):
        self.id_alumno = nueva_id_alumno

    def modificar_id_mat(self, nueva_id_materia):
        self.id_materia = nueva_id_materia

    def modificar_fecha_desde(self, nueva_fecha_desde):
        self.fecha_desde = nueva_fecha_desde

    def modificar_fecha_hasta(self, nueva_fecha_hasta):
        self.fecha_hasta = nueva_fecha_hasta

    def modificar_condicion(self, nueva_condicion):
        self.aprobada = nueva_condicion

    def get_id_alum(self):
        return self.id_alumno

    def get_id_mat(self):
        return self.id_materia

    def get_condicion(self):
        return self.aprobada