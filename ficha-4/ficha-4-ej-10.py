#Título
print("Terreno\n")

#Carga de datos
frente = float(input("Ingresa la medida de frente del terreno: "))
fondo = float(input("Ingresa la medida de fondo del terreno: "))

#Procesos
es_cuadrado = frente == fondo
sup = frente * fondo

if es_cuadrado:
    forma = "\nEs un terreno cuadrado"
else:
    forma = "\nEs un terreno rectangular"

mensaje = f"{forma} y posee una superficie de {sup} mt2"

#Resultado
print(mensaje)