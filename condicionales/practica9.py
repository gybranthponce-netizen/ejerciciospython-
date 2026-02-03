#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))
num3 = int(input("Dime el número 3: "))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print(numeros[0], numeros[1], numeros[2])
