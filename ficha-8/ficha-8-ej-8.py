#Título
print("Menu de Opciones con Secuencias\n")

OPCIONES = "abcd"
MENU = "a) Determinar cantidad y porcentaje de números múltiplos de 3 y 5 " \
       "dentro de una secuencia de números\nb) Determinar la cantidad " \
       "de palabras de más de 4 letras en un texto\nc) Determinar el alumno " \
       "con peor nota final de tres alumnos de posgrado\nd) Salir\n..."

op = "z"

while not op in OPCIONES:
    op = input("\nSeleccione una opción del menú:\n" + MENU)
    if not op in OPCIONES:
        print("Error: Opción seleccionada invalida")
    # Opción de salida
    if op == "d":
        break
    elif op == "a":
        rondas = n = -1
        mult_3 = mult_5 = porc_3 = porc_5 = 0
        while rondas < 0:
            rondas = int(input("Cuantos números se desean cargar?: "))

            # Validar cantidad de cargas mayores o iguales a 0
            if rondas < 0:
                print("Error: No se puede realizar un número "
                      "negativo de cargas")

        #Carga de los "n" números 1 por 1
        for i in range(rondas):
            # Validar carga de números positivos
            while n < 1:
                n = float(input("Ingrese un número positivo: "))
                if n < 1:
                    print("Error: Solo se deben cargar números mayores a 0")

             # Contar múltiplos de 3 y 5
            if n % 3 == 0:
                mult_3 += 1
            if n % 5 == 0:
                    mult_5 += 1

            # Forzar ingreso y validación de más números
            n = -1

        # Verificar división por 0
        if rondas:
            porc_5 = mult_5 * (100 / rondas)
            porc_3 = mult_3 * (100 / rondas)

        # Visualización de resultados
        print("\nCantidad de números múltiplos de 3:", mult_3,
                "\tPorcentaje: %", porc_3)
        print("Cantidad de números múltiplos de 5:", mult_5,
                "\tPorcentaje: %", porc_5)

    elif op == "b":
        texto = ""
        letras = palabras_de_4 = 0
        anterior = ""
        while len(texto) == 0 or texto[-1] != ".":
            texto = input("Ingrese un texto finalizado en punto:\n...")
            if len(texto) == 0 or texto[-1] != ".":
                print("Error: El texto ingresado no es válido")
        # Iterar texto
        for i in texto:
            if i == ".":
                # Validar si se formó una palabra de más de 4 letras
                # antes de finalizar el texto
                if letras > 4:
                    palabras_de_4 += 1
                break

            elif (anterior.isalpha() or not anterior) and i.isalpha():
                # Contar la cantidad de letras consecutivas
                letras += 1

            else:
                # Reiniciar contador cuando se corte la secuencia de letras
                if letras > 4:
                    palabras_de_4 += 1
                letras = 0

        # Visualizar resultados
        print("\nCantidad de palabras con más de 4 letras:", palabras_de_4)

        # Actualizar el valor de la anterior letra
        anterior = i

    else:
        min_nom = min_nota = None
        for i in "123":
            nom = input("Ingrese el nombre del " + i + "º alumno: ")
            nota = -1
            # Validación de nota
            while nota < 0 or nota > 10:
                nota = int(input("Ingrese la nota obtenida: "))
                if nota < 0 or nota > 10:
                    print("Error: La nota debe ser un valor entre 0 y 10")

            if min_nota is None or nota < min_nota:
                min_nota, min_nom = nota, nom

        # Visualización de resultados
        print("\nAlumno con peor nota:", min_nom)


    # Forzar la visualización del menú
    op = "z"

print("\nFinalización del programa")
