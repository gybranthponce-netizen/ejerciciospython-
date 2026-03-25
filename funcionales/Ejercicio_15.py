# Procedimiento IncializarCola: Recibe un vector (cola) y su tamaño. 
# Recorre el vector e inicializa sus elementos a *. 
# El * representa que el elemento está vacío.
#Parámetros de entrada: Tamaño del vector
#Parámetros de entrada y salida: El vector (cola)
# Realiza un programa principal que nos permita usar funciones para manipular colas.
ef programa_cola():

    cola = []
    size_max = 3

    while True:
        print(f"\nCola actual: {cola}")
        print("1. Añadir | 2. Sacar | 3. Longitud | 4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if len(cola) < size_max:
                elem = input("Dato para añadir: ")
                cola.append(elem) # Añade al final
            else:
                print("Error: La cola está llena")
        
        elif opcion == "2":
            if len(cola) > 0:
                # pop(0) saca el primero y desplaza el resto automáticamente
                print(f"Elemento sacado: {cola.pop(0)}")
            else:
                print("Error: La cola está vacía")
        
        elif opcion == "3":
            print(f"Logitud actual:{len(cola))}")

        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion incorrecta")

        programa_cola()
        

