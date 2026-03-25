# Crea una función EsMultiplo que reciba los dos
# y devuelva si el primero es múltiplo del segundo.
def EsMultiplo(n1, n2):
    if n2 == 0: 
        return False
    return n1 % n2 == 0

    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))

    if EsMultiplo(numero1, numero2):
        print(f"{numero1} es múltiplo de {numero2}")
    elif EsMultiplo(numero2, numero1):
        print(f"{numero2} es múltiplo de {numero1}")
    else:
        print("Ninguno es múltiplo del otro")

    except:
    print("Error: Por favor introduce solo números enteros.")
