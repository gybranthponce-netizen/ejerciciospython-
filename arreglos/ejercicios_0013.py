
nombre = []
kms = [] 

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

tam_conductores_max = 10

while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    
    if num_conductores <= tam_conductores_max:
        break
    else:
        print(f"Como máximo puedo guardar la información de {tam_conductores_max} conductores")

for indice_cond in range(num_conductores):
    nom = input(f"Nombre del conductor {indice_cond + 1}: ")
    nombre.append(nom)
    
    fila_kms = []
 
    for indice_dias in range(7):
        km = int(input(f"¿Cuántos km ha realizado el {dias[indice_dias]}?: "))
        fila_kms.append(km)
    
    fila_kms.append(0)
    
    kms.append(fila_kms)

for indice_cond in range(num_conductores):
    for indice_dias in range(7):
        kms[indice_cond][7] = kms[indice_cond][7] + kms[indice_cond][indice_dias]

# Mostrar resultados
print("\nKilómetros totales por conductor")
print("=================================")

for indice_cond in range(num_conductores):
    print(f"{nombre[indice_cond]} ha realizado {kms[indice_cond][7]} kms.")