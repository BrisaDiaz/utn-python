'''
13. Triángulo Rectángulo
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

Valor de la hipotenusa (redondeado a 2 decimales)
Valor del lado mayor
Valor del lado menor
'''

#Título y carga de datos
print("Triángulo Rectángulo\n")
cateto1 = float(input("Ingrese el valor del catato 1: "))
cateto2 = float(input("Ingrese el valor del catato 2: "))

#Procesos
hipotenusa = round((pow(cateto1, 2) + pow(cateto2, 2))**0.5, 2)
lado_mayor = max(cateto1, cateto2)
lado_menor = min(cateto1, cateto2)

#resultados
linea1 = f"\nLa hipotenusa es: {hipotenusa}"
linea2 = f"\nEl lado mayor es: {lado_mayor}\nEl lado menor es: {lado_menor}"
print(linea1.format(hipotenusa), linea2.format(lado_menor, lado_mayor))
