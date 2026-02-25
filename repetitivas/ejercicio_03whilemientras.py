# Programa que calcula la suma y la media hasta introducir 0
# ###############################################################

# 1.- Inicializo variables
suma = 0
cont = 0

# 2.- Leer num
num = int(input("Número (0 para salir): "))

# 3.- Mientras num != 0
while num != 0:
    
    # 4.- Acumulo
    suma = suma + num
    
    # 5.- Contador
    cont = cont + 1
    
    # 6.- Leer num
    num = int(input("Número (0 para salir): "))

# 7 y 8.- Calcular media
if cont > 0:
    media = suma / cont
else:
    media = 0

# 9.- Mostrar resultados
print("Suma:", suma)
print("Media:", media)

#fin