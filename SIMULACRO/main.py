from Funciones import (
    cargar_productos,
    buscar_producto,
    ordenar_por_precio_barato,
    ordenamiento_precio_caro,


)
'''inventario = [
    ["Laptop", 1500.00, 10],
    ["silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor",300.00, 30],
]'''
inventario = []

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Mostrar producto mas bartato")
    print("4. Mostrar producto más caro")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    match opcion:
        case "1":
            cargar_productos(inventario)
        case "2":
            buscar_producto(inventario)
        case "3":
            ordenar_por_precio_barato(inventario)
            print("✅ Inventario ordenado por precio.")
        case "4":
            ordenamiento_precio_caro(inventario)
            print("✅ Inventario ordenado por precio.")
        case "5":
            print(" Saliendo del programa...")
            break
        case _:
            print("❌ Opción no válida. Intente nuevamente.")


































