# Programa que calcula el sueldo semanal de N trabajadores
# registrando días trabajados y horas por cada día

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

horas_acum = 0

for trabajador in range(1, trabajadores + 1):
    horas_por_trabajador = 0
    
    dias = int(input("¿Cuántos días ha trabajado el trabajador " + str(trabajador) + "?: "))
    
    for dia in range(1, dias + 1):
        horas = int(input("¿Cuántas horas trabajó el día " + str(dia) + "?: "))
        horas_por_trabajador = horas_por_trabajador + horas
    
    sueldo = horas_por_trabajador * sueldo_por_hora
    print("El trabajador", trabajador, "tiene de sueldo", sueldo)
    
    horas_acum = horas_acum + horas_por_trabajador

total_pagado = horas_acum * sueldo_por_hora

print("El pago total a los", trabajadores, "trabajadores es:", total_pagado)

#fin