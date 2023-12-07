""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Calcular la depreciación de un vehículo usado, dado el modelo, el año, la
marca y el kilometraje actual. La depreciación se debe calcular como un
porcentaje del valor original del vehículo."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def calcular_depreciacion(valor_original, anio_fabricacion, kilometraje_actual):
    anios_transcurridos = 2023 - anio_fabricacion  # Se asume que el año actual es 2023
    porcentaje_depreciacion_anual = 0.10  

    depreciacion_total = valor_original * porcentaje_depreciacion_anual * anios_transcurridos
    depreciacion_total -= depreciacion_total * (kilometraje_actual / 100000)  # Se considera la influencia del kilometraje

    return depreciacion_total


valor_original = 50000000  
anio_fabricacion = 2018  
kilometraje_actual = 80000  

depreciacion = int(calcular_depreciacion(valor_original, anio_fabricacion, kilometraje_actual))

print("La depreciación del vehículo es:", depreciacion)
