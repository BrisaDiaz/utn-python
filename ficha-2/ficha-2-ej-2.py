'''
2. Descuento en medicinas
Calcular el descuento y el monto a pagar por un medicamento cualquiera
en una farmacia (cargar por teclado el precio de ese medicamento) sabiendo
que todos los medicamentos tienen un descuento del 35%.
Mostrar el precio actual, el monto del descuento y el monto final a pagar.
'''

#Título y carga de datos
print("Descuento en medicinas\n")
precio = float(input("Ingrese el precio del medicamento: "))

#Procesos
DESCUENTO = 35 / 100
desc = precio * DESCUENTO
precio_f = precio - desc

#Resultado
rta = f"\nPrecio: ${precio}\nDesconto: ${desc}\nPrecio final: ${precio_f}"
print(rta.format(precio, desc, precio_f))