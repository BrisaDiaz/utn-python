import random

#Título
print("Lanzamiento de dados\n")

#Constantes
RANGE = 1, 6

#Procesos
dado_1 = random.randint(*RANGE)
dado_2 = random.randint(*RANGE)
suma = dado_1 + dado_2

es_igual = dado_1 == dado_2
es_impar = suma%2

if es_igual or es_impar:
    mensaje = "Ganaste!"
else:
    mensaje = "Perdiste, vuelve a intentar."

#Resultado
print(mensaje)