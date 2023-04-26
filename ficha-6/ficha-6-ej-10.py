#Título
print("Comisión de Vendedores\n")

CATEGORIAS = 1, 2, 3, 4
COMICION_1 = 0.10
COMICION_2 = 0.25
COMICION_3 = 0.30
COMICION_4 = 0.40

ronda = 1
total = a_pagar_1 = a_pagar_2 = a_pagar_3 = a_pagar_4 = 0

#Carga de datos
print("vendedor nº", ronda)
cat = int(input("Ingrese la categoría del vendedor (1 a 4): "))

if cat in CATEGORIAS or cat == 0:
    while cat != 0:
        monto_ventas = float(input("Ingrese el monto total en ventas: "))

        if cat == 1:
            pago = monto_ventas * COMICION_1
            total += pago
            a_pagar_1 += pago
        elif cat == 2:
            pago = monto_ventas * COMICION_2
            total += pago
            a_pagar_2 += pago
        elif cat == 3:
            pago = monto_ventas * COMICION_3
            total += pago
            a_pagar_3 += pago
        else:
            pago = monto_ventas * COMICION_4
            total += pago
            a_pagar_4 += pago

        #Actualización de datos
        ronda += 1
        print("vendedor nº", ronda)
        cat = int(input("Ingrese la categoría del vendedor (1 a 4): "))

    #visualización de resultados
    print()
    print("Tota a pagar: $", total)
    print("Monto a pagar por categoría:")
    print("Categoría 1: $", a_pagar_1, "\nCategoría 2: $", a_pagar_2,
          "\nCategoría 3: $", a_pagar_3, "\nCategoría 4: $", a_pagar_4)

else:
    print("Error: Categoría no válida")



