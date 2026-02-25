# Programa que dice si un carácter es vocal
# Termina cuando se introduce un espacio

car = input("Introduce un carácter: ")

while car != " ":
    
    if len(car) == 1:
        if car.upper() == "A" or car.upper() == "E" or car.upper() == "I" or car.upper() == "O" or car.upper() == "U":
            print("VOCAL")
        else:
            print("NO VOCAL")
    else:
        print("Ingresa solo un carácter")
    
    car = input("Introduce un carácter: ")