# Programa que calcula el sueldo semanal de N trabajadores
# y el total que paga la empresa

horas_acum = 0

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

for trabajador in range(1, trabajadores + 1):
    horas_por_semana = int(input("¿Cuántas horas ha trabajado el trabajador " + str(trabajador) + "?: "))
    
    sueldo = horas_por_semana * sueldo_por_hora
    print("El trabajador", trabajador, "tiene de sueldo", sueldo)
    
    horas_acum = horas_acum + horas_por_semana

total_pagado = horas_acum * sueldo_por_hora

print("El pago total a los", trabajadores, "trabajadores es:", total_pagado)