// Realizar una funci�n que reciba 4 n�meros y nos indique cuantos n�meros son
// mayores a 5.
Funcion cuatro_numeros <- mayor_que_cinco ( n1,n2,n3,n4 )
	cuatro_numeros= 0
	si n1 > 5 Entonces
		cuatro_numeros = cuatro_numeros +1
	FinSi
	si n2 > 5 Entonces
		cuatro_numeros = cuatro_numeros +1
	FinSi
	si n3 > 5 Entonces
		cuatro_numeros = cuatro_numeros+1
	FinSi
	si n4 > 5 Entonces
		cuatro_numeros = cuatro_numeros+1
	FinSi
Fin Funcion

Algoritmo Ejercicio4
	valor = mayor_que_cinco (11,7,8,13) 
	Mostrar (valor)
FinAlgoritmo
