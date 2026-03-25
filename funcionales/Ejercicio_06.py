#Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia y
#devuelve el área y el perímetro.
#Parámetros de entrada: radio (real)
#Parámetros de entrada y salida: área y perímetro (real)

radio = float(input("Introduce el radio: "))
import math 
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

