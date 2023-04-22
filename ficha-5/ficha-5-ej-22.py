#Título
print("Votación en el Senado\n")

#Constantes
CANT_SENADORES = 72

#Carga de datos
votos_favor = int(input("Ingrese la cantidad de votos a favor: "))
votos_contra = int(input("Ingrese la cantidad de votos en contra: "))
abtenciones = int(input("Ingrese la cantidad de abtenciones: "))
print("")

#Procesos
total_votos = votos_favor + votos_contra + abtenciones

if total_votos > CANT_SENADORES:
    print("ERROR: La cantidad de votos totales es errónea!")
else:
    porcentaje_favor = votos_favor * (100 / total_votos)

    if porcentaje_favor > 50:
        print("La ley fue aprobada por mayoría absoluta")
    elif votos_favor > votos_contra:
        print("La ley fue aprobada por mayoría simple")
    else:
        print("La ley no fue aprobada")

    cant_ausentes = CANT_SENADORES - total_votos
    print("Cantidad de senadores ausentes:", cant_ausentes)

