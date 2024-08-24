# Realizar un programa que, dada una cantidad de dólares y su cotización permita obtener el equivalente en pesos.

total_dolar = float(input("Ingrese la cantidad de dolares a convertir: "))
# 1 dolar -> cotizacion pesos
cotizacion = float(input("Ingrese la cotizacion de dolares a pesos: "))
total_pesos = total_dolar * cotizacion

print(f"Tienes {total_pesos} pesos")