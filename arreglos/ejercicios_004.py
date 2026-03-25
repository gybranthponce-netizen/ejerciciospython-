vector = []

tam_vector = 10
indice = 0

while True:
    num = int(input(f"Introduce un número en el vector. Número {indice + 1}: "))
    
    vector.append(num)
    indice = indice + 1
 
    if indice == tam_vector or num < 0:
        break

print("Elementos del vector:")

indice = 0

while indice < len(vector) and vector[indice] >= 0:
    print(vector[indice], end=" ")
    indice = indice + 1