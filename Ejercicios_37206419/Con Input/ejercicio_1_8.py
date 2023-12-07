#Realizar una función que concatene 2 cadenas de texto.

def concatenar_2_textos():
    texto1 = input("Primer texto a concaternar: ")
    texto2 = input("Segundo texto a concaternar: ")

    return texto1 + " " + texto2

res = concatenar_2_textos()
print("El resultado de la concatenación es:", res)

#Se concatenan con un espacio vacio " " para poner un espacio entre los textos concatenados