#Título
print("Mayor número en orden par\n")

#Carga de datos
num = float(input("Ingrese un número (0 para finalizar): "))

ronda = 1
may = num

while num != 0:

    if num % 2 == 0 and ronda % 2 == 0 and num > may:
        may = num

    # Actualización de datos
    ronda += 1
    num = float(input("Ingrese un número (0 para finalizar): "))

print()
#Visualización de datos
print("Mayor de todos los números pares con número de orden es par:", may)