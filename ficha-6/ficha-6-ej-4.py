import random

#Título
print("Promedio de números aleatorios\n")
RANGO = (0, 100000)
CANTIDAD = 1000

ronda = 0
suma = 0

while ronda <= CANTIDAD:
    suma += random.randint(*RANGO)

    # Actualización de datos
    ronda += 1

prom = suma / ronda

#Visualización de datos
print("Promedio de 1000 números aleatorios en el rango [0, 100000]:", prom)
