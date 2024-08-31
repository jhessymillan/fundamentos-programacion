# Ingresar dos números enteros e indicar si son iguales o distintos. 

# Entrada: Ingresar 2 numeros y guardarlos en num1 y num2 
# Salida: Mostrar por pantalla si son iguales o distintos
# INICIO:
# 1. Solicitar por teclado el ingreso de un numero entero y guardarlo en num1
# 2. Solicitar por teclado el ingreso de un numero entero y guardarlo en num2
# 3. Comparar num1 y num2
#   Si son iguales mostrar por pantalla num1 y num2 son iguales
#   sino mostrar mostrar por pantalla num1 y num2 son distintos
# FIN
num1 = int(input("Ingrese un número entero "))
num2 = int(input("Nuevamente ingrese un número entero "))

if num1 == num2:
    print(f"{num1} y {num2} son iguales")
else:
    print(f"{num1} y {num2} son distintos")