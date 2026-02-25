# Programa que muestra las tablas del 1 al 5

for tabla in range(1, 6):
    print("Tabla del", tabla)
    
    for num in range(1, 11):
        print(tabla, "*", num, "=", tabla * num)
    
    print()  # Línea en blanco para separar tablas