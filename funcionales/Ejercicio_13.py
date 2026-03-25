#Pocedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#salida e intercambia sus valores si el segundo es mayor que el primero.
#Parámetros de entrada y salida: dos números
def operar(n1, d1, n2, d2, operacion):
    
    """Realiza la operación matemática y devuelve la fracción simplificada."""
    if operacion == '1': # Suma: (a/b + c/d) = (ad + bc) / bd
        num_res = n1 * d2 + n2 * d1
        den_res = d1 * d2
    elif operacion == '2': # Resta: (a/b - c/d) = (ad - bc) / bd
        num_res = n1 * d2 - n2 * d1
        den_res = d1 * d2
    elif operacion == '3': # Multiplicación: (a/b * c/d) = (ac) / (bd)
        num_res = n1 * n2
        den_res = d1 * d2
    elif operacion == '4': # División: (a/b / c/d) = (ad) / (bc)
        num_res = n1 * d2
        den_res = d1 * n2
    mcd = math.gcd(num_res, den_res)
    return num_res // mcd, den_res // mcd

def mostrar_resultado(n, d):
    """Muestra la fracción de forma bonita."""
    if d == 1:
        print(f"\n> Resultado: {n}")
    else:
        print(f"\n> Resultado: {n}/{d}")
    print("-" * 20)

def ejecutar_programa():
    while True:
        print("\n--- CALCULADORA DE FRACCIONES ---")
        print("1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir | 5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '5':
            print("¡Adiós!")
            break
        
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida, intenta de nuevo.")
            continue

        print("\nIntroduce la primera fracción:")
        n1 = int(input("  Numerador: "))
        d1 = int(input("  Denominador: "))
        
        print("Introduce la segunda fracción:")
        n2 = int(input("  Numerador: "))
        d2 = int(input("  Denominador: "))

        if d1 == 0 or d2 == 0:
            print("\nError: El denominador no puede ser 0.")
            continue

        res_num, res_den = operar (n1, d1, n2, d2, opcion)
        mostrar_resultado(res_num, res_den)

def ejecutar_programa():
    while True:
ejecutar_programa()

