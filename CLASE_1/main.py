#Crear dos variables, intercambiar sus valores y mostrar valores actuales y luego 
#los valores modificados. 

variable_a = 10 
variable_b = 5 
bandera = 0 

print(f"valores actuales: variable_a = {variable_a}, variable_b = {variable_b}")

bandera = variable_a 
variable_a = variable_b 
variable_b = variable_a 

print(f"Valores modificados: variable_a = {variable_a}, variable_b = {variable_b}")
"------------------------------------------------------------------------------------------------------"

#Definir 5 variables numericas int o float. calcular el promedio y mostrar en pantalla 

num_1 = 10
num_2 = 10
num_3 = 10
num_4 = 10
num_5 = 10

Suma = (num_1 + num_2 + num_3 + num_4 + num_5) 
promedio = Suma / 5 
print(f"El promedio calculado es {promedio}")


"--------------------------------------------------------------------------------------------------------"
'''A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
'''

tamaño_jugador = int(input("Ingrese tamaño del jugador: "))

if tamaño_jugador < 160: 
    posicion = "Base"

elif 160 <= tamaño_jugador <= 179 :
    posicion = "Escolta"

elif 180 <= tamaño_jugador <= 199: 
    posicion = "Alero"

else: 
    posicion = "Ala-pivot o pivot"

print(f"El jugador ingresado juega de: {posicion}")

"-------------------------------------------------------------------------------------------------------------"
'''Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
'''

import random 

numero = random.randint(1,10)

if numero > 6 : 
    condicion = " Promocion directa"

elif numero >= 4:
    condicion = "Aprobado"

else:
    condicion = "desaprobado"

print (f"La condicion del alumno es:{condicion}, la nota es {numero}")