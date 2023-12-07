#Realizar una función que determine si un número es par o impar.

def par_o_impar(num):
    if num %2 == 0:
        return "Este numero es Par"
    else:
        return "Este numero es Impar"

num = float(input("Numero para comprobar "))

print(par_o_impar(num))

#Otra alternativa:

#def par_o_impar(num):
    #if num %2 == 0:
        #return "Este numero es Par"
    #if num %2 == 1:
        #return "Este numero es Impar"

#num = float(input("Numero para comprobar "))

#print(par_o_impar(num))