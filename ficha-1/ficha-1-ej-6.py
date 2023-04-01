'''
 6. Viaje Córdoba-Rosario

 Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista.
 La distancia aproximada entre ambas ciudades es de 400 kilómetros. El vehículo se desplaza con velocidad promedio de 122 km/h.
 Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Rosario.
 De nuevo, no es necesario convertir a horas, minutos y segundos:
 exprese en resultado como un número real, tal cual lo haya obtenido del cálculo.
'''
#Datos
DISTANCIA = 400
VELOCIDAD = 122

#Procesos
horas=  DISTANCIA / VELOCIDAD

#Resultado
rta = f"El minimo de horas que demora un vehículo a {VELOCIDAD}m/s en llegar a Rosario desde Córdoba es: {horas}horas"
print("--------------------------")
print(rta.format(VELOCIDAD,horas))