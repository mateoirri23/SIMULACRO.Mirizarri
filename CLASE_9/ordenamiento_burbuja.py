def ordenamiento_burbuja(elementos):
    longitud = len(elementos)

    for i in range(longitud):
        for j in range(longitud-1):
            if elementos[j] < elementos[j + 1]: #------> Accede a la lista y compara el elemento j con el siguiente
                axuliar = elementos[j]
                elementos[j] = elementos[j + 1]
                elementos[j + 1] = axuliar

elementos = [5, 2, 9, 1, 5, 6, 3, 7, 8]
ordenamiento_burbuja(elementos)
print("Lista ordenada:", elementos)

print("--------------------------------------------------------------------------------------")

def ordenar_por_precio(lista):
    
    longitud = len(lista)

    for i in range(longitud):
        for j in range(longitud-1-i):
            if lista[j][2] > lista[j + 1][2]:   
                aux = lista[j + 1 ]
                lista[j + 1] = lista[j]
                lista[j] = aux


lista = [
        {"nombre": "Producto A", "precio": 10.99},
        {"nombre": "Producto B", "precio": 5.49},
        {"nombre": "Producto C", "precio": 7.99},
        {"nombre": "Producto D", "precio": 12.50},
        {"nombre": "Producto E", "precio": 3.75},
        {"nombre": "Producto B", "precio": 5.49},
        {"nombre": "Producto C", "precio": 7.99},
        {"nombre": "Producto D", "precio": 12.50}, 
        {"nombre": "Producto C", "precio": 7.99},
        {"nombre": "Producto D", "precio": 12.50},
    ]

ordenar_por_precio(lista)
print("Lista ordenada por precio:", lista)

print("--------------------------------------------------------------------------------------")


