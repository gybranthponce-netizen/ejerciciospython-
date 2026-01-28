#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados 
#Celsius.

def calcular_grados_celsius():
    fahrenheit = float(input("Introduce la temperatura en ºF: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("La temperatura es", celsius, "ºC.")

calcular_grados_celsius()

#Fin