#Realizar una función que reciba tres (3) notas y nos retorno como resultado el promedio#

def calcular_promedio(num1, num2, num3):
    suma = num1 + num2 + num3
    promedio = suma / 3
    return promedio

# Pedimos al usuario que ingrese los tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Llamamos a la función para calcular el promedio y lo imprimimos en pantalla
print("El promedio de los tres números es:", calcular_promedio(num1, num2, num3))
