# Programa que verifica si un número es primo

import math

numero = int(input("Introduce un número para comprobar si es primo: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for num in range(2, int(math.sqrt(numero)) + 1):
        if numero % num == 0:
            es_primo = False
            break

if es_primo:
    print("Es primo")
else:
    print("No es primo")