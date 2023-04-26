#Título
print("Complejo de cines\n")

#Constantes
PRECIO_ESTANDAR = 75
PRECIO_DESCUENTO = 50
RESPUESTAS = "sn"

#Carga de datos
cant_espec = int(input("Ingrese la cantidad de espectadores: "))
cant_func = cant_func_desc = recaudacion = 0

if cant_espec < 0:
    print("Error: La cantidad de espectadores no puede ser negativa")

else:
    while cant_espec != 0:
        desc = input("Indique si se aplica o no descuento (s/n): ").lower()
        if not (desc in RESPUESTAS):
            print("Error: Respuesta de descuento invalida")
        else:
            cant_func += 1

            if desc == "s":
                cant_func_desc += 1
                recaudacion = cant_espec * PRECIO_DESCUENTO
            else:
                recaudacion = cant_espec * PRECIO_ESTANDAR

            # Actualización de datos
            cant_espec = int(input("Ingrese la cantidad de espectadores: "))

porc_descuento = cant_func_desc * (100 / cant_func)

print()
#Visualización de datos
print("Recaudación total: $", recaudacion)
print("Cantidad de funciones con descuentos:", cant_func_desc)
print("Porcentaje de funciones con descuento: %", porc_descuento)