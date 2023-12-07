# Dadas las características de un producto y una lista de productos, se deberá devolver si existe o no en la lista de productos.

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def verificar_existencia_producto(caracteristicas_producto, lista_productos):
    for producto in lista_productos:
        if all(producto[caracteristica] == valor for caracteristica, valor in caracteristicas_producto.items()):
            return True

    return False

caracteristicas_producto_buscado = {"nombre": "Mesa", "color": "negro", "tipo": "mueble"}
existe_producto = verificar_existencia_producto(caracteristicas_producto_buscado, productos)
if existe_producto:
    print("El producto existe")
else:
    print("El producto no existe")
