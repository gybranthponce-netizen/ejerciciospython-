nombre = []
edad = []

tam_vector = 30
indice = 0

while True:
    nom = input("Dime el nombre de un alumno: ")
    
    nombre.append(nom)
    
    if nom != "*":
        ed = int(input("Dime su edad: "))
        edad.append(ed)
    else:
        edad.append(0) 
        break
    
    indice = indice + 1
    
    if indice == tam_vector:
        break

indice = 0
edad_max = edad[0]

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] > edad_max:
        edad_max = edad[indice]
    indice = indice + 1

indice = 0
print("\nAlumnos mayores de edad")
print("=======================")

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] >= 18:
        print(nombre[indice])
    indice = indice + 1

indice = 0
print("\nAlumnos mayores")
print("===============")

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] == edad_max:
        print(nombre[indice])
    indice = indice + 1