#Título
print("Punto en el plano\n")

#Carga de datos
x = int(input("Ingrese las coordenada de x: "))
y = int(input("Ingrese las coordenada de y: "))

#Procesos

if x >= 0 and y >= 0:
    cuadrante = "1º"
elif x < 0 and y < 0:
    cuadrante = "3º"
elif x >= 0 and y < 0:
    cuadrante = "4º"
else:
    cuadrante = "2º"

print("\nEl punto se encuentra en el", cuadrante, "cuadrante")