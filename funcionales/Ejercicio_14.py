#Procedimiento IncializarPila: Recibe un vector (pila) y su tamaño. 
#Recorre el vector e inicializa sus elementos a *. 
#El * representa que el elemento está vacío.
#Parámetros de entrada: Tamaño del vector
#Parámetros de entrada y salida: El vector (pila)

def ejecutar_pila():
    pila = []  
    tam_max = 10

    while True:
        print(f"\n--- PILA ACTUAL: {pila} ---")
        print("1. Añadir | 2. Sacar | 3. Tamaño | 4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            if len(pila) < tam_max:
                elem = input("Dato para añadir: ")
                pila.append(elem) # Equivale a AddPila
            else:
                print("¡Error! La pila está llena.")

        elif opcion == '2':
            if len(pila) > 0:
                
                sacado = pila.pop() 
                print(f"Sacaste: {sacado}")
            else:
                print("¡Error! La pila está vacía.")

        elif opcion == '3':
            print(f"Longitud actual: {len(pila)}")

        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

ejecutar_pila()
