
#Título
print("Secuencia numérica\n")

num = float(input("Ingrese un número (0 para finalizar): "))
total = porc = div_3 = cuadrados = 0
anterior = may_impar = None

while num != 0:
       total = 1
       #verificar divisibilidad por 3
       if num % 3 == 0:
              div_3 += 1

       #verificar si es cuadrado del número anterior
       if not anterior is None and num == anterior**2:
              cuadrados += 1

       #reasignar número anterior
       anterior = num

       #verificar y reasignar el mayor impar
       if num % 2 == 1 and (may_impar is None or num > may_impar):
              may_impar = num

       num = float(input("Ingrese un número (0 para finalizar): "))

if total:
       porc = div_3 / (100 / total)

print("\nEl porcentaje de los números divisibles por 3 es: %", porc)
print("Cantidad de números que son cuadrados del anterior:", cuadrados)
if may_impar:
       print("El mayor número impar es:", may_impar)
else:
       print("No se han cargado impares")