#Título
print("Dirección de Tránsito\n")

#Carga de datos
patente = input("Ingrese una patente: ")
largo = len(patente)

while largo != 7 and largo != 6:
    print("Error: Largo de patente inválido")
    patente = input("Ingrese una patente de 6 o 7 caracteres: ").strip()
    largo = len(patente)

espacios_ok = True
antigua_ok = nueva_ok = False


if largo == 6:
    antigua_ok = True
else:
    nueva_ok = True

for i in range(len(patente)):
    if patente[i] == " ":
        espacios_ok = False

    if antigua_ok and (i < 3 and patente[i].isnumeric()) or\
        i > 2 and patente[i].isalpha():
        antigua_ok = False

    if nueva_ok and (i < 2 and patente[i].isnumeric()) or\
       5 > i > 1 and patente[i].isalpha() or \
       i > 4 and patente[i].isnumeric():
        nueva_ok = False

#visualización de datos
print()
if not espacios_ok:
    print("Error: Patente contiene espacios en blanco")
if not (antigua_ok or nueva_ok):
    print("Error: La patente no contiene las letras y números esperados")
elif antigua_ok:
    print("Se trata de una patente en formato antiguo")
else:
    print("Se trata de una patente en formato nuevo")