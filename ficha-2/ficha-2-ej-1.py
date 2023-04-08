'''
1. Cuadrados y cubos
Leer dos números y calcular:

La suma de sus cuadrados.
El promedio de sus cubos.
'''

#Título y carga de datos
print("Cuadrados y cubos\n")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#Procesos
suma = pow(a, 2) + pow(b, 2)
prom = (pow(a, 3) + pow(b, 3))/2

#Resultado
rta= f"\nSuma de los cuadrados: {suma}\nPromedio de los cubos: {prom}"
print(rta.format(suma ,prom))