'''
5. Control electoral
Desarrollar un programa de control electoral en un centro vecinal,
en el que se ingresen, para cierto candidato: apellido, nombre y cantidad de votos.
Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
cantidad de votos entre paréntesis, y debajo una línea con tantas  "x" como votos obtenidos
(por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como esta:
"xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal no hay demasiados electores,
de forma que podamos estar seguros que no habrá miles o millones de votos...
sólo unos pocos para darle sentido al enunciado).
'''

#Título y carga de datos
print("Control electoral\n")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
votos = int(input("Ingrese la cantidad de votos: "))

#Procesos
votos_x = "x" * votos
iniciales = nombre[0].upper()+"."+apellido[0].upper()

#Resultados
rta = f"\n{iniciales}({votos})\n{votos_x}"
print(rta.format(iniciales, "\n", votos, votos_x))