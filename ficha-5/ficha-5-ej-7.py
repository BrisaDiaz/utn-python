import random

#Título
print("Juego de Dados: Pares e Impares\n")

#Carga de datos
record = int(input("Ingrese el record del campeón: "))

#procesos
#inicialización de puntajes de los retadores
jugador_1_p = 0
jugador_2_p = 0

#tirar dados 1º ronda
print("\n1º RONDA")
dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)
print("dado 1:", dado_1, "\t", "dado 2:", dado_2)

suma_dados = dado_1 + dado_2

if suma_dados%2:
    # la suma es impar
    jugador_2_p += suma_dados
else:
    # la suma es par
    jugador_1_p += suma_dados

print("retador 1:", jugador_1_p, "\t", "retador 2:", jugador_2_p)

#tirar dados 2º ronda
print("\n2º RONDA")
dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)
print("dado 1:", dado_1, "\t", "dado 2:", dado_2)
suma_dados = dado_1 + dado_2
max_valor = max(dado_1, dado_2)
min_valor = min(dado_1, dado_2)

if suma_dados%2:
    # la suma es impar
    jugador_2_p += max_valor
    jugador_1_p -= min_valor
else:
    # la suma es par
    jugador_1_p += max_valor
    jugador_2_p -= min_valor


print("retador 1:", jugador_1_p, "\t", "retador 2:", jugador_2_p)

print("\n3º RONDA")
may_p = jugador_1_p
may_jugador = "retador 1"

if jugador_2_p > jugador_1_p:
    may_p = jugador_2_p
    may_jugador = "retador 2"

if may_p > record:
    print("El ganador es el", may_jugador)
    print("Se supero el record con", may_p, "puntos")
else:
    print("El campeón mantiene su puesto")

