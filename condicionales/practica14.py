################################################################################
#lasociación de vinicultores tiene como política fijar un precio inicial 
#al kilo de uva, la cual se clasifica en tipos A y B,  y además en tamaños 1 y 2. 
#Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
#requiere determinar cuánto recibirá un productor por la uva que entrega en un 
#embarque considerando lo siguiente: 
#es de tipo A, se le cargan 20 céntimos al precio inicial cuando es 
#tamaño 1; y 30 céntimos si es de tamaño 2. 
#siesde tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos 
#cuando es de tamaño2. 
#realice unlgoritmo para determinar la ganancia obtenida.
precio = int(input("Introduce el precio inicial por kilo (céntimos): "))
kilos = int(input("Introduce los kilos vendidos: "))
tipo = input("Introduce el tipo de uva (A/B): ").upper()

if tipo != "A" and tipo != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la uva (1/2): ")

    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        if tipo == "A":
            if tamano == "1":
                precio += 20
            else:
                precio += 30
        else:
            if tamano == "1":
                precio -= 20
            else:
                precio -= 30

        total = precio * kilos
        print("La ganancia es", total / 100, "euros")

