'''
6. Precio de venta
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento)
Precio de venta con tarjeta (5% de recargo)
'''

#Título y carga de datos
print("Precio de venta\n")
precio_articulo = float(input("Ingrese el precio del artículo: "))

#Procesos
DESCUENTO_CONTADO = 10/100
RECARGO_TARJETA = 5/100

precio_contado = precio_articulo - (precio_articulo*DESCUENTO_CONTADO)
precio_tarjeta = precio_articulo + (precio_articulo*RECARGO_TARJETA)

#Resultado
rta = f"\nPrecio al contado: ${precio_contado}\nPrecio con tarjeta: ${precio_tarjeta}"
print(rta.format(precio_contado, precio_tarjeta))