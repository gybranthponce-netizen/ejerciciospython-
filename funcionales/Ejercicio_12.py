#Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y 
#devuelve si la fecha es correcta o no.
#Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes
#Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto
#la fecha va a ser incorrecta.
#Parámetros de entrada: día, mes y año
#Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)
def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dias_del_mes(month, year):
    
    if month in [1, 3, 5, 7, 8, 10, 12]: return 31
    if month in [4, 6, 9, 11]: return 30
    if month == 2: return 29 if es_bisiesto(year) else 28
    return 0  # 

def validar_fecha(day, month, year):
    if day < 1 or day > dias_del_mes(month, year):
        return False
    return True
print(" Cálculo con Validación")

while True:
    d = int(input("Día: "))
    m = int(input("Mes: "))
    a = int(input("Año: "))
    
    if validar_fecha(d,m,a):
        break#
        else:print("Fecha no valida, intenta de nuevo.")

diaj =sum(dias_del_mes(mes,a)for mes in range(1,m)+d)
 print(f "El dia Juliano es: {diaj}")


