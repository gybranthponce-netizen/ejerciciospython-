# Programa: Quiniela de fútbol

# Definimos las estructuras
equipos = []     # matriz 15 x 2 (nombres)
resultados = []  # matriz 15 x 2 (goles)

num_equipos = 15

# Entrada de datos
for indice in range(num_equipos):
    print(f"\nPartido {indice + 1}")
    
    equipo1 = input("Introduce el nombre del equipo 1: ")
    equipo2 = input("Introduce el nombre del equipo 2: ")
    
    goles1 = int(input(f"Goles de {equipo1}: "))
    goles2 = int(input(f"Goles de {equipo2}: "))
    
    equipos.append([equipo1, equipo2])
    resultados.append([goles1, goles2])

# Mostrar quiniela
print("\nQUINIELA")
print("========")

for indice in range(num_equipos):
    eq1 = equipos[indice][0]
    eq2 = equipos[indice][1]
    
    g1 = resultados[indice][0]
    g2 = resultados[indice][1]
    
    # Determinar resultado
    if g1 > g2:
        signo = "1"
    elif g1 < g2:
        signo = "2"
    else:
        signo = "X"
    
    print(f"{eq1} - {eq2} -> {signo}")