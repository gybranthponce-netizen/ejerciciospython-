# Programa que calcula la suma y la media hasta que se ingrese 0

suma = 0
cont = 0

while True:
    num = int(input("Número (0 para salir): "))
    
    if num == 0:
        break
    
    suma = suma + num
    cont = cont + 1

if cont == 0:
    media = 0
else:
    media = suma / cont

print("Suma:", suma)
print("Media:", media)