'''
 7. Precio del boleto

 Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
 Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
 más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
 Por cada kilómetro a recorrer se cobra $0.30 de adicional.
'''

precioBase= float(input("Ingrese el precio base del boleto: "))
km= float(input("Ingrese la distancia a recorrer expresada en kilometros: "))
precioXkm= 0.30

print("--------------------------")
respuesta= precioBase + km * precioBase
rta=f"El precio total del boleto de ómnibus para un recorrido de {km} kilometros es de: {respuesta}"
print(rta.format(km,respuesta))