// Realizar una función que determine si un número es divisible por 3 o por 5.
Funcion dibisible_por_3_o_5 <- dividendo (n) 
	si n %3 = 0 Entonces
		Mostrar ("Es divisible por 3")
		dibisible_por_3_o_5 = n
	FinSi
	si n %5 = 0 Entonces
		Mostrar ("Es dibisible por 5")
		dibisible_por_3_o_5 = n
	FinSi
	
Fin Funcion

Algoritmo Ejercicio5
	valor = dividendo (36)
	Mostrar  (valor)
FinAlgoritmo
