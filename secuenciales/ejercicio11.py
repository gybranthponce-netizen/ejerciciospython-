#Pide al usuario dos números y muestra la "distancia" entre ellos 
#el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

def calcular_distancia():
    num1 = int(input("Dime el número 1: "))
    num2 = int(input("Dime el número 2: "))

    distancia = abs(num1 - num2)

    print("Distancia:", distancia)

calcular_distancia()