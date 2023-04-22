#Título
print("Pago a un Proveedor\n")

#Constantes
CATEGORIAS = "AB"
DESCUENTO_A = 0.05
DESCUENTO_B = 0.02

#Carga de datos
importe_orginal = float(input("ingrese el importe original a pagar: "))
categoria = input("ingrese la categoría (A/B): ").upper()

#Procesos

if categoria in CATEGORIAS:
    importe_final = importe_orginal
    if categoria == "A" and importe_orginal > 1000:
        importe_final -= importe_orginal * DESCUENTO_A
    elif categoria == "B" and 2500 >= importe_orginal >= 1500:
        importe_final -= importe_orginal * DESCUENTO_B
    print("\nImporte final a pagar: $"+str(importe_final))
else:
    print("\nERROR: Categoría no válida!")