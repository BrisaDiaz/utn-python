#Título
print("Galería de arte\n")

#constantes
S_XX = 1901

#Carga de datos
c1 = int(input("Ingresa el año de creación del cuadro 1: "))
c2 = int(input("Ingresa el año de creación del cuadro 2: "))
c3 = int(input("Ingresa el año de creación del cuadro 3: "))
fecha = int(input("Ingrese el año a comparar: "))

#Procesos
son_pre_s_xx = c1 < S_XX and c2 < S_XX and c3 < S_XX
hay_coincidencia = c1 == fecha or c2 == fecha or c3 == fecha

dif_fecha = max(c1, c2, c3) - min(c1, c2, c3)

if son_pre_s_xx:
    mensaje = "\nTodos los cuadros son anteriores al siglo XX"
else:
    mensaje = "\nNo todos los cuadros son anteriores al siglo XX"

if hay_coincidencia:
    mensaje = mensaje + "\nAlguna obra fue creada en el año " + str(fecha)
else:
    mensaje = mensaje + "\nNinguna obra fue creada en el año " + str(fecha)

mensaje = mensaje + "\nLa diferencia en años entre la obra más nueva " \
                    "y la más antigua es: " + str(dif_fecha) + " años"

#Resultado
print(mensaje)