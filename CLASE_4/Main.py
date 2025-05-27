'''''Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
Mostrar la suma de los números desde el 1 hasta el 10.'''

# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

for i in range (1, 11):    
    print(i)
print("-----------------------------------------------------------")
#Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

for i in range (10,0, -1):
    print(i)
print("-------------------------------------------------------------")
#Mostrar la suma de los números desde el 1 hasta el 10.

suma = 0 
for i in range (1, 11):
    suma += i 
    
print(f"La suma de todos los numeros es {suma}")
print("--------------------------------------------------------------")
#Imprimir los números múltiplos de 3 entre el 1 y el 10.
#Mostrar los números pares que hay desde la unidad hasta el número 50.
#Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:print("multiplos de 3 entre 1 y el 10")
prueba = ""
for i in range (1, 11):
    if i % 3 == 0:
        for i in range (1, i +1):
            prueba += str(i)
            print(prueba)

print("-----------------------------------------------------------")  

print("multiplos de 2 entre 1 y el 50")

for i in range (1, 51):
    if i % 2 == 0:
        print(i) 

numero = int(input("Ingrese un numero: "))
prueba = ""

for i in range (1, numero +1):
    prueba += str(i)
    print(prueba)

    




