#Título
print("Secuencia de impares\n")

#Carga de datos
a = int(input("Ingrese la cota menor del rango: "))
b = int(input("Ingrese la cota mayor del rango: "))

#ordenar cotas
if a > b:
    a, b = b, a

print("\nNúmeros pares de menor a mayor entre:", a, "y", b)
#generar número de 2 en 2 desde el primer par al último
for i in range(a + (a % 2), b + 1, 2):
        print(i)
#generar número de 2 en 2 desde el último par al primero
print("Números pares de mayor a menor entre:", a, "y", b)
for i in range(b - (b % 2), a - 1, -2):
    print(i)

