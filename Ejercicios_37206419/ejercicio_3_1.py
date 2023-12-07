""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Dada una lista de autos a la venta y un color, debemos filtrar y
únicamente devolver los vehículos rojos"""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def filtrar_autos_por_color(autos, color):
    autos_rojos = [auto for auto in autos if auto["color"] == color]
    return autos_rojos

color_busqueda = "rojo"
autos_rojos = filtrar_autos_por_color(autos_a_venta, color_busqueda)
print("Autos rojos disponibles:")
for auto in autos_rojos:
    print(auto)
