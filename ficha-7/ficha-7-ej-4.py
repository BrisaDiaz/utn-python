import random

#Título
print("Decimal a Hexadecimal\n")

#Constantes
RANGO = 5000, 450000
BASE_HEXADECIMAL = 16

#Carga de datos
cantidad = int(input("Cuantos números hexadecimales que desea generar?: "))

for i in range(cantidad):
    decimal = random.randint(*RANGO)
    hexa = hex(decimal)

    print("\nDecimal:", decimal, "\t", "Hexadecimal:", hexa)