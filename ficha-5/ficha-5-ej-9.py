import random

#Constantes
OPCIONES = ("piedra", "papel", "tijera")

#Título y carga de datos
op_jugador = input("¿Piedra, Papel o Tijera?: ").strip().lower()
print("")

#procesos

if op_jugador in OPCIONES:
    op_pc = random.choice(OPCIONES)

    if op_pc == op_jugador:
        print("Hubo un empate!")
    elif op_jugador == "tijera":
        if op_pc == "papel":
            print("Ganaste!")
        else:
            print("Perdiste!")
    elif op_jugador == "piedra":
        if op_pc == "tijera":
            print("Ganaste!")
        else:
            print("Perdiste!")
    elif op_pc == "piedra":
        print("Ganaste!")
    else:
        print("Perdiste!")
else:
    print("ERROR: Opción inválida!")
