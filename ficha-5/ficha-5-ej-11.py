#Título
print("Calculo de Regularidad\n")

#Carga de datos
nota_1 = int(input("Carge la nota del 1º parcial: "))
nota_2 = int(input("Carge la nota del 2º parcial: "))
nota_3 = int(input("Carge la nota del TP: "))

#Procesos

if 0 > nota_1 > 10 or 0 > nota_2 > 10 or 0 > nota_2 > 10:
    input("\nERROR: Las notas cargadas no son válidas!")
else:
    prom = (nota_1 + nota_2 + nota_3) / 3

    if prom < 4:
        estado = "Libre"
    elif prom <= 8:
        estado = "Regular"
    else:
        estado = "Promocionado"

    print("\nCondición del alumno:", estado)
