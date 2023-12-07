#La palabra reservaba def se utiliza para definir una funcion
# Seguido a la def se escribe el nombre de la funcion
# Entre parentesis, van los parametros
# Si no tiene parametros, los parentesis se escriben igual
# Los parametros se separan con coma
# Las funicones se escriben con palabras separadas por _
# Class se usa Camel Case

#Realizar una función que reciba 4 notas de exámenes finales y devuelva la cantidad de alumnos aprobaron la materia.

def obtener_cantidad_aprobados(nota1, nota2, nota3, nota4):
    contador = 0
    if nota1 >= 7:
        contador = contador + 1
    if nota2 >= 7:
        contador = contador + 1
    if nota3 >= 7:
        contador = contador + 1
    if nota4 >= 7:
        contador = contador + 1
    return contador

# Pedimos al usuario que ingrese los tres números
nota1 = float(input("Ingresa el primer número: "))
nota2 = float(input("Ingresa el segundo número: "))
nota3 = float(input("Ingresa el tercer número: "))
nota4 = float(input("Ingresa el tercer número: "))

print("La cantidad de alumnos aprobados "+ str(obtener_cantidad_aprobados(nota1, nota2, nota3, nota4)))
