'''
7. Cálculo presupuestario
En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y
Traumatología. El presupuesto anual del hospital se reparte de la siguiente manera:

Área               Presupuesto
Urgencias          37%
Pediatría          42%
Traumatología      21%

Cargar por teclado el monto del presupuesto total del hospital,
y calcular y mostrar el monto que recibirá cada área.
'''

#Título y carga de datos
print("\nCálculo presupuestario")
presupuesto = float(input("Ingrese el presupuesto anual: "))

#Declaración de constantes
URG_PRESUP = 37
PED_PRESUP = 42
TRAUM_PRESUP = 21

#Procesos

urg = presupuesto * (URG_PRESUP / 100)
ped= presupuesto * (PED_PRESUP / 100)
traum = presupuesto * (TRAUM_PRESUP / 100)

#Resultados
cabecera = "\nÁrea\t\t\t\tPresupuesto"
rta = f"\nUrgencias:\t\t\t${urg}\nPediatría:\t\t\t${urg}\nTraumatología:\t\t${urg}\n"

print(cabecera,format(rta.format(urg, ped, traum)))