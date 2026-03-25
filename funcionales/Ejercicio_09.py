#Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#salida e intercambia sus valores si el segundo es mayor que el primero.
#Parámetros de entrada y salida: dos números

def intercambiar(n1, n2):
    return (n2, n1) if n1 < n2 else (n1, n2)

def calcular_mcd(n1, n2):
    n1, n2 = intercambiar(n1, n2)
    resto = n1 % n2
    return n2 if resto == 0 else calcular_mcd(n2, resto)

try:
    a = int(input("n1: "))
    b = int(input("n2: "))
    print(f"MCD: {calcular_mcd(a, b)}")
except:
    print("Error")
    