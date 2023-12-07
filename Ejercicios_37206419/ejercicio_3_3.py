""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Calcular el precio total de una compra de unidades nuevas de BMW, dado
el precio de cada unidad y la cantidad de unidades a comprar."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def calcular_precio_total(autos, cantidad):
    precio_total = 0
    for auto in autos:
        precio_unitario = auto["precio"]
        precio_total += precio_unitario * cantidad
    return precio_total


cantidad_unidades = 3  
precio_total = calcular_precio_total(autos_a_venta, cantidad_unidades)
print("Precio total de la compra:", precio_total)
