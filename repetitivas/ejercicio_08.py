# Programa del intervalo (versión principiante)

suma_dentro = 0
cont_fuera = 0

lim_inf = int(input("Introduce el límite inferior: "))
lim_sup = int(input("Introduce el límite superior: "))

num = int(input("Introduce un número (0 para salir): "))

while num != 0:
    
    if num > lim_inf and num < lim_sup:
        suma_dentro = suma_dentro + num
    else:
        cont_fuera = cont_fuera + 1   # ERROR típico: aquí también cuenta los límites como fuera
    
    num = int(input("Introduce un número (0 para salir): "))

print("Suma dentro del intervalo:", suma_dentro)
print("Cantidad fuera del intervalo:", cont_fuera)
fin