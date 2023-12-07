//Realizar una función que determine si un año es bisiesto.
Funcion año_viciestro <- años( n )
	si n %4 = 0 Entonces
		Mostrar ("Es un año bisiesto")
		año_viciestro = n
	FinSi
Fin Funcion

Algoritmo Ejercicio6
	valor = años(2024)
	Mostrar (valor)
FinAlgoritmo
