#Título
print("Números: Mayor y Menor\n")

#Carga de datos
cant = int(input("Ingrese la cantidad de números que desea cargar: "))
may_par = min_impar = 0

for i in range(1, cant + 1):
    num = int(input("Ingrese el número natural nº" + str(i) + ": "))

    #validar carga de números naturales
    while num < 0:
        print("Error: Solo debe cargarse números positivos")
        num = int(input("Ingrese el número natural nº" + str(i) + ": "))

    if num != 0:
        if num % 2 == 0 and num > may_par:
            may_par = num
        if num % 2 == 1 and num < min_impar \
           or num % 2 == 1 and min_impar == 0:
            min_impar = num

#Visualización de datos
print("\nMayor número par:", may_par, "\nMenor número impar:", min_impar)
