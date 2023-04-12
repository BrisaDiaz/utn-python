#Título y carga de datos
print("Temperatura diaria\n")

temp_1 = float(input("Ingrese la primer temperatura: "))
temp_2 = float(input("Ingrese la segunda temperatura: "))
temp_3 = float(input("Ingrese la tercer temperatura: "))

#Procesos
prom = (temp_1 + temp_2 + temp_3 ) / 3

if temp_1 > prom or temp_2 > prom or temp_3 > prom:
    mensaje = "\nExiste al menos una temperatura mayor a la promedio"
else:
    mensaje = "\nNo existe alguna temperatura mayor a la promedio"

#Resultados
print(mensaje)
