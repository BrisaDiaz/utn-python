'''
11. Palabra enmascarada
Desarrollar un programa que permita ingresar una palabra por teclado y
la devuelva enmascarada, mostrando la primer letra y la última,
pero reemplazando los caracteres intermedios por asteriscos.

Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
'''

#Título y carga de datos
print("Palabra enmascarada\n")
palabra = input("Ingrese una palabra: ")

#Procesos
primera, ultima = palabra[0], palabra[-1]
cant_intermedios = len(palabra) - 2
enmascarada = primera + "*"*cant_intermedios + ultima

#resultados
print("\nLa palabra enmascarada es: ", enmascarada)