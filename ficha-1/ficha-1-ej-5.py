'''
 5. Conversión de medidas

 Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

 yardas
 pulgadas
 centímetros
 metros
 Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.
'''
pie= float(input("ingrese una medida expresada en pies: "))
yardaXpies= 3
yarda = pie / yardaXpies
pulgadaXpie = 12
pulgada = pie * pulgadaXpie
cmXpulgada= 2.54
cm = pulgada * cmXpulgada
cmXmetro = 100
mtr = cm / cmXmetro
print("--------------------------")
rta=f"{pie} pies equivale a:\n\n- {yarda:.1f} yardas\n- {pulgada:.1f} pulgadas\n- {cm:.1f} centímetros \n- {mtr:.1f} metros"
print(rta.format(pie,yarda,pulgada,cm,mtr))
