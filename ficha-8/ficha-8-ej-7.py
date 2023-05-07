#Título
print("Validación Datos Personales\n")

OPCIONES = "abc"
MENU = "a) Validar número CUIT\nb) Validar DNI\nc) Salir\n..."
SECUENCIA_CUIT = "5432765432"
op = "z"

while not op in OPCIONES:
    op = input("\nSeleccione una opción del menú:\n" + MENU).lower()
    # Validar opción ingresada
    if not op in OPCIONES:
        print("Error: Opción inválida")
    # Operaciones del menú
    if op == "c":
        # Salida
        break
    elif op == "a":
        # Validación de CUIT
        valid = False
        cuit = input("Ingrese un número CUIT (99-99999999-9): ")
        # validar largo
        if len(cuit) < 13:
            print("Invalido: El número CUIT debe contener 13 caracteres")
        else:
            ultimo_dig = cuit[-1]
            resto_dig = cuit[0:2] + cuit[3:11]

            if cuit[2] != "-" or cuit[11] != "-":
                print("Invalido: Se deben incluir un guion en la 3º "
                      "y 11º posición")
            elif not resto_dig.isnumeric() or not ultimo_dig.isnumeric():
                print("Invalido: Solo se permiten números y guiones")
            else:
                # Calcular dígito verificador
                prod = 0
                for i in range(0, 10):
                    prod += int(resto_dig[i]) * int(SECUENCIA_CUIT[i])
                digito_verificador = 11 - (prod % 11)

                # verificar igualdad con el último número del CUIT
                if digito_verificador != int(ultimo_dig):
                    print("Invalido:  El dígito verificador no es igual al "
                          "último dígito del CUIT")
                else:
                    valid = True

            if valid:
                print("\nNúmero CUIT válido")
    else:
        dni = input("Ingrese un número DNI (X9.999.999): ")
        if len(dni) < 7 or len(dni) > 8:
            print("Invalido: En número DNI debe contener 7 o 8 caracteres")
        elif not dni.isnumeric():
            print("Invalido: Solo se admiten números")
        else:
            print("\nNúmero DNI válido")

    # Forzar la visualización del menú
    op = "z"

print("\nFinalización del programa")