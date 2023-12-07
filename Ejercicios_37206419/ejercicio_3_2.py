""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Dada una lista de vehículos, debemos contar cuantos son de gama alta,
teniendo en cuenta que para saber que son de alta gama, el precio
debe ser superior a los 40.000 dólares, se debe tener en cuenta lo
siguiente: los precios están en pesos, la cotización del dólar está a 525
pesos por cada dólar."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def contar_vehiculos_gama_alta(autos):
    contador = 0
    for auto in autos:
        precio_dolares = auto["precio"] / 525  
        if precio_dolares > 40000:
            contador += 1
    return contador

cantidad_gama_alta = contar_vehiculos_gama_alta(autos_a_venta)
print("Cantidad de vehículos de gama alta:", cantidad_gama_alta)
