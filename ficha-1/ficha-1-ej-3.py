'''
3. Área de un triángulo

 Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura
 es igual al cuadrado de la base. (Observar que la altura no es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).
'''
#Ingreso de datos
#Procesos
#Resultado
base = float(input("ingrese el valor de la base del triangulo: "))
altura= round(base**2,1)
print("--------------------------")
area = base * altura
rta = f"El area del triángulo de base {base} vale: {area:.1f}"
print(rta.format(base,area) )