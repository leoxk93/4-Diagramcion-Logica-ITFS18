# Dado el color de un producto, su tipo y una lista de productos, se
# deberá retornar si existe o no un producto con esas características en stock.

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def verificar_existencia_producto(color, tipo, lista_productos):
    for producto in lista_productos:
        if producto["color"] == color and producto["tipo"] == tipo:
            return True

    return False


color_buscado = "blanco"
tipo_buscado = "mueble"
existe_producto = verificar_existencia_producto(color_buscado, tipo_buscado, productos)
if existe_producto:
    print("El producto existe en stock")
else:
    print("El producto no existe en stock")
