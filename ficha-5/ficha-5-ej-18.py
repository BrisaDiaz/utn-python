#Título
print("Lluvias\n")

#Carga de datos
mm_mes_1 = float(input("Ingrese los milímetros de lluvia en el 1º mes: "))
mm_mes_2 = float(input("Ingrese los milímetros de lluvia en el 2º mes: "))
mm_mes_3 = float(input("Ingrese los milímetros de lluvia en el 3 mes: "))

prom = (mm_mes_1 + mm_mes_2 + mm_mes_3) / 3

print("\nPromedio de milímetros caídos:", prom)

cant_may_prom = 0
if mm_mes_1 >= prom:
    cant_may_prom += 1
if mm_mes_2 >= prom:
    cant_may_prom += 1
if mm_mes_3 >= prom:
    cant_may_prom += 1

print("Cantidad de meses con más o igual lluvia que el promedio:",
      cant_may_prom)

min_mm = mm_mes_1
min_mes = "1º mes"

if mm_mes_2 < mm_mes_1:
    min_mm = mm_mes_2
    min_mes = "2º mes"

if mm_mes_3 < min_mm:
    min_mm = mm_mes_3
    min_mes = "3º mes"

print("Mes con menos lluvias en el trimestre:", min_mes)
if min_mm == 0:
    print("No se registraron lluvias en dicho més.")
