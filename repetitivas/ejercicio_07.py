# Programa que muestra la tabla de multiplicar

tabla = int(input("¿De qué número quieres ver la tabla?: "))

for num in range(1, 11):
    print(num, "*", tabla, "=", num * tabla)