'''
6. Precio de venta
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento)
Precio de venta con tarjeta (5% de recargo)
'''
#Ingreso de datos
precioArticulo= float(input("Ingrese el precio del artículo: "))

#Procesos
DESCUENTO_CONTADO= 10/100
RECARGO_TARJETA=5/100

precioAlContado= precioArticulo - (precioArticulo*DESCUENTO_CONTADO)
precioConTarjeta= precioArticulo + (precioArticulo*RECARGO_TARJETA)

#Resultado
rta=f"El precio de venta al contado es de: ${precioAlContado}\nEl precio de venta con tarjeta es de: ${precioConTarjeta}"
print("--------------------------")
print(rta.format(precioAlContado,precioConTarjeta))