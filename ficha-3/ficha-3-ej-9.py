'''
9. Costos del Proyecto
Una pequeña empresa de informática tiene que desarrollar un sistema de
información y para ello tiene un presupuesto de x pesos para cubrir
los costos de crear el sistema. Sabiendo que tiene pensado ganar al
menos 17% por el proyecto, determine cuál es el valor máximo que pueden
alcanzar los costos del proyecto.
'''

#Título y carga de datos
print("Costos del Proyecto\n")
presupuesto = float(input("Ingrese el presupuesto del proyecto: "))

#Declaración de constantes
PORC_GANANCIA = 17

#Procesos
ganancia = presupuesto * (PORC_GANANCIA / 100)
costos_max = presupuesto - ganancia

#resultados
rta = f"\nEl valor máximo que pueden alcanzar los costos es: ${costos_max}"
print(rta.format(costos_max))