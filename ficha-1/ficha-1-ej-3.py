'''
3. Área de un triángulo
Desarrolle un programa para calcular el área de un triángulo, cargando
por teclado el valor de la base, pero sabiendo que su altura es igual
al cuadrado de la base. (Observar que la altura no es un dato... sólo se
indica la forma de calcularla de acuerdo a la base que sí es un dato).
'''

#Título y carga de datos
print("Área de un triángulo\n")
base = float(input("ingrese el valor de la base del triangulo: "))

#Procesos
altura = base**2
area = base * altura

#Resultado
rta = f"\nArea del triángulo: {area}"
print(rta.format(area))