matriz = []

num_filas = 5
num_cols = 15

for fila in range(num_filas):
    fila_datos = []
    for col in range(num_cols):
        
        if fila == 0 or fila == num_filas - 1 or col == 0 or col == num_cols - 1:
            fila_datos.append(1)
        else:
            fila_datos.append(0)
    
    matriz.append(fila_datos)

for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col], end=" ")
    print()