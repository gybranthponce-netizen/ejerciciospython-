
################################################################################
#Análisis
#Leo un cadena y dos caracteres, recorro la cadena, si encuentro un carácter 
#igual al primer carácter que he leído lo sustituyo por el segundo. Para ello voy 
#a ir copiando los caracteres de la cadena a otra cadena, cuando tenga que 
#sustituir un carácter por otro copiaré el segundo.
#Datos de entrada: Cadena de caracteres, el carácter a buscar y a reemplazar.
#Información de salida: Cadena con el carácter indicado cambiado por el segundo.
#Variables:cad, newcad, car_buscar, car_sustituir (carácter), posicion (entero)
################################################################################

# ###############################################################
# Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.
# ###############################################################

# Leer cadena
cad = input("Introduce una cadena: ")

# Validar carácter a buscar
while True:
    car_buscar = input("Introduce un caracter a buscar: ")
    if len(car_buscar) == 1:
        break
    print("Error: Debe ser un solo carácter.")

# Validar carácter a sustituir
while True:
    car_sustituir = input("Introduce un caracter para sustituir: ")
    if len(car_sustituir) == 1:
        break
    print("Error: Debe ser un solo carácter.")

# Procesar la cadena
newcad = ""

for posicion in range(len(cad)):
    if cad[posicion] == car_buscar:
        newcad += car_sustituir
    else:
        newcad += cad[posicion]

# Mostrar resultado
print("La cadena modificada es:", newcad)

#fin_del_proceso