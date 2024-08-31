# 3. Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer
# el usuario. Tiene la siguiente tarifa:
#    - Viaje mínimo $50
#    - Si recorre entre 0 y 10 km: $20/km
#    - Si recorre 10 km o más: $15/km
#
# INICIO:
# 1. Guardar el precio del viaje minimo en MINVIAJE
# 2. Solicitar por teclado los KM que desea recorrer y guardarlo en kmViaje
# 3. Calcular el total del viaje de acuerdo con el kmViaje:
#       Si recorre entre 0 y 10 km:
#           Multiplicar kmViaje por 20 y guardarlo en precioViaje
#       Si recorre 10 km o más:
#           Multiplicar kmViaje por 15 y guardarlo en precioViaje
# 4. Si el precio del viaje es menor a viaje minimo:
#       Guardar en el precio del viaje el viaje minimo
# 5. Mostrar en pantalla el precio del viaje
# FIN

MINVIAJE = 50
kmViaje = int(input("Cuantos km desea recorrer? "))
precioViaje = 0

if kmViaje > 0 and kmViaje < 10:
    precioViaje = kmViaje * 20

if kmViaje >= 10:
    precioViaje = kmViaje * 20

if precioViaje < MINVIAJE:
    precioViaje = MINVIAJE

print(f"El precio del viaje es {precioViaje}")