""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Función que permita ingresar información sobre un vehículo usado
(modelo, año, marca, kilometraje, etc.) y determine si el vehículo es
elegible para ser tomado como parte de pago y financiar con un crédito la
compra de un vehículo nuevo. Para ello, el vehículo debe superar en un
30% el valor del nuevo."""

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

def calcular_precio_venta(modelo, anio, marca, kilometraje):
    vehiculo = None
    for auto in autos_a_venta:
        if auto["modelo"] == modelo and auto["marca"] == marca:
            vehiculo = auto
            break

    if vehiculo is None:
        return None  # El vehículo no está disponible para la venta

    valor_original = vehiculo["precio"]
    depreciacion = calcular_depreciacion(valor_original, anio, kilometraje)

    precio_venta = valor_original - depreciacion
    return precio_venta

def es_elegible_para_financiamiento(modelo_usado, anio_usado, marca_usado, kilometraje_usado, precio_nuevo):
    for auto in autos_a_venta:
        if auto["modelo"] == modelo_usado and auto["marca"] == marca_usado:
            precio_usado = calcular_precio_venta(modelo_usado, anio_usado, marca_usado, kilometraje_usado)
            if precio_usado >= precio_nuevo * 1.3:  # Supera en un 30% el valor del nuevo
                return True

    return False


modelo_usado = "Serie 3"
anio_usado = 2017
marca_usado = "BMW"
kilometraje_usado = 50000
precio_nuevo = 4000000

elegible = es_elegible_para_financiamiento(modelo_usado, anio_usado, marca_usado, kilometraje_usado, precio_nuevo)

if elegible:
    print("El vehículo es elegible para ser tomado como parte de pago y financiar la compra de un vehículo nuevo.")
else:
    print("El vehículo no cumple con las condiciones para ser tomado como parte de pago y financiamiento.")
