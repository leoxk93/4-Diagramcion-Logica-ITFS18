#Realizar una función que reciba dos números y nos indique cual de los números es el mayor.

def numero_mayor(num1, num2):
    if num1 > num2:
     return num1
    if num1 < num2:
     return num2
    if num1 == num2:
     return "son iguales"

# Pedimos al usuario que ingrese los tres números
num1 = 4
num2 = 5

# Llamamos a la función para calcular el promedio y lo imprimimos en pantalla
print("El numero mas grande es ", str(numero_mayor(num1, num2)))