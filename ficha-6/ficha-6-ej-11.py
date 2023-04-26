#Título
print("Proceso de Discriminantes\n")

#Contadores
seguir = "s"
total = cant_imaginarios= cant_doble = cant_unico = 0

while seguir == "s":
    #Carga de datos
    discriminante = float(input("Ingrese un determinante: "))
    if discriminante < 0:
        cant_imaginarios += 1
    elif discriminante == 0:
        cant_unico += 1
    else:
        cant_doble += 1

    total += 1

    # Actualización de datos
    seguir = input("Desea continuar? (s/n): ").lower().strip()

porcentaje_imaginarios = cant_imaginarios * (100 / total)

print()
#visualización de resultados
print("Cantidad de discriminantes de 2 raíces:", cant_doble)
print("Cantidad de discriminantes de una única raíz:", cant_unico)
print("cantidad de discriminantes de raíces imaginarias:", cant_imaginarios)
print("Porcentaje de raíces imaginarias: %", porcentaje_imaginarios)