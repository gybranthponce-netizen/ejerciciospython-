temperatura = []

cant_dias = 5

for indice in range(cant_dias):
    temp_min = float(input(f"Día {indice + 1}. Temperatura mínima: "))
    temp_max = float(input(f"Día {indice + 1}. Temperatura máxima: "))
    
    temperatura.append([temp_min, temp_max])

print("\nTemperaturas medias")
print("===================")

for indice in range(cant_dias):
    media = (temperatura[indice][0] + temperatura[indice][1]) / 2
    print(f"Día {indice + 1}. Temperatura media: {media}")

temp_min_global = temperatura[0][0]

for indice in range(cant_dias):
    if temperatura[indice][0] < temp_min_global:
        temp_min_global = temperatura[indice][0]

print("\nDías con menos temperatura")
print("==========================")

for indice in range(cant_dias):
    if temperatura[indice][0] == temp_min_global:
        print(f"Día {indice + 1}")

print("\nDías con temperatura máxima")
print("===========================")

buscar_temp = float(input("Introduce una temperatura: "))
existe_temperatura = False

for indice in range(cant_dias):
    if temperatura[indice][1] == buscar_temp:
        print(f"Día {indice + 1}")
        existe_temperatura = True

if existe_temperatura == False:
    print("No hay ningún día con dicha temperatura.")