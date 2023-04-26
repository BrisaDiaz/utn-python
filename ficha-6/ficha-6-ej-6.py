import random

#Título
print("Menores y promedio\n")
RANGO = (0, 100000)
CANTIDAD = 5000

ronda = 0
cant_menor_10000 = 0
suma_menor_10000 = 0
menor = None

while ronda <= CANTIDAD:
    num = random.randint(*RANGO)
    if num < 10000:
        suma_menor_10000 += num
        cant_menor_10000 += 1

    if menor is None or num < menor:
        menor = num

    # Actualización de datos
    ronda += 1

prom_menor_10000 = suma_menor_10000 / cant_menor_10000

#Visualización de datos
print("Valor promedio de los números menores a 10.000:", prom_menor_10000)