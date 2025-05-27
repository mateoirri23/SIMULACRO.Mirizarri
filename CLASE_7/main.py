"""Debe crear un programa que permita ingresar una edad 
(entre 1 y 99 años, validar mediante una funcion) y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion).
En caso de ingresar valores erróneos (edad fuera de rango, o generos inexistentes), 
informar de esa situación mostrando un mensaje y terminar el programa.
Si todos los datos fueron bien ingresados, el programa debe ser capas de indicar, 
sabiendo que las mujeres se jubilan a los 60 años o mas, los hombres con 65 años o mas,
para los no binarios establecemos un promedio de ambas edades. 
Determinar mediante funciones si una persona puede o no jubilarse."""

def validar_edad(edad:int):
    if 1 <= edad <= 99:
        return True
    else:
        print("Edad inválida. Debe estar entre 1 y 99 años.")
    
def validar_genero(genero:str):
    generos_validos = ['F', 'M', 'X']
    if genero in generos_validos:
        return True
    else:
        print("Género inválido. Debe ser 'F', 'M' o 'X'.")
    
def puede_jubilarse(edad:int, genero:str):
    if genero == 'F' and edad >= 60:
        print("Puede jubilarse.")
    elif genero == 'M' and edad >= 65:
        print("Puede jubilarse.")
    elif genero == 'X' and edad >= 62.5:  # Promedio de 60 y 65
        print("Puede jubilarse.")
    else:
        print("No esta habilitado para jubilarse aún.")    

ingrese_edad = int(input("Ingrese su edad (1-99): "))
es_valida = validar_edad(ingrese_edad)



