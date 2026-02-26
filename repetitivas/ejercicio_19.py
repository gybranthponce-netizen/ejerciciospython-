opcion = 0

while opcion != 5:
    # Mostrar menú
    print("\nMenú de recomendaciones")
    print("1. Literatura")
    print("2. Cine")
    print("3. Música")
    print("4. Videojuegos")
    print("5. Salir")

    # Leer opción
    try:
        opcion = int(input("Elija una opción (1-5): "))
    except:
        opcion = 0

    # Procesar opción
    if opcion == 1:
        print("\nLecturas recomendables:")
        print("- Esperándolo a Tito y otros cuentos de fútbol")
        print("- El juego de Ender")
        print("- El sueño de los héroes")

    elif opcion == 2:
        print("\nPelículas recomendables:")
        print("- Matrix")
        print("- El último samurái")
        print("- Cars")

    elif opcion == 3:
        print("\nDiscos recomendables:")
        print("- Despedazado por mil partes")
        print("- Búfalo")
        print("- Gaia")

    elif opcion == 4:
        print("\nVideojuegos clásicos recomendables:")
        print("- Día del tentáculo")
        print("- Terminal Velocity")
        print("- Death Rally")

    elif opcion == 5:
        print("Gracias, REGRESA OTRA VEZ, CUANDO QUIERAS ")

    else:
        print("Opción no válida")

    input("\nPresione Enter para continuar...")