'''
2. Fecha como cadena
Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato
'dd/mm/aaaa', y muestre por separado el día, el mes y el año.
Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.
'''

#Título y carga de datos
print("Fecha como cadena\n")
fecha_cadena = input("Ingrese una fecha: ")

#Procesos
día, mes, año = fecha_cadena[:2], fecha_cadena[3:5],fecha_cadena[-4:]

#Resultados
rta = f"\nDía: {día}  -  Mes: {mes}  -  Año: {año}"
print(rta.format(día, mes, año))