#Título
print("Institución Educativa\n")

#Carga de datos
id_1 = input("Ingrese el código de identificación del 1º curso: ")
cant_1 = input("Ingrese la cantidad de niños-niñas: ")
id_2 = input("Ingrese el código de identificación del 2º curso: ")
cant_2 = input("Ingrese la cantidad de niños-niñas: ")
id_3 = input("Ingrese el código de identificación del 3º curso: ")
cant_3 = input("Ingrese la cantidad de niños-niñas: ")
cupo = int(input("Ingrese el cupo máximo de alumnos por curso: "))

#Procesos
cant_m_1 = int(cant_1[:cant_1.index("-")])
cant_f_1 = int(cant_1[cant_1.index("-")+1:])
cant_m_2 = int(cant_2[:cant_2.index("-")])
cant_f_2 = int(cant_2[cant_2.index("-")+1:])
cant_m_3 = int(cant_3[:cant_3.index("-")])
cant_f_3 = int(cant_3[cant_3.index("-")+1:])

total_1 = cant_f_1 + cant_m_1
total_2 = cant_f_1 + cant_m_2
total_3 = cant_f_3 + cant_m_3

#Buscar el que tiene menos alumnos
min_cant = total_1
min_id = id_1

if total_2 < total_1:
    min_cant, min_id = total_2, id_2

if total_3 < min_cant:
    min_cant, min_id = total_3, id_3

print("\nEl curso con menor cantidad de alumnos es:", min_id)

#calcular porcentajes de niñas
porc_f_1 = cant_f_1 * (100 / total_1)
porc_f_2 = cant_f_2 * (100 / total_2)
porc_f_3 = cant_f_3 * (100 / total_3)

print("\nPorcentaje de niñas por curso:")
rta = f"{id_1}: {porc_f_1}%\n{id_2}: {porc_f_2}%\n{id_3}: {porc_f_3}%"
print(rta.format(id_1, porc_f_1, id_2, porc_f_2, id_3, porc_f_3))

#calcular porcentajes de niños
porc_m_1 = 100 - porc_f_1
porc_m_2 = 100 - porc_f_2
porc_m_3 = 100 - porc_f_3

print("\nPorcentaje de niños por curso:")
rta = f"{id_1}: {porc_m_1}%\n{id_2}: {porc_m_2}%\n{id_3}: {porc_m_3}%"
print(rta.format(id_1, porc_m_1, id_2, porc_m_2, id_3, porc_m_3))

#calcular promedio de alumnos por curso
prom = (total_1 + total_2 + total_3) / 3
print("\nEl promedio general de alumnos es de:", prom)

#verificar si se supero el cupo
if total_1 > cupo or total_2 > cupo or total_3 > cupo:
    print("\nEl cupo de alumnos fue superado,"
          "es necesaria la apertura de una nueva división")