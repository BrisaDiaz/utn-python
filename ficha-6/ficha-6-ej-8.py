#Título
print("Censo\n")

SEXOS = "MF"

cant = 1
cant_m = cant_f = cant_f_edad_escolar = 0
cargo_m_mayor_80 = False

print("Persona nº", cant)
#Carga de datos
sexo = input("Ingrese el sexo (M/F): ").upper().strip()

#Procesos
while sexo in SEXOS:
    edad = int(input("Ingrese la edad: "))
    if sexo == "M":
        cant_m += 1
        if edad > 80:
            cargo_m_mayor_80 = True
    else:
        cant_f += 1
        if 18 >= edad >= 4:
            cant_f_edad_escolar += 1

    # Actualización de datos
    cant += 1
    print("Persona nº", cant)
    sexo = input("Ingrese el sexo (M/F): ").upper().strip()

print()
#Visualización de datos
if cant_f > cant_m:
    print("Hay mayor cantidad de mujeres")
elif cant_m > cant_f:
    print("Hay mayor cantidad de hombres")
else:
    print("Hay la misma cantidad de hombres y mujeres")

print("Cantidad de mujeres en edad preescolar:", cant_f_edad_escolar)

if cargo_m_mayor_80:
    print("Hay algún varón que supere los 80 años de edad")
else:
    print("Ningún varón supera lo 80 años de edad")