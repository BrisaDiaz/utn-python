'''
7. Votación en el Congreso

En el Congreso se vota la sanción de una ley muy importante.
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.
'''
#Ingreso de datos
cantidadAFavor= float(input("Ingrese la cantidad de votos a favor de la sanción: "))
cantidadEnContra= float(input("Ingrese la cantidad de votos en contra de la sanción: "))

#Procesos
totalDeVotos= cantidadAFavor+cantidadEnContra
porcentajeAFavor=(cantidadAFavor/totalDeVotos)*100
porcentajeEnContra=(cantidadEnContra/totalDeVotos)*100

#Resultado
rta= f"El porcentaje de votas a favor es: {porcentajeAFavor}%\nEl porcentaje de votas en contra es: {porcentajeEnContra}%"
print("--------------------------")
print(rta.format(porcentajeAFavor,porcentajeEnContra))
