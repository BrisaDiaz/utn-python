'''
3. Importe como cadena
Desarrollar un programa que cargue por teclado un importe (cantidad de dinero)
expresado como número en coma flotante y muestre un mensaje con esa cantidad
pero en dos formatos: en uno debe aparecer precedida por el signo '$' y en el
otro debe aparecer precedida por la palabra "pesos".
'''

#Título y carga de datos
print("Importe como cadena\n")
importe = float(input("Ingrese el monto del importe: "))

#Procesos
importe_str = str(importe)
importe_signo = "$" + importe_str
importe_texto = importe_str + " pesos"

#Resultados
print("\n", importe_signo, "\n", importe_texto)