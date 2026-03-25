dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nombre_mes = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

while True:
    mes = int(input("Introduce un mes (1-12): "))
    
    if mes >= 1 and mes <= 12:
        break
    else:
        print("Error: mes incorrecto.")

print(f"El mes de {nombre_mes[mes - 1]} tiene {dias[mes - 1]} días.")