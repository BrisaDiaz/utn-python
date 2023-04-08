'''
12. Calculo de Posta de Natacion
En la disciplina olímpica una de las pruebas mas esperadas en la natacion es
la posta 4x100. En esta disciplina el equipo ganador registró los siguientes
tiempos en cada estilo:

Espalda: 52 segundos 15 centésimas.
Pecho: 1 minuto 2 segundos 75 centésimas.
Mariposa: 59 segundos 80 centésimas.
Libre: 48 segundos 15 centésimas.
Usted debe averiguar el tiempo total de la carrera del equipo ganador
y representarlo en minutos, segundos y centésimas.


Para recordar:

1 minutos son 60 segundos.
1 segundo son 100 centesimas.
'''

#Título y carga de datos
print("Calculo de Posta de Natación\n")

#Asignación de constantes
SEGUNDOS_X_MINUTO = 60
CENTESIMAS_x_SEGUNDO = 100

TIEMPO_ESPALDA = 0, 52, 15
TIEMPO_PECHO = 1, 2, 75
TIEMPO_MARIPOSA = 0, 59, 80
TIEMPO_LIBRE = 0, 48, 15

#Procesos
suma_m = TIEMPO_ESPALDA[0] + TIEMPO_PECHO[0] + TIEMPO_MARIPOSA[0] + TIEMPO_LIBRE[0]
suma_s = TIEMPO_ESPALDA[1] + TIEMPO_PECHO[1] + TIEMPO_MARIPOSA[1] + TIEMPO_LIBRE[1]
suma_c = TIEMPO_ESPALDA[2] + TIEMPO_PECHO[2] + TIEMPO_MARIPOSA[2] + TIEMPO_LIBRE[2]

centecimas_x_minuto = SEGUNDOS_X_MINUTO * CENTESIMAS_x_SEGUNDO

total_c = suma_c + (suma_s*CENTESIMAS_x_SEGUNDO) + (suma_m*centecimas_x_minuto)

minutos, resto = divmod(total_c, centecimas_x_minuto)
segundos, centecimas = divmod(resto, CENTESIMAS_x_SEGUNDO)

#resultados
rta = f"\nEl tiempo total de la carrera es: {minutos}:{segundos}:{centecimas}"
print(rta.format(minutos, segundos, centecimas))
