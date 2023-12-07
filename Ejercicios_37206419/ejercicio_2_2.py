# Dado un precio de un producto, la cantidad de productos a entregar y la cantidad de productos 
# que deberá pagar nos calcule el precio unitario de cada producto. 
# Ya que están implementando promociones del tipo 3x2, 4x2, 2x1, etc y quieren saber a cuanto queda el precio por unidad.

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

for producto in productos:
    precio_producto = producto["precio"]

cantidad_entregar = 5  # Cantidad de productos a entregar
cantidad_pagar = 4  # Cantidad de productos a pagar

# Calcular la cantidad total de productos (incluyendo los promocionales gratuitos)
cantidad_total = cantidad_entregar + (cantidad_entregar // cantidad_pagar)

precio_total = precio_producto * cantidad_entregar

precio_unitario = precio_total / cantidad_total

# Mostrar el precio unitario del producto
print("Producto:", producto["nombre"])
print("Precio unitario:", precio_unitario)




