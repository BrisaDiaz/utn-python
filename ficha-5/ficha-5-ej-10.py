import random

#Título
print("Impuesto Automotor\n")

#Constantes
TIPOS = ("P", "T", "R")
PAGO_MENOS_10_ANTIGUEDAD_P = 200
PAGO_ENTRE_10_20_ANTIGUADAD_P = 150
PAGO_MAS_20_ANTIGUEDAD_P = 0
PAGO_X_LICENCIA_T = 150
PAGO_X_ANTIGUEDAD_R = 100
A_ACUAL = 2023

#Carga de datos
modelo = int(input("Ingrese el modelo del vihículo: "))
print("Ingrese el tipo de vehículo:")
tipo = input("P:Particular\tT:Taxi\t\tR:Remis\n...").upper()

#procesos
antiguedad = A_ACUAL - modelo

if not tipo in TIPOS:
    print("\nERROR: Tipo de vehículo no válido!")
elif antiguedad < 0:
    print("\nERROR: Modelo de vehículo no válido!")
else:
    if tipo == "R":
        inpuesto = antiguedad * PAGO_X_ANTIGUEDAD_R
    elif antiguedad < 10:
        inpuesto = antiguedad * PAGO_MENOS_10_ANTIGUEDAD_P
    elif antiguedad <= 20:
        inpuesto = antiguedad * PAGO_ENTRE_10_20_ANTIGUADAD_P
    else:
        inpuesto = antiguedad * PAGO_MAS_20_ANTIGUEDAD_P
    if tipo == "T":
        inpuesto += PAGO_X_LICENCIA_T

    print("\nMonto a pagar en impuestos: $" + str(inpuesto))


