vector1 = []
vector2 = []
vector3 = []

tam_vector = 5

for indice in range(tam_vector):
    num = int(input(f"Introduce el elemento {indice + 1} del vector1: "))
    vector1.append(num)

for indice in range(tam_vector):
    num = int(input(f"Introduce el elemento {indice + 1} del vector2: "))
    vector2.append(num)

for indice in range(tam_vector):
    resultado = vector1[indice] + vector2[indice]
    vector3.append(resultado)

print("La suma de los vectores es:")
for indice in range(tam_vector):
    print(vector3[indice], end=" ")