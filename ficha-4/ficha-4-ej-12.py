import random

print("Cartas de Truco\n")

#constantes
PALOS_R = 0, 4
NUMEROS_R = 0, 10
PALOS = 'Espada', 'Basto', 'Oro', 'Copa'
NUMEROS = "1", "2", "3", "4", "5", "6", "7", "10", "11", "12"

#Procesos
carta_1 = random.randrange(*NUMEROS_R), random.choice(PALOS)
carta_2 = random.randrange(*NUMEROS_R), random.choice(PALOS)
carta_3 = random.randrange(*NUMEROS_R), random.choice(PALOS)

es_mismo_palo = carta_1[1] == carta_2[1] == carta_3[1]

hay_as_espada = carta_1[1] == "Espada" and NUMEROS[carta_1[0]] == "1" \
             or carta_2[1] == "Espada" and NUMEROS[carta_2[0]] == "1"\
             or carta_3[1] == "Espada" and NUMEROS[carta_3[0]] == "1"

if hay_as_espada:
    mensaje = "\nSe encuentra el as de espada"
else:
    mensaje = "\nNo se encuentra el as de espada"

if es_mismo_palo:
    may = NUMEROS[max(carta_1[0], carta_2[0], carta_3[0])]
    palo = carta_1[1]
    mensaje = mensaje + "\nLa mayor carta es el " + may + " de " + palo
else:
    mensaje = mensaje + "\nLas cartas no son del mismo palo"

#Resultado
print(mensaje)