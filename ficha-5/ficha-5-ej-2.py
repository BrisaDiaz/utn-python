#Título
print("Elecciones Presidenciales\n")

#Carga de datos
f1 = input("Ingrese presidente + vicepresidente de la 1º formula: ")
f1_votos = int(input("Ingrese la cantidad de votos de la 1º formula: "))
f2 = input("Ingrese presidente + vicepresidente de la 2º formula: ")
f2_votos = int(input("Ingrese la cantidad de votos de la 2º formula: "))
f3 = input("Ingrese presidente + vicepresidente de la 3º formula: ")
f3_votos = int(input("Ingrese la cantidad de votos de la 3º formula: "))

#Procesos

#mayor votos
may_v = f1_votos
may_f = f1

#segundo mayor votos
seg_may_v = f2_votos
seg_may_f = f2

if f2_votos > f1_votos:
    may_v, seg_may_v = f2_votos, f1_votos
    may_f, seg_may_f = f2, f1

if f3_votos > may_v:
    may_v, seg_may_v = f3_votos, may_v
    may_f, seg_may_f = f3, may_f
elif f3_votos > seg_may_v:
    seg_may_v, seg_may_f = f3_votos, f3

#Porcentajes
total_v = f3_votos + f2_votos + f3_votos

may_porcentaje = may_v * (100/total_v)
s_may_porcentaje = seg_may_v * (100/total_v)

print("\n formula ", may_f, "obtuvo la mayor cantidad de votos con %",
      may_porcentaje)

#diferencia de puntos porcentuales
dif_puntos = may_porcentaje - s_may_porcentaje

if may_porcentaje > 45 or (may_porcentaje >= 40 and dif_puntos > 10):
    print("\nLa formula elegida es: ", may_f)
else:
    print("\nSe requiere realizar una segunda entre las formulas:\n", may_f, "\t\t", seg_may_f)