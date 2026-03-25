notas = []

tam_notas = 5

for indice in range(tam_notas):
    while True:
        nota = float(input(f"Introduce la nota {indice + 1}: "))
        
        # Validación con if
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            break
        else:
            print("Error: la nota debe estar entre 0 y 10")

nota_max = notas[0]
nota_min = notas[0]
suma = 0

for indice in range(tam_notas):
    suma = suma + notas[indice]
    
    if notas[indice] > nota_max:
        nota_max = notas[indice]
  
    if notas[indice] < nota_min:
        nota_min = notas[indice]

nota_media = suma / tam_notas

print("\nNotas:", end=" ")
for indice in range(tam_notas):
    print(notas[indice], end=" ")

print("\nNota media:", nota_media)
print("Nota máxima:", nota_max)
print("Nota mínima:", nota_min)