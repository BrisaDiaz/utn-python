#Título y carga de datos
print("Generador de Dirección de Mail\n")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dominio = input("Ingrese el dominio: ")

#Procesos
email = apellido+"@"+dominio

if nombre[0] == apellido[0]:
    email = nombre + "." + email
else:
    email = nombre[0] + email

#Resultados
print("\nDirección de email: ", email)