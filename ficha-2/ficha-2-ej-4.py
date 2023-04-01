'''
4. Polinomio de segundo grado

Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado). Además, para el mismo polinomio,
calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.
'''

#Ingreso de datos
a = float(input("Ingrese el coeficiente a del polinomio: "))
b = float(input("Ingrese el coeficiente b del polinomio: "))
c = float(input("Ingrese el coeficiente c del polinomio: "))
x = float(input("Ingrese el valor de la variable x : "))

#Procesos
valorEnX = a*pow(x,2)+b*x+c
discriminante = pow(b,2)-4*a*c

#Resultado
rta = f"El valor del polinomio en el punto x:{x} es: {valorEnX}\nEl valor del discriminante es: {discriminante}"
print("--------------------------")
print(rta.format(x,valorEnX,discriminante))