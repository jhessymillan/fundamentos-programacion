# Desarrollar un programa para cargar 5 notas. Validar que se encuentren entre 1 y 10. 
# Al finalizar, mostrar el promedio de las notas.

nota = int(input("Ingrese la nota 1: "))
promedio = 0
sumatoria = 0

while nota < 1 or nota > 10:
    print("La nota no se encuentra en el rango de 1 al 10")
    nota = int(input("Ingrese nuevamente la nota 1: "))

sumatoria = nota
for i in range(2, 5 + 1):
    nota = int(input(f"Ingrese nuevamente la nota {i}: "))

    while nota < 1 or nota > 10:
        print("La nota no se encuentra en el rango de 1 al 10")
        nota = int(input(f"Ingrese nuevamente la nota {i}: "))
    
    sumatoria += nota

promedio = sumatoria / 5
print(f"El promedio es {promedio}")