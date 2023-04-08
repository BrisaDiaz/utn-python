'''
9. Datos de un rectángulo

Hacer un programa que tome como entrada el ancho y el alto de un rectángulo
y determine el perímetro y la superficie del mismo.
'''

#Título y carga de datos
print("Datos de un rectángulo\n")
ancho = float(input("Ingrese el ancho del largo del rectángulo: "))
alto = float(input("Ingrese el alto del largo del rectángulo: "))

#Procesos
perímetro = 2*ancho+2*alto
superficie = ancho * alto

#Resultado
rta=f"\nEl perímetro es: {perímetro} \nLa superficie es: {superficie}"
print(rta.format(perímetro, superficie))

