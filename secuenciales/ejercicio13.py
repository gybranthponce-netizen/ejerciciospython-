#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada 
#y su raíz cúbica.
#PSeInt no tiene ninguna función predefinida que permita calcular la raíz cúbica,
#¿cómo se puede calcular?

import math

def calcular_raices():
    num = int(input("Dime el número: "))

    raiz_cuadrada = math.sqrt(num)
    raiz_cubica = num ** (1/3)

    print("Raíz cuadrada:", raiz_cuadrada)
    print("Raíz cúbica:", raiz_cubica)

calcular_raices()