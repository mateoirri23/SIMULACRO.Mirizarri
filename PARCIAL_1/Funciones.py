
def cargar_pacientes(lista_pacientes):
    cantidad_pacientes = int(input("Ingrese la cantidad de pacientes ingresados: ")) 

    for i in range(cantidad_pacientes): 
        numero_historia_clinica = int(input("Ingrese el número de historia clínica del paciente: "))
        nombre_del_paciente = input("Ingrese el nombre del paciente: ") 
        edad_paciente = int(input("Ingrese la edad del paciente: ")) 
        diagnostico = str(input("Ingrese el diagnostico del paciente: ")) 
        cant_dias_hospitalizado = int(input("Ingrese la cantidad de días hospitalizado: "))

        pacientes = [numero_historia_clinica, nombre_del_paciente, edad_paciente, diagnostico, cant_dias_hospitalizado]
        # Aquí se crea una lista con los datos del paciente
        # y se agrega al inventario
        lista_pacientes += [pacientes] 
        print("Paciente cargado correctamente.") 

    return pacientes


def imprimir_pacientes(lista_pacientes):
    print("\nLista de pacientes:")
    for paciente in lista_pacientes:
        print("Numero historial clinica:", paciente[0])
        print("Nombre paciente:", paciente[1])
        print("Edad paciente:", paciente[2])
        print("Diagnóstico:", paciente[3])
        print("Cantidad de días hospitalizado:", paciente[4])
        print("-" * 20)  # separador entre pacientes


def buscar_paciente(lista_pacientes):
    historia = input("Ingrese el número de historia clínica (DNI) a buscar: ")

    encontrado = False
    for paciente in lista_pacientes:
        if paciente[0] == historia:
            print("\nPaciente encontrado:")
            print("Numero historial clinico:", paciente[0])
            print("Nombre paciente:", paciente[1])
            print("Edad:", paciente[2])
            print("Diagnostico:", paciente[3])
            print("Cantidad de días hospitalizado:", paciente[4])
            encontrado = True
            break

    if encontrado == False:
        print("❌ Paciente no encontrado.")


def ordenar_forma_ascendente(lista_pacientes):
    
    longitud = len(lista_pacientes)

    for i in range(longitud):
        for j in range(longitud-1-i):
            if lista_pacientes[j][0] > lista_pacientes[j + 1][0]:   
                aux = lista_pacientes[j + 1 ]
                lista_pacientes[j + 1] = lista_pacientes[j]
                lista_pacientes[j] = aux

    print("Lista ordenada de forma ascendente:", lista_pacientes)


def paciente_mas_dias(lista_pacientes):
    """
    Determina e imprime el paciente con mayor cantidad de días de internación.

    La función ordena la lista de pacientes de forma descendente según la cantidad de días
    internados (usando el algoritmo de Bubble Sort) y luego imprime los datos completos del
    paciente con más días. Si la lista está vacía, muestra un mensaje informativo.
    
    Salida:
    -------
    Imprime por pantalla los datos del paciente con más días de internación. En caso de que
    la lista esté vacía, muestra un mensaje indicando que no hay pacientes cargados.
.
    """


    longitud = len(lista_pacientes)

    for i in range(longitud):
        for j in range(longitud-1-i):
            if lista_pacientes[j][4] < lista_pacientes[j + 1][4]:   
                aux = lista_pacientes[j + 1 ]
                lista_pacientes[j + 1] = lista_pacientes[j]
                lista_pacientes[j] = aux

    print("Paciente con mas dias de internacion :", lista_pacientes)

def paciente_menos_dias(lista_pacientes):
    longitud = len(lista_pacientes)

    for i in range(longitud):
        for j in range(longitud-1-i):
            if lista_pacientes[j][4] > lista_pacientes[j + 1][4]:   
                aux = lista_pacientes[j + 1 ]
                lista_pacientes[j + 1] = lista_pacientes[j]
                lista_pacientes[j] = aux

    print("Paciente con menos dias de internacion :", lista_pacientes)


def contar_pacientes_mas_5_dias(lista_pacientes):
    """
    Muestra todos los datos de los pacientes que estuvieron internados al menos 5 días.

    Parámetros:
    -----------
    lista_pacientes : list
        Lista de pacientes. Cada paciente es una sublista con la siguiente estructura:
        [nombre (str), edad (int), dni (str), diagnóstico (str), días_internado (int)]

    Salida:
    -------
    Imprime todos los datos de cada paciente cuya cantidad de días de internación
    es igual o superior a 5. Si ninguno cumple la condición, se muestra un mensaje informativo.
    """

    if len(lista_pacientes) == 0:
        print("No hay pacientes cargados.")
        return

    encontrados = False
    print("\nPacientes con 5 o más días de internación:")

    for paciente in lista_pacientes:
        if paciente[4] >= 5:
            print("------------------------------")
            print("\nPaciente encontrado:")
            print("Numero historial clinico:", paciente[0])
            print("Nombre paciente:", paciente[1])
            print("Edad:", paciente[2])
            print("Diagnostico:", paciente[3])
            print("Cantidad de días hospitalizado:", paciente[4])
            encontrados = True

    if not encontrados:
        print("Ningún paciente estuvo internado 5 días o más.")


def promedio_dias_internacion(lista_pacientes):
    """
    Calcula e imprime el promedio de días de internación de todos los pacientes.

    Parámetros:
    -----------
    lista_pacientes : list
        Lista de pacientes. Cada paciente es una sublista con la siguiente estructura:
        [nombre (str), edad (int), dni (str), diagnóstico (str), días_internado (int)]

    Salida:
    -------
    Imprime el promedio de días de internación de todos los pacientes.
    Si la lista está vacía, muestra un mensaje informativo.
    """

    if len(lista_pacientes) == 0:
        print("No hay pacientes cargados.")
        return

    total_dias = 0
    for paciente in lista_pacientes:
        total_dias += paciente[4]  # días de internación

    promedio = total_dias / len(lista_pacientes)

    print(f"\nPromedio de días de internación: {promedio}")