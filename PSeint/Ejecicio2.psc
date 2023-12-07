// Realizar una función que reciba 4 notas de exámenes finales y devuelva la
//cantidad de alumnos aprobaron la materia.
Funcion cantidad_alumnos<-cantidad_alumnos_probados ( nota1,nota2,nota3,nota4 )
	cantidad_alumnos= 0
	nota_promocion = 7
	si nota1 >= nota_promocion Entonces
		Mostrar ("La nota 1 es mayor a la nota de promocion")
		cantidad_alumnos = cantidad_alumnos +1
	FinSi
	si nota2 >= nota_promocion Entonces
		Mostrar ("La nota 2 es mayor a la nota de promocion")
	       cantidad_alumnos = cantidad_alumnos +1
	FinSi
	si nota3 >= nota_promocion Entonces
			Mostrar ("La nota 3 es mayor a la nota de promocion")
			cantidad_alumnos = cantidad_alumnos +1
	FinSi
	si nota4 >= nota_promocion Entonces
			Mostrar ("La nota 4 es mayor a la nota de promocion")
			cantidad_alumnos = cantidad_alumnos +1
	FinSi
Fin Funcion

Algoritmo cantidad_aprobado 
	valor =(cantidad_alumnos_probados(1,6,3,9))
	Mostrar (valo)
FinAlgoritmo
