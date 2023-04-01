'''
 7. Precio del boleto

 Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
 Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
 más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
 Por cada kilómetro a recorrer se cobra $0.30 de adicional.
'''
#Ingreso de datos
precioBase= float(input("Ingrese el precio base del boleto: "))
km= float(input("Ingrese la distancia a recorrer expresada en kilómetros: "))

#Procesos
PRECIO_X_KM= 0.30
respuesta= precioBase + km * PRECIO_X_KM

#Resultado
print("--------------------------")
rta=f"El precio total del boleto de ómnibus para un recorrido de {km} kilómetros es de: ${respuesta}"
print(rta.format(km,respuesta))