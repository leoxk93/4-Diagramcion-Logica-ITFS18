# Dado el ID de un producto y una lista de productos se deberá retornar si existe el producto.


# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def verificar_existencia_producto(id_producto, lista_productos):
    for producto in lista_productos:
        if producto["id"] == id_producto:
            return True

    return False


id_producto_buscado = 3
existe_producto = verificar_existencia_producto(id_producto_buscado, productos)
if existe_producto:
    print("El producto existe")
else:
    print("El producto no existe")
