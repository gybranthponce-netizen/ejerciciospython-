#Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
#y calcula a cuantos segundos corresponde.
#Parámetros de entrada: hora, minutos y segundos
#Dato devuelto: Segundos totales


def calcular_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return h, m, s

def calcular_total(h, m, s):
    return (h * 3600) + (m * 60) + s

op = 0
while op != 3:
    print("\n1.Segundos 2.HMS 3.Salir")
    try:
        op = int(input("Opcion: "))
        if op == 1:
            h = int(input("H: "))
            m = int(input("M: "))
            s = int(input("S: "))
            print("Total seg:", calcular_total(h, m, s))
        elif op == 2:
            cant_seg = int(input("Segundos: "))
            h, m, s = calcular_hms(cant_seg)
            print(f"Resultado: {h}:{m}:{s}")
    except:
        print("Error: Pon un numero")
