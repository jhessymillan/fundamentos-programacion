# 1. Utilizar la instrucción print para mostrar cada resultado de las siguientes expresiones. 
# Explicar en un comentario de una sola línea el orden que ejecuta el intérprete Python en cada una de ellas. 
# Ejemplo: 12*4+4*5 = 68 orden: multiplicación, suma:

# 12 * 4 + 4 * 5 
# Orden: Multiplicacion, suma
print("12 * 4 + 4 * 5: ", 12 * 4 + 4 * 5)

# 12 * (4 + 4) * 5
# Orden: Suma del parentesis, multiplicacion
print("12 * (4 + 4) * 5: ", 12 * (4 + 4) * 5)

# 5 * 4 / 2
# Orden: Division, multiplicacion
print("5 * 4 / 2: ", 5 * 4 / 2)

# 5 * (4 / 2) 
# Orden: Division del parentesis, multiplicacion
print("5 * (4 / 2): ", 5 * (4 / 2))

# (12 + (12 + 6 * 4)) / 3
# Orden: Multiplicacion despues suma dentro del parentesis mas interno, suma del otro parentesis y por ultimo la division
print("(12 + (12 + 6 * 4)) / 3: ", (12 + (12 + 6 * 4)) / 3)

# 3 * ((4 + 5) / (18 / 6) - 4)
# Orden: Division del parentesis interno, suma del parentesis interno, division y despues resta del otro parentesis y por ultimo la multiplicacion
print("3 * ((4 + 5) / (18 / 6) - 4): ", 3 * ((4 + 5) / (18 / 6) - 4))

