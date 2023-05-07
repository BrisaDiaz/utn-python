#Título
print("Secuencia numérica II\n")

total = multiplo_6 = suma_multiplo_6 = div_anterior = cant_secuencia = 0
anterior = None
secuencia_impar = ()

n = float(input("Ingrese un número (0 para finalizar): "))

while n != 0:
    if n % 6 == 0:
        multiplo_6 += 1
        suma_multiplo_6 += n

    # verificar divisibilidad exacta por el anterior valor
    if not anterior is None and anterior % n == 0:
        div_anterior += 1

    if n % 2 == 1:
        if len(secuencia_impar) == 0:
            # inicializar la secuencia
            secuencia_impar = (n,)
        elif n > secuencia_impar[-1]:
            # concatenar a la secuencia solo números acendentes
                secuencia_impar += (n,)
        else:
            if len(secuencia_impar) > 2:
                # verificar si existía una secuencia igual a mayor a 3
                # cuando se ingreso un número no acendente
                cant_secuencia += 1
            # reiniciar la secuencia
            secuencia_impar = ()
    else:
        if len(secuencia_impar) > 2:
            # verificar si existía una secuencia igual a mayor a 3
            # cuando se ingreso un número par
            cant_secuencia += 1
        # reiniciar la secuencia
        secuencia_impar = ()

    # actualizar el valor del anterior
    anterior = n

    n = float(input("Ingrese un número (0 para finalizar): "))
else:
    # verificar si existía una secuencia igual a mayor a 3
    # cuando se ingreso 0
    if len(secuencia_impar) > 2:
        cant_secuencia += 1

print()
if multiplo_6:
    prom = suma_multiplo_6 / suma_multiplo_6
    print("Promedio de los valores múltiplo de 6:", prom)
else:
    print("No se ingreso ningún valor múltiplo de 6")

print("Cantidad de números que son divisor exacto del anterior: ",
      div_anterior)
print("Cantidad de veces que se generó una secuencia ascendente de"
      " 3 o más números impares:", cant_secuencia)