'''
6. Cálculo de sueldo
Se conoce el monto del salario actual de un empleado, el nombre del empleado
y el área funcional al cual pertenece. Se pide calcular el nuevo salario
del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual
y un descuento de 2.5% por servicios, informando los resultados con el formato
que se especifica a continuación:

       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx

       Área Funcional:  xxxxxxxxxxxx

       Salario Actual: $ xxxx
'''

#Título y carga de datos
print("Cálculo de sueldo\n")
nombre = input("Ingrese el nombre del empleado: ")
area = input("Ingrese el area funcional: ")
salario_actual = float(input("Ingrese el monto del salario actual: "))

#Declaración de constantes
INCREMENTO = 8
DESCUENTO = 2.5

#Procesos
aumento_neto = salario_actual * (INCREMENTO - DESCUENTO) / 100
salario_final = salario_actual + aumento_neto

#Resultados
line1 = f"\n\tNombre Empleado: {nombre}\t\t\t\tNuevo Salario: $ {salario_final}"
line2= f"\n\tÁrea Funcional: {area}\n\tSalario Actual: $ {salario_actual}"
print(line1.format(nombre, salario_final), line2.format(area, salario_actual))