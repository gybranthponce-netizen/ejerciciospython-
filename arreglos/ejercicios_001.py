import random

def cuadrado_cubo_vector():
    vector_numeros = [0] * 10

    for indice in range(10):
        vector_numeros[indice] = random.randint(1, 10)

    for indice in range(10):
        numero = vector_numeros[indice]
        print(numero, numero**2, numero**3)

cuadrado_cubo_vector()