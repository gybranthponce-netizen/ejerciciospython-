# Programa que calcula horas trabajadas y sueldo semanal

horas_acum = 0

sueldo_por_hora = float(input("Introduce el sueldo por hora: "))

for dia in range(1, 7):
    horas = float(input("¿Cuántas horas trabajaste el día " + str(dia) + "?: "))
    horas_acum = horas_acum + horas

print("Horas trabajadas en la semana:", horas_acum)

sueldo_total = sueldo_por_hora * horas_acum
print("Sueldo semanal:", sueldo_total)