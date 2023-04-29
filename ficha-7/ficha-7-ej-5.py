#Título
print("Números Enteros\n")

#Carga de datos
cant = int(input("Ingrese la cantidad de coordenadas que desea cargar: "))
may_punto = None
cant_cuadrante_1_0_3 = 0

for i in range(1, cant + 1):
    coordenadas = input("Ingrese las coordenada en x e y del punto "
                        + str(i) + ": ").split(" ")
    x, y = float(coordenadas[0]), float(coordenadas[1])

    if x >= 0:
        if y >= 0:
            cuadrante = "1º cuadrante"
            cant_cuadrante_1_0_3 += 1
        else:
            cuadrante = "4º cuadrante"
    elif y >= 0:
        cuadrante = "2º cuadrante"
    else:
        cuadrante = "3º cuadrante"
        cant_cuadrante_1_0_3 += 1

    print("Cuadrante del punto:", cuadrante)

    if may_punto is None:
        may_punto = (x, y)
    else:
        #comparar la distancia del punto con respecto al eje
        hipotenusa_punto = pow(x**2 + y**2, 0.5)
        hipotenusa_may_punto = pow(may_punto[0]**2 + may_punto[1]**2, 0.5)

        if hipotenusa_punto > hipotenusa_may_punto:
            may_punto = (x, y)


print("\nCantidad de puntos que se encuentran en el 1º o 3º cuadrante:",
      cant_cuadrante_1_0_3)

print("Punto a mayor distancia del origen de coordenadas:", may_punto)