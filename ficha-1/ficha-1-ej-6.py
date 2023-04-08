'''
 6. Viaje Córdoba-Rosario

 Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista.
 La distancia aproximada entre ambas ciudades es de 400 kilómetros. El vehículo se desplaza con velocidad promedio de 122 km/h.
 Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Rosario.
 De nuevo, no es necesario convertir a horas, minutos y segundos:
 exprese en resultado como un número real, tal cual lo haya obtenido del cálculo.
'''
#Título
print("Viaje Córdoba-Rosario\n")

#Declaración de constantes
DISTANCIA = 400
VELOCIDAD = 122

#Procesos
horas =  DISTANCIA / VELOCIDAD

#Resultado
rta = f"\nEl minimo de horas que demorará el vehículo: {horas}"
print(rta.format(VELOCIDAD, horas))