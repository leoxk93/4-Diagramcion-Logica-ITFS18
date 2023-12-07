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
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
num4 = int(input("Ingresa el tercer número: "))

# Llamamos a la función para calcular el promedio y lo imprimimos en pantalla
print("Hay", mayor_a_5(num1, num2, num3, num4), "numeros mayores a 5")