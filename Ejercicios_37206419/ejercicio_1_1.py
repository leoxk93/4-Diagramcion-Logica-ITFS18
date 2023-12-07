#Realizar una función que reciba tres (3) notas y nos retorno como resultado el promedio#

def calcular_promedio(num1, num2, num3):
    suma = num1 + num2 + num3
    promedio = suma / 3
    return promedio

# Pedimos al usuario que ingrese los tres números
num1 = 5
num2 = 6
num3 = 7

# Llamamos a la función para calcular el promedio y lo imprimimos en pantalla
print("El promedio de los tres números es:", int(calcular_promedio(num1, num2, num3)))
