import random

#Título
print("Tito el robot\n")

RANGE = 0, 100
OPCIONES = "abcde"
MENU = "a) Girar al norte y avanzar 10 pasos\n" \
       "b) Girar al sur y avanzar 20 pasos\n" \
       "c) Girar al este y avanzar 10 pasos\n" \
       "d) Girar al oeste y avanzar 20 pasos\n" \
       "e) Finalizar\n..."

coordenadas = (random.randint(*RANGE), random.randint(*RANGE))
op = "z"

# validar ingrese de una opción del menu
while not op in OPCIONES:
    print("\nPosición actual:", coordenadas)
    op = input("Seleccione la siguiente operación:\n" + MENU)
    if not op in OPCIONES:
        print("Error: Operación inválida")

    # Operaciones del menú
    if op == "e":
        break
    if op == "a":
        coordenadas = (coordenadas[0], coordenadas[1] + 10)

    elif op == "b":
        coordenadas = (coordenadas[0], coordenadas[1] - 20)

    elif op == "c":
        coordenadas = (coordenadas[0] + 10, coordenadas[1])

    else:
        coordenadas = (coordenadas[0] - 20, coordenadas[1])

    # forzar visualización del menú
    op = "z"

print("\nPoción final:", coordenadas)




