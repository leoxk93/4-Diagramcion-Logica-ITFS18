""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Simular el cálculo de un crédito para la compra de un vehículo, dado el
monto a financiar, el plazo en meses y la tasa de interés anual."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]

def calcular_cuota(monto, plazo, tasa_interes):
    tasa_mensual = tasa_interes / 100 / 12  # Conversión de la tasa de interés anual a mensual
    cuota = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo)
    return cuota


monto_financiar = 5000000  
plazo_meses = 36  
tasa_interes_anual = 10  # Tasa de interés anual (%)

cuota_mensual = round(calcular_cuota(monto_financiar, plazo_meses, tasa_interes_anual))
print("Cuota mensual:", cuota_mensual)
