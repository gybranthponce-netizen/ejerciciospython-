#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
Definir car Como Caracter;
	Repetir
		Escribir "Introduce un carácter:";
		Leer car;
	Hasta que Longitud(car)=1;
	Mientras car<>" " Hacer
		Si Mayusculas(car)="A" o Mayusculas(car)="E" 
		 Mayusculas(car)="I" o Mayusculas(car)="O" o Mayusculas(car)="U" Entonces
			Escribir "VOCAL";
			Escribir "NO VOCAL";
			Escribir "Introduce un carácter:";
			Leer car;
		Hasta que Longitud(car)=1;