#Título
print("Mantenimiento Informático\n")

#Constantes
CAUSAS = (1, 2)

menu_msg = "Ingrese la causa de mantenimiento:" \
           "\n1-Problema de Hardware\n2-Problema de Software\n..."
tiempo_msg = "Ingrese el tiempo de reparación en minutos: "

#Carga de datos
id_1 = int(input("Ingrese el id de la 1º pc: "))
tiempo_1 = int(input(tiempo_msg))
causa_1 = int(input(menu_msg))
id_2 = int(input("Ingrese el id de la 2º pc: "))
tiempo_2 = int(input(tiempo_msg))
causa_2 = int(input(menu_msg))
id_3 = int(input("Ingrese el id de la 3º pc: "))
tiempo_3 = int(input(tiempo_msg))
causa_3 = int(input(menu_msg))

#Procesos
if causa_1 in CAUSAS and causa_2 in CAUSAS and causa_3 in CAUSAS:
    tiempo_total = tiempo_1 + tiempo_2 + tiempo_3
    print("\nEl tiempo total de reparación es de: ", tiempo_total, "minutos")

    may_t = tiempo_1
    may_id = id_1

    if tiempo_2 > tiempo_1:
        may_t = tiempo_2
        may_id = id_2

    if tiempo_3 > may_t:
        may_t = tiempo_3
        may_id = id_3

    print("\nLa pc con mayor tiempo de mantenimiento es: ", may_id)

    tiempo_prom = tiempo_total / 3
    print("El tiempo promedio en tareas de mantenimiento es: ",
          tiempo_prom, "minutos")

    if causa_1 == 1 and causa_2 == 1 and causa_3 == 1:
        print("Todas las pc tuvieron problemas de hardware")
    else:
        print("No todas las pc tuvieron problemas de hardware")
else:
    print("ERROR: Se ingreso alguna causa de mantenimiento no valida!")
