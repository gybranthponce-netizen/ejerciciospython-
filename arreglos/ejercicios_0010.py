matriz = []

num_filas = 5
num_cols = 5

for fila in range(num_filas):
    fila_datos = []
    for col in range(num_cols):
        num = int(input(f"Introduce el número de la fila {fila + 1} y columna {col + 1}: "))
        fila_datos.append(num)
    matriz.append(fila_datos)

for fila in range(num_filas):
    suma = 0
    for col in range(num_cols):
        suma = suma + matriz[fila][col]
    print(f"La suma de los elementos de la fila {fila + 1} es {suma}")

for col in range(num_cols):
    suma = 0
    for fila in range(num_filas):
        suma = suma + matriz[fila][col]
    print(f"La suma de los elementos de la columna {col + 1} es {suma}")