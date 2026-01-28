#Dadas dos variables numéricas A y B, que el usuario debe teclear, 
#se pide realizar un algoritmo que intercambie los valores de ambas variables 
#y muestre cuanto valen al final las dos variables.

def intercambiar_variables():
    a = int(input("Introduce valor de la variable A: "))
    b = int(input("Introduce valor de la variable B: "))

    aux = a
    a = b
    b = aux

    print("Nuevo valor de A:", a)
    print("Nuevo valor de B:", b)

intercambiar_variables()