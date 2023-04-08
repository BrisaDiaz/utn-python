'''
4. Últimos dígitos
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue
un número entero por teclado,y muestre el último dígito del mismo (por un lado)
y los dos últimos dígitos (por otro lado) [Ayuda: ¿cuáles son los posibles restos
que se obtienen de dividir un número cualquiera por 10?
'''

#Título y carga de datos
print("Últimos dígitos\n")
entero = int(input("ingrese un número entero: "))

#Procesos
ult = entero % 10
dos_ult = entero % 100

#Resultado
rta = f"\núltimo digito: {ult}\nDos últimos dígitos: {dos_ult}"
print(rta.format(ult, dos_ult))