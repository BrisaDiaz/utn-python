#Título
print("Premio por Ventas\n")
PORCENTAJE_COMICION = 0.5
PLUS_MIN_MONTO = 1001
PORCENTAJE_PLUS = 0.10

#Carga de datos
monto_1 = float(input("Ingrese el monto vendido en el 1º mes: "))
monto_2 = float(input("Ingrese el monto vendido en el 2º mes: "))
monto_3 = float(input("Ingrese el monto vendido en el 3º mes: "))

#proceso

min_monto = min(monto_1, monto_2, monto_3)

premio = min_monto * PORCENTAJE_COMICION

if monto_1 >= PLUS_MIN_MONTO and monto_2 >= PLUS_MIN_MONTO \
   and monto_3 >= PLUS_MIN_MONTO:

    premio += premio * PORCENTAJE_PLUS

print("\nMonto del premio: $" + str(premio))
