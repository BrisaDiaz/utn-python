import random

#Título
print("Tarjeta de Bingo\n")

#Constantes
RANGE = 1, 100

#funcón generadora de numeros randoms
get_rand = random.randint

#Procesos
r1, r2, r3, r4, r5, r6 = (get_rand(*RANGE), get_rand(*RANGE), get_rand(*RANGE),
                          get_rand(*RANGE), get_rand(*RANGE), get_rand(*RANGE))
r7, r8, r9, r10, r11 = (get_rand(*RANGE), get_rand(*RANGE), get_rand(*RANGE),
                        get_rand(*RANGE), get_rand(*RANGE))
r12, r13, r14, r15 = (get_rand(*RANGE), get_rand(*RANGE), get_rand(*RANGE),
                      get_rand(*RANGE))

#Carga de datos
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el primer segundo: "))
n3 = float(input("Ingrese el primer tercer: "))

#Procesos
if (n1 == r1 or n1 == r2 or n1 == r3 or n1 == r4 or n1 == r5 or n1 == r6
    or n1 == r7 or n1 == r8 or n1 == r9 or n1 == r10 or n1 == r11 or
    n1 == r12 or n1 == r13 or n1 == r14 or n1 == r15
    or n2 == r1 or n2 == r2 or n2 == r3 or n2 == r4 or n2 == r5 or n2 == r6
    or n2 == r7 or n2 == r8 or n2 == r9 or n2 == r10 or n2 == r11 or
    n2 == r12 or n2 == r13 or n2 == r14 or n2 == r15
    or n3 == r1 or n3 == r2 or n3 == r3 or n3 == r4 or n3 == r5 or n3 == r6
    or n3 == r7 or n3 == r8 or n3 == r9 or n3 == r10 or n3 == r11 or
    n3 == r12 or n3 == r13 or n3 == r14 or n3 == r15):
    mensaje = "\nEl jugador tiene mala suerte, no marcó ninguna casilla"
else:
    mensaje = "\nEl jugador marcó algún numero de la tarjeta"

#Resultados
print(mensaje)
