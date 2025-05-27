numero = 7 

match numero: 
    case n if n < 0: 
        print ("Numero negativo")
    case 0: 
        print( "Cero")
    case 1 | 2 | 3 : 
        print("Numero pequeño")
    case 7 : 
        print(" numero jhihpgh9u")


print("------------------------------------------------------------------------------------------")

"""
Identificar el día de la semana
Solicita al usuario que ingrese un número entero entre 1 y 7. 
Utiliza match-case para imprimir el nombre del día de la semana 
correspondiente (por ejemplo, 1 para "Lunes", 2 para "Martes", etc.). 
Si el número no está en ese rango, muestra un mensaje indicando que el número es inválido.
Agregar la siguiente funcionalidad luego:
En el dia Sabado o Domingo si la temperatura (debera soliciar al usuario) esta entre 20 y 30 grados, imprimir "Puedes salir de la ca
"Puedes salir de la casa",
si la temperatura es mayor a 30 grados, imprimir No puedes salir de la casa porque hace mucho calor,
si la temperatura es menor a 20 grados, imprimir No puedes salir de la casa porque hace mucho frio.

"""

dia = int(input("Ingrese un numero del 1 al 7: "))

match dia : 
    case 1:
        print("Lunes")

    case 2:
        print("Martes")

    case 3:
        print("Miercoles")
    
    case 4:
        print("Jueves")

    case 5:
        print("Viernes")

    case 6:
        print("Sabado")
        temperatura = int(input("Ingrese una temperatura entre 20° o 30°: "))
        if temperatura > 20 and temperatura < 30: 
            print("Puedes salir de la casa")

        elif temperatura > 30: 
            print("imprimir No puedes salir de la casa porque hace mucho calor")

        elif temperatura < 20: 
            print("imprimir No puedes salir de la casa porque hace mucho frio.")

        
    case 7:
        print("Domingo")
        temperatura = int(input("Ingrese una temperatura 20° o 30°: "))
        if temperatura > 20 and temperatura < 30: 
            print("Puedes salir de la casa")

        elif temperatura > 30: 
            print("imprimir No puedes salir de la casa porque hace mucho calor")

        elif temperatura < 20: 
            print("imprimir No puedes salir de la casa porque hace mucho frio.")

    case _:
        print("Numero invalido, favor de ingresar un numero dentro del rango.")


print("------------------------------------------------------------------------------------------")

"""
Calculadora simple con match-case
Pide al usuario que ingrese dos números y un operador (como cadena: '+', '-', '*' o '/'). 
Utiliza match-case para ejecutar la operación correspondiente. Incluye condicionales en los 
casos para manejar la división, de modo que si se intenta dividir por cero se muestre un mensaje de error.
"""

