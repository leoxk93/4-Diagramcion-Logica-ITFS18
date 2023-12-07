# Dado el nombre de un producto y una lista de productos se deberá buscar el producto en dicha lista 
# y en caso de encontrar una o más coincidencias se deberá devolver los resultados como una nueva lista.

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def buscar_productos_por_nombre(nombre, productos):
    nueva_lista_de_productos = []

    for producto in productos:
        if producto ["nombre"] == nombre:
            nueva_lista_de_productos.append(producto)
            return nueva_lista_de_productos
        
print(buscar_productos_por_nombre("mesa", productos))