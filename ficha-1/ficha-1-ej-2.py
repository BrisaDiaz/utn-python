'''
2. Cuadrado de un binomio

 Un binomio al  cuadrado (suma) es igual al cuadrado del primer término,
 más el doble producto del primero por el segundo más el cuadrado del segundo.

 Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b,
 el valor del cuadrado del binomio.
'''
#Ingreso de datos
a = float(input("ingresar la primer variable del binomio: "))
b = float(input("ingresar el segundo variable del binomio: "))

#Procesos
resultado = round(a**2+2*a*b+b**2,1)

#Resultado
print("--------------------------")
rta =f"El resultado del binomio cuadrado perfecto de ({a} + {b}) es {resultado}"
print(rta.format(a,b,resultado))
