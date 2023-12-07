#Realizar una función que determine si un número es divisible por 3 o por 5.

def es_divisible_x3_o_x5(num):
    if num % 3 == 0 and num % 5 == 0:
        return "divisible por 3 y por 5"
    elif num % 3 == 0:
        return "divisible por 3"
    elif num % 5 == 0:
        return "divisible por 5"
    else:
        return "no es divisible ni por 3 ni por 5"
    
num = float(input("Ingresa el número: "))

print(es_divisible_x3_o_x5(num))