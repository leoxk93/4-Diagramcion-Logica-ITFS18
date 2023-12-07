""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Calcular el precio de venta de un vehículo usado, dado el modelo, el año, la
marca, el kilometraje. Debe utilizar la función que creo en el ejercicio 3.8."""

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


modelo = "Serie 3"
anio = 2018
marca = "BMW"
kilometraje = 80000

precio_venta = round(calcular_precio_venta(modelo, anio, marca, kilometraje))

if precio_venta is None:
    print("El vehículo no está disponible para la venta.")
else:
    print("El precio de venta del vehículo usado es:", precio_venta)
