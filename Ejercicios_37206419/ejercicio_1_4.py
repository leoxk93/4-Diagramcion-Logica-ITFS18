#Realizar una función que reciba 4 números y nos indique cuantos números son mayores a 5.

def mayor_a_5(num1, num2, num3, num4):
    contador = 0
    if num1 > 5:
        contador = contador + 1
    if num2 > 5:
        contador += 1
    if num3 > 5:
        contador += 1
    if num4 > 5:
        contador += 1
    return contador

# Pedimos al usuario que ingrese los tres números
num1 = 4
num2 = 6
num3 = 7
num4 = 8

# Llamamos a la función para calcular el promedio y lo imprimimos en pantalla
print("Hay", mayor_a_5(num1, num2, num3, num4), "numeros mayores a 5")