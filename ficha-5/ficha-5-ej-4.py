#Título
print("Observatorio meteorológico\n")

#Carga de datos
tem_1 = int(input("Ingrese el valor de la 1º temperatura: "))
tem_2 = int(input("Ingrese el valor de la 2º temperatura: "))
tem_3 = int(input("Ingrese el valor de la 3º temperatura: "))
tem_4 = int(input("Ingrese el valor de la 4º temperatura: "))

suma_temp = tem_1 + tem_2 + tem_3 + tem_4
tem_prom = suma_temp / 4

print("La temperatura diaria promedio es de: ", tem_prom, "grados")

#sacar la menor y mayor temp en dos grupos

may_1, min_1 = tem_1, tem_2
if tem_2 > tem_1:
    may_1, min_1 = tem_2, tem_1

may_2, min_2 = tem_3, tem_4
if tem_4 > tem_3:
    may_2, min_2 = tem_4, tem_3

#sacar la menor y mayor temp entre los grupos
if may_1 > may_2:
    may_temp = may_1
else:
    may_temp = may_2

if min_1 < min_2:
    min_temp = min_1
else:
    min_temp = min_2

print("\nLa mayor temperatura registrada es de:", may_temp, "grados")
print("La menor temperatura registrada es de:", min_temp, "grados")


if tem_1 > tem_prom or tem_2 > tem_prom or tem_3 > tem_prom \
   or tem_4 > tem_prom:
    print("Algunas de las temperaturas supera a la temperatura promedio")
else:
    print("Ninguna de las temperaturas supera a la temperatura promedio")
