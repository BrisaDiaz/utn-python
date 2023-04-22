#Título
print("Operaciones de orden con 3 nros\n")

#Carga de datos
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

#número mayor
may = n1
#número menor
min = n2
#número medio
med = n3

#Procesos

#ordenar números
if n2 > n1:
    may, min = n2, n1

if n3 > may:
    may, med = n3, may
elif n3 < min:
    min, med = n3, min

rta = print("\nNúmeros ordenados: ", "\n1)", may, "\n2)", med, "\n3)", min)

#calcular el resto de la divición de los dos primeros números
resto_primeros = may % med

if resto_primeros == min:
    print("\nEl tercero es el resto de la división de los dos primeros")
else:
    print("\nEl tercero NO es el resto de la división de los dos primeros")
