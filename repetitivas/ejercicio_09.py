# Programa que calcula una potencia sin usar el operador **

base = float(input("Dame la base de la potencia: "))

# Validar que el exponente sea entero positivo
while True:
    exponente = int(input("Dame el exponente (entero positivo): "))
    if exponente >= 0:
        break
    else:
        print("ERROR: El exponente debe ser positivo")

potencia = 1

for i in range(exponente):
    potencia = potencia * base

print("Resultado de la potencia:", potencia)