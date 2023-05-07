# Título
print("Secuencia de n números\n")

rondas = int(input("Cuantos números desea ingresar?: "))
n = term_5 = rep_primero = cant_mayores = 0
primero = anterior = None

for i in range(rondas):
    # validar que sea mayor a 0
    while n < 1:
        n = float(input("Ingrese un número mayor a 0: "))
        if n < 1:
            print("Error: solo se permiten ingresar números mayores a 0")

    # verificar si termina en 5
    if n % 5 == 0 and n % 10 != 0:
        term_5 += 1

    # inicializar primer número y contar apariciones
    if primero is None:
        primero = n
        rep_primero = 1
    elif n == primero:
        rep_primero += 1

    # contar aparición de valores mayores al anterior
    if not anterior is None and n > anterior:
        cant_mayores += 1

    # actualizar el valor del anterior
    anterior = n

    # forzar carga y validación
    n = -1


print("\nCantidad de números que terminan en 5:", term_5)
print("Cantidad de veces que aparece el primer número:", rep_primero)
print("Cantidad de números mayores al anterior:", cant_mayores)


