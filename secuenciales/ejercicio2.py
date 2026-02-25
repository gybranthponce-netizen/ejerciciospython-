################################################################################
#Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################
#Análisis
#Tenemos que leer la base y la altura del triangulo y calcular el perí­metro y el 
#área
#Datos de entrada: base(real), altura(real)
#Información de salida: perímetro(real) y área(real)
#Variables: base, altura, perimetro y area (Real)
################################################################################
#Diseño
#Leer base y altura
#Calcular perí­metro(2*base + 2*altura)
#Calcular área (base * altura
#Mostrar perí­metro y área
################################################################################

#Proceso Rectangulo
#Definir base,altura,perimetro,area Como Real;
#Escribir "Introduce la base:";
#Leer base;
#Escribir "Introduce la altura:";
#Leer altura;
#perimetro <- 2 * base + 2 * altura;
#area <- base * altura;
#Escribir "El perí­metro es ",perimetro," y el área es ",area;
#Fin

def rectangulo():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))

    perimetro = 2 * base + 2 * altura
    area = base * altura

    print("El perímetro es", perimetro, "y el área es", area)

rectangulo()