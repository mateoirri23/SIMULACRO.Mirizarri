import math 
'''1-Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2-Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3-Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
'''

def pedir_numero():
    numero = int(input("Ingrese un numero: "))
    return numero

numero_ingresado = pedir_numero()
print ("El numero ingresado es ", numero_ingresado)

print("-----------------------------------------------------------------------------------------------------------")

def pedir_numero():
    numero = float(input("Ingrese un numero flotante: "))
    return numero

numero_ingresado = pedir_numero()
print ("El numero ingresado es ", numero_ingresado)

print("------------------------------------------------------------------------------------------------------------")

def pedir_cadena(mensaje): 
    cadena = input(mensaje)
    return cadena 

cadena_ingresada = pedir_cadena("Ingrese cadena: ")
print ("Tu nombre es: ", cadena_ingresada)

print("-------------------------------------------------------------------------------------------------------------")

'''1-Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
2-Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
3-Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
'''
def solicitar_datos_rectangulo():
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    area = base * altura /2
    return area 

datos_rectangulo = solicitar_datos_rectangulo()
print("El area de su rectangulo es:", datos_rectangulo)

print("-------------------------------------------------------------------------------------------------------------")

def solitar_datos_circulo():
    radio = float(input("Ingrese el radio del circulo: "))
    area = math.pi * radio ** 2
    return area 

datos_circulo = solitar_datos_circulo()
print("El area de su circulo es:", datos_circulo)

print("-------------------------------------------------------------------------------------------------------------")

def verificar_par_impar(numero:int) -> None:
    if numero % 2 == 0:
        print(f"Tu número {numero} es par.")
        
    else :
        print(f"Tu número {numero} es impar.")

numero = int(input("Ingrese un número para verificar si es par o impar: "))
(verificar_par_impar(numero))

print("-----------------------------------------------------------------------------------------------------------")

#8-Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#9-Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado. (se puede intentar hacer con pca l() que esta en math)

def definir_num_mayor(a:int, b:int, c:int) -> int:
    if a >= b and a >= c: 
        return a 
    
    elif b >= a and b >= c: 
        return b 

    else:
        return c 

num_1 = int(input("Ingresar primer numero: ")) 
num_2 = int(input("Ingresar segundo numero: "))   
num_3 = int(input("Ingresar tercer numero: "))

numero_maximo = definir_num_mayor(num_1, num_2, num_3)
print("El numero mayor es: ", numero_maximo)

print("---------------------------------------------------------------------------------------------------------")

def calcular_potencia(base:int, exponente:int):
    return math.pow(base, exponente)

base = int(input("Ingrese su numero base: "))
exponente = int(input("Ingrese su exponente: "))

resultado = calcular_potencia(base, exponente)

print(f"Base ingresada: {base}, exponente ingresado: {exponente}, resultado", resultado )
      
print("-----------------------------------------------------------------------------------------------------------")