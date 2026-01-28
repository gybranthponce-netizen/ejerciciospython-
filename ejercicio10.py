#Un alumno desea saber cual será su calificación final en la materia de Algoritmos
#Dicha calificación se compone de los siguientes porcentajes:

def calcular_nota_final():
    parcial1 = float(input("Dime la nota del parcial 1: "))
    parcial2 = float(input("Dime la nota del parcial 2: "))
    parcial3 = float(input("Dime la nota del parcial 3: "))
    examen = float(input("Dime la nota del examen: "))
    trabajo = float(input("Dime la nota del trabajo: "))

    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
    nota_final = promedio_parciales * 0.55 + examen * 0.30 + trabajo * 0.15

    print("Nota final:", nota_final)

calcular_nota_final()