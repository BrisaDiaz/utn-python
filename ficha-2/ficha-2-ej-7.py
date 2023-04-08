'''
7. Votación en el Congreso

En el Congreso se vota la sanción de una ley muy importante.
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.
'''

#Título y carga de datos
print("Votación en el Congreso\n")
cantidadAFavor = int(input("Ingrese la cantidad de votos a favor de la sanción: "))
cantidadEnContra = int(input("Ingrese la cantidad de votos en contra de la sanción: "))

#Procesos
totalDeVotos = cantidadAFavor+cantidadEnContra
porcentajeAFavor = (cantidadAFavor/totalDeVotos) * 100
porcentajeEnContra = (cantidadEnContra/totalDeVotos) * 100

#Resultado
linea1 = f"\nEl porcentaje de votas a favor es: {porcentajeAFavor}%"
linea2 = f"\nEl porcentaje de votas en contra es: {porcentajeEnContra}%"
print(linea1.format(porcentajeAFavor), linea2.format(porcentajeEnContra))
