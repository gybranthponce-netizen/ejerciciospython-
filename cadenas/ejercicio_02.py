################################################################################
#Función EsMultiplo: Recibe dos número e indica si el primero el múltiplo del 
#segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
#Parámetros de entrada: dos números
#Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo 
#del segundo, Falso en caso contrario.

# ################################################################################
# Función EsMultiplo: Recibe dos números e indica si el primero es múltiplo del 
# segundo. Para ello calcula el resto de la división; si es 0, es múltiplo.
# ################################################################################

def es_multiplo(num1, num2):
    # Verificamos si el residuo de la división es cero
    if num1 % num2 == 0:
        return True
    else:
        return False

# ################################################################################
# Programa principal: Pide dos números enteros al usuario y utiliza la función
# es_multiplo para determinar la relación entre ellos.
# ################################################################################

def calcular_multiplo():
    # Pedir los datos al usuario
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    
    # Llamada a la función y muestra de resultados
    if es_multiplo(numero1, numero2):
        print(f"{numero1} es múltiplo de {numero2}")
    else:
        print(f"{numero1} no es múltiplo de {numero2}")

# Ejecución del programa
if __name__ == "__main__":
    calcular_multiplo()

    #fin_del_processo