#Título
print("Validación de cuenta\n")

#Carga de datos
email = input("Ingrese una cuenta de email: ").strip()
print()

arroba_ok = puntos_ok = True
cant_arroba = prev_punto_index = 0

if email[0] == "@" or email[-1] == "@":
    arroba_ok = False
    cant_arroba += 1
    print("Email empieza/termina con @")

if email[0] == "." or email[-1] == ".":
    puntos_ok = False
    print("Email empieza/termina con un punto")

for i in range(len(email)):

    if email[i] == "@" and arroba_ok:
        if cant_arroba >= 1:
            arroba_ok = False
            print("Email posee más de un solo @")
        else:
            cant_arroba += 1

    if email[i] == "." and puntos_ok:
        if prev_punto_index + 1 == i:
            puntos_ok = False
            print("Email posee dos puntos seguidos")
        else:
            prev_punto_index = i

if cant_arroba != 1:
    arroba_ok = False
    print("EL email no contiene ningún @")

if arroba_ok and puntos_ok:
    print("\nEl email es válido")
else:
    print("\nEl email no es válido")
