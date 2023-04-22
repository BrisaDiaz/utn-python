#Título
print("Análisis Estadístico (*) - Variante\n")

#Carga de datos
valor_1 = float(input("Ingrese el 1º valor: "))
valor_2 = float(input("Ingrese el 2º valor: "))
valor_3 = float(input("Ingrese el 3º valor: "))
print("")

if valor_1 % 5 == 0 or valor_2 % 5 == 0 or valor_3 % 5 == 0:
    print("Alguno de los valores es múltiplo de 5")
else:
    print("Ninguno de los valores es múltiplo de 5")

cant_impar = int(valor_1 % 2 + valor_2 % 2 + valor_3 % 2)

print("Cantidad de valores impares:", cant_impar)

max_value = max(valor_1, valor_2, valor_3)
suma_resto = valor_1 + valor_2 + valor_3 - max_value

if max_value > suma_resto:
    print("El mayor de los valores supera a la suma de los otros 2")
