#Título
print("Postulantes a un empleo\n")

#Carga de datos
cant_preguntas = int(input("Ingrese el número de preguntas realizadas: "))
postulante_1 = input("Ingrese el nombre del 1º postulante: ")
nro_correcta_1 = int(input("Ingrese la cantidad de respuestas correctas: "))
postulante_2 = input("Ingrese el nombre del 2º postulante: ")
nro_correcta_2 = int(input("Ingrese la cantidad de respuestas correctas: "))
postulante_3 = input("Ingrese el nombre del 3º postulante: ")
nro_correcta_3 = int(input("Ingrese la cantidad de respuestas correctas: "))
print("")

#Procesos
porcent_1 = nro_correcta_1 * (100/cant_preguntas)
porcent_2 = nro_correcta_2 * (100/cant_preguntas)
porcent_3 = nro_correcta_3 * (100/cant_preguntas)

if porcent_1 >= 90:
        nivel_1 = "Nivel Superior"
elif 75 <= porcent_1 < 90:
        nivel_1 = "Nivel Medio"
elif 50 <= porcent_1 < 75:
        nivel_1 = "Nivel Regular"
else:
        nivel_1 = "Fuera de Nivel"

if porcent_1 >= 90:
        nivel_2 = "Nivel Superior"
elif 75 <= porcent_2 < 90:
        nivel_2 = "Nivel Medio"
elif 50 <= porcent_2 < 75:
        nivel_2 = "Nivel Regular"
else:
        nivel_2 = "Fuera de Nivel"

if porcent_3 >= 90:
        nivel_3 = "Nivel Superior"
elif 75 <= porcent_3 < 90:
        nivel_3 = "Nivel Medio"
elif 50 <= porcent_3 < 75:
        nivel_3 = "Nivel Regular"
else:
        nivel_3 = "Fuera de Nivel"

print(postulante_1 + ": ", nivel_1)
print(postulante_2 + ": ", nivel_2)
print(postulante_3 + ": ", nivel_3)

max_porcent = max(porcent_1, porcent_2, porcent_3)
ganador = postulante_1

if max_porcent == porcent_2:
    ganador = postulante_2
elif max_porcent == porcent_3:
    ganador = postulante_3

    print("\nGanador del puesto:", ganador)