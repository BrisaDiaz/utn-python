import random

#Título
print("Búsqueda de mayor\n")
RANGO = (-100000, 100000)
CANTIDAD = 10000

ronda = 0
cant_positivos = 0
may = None

while ronda <= CANTIDAD:
    num = random.randint(*RANGO)
    if num > 0:
        cant_positivos += 1

    if may is None or num > may:
        may = num

    # Actualización de datos
    ronda += 1

porc_positivos = cant_positivos * (100 / ronda)

#Visualización de datos
print("El mayor número de 10.000 números aleatorios en el rango de "
      "[-100.000, 100.000]:", may)
print("Porcentaje de números positivos: %", porc_positivos)
