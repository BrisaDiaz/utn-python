import random

##Constantes
OPCIONES = ("cara", "cruz")

#Título
print("Tirada de moneda\n")

#Carga de datos
selec = input("Ingrese su apuesta, cara o cruz (minuscula): ")

#Procesos
random = random.choice(OPCIONES)

if selec != OPCIONES[0] and selec != OPCIONES[1]:
    mensaje = "La opción seleccionada no es valida"
elif selec == random:
    mensaje = "Aserto su apuesta!"
else:
    mensaje = "No aserto su apuesta"

#Respuesta
print(mensaje)


