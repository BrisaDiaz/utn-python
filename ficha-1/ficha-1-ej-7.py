'''
 7. Precio del boleto

 Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
 Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
 más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
 Por cada kilómetro a recorrer se cobra $0.30 de adicional.
'''

#Título y carga de datos
print("Precio del boleto\n")
precio_base = input("Ingrese el precio base del boleto: "))
km = input("Ingrese la distancia a recorrer expresada en kilómetros: "))

#Declaración de constantes
PRECIO_X_KM= 0.30

#Procesos
respuesta= precio_base + km * PRECIO_X_KM

#Resultado
rta=f"\nPrecio total del boleto: ${respuesta}"
print(rta.format(km,respuesta))