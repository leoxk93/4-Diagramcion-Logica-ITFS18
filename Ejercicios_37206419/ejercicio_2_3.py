# Dado un precio y su respectivo IVA, deberá calcular el precio total más
# IVA del producto. Por ejemplo, si el producto vale $100 y el IVA es del
# 10,5% nos deberá devolver $110,50

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

iva_porcentaje = 10.5  

for producto in productos:
    precio_producto = producto["precio"]

    iva = (precio_producto * iva_porcentaje) / 100

    precio_total = precio_producto + iva

print("Producto:", producto["nombre"])
print("Precio total más IVA:", precio_total)