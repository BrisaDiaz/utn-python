'''
1. División con resto

 Plantear un script (directamente en el shell de Python) que permita informar,
 para dos valores a y b el resultado de la división a/b y el resto de esa divisón.
'''
#Ingreso de datos
a = float(input("ingresar el dividendo: "))
b = float(input("ingresar el divisor: "))

#Procesos
resultado = int(a/b)
resto= a%b

#Resultado
print("--------------------------")
rta = f"El resultado de la división entre {a} y {b} es: {resultado} y el resto es:{resto}"
print(rta.format(a,b, resultado))
