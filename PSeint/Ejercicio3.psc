//Realizar una funci�n que reciba dos n�meros y nos indique cual de los
//n�meros es el mayor.
Funcion mayor_menor <-numero_mayor ( n1,n2)
	mayor_menor= 0
	si n1 > n2 Entonces
		Mostrar ("El numero mayor es el primero")
		mayor_menor = mayor_menor +n1
	SiNo
		Mostrar ("El numero mayor es el segundo")
		mayor_menor = mayor_menor +n2
	FinSi
	
Fin Funcion

Algoritmo Ejercicio3
	valor = numero_mayor(4,7)
	Mostrar (valor)
FinAlgoritmo
