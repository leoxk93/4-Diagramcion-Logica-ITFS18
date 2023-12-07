# Dado un producto devolver el nombre del mismo, el color y su precio.
# producto={“nombre”: “Mesa”, “color”: “negro”, “precio”: “30000”}
# Por ejemplo, deberá devolver: “Mesa negro $30000”


# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def obtener_info_producto(nombre_producto):
    for producto in productos:
        if producto["nombre"] == nombre_producto:
            nombre = producto["nombre"]
            color = producto["color"]
            precio = producto["precio"]
            return f"{nombre} {color} ${precio}"

    return "Producto no encontrado"

producto_buscado = "Mesa"
info_producto = obtener_info_producto(producto_buscado)
print(info_producto)

