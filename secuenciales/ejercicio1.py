################################################################################
#Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
################################################################################
#Análisis
#Tenemos que pedir un nombre por teclado y luego escribir un mensaje de saludo
#Datos de entrada: nombre (Cadena)
#Variables: nombre (Cadena)
################################################################################
#Diseño
#Leer nombre
#Escribir mensaje de saludo
################################################################################

#Proceso Saludar
#Definir nombre Como Cadena;
#Escribir "Dime tu nombre:";
#Leer nombre;
#Escribir "Hola ",nombre;
#Fin

def saludar():
    nombre = input("Que tal Dime tu nombre: ")
    print("Hola", nombre)

saludar()

#fin