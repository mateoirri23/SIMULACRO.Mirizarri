from Funciones import (
    cargar_pacientes,
    imprimir_pacientes,
    buscar_paciente,
    ordenar_forma_ascendente, 
    paciente_mas_dias, 
    paciente_menos_dias, 
    contar_pacientes_mas_5_dias, 
    promedio_dias_internacion
)
lista_pacientes = []

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print ("\n----SISTEMA DE GESTION DE PACIENTES----")
    print("1. Cargar pacientes")
    print("2. Mostrar pacientes")
    print("3. Buscar paciente por número de historia clínica")
    print("4. Orenar de forma ascendente por número de historia clínica")
    print("5. Paciente con mayor cantidad de días hospitalizado")
    print("6. Paciente con menor cantidad de días hospitalizado")
    print("7. Paciente con mas de 5 dias de hospitalización")
    print("8. Promedio de días de internación")
    print("9. Salir del programa")

    opcion = input("Seleccione una opción (1-8): ")

    match opcion:
        case "1":
            cargar_pacientes(lista_pacientes)
        case "2":
            imprimir_pacientes(lista_pacientes)
        case "3":
            buscar_paciente(lista_pacientes)
            print("")
        case "4":
            ordenar_forma_ascendente(lista_pacientes)
            print("")
        case "5":
            paciente_mas_dias(lista_pacientes)
        case "6":
            paciente_menos_dias(lista_pacientes)
        case "7":
            contar_pacientes_mas_5_dias(lista_pacientes)
        case "8":
            promedio_dias_internacion(lista_pacientes)
        case "9":
            print(" Saliendo del programa...")
            break
        case _:
            print("❌ Opción no válida. Intente nuevamente.")

