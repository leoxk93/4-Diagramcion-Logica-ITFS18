""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Calcular el valor de un vehículo usado que se entrega como parte de pago
al comprar un vehículo nuevo, dado el modelo, el año, la marca y el
kilometraje. Pueden crear el algoritmo que quieran, son libres."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def calcular_valor_usado(modelo, año, marca, kilometraje):
    valor_base = 1000000 

    if modelo == "Serie 3":
        valor_base += 500000
    elif modelo == "Serie 5":
        valor_base += 800000
    elif modelo == "X5":
        valor_base += 1000000
    
    if año < 2010:
        valor_base -= 200000
    elif año > 2015:
        valor_base += 200000
    
    if marca == "BMW":
        valor_base += 300000
    
    valor_base -= kilometraje * 0.05  # Descuento por kilometraje (5% por cada 1000 km)
    
    return valor_base


modelo_usado = "Serie 3"
año_usado = 2012
marca_usado = "BMW"
kilometraje_usado = 80000

valor_usado = int(calcular_valor_usado(modelo_usado, año_usado, marca_usado, kilometraje_usado))
print("Valor del vehículo usado:", valor_usado)
