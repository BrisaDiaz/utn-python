#Constantes
VOCS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

#Título
print("Analisis de palabra\n")

#Carga de datos
palabra = input("Ingrese una palabra: ")

#Procesos
cant_letras = len(palabra)

if cant_letras:
    ult_letra = palabra[-1]

if not cant_letras:
    mensaje = "La palabra no posee ningun caracter!"
elif (ult_letra == VOCS[0] or ult_letra == VOCS[1] or ult_letra == VOCS[2] or
    ult_letra == VOCS[3] or ult_letra == VOCS[4] or ult_letra == VOCS[5] or
    ult_letra == VOCS[6] or ult_letra == VOCS[7] or ult_letra == VOCS[8] or
    ult_letra == VOCS[9]):
    mensaje = "\nLa palabra termina en vocal"
else:
    mensaje = "\nLa palabra no termina en vocal"

#Resultados
print(mensaje)
