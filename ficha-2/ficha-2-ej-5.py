'''
5. Cálculo de ángulos
Se sabe que la suma de dos ángulos desconocidos (alfa + beta) es igual a cierto
valor x que se carga por teclado. Además se sabe que la diferencia entre esos
mismos dos ángulos (alfa - beta) es igual a otro valor y que también se carga
por teclado.Desarrolle un programa que dados los valores x e y, determine el
valor de los dos ángulos alfa y beta. No es necesario convertir a grados,
minutos y segundos el valor de cada ángulo: expréselos como números reales,
tal cual hayan sido obtenidos.
'''

#Título y carga de datos
print("Cálculo de ángulos\n")
x = float(input("Ingrese el valor de la variable x: "))
y = float(input("Ingrese el valor de la variable y: "))

#Procesos
'''
1) Despejamos alfa y obtenemos:
   alfa = x - beta
2) Sustituimos alfa en la segunda ecuación y obtenemos
   x - beta - beta = y
              beta = (y-x)/-2 
'''
beta = (y-x) / -2
alfa = x - beta

#Resultado
rta = f"\nValor del ángulo alfa: {alfa}\nValor del ángulo beta: {beta}"
print(rta.format(alfa, beta))