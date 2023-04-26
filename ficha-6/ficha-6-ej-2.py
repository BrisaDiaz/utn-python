#Título
print("Ventas por sucursal\n")

#Carga de datos
cant_ventas = int(input("Ingrese la cantidad de ventas: "))
print()

total_ventas = rango_1 = unid_1 = unid_2 = unid_3 = 0
inf_band = False

while cant_ventas >= 0:
    print("Cantidad de ventas: ", cant_ventas)
    total_ventas += cant_ventas
    if 300 >= cant_ventas >= 100:
        rango_1 += 1
    elif cant_ventas < 50:
        inf_band = True
    elif cant_ventas == 600:
        unid_1 += 1
    elif cant_ventas == 500:
        unid_2 += 1
    elif cant_ventas == 400:
        unid_3 += 1

    # Actualización de datos
    cant_ventas = int(input("Ingrese la cantidad de ventas: "))

#Visualización de datos
print("Total de ventas:", total_ventas)
print("Cantidad de ventas entre 100 y 300 unidades:", rango_1)
print("Cantidad de ventas con 600 unidades:", unid_1)
print("Cantidad de ventas con 500 unidades:", unid_2)
print("Cantidad de ventas con 400 unidades:", unid_3)

if inf_band:
    print("Hubo alguna cantidad de ventas inferior a 50 unidades")
else:
    print("No hubo alguna cantidad de ventas inferior a 50 unidades")