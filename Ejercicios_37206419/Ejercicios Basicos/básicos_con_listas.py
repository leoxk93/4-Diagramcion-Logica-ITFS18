#3.1. Crea una lista de números y muestra la suma de todos los elementos
num = [10, 20, 30, 40, 50]
suma_total = sum(num)

print(suma_total)

#3.2. Crea una lista de números y muestra la suma de los números pares en la lista.
num = [10, 20, 30, 40, 50]
suma_pares = sum(num for num in num if num % 2 == 0)

print(suma_pares)

#3.3. Crea una lista de números y muestra la suma de los números impares en la lista.
num = [10, 20, 30, 40, 50]
suma_impares = sum(num for num in num if num % 2 != 0)

print(suma_impares)

#3.4. Crea una lista de números y muestra la suma de los números mayores que 10 en la lista.
num = [10, 20, 30, 40, 50]
suma_mayores_10 = sum(num for num in num if num > 10)

print(suma_mayores_10)