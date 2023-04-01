'''
10. Cálculo de Ganancias de Película

Una empresa dedicada al pago de ganancias por las películas que se realizan en los estudios,
necesita un sistema que permita cargar el total que la película recaudó,
el nombre del participante de la película que se tiene que abonar, el porcentaje que se le debe pagar.
Con esos datos mostrar el nombre del actor y el monto que recibirá de las ganancias
'''
#Ingreso de datos
recaudación= float(input("Ingrese la recaudación total de la película: "))
nombre= input("Ingrese el nombre del actor: ")
porcentajeAPagar= float(input("Ingrese el porcentaje de ganancias correspondiente: "))

#Procesos
montoAPagar = recaudación*(porcentajeAPagar/100)

#Resultado
rta=f"Nombre del actor: {nombre} \nMonto de ganancias a recibir: ${montoAPagar}"
print("--------------------------")
print(rta.format(nombre,montoAPagar))
