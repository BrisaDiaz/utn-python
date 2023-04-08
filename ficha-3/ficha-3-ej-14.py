'''
14. Sumador de Ángulos
Se desea un programa que dados 2 ángulos expresados en grados minutos
y segundos, informe la suma de ambos en grados minutos y segundos.
'''

#Título y carga de datos
print("Sumador de Ángulos\n")
alfa = input("Ingrese el valor del ángulo alfa: ")
beta = input("Ingrese el valor del ángulo beta: ")

#Declaración de constantes
SEGUNDOS_X_MINUTO = 60
MINUTOS_X_GRADO = 60

#Procesos
alfa_g = int(alfa[:alfa.index("º")])
alfa_m = int(alfa[alfa.index("º")+1:alfa.index("\'")])
alfa_s = int(alfa[alfa.index("'")+1:alfa.index("\"")])

beta_g = int(beta[:beta.index("º")])
beta_m = int(beta[beta.index("º")+1:beta.index("\'")])
beta_s = int(beta[beta.index("'")+1:beta.index("\"")])

segundos_x_grado = MINUTOS_X_GRADO * SEGUNDOS_X_MINUTO

suma_g = alfa_g + beta_g
suma_m = alfa_m + beta_m
suma_s = alfa_s + beta_s

total_s = suma_s + suma_m*SEGUNDOS_X_MINUTO + suma_g*segundos_x_grado

grados, resto = divmod(total_s, segundos_x_grado)
minutos, segundos = divmod(resto, SEGUNDOS_X_MINUTO)

#Resultados
rta = f"\nLa suma de los ángulos es: {grados}º{minutos}'{segundos}''"
print(rta.format(grados, minutos, segundos))