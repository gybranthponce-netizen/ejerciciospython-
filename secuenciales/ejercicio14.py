#Dado un número de dos cifras, diseñar un algoritmo que permita obtener el 
#número invertido. 

def calcular_decenas_unidades():
    num = int(input("Dime un número de dos cifras: "))

    decenas = num // 10
    unidades = num % 10

    print("Primera cifra (decenas):", decenas)
    print("Segunda cifra (unidades):", unidades)

calcular_decenas_unidades()
