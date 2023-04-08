'''
10. Tiempos de Triatlon
Un triatlón es una competición deportiva en que los participantes realizan
tres carreras: una de natación, una ciclista y una pedestre.
Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos)
logrados en cada etapa por uno de los deportistas participantes.

Con esos datos determinar:

Tiempo total de la prueba (en formato hh:mm:ss)
Tiempo máximo y mínimo (en segundos)
Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones
'''

#Título y carga de datos
print("Tiempos de Triatlon\n")
tiempo_nat = input("Ingrese el tiempo logrado en natación: ")
tiempo_cic = input("Ingrese el tiempo logrado en ciclismo: ")
tiempo_ped = input("Ingrese el tiempo logrado en carrera de fondo: ")

#Declaración de constantes
SEGUNDOS_X_HORA = 3600
SEGUNDOS_X_MINUTO = 60

#Procesos
m_nat, s_nat = int(tiempo_nat[:2]), int(tiempo_nat[3:5])
m_cic, s_cic = int(tiempo_cic[:2]), int(tiempo_cic[3:5])
m_ped, s_ped = int(tiempo_ped[:2]), int(tiempo_ped[3:5])

nat_total_s = m_nat*60 + s_nat
cic_total_s = m_cic*60 + s_cic
ped_total_s = m_ped*60 + s_ped

tiempo_total_s = nat_total_s + cic_total_s + ped_total_s

tiempo_max = max(nat_total_s, cic_total_s, ped_total_s)
tiempo_min = min(nat_total_s, cic_total_s, ped_total_s)

tiempo_prom = round(tiempo_total_s/3, 2)

horas, resto_h = divmod(tiempo_total_s,SEGUNDOS_X_HORA)
minutos, segundos = divmod(resto_h,SEGUNDOS_X_MINUTO)

#resultados
a = f"\nTiempo total de la prueba: {horas}:{minutos}:{segundos}"
b = f"Tiempo máximo: {tiempo_max}s\nTiempo mínimo: {tiempo_min}s"
c = f"Tiempo promedio: {tiempo_prom}s"

print(a.format(horas, minutos, segundos))
print(b.format(tiempo_max, tiempo_min))
print(c.format(tiempo_prom))
