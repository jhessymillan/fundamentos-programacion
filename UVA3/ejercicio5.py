# 5. Realizar un programa que, dado un número ingresado por teclado, 
# obtenga su tabla de multiplicar hasta el 10 y la muestre en un formato similar a este:
# Número ingresado: 5
# 1 x 5 = 5
# 2 x 5 = 10    
# 3 x 5 = 15
# ...
# 10 x 5 = 50
# NOTA: para este ejercicio no está permitido utilizar ciclos de repetición, que veremos más adelante.

number = int(input("Ingrese un numero: "))

print(f"Numero Ingresado: {number}")
print(f"1 x {number} =", number * 1 )
print(f"2 x {number} =", number * 2 )
print(f"3 x {number} =", number * 3 )
print(f"4 x {number} =", number * 4 )
print(f"5 x {number} =", number * 5 )
print(f"6 x {number} =", number * 6 )
print(f"7 x {number} =", number * 7 )
print(f"8 x {number} =", number * 8 )
print(f"9 x {number} =", number * 9 )
print(f"10 x {number} =", number * 10 )