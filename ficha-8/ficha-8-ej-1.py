# Título
print("Menu de Opciones con secuencias\n")

# Constantes
VOCALES = "aeiou"
OPCIONES = "abcd"
MENU = "a) Calcular la sumatoria de los cuadrados de los números enteros " \
       "entre 1 y \"n\"\nb) Contar la cantidad de palabras terminadas " \
       "en vocal dentro de un texto\nc) Determinar si hay mayoría par o " \
       "impar de una serie de números cargados\nd) Salir\n..."

op = "z"

while not op in OPCIONES:

    # Validación de opción ingresada
    op = input("\nSeleccione una opción de menú:\n" + MENU).lower()
    if not op in OPCIONES:
        input("Error: La opción seleccionada no es válida")

    # Opciones del menú
    if op == "d":
        break
    elif op == "a":
        n = suma = 0

        # Validar el ingreso de solo positivos
        while n < 1:
            n = int(input("Ingrese un número positivo:"))
            if n < 1:
                print("Error: No se permiten negativos")

        # Expresión general de sumatoria de cuadrados
        suma = n * (n + 1) * (2*n + 1) * 1/6

        # Visualización de resultados
        print("\nSumatoria de los cuadrados desde 1 a " + str(n) + ":", suma)
    elif op == "b":
        texto = ""
        fin_vocal = 0

        # Validar la finalización en punto
        while len(texto) == 0 or texto[-1] != ".":
            texto = input("Ingrese un texto finalizado en punto:")
            if len(texto) == 0 or texto[-1] != ".":
                print("Error: Se debe finalizar el texto con un punto")

        # Iterar el texto hasta antes del punto
        for i in range(len(texto) - 1):
            # Comprobar el final de palabra
            if texto[i + 1].isspace() or texto[i + 1] == ".":
                if texto[i] in VOCALES:
                    fin_vocal += 1

        # Visualización de resultados
        print("\nCantidad de palabras finalizadas en vocal:", fin_vocal)

    else:
        pares = impares = 0
        n = int(input("Ingrese un número (0 para finalizar): "))
        while n != 0:

            # Validar si es par o impar
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1

            n = int(input("Ingrese un número (0 para finalizar): "))

        # Visualización de resultados
        if pares > impares:
            print("\nSe cargaron más números pares que impares")
        elif impares > pares:
            print("\nSe cargaron más números impares que pares")
        else:
            print("\nSe cargo la misma cantidad de números pares e impares")

    # Forzar visualización del menú
    op = "z"

print("\nFinalización del programa")