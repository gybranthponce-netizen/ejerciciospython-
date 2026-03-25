precio = []
cantidad = []  # matriz: 4 sucursales x 5 artículos

# Leer precios
for indice_art in range(5):
    p = float(input(f"Ingrese Precio Artículo {indice_art + 1}: "))
    precio.append(p)

# Leer cantidades
for indice_sucursal in range(4):
    fila = []
    for indice_art in range(5):
        c = float(input(f"Ingrese Cant. de Artículo {indice_art + 1}, en Sucursal {indice_sucursal + 1}: "))
        fila.append(c)
    cantidad.append(fila)

# Cantidades totales por artículo
print("\nCantidades por artículos:")
for indice_art in range(5):
    suma = 0
    for indice_sucursal in range(4):
        suma = suma + cantidad[indice_sucursal][indice_art]
    print(f"Total artículo {indice_art + 1}: {suma}")

# Total de artículos en sucursal 2
articulos_sucursal2 = 0
for indice_art in range(5):
    articulos_sucursal2 = articulos_sucursal2 + cantidad[1][indice_art]

print(f"\nTotal Sucursal 2: {articulos_sucursal2}")

# Cantidad del artículo 3 en sucursal 1
print(f"Sucursal 1, Artículo 3: {cantidad[0][2]}")

# Recaudaciones
mayor_rec = 0
num_mayor = 0
total_empresa = 0

print("\nRecaudaciones por sucursal:")

for indice_sucursal in range(4):
    total_sucursal = 0
    
    for indice_art in range(5):
        total_sucursal = total_sucursal + (cantidad[indice_sucursal][indice_art] * precio[indice_art])
    
    print(f"Sucursal {indice_sucursal + 1}: {total_sucursal}")
    
    # Buscar mayor recaudación
    if total_sucursal > mayor_rec:
        mayor_rec = total_sucursal
        num_mayor = indice_sucursal + 1
    
    total_empresa = total_empresa + total_sucursal

# Resultados finales
print(f"\nRecaudación total de la empresa: {total_empresa}")
print(f"Sucursal de mayor recaudación: {num_mayor}")