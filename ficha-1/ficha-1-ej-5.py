'''
 5. Conversión de medidas

 Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

 yardas
 pulgadas
 centímetros
 metros
 Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.
'''
#Ingreso de datos
pie= float(input("ingrese una medida expresada en pies: "))

#Procesos
YARDA_X_PIES= 3
yarda = pie / YARDA_X_PIES
PULGADA_X_PIES = 12
pulgada = pie * PULGADA_X_PIES
CM_X_PULGADA= 2.54
cm = pulgada * CM_X_PULGADA
CM_X_M = 100
mtr = cm / CM_X_M

#Resultado
print("--------------------------")
rta=f"{pie} pies equivale a:\n\n- {yarda:.1f} yardas\n- {pulgada:.1f} pulgadas\n- {cm:.1f} centímetros \n- {mtr:.1f} metros"
print(rta.format(pie,yarda,pulgada,cm,mtr))
