'''
4. Duración de un vuelo
Desarrollar un programa que, conociendo el horario de partida y llegada de un
vuelo (hora y minutos), determine cuál es su duración en minutos. Si el viajero
necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado,
¿a qué hora llegara al mismo?
'''

#Título y carga de datos
print("Duración de un vuelo\n")

'''Un formato aceptable de horario es = hh:mm
El separador entre horas y minutos debe ser de solo 1 dígito'''

horario_partida = input("Ingrese el horario de partida: ")
horario_llegada = input("Ingrese el horario de llegada: ")

#Asignación de constantes
MINUTOS_AL_HOTEL = 45
MINUTOS_X_HORA = 60

#Procesos
h_partida, m_partida = int(horario_partida[:2]),int( horario_partida[-2:])
h_llegada, m_llegada = int(horario_llegada[:2]),int( horario_llegada[-2:])

h_de_vuelo = h_llegada - h_partida
m_de_vuelo = m_llegada - m_partida

h_a_m_de_vuelo = h_de_vuelo * MINUTOS_X_HORA
m_total_de_vuelo = h_a_m_de_vuelo + m_de_vuelo

h_de_mas, m_de_mas = divmod(m_llegada + MINUTOS_AL_HOTEL, 60)

horario_final_h, horario_final_m = h_llegada + h_de_mas, m_de_mas

#Resultados
rta = f"\nLa duración del vuelo es de: {m_total_de_vuelo} minutos"
rta2 = f"El horario de llegada al hotel es: {horario_final_h}:{horario_final_m}"
print(rta.format(m_total_de_vuelo))
print( rta2.format(horario_final_h, horario_final_m))