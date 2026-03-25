
################################################################################
#Procedimiento centrar: Recibe una cadena y la imprime centrada en la pantalla.
#Suponemos que tenemos una pantalla de 80 caracteres de ancho. 
#Para centrar usamos la formula 40 - (Longitud(cad)/2)
#Parámetros de entrada: cadena a imprimir centrada

# ################################################################################
# Procedimiento centrar: Recibe una cadena y la imprime centrada.
# ################################################################################

def centrar(cad):
    #Calculamos  posición inicial (40 menos la mitad de la longitud)
    #int() para que el resultado sea un número entero
    espacios = int(40 - (len(cad) / 2))
    
    #Imprimimos  espacios en blanco  ciclo
    for i in range(espacios): 
        print(" ", end="") # el end="" evita que salte de línea
    
    #Imprimimos el texto
    print(cad)
    
    #Ahora el subrayado: primero los espacios
    for i in range(espacios):
        print(" ", end="")
        
    #símbolos "=" según el largo del texto
    for i in range(len(cad)):
        print("=", end="")
    
    #separar del siguiente mensaje
    print("")

# ################################################################################
# Proceso EscribirCentrado
# ################################################################################

def EscribirCentrado():
    mensaje1 = "Un mensaje al centro"
    centrar(mensaje1)
    
    mensaje2 = "segundo mensaje"
    centrar(mensaje2)

# función principal
EscribirCentrado()

#fin