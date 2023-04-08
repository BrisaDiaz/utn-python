'''
2. Cuadrado de un binomio
Un binomio al  cuadrado (suma) es igual al cuadrado del primer término,
más el doble producto del primero por el segundo más el cuadrado del segundo.
Plantear un script directamente en el shell de Python, que permita mostrar,
para dos valores a y b,el valor del cuadrado del binomio.
'''

#Título y carga de datos
print("Cuadrado de un binomio\n")
a = float(input("ingresar el primer elemento del binomio: "))
b = float(input("ingresar el segundo elemento del binomio: "))

#Procesos
resultado = a**2 + 2*a*b + b**2

#Resultado
rta = f"\nValor del cuadrado perfecto de ({a} + {b}): {resultado}"
print(rta.format(a, b, resultado))
