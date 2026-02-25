# ###############################################################
# Juego: Adivina el número secreto
# ###############################################################

import random

# 1.- Genero un numero aleatorio del 1 al 100
num_secreto = random.randint(1, 100)

# 2.- intentos = 10
intentos = 10

print("Adivina el número (del 1 al 100):")
num_ingresado = int(input())

# 4.- Mientras no acierte y queden intentos
while num_ingresado != num_secreto and intentos > 1:
    
    if num_secreto > num_ingresado:
        print("Muy bajo")
    else:
        print("Muy alto")
    
    intentos = intentos - 1
    print("Te quedan", intentos, "intentos")
    
    num_ingresado = int(input())

# 10 y 11.- Resultado final
if num_ingresado == num_secreto:
    print("¡Exacto! Adivinaste en", 11 - intentos, "intentos.")
else:
    print("Has perdido ups. El número era:", num_secreto)