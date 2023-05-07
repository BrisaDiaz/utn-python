#Título
import random

print("Menú de opciones y validación\n")

OPCIONES = "abce"
MENU = "a) Calcular su promedio de una serie de números\n" \
       "b) Determinar la cantidad de valores negativos y positivos " \
       "de un número de valores aleatorios entre -100 y 100\n" \
       "c) Validar si alumno aprovo un examen\n" \
       "e) Finalizar\n..."

op = "z"

while op != "e":
    while not op in OPCIONES:
        op = input("\nSeleccione una operación del menú:\n" + MENU)
        if not op in OPCIONES:
            print("Error: Operación inválida")

    if op == "e":
        break

    if op == "a":
        suma = conteo = promedio = 0
        n = -2
        while n < -1:
            n = float(input("Ingrese un número positivo (-1 para finalizar): "))
            if n == -1:
                break
            if n < -1:
                print("Error: Solo se permiten números positivos")
            conteo += 1
            suma += n
            # Forzar ingrese de otro número positivo
            n = -2

        # validar que no se divida por cero
        if conteo:
            promedio = suma / conteo
        print("\nPromedio de los números ingresados:", promedio)

    if op == "b":
        positivos = negativos = 0
        rondas = -1
        # validad cantidad de valores a generar
        while rondas < 0:
            rondas = int(input("Cuantos números aleatorios desea generar?: "))
            if rondas < 0:
                print("Error: No se puede generar una cantidad negativa de valores")
        # Generar valores y contar
        for i in range(rondas):
            n = random.randint(-100, 100)
            if n >= 0:
                positivos += 1
            else:
                negativos += 1

        print("\nCantidad de valores  generados positivos:", positivos)
        print("Cantidad de valores  generados negativos:", negativos)

    else:
        nota = -1
        condicion = "Aprobado"

        # Validar que la nota sea enter 0 y 10
        while 10 < nota or nota < 0:
            nota = int(input("Ingrese la nota del alumno: "))
            if 10 < nota or nota < 0:
                print("Error: La nota debe ser un valor entre 0 y 10")
        # Definir condición del alumno
        if nota < 4:
            condicion = "Desaprobado"

        print("\nCondición del alumno:", condicion)

    # Forzar visualización del menú
    op = "z"

print("\nFinalización del programa")

