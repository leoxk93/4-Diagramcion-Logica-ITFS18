""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Función que permita ingresar información sobre un vehículo (modelo, año,
marca, kilometraje, etc.) y determine si el vehículo es elegible para ser
entregado como parte de pago en la compra de un vehículo nuevo.
Condiciones: La depreciación no debe superar el 60% y el año de
fabricación no debe superar los 20 años y el kilometraje tiene que estar
dentro de un rango aceptable de 20.000 kilómetros por año y solo aceptan
autos BMW."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]


def calcular_depreciacion(valor_original, anio_fabricacion, kilometraje_actual):
    anios_transcurridos = 2023 - anio_fabricacion  
    porcentaje_depreciacion_anual = 0.10  

    depreciacion_total = valor_original * porcentaje_depreciacion_anual * anios_transcurridos
    depreciacion_total -= depreciacion_total * (kilometraje_actual / 100000)  # Se considera la influencia del kilometraje

    return depreciacion_total

def es_elegible_para_entrega(modelo, anio, marca, kilometraje):
    if marca != "BMW":
        return False  # Solo aceptan autos BMW

    anio_actual = 2023

    # Comprobación del año de fabricación
    if anio > anio_actual - 20:
        return False  

 
    kilometraje_maximo = (anio_actual - anio) * 20000  # 20.000 kilómetros por año
    if kilometraje > kilometraje_maximo:
        return False  # El kilometraje supera el rango aceptable

    # Cálculo de la depreciación máxima permitida (60%)
    valor_original = None
    for auto in autos_a_venta:
        if auto["modelo"] == modelo and auto["marca"] == marca:
            valor_original = auto["precio"]
            break

    if valor_original is None:
        return False  

    depreciacion_maxima = valor_original * 0.6

   
    depreciacion = calcular_depreciacion(valor_original, anio, kilometraje)
    if depreciacion > depreciacion_maxima:
        return False 

    return True  # El vehículo es elegible para entrega como parte de pago


modelo = "Serie 3"
anio = 2022
marca = "BMW"
kilometraje = 10000

elegible = es_elegible_para_entrega(modelo, anio, marca, kilometraje)

if elegible:
    print("El vehículo es elegible para ser entregado como parte de pago.")
else:
    print("El vehículo no cumple con las condiciones para ser entregado como parte de pago.")
