#Título
print("Ejercicio Estadística de Guardería Náutica\n")

#Constantes

# (1 si es velero, 2 si es lancha)
TIPOS = 1, 2
MESES_X_AÑO = 12

#Carga de datos
cant_barcos = int(input("Ingrese la cantidad de barcos: "))

total_anual_1 = total_anual_2 = total_cuotas = cuotas_1 = cuotas_2 = 0
may_1 = may_cuota_1 = None

for i in range(1, cant_barcos + 1):
    nombre = input("Ingrese el nombre del barco nº" + str(i) + ": ")
    tipo = int(input("Ingrese el tipo (1 si es velero, 2 si es lancha): "))

    #validar tipo de barco
    while not (tipo in TIPOS):
        print("Error: Tipo de barco no válido")
        tipo = int(input("Ingrese el tipo (1 si es velero, 2 si es lancha): "))

    cuota = float(input("Ingrese el monto mensual a pagar por guardería: "))

    if tipo == 1:
        total_anual_1 += cuota * MESES_X_AÑO
        cuotas_1 += cuota
        if may_1 is None or cuota > may_cuota_1:
            may_cuota_1 = cuota
            may_1 = nombre
    else:
        total_anual_2 += cuota * MESES_X_AÑO
        cuotas_2 += cuota

total_cuotas += cuotas_1 + cuotas_2
cuota_promedio = total_cuotas / cant_barcos

#visualización de datos
print("\nTotal anual aportado por los veleros: $", total_anual_1)
print("Total anual aportado por las lanchas: $", total_anual_2)
print("Velero con mayor cuota de guardería:" + may_1 + " $", may_cuota_1)
print("Valor promedio de cuotas de guardería: $", cuota_promedio)