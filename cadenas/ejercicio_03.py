################################################################################
#Función calcularTemperaturaMedia: Recibe dos números reales que representan 
#dos temperaturas y devuelve la temperatura media.
#Parámetros de entrada: dos temperaturas (real)
#Dato devuelto: La temperatura media (real)
################################################################################

#Funcion tmedia <- calcularTemperaturaMedia(temp1,temp2)
	#Definir tmedia Como Real;
	#tmedia<-(temp1+temp2)/2;
#FinFuncion

# ################################################################################
# Función calcular_temperatura_media: 
# Recibe dos números (float) y devuelve su promedio.
# ################################################################################

def calcular_temperatura_media(temp1, temp2):
    tmedia = (temp1 + temp2) / 2
    return tmedia

# ################################################################################
# Programa Principal
# Pide al usuario el número de días y calcula la media de cada uno
# ################################################################################

def principal():
    try:
        # Pedimos el número de días a procesar
        cantidad = int(input("¿Cuántas temperaturas se van a calcular?: "))
        
        # cantidad de iteraciones
        for i in range(cantidad):
            print(f"\n--- Día {i + 1} ---")
            
            # permitir decimales (float)
            tmin = float(input("Introduce temperatura mínima: "))
            tmax = float(input("Introduce temperatura máxima: "))
            
            # función y  el resultado
            media = calcular_temperatura_media(tmin, tmax)
            
            print(f"Temperatura media: {media}")
            
    except ValueError:
        print("¡Error! escribe solo números.")


if __name__ == "__main__":
    principal()

	#fin