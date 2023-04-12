#Título
import random

print("Calculo de Precios con Descuento\n")

#Constantes
VALID_LEN = 3
RAN_RANGE = 0, 9
PROM_PRICE = 50
NORM_PRICE = 90
DESC = 0.10
DESC_7 = 0.50
#Datos
patente = str(int(input("Ingrese los dígitos de la patente xxx: ")))

#Procesos
rand = random.randint(*RAN_RANGE)

if len(patente) == VALID_LEN or patente[0] != "-":
    ult_dig = patente[-1]

    if rand == ult_dig:
        tarifa = PROM_PRICE
    else:
        tarifa = NORM_PRICE

    if ult_dig == 7:
        descuento = tarifa * DESC_7
    else:
        descuento = tarifa * DESC

    abono = tarifa - descuento
    mensaje = "\nMonto a abonar: $" + str(abono)

else:
    mensaje = "ERROR: Los dígitos de la patente no son validos!"



#Resultados
print(mensaje)