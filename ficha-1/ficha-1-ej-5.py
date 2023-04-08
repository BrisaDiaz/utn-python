'''
5. Conversión de medidas
Desarrolle un programa para convertir una medida dada en pies
a sus equivalentes en:
- yardas
- pulgadas
- centímetros
- metros

Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 centímetros
1 metro = 100 centímetros.

'''

#Título y carga de datos
print("Conversión de medidas\n")
pie = float(input("ingrese una medida expresada en pies: "))

#Declaración de constantes
YARDA_X_PIES = 3
PULGADA_X_PIES = 12
CM_X_PULGADA = 2.54
CM_X_M = 100

#Procesos
yarda = pie / YARDA_X_PIES
pulgada = pie * PULGADA_X_PIES
cm = pulgada * CM_X_PULGADA
mtr = cm / CM_X_M

#Resultado
rta = f"\n{yarda} yardas\n{pulgada} pulgadas\n{cm} cm \n{mtr:.1f} mtr"
print(rta.format(pie, yarda, pulgada, cm, mtr))
