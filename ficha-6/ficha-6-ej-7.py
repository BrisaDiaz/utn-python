#Título
print("Números pares e impares\n")

#Carga de datos
num = float(input("Ingrese un número: "))

suma_50_a_100 = cant_par = cant_impar = 0
cargo_0 = False
alternado = True
paridad_anterior = None

#Procesos
while num >= 0:
    if 50 <= num <= 100:
        suma_50_a_100 += num
    elif num == 0:
        cargo_0 = True

    if num % 2 == 0:
        cant_par += 1
        if paridad_anterior == "par":
            alternado = False
        paridad_anterior = "par"
    else:
        cant_impar += 1
        if paridad_anterior == "impar":
            alternado = False
        paridad_anterior = "impar"

    # Actualización de datos
    num = float(input("Ingrese un número: "))

print()
print("Sumatorio de números entre 50 y 100:", suma_50_a_100)
print("Cantidad de números pares:", cant_par)
print("Cantidad de números impares:", cant_impar)

if cargo_0:
    print("Se ingreso al menos un número 0")
else:
    print("No se ingreso ningún número 0")

if alternado:
    print("La serie contiene solo números pares e impares alternados")
else:
    print("La serie no contiene solo números pares e impares alternados")