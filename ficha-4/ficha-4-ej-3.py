
#Constantes
DIURNO = 1
NOCTURNO = 2
PAGO_H_x_TURNO = 35.50, 40.60

#Título y carga de datos
print("Jornal de un Operario\n")

cod = int(input("Ingrese el código de turno (1 = Diurno, 2 = Nocturno): "))
horas = float(input("Ingrese la cantidad de horas trabajadas: "))

#Procesos

if cod != DIURNO and cod != NOCTURNO:
    mensaje = "\nCódigo de turno inválido! (1 = Diurno, 2 = Nocturno)"
elif horas < 0:
    mensaje = "\nLas horas trabajadas no puede ser un número negativo!"
else:
    pago = horas * PAGO_H_x_TURNO[cod - 1]
    mensaje = "\nEl jornal es de: $" + str(pago)

#Resultados
print(mensaje)