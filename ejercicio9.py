#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
#desea saber cuanto deberá pagar finalmente por su compra.

def calcular_precio_final():
    precio = float(input("Dime el precio: "))

    precio_final = precio - (precio * 0.15)

    print("Precio final:", precio_final)

calcular_precio_final()

#fin