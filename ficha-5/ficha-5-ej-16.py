#Título
print("Raíces de un polinomio de segundo grado\n")

#Carga de datos
a = float(input("Ingrese el coeficiente del 1º término: "))
b = float(input("Ingrese el coeficiente del 2º término: "))
c = float(input("Ingrese el coeficiente del 3º término: "))

#Procesos
determinante = b**2 - 4*a*c

if determinante < 0:
    print("\nLas raíces del polinomio son imaginarias")
else:
    print("\nLas raíces del polinomio son reales")
    raiz_1 = (-b + pow(determinante, 0.5)) / a*2

    if determinante == 0:
        print("Raíces iguales:", raiz_1)
    else:
        raiz_2 = (-b - pow(determinante, 0.5)) / a*2
        print("Raíz 1:", raiz_1, "\tRaíz 2:", raiz_2)