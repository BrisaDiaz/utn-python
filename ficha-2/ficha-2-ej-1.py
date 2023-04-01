'''
1. Cuadrados y cubos
Leer dos números y calcular:

La suma de sus cuadrados.
El promedio de sus cubos.
'''

#Ingreso de datos
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#Procesos
suma= pow(a,2)+pow(b,2)
prom= (pow(a,3)+pow(b,3))/2

#Resultado
rta= f"La suma de los cuadrados es: {suma}\nEl promedio de los cubos es: {prom}"
print("--------------------------")
print(rta.format(suma,prom))