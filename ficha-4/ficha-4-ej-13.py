#Título
print("Calculo de Precios con Descuento\n")

#Constantes
DESC_EFECT = 0.05
UNI_X_MAYOR = 10
DESC_EFECT_X_MAYOR = 0.15

#Datos
precio_uni = float(input("Ingrese el precio unitario: "))
cant = int(input("Ingrese la cantidad de unidades: "))
efectivo = input("Se paga en efectivo? (si/no): ")

#Procesos
precio_bruto = precio_uni * cant
descuento = 0

if efectivo == "si" and cant > UNI_X_MAYOR:
    descuento = precio_bruto * DESC_EFECT_X_MAYOR
elif efectivo == "si":
    descuento = precio_bruto * DESC_EFECT

#Resultados
print("\nPrecio sin descuento: $", precio_bruto, "\nDescuento: $", descuento)