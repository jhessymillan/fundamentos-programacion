# Realizar un programa que permita obtener la suma, resta, multiplicación y división de dos números x e y ingresados por teclado. 
# El programa debe imprimir los números pedidos y el resultado de las cuatro operaciones.

x = float(input("Ingrese un numero: "))
y = float (input("Ingrese otro numero: "))

# Suma:
print(f"{x} + {y}: ", x + y)

# Resta:
print(f"{x} - {y}: ", x - y)

# Multiplicacion:
print(f"{x} * {y}: ", x * y)

# Division:
if y == 0: 
    print(f"{x} / {y}: ", "No se puede dividir por 0")
else:
    print(f"{x} / {y}: ", x / y)