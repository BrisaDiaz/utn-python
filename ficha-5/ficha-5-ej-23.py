#Título
print("Triatlón del Ironman\n")

#Carga de datos
compet_1 = input("Ingrese el nombre del 1º competidor: ")
tiempo_1 = input("Ingrese el el tiempo del 1º competidor: ").strip()
compet_2 = input("Ingrese el nombre del 2º competidor: ")
tiempo_2 = input("Ingrese el el tiempo del 2º competidor: ").strip()
compet_3 = input("Ingrese el nombre del 3º competidor: ")
tiempo_3 = input("Ingrese el el tiempo del 3º competidor: ").strip()

#tiempo reloj de cada competidor a segundos
tiempo_1_s = int(tiempo_1[:2]) * 3600 + int(tiempo_1[3:5]) * 60 +\
             int(tiempo_1[6:])
tiempo_2_s = int(tiempo_2[:2]) * 3600 + int(tiempo_2[3:5]) * 60 +\
             int(tiempo_2[6:])
tiempo_3_s = int(tiempo_3[:2]) * 3600 + int(tiempo_3[3:5]) * 60 +\
             int(tiempo_3[6:])

#promedio de tiempo
total_s = tiempo_1_s + tiempo_2_s + tiempo_3_s
prom_total_s = total_s // 3

#tiempo promedio de segundos a horar, minutos y segundos
prom_h, resto_s = divmod(prom_total_s, 3600)
prom_m, prom_s = divmod(resto_s, 60)

#tiempo promedio en formato reloj
if prom_h < 10:
    prom_reloj = "0" + str(prom_h) + ":"
else:
    prom_reloj = str(prom_h) + ":"

if prom_m < 10:
    prom_reloj = "0" + prom_reloj + str(prom_m) + ":"
else:
    prom_reloj = prom_reloj + str(prom_m) + ":"

if prom_s < 10:
    prom_reloj = "0" + prom_reloj + str(prom_s)
else:
    prom_reloj = prom_reloj + str(prom_s)

print("\nTiempo promedio de la prueba: ", prom_reloj)

#orden por default
min_tiempo, puesto_1 = tiempo_1_s, compet_1
med_tiempo, puesto_2 = tiempo_2_s, compet_2
max_tiempo, puesto_3 = tiempo_3_s, compet_3

#comparar y reordenar
if tiempo_2_s < tiempo_1_s:
    min_tiempo, med_tiempo = tiempo_2_s, tiempo_1_s
    puesto_1, puesto_2 = compet_2, compet_1
if tiempo_3_s < min_tiempo:
    min_tiempo, med_tiempo, max_tiempo = tiempo_3_s, min_tiempo, med_tiempo
    puesto_1, puesto_2, puesto_3 = compet_3, puesto_1, puesto_2
elif tiempo_3_s < med_tiempo:
    med_tiempo, max_tiempo = tiempo_3_s, med_tiempo
    puesto_2, puesto_3 = compet_3, puesto_2

print("PODIUM:")
print("1ºPuesto:", puesto_1, "\n2ºPuesto:", puesto_2, "\n3ºPuesto:", puesto_3)

if min_tiempo > prom_total_s:
    print("El tiempo ganador fue superior al tiempo promedio de la prueba")
else:
    print("El tiempo ganador no fue superior al tiempo promedio de la prueba")