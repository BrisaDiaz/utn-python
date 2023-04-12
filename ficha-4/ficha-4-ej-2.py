#Título y carga de datos
print("Suma - División - Potencia\n")

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el primer segundo: "))
n3 = float(input("Ingrese el primer tercer: "))

#Procesos
suma = n1 + n2 + n3

if suma > 10:
    resultado = round(suma / 2)
else:
    resultado = pow(suma, 3)

#Resultados
print("\nEl resultado es: ", resultado)