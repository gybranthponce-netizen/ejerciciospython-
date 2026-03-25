################################################################################
#Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.
################################################################################
#Análisis
#Leo dos cadenas. Tengo que ir comprobando todas las subcadenas de la primera 
#cadena que tengan la misma longitud que la segunda. Si alguna de estas subcadenas
# es igual a la segunda, la primera cadena contiene la segunda.
# Datos de entrada: Cadena de caracteres y subcadena a buscar.
# Información de salida: Mensaje indicadndo si la cadea contiene la subcadena o no.
# Variables:cad, subcad  (carácter), num_subcadenas,nsubc (entero), 
#			 indicador (lógico)
################################################################################

Proceso ContieneSubCadena
	Definir cad, subcad Como Caracter;
	Definir num_subcadenas,nsubc Como Entero;
	Definir indicador Como Logico;
	indicador<-Falso;
	Escribir Sin Saltar "Introduce una cadena:";
	Leer cad;
	Escribir Sin Saltar "Introduce una subcadena:";
	Leer subcad;
	num_subcadenas<- Longitud(cad)-Longitud(subcad)+1;
	Para nsubc<-0 hasta num_subcadenas-1 Hacer
		Si Subcadena(cad,nsubc,nsubc+Longitud(subcad)-1)=subcad Entonces
			indicador<-Verdadero;
		FinSi
	FinPara
	Si indicador Entonces
		Escribir "La cadena contiene la subcadena.";
	SiNo
		Escribir "La cadena no contiene la subcadena.";
	FinSi
FinProceso

# Programa que comprueba si una cadena contiene una subcadena

# Leer datos
cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

# Variable indicador
indicador = False

# Calcular número de posibles subcadenas
num_subcadenas = len(cad) - len(subcad) + 1

# Recorrer la cadena
for nsubc in range(num_subcadenas):
    # Obtener subcadena de la cadena principal
    parte = cad[nsubc:nsubc + len(subcad)]
    
    # Comparar
    if parte == subcad:
        indicador = True

# Mostrar resultado
if indicador:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena no contiene la subcadena.")
	

    frase = input('Ingresa una frase: ')
	palabra = input('Ingresa una palabra: ')

if palabra in frase:
	print(f´"{ palabra }"" se encuentra en "{frase}"´)
else:
	print(f´{ palabra } No se encuentra en #´)

