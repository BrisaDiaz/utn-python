'''
1. División con resto
Plantear un script (directamente en el shell de Python) que permita informar,
para dos valores a y b el resultado de la división a/b y el resto de esa divisón.
'''

#Título y carga de datos
print("División con resto\n")
a = float(input("ingresar el dividendo: "))
b = float(input("ingresar el divisor: "))

#Procesos
resultado = int(a/b)
resto = a % b

#Resultado
rta = f"\nCociente de la división: {resultado}\nResto de la división: {resto}"
print(rta.format(a, b, resultado))
