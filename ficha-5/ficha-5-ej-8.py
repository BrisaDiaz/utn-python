import random

#Título
print("Juego del Punto\n")

#procesos

#inicialización de puntaje
puntaje = 0

#tirada de dedos
dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)
dado_3 = random.randint(1, 6)
pares_iguales = False

if dado_1 % 2 == 1:
    if dado_1 == 1:
        puntaje += 1
    else:
        puntaje += dado_1 - 1
else:
    if dado_1 == dado_2 == dado_3:
        pares_iguales = True

if dado_2 % 2 == 1:
    if dado_2 == 1:
        puntaje += 1
    else:
        puntaje += dado_2 - 1

if dado_3 % 2 == 1:
    if dado_3 == 1:
        puntaje += 1
    else:
        puntaje += dado_3 - 1

#Carga de datos
prev_puntaje = int(input("Ingrese su puntaje previo: "))

puntaje += prev_puntaje

print("\nPuntaje acumulado:", puntaje)
print("Puntaje previo:", prev_puntaje)

if pares_iguales:
    print("Felicidades,al finalizar duplicaras tu acumulado de puntos!")