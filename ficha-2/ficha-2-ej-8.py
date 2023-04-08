'''
8. Rinde de un Campo Agricola
Un productor agricola desea saber cuantos quintales de trigo puede producir
en su parcela. Se pide ingresar el largo y el ancho en metros de la parcela
y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.
'''

#Título y carga de datos
print("Rinde de un Campo Agricola\n")
largo = float(input("Ingrese la medida (metros) del largo de la parcela: "))
ancho = float(input("Ingrese la medida (metros) del ancho de la parcela: "))

#Procesos
m2 = largo * ancho
rinde = int((m2//10)*2)

#Resultado
rta = f"\nEl número de quintales que se pueden producir es: {rinde}"
print(rta.format(rinde))

