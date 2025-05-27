'''Crea una función recursiva que sume los números naturales, o sea, la suma de 1 hasta un número dado n'''

def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n - 1)

# Ejemplo de uso:
numero = int(input("Ingrese un número natural: "))
if numero >= 1:
    resultado = suma_naturales(numero)
    print("La suma de los números naturales hasta", numero, "es:", resultado)
else:
    print("Debe ingresar un número natural (mayor o igual a 1).")