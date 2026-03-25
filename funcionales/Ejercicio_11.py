#Función EsBisiesto: Recibe un año y devuelve si es o no bisiesto
#Parámetros de entrada: año
#Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)

def es_bisiestro  
return(year % 4 = 0 Y NO (year % 100 = 0)) O year % 400 = 0r):def calcular_dia_juliano(d, m, a):
    
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if es_bisiesto(a):
        dias_mes[2] = 29
    return sum(dias_mes[:m]) + d

print("Cálculo de Día Juliano ")
dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

resultado = calcular_dia_juliano(dia, mes, anio)
print(f"El Día Juliano es: {resultado}")

