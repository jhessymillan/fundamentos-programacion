# Crear un programa que pida un número de día (ejemplo: 1) y escriba el nombre del día en letras ("lunes"). 
# Verificar que el día esté entre 1 y 7, e informar en caso de que no lo sea.

# Entrada: Ingresar por teclado un numero entero de dia y guardarlo en numDia
# Salida: Imprimir por pantalla el nombre del dia en letras
# INICIO:
# 1. Solicitar por teclado un numero de dia, guardarlo en numDia 
# 2. Mostrar de acuerdo al numero de dia el dia en letras
#     Si es 1 mostrar en pantalla Lunes
#     Si es 2 mostrar en pantalla Martes
#     Si es 3 mostrar en pantalla Miercoles
#     Si es 4 mostrar en pantalla Jueves
#     Si es 5 mostrar en pantalla Viernes
#     Si es 6 mostrar en pantalla Sabado
#     Si es 7 mostrar en pantalla Domingo
#     Sino mostrar en pantalla El numero no corresponde a un dia
# FIN

numDia = int(input("Ingresar un numero de día: "))
if numDia == 1:
    print("Lunes")
elif numDia == 2:
    print("Martes")
elif numDia == 3:
    print("Miercoles")
elif numDia == 4:
    print("Jueves")
elif numDia == 5:
    print("Viernes")
elif numDia == 6:
    print("Sabado")
elif numDia == 7:
    print("Domingo")
else:
    print("El numero no corresponde a un dia")