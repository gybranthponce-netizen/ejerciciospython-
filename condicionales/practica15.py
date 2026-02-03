#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("¿Cuántos alumnos participan?: "))

if alumnos <= 0:
    print("El número de alumnos debe ser un valor positivo")
else:
    if alumnos >= 100:
        costo_por_alumno = 65
    elif alumnos >= 50:
        costo_por_alumno = 70
    elif alumnos >= 30:
        costo_por_alumno = 95
    else:
        costo_por_alumno = 4000 / alumnos

    costo_autobus = costo_por_alumno * alumnos

    print("El coste por alumno es", costo_por_alumno, "euros")
    print("El coste del autobús es", costo_autobus, "euros")
