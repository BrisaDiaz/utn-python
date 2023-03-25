'''
 4. Últimos dígitos

 ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado,
 y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)
 [Ayuda: ¿cuáles son los posibles restos que se obtienen de dividir un número cualquiera por 10?
'''

entero = int(input("ingrese un número entero: "))
ultDig = entero % 10
dosUltDig = entero % 100
print("--------------------------")
rta1= f"El último digito del número entero {entero} es: {ultDig}"
rta2= f"Los dos últimos digitos del número entero {entero} son: {dosUltDig}"

print(rta1.format(entero,ultDig))
print(rta2.format(entero,dosUltDig))