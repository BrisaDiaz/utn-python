#Título
print("Menú de Opciones Básico\n")

#Constantes
MENU = "Seleccione una de las siguientes opciones:" \
       "\n1-Superficie del triángulo\n2-Perímetro del triángulo" \
       "\n3-Longitud del lado menor\n..."
OPCIONES = (1, 2, 3)


#Carga de datos
l_a = int(input("Ingrese el valor de lado A del triángulo: "))
l_b = int(input("Ingrese el valor de lado B del triángulo: "))
l_c = int(input("Ingrese el valor de lado C del triángulo: "))

opcion = int(input(MENU))

if opcion in OPCIONES:
    perimetro = l_a + l_b + l_c
    if opcion == 1:
        s = perimetro / 2
        sup = pow(s * (s - l_a) * (s - l_b) * (s - l_c), 0.5)
        print("\nLa superficie del triángulo es:", sup)
    elif opcion == 2:
        print("\nEl perímetro del triangulo es:", perimetro)
    else:
        l_may = max(l_a, l_b, l_c)
        print("\nLa medida del lado mayor es:", l_may)
else:
    print("\nERROR: La opción ingresada no es válida!")