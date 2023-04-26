import random

#Título
print("Menú y números aleatorios\n")

MENU = "Opción 1: Calcular promedio de 1.000 números aleatorios generados "\
       " en el rango de [0, 100.000].\nOpción 2: Buscar el mayor de 10.000"\
       " números aleatorios generados en el rango de [0, 100.000]."\
       "\nOpción 3: Buscar el menor de 5.000 números aleatorios "\
       "generados en el rango de [0, 100.000] y calcular el valor promedio " \
       "de los números menores a 10.000.\nCualquier otro número: " \
       "Salir del programa\n...."
OPCIONES = 1, 2, 3

#Carga de datos
print("Ingrese una opción: ")
op = int(input(MENU))

while op in OPCIONES:
    print()
    if op == 1:
        ronda = 1
        suma = 0

        while ronda <= 1000:
            suma += random.randint(0, 100000)

            # Actualización de datos
            ronda += 1

        prom = suma / ronda

        # Visualización de datos
        print("Promedio de 1.000 números:", prom)

    elif op == 2:
        ronda = 1
        may = None

        while ronda <= 10000:
            num = random.randint(0, 100000)

            if may is None or num > may:
                may = num

            # Actualización de datos
            ronda += 1

        # Visualización de datos
        print("Mayor número entre 10.000:", may)

    else:
        ronda = 1
        min = None
        suma = cant_min = 0

        while ronda <= 5000:
            num = random.randint(0, 100000)

            if min is None or num < min:
                min = num

            if num < 10000:
                suma += num
                cant_min += 1

            # Actualización de datos
            ronda += 1

        prom = suma / cant_min

        # Visualización de datos
        print("Menor número entre 5.000:", may)
        print("Promedio:", prom)

    print()
    print("Ingrese una opción: ")
    op = int(input(MENU))

