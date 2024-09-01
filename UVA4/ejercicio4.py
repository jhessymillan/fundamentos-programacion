# 4. Ingresar las notas de los dos parciales de un alumno e indicar si promociona, aprueba o debe recuperar. 
# Si el valor de la nota no está entre 0 y 10, debe informar un error.
#    - Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#    - Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#    - Recupera cuando al menos una de las dos notas es menor a 4.
#
#   INICIO:
#   1. Solicitar por teclado la nota del primer parcial y guardarlo en nota1
#   2. Si la nota1 se encuentre entre 0 y 10:
#       Solicitar por teclado la nota del segundo parcial y guardarlo en nota2
#           Si la nota2 se encuentre entre 0 y 10:
#               Si nota 1 y nota2 son mayores o iguales a 7:
#                   Mostrar por pantalla "Promociona"
#               Si nota 1 y nota2 son mayores o iguales a 4:
#                   Mostrar por pantalla "Aprueba"
#               Si nota 1 o nota2 es menor a 4:
#                   Mostrar por pantalla "Recupera"
#           Sino:
#            Mostrar un error por pantalla "El valor de la nota no está entre 0 y 10"
#      Sino:
#       Mostrar un error por pantalla "El valor de la nota no está entre 0 y 10"
ERROR_STR = "El valor de la nota no está entre 0 y 10"
nota1 = int(input("Ingrese la nota del primer parcial: "))
if 0 <= nota1 <= 10:
    nota2 = int(input("Ingrese la nota del segundo parcial: "))
    if 0 <= nota2 <= 10:
        if nota1 >= 7 and nota2 >= 7:
            print("Promociona")
        elif 4 <= nota1 and 4 <= nota2:
            print("Aprueba")
        else:
            print("Recupera")
    else:
        print(ERROR_STR)
else:
    print(ERROR_STR)
