import random

vector = []

tam_vector = 10

for indice in range(tam_vector):
    num = random.randint(1, 10)
    vector.append(num)

print("Vector original:")
for i in range(tam_vector):
    print(vector[i], end=" ")

while True:
    cambios = 0
    
    for indice in range(tam_vector - 1):
        if vector[indice] > vector[indice + 1]:
            aux = vector[indice]
            vector[indice] = vector[indice + 1]
            vector[indice + 1] = aux
            cambios = cambios + 1
    
    if cambios == 0:
        break

print("\nVector ordenado:")
for i in range(tam_vector):
    print(vector[i], end=" ")