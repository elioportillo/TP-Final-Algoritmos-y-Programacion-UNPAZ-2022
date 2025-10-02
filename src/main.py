import pickle
from globales import ALUMNOS, MATERIAS, INSCRIPCIONES, buscar_alumno_por_codigo_identificador, buscar_materia_por_codigo_identificador
from Inscripcion import Inscripcion
from Fecha import Fecha
from Materia import Materia
from Alumno import Alumno
from os import path


opcion = 0
opcion_menu_alumnos = 0
opcion_menu_materias = 0
opcion_menu_inscripciones = 0
salir = False
salir_menu_alumnos = False
salir_menu_materias = False
salir_menu_inscripciones = False

ALUMNOS_CSV_FILENAME = "alumnos.tsv"
MATERIAS_CSV_FILENAME = "materias.tsv"
INSCRIPCIONES_CSV_FILENAME = "inscripciones.tsv"

ALUMNOS_BIN_FILENAME = "alumnos.bin"
MATERIAS_BIN_FILENAME = "materias.bin"
INSCRIPCIONES_BIN_FILENAME = "inscripciones.bin"

FECHAS = []



#agrego una funcion para escribir alumnos en archivo binario
def escribir_binario_alumnos():
    with open(ALUMNOS_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(ALUMNOS, archivo_binario)

#agrego una funcion para escribir materias en archivo binario
def escribir_binario_materias():
    with open(MATERIAS_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(MATERIAS, archivo_binario)

def escribir_binario_inscripciones():
    with open(INSCRIPCIONES_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(INSCRIPCIONES, archivo_binario)

def cargar_desde_binario_alumnos():
    if path.exists(ALUMNOS_BIN_FILENAME) and path.isfile(ALUMNOS_BIN_FILENAME):
        with open(ALUMNOS_BIN_FILENAME, 'rb') as archivo_binario:
            alumnos = pickle.load(archivo_binario)
            ALUMNOS.extend(alumnos)

def cargar_desde_binario_materias():
    if path.exists(MATERIAS_BIN_FILENAME) and path.isfile(MATERIAS_BIN_FILENAME):
        with open(MATERIAS_BIN_FILENAME, 'rb') as archivo_binario:
            materias = pickle.load(archivo_binario)
            MATERIAS.extend(materias)

def cargar_desde_binario_inscripciones():
    if path.exists(INSCRIPCIONES_BIN_FILENAME) and path.isfile(INSCRIPCIONES_BIN_FILENAME):
        with open(INSCRIPCIONES_BIN_FILENAME, 'rb') as archivo_binario:
            inscripciones = pickle.load(archivo_binario)
            INSCRIPCIONES.extend(inscripciones)

def comparar_fechas(fecha_desde, fecha_hasta):
    if fecha_desde.get_anio() > fecha_hasta.get_anio():
        print('La fecha en la que inicia no puede ser mayor a cuando finaliza.')
        return True
    if fecha_desde.get_anio() == fecha_hasta.get_anio() and fecha_desde.get_mes() > fecha_hasta.get_mes():
        print('La fecha en la que inicia no puede ser mayor a cuando finaliza.')
        return True
    if fecha_desde.get_anio() == fecha_hasta.get_anio() and fecha_desde.get_mes() == fecha_hasta.get_mes() and fecha_desde.get_dia() > fecha_hasta.get_dia():
        print('La fecha en la que inicia no puede ser mayor a cuando finaliza.')
        return True

def inicializar_alumnos():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(ALUMNOS_CSV_FILENAME) and path.isfile(ALUMNOS_CSV_FILENAME):
        with open(ALUMNOS_CSV_FILENAME, encoding='utf-8') as archivo_alum_tsv:
            archivo_cargado = archivo_alum_tsv.readlines()
            for linea in archivo_cargado[1:]:
                datos = linea.split('\t')
                codigo_identificador = int(datos[0])
                nombre = datos[1]
                apellido = datos[2]
                genero = datos[3]
                alum = Alumno(codigo_identificador, nombre, apellido, genero)
                ALUMNOS.append(alum)
        escribir_binario_alumnos()




def inicializar_materias():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(MATERIAS_CSV_FILENAME) and path.isfile(MATERIAS_CSV_FILENAME):
        with open(MATERIAS_CSV_FILENAME, encoding='utf-8') as archivo_alum_tsv:
            archivo_cargado = archivo_alum_tsv.readlines()
            for linea in archivo_cargado[1:]:
                datos = linea.split('\t')
                codigo_identificador = int(datos[0])
                nombre = datos[1]
                correlativas_str = datos[2]
                correlativas_int = [int(correlativa) for correlativa in correlativas_str.split(',') if correlativa.strip()]
                mat = Materia(codigo_identificador, nombre, correlativas_int)
                MATERIAS.append(mat)
        escribir_binario_materias()


def inicializar_inscripciones():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(INSCRIPCIONES_CSV_FILENAME) and path.isfile(INSCRIPCIONES_CSV_FILENAME):
        with open(INSCRIPCIONES_CSV_FILENAME, encoding='utf-8') as archivo_tsv:
            todas_las_lineas = archivo_tsv.readlines()
            for linea in todas_las_lineas[1:]:
                columnas = linea.split('\t')
                columnas = [valor.strip() for valor in columnas]
                id_alumno = int(columnas[0])
                id_materia = int(columnas[1])
                fecha_desde_separado = columnas[2].split('/')
                fecha_desde = Fecha(int(fecha_desde_separado[0]), int(fecha_desde_separado[1]),
                                    int(fecha_desde_separado[2]))
                fecha_hasta_separado = columnas[3].split('/')
                fecha_hasta = Fecha(int(fecha_hasta_separado[0]), int(fecha_hasta_separado[1]),
                                    int(fecha_hasta_separado[2]))
                if not comparar_fechas(fecha_desde, fecha_hasta):
                    aprobado = True if columnas[4].upper() == 'TRUE' else False
                    inscripcion = Inscripcion(id_alumno, id_materia, fecha_desde, fecha_hasta, aprobado)
                    INSCRIPCIONES.append(inscripcion)
                else:
                    print(f'Error de carga del alumno COD: {id_alumno} en la materia COD: {id_materia}.')

        escribir_binario_inscripciones()


def ordenar_alumnos(ALUMNOS, inicio, fin):
    if inicio >= fin:
        return
    anterior = inicio
    posterior = fin
    pivot = ALUMNOS[inicio]
    while anterior < posterior:
        while anterior < posterior and ALUMNOS[posterior].get_cod_identificador_alum() > pivot.get_cod_identificador_alum():
            posterior = posterior - 1
        if anterior < posterior:
            ALUMNOS[anterior] = ALUMNOS[posterior]
            anterior = anterior + 1
        while anterior < posterior and ALUMNOS[anterior].get_cod_identificador_alum() <= pivot.get_cod_identificador_alum():
            anterior = anterior + 1
        if anterior < posterior:
            ALUMNOS[posterior] = ALUMNOS[anterior]
            posterior = posterior - 1
    ALUMNOS[anterior] = pivot
    ordenar_alumnos(ALUMNOS, inicio, anterior - 1)
    ordenar_alumnos(ALUMNOS, anterior + 1, fin)

def ordenar_materias(MATERIAS, inicio, fin):
    if inicio >= fin:
        return
    anterior = inicio
    posterior = fin
    pivot = MATERIAS[inicio]
    while anterior < posterior:
        while anterior < posterior and MATERIAS[posterior].get_cod_identificador_mat() > pivot.get_cod_identificador_mat():
            posterior = posterior - 1
        if anterior < posterior:
            MATERIAS[anterior] = MATERIAS[posterior]
            anterior = anterior + 1
        while anterior < posterior and MATERIAS[anterior].get_cod_identificador_mat() <= pivot.get_cod_identificador_mat():
            anterior = anterior + 1
        if anterior < posterior:
            MATERIAS[posterior] = MATERIAS[anterior]
            posterior = posterior - 1
    MATERIAS[anterior] = pivot
    ordenar_materias(MATERIAS, inicio, anterior - 1)
    ordenar_materias(MATERIAS, anterior + 1, fin)




def mostrar_todo_inscripciones():
    for inscripcion in INSCRIPCIONES:
        print(inscripcion)
        print('\n')

def mostrar_todo_alumnos():
    ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
    for alumno in ALUMNOS:
        print(alumno)


def mostrar_todo_materias():
    ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
    for materia in MATERIAS:
        print(materia)



def inicializar():
    #Dejo comentadas las demás inicializaciones para no tener una doble carga
    #inicializar_alumnos()
    #inicializar_materias()
    #inicializar_inscripciones()
    cargar_desde_binario_alumnos()
    cargar_desde_binario_materias()
    cargar_desde_binario_inscripciones()


def validar_longitud_50(texto):
    if len(texto) > 50:
        return False
    if texto == '':
        print('El dato ingresado no puede estar vacío')
        return False
    return True

def validar_longitud_100(texto):
    if len(texto) > 100:
        return False
    if texto == '':
        print('El dato ingresado no puede estar vacío')
        return False
    return True


def validar_entero_positivo(valor):
    try:
        valor = int(valor)
        if valor <= 0:
            print('Error: el valor debe ser un entero positivo.')
            return False
        return True
    except ValueError:
        print('Error: el valor debe ser un número entero.')
        return False

def validar_entero_positivo_dia(valor):
    try:
        valor = int(valor)
        if valor <= 0 or valor > 31:
            print('Error: el valor debe ser un entero positivo menor o igual a 31.')
            return False
        return True
    except ValueError:
        print('Error: el valor debe ser un número entero.')
        return False

def validar_entero_positivo_mes(valor):
    try:
        valor = int(valor)
        if valor <= 0 or valor > 12:
            print('Error: el valor debe ser un entero positivo menor o igual a 12.')
            return False
        return True
    except ValueError:
        print('Error: el valor debe ser un número entero.')
        return False

def validar_entero_positivo_anio(valor):
    try:
        valor = int(valor)
        if valor <= 2000 or valor >= 2100:
            print('Error: el valor debe encontrarse entre los años 2000 y 2100.')
            return False
        return True
    except ValueError:
        print('Error: el valor debe ser un número entero.')
        return False

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestión de alumnos")
    print("2. Gestión de materias")
    print("3. Gestión de inscripciones")
    print("4. Salir")
    print("\n")

def mostrar_menu_alumnos():
    print("\n--- GESTIÓN DE ALUMNOS ---")
    print("1. Crear nuevo alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Volver al menú principal")

def mostrar_menu_materias():
    print("\n--- GESTIÓN DE MATERIAS ---")
    print("1. Crear nueva materia")
    print("2. Mostrar todas las materias")
    print("3. Actualizar materia")
    print("4. Eliminar materia")
    print("5. Volver al menú principal")

def mostrar_menu_inscripciones():
    print("\n--- GESTIÓN DE INSCRIPCIONES ---")
    print("1. Crear nueva inscripción")
    print("2. Mostrar todas las inscripciones")
    print("3. Actualizar inscripción")
    print("4. Eliminar inscripción")
    print("5. Volver al menú principal")


def opciones_menu_principal():
    global salir
    global salir_menu_alumnos
    global salir_menu_materias
    global salir_menu_inscripciones

    salir_menu_alumnos = False
    salir_menu_materias = False
    salir_menu_inscripciones = False

    validacion_opciones()
    if opcion == 1:
        mostrar_menu_alumnos()
        opciones_menu_alumnos()

    elif opcion == 2:
        mostrar_menu_materias()
        opciones_menu_materias()

    elif opcion == 3:
        mostrar_menu_inscripciones()
        opciones_menu_inscripciones()
    elif opcion == 4:
        salir = True
    else:
        print('Opción inválida')


def opciones_menu_alumnos():
    global salir_menu_alumnos
    while not salir_menu_alumnos:
        validacion_opciones()
        if opcion == 1:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            crear_alumno()
            mostrar_menu_alumnos()


        elif opcion == 2:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            mostrar_todo_alumnos()
            mostrar_menu_alumnos()

        elif opcion == 3:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            editar_alumno()
            mostrar_menu_alumnos()
        elif opcion == 4:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            eliminar_alumno()
            mostrar_menu_alumnos()
        elif opcion == 5:
            salir_menu_alumnos = True
        else:
            print('\n')
            print('Opción inválida')

def opciones_menu_materias():
    global salir_menu_materias
    while not salir_menu_materias:
        validacion_opciones()
        if opcion == 1:
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            crear_materia()
            mostrar_menu_materias()

        elif opcion == 2:
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            mostrar_todo_materias()
            mostrar_menu_materias()

        elif opcion == 3:
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            editar_materia()
            mostrar_menu_materias()
        elif opcion == 4:
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            eliminar_materia()
            mostrar_menu_materias()
        elif opcion == 5:
            salir_menu_materias = True
        else:
            print('\n')
            print('Opción inválida')


def opciones_menu_inscripciones():
    global salir_menu_inscripciones
    while not salir_menu_inscripciones:
        validacion_opciones()
        if opcion == 1:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            crear_inscripciones()
            mostrar_menu_inscripciones()

        elif opcion == 2:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            mostrar_todo_inscripciones()
            mostrar_menu_inscripciones()

        elif opcion == 3:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            editar_inscripciones()
            mostrar_menu_inscripciones()
        elif opcion == 4:
            ordenar_alumnos(ALUMNOS, 0, len(ALUMNOS) - 1)
            ordenar_materias(MATERIAS, 0, len(MATERIAS) - 1)
            eliminar_inscripcion()
            mostrar_menu_inscripciones()
        elif opcion == 5:
            salir_menu_inscripciones = True
        else:
            print('\n')
            print('Opción inválida')



def validacion_opciones():
    global opcion
    opcion = None
    while opcion is None:
        try:
            opcion = int(input('Seleccione una opción: '))
        except ValueError:
            print('\n')
            print('Opción inválida. Ingrese un número entero.')


def validar_correlativas_aprobadas(id_alumno, id_materia):
    materias_aprobadas = []
    correlativas = None

    for inscripcion in INSCRIPCIONES:
        if inscripcion.get_id_alum() == id_alumno and inscripcion.get_condicion() is True:
            materias_aprobadas.append(inscripcion.get_id_mat())

    for materia in MATERIAS:
        if materia.get_cod_identificador_mat() == id_materia:
            correlativas = materia.get_correlativas()


    if correlativas is None or len(correlativas) == 0:
        print('La materia no requiere de correlativas previas')
        return True
    elif all(correlativa in materias_aprobadas for correlativa in correlativas):
        print('Cumple con las correlativas necesarias.')
        return True
    else:
        print('No se cumplen todas las correlativas necesarias.')
        return False


def crear_alumno():
    cod = None
    nombre = None
    apellido = None
    genero = None
    while cod is None:
        aux = input('Ingrese código del alumno: ')
        if validar_entero_positivo(aux):
            cod = int(aux)
            if buscar_alumno_por_codigo_identificador(cod):
                print('Ya existe un alumno con ese código.')
                cod = None
        else:
            print('El código ingresado no es válido.')

    while nombre is None or not validar_longitud_50(nombre):
        nombre = input('Ingrese el nombre del alumno:   ')
        nombre = nombre.capitalize()
        if nombre != '' and not validar_longitud_50(nombre):
            print("El nombre debe tener menos de 50 caracteres.")

    while apellido is None or not validar_longitud_50(apellido):
        apellido = input('Ingrese el apellido del alumno:   ')
        apellido = apellido.capitalize()
        if apellido != '' and not validar_longitud_50(apellido):
            print("El apellido debe tener menos de 50 caracteres.")

    while genero is None:
        genero = input('Ingrese el género del alumno:   ')
        genero = genero.upper()
        if genero == 'M' or genero == 'F' or genero == 'O':
            break
        else:
            print('El género debe ser "M", "F" u "O"')
            genero = None

    alum = Alumno(cod, nombre, apellido, genero)
    ALUMNOS.append(alum)
    escribir_binario_alumnos()
    print('\n')
    print(f'El alumno {nombre} {apellido} fue creado con éxito.')
def crear_materia():

    cod = None
    nombre = None
    correlativas = []
    while cod is None:
        aux = input('Ingrese código de la materia: ')
        if validar_entero_positivo(aux):
            cod = int(aux)
            if buscar_materia_por_codigo_identificador(cod):
                print('Ya existe una materia con ese código.')
                cod = None
        else:
            print('El código ingresado no es válido.')

    while nombre is None or not validar_longitud_100(nombre):
        nombre = input('Ingrese el nombre de la materia:   ')
        nombre = nombre.capitalize()
        if nombre != '' and not validar_longitud_100(nombre):
            print("El nombre debe tener menos de 100 caracteres.")

    while True:
        correlativa = input('Ingrese individualmente los códigos de las materias correlativas (deje en blanco para finalizar): ')
        if correlativa == '':
            break
        elif validar_entero_positivo(correlativa):
            correlativas.append(int(correlativa))

    mat = Materia(cod, nombre, correlativas)
    MATERIAS.append(mat)
    escribir_binario_materias()
    print('\n')
    print(f'La materia {nombre} fue creada con éxito.')


def crear_inscripciones():
    encontrado = False
    cod_alum = input('Ingrese código del alumno: ')
    while not validar_entero_positivo(cod_alum):
        print('El código del alumno debe ser un entero positivo.')
        cod_alum = input('Ingrese código del alumno: ')
    cod_alum = int(cod_alum)
    if not buscar_alumno_por_codigo_identificador(cod_alum):
        print('El código de alumno ingresado no existe.')
        return

    cod_mat = input('Ingrese código de la materia: ')
    while not validar_entero_positivo(cod_mat):
        print('El código de la materia debe ser un entero positivo.')
        cod_mat = input('Ingrese código de la materia: ')
    cod_mat = int(cod_mat)
    if not buscar_materia_por_codigo_identificador(cod_mat):
        print('El código de la materia ingresado no existe.')

        return
    if buscar_materia_por_codigo_identificador(cod_mat) and buscar_alumno_por_codigo_identificador(cod_alum):
        encontrado = True

    if encontrado == True:
        if validar_correlativas_aprobadas(cod_alum, cod_mat):

            fecha_desde = None
            fecha_hasta = None

            while fecha_desde is None or fecha_hasta is None or comparar_fechas(fecha_desde, fecha_hasta):
                dia_desde = input('Ingrese día de inicio: ')
                while not validar_entero_positivo_dia(dia_desde):
                    dia_desde = input('Ingrese día de inicio: ')
                dia_desde = int(dia_desde)

                mes_desde = input('Ingrese mes de inicio: ')
                while not validar_entero_positivo_mes(mes_desde):
                    mes_desde = input('Ingrese mes de inicio: ')
                mes_desde = int(mes_desde)

                anio_desde = input('Ingrese año de inicio: ')
                while not validar_entero_positivo_anio(anio_desde):
                    anio_desde = input('Ingrese año de inicio: ')
                anio_desde = int(anio_desde)

                fecha_desde = Fecha(dia_desde, mes_desde, anio_desde)
                FECHAS.append(fecha_desde)

                dia_hasta = input('Ingrese día de finalización: ')
                while not validar_entero_positivo_dia(dia_hasta):
                    dia_hasta = input('Ingrese día de finalización: ')
                dia_hasta = int(dia_hasta)

                mes_hasta = input('Ingrese mes de finalización: ')
                while not validar_entero_positivo_mes(mes_hasta):
                    mes_hasta = input('Ingrese mes de finalización: ')
                mes_hasta = int(mes_hasta)

                anio_hasta = input('Ingrese año de finalización: ')
                while not validar_entero_positivo_anio(anio_hasta):
                    anio_hasta = input('Ingrese año de finalización: ')
                anio_hasta = int(anio_hasta)

                fecha_hasta = Fecha(dia_hasta, mes_hasta, anio_hasta)

                FECHAS.append(fecha_hasta)

            condicion = None
            while condicion is None:

                condicion = input('Materia aprobada (Si o No): ')
                condicion = condicion.upper()
                if condicion == 'SI':
                    condicion = True
                    break
                elif condicion == 'NO':
                    condicion = False
                    break
                elif condicion != 'SI' and condicion != 'NO':
                    print('La opción ingresada es incorrecta')
                    condicion = None

            insc = Inscripcion(cod_alum, cod_mat, fecha_desde, fecha_hasta, condicion)
            INSCRIPCIONES.append(insc)
            escribir_binario_inscripciones()

            print('\n')
            print('La inscripción fue creada con éxito.')


    else:
        print("No se encontró la inscripción correspondiente al alumno y materia especificados.")

def editar_alumno():

    encontrado = False
    cod = None
    nombre = None
    apellido = None
    genero = None
    while cod is None:
        aux = input('Ingrese código del alumno: ')
        if validar_entero_positivo(aux):
            cod = int(aux)

        else:
            print('El código ingresado no es válido.')
    for alumno in ALUMNOS:
        if alumno.get_cod_identificador_alum() == cod:
            encontrado = True


            while nombre is None or not validar_longitud_50(nombre):
                nombre = input('Ingrese el nuevo nombre del alumno (vacio para mantener el anterior): ')
                nombre = nombre.capitalize()
                if nombre == '':
                    break
                if nombre != '' and not validar_longitud_50(nombre):
                    print("El nombre debe tener menos de 50 caracteres.")

            while apellido is None or not validar_longitud_50(apellido):
                apellido = input('Ingrese el nuevo apellido del alumno (vacio para mantener el anterior): ')
                apellido = apellido.capitalize()
                if apellido == '':
                    break
                if apellido != '' and not validar_longitud_50(apellido):
                    print("El apellido debe tener menos de 50 caracteres.")

            while genero is None:
                genero = input('Ingrese el nuevo género del alumno (vacio para mantener el anterior): ')
                genero = genero.upper()
                if genero == '' or genero == 'M' or genero == 'F' or genero == 'O':
                    break
                else:
                    print('El género debe ser "M", "F" u "O"')
                    genero = None


            if nombre != '':
                alumno.modificar_nombre(nombre)
            if apellido != '':
                alumno.modificar_apellido(apellido)
            if genero != '':
                alumno.modificar_genero(genero)
            print(f"El alumno {alumno} se actualizó correctamente.")
            break

    if not encontrado:
        print("No se encontró el alumno especificado.")
    escribir_binario_alumnos()



def editar_materia():
    encontrado = False
    cod = None
    nombre = None
    correlativas = []

    while cod is None:
        aux = input('Ingrese código de la materia: ')
        if validar_entero_positivo(aux):
            cod = int(aux)
        else:
            print('El código ingresado no es válido.')

    for materia in MATERIAS:
        if materia.get_cod_identificador_mat() == cod:
            encontrado = True

            while nombre is None or not validar_longitud_100(nombre):
                nombre = input('Ingrese el nuevo nombre de la materia (vacio para mantener el anterior): ')
                nombre = nombre.capitalize()
                if nombre == '':
                    break
                if nombre != '' and not validar_longitud_100(nombre):
                    print("El nombre debe tener menos de 100 caracteres.")

            while True:
                correlativa = input('Ingrese individualmente los nuevos códigos de las materias correlativas (deje en blanco para finalizar):  ')
                if correlativa == '':
                    break
                elif validar_entero_positivo(correlativa):
                    correlativas.append(int(correlativa))

            if nombre != '':
                materia.modificar_nombre(nombre)

            materia.modificar_correlativas(correlativas)

            print(f"La materia {materia} se actualizó correctamente.")
            break


    if not encontrado:
        print("No se encontró la materia especificada.")
    escribir_binario_materias()
def editar_inscripciones():
    encontrado = False
    cod_alum = input('Ingrese código del alumno a editar: ')
    while not validar_entero_positivo(cod_alum):
        print('El código del alumno debe ser un entero positivo.')
        cod_alum = input('Ingrese código del alumno a editar: ')
    cod_alum = int(cod_alum)

    cod_mat = input('Ingrese código de la materia a editar: ')
    while not validar_entero_positivo(cod_mat):
        print('El código de la materia debe ser un entero positivo.')
        cod_mat = input('Ingrese código de la materia a editar: ')
    cod_mat = int(cod_mat)

    for inscripcion in INSCRIPCIONES:
        if inscripcion.get_id_alum() == cod_alum and inscripcion.get_id_mat() == cod_mat:
            encontrado = True

            nuevo_cod_alum = input("Ingrese el nuevo código de alumno: ")
            while not validar_entero_positivo(nuevo_cod_alum):
                print('El código del alumno debe ser un entero positivo.')
                nuevo_cod_alum = input('Ingrese el nuevo código de alumno: ')
            nuevo_cod_alum = int(nuevo_cod_alum)
            if not buscar_alumno_por_codigo_identificador(nuevo_cod_alum):
                print('El código de alumno ingresado no existe.')
                return

            nuevo_cod_mat = input('Ingrese el nuevo código de la materia: ')
            while not validar_entero_positivo(nuevo_cod_mat):
                print('El código de la materia debe ser un entero positivo.')
                nuevo_cod_mat = input('Ingrese el nuevo código de la materia: ')
            nuevo_cod_mat = int(nuevo_cod_mat)
            if not buscar_materia_por_codigo_identificador(nuevo_cod_mat):
                print('El código de materia ingresado no existe.')
                return

            if validar_correlativas_aprobadas(nuevo_cod_alum, nuevo_cod_mat):
                nueva_fecha_desde = None
                nueva_fecha_hasta = None

                while nueva_fecha_desde is None or nueva_fecha_hasta is None or comparar_fechas(nueva_fecha_desde, nueva_fecha_hasta):
                    nuevo_dia_desde = input('Ingrese día de inicio: ')
                    while not validar_entero_positivo_dia(nuevo_dia_desde):
                        nuevo_dia_desde = input('Ingrese día de inicio: ')
                    nuevo_dia_desde = int(nuevo_dia_desde)

                    nuevo_mes_desde = input('Ingrese mes de inicio: ')
                    while not validar_entero_positivo_mes(nuevo_mes_desde):
                        nuevo_mes_desde = input('Ingrese mes de inicio: ')
                    nuevo_mes_desde = int(nuevo_mes_desde)

                    nuevo_anio_desde = input('Ingrese año de inicio: ')
                    while not validar_entero_positivo_anio(nuevo_anio_desde):
                        nuevo_anio_desde = input('Ingrese año de inicio: ')
                    nuevo_anio_desde = int(nuevo_anio_desde)
                    nueva_fecha_desde = Fecha(nuevo_dia_desde, nuevo_mes_desde, nuevo_anio_desde)

                    nuevo_dia_hasta = input('Ingrese día de finalización: ')
                    while not validar_entero_positivo_dia(nuevo_dia_hasta):
                        nuevo_dia_hasta = input('Ingrese día de finalización: ')
                    nuevo_dia_hasta = int(nuevo_dia_hasta)

                    nuevo_mes_hasta = input('Ingrese mes de finalización: ')
                    while not validar_entero_positivo_mes(nuevo_mes_hasta):
                        nuevo_mes_hasta = input('Ingrese mes de finalización: ')
                    nuevo_mes_hasta = int(nuevo_mes_hasta)

                    nuevo_anio_hasta = input('Ingrese año de finalización: ')
                    while not validar_entero_positivo_anio(nuevo_anio_hasta):
                        nuevo_anio_hasta = input('Ingrese año de finalización: ')
                    nuevo_anio_hasta = int(nuevo_anio_hasta)
                    nueva_fecha_hasta = Fecha(nuevo_dia_hasta, nuevo_mes_hasta, nuevo_anio_hasta)

                nueva_condicion = None
                while nueva_condicion is None:
                    nueva_condicion = input('Materia aprobada (Si o No, dejar en blanco para no modificar): ')
                    nueva_condicion = nueva_condicion.upper()
                    if nueva_condicion == 'SI':
                        nueva_condicion = True
                        break
                    elif nueva_condicion == 'NO':
                        nueva_condicion = False
                        break
                    elif nueva_condicion != '':
                        print('La opción ingresada es incorrecta')
                        nueva_condicion = None

                if nuevo_cod_alum != '':
                    inscripcion.modificar_id_alumno(int(nuevo_cod_alum))

                if nuevo_cod_mat != '':
                    inscripcion.modificar_id_mat(int(nuevo_cod_mat))

                if nueva_fecha_desde != '':
                    inscripcion.modificar_fecha_desde(nueva_fecha_desde)

                if nueva_fecha_hasta != '':
                    inscripcion.modificar_fecha_hasta(nueva_fecha_hasta)

                if nueva_condicion != '':
                    inscripcion.modificar_condicion(nueva_condicion)

                print(f"Inscripción actualizada: {inscripcion}")
                break

    if not encontrado:
        print("No se encontró la inscripción correspondiente al alumno y materia especificados.")

    escribir_binario_inscripciones()



def eliminar_alumno():
    cod = None
    while cod is None:
        aux = input('Ingrese código del alumno a eliminar: ')
        if validar_entero_positivo(aux):
            cod = int(aux)

        else:
            print('El código ingresado no es válido.')
    alumno_encontrado = buscar_alumno_por_codigo_identificador(cod)
    if alumno_encontrado is not None:
        ALUMNOS.remove(alumno_encontrado)

        print(f"El alumno {alumno_encontrado} ha sido eliminado correctamente.")
    else:
        print("No se encontró ningún alumno con el código especificado.")
    escribir_binario_alumnos()
def eliminar_materia():
    cod = None
    while cod is None:
        aux = input('Ingrese código de la materia a eliminar ')
        if validar_entero_positivo(aux):
            cod = int(aux)

        else:
            print('El código ingresado no es válido.')
    materia_encontrada = buscar_materia_por_codigo_identificador(cod)
    if materia_encontrada is not None:
        MATERIAS.remove(materia_encontrada)

        print(f"La materia {materia_encontrada} ha sido eliminado correctamente.")
    else:
        print("No se encontró ninguna materia con el código especificado.")

    escribir_binario_materias()

def eliminar_inscripcion():
    cod_alum = None
    cod_mat = None

    while cod_alum is None:
        cod_alum = input("Ingrese el código del alumno de la inscripción a eliminar: ")
        if not validar_entero_positivo(cod_alum):
            cod_alum = None
        else:
            cod_alum = int(cod_alum)

    while cod_mat is None:
        cod_mat = input("Ingrese el código de la materia de la inscripción a eliminar: ")
        if not validar_entero_positivo(cod_mat):
            cod_mat = None
        else:
            cod_mat = int(cod_mat)

    inscripcion_encontrada = None
    for inscripcion in INSCRIPCIONES:
        if inscripcion.get_id_alum() == cod_alum and inscripcion.get_id_mat() == cod_mat:
            inscripcion_encontrada = inscripcion
            break

    if inscripcion_encontrada is not None:
        INSCRIPCIONES.remove(inscripcion_encontrada)
        escribir_binario_inscripciones()
        print("La inscripción ha sido eliminada correctamente.")
    else:
        print("No se encontró la inscripción especificada.")




inicializar()
while not salir:

    mostrar_menu()
    opciones_menu_principal()




