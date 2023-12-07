#Realizar una función que determine si un año es bisiesto.

def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
anio = int(input("Ingresa un año a comprobar: "))

if es_bisiesto(anio):
    print(anio, "es bisiesto")
else:
    print(anio, "no es bisiesto")

