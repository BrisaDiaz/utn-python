'''
1. Plazo fijo
Desarrollar un programa que cargue por teclado la cantidad de dinero depositada
en plazo fijo por un cliente de un banco y calcular el saldo que tendrá esa
cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3%
y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.
'''

#Título y carga de datos
print("Plazo fijo\n")
deposito = float(input("Ingrese el monto del dinero depositado: "))
meses = int(input("Ingrese la cantidad de meses: "))

#Asignación de constantes
INTERES = 2.3/100
GASTOS_FIJOS = 20

#Procesos
saldo_bruto_mensual = deposito + deposito*INTERES
saldo_neto_mensual = saldo_bruto_mensual - GASTOS_FIJOS
saldo_final = saldo_neto_mensual * meses

#Resultados
rta = f"\nEl saldo de su cuenta sera de: ${saldo_final}"
print(rta.format(saldo_final))
