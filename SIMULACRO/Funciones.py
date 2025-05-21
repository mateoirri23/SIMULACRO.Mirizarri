def cargar_productos(inventario):
    cantidad_productos = int(input("Ingrese la cantidad de productos a cargar: ")) 

    for i in range(cantidad_productos): 
        nombre = input("Ingrese el nombre del producto: ") 
        precio = float(input("Ingrese el precio del producto: ")) 
        cantidad = int(input("Ingrese la cantidad del producto: ")) 

        productos = [nombre, precio, cantidad]
        inventario.append(productos) 
        print("Producto cargado correctamente.") 

    return inventario

"-------------------------------------------------------------------------------------------------------"

def buscar_producto(inventario): 
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False

    for producto in inventario:
        nombre, precio, cantidad = producto
        if nombre == nombre_producto:
            print("\n✅ Producto encontrado:")
            print("Nombre  :", nombre)
            print("Precio  :", precio)
            print("Cantidad:", cantidad)
            encontrado = True
            break  # Salir del bucle al encontrarlo

    # Mostrar mensaje si no se encontró (sin usar if not)
    if encontrado == False:
        print("❌ Producto no encontrado en el inventario.")


"-------------------------------------------------------------------------------------------------------"


def ordenar_por_precio_barato(inventario):
    
    longitud = len(inventario)

    for i in range(longitud):
        for j in range(longitud-1-i):
            if inventario[j][2] > inventario[j + 1][2]:   
                aux = inventario[j + 1 ]
                inventario[j + 1] = inventario[j]
                inventario[j] = aux

    print("Lista ordenada por precio:", inventario)

"-------------------------------------------------------------------------------------------------------"


def ordenamiento_precio_caro(inventario):
    longitud = len(inventario)

    for i in range(longitud):
        for j in range(longitud-1):
            if inventario[j] < inventario[j + 1]: #------> Accede a la lista y compara el elemento j con el siguiente
                axuliar = inventario[j]
                inventario[j] = inventario[j + 1]
                inventario[j + 1] = axuliar

    print("Lista ordenada por precio:", inventario)


"--------------------------------------------------------------------------------------------------------"

