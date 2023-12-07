#4.1. Crea un diccionario con información de una persona (nombre, edad, ciudad) ymuestra todos los datos en pantalla.
persona = { "nombre": "Diego", "edad": 30, "ciudad": "Argetina" }

for clave, valor in persona.items():
    print(clave + ": " + str(valor))

#4.2. Crea una lista de diccionarios que contengan información de varias personas y muestra el nombre de cada persona en pantalla.
personas = [
    {"nombre": "Leo", "edad": 30, "ciudad": "Buenos Aires"},
    {"nombre": "Agus", "edad": 25, "ciudad": "Santa Fe"},
    {"nombre": "Pablo", "edad": 35, "ciudad": "Cordoba"}
]

for persona in personas:
    print(persona["nombre"])

#4.3. Crea una lista de diccionarios que contengan información de libros (título, autor, año de publicación) y muestra el título y el autor de cada libro en pantalla.
libros = [
    {"título": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"título": "1984", "autor": "George Orwell", "año": 1949},
    {"título": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "año": 1925}
]

for libro in libros:
    print(libro["título"] + " - " + libro["autor"])

#4.4. Crea un diccionario con nombres de frutas y sus cantidades correspondientes. Muestra solo las frutas que tienen una cantidad mayor que 10.
frutas = {
    "manzana": 15,
    "banana": 5,
    "naranja": 20,
    "pera": 8,
    "kiwi": 12
}

for fruta, cantidad in frutas.items():
    if cantidad > 10:
        print(fruta)
