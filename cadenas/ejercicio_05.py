################################################################################
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.
################################################################################
#Análisis
#Tengo que ir quedándome con las primeras letras de cada palabra (las voy 
#concatenando en una variable cadena).
#Me posiciono en la primera letra de la primera palabra, a continuación 
#voy buscando un espacio, recorriendo los posibles espacios que hay entre palabras,
# y quedándome con el primer carácter de la siguiente palabra.
# Datos de entrada: Frase
# Información de salida: Iniciales
# Variables: cad, iniciales (Caracter), posicion, cont (enteros)

# ###############################################################
# Si tenemos una cadena con nombre y apellidos, mostrar iniciales
# ###############################################################

# Pedir la cadena
cad = input("Introduce una cadena: ")

# Variables
iniciales = ""
posicion = 0

# Evitar espacios al inicio
while posicion < len(cad) and cad[posicion] == " ":
    posicion += 1

# Primera inicial (si hay texto)
if posicion < len(cad):
    iniciales += cad[posicion]

# Recorrer la cadena
while posicion < len(cad):
    if cad[posicion] == " ":
        # Saltar espacios
        while posicion < len(cad) and cad[posicion] == " ":
            posicion += 1
        # Agregar la siguiente inicial si existe
        if posicion < len(cad):
            iniciales += cad[posicion]
    posicion += 1

# Mostrar resultado en mayúsculas
print("Iniciales:", iniciales.upper())