#Título
print("Puntos en un plano\n")

#Carga de datos
numero = float(input("Ingrese un número (0 para salir): "))

#Inicializción de contadores, acumuladores y banderas
menor = numero
segundo_menor = may_negativo = None
suma_positivo = cant_positivo = promedio_positivos = 0

if numero > 0:
    suma_positivo += numero
    cant_positivo += 1
else:
    may_negativo = numero

while numero:
    numero = float(input("Ingrese un número (0 para salir): "))

    #comparar y actualizar menor y segundo menor
    if segundo_menor is None:
        segundo_menor = numero
    if numero < menor:
        menor, segundo_menor = numero, menor
    elif numero < segundo_menor:
        segundo_menor = numero

    #actualizar el mayor negativo
    if may_negativo is None or numero < 0 and numero < may_negativo:
        may_negativo = numero

    #contavilizar y sumar positivos
    if numero > 0:
        suma_positivo += numero
        cant_positivo += 1

#validar si no se ingreso nigún valor positivo
if cant_positivo != 0:
    promedio_positivos = suma_positivo / cant_positivo
if segundo_menor is None:
    segundo_menor = 0

#Visualización de resultados
print("\nSegundo menor número: ", segundo_menor)
print("Promedio de los números positivos:", promedio_positivos)
print("Mayor de los números negativos:", may_negativo)