# Programa que imprime números pares entre dos números

num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))

# Si num1 es impar, le sumo 1 para que sea par
if num1 % 2 == 1:
    num1 = num1 + 1

# Imprimir pares de 2 en 2
for num in range(num1, num2 + 1, 2):
    print(num, end=" ")