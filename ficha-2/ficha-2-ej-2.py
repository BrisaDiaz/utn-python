'''
2. Descuento en medicinas
Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%.
Mostrar el precio actual, el monto del descuento y el monto final a pagar.
'''
#Ingreso de datos
precioAct= float(input("Ingrese el precio del medicamento: "))

#Procesos
DESCUENTO=35/100
montoDesc= precioAct * DESCUENTO
precioFinal= precioAct-montoDesc

#Resultado
rta= f"Precio del medicamento: ${precioAct}\nMonto descontado: ${montoDesc}\nPrecio final a pagar: ${precioFinal}"
print("--------------------------")
print(rta.format(precioAct,montoDesc,precioFinal))