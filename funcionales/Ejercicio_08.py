#Crear una función recursiva que permita calcular el factorial de un número. 
#Realiza un programa principal donde se lea un entero y se muestre el resultado 
#del factorial.

def calcular_factorial(num):
    if num == 0 or num == 1:
        return 1    
    else:
        return num * calcular_factorial(num - 1)
    try:
    numero = int(input("Introduce un número entero: "))

    if numero < 0:
            print("Lo siento, el factorial no existe para negativos")
        else:
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")

    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")
        