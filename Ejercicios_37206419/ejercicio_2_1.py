# Dado un precio de un producto y un porcentaje variable, nos devuelva
# el precio aumentado en dicho porcentaje. 
# Por ejemplo, si el valor es $100 y aumenta en un 15% nos debería devolver $115

# Base de datos de nuestro cliente
productos = [
{"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
{"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
{"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
{"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
{"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def calcular_precio_aumentado(precio, porcentaje):
    aumento = precio * (porcentaje / 100)
    nuevo_precio = precio + aumento
    return nuevo_precio

nombre_producto = "Camiseta" 
porcentaje_aumento = 15  


producto = [p for p in productos if p["nombre"] == nombre_producto]

if producto:
    precio_inicial = producto[0] ["precio"]
    nuevo_precio = calcular_precio_aumentado(precio_inicial, porcentaje_aumento)
    producto[0]["nuevo_precio"] = nuevo_precio
    print("El nuevo precio de", nombre_producto, "es:", int(nuevo_precio))
else:
    print("No se encontró ningún producto con el nombre especificado.")



"""
#EJ: Aumento de Precio para todos los productos

def precio_aumentado(precio, porcentaje):
    aumento = precio * (porcentaje / 100)
    nuevo_precio = precio + aumento
    return nuevo_precio

porcentaje_aumento = 15  # Porcentaje de aumento variable

for producto in productos:
    precio_inicial = producto["precio"]
    nuevo_precio = precio_aumentado(precio_inicial, porcentaje_aumento)
    producto["nuevo_precio"] = nuevo_precio

print(productos)

"""
