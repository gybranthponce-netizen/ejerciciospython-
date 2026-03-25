def vector_inverso():
    vector1 = [""] * 5
    vector2 = [""] * 5

    for i in range(5):
        vector1[i] = input(f"Dame la cadena {i + 1}: ")

    j = 0
    for i in range(4, -1, -1):
        vector2[j] = vector1[i]
        j += 1

    for i in range(5):
        print(f"La cadena {i + 1}: {vector2[i]}")

vector_inverso()