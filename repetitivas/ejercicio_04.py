# Programa que cuenta positivos, negativos y ceros

cont_positivos = 0
cont_negativos = 0
cont_ceros = 0

cantidad_num = int(input("¿Cuántos números vas a introducir?: "))

for i in range(1, cantidad_num + 1):
    num = int(input("Número " + str(i) + ": "))
    
    if num > 0:
        cont_positivos = cont_positivos + 1
    elif num < 0:
        cont_negativos = cont_negativos + 1
    else:
        cont_ceros = cont_ceros + 1

print("Números positivos:", cont_positivos)
print("Números negativos:", cont_negativos)
print("Números iguales a 0:", cont_ceros)