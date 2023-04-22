#Título
print("Comercio\n")

#Carga de datos
ventas_1 = int(input("Ingrese la cantidad vendida del 1º product:"))
precio_1 = float(input("Ingrese su precio unitario: "))
ventas_2 = int(input("Ingrese la cantidad vendida del 2º product:"))
precio_2 = float(input("Ingrese su precio unitario: "))
ventas_3 = int(input("Ingrese la cantidad vendida del 3º product:"))
precio_3 = float(input("Ingrese su precio unitario: "))

ingreso_1, ingreso_2 = ventas_1 * precio_1, ventas_2 * precio_2
ingreso_3 = ventas_3 * precio_3

may_ingreso = ingreso_1
may_producto = "1º"

if ingreso_2 > ingreso_1:
    may_ingreso = ingreso_2
    may_producto = "2º"

if ingreso_3 > may_ingreso:
    may_ingreso = ingreso_3
    may_producto = "3º"

ingreso_total = ingreso_1 + ingreso_2 + ingreso_3

may_porcentaje = may_ingreso * (100 / ingreso_total)

print("\nEl producto que registro mayor ingresos es el", may_producto)
print("Porcentaje sobre los ingresos absolutos:", str(may_porcentaje) + "%")