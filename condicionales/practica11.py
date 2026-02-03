#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
#dimensiones de los lados de un triángulo. 
#El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = float(input("Introduce longitud lado A: "))
b = float(input("Introduce longitud lado B: "))
c = float(input("Introduce longitud lado C: "))

# Triángulo rectángulo (Pitágoras)
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("Triángulo rectángulo")

# Tipo según lados
if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print("Triángulo isósceles")
elif a == b and a == c:
    print("Triángulo equilátero")
else:
    print("Triángulo escaleno")
