'''
3. Ecuación de Einstein
La famosa ecuación de Einstein para conversión de una masa m en energía
viene dada por la fórmula:
E = mc2
Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
Desarrolle un programa que lea el valor una masa m en kilogramos y obtenga
la cantidad de energía E producida en la conversión.
'''

#Título y carga de datos
print("Ecuación de Einstein\n")
masa = float(input("Ingrese el valor de masa en kilogramos: "))

#Procesos
VELOCIDAD_DE_LUZ = 299792.458
energia = masa*pow(VELOCIDAD_DE_LUZ, 2)

#Resultado
rta = f"\nCantidad de energía producida: {energia} Julios"
print(rta.format(energia))