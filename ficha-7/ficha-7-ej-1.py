#Título
print("Ciclistas\n")

#Carga de datos
n_competidores = int(input("Ingrese el número de competidores: "))
record_previo = int(input("Ingrese el tiempo record anterior: "))
print()
suma_tiempo = 0
min_tiempo = ganador = None

for i in range(n_competidores):
    nombre = input("Ingrese el nombre del el competidor nº" +
                   str(i + 1) + ": ")
    tiempo = int(input("Ingrese su tiempo de carrera: "))

    #actualizar el competidor con menor tiempo
    if min_tiempo is None or tiempo < min_tiempo:
        min_tiempo = tiempo
        ganador = nombre

    suma_tiempo += tiempo

prom_tiempo = suma_tiempo / n_competidores

#Visualización de resultado
print("\nGanador de la carrera:", ganador)
print("Promedio de tiempo de los ciclistas:", prom_tiempo)

if record_previo > min_tiempo:
    print("El ciclista ganador impuso un nuevo tiempo record")
else:
    print("El ciclista no vatio el tiempo record")

