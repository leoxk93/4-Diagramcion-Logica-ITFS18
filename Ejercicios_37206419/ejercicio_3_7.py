""""Una concesionaria de BMW necesita que se les desarrolle funciones para
mejorar el flujo de compra de nuevas unidades, incluyendo la entrega de
usados, simulación de créditos, generación de planes de pago"""

"""Generar un plan de pago para un crédito para la compra de un vehículo,
dado el monto a financiar, el plazo en meses y la tasa de interés anual. El
plan de pago debe incluir las cuotas mensuales y el saldo pendiente
después de cada cuota."""

autos_a_venta = [
    {"marca": "BMW", "modelo": "Serie 3", "color": "rojo", "precio": 3000000},
    {"marca": "BMW", "modelo": "Serie 5", "color": "azul", "precio": 60000000},
    {"marca": "BMW", "modelo": "X5", "color": "blanco", "precio": 70000000},
    {"marca": "BMW", "modelo": "X3", "color": "negro", "precio": 8000000},
]


def generar_plan_pago(monto_financiar, plazo_meses, tasa_interes_anual):
    tasa_interes_mensual = tasa_interes_anual / 100 / 12  # Conversión de la tasa de interés anual a mensual
    cuota_mensual = (monto_financiar * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -plazo_meses)

    plan_pago = []
    saldo_pendiente = monto_financiar

    for mes in range(1, plazo_meses + 1):
        interes_mensual = saldo_pendiente * tasa_interes_mensual
        amortizacion_mensual = cuota_mensual - interes_mensual
        saldo_pendiente -= amortizacion_mensual

        plan_pago.append({
            "mes": mes,
            "cuota_mensual": round(cuota_mensual),
            "saldo_pendiente": round(saldo_pendiente)
        })

    return plan_pago


monto_financiar = 5000000 
plazo_meses = 36  
tasa_interes_anual = 10  # Tasa de interés anual (%)

plan_pago = generar_plan_pago(monto_financiar, plazo_meses, tasa_interes_anual)


for cuota in plan_pago:
    print("Mes:", cuota["mes"])
    print("Cuota mensual:", cuota["cuota_mensual"])
    print("Saldo pendiente:", cuota["saldo_pendiente"])

