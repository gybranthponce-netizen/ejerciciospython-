# Programa que calcula el ahorro acumulado en un año

ahorro_acum = 0.0

for mes in range(1, 13):
    cant_mensual = float(input("¿Cuánto ahorraste en el mes " + str(mes) + "?: "))
    
    ahorro_acum = ahorro_acum + cant_mensual
    
    print("En el mes", mes, "llevas ahorrado:", ahorro_acum)

print("Total ahorrado en el año:", ahorro_acum)