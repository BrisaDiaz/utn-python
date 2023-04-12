#Título
print("Edad mínima\n")

#Carga de datos
min_edad = int(input("Ingrese la edad mínima: "))
edad_1 = int(input("Ingresa la edad del participantes 1: "))
edad_2 = int(input("Ingresa la edad del participantes 2: "))
edad_3 = int(input("Ingresa la edad del participantes 3: "))

#Procesos


if edad_1 >= min_edad and edad_2 >= min_edad and edad_3 >= min_edad:
    mensaje = "\nTodos los participantes cumplen con la edad mínima"
else:
    mensaje = "\nNo todos los participantes cumplen con la edad mínima"

#Resultado
print(mensaje)