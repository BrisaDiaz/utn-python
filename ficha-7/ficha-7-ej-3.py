#Título
print("Sueldos y aguinaldo\n")

#Constantes
CANTIDAD_DE_MESES_EN_UN_SEMESTRE = 6
MESES_DEL_SEMESTRE1 = "Enero", "Febrero", "Marzo", "Abril", "Junio", "Julio"

may_sueldo = min_sueldo = None
min_mes, suma_sueldos = 1, 0


for i in range(CANTIDAD_DE_MESES_EN_UN_SEMESTRE):
    #obtener el mes correspondiente
    mes = MESES_DEL_SEMESTRE1[i]
    sueldo = float(input("Ingrese el sueldo de " + mes + ": "))
    #actualizar el mayor sueldo
    if may_sueldo is None or sueldo > may_sueldo:
        may_sueldo = sueldo
    #actualizar el menor sueldo
    if min_sueldo is None or sueldo < min_sueldo:
        min_sueldo = sueldo
        min_mes = mes
    #agregar sueldo al total
    suma_sueldos += sueldo

aguinaldo = may_sueldo / 2
sueldo_promedio = suma_sueldos / CANTIDAD_DE_MESES_EN_UN_SEMESTRE


print("\nMonto del aguinaldo: $", aguinaldo)
print("Mes con menor sueldo:", min_mes)
print("Sueldo promedio del semestre:", sueldo_promedio)